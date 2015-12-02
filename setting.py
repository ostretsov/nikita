db_info = {
    'host' = '',
    'user' = '',
    'password' = '',
    'db' = '',
    'charset' = 'utf8',
    'cursorclass' = 'pymysql.cursors.DictCursor',
}

sql_template = 'SELECT `calldate` AS `calldate`, `dstchannel` AS `dstchannel`, ( SELECT COUNT( `disposition` ) FROM `asteriskcdrdb`.`cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `billsec` BETWEEN 40 AND 80 AND `disposition` = "ANSWERED" AND `calldate` <= "2015-11-24" ) AS `answered >=40 <=80`, ( SELECT COUNT( `disposition` ) FROM `asteriskcdrdb`.`cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `billsec` > 80 AND `disposition` = "ANSWERED" AND `calldate` <= "2015-11-24" ) AS `answered >80`, ( SELECT COUNT( `disposition` ) FROM `asteriskcdrdb`.`cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `billsec` BETWEEN 15 AND 39.9999 AND `disposition` = "ANSWERED" AND `calldate` <= "2015-11-24" ) AS `answered >=15 <40`, ( SELECT COUNT( `disposition` ) FROM `asteriskcdrdb`.`cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `disposition` = "NO ANSWER" AND `calldate` <= "2015-11-24" ) AS "NO ANSWER", ( SELECT COUNT( `disposition` ) FROM `asteriskcdrdb`.`cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `disposition` = "BUSY" AND `calldate` <= "2015-11-24" ) AS "BUSY", ( SELECT COUNT( `disposition` ) FROM `asteriskcdrdb`.`cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `disposition` = "FAILED" AND `calldate` <= "2015-11-24" ) AS "FAILED", ( SELECT COUNT( `disposition` ) FROM `asteriskcdrdb`.`cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `billsec` < 15 AND `disposition` = "ANSWERED" AND `calldate` <= "2015-11-24" ) AS `answered <15` FROM `asteriskcdrdb`.`cdr` AS `cdr` WHERE `calldate` >= "2015-11-23" AND `dstchannel` LIKE "SIP/4101%" AND `calldate` <= "2015-11-24"'
