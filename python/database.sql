DROP DATABASE IF EXISTS asset_management;
CREATE DATABASE asset_management;
USE asset_management;

-- 用户表
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    role ENUM('admin', 'user') NOT NULL DEFAULT 'user',
    email VARCHAR(120),  -- 添加邮箱字段
    phone VARCHAR(20),   -- 添加电话字段
    department VARCHAR(50),  -- 添加部门字段
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 添加创建时间
    last_login DATETIME  -- 添加最后登录时间
);

-- 初始化管理员账号（使用明文密码）
INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin');

-- 电脑管理表
CREATE TABLE computers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id VARCHAR(50) NOT NULL,
    serial_number VARCHAR(100) NOT NULL UNIQUE,
    ip_address VARCHAR(15),
    mac_address VARCHAR(17),
    status ENUM('在用', '闲置', '维修', '报废') NOT NULL,
    manager VARCHAR(50) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 软件管理表
CREATE TABLE software (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    version VARCHAR(50) NOT NULL,
    status ENUM('在用', '闲置', '过期') NOT NULL,
    user TEXT NOT NULL,
    license_count INT NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY `uk_name_version` (name, version)
);

-- 其他物品管理表
CREATE TABLE other_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    hardware_name VARCHAR(100),  -- 硬件名
    software_name VARCHAR(100),  -- 软件名
    quantity INT NOT NULL DEFAULT 1,  -- 数量
    price DECIMAL(10,2),  -- 报价
    category VARCHAR(50),  -- 种别
    purpose TEXT,  -- 用途
    supplier VARCHAR(100),  -- 入手先
    purchase_date DATE,  -- 入手时间
    purchase_method VARCHAR(50),  -- 入手方式
    manager VARCHAR(50) NOT NULL,  -- 管理者
    location VARCHAR(100),  -- 管理场所
    expiry_date DATE,  -- 有效期限
    disposal_method VARCHAR(100),  -- 处理方法
    borrower VARCHAR(100),  -- 貸出先
    borrow_date DATE,  -- 貸出日
    return_date DATE,  -- 貸出期限
    confidentiality_level VARCHAR(20),  -- 機密级别
    status ENUM('在用', '闲置', '维修', '报废', '借出') NOT NULL,
    user VARCHAR(50) NOT NULL,
    start_date DATE,
    end_date DATE,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 设备管理表
CREATE TABLE devices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    company_id VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    status ENUM('在用', '闲置', '维修', '报废', '借出') NOT NULL,
    manager VARCHAR(50) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 操作日志表
CREATE TABLE operation_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    username VARCHAR(50) NOT NULL,
    module VARCHAR(50) NOT NULL,  -- 模块：电脑/软件/设备/其他物品/用户
    operation VARCHAR(20) NOT NULL,  -- 操作类型：添加/修改/删除
    target_id INT NOT NULL,  -- 操作对象ID
    target_name VARCHAR(100) NOT NULL,  -- 操作对象名称
    details TEXT,  -- 操作详情（JSON格式存储变更内容）
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
); 