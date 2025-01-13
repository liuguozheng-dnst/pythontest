-- 为users表添加新字段
ALTER TABLE users
ADD COLUMN email VARCHAR(120),
ADD COLUMN phone VARCHAR(20),
ADD COLUMN department VARCHAR(50),
ADD COLUMN create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN last_login DATETIME;

-- 更新现有管理员账号的密码
UPDATE users 
SET password = 'admin123'
WHERE username = 'admin'; 

-- 修改电脑表，添加新字段
ALTER TABLE computers
ADD COLUMN purchase_type ENUM('购买', '租赁') NOT NULL DEFAULT '购买' COMMENT '采购形式',
ADD COLUMN department VARCHAR(100) COMMENT '管理部门',
ADD COLUMN system_type VARCHAR(50) COMMENT '系统类型',
ADD COLUMN is_gspc BOOLEAN DEFAULT FALSE COMMENT '是否GSPC',
ADD COLUMN has_bigfix BOOLEAN DEFAULT FALSE COMMENT '是否安装Bigfix',
ADD COLUMN has_defender BOOLEAN DEFAULT FALSE COMMENT '是否安装Defender',
ADD COLUMN has_sccm BOOLEAN DEFAULT FALSE COMMENT '是否安装SCCM',
ADD COLUMN has_tpm2 BOOLEAN DEFAULT FALSE COMMENT '是否有TPM2.0',
ADD COLUMN usb_status VARCHAR(50) COMMENT 'USB开放状态',
ADD COLUMN purchase_company VARCHAR(100) COMMENT '采购会社',
ADD COLUMN start_date DATE COMMENT '开始日',
ADD COLUMN end_date DATE COMMENT '结束日'; 

-- 修改其他物品表的入手方式字段
ALTER TABLE other_items 
MODIFY COLUMN purchase_method ENUM('购买', '租赁', '租借') NOT NULL DEFAULT '购买' COMMENT '入手方式'; 

-- 修改设备表
ALTER TABLE devices
CHANGE COLUMN company_id asset_id VARCHAR(50) NOT NULL COMMENT '公司资产编号',
ADD COLUMN purchase_method ENUM('购买', '租赁', '租借') NOT NULL DEFAULT '购买' COMMENT '入手方式',
ADD COLUMN supplier VARCHAR(100) COMMENT '入手先',
ADD COLUMN remarks TEXT COMMENT '备考'; 

-- 修改软件表结构
ALTER TABLE software
MODIFY COLUMN user TEXT NOT NULL COMMENT '使用者',
ADD COLUMN total_users INT GENERATED ALWAYS AS (
    (LENGTH(user) - LENGTH(REPLACE(user, ',', '')) + 1)
) STORED COMMENT '总用户数',
ADD COLUMN available_count INT GENERATED ALWAYS AS (
    license_count - (LENGTH(user) - LENGTH(REPLACE(user, ',', '')) + 1)
) STORED COMMENT '可用数量'; 

-- 更新操作记录表，添加导入操作类型
ALTER TABLE operation_logs 
MODIFY COLUMN operation ENUM('添加', '修改', '删除', '导入') NOT NULL;

-- 添加索引以提高查询性能
CREATE INDEX idx_operation_logs_module ON operation_logs(module);
CREATE INDEX idx_operation_logs_operation ON operation_logs(operation);
CREATE INDEX idx_operation_logs_create_time ON operation_logs(create_time); 