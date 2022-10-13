-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema belt
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema belt
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belt` DEFAULT CHARACTER SET utf8 ;
USE `belt` ;

-- -----------------------------------------------------
-- Table `belt`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(250) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt`.`grados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt`.`grados` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `alumno` VARCHAR(45) NULL,
  `stack` VARCHAR(45) NULL,
  `fecha` DATE NULL,
  `calificacion` TINYINT(2) NULL,
  `cinturon` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_grados_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_grados_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `belt`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
