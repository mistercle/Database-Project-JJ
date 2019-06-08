-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Province`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Province` (
  `provinceCd` VARCHAR(45) NOT NULL,
  `provinceNm` VARCHAR(45) NULL,
  PRIMARY KEY (`provinceCd`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`RunningArea`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`RunningArea` (
  `runningAreaCd` VARCHAR(45) NOT NULL,
  `RunningAreaNm` VARCHAR(45) NULL,
  `provinceCd` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`runningAreaCd`),
  CONSTRAINT `fk_RunningArea_Province1`
    FOREIGN KEY (`provinceCd`)
    REFERENCES `mydb`.`Province` (`provinceCd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Party`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Party` (
  `partyCd` VARCHAR(45) NOT NULL,
  `partyNm` VARCHAR(45) NULL,
  `partyNum` INT NULL,
  `partyLeaderCd` VARCHAR(45) NULL,
  `dateOfEstablish` VARCHAR(45) NULL,
  PRIMARY KEY (`partyCd`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Assemblyman`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Assemblyman` (
  `assemblymanCd` VARCHAR(45) NOT NULL,
  `empNm` VARCHAR(45) NULL COMMENT '국회의원 한글이름\n',
  `partyNm` VARCHAR(45) NOT NULL,
  `reeleGbnNm` VARCHAR(45) NULL,
  `origCd` VARCHAR(45) NULL,
  `hobbyNm` VARCHAR(45) NULL,
  PRIMARY KEY (`assemblymanCd`),
  CONSTRAINT `fk_Assemblyman_RunningArea1`
    FOREIGN KEY (`origCd`)
    REFERENCES `mydb`.`RunningArea` (`runningAreaCd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Assemblyman_Party1`
    FOREIGN KEY (`partyNm`)
    REFERENCES `mydb`.`Party` (`partyNm`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Comittee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Comittee` (
  `comitteeCd` VARCHAR(45) NOT NULL,
  `comitteeNm` VARCHAR(45) NULL,
  `chairmanCd` VARCHAR(45) NULL,
  PRIMARY KEY (`comitteeCd`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Assemblyman_has_Comittee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Assemblyman_has_Comittee` (
  `assemblymanCd` VARCHAR(45) NOT NULL,
  `comitteeCd` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`assemblymanCd`, `comitteeCd`),
  CONSTRAINT `fk_Assemblyman_has_Comittee_Assemblyman1`
    FOREIGN KEY (`assemblymanCd`)
    REFERENCES `mydb`.`Assemblyman` (`assemblymanCd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Assemblyman_has_Comittee_Comittee1`
    FOREIGN KEY (`comitteeCd`)
    REFERENCES `mydb`.`Comittee` (`comitteeCd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Proposal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Proposal` (
  `proposalCd` VARCHAR(45) NOT NULL,
  `proposalNm` VARCHAR(45) NULL,
  `proposerCd` VARCHAR(45) NULL,
  PRIMARY KEY (`proposalCd`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Assemblyman_has_Proposal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Assemblyman_has_Proposal` (
  `assemblymanCd` VARCHAR(45) NOT NULL,
  `proposalCd` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`assemblymanCd`, `proposalCd`),
  CONSTRAINT `fk_Assemblyman_has_Proposal_Assemblyman1`
    FOREIGN KEY (`assemblymanCd`)
    REFERENCES `mydb`.`Assemblyman` (`assemblymanCd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Assemblyman_has_Proposal_Proposal1`
    FOREIGN KEY (`proposalCd`)
    REFERENCES `mydb`.`Proposal` (`proposalCd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
