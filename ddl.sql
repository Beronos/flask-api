-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2021 at 02:31 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `capstone_bookstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `authorID` int(11) NOT NULL,
  `FirstName` varchar(40) DEFAULT NULL,
  `LastName` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `author`
--

INSERT INTO `author` (`authorID`, `FirstName`, `LastName`) VALUES
(1, 'Dan', 'Brown'),
(2, 'Khaled', 'Hosseini'),
(3, 'Louisa', 'May Alcott'),
(5, 'Philip', 'Japikse'),
(6, 'Ismail', 'Kadare'),
(7, 'J.K', 'Rowling'),
(8, 'George', 'Orwell'),
(9, 'Fyodor', 'Dostoevsky'),
(10, 'newName', 'newLastName'),
(16, 'new authorafaa', 'ccc');

-- --------------------------------------------------------

--
-- Table structure for table `authorbook`
--

CREATE TABLE `authorbook` (
  `ab_id` int(11) NOT NULL,
  `bookISBN` int(11) NOT NULL,
  `authorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `authorbook`
--

INSERT INTO `authorbook` (`ab_id`, `bookISBN`, `authorID`) VALUES
(1, 1, 1),
(2, 2, 2),
(12, 2, 16),
(3, 3, 3),
(4, 4, 1),
(5, 5, 2),
(6, 6, 2),
(7, 10, 5),
(8, 25, 1),
(9, 35, 8),
(10, 43, 6),
(11, 44, 9);

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `ISBN` int(11) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `PublicationYear` varchar(4) NOT NULL,
  `Stock` smallint(11) NOT NULL,
  `Rating` decimal(2,1) DEFAULT NULL CHECK (`Rating` >= 1 and `Rating` <= 5),
  `Description` text NOT NULL,
  `Genre` varchar(30) NOT NULL,
  `IMGLocation` varchar(255) DEFAULT NULL
) ;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`ISBN`, `Title`, `PublicationYear`, `Stock`, `Rating`, `Description`, `Genre`, `IMGLocation`) VALUES
(1, 'The Da Vinci Code', '2003', 4, '3.9', 'The Da Vinci Code is a 2003 mystery thriller novel by Dan Brown. It is Brown\'s second novel to include the character Robert Langdon: the first was his 2000 novel Angels & Demons.', 'Mystery', 'the-da-vinci-code.jpg'),
(2, 'The Kite Runner', '2021', 1, '4.3', 'The Kite Runner is the first novel by Afghan-American author Khaled Hosseini. Published in 2003 by Riverhead Books, it tells the story of Amir, a young boy from the Wazir Akbar Khan district of Kabul.', 'Drama', 'kite-runner.jpg'),
(3, 'Little Women and Good Wives', '1868', 2, '4.1', 'Little Women is a coming of age novel written by American novelist, Louisa May Alcott which was originally published in two volumes in 1868 and 1869. Alcott wrote the book over several months at the request of her publisher.', 'Drama', 'little-women.jpg'),
(4, 'Angels and Demons', '2000', 1, '3.9', 'Angels & Demons is a 2000 bestselling mystery-thriller novel written by American author Dan Brown and published by Pocket Books and then by Corgi Books. The novel introduces the character Robert Langdon, who recurs as the protagonist of Brown\'s subsequent novels.', 'Mystery', 'angels-and-demons.jpg'),
(5, 'A Thousand Splendid Suns-2', '2007', 2, '4.4', 'A Thousand Splendid Suns is a 2007 novel by Afghan-American author Khaled Hosseini. It is his second, following his bestselling 2003 debut, The Kite Runner. Mariam is an illegitimate child, and suffers from both the stigma surrounding her birth along with the abuse she faces throughout her marriage. ', 'Novel', 'a-thousand-splendid-suns.jpg'),
(6, 'And the Mountains Echoed', '2013', 4, '4.0', 'And the Mountains Echoed is the third novel by Afghan-American author Khaled Hosseini. Published in 2013 by Riverhead Books, it deviates from Hosseini\'s style in his first two works through his choice to avoid focusing on any one character.', 'Novel', 'and-the-mountains-echoed.jpg'),
(10, 'Pro C# 8 with .NET Core 3', '2020', 2, '4.3', 'Includes new chapters on .NET Core, including ASP.NET Core web services, ASP.NET Core web applications with MVC, Entity Framework Core, and insight into the philosophy behind the new lightweight framework', 'Computer Science', 'c-sharp.jpg'),
(25, 'Inferno', '2013', 9, '3.9', 'Inferno is a 2013 mystery thriller novel by American author Dan Brown and the fourth book in his Robert Langdon series, following Angels & Demons, The Da Vinci Code and The Lost Symbol. The book was published on May 14, 2013, ten years after publication of The Da Vinci Code, by Doubleday', 'Mystery', 'inferno.jpg'),
(35, 'Nineteen Eighty-Four', '1949', 3, '4.5', 'Nineteen Eighty-Four: A Novel, often published as 1984, is a dystopian social science fiction novel by English novelist George Orwell. It was published on 8 June 1949 by Secker & Warburg as Orwell\'s ninth and final book completed in his lifetime.', 'Political fiction', '1984.png'),
(43, 'Kush e solli Doruntinen-2', '1980', 3, '3.9', 'Doruntine or The Ghost Rider is a novel by Albanian writer Ismail Kadare. It is based on the old Albanian legend of Constantin and Doruntine.', 'Mister', 'kush-e-solli-doruntinen.jpg'),
(44, 'Crime and Punishment', '1866', 1, '4.6', 'Crime and Punishment is a novel by the Russian author Fyodor Dostoevsky. It was first published in the literary journal The Russian Messenger in twelve monthly installments during 1866. It was later published in a single volume.', 'Drama', 'crime-and-punishment.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `commentID` int(11) NOT NULL,
  `content` text NOT NULL,
  `ISBN` int(11) NOT NULL,
  `username` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `loanID` int(11) NOT NULL,
  `ISBN` int(11) NOT NULL,
  `username` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`loanID`, `ISBN`, `username`) VALUES
