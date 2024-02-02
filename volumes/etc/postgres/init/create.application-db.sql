-- Создание базы данных, если она не существует
DO
$$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = 'oleg') THEN
        CREATE USER oleg WITH PASSWORD 'Zxcv7890';
    END IF;
END
$$;

CREATE DATABASE IF NOT EXISTS onec_cinfo;

\c onec_cinfo

-- Создание таблицы
CREATE TABLE IF NOT EXISTS message_data (
    sending_process_status BOOLEAN,
    need_rewrite BOOLEAN,
    message_type VARCHAR(32),
    processing_type VARCHAR(32) DEFAULT 'default',
    receiver_system VARCHAR(32) DEFAULT 'default',
    message_id VARCHAR(50) DEFAULT 'default',
    sender_system VARCHAR(32) DEFAULT 'default',
    data BYTEA,
    received BOOLEAN,
    send_time TIMESTAMP,
    arrival_time TIMESTAMP
);

-- Назначение привилегий для пользователя oleg на таблицу message_data
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE message_data TO oleg;




