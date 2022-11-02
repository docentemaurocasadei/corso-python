-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 02, 2022 alle 12:06
-- Versione del server: 10.4.14-MariaDB
-- Versione PHP: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `personale`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `timbrature`
--

CREATE TABLE `timbrature` (
  `id` bigint(20) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp(),
  `codice` varchar(10) NOT NULL,
  `nominativo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `timbrature`
--

INSERT INTO `timbrature` (`id`, `data`, `codice`, `nominativo`) VALUES
(2, '2022-10-31 11:11:39', 'cod001', 'Mario Rossi'),
(3, '2022-10-31 11:11:40', 'cod001', 'Mario Rossi'),
(4, '2022-10-31 11:11:41', 'cod001', 'Mario Rossi'),
(5, '2022-10-31 11:28:39', 'cod002', 'Giuseppe Verdi'),
(6, '2022-10-31 11:28:53', 'cod003', 'Silvia Santi'),
(7, '2022-10-31 11:29:03', 'cod004', 'Vanessa Angeli'),
(8, '2022-10-31 11:45:48', 'cod005', 'Martino Carli'),
(9, '2022-10-31 12:49:36', 'M1', 'Marco');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `timbrature`
--
ALTER TABLE `timbrature`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `timbrature`
--
ALTER TABLE `timbrature`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
