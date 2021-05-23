CREATE TABLE `Roles` (
  `role_id` int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `role_name` varchar(255),
  `role_desc` varchar(255)
);
CREATE TABLE `User` (
  `user_id` int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_name` varchar(255) NOT NULL UNIQUE,
  `user_email` varchar(255) NOT NULL,
  `user_address` varchar(255) NOT NULL,
  `user_mobile` varchar(10) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `pass_desc` varchar(255),
  `pass_type` varchar(255),
	`login_time` datetime NOT NULL,
  `login_ip` varchar(255) NOT NULL,
	`create_time` varchar(255) NOT NULL,
	`role_id`  int UNSIGNED NOT NULL,
	 FOREIGN KEY (role_id) REFERENCES Roles (role_id)
);

INSERT INTO Roles VALUES 
(null, 'moderator', 'cool'),
(null, 'admin', 'brilliant'),
(null, 'normal', 'soso');

INSERT INTO User VALUES 
(null, 'Jeff', '123@gmail.com', '@home', '0988787666', '123', 'nice password', 'admin', '2009-10-04 22:23:00', '192.168.1.1', '2009-10-04 22:23:00', '1'),
(null, '@x0mg', '999@gmail.com', '@school', '0912333456', '123', 'nice password', 'root', '2009-10-04 22:23:00', '192.168.2.3', '2009-10-04 22:23:00', '1')