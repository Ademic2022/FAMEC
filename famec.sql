-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: famec_db
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('your_revision_id');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `families`
--

DROP TABLE IF EXISTS `families`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `families` (
  `name` varchar(128) NOT NULL,
  `owner_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `families_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `families`
--

LOCK TABLES `families` WRITE;
/*!40000 ALTER TABLE `families` DISABLE KEYS */;
INSERT INTO `families` VALUES ('fatimah','a57294fd-cd64-4a06-9a01-842a1a539f0e','4b256934-0c9e-4676-9a3f-4eb822b445cd','2023-09-06 16:05:44','2023-09-06 16:05:44'),('James','8453cdd2-a156-447e-bc8b-fd2e9771d700','8b318e9b-30c4-4430-bc64-3bf9d8706958','2023-09-18 00:02:51','2023-09-18 00:02:51');
/*!40000 ALTER TABLE `families` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `sender_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `recipient_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` varchar(255) NOT NULL,
  `is_read` tinyint(1) DEFAULT NULL,
  `family_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `recipient_id` (`recipient_id`),
  KEY `family_id` (`family_id`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  CONSTRAINT `notifications_ibfk_2` FOREIGN KEY (`recipient_id`) REFERENCES `users` (`id`),
  CONSTRAINT `notifications_ibfk_3` FOREIGN KEY (`family_id`) REFERENCES `families` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES ('ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','a57294fd-cd64-4a06-9a01-842a1a539f0e','A new task \'William Assignment\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','00449ac1-4905-416d-84a7-72bf51e1db3a','2023-09-09 00:26:40','2023-09-09 00:26:40'),('a57294fd-cd64-4a06-9a01-842a1a539f0e','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'Bedroom Arrangment\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','065dfada-11e9-4a11-8dbf-dae0cdbb1f96','2023-09-06 18:42:45','2023-09-06 18:42:45'),('a57294fd-cd64-4a06-9a01-842a1a539f0e','43823a9e-fe3a-4e09-9e74-6809293515a7','A new task \'Bedroom Arrangment\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','19581be7-321e-4f4d-bbb1-b6cd68a1bf19','2023-09-06 18:42:45','2023-09-06 18:42:45'),('43823a9e-fe3a-4e09-9e74-6809293515a7','a57294fd-cd64-4a06-9a01-842a1a539f0e','A new task \'Bedroom  spaces\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','2bfa16e4-34b9-4b48-847f-c207f016ceef','2023-09-06 20:36:36','2023-09-06 20:36:36'),('ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'Bedroom \' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','2c90db3d-e40b-46f9-8512-e816e8269eca','2023-09-09 00:46:34','2023-09-09 00:46:34'),('a57294fd-cd64-4a06-9a01-842a1a539f0e','43823a9e-fe3a-4e09-9e74-6809293515a7','A new task \'Bedroom Arrangement\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','3a2a2711-79c6-4b1f-914c-08c6347dddc2','2023-09-11 21:38:34','2023-09-11 21:38:34'),('ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'William Assignment\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','43a4bb8d-50a3-4258-8433-4c39bd7e130e','2023-09-09 00:26:40','2023-09-09 00:26:40'),('ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','a57294fd-cd64-4a06-9a01-842a1a539f0e','A new task \'Bedroom \' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','6b8b8b65-92a4-4ea4-9ae7-4583b329a033','2023-09-09 00:46:34','2023-09-09 00:46:34'),('43823a9e-fe3a-4e09-9e74-6809293515a7','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'Bedroom  spaces\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','7bc04d61-3c77-46cc-862e-2b8e831d4a4b','2023-09-06 20:36:36','2023-09-06 20:36:36'),('a57294fd-cd64-4a06-9a01-842a1a539f0e','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'Bedroom Arrangement\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','882eee27-391c-411c-bdbf-5ac9442e28d0','2023-09-11 21:38:34','2023-09-11 21:38:34'),('ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','43823a9e-fe3a-4e09-9e74-6809293515a7','A new task \'Bedroom \' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','90cdc3fb-6ea2-4f06-aff6-8d8c0ce93db6','2023-09-09 00:46:34','2023-09-09 00:46:34'),('43823a9e-fe3a-4e09-9e74-6809293515a7','a57294fd-cd64-4a06-9a01-842a1a539f0e','A new task \'General Cleaning\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','970501be-146b-45c6-bea8-3cbde1852cc6','2023-09-09 00:40:27','2023-09-09 00:40:27'),('43823a9e-fe3a-4e09-9e74-6809293515a7','ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','A new task \'General Cleaning\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','a31a8baf-05c6-4a2c-9a18-2e70eceb076e','2023-09-09 00:40:27','2023-09-09 00:40:27'),('a57294fd-cd64-4a06-9a01-842a1a539f0e','ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','A new task \'Bedroom Arrangement\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','ad882b84-5189-496d-aea2-de18d01b5cb2','2023-09-11 21:38:34','2023-09-11 21:38:34'),('a57294fd-cd64-4a06-9a01-842a1a539f0e','44462223-ff08-45ba-b256-93aec3c5911c','A new task \'Bedroom Arrangement\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','b51867a4-6384-4bb8-81d0-a461279e2a1d','2023-09-11 21:38:34','2023-09-11 21:38:34'),('43823a9e-fe3a-4e09-9e74-6809293515a7','9912a299-220b-4bae-8d8a-02dc2d966189','A new task \'General Cleaning\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','c82cde64-f9cd-4cee-8c53-6e8b95e51e0b','2023-09-09 00:40:27','2023-09-09 00:40:27'),('ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','43823a9e-fe3a-4e09-9e74-6809293515a7','A new task \'William Assignment\' has been created in your family.',0,'4b256934-0c9e-4676-9a3f-4eb822b445cd','f05ec494-6cdb-4e3f-a968-548a163559b7','2023-09-09 00:26:40','2023-09-09 00:26:40');
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `title` varchar(255) NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `due_date` varchar(50) DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `user_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `family_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  KEY `family_id` (`family_id`),
  CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `tasks_ibfk_2` FOREIGN KEY (`family_id`) REFERENCES `families` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES ('Bedroom  spaces','describe task','2023-09-12',0,0,'43823a9e-fe3a-4e09-9e74-6809293515a7','4b256934-0c9e-4676-9a3f-4eb822b445cd','79adcf76-9236-4252-9488-d6fd5d487a94','2023-09-06 20:36:34','2023-09-11 17:04:02'),('William Assignment','Please someone help me fix this','2023-09-10',0,0,'ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','4b256934-0c9e-4676-9a3f-4eb822b445cd','977c353e-6b74-418e-8985-0107eb502d73','2023-09-09 00:26:40','2023-09-09 00:26:40'),('General Cleaning','Everyone should be around','2023-09-15',1,0,'43823a9e-fe3a-4e09-9e74-6809293515a7','4b256934-0c9e-4676-9a3f-4eb822b445cd','9c5e2fad-d3d8-4ef5-aade-769e730894cd','2023-09-09 00:40:27','2023-09-09 00:40:27'),('Bedroom Arrangement','additional descriptions...','2023-09-29',0,0,'a57294fd-cd64-4a06-9a01-842a1a539f0e','4b256934-0c9e-4676-9a3f-4eb822b445cd','a9198f73-9c5b-47e6-a23e-07df5098abb7','2023-09-11 21:38:33','2023-09-11 21:38:33'),('Bedroom ','i want to work on this ','2023-09-14',0,1,'ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','4b256934-0c9e-4676-9a3f-4eb822b445cd','b3f6999c-b87c-4579-9034-8b51c58a59b6','2023-09-09 00:46:34','2023-09-17 21:08:40');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `firstname` varchar(128) NOT NULL,
  `lastname` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `address` varchar(255) NOT NULL,
  `country` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `zipcode` int NOT NULL,
  `birthday` varchar(10) DEFAULT NULL,
  `family_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `profile_img` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `family_id` (`family_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`family_id`) REFERENCES `families` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('ademic','Michael','mike@gmail.com','25d55ad283aa400af464c76d713c07ad','ademic','something','Nigeria','Oyo State',45234,'2/12','4b256934-0c9e-4676-9a3f-4eb822b445cd','43823a9e-fe3a-4e09-9e74-6809293515a7','2023-09-06 16:33:57','2023-09-06 16:33:57','avatar.png'),('Richard','Milli','richie@gmail.com','25d55ad283aa400af464c76d713c07ad','richie','something','Nigeria','Oyo State',45234,'2/14','4b256934-0c9e-4676-9a3f-4eb822b445cd','44462223-ff08-45ba-b256-93aec3c5911c','2023-09-11 05:29:19','2023-09-11 05:29:19','avatar.png'),('James','Tochie','james@gmail.com','25d55ad283aa400af464c76d713c07ad','Tochie','something','Nigeria','Oyo State',45234,'6/14','8b318e9b-30c4-4430-bc64-3bf9d8706958','8453cdd2-a156-447e-bc8b-fd2e9771d700','2023-09-18 00:02:50','2023-09-18 00:02:50','avatar.png'),('Adeeyo','Michael','miked@gmail.com','25d55ad283aa400af464c76d713c07ad','iammelody','something','Nigeria','Oyo State',45234,'2/12','4b256934-0c9e-4676-9a3f-4eb822b445cd','9912a299-220b-4bae-8d8a-02dc2d966189','2023-09-06 18:29:00','2023-09-06 18:29:00','avatar.png'),('Fatimah','Hassan','fatimahhassan@gmail.com','25d55ad283aa400af464c76d713c07ad','kennyfatimah','something','Nigeria','Oyo State',45234,'3/14','4b256934-0c9e-4676-9a3f-4eb822b445cd','a57294fd-cd64-4a06-9a01-842a1a539f0e','2023-09-06 16:05:43','2023-09-06 16:05:43','af95be49.png'),('William','Lane','williamclane32@gmail.com','25d55ad283aa400af464c76d713c07ad','william','something','Nigeria','Oyo State',42209,'6/23','4b256934-0c9e-4676-9a3f-4eb822b445cd','ed9a391c-6d4c-4deb-9ad7-1ee27f9036ad','2023-09-09 00:22:01','2023-09-09 00:22:01','bcabd656.png');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-18 12:58:24