(1, 6, 'betim'),
(2, 4, 'betim'),
(3, 25, 'enisa'),
(4, 2, 'driton');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserName` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `isAdmin` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserName`, `Password`, `isAdmin`) VALUES
('betim', 'e10adc3949ba59abbe56e057f20f883e', 0),
('driton', '427991a2b689c0e97ad550a62a38745a', 0),
('enisa', 'fdd1230973402f7d7c149ab2b965f6f1', 0),
('master', 'e10adc3949ba59abbe56e057f20f883e', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`authorID`);

--
-- Indexes for table `authorbook`
--
ALTER TABLE `authorbook`
  ADD PRIMARY KEY (`ab_id`),
  ADD UNIQUE KEY `bookISBN` (`bookISBN`,`authorID`),
  ADD KEY `authorID` (`authorID`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`ISBN`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`commentID`),
  ADD KEY `ISBN` (`ISBN`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `loan`
--
ALTER TABLE `loan`
  ADD PRIMARY KEY (`loanID`),
  ADD KEY `ISBN` (`ISBN`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserName`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `author`
--
ALTER TABLE `author`
  MODIFY `authorID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `authorbook`
--
ALTER TABLE `authorbook`
  MODIFY `ab_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `ISBN` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `commentID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan`
--
ALTER TABLE `loan`
  MODIFY `loanID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authorbook`
--
ALTER TABLE `authorbook`
  ADD CONSTRAINT `authorbook_ibfk_1` FOREIGN KEY (`bookISBN`) REFERENCES `book` (`ISBN`),
  ADD CONSTRAINT `authorbook_ibfk_2` FOREIGN KEY (`authorID`) REFERENCES `author` (`authorID`);

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `book` (`ISBN`),
  ADD CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`UserName`);

--
-- Constraints for table `loan`
--
ALTER TABLE `loan`
  ADD CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `book` (`ISBN`),
  ADD CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`UserName`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
