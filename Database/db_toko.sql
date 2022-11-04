-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 18, 2022 at 11:47 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_toko`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('1934c14e6025');

-- --------------------------------------------------------

--
-- Table structure for table `category_product`
--

CREATE TABLE `category_product` (
  `kd_cat` bigint(20) NOT NULL,
  `category` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category_product`
--

INSERT INTO `category_product` (`kd_cat`, `category`) VALUES
(1, 'Beras'),
(2, 'Minyak Goreng'),
(3, 'Micin'),
(4, 'Tepung '),
(14, 'Daging Halal');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `kd` bigint(20) NOT NULL,
  `nama` varchar(200) NOT NULL,
  `jumlah` bigint(20) NOT NULL,
  `harga` float NOT NULL,
  `kd_cat` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`kd`, `nama`, `jumlah`, `harga`, `kd_cat`) VALUES
(1, 'Asus Vivobook', 23, 25000000, 2),
(2, 'DELL', 65, 20000000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `todos`
--

CREATE TABLE `todos` (
  `id` bigint(20) NOT NULL,
  `todo` varchar(140) NOT NULL,
  `description` text DEFAULT NULL,
  `created_ad` datetime DEFAULT NULL,
  `updated_ad` datetime DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `token_acces` text DEFAULT NULL,
  `token_refresh` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `todos`
--

INSERT INTO `todos` (`id`, `todo`, `description`, `created_ad`, `updated_ad`, `user_id`, `token_acces`, `token_refresh`) VALUES
(1, 'Melakukan Login', 'User Melakukan Proses Login', '2022-08-12 02:03:13', '2022-08-12 02:03:13', 3, NULL, NULL),
(2, 'Melakukan Login', 'User Melakukan Proses Login dengan API', '2022-08-12 02:30:31', '2022-08-12 02:30:31', 1, NULL, NULL),
(3, 'Melakukan Login', 'User Melakukan Proses Login dengan API', '2022-08-12 02:44:39', '2022-08-12 02:44:39', 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `name` varchar(230) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(128) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `update_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `created_at`, `update_at`) VALUES
(1, 'Jidane Adi R', 'xyz@gmail.com', '123', '2022-08-05 04:04:58', '2022-08-05 04:07:58'),
(2, 'Sasa Weraa', 'abc@gmail.com', '123', '2022-08-12 04:43:31', '2022-08-12 04:43:31'),
(3, 'Andi Suryono Mangkurondo Limo', 'xyz@yahoo.co.id', '123', '2022-08-09 01:41:16', '2022-08-09 01:41:16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `category_product`
--
ALTER TABLE `category_product`
  ADD PRIMARY KEY (`kd_cat`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`kd`),
  ADD KEY `kd_cat` (`kd_cat`);

--
-- Indexes for table `todos`
--
ALTER TABLE `todos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `ix_todos_created_ad` (`created_ad`),
  ADD KEY `ix_todos_updated_ad` (`updated_ad`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_users_email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category_product`
--
ALTER TABLE `category_product`
  MODIFY `kd_cat` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `kd` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `todos`
--
ALTER TABLE `todos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`kd_cat`) REFERENCES `category_product` (`kd_cat`);

--
-- Constraints for table `todos`
--
ALTER TABLE `todos`
  ADD CONSTRAINT `todos_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
