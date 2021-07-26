use location;


CREATE TABLE IF NOT EXISTS `TL_PROVINCE` (
  `ProvinceID` INT(6) UNSIGNED NOT NULL PRIMARY KEY,
  `ProvinceName` VARCHAR(50)  NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `TL_PROVINCE` (`ProvinceID`, `ProvinceName`) VALUES
(1, '北京市'),
(2, '天津市'),
(3, '河北省'),
(4, '山西省'),
(5, '内蒙古自治区'),
(6, '辽宁省'),
(7, '吉林省'),
(8, '黑龙江省'),
(9, '上海市'),
(10, '江苏省'),
(11, '浙江省'),
(12, '安徽省'),
(13, '福建省'),
(14, '江西省'),
(15, '山东省'),
(16, '河南省'),
(17, '湖北省'),
(18, '湖南省'),
(19, '广东省'),
(20, '广西壮族自治区'),
(21, '海南省'),
(22, '重庆市'),
(23, '四川省'),
(24, '贵州省'),
(25, '云南省'),
(26, '西藏自治区'),
(27, '陕西省'),
(28, '甘肃省'),
(29, '青海省'),
(30, '宁夏回族自治区'),
(31, '新疆维吾尔自治区'),
(32, '香港特别行政区'),
(33, '澳门特别行政区'),
(34, '台湾省');
