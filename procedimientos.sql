-- ==============================================================================
-- ARCHIVO 2: PROCEDIMIENTOS ALMACENADOS OFICIALES DEL SISTEMA (bd_libros)
-- Contiene: Autenticación, CRUD Roles, CRUD Programas, CRUD Empleados,
--           Reportes Multinivel (S25-S26) y Dashboard Estadístico (S27)
-- ==============================================================================

USE bd_libros;
DELIMITER $$

-- ==============================================================================
-- MÓDULO 1: AUTENTICACIÓN (Sesión 19)
-- ==============================================================================
DROP PROCEDURE IF EXISTS sp_obtener_usuario_por_username $$
CREATE PROCEDURE sp_obtener_usuario_por_username(
    IN p_username VARCHAR(100)
)
BEGIN
    SELECT 
        u.id_usuario,
        u.username,
        CONCAT(u.apellidos, ', ', u.nombres) AS nombre_completo,
        r.nombre_rol AS rol,
        u.es_activo,
        u.password_hash
    FROM usuarios u
    INNER JOIN roles r ON u.rol_id = r.id_rol
    WHERE u.username = p_username
    LIMIT 1;
END $$

-- ==============================================================================
-- MÓDULO 2: MANTENIMIENTO CRUD DE ROLES
-- ==============================================================================
DROP PROCEDURE IF EXISTS sp_roles_listar $$
CREATE PROCEDURE sp_roles_listar()
BEGIN
    SELECT id_rol, nombre_rol, IFNULL(descripcion, '') AS descripcion, estado
    FROM roles
    ORDER BY id_rol ASC;
END $$

DROP PROCEDURE IF EXISTS sp_roles_buscar $$
CREATE PROCEDURE sp_roles_buscar(IN p_criterio VARCHAR(100))
BEGIN
    SET @termino = CONCAT('%', IFNULL(p_criterio, ''), '%');
    SELECT id_rol, nombre_rol, IFNULL(descripcion, '') AS descripcion, estado
    FROM roles
    WHERE nombre_rol LIKE @termino OR descripcion LIKE @termino
    ORDER BY id_rol ASC;
END $$

DROP PROCEDURE IF EXISTS sp_roles_obtener_por_id $$
CREATE PROCEDURE sp_roles_obtener_por_id(IN p_id_rol INT)
BEGIN
    SELECT id_rol, nombre_rol, IFNULL(descripcion, '') AS descripcion, estado
    FROM roles
    WHERE id_rol = p_id_rol;
END $$

DROP PROCEDURE IF EXISTS sp_roles_registrar $$
CREATE PROCEDURE sp_roles_registrar(
    IN p_nombre_rol VARCHAR(50),
    IN p_descripcion VARCHAR(150)
)
BEGIN
    IF EXISTS (SELECT 1 FROM roles WHERE UPPER(nombre_rol) = UPPER(TRIM(p_nombre_rol))) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ya existe un rol registrado con ese nombre.';
    END IF;

    INSERT INTO roles (nombre_rol, descripcion, estado)
    VALUES (TRIM(p_nombre_rol), TRIM(p_descripcion), 'Activo');
END $$

DROP PROCEDURE IF EXISTS sp_roles_actualizar $$
CREATE PROCEDURE sp_roles_actualizar(
    IN p_id_rol INT,
    IN p_nombre_rol VARCHAR(50),
    IN p_descripcion VARCHAR(150),
    IN p_estado VARCHAR(10)
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM roles 
        WHERE UPPER(nombre_rol) = UPPER(TRIM(p_nombre_rol)) AND id_rol != p_id_rol
    ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Otro rol ya utiliza ese nombre.';
    END IF;

    UPDATE roles
    SET nombre_rol = TRIM(p_nombre_rol),
        descripcion = TRIM(p_descripcion),
        estado = p_estado
    WHERE id_rol = p_id_rol;
END $$

DROP PROCEDURE IF EXISTS sp_roles_eliminar_logico $$
CREATE PROCEDURE sp_roles_eliminar_logico(IN p_id_rol INT)
BEGIN
    UPDATE roles SET estado = 'Inactivo' WHERE id_rol = p_id_rol;
END $$

DROP PROCEDURE IF EXISTS sp_roles_eliminar_fisico $$
CREATE PROCEDURE sp_roles_eliminar_fisico(IN p_id_rol INT)
BEGIN
    DELETE FROM roles WHERE id_rol = p_id_rol;
END $$

-- ==============================================================================
-- MÓDULO 3: MANTENIMIENTO CRUD DE PROGRAMAS DE ESTUDIO (Sesiones 20-21)
-- ==============================================================================
DROP PROCEDURE IF EXISTS sp_programas_listar $$
CREATE PROCEDURE sp_programas_listar()
BEGIN
    SELECT id_programa, codigo_programa, nombre_programa, estado, creado_en
    FROM programas_estudio
    ORDER BY id_programa DESC;
END $$

DROP PROCEDURE IF EXISTS sp_programas_buscar $$
CREATE PROCEDURE sp_programas_buscar(IN p_criterio VARCHAR(100))
BEGIN
    SET @termino = CONCAT('%', IFNULL(p_criterio, ''), '%');
    SELECT id_programa, codigo_programa, nombre_programa, estado, creado_en
    FROM programas_estudio
    WHERE codigo_programa LIKE @termino OR nombre_programa LIKE @termino
    ORDER BY id_programa DESC;
END $$

DROP PROCEDURE IF EXISTS sp_programas_obtener_por_id $$
CREATE PROCEDURE sp_programas_obtener_por_id(IN p_id_programa INT)
BEGIN
    SELECT id_programa, codigo_programa, nombre_programa, estado, creado_en
    FROM programas_estudio
    WHERE id_programa = p_id_programa;
END $$

DROP PROCEDURE IF EXISTS sp_programas_registrar $$
CREATE PROCEDURE sp_programas_registrar(
    IN p_codigo VARCHAR(10),
    IN p_nombre VARCHAR(120)
)
BEGIN
    IF EXISTS (SELECT 1 FROM programas_estudio WHERE UPPER(codigo_programa) = UPPER(TRIM(p_codigo))) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El código del programa de estudio ya está registrado.';
    END IF;

    INSERT INTO programas_estudio (codigo_programa, nombre_programa, estado)
    VALUES (UPPER(TRIM(p_codigo)), UPPER(TRIM(p_nombre)), 'Activo');
END $$

DROP PROCEDURE IF EXISTS sp_programas_actualizar $$
CREATE PROCEDURE sp_programas_actualizar(
    IN p_id_programa INT,
    IN p_codigo VARCHAR(10),
    IN p_nombre VARCHAR(120),
    IN p_estado VARCHAR(10)
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM programas_estudio 
        WHERE UPPER(codigo_programa) = UPPER(TRIM(p_codigo)) AND id_programa != p_id_programa
    ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El código ya pertenece a otro programa de estudio.';
    END IF;

    UPDATE programas_estudio
    SET codigo_programa = UPPER(TRIM(p_codigo)),
        nombre_programa = UPPER(TRIM(p_nombre)),
        estado = p_estado
    WHERE id_programa = p_id_programa;
END $$

DROP PROCEDURE IF EXISTS sp_programas_eliminar_logico $$
CREATE PROCEDURE sp_programas_eliminar_logico(IN p_id_programa INT)
BEGIN
    UPDATE programas_estudio SET estado = 'Inactivo' WHERE id_programa = p_id_programa;
END $$

DROP PROCEDURE IF EXISTS sp_programas_eliminar_fisico $$
CREATE PROCEDURE sp_programas_eliminar_fisico(IN p_id_programa INT)
BEGIN
    DELETE FROM programas_estudio WHERE id_programa = p_id_programa;
END $$

-- ==============================================================================
-- MÓDULO 4: MANTENIMIENTO CRUD TRANSACCIONAL DE EMPLEADOS (Sesiones 22-23)
-- ==============================================================================
DROP PROCEDURE IF EXISTS sp_empleados_listar $$
CREATE PROCEDURE sp_empleados_listar(IN p_criterio VARCHAR(100))
BEGIN
    SET @termino = CONCAT('%', IFNULL(p_criterio, ''), '%');
    SELECT 
        u.id_usuario,
        e.codigo_empleado,
        u.numero_documento,
        CONCAT(u.apellidos, ', ', u.nombres) AS nombre_completo,
        e.cargo,
        e.turno,
        r.nombre_rol AS rol,
        IF(u.es_activo = 1, 'Activo', 'Inactivo') AS estado
    FROM usuarios u
    INNER JOIN empleados e ON u.id_usuario = e.usuario_id
    INNER JOIN roles r ON u.rol_id = r.id_rol
    WHERE u.numero_documento LIKE @termino
       OR CONCAT(u.apellidos, ' ', u.nombres) LIKE @termino
       OR e.codigo_empleado LIKE @termino
    ORDER BY u.id_usuario DESC
    LIMIT 50;
END $$

DROP PROCEDURE IF EXISTS sp_empleado_obtener_por_id $$
CREATE PROCEDURE sp_empleado_obtener_por_id(IN p_id_usuario INT)
BEGIN
    SELECT 
        u.id_usuario,
        u.numero_documento,
        u.nombres,
        u.apellidos,
        u.username,
        u.rol_id,
        u.es_activo,
        e.codigo_empleado,
        e.cargo,
        e.turno
    FROM usuarios u
    INNER JOIN empleados e ON u.id_usuario = e.usuario_id
    WHERE u.id_usuario = p_id_usuario;
END $$

DROP PROCEDURE IF EXISTS sp_empleado_registrar $$
CREATE PROCEDURE sp_empleado_registrar(
    IN p_numero_documento VARCHAR(15),
    IN p_nombres VARCHAR(80),
    IN p_apellidos VARCHAR(80),
    IN p_username VARCHAR(100),
    IN p_password_hash VARCHAR(255),
    IN p_rol_id INT,
    IN p_codigo_empleado VARCHAR(20),
    IN p_cargo VARCHAR(80),
    IN p_turno VARCHAR(30),
    OUT p_id_generado INT
)
sp_bloque: BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

        IF EXISTS (SELECT 1 FROM usuarios WHERE numero_documento = p_numero_documento) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El DNI ingresado ya pertenece a otro usuario.';
        END IF;

        IF EXISTS (SELECT 1 FROM usuarios WHERE username = p_username) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El correo/usuario ya está registrado.';
        END IF;

        IF EXISTS (SELECT 1 FROM empleados WHERE codigo_empleado = p_codigo_empleado) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El código de empleado ya existe.';
        END IF;

        INSERT INTO usuarios (numero_documento, nombres, apellidos, username, password_hash, rol_id, es_activo)
        VALUES (p_numero_documento, p_nombres, p_apellidos, p_username, p_password_hash, p_rol_id, 1);

        SET p_id_generado = LAST_INSERT_ID();

        INSERT INTO empleados (usuario_id, codigo_empleado, cargo, turno)
        VALUES (p_id_generado, p_codigo_empleado, p_cargo, p_turno);

    COMMIT;
END sp_bloque $$

DROP PROCEDURE IF EXISTS sp_empleado_actualizar $$
CREATE PROCEDURE sp_empleado_actualizar(
    IN p_id_usuario INT,
    IN p_numero_documento VARCHAR(15),
    IN p_nombres VARCHAR(80),
    IN p_apellidos VARCHAR(80),
    IN p_username VARCHAR(100),
    IN p_password_hash VARCHAR(255),
    IN p_rol_id INT,
    IN p_codigo_empleado VARCHAR(20),
    IN p_cargo VARCHAR(80),
    IN p_turno VARCHAR(30)
)
sp_bloque: BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

        IF EXISTS (SELECT 1 FROM usuarios WHERE numero_documento = p_numero_documento AND id_usuario != p_id_usuario) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El documento ingresado pertenece a otro usuario registrado.';
        END IF;

        IF EXISTS (SELECT 1 FROM usuarios WHERE username = p_username AND id_usuario != p_id_usuario) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El correo o nombre de usuario ya está asignado a otra cuenta.';
        END IF;

        IF EXISTS (SELECT 1 FROM empleados WHERE codigo_empleado = p_codigo_empleado AND usuario_id != p_id_usuario) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El código corporativo de empleado ya pertenece a otro trabajador.';
        END IF;

        IF p_password_hash = '' THEN
            UPDATE usuarios SET
                numero_documento = p_numero_documento,
                nombres = p_nombres,
                apellidos = p_apellidos,
                username = p_username,
                rol_id = p_rol_id
            WHERE id_usuario = p_id_usuario;
        ELSE
            UPDATE usuarios SET
                numero_documento = p_numero_documento,
                nombres = p_nombres,
                apellidos = p_apellidos,
                username = p_username,
                password_hash = p_password_hash,
                rol_id = p_rol_id
            WHERE id_usuario = p_id_usuario;
        END IF;

        UPDATE empleados SET
            codigo_empleado = p_codigo_empleado,
            cargo = p_cargo,
            turno = p_turno
        WHERE usuario_id = p_id_usuario;

    COMMIT;
END sp_bloque $$

DROP PROCEDURE IF EXISTS sp_empleado_eliminar_logico $$
CREATE PROCEDURE sp_empleado_eliminar_logico(IN p_id_usuario INT)
BEGIN
    UPDATE usuarios SET es_activo = 0 WHERE id_usuario = p_id_usuario;
END $$

DROP PROCEDURE IF EXISTS sp_empleado_eliminar_fisico $$
CREATE PROCEDURE sp_empleado_eliminar_fisico(IN p_id_usuario INT)
sp_bloque: BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;
        DELETE FROM usuarios WHERE id_usuario = p_id_usuario;
    COMMIT;
END sp_bloque $$

-- ==============================================================================
-- MÓDULO 5: REPORTES MULTINIVEL (S25-S26) Y DASHBOARD ESTADÍSTICO (S27)
-- ==============================================================================
DROP PROCEDURE IF EXISTS sp_empleados_filtrar_multinivel $$
CREATE PROCEDURE sp_empleados_filtrar_multinivel(
    IN p_rol_id INT,
    IN p_turno VARCHAR(20),
    IN p_solo_activos INT,
    IN p_criterio VARCHAR(100)
)
BEGIN
    SELECT 
        u.id_usuario,
        e.codigo_empleado,
        u.numero_documento,
        CONCAT(u.apellidos, ', ', u.nombres) AS nombre_completo,
        e.cargo,
        e.turno,
        r.nombre_rol AS rol,
        IF(u.es_activo = 1, 'Activo', 'Inactivo') AS estado
    FROM usuarios u
    INNER JOIN empleados e ON u.id_usuario = e.usuario_id
    INNER JOIN roles r ON u.rol_id = r.id_rol
    WHERE (p_rol_id = 0 OR u.rol_id = p_rol_id)
      AND (p_turno = 'TODOS' OR e.turno = p_turno)
      AND (p_solo_activos = 0 OR u.es_activo = 1)
      AND (p_criterio = '' 
           OR u.numero_documento LIKE CONCAT('%', p_criterio, '%')
           OR CONCAT(u.apellidos, ' ', u.nombres) LIKE CONCAT('%', p_criterio, '%'))
    ORDER BY u.apellidos ASC;
END $$

DROP PROCEDURE IF EXISTS sp_dashboard_estadisticas_personal $$
CREATE PROCEDURE sp_dashboard_estadisticas_personal(
    IN p_rol_id INT,
    IN p_turno VARCHAR(20),
    IN p_solo_activos INT
)
BEGIN
    SELECT 
        COUNT(u.id_usuario) AS total_personal,
        IFNULL(SUM(CASE WHEN u.es_activo = 1 THEN 1 ELSE 0 END), 0) AS total_activos,
        IFNULL(SUM(CASE WHEN u.es_activo = 0 THEN 1 ELSE 0 END), 0) AS total_inactivos,
        IFNULL(SUM(CASE WHEN e.turno = 'Mañana'   THEN 1 ELSE 0 END), 0) AS turno_manana,
        IFNULL(SUM(CASE WHEN e.turno = 'Tarde'    THEN 1 ELSE 0 END), 0) AS turno_tarde,
        IFNULL(SUM(CASE WHEN e.turno = 'Noche'    THEN 1 ELSE 0 END), 0) AS turno_noche,
        IFNULL(SUM(CASE WHEN e.turno = 'Completo' THEN 1 ELSE 0 END), 0) AS turno_completo
    FROM usuarios u
    INNER JOIN empleados e ON u.id_usuario = e.usuario_id
    WHERE (p_rol_id = 0 OR u.rol_id = p_rol_id)
      AND (p_turno = 'TODOS' OR e.turno = p_turno)
      AND (p_solo_activos = 0 OR u.es_activo = 1);
END $$

DELIMITER ;