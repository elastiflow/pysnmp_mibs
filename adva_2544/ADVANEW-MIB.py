# SNMP MIB module (ADVANEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/ADVANEW-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:56 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(EnableState,
 OnOff,
 ServiceImpairment,
 TrapAlarmSeverity,
 advaMIB,
 config,
 neEventLogIdentityTranslation,
 neEventLogTimeStamp) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "EnableState",
    "OnOff",
    "ServiceImpairment",
    "TrapAlarmSeverity",
    "advaMIB",
    "config",
    "neEventLogIdentityTranslation",
    "neEventLogTimeStamp")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2",
    "snmpModules")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

advaNewMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 9999)
)
if mibBuilder.loadTexts:
    advaNewMIB.setRevisions(
        ("2007-10-04 00:00",
         "2007-09-24 00:00",
         "2007-05-07 00:00",
         "2006-11-15 00:00",
         "2006-06-14 00:00",
         "2006-05-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("bidirectional", 1),
          ("unidirectional", 2))
    )



class ApsHoldoffTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("e20ms", 2),
          ("e100ms", 3),
          ("e200ms", 4),
          ("e300ms", 5),
          ("e400ms", 6),
          ("e500ms", 7),
          ("e600ms", 8),
          ("e700ms", 9),
          ("e800ms", 10),
          ("e900ms", 11),
          ("e1000ms", 12),
          ("e1100ms", 13),
          ("e1200ms", 14),
          ("e1300ms", 15),
          ("e1400ms", 16),
          ("e1500ms", 17),
          ("e1600ms", 18),
          ("e1700ms", 19),
          ("e1800ms", 20),
          ("e1900ms", 21),
          ("e2000ms", 22),
          ("e2100ms", 23),
          ("e2200ms", 24),
          ("e2300ms", 25),
          ("e2400ms", 26),
          ("e2500ms", 27),
          ("e2600ms", 28),
          ("e2700ms", 29),
          ("e2800ms", 30),
          ("e2900ms", 31),
          ("e3000ms", 32),
          ("e3100ms", 33),
          ("e3200ms", 34),
          ("e3300ms", 35),
          ("e3400ms", 36),
          ("e3500ms", 37),
          ("e3600ms", 38),
          ("e3700ms", 39),
          ("e3800ms", 40),
          ("e3900ms", 41),
          ("e4000ms", 42),
          ("e4100ms", 43),
          ("e4200ms", 44),
          ("e4300ms", 45),
          ("e4400ms", 46),
          ("e4500ms", 47),
          ("e4600ms", 48),
          ("e4700ms", 49),
          ("e4800ms", 50),
          ("e4900ms", 51),
          ("e5000ms", 52),
          ("e5100ms", 53),
          ("e5200ms", 54),
          ("e5300ms", 55),
          ("e5400ms", 56),
          ("e5500ms", 57),
          ("e5600ms", 58),
          ("e5700ms", 59),
          ("e5800ms", 60),
          ("e5900ms", 61),
          ("e6000ms", 62),
          ("e6100ms", 63),
          ("e6200ms", 64),
          ("e6300ms", 65),
          ("e6400ms", 66),
          ("e6500ms", 67),
          ("e6600ms", 68),
          ("e6700ms", 69),
          ("e6800ms", 70),
          ("e6900ms", 71),
          ("e7000ms", 72),
          ("e7100ms", 73),
          ("e7200ms", 74),
          ("e7300ms", 75),
          ("e7400ms", 76),
          ("e7500ms", 77),
          ("e7600ms", 78),
          ("e7700ms", 79),
          ("e7800ms", 80),
          ("e7900ms", 81),
          ("e8000ms", 82),
          ("e8100ms", 83),
          ("e8200ms", 84),
          ("e8300ms", 85),
          ("e8400ms", 86),
          ("e8500ms", 87),
          ("e8600ms", 88),
          ("e8700ms", 89),
          ("e8800ms", 90),
          ("e8900ms", 91),
          ("e9000ms", 92),
          ("e9100ms", 93),
          ("e9200ms", 94),
          ("e9300ms", 95),
          ("e9400ms", 96),
          ("e9500ms", 97),
          ("e9600ms", 98),
          ("e9700ms", 99),
          ("e9800ms", 100),
          ("e9900ms", 101),
          ("e10000ms", 102))
    )



class ApsHoldoffTimeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNone", 1),
          ("capE20ms", 2),
          ("capE100ms", 3),
          ("capE200ms", 4),
          ("capE300ms", 5),
          ("capE400ms", 6),
          ("capE500ms", 7),
          ("capE600ms", 8),
          ("capE700ms", 9),
          ("capE800ms", 10),
          ("capE900ms", 11),
          ("capE1000ms", 12),
          ("capE1100ms", 13),
          ("capE1200ms", 14),
          ("capE1300ms", 15),
          ("capE1400ms", 16),
          ("capE1500ms", 17),
          ("capE1600ms", 18),
          ("capE1700ms", 19),
          ("capE1800ms", 20),
          ("capE1900ms", 21),
          ("capE2000ms", 22),
          ("capE2100ms", 23),
          ("capE2200ms", 24),
          ("capE2300ms", 25),
          ("capE2400ms", 26),
          ("capE2500ms", 27),
          ("capE2600ms", 28),
          ("capE2700ms", 29),
          ("capE2800ms", 30),
          ("capE2900ms", 31),
          ("capE3000ms", 32),
          ("capE3100ms", 33),
          ("capE3200ms", 34),
          ("capE3300ms", 35),
          ("capE3400ms", 36),
          ("capE3500ms", 37),
          ("capE3600ms", 38),
          ("capE3700ms", 39),
          ("capE3800ms", 40),
          ("capE3900ms", 41),
          ("capE4000ms", 42),
          ("capE4100ms", 43),
          ("capE4200ms", 44),
          ("capE4300ms", 45),
          ("capE4400ms", 46),
          ("capE4500ms", 47),
          ("capE4600ms", 48),
          ("capE4700ms", 49),
          ("capE4800ms", 50),
          ("capE4900ms", 51),
          ("capE5000ms", 52),
          ("capE5100ms", 53),
          ("capE5200ms", 54),
          ("capE5300ms", 55),
          ("capE5400ms", 56),
          ("capE5500ms", 57),
          ("capE5600ms", 58),
          ("capE5700ms", 59),
          ("capE5800ms", 60),
          ("capE5900ms", 61),
          ("capE6000ms", 62),
          ("capE6100ms", 63),
          ("capE6200ms", 64),
          ("capE6300ms", 65),
          ("capE6400ms", 66),
          ("capE6500ms", 67),
          ("capE6600ms", 68),
          ("capE6700ms", 69),
          ("capE6800ms", 70),
          ("capE6900ms", 71),
          ("capE7000ms", 72),
          ("capE7100ms", 73),
          ("capE7200ms", 74),
          ("capE7300ms", 75),
          ("capE7400ms", 76),
          ("capE7500ms", 77),
          ("capE7600ms", 78),
          ("capE7700ms", 79),
          ("capE7800ms", 80),
          ("capE7900ms", 81),
          ("capE8000ms", 82),
          ("capE8100ms", 83),
          ("capE8200ms", 84),
          ("capE8300ms", 85),
          ("capE8400ms", 86),
          ("capE8500ms", 87),
          ("capE8600ms", 88),
          ("capE8700ms", 89),
          ("capE8800ms", 90),
          ("capE8900ms", 91),
          ("capE9000ms", 92),
          ("capE9100ms", 93),
          ("capE9200ms", 94),
          ("capE9300ms", 95),
          ("capE9400ms", 96),
          ("capE9500ms", 97),
          ("capE9600ms", 98),
          ("capE9700ms", 99),
          ("capE9800ms", 100),
          ("capE9900ms", 101),
          ("capE10000ms", 102))
    )


class ApsRevertMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("nonrevertive", 1),
          ("revertive", 2))
    )



class ApsRevertModeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNonrevertive", 1),
          ("capRevertive", 2))
    )


class ApsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("line", 2),
          ("sncN", 3),
          ("sncI", 4),
          ("sncS", 5),
          ("eth", 6),
          ("phys", 7),
          ("sncNPM", 8),
          ("sncNTCM", 9),
          ("sncISM", 10),
          ("mux", 11),
          ("pcs", 12))
    )



class AssignmentState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("assigned", 1),
          ("unassigned", 2),
          ("notassignable", 3))
    )



class BootState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("complete", 1),
          ("started", 2),
          ("failed", 3))
    )



class ClockDataRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("transparent", 1),
          ("mb10", 2),
          ("mb125", 3),
          ("mb192", 4),
          ("mb155", 5),
          ("mb200", 6),
          ("mb266", 7),
          ("mb270", 8),
          ("mb326", 9),
          ("mb576", 10),
          ("mb622", 11),
          ("mb1062", 12),
          ("mb1244", 13),
          ("mb1250", 14),
          ("mb2125", 15),
          ("mb2488", 16),
          ("mb2500", 17),
          ("mb4250", 18),
          ("mb9953", 19),
          ("mb10312", 20),
          ("mb1062cl", 21),
          ("mb2125cl", 22),
          ("mb155als2", 23),
          ("mb622als2", 24),
          ("mb2488als2", 25),
          ("adaptive3R", 26),
          ("adaptive3ROddRates", 27),
          ("mb10518", 28),
          ("mb10709", 29),
          ("mb11095", 30),
          ("mb9953als2", 31),
          ("mb11317", 32))
    )



class CommandEqpt(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("install", 2),
          ("reboot", 3),
          ("active", 4),
          ("update", 5))
    )



class EnableStateCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capStateEnabled", 1),
          ("capStateDisabled", 2))
    )


class EntityClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("other", 1),
          ("unknown", 2),
          ("chassis", 3),
          ("backplane", 4),
          ("container", 5),
          ("powerSupply", 6),
          ("fan", 7),
          ("sensor", 8),
          ("module", 9),
          ("plug", 10),
          ("stack", 11),
          ("group", 12),
          ("clientPort", 13),
          ("networkPort", 14),
          ("virtualChannel", 15),
          ("connection", 16),
          ("vc4Container", 17),
          ("vc3sts1Container", 18),
          ("vc12vt15Container", 19),
          ("dcnChannel", 20),
          ("routerConfig", 21),
          ("environmentPort", 22),
          ("internalPort", 23),
          ("upgradePort", 24),
          ("midstagePort", 25),
          ("serialPort", 26),
          ("pppIpInterface", 27),
          ("lanIp", 28),
          ("vs1Container", 29),
          ("sts3cContainer", 30),
          ("payloadChannel", 31))
    )



class EntityIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EntityType(TextualConvention, Integer32):
    status = "current"


class EquipmentState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("equipped", 1),
          ("unequipped", 2))
    )



class EthDuplexMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ethHalfDuplex", 1),
          ("ethFullDuplex", 2))
    )



class EthDuplexModeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capEthHalfDuplex", 1),
          ("capEthFullDuplex", 2))
    )


class FileArea(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("activeArea", 1),
          ("standbyArea", 2),
          ("rDisk", 3))
    )



class FileType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("pgm", 1),
          ("dbs", 2),
          ("unknown", 3))
    )



class FspR7EquipmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              122,
              123,
              124)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("eqpSh1hu", 1),
          ("eqpSh1huDc", 2),
          ("eqpSh3hu", 3),
          ("eqpSh7hu", 4),
          ("eqpF2kSh5hu", 5),
          ("eqpF2kSh6hu", 6),
          ("eqpDcm", 7),
          ("eqpUnknown", 19),
          ("eqpNcu", 20),
          ("eqpNcutif", 21),
          ("eqpScu", 22),
          ("eqpScue", 23),
          ("eqpR6cu", 24),
          ("eqpPsu1huac", 25),
          ("eqpPsu7huac", 26),
          ("eqpPsu7hudc", 27),
          ("eqpFcu7hu", 28),
          ("eqp2clsmd", 29),
          ("eqp2absmc", 30),
          ("eqp2bsmd", 31),
          ("eqp1Gsmud", 32),
          ("eqp4gsmd", 33),
          ("eqp8gsmd", 34),
          ("eqp1csmuc", 35),
          ("eqp1csmuewc", 36),
          ("eqp4csmd", 37),
          ("eqp4csmud", 38),
          ("eqp4csmc", 39),
          ("eqpOsfm", 40),
          ("eqp1pm", 41),
          ("eqp2pm", 42),
          ("eqp40csmd", 43),
          ("eqpDcf", 44),
          ("eqpEdfas", 45),
          ("eqpEdfasgc", 46),
          ("eqpEdfadgc", 47),
          ("eqpRaman", 48),
          ("eqp4tcc2g5", 49),
          ("eqp4tcc2g5d", 50),
          ("eqp4tcc10gd", 51),
          ("eqp4tcc10gc", 52),
          ("eqpWcc10gd", 53),
          ("eqpWcc10gc", 54),
          ("eqpWcc2g71N", 55),
          ("eqpWcc2g7d", 56),
          ("eqp2tcm2g5", 57),
          ("eqp2tca2g5", 58),
          ("eqp8tca10gd", 59),
          ("eqp8tca10gc", 60),
          ("eqpWca10gd", 61),
          ("eqpWca10gc", 62),
          ("eqp4tca4gd", 63),
          ("eqp4tca4gc", 64),
          ("eqpwca2g5", 65),
          ("eqp4tca1g3d", 66),
          ("eqp4tca1g3c", 67),
          ("eqp8tce2g5d", 68),
          ("eqp8tce2g5c", 69),
          ("eqpWcelsd", 70),
          ("eqpWcelsc", 71),
          ("eqpVsm", 72),
          ("eqpRsmolm", 73),
          ("eqpRsmsf", 74),
          ("eqpOscm", 75),
          ("eqp2oscm", 76),
          ("eqpDrm", 77),
          ("eqpXfpG", 78),
          ("eqpsfpd", 79),
          ("eqpSfpc", 80),
          ("eqpSfpg", 81),
          ("eqpSfpe", 82),
          ("eqpSh1hudcm", 83),
          ("eqpCustomc", 84),
          ("eqpCustomd", 85),
          ("eqpPsu1hudc", 86),
          ("eqpWcc2g7c", 87),
          ("eqp1csmuEwD", 88),
          ("eqp1csmuG", 89),
          ("eqp3BsmC", 90),
          ("eqp2Tca2g5s", 91),
          ("eqp8Csmuc", 92),
          ("eqpEdfaDgcb", 93),
          ("eqpOscm2n", 94),
          ("eqp4Tcc10gtd", 95),
          ("eqp4Tca4g", 96),
          ("eqpDcg", 97),
          ("eqp2Tcm2g5d", 98),
          ("eqp2Tcm2g5c", 99),
          ("eqpWcm2g5d", 100),
          ("eqpWcm2g5c", 101),
          ("eqpEdfmSgc", 102),
          ("eqpF2kDemiV2", 103),
          ("eqpPsm", 104),
          ("eqpNcu2e", 105),
          ("eqp8TceGl2g5d", 106),
          ("eqp8TceGl2g5c", 107),
          ("eqpDcf1hu", 108),
          ("eqp10tcc10gtd", 109),
          ("eqp10tcc10gd", 110),
          ("eqp10tcc10gc", 111),
          ("eqp16csmSfd", 112),
          ("eqpOsfmSf", 113),
          ("eqp2clsmSfd", 114),
          ("eqp3bsmEwc", 115),
          ("eqpEdfaSgcb", 116),
          ("eqpEdfaDgcv", 117),
          ("eqpWcc10gtd", 118),
          ("eqp2csmuEwc", 119),
          ("eqpEroadmDc", 120),
          ("eqpScuS", 122),
          ("eqp4opcm", 123),
          ("eqpUtm", 124))
    )



class FspR7EquipmentTypeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capEqpSh1hu", 1),
          ("capEqpSh1huDc", 2),
          ("capEqpSh3hu", 3),
          ("capEqpSh7hu", 4),
          ("capEqpF2kSh5hu", 5),
          ("capEqpF2kSh6hu", 6),
          ("capEqpDcm", 7),
          ("capEqpUnknown", 19),
          ("capEqpNcu", 20),
          ("capEqpNcutif", 21),
          ("capEqpScu", 22),
          ("capEqpScue", 23),
          ("capEqpR6cu", 24),
          ("capEqpPsu1huac", 25),
          ("capEqpPsu7huac", 26),
          ("capEqpPsu7hudc", 27),
          ("capEqpFcu7hu", 28),
          ("capEqp2clsmd", 29),
          ("capEqp2absmc", 30),
          ("capEqp2bsmd", 31),
          ("capEqp1Gsmud", 32),
          ("capEqp4gsmd", 33),
          ("capEqp8gsmd", 34),
          ("capEqp1csmuc", 35),
          ("capEqp1csmuewc", 36),
          ("capEqp4csmd", 37),
          ("capEqp4csmud", 38),
          ("capEqp4csmc", 39),
          ("capEqpOsfm", 40),
          ("capEqp1pm", 41),
          ("capEqp2pm", 42),
          ("capEqp40csmd", 43),
          ("capEqpDcf", 44),
          ("capEqpEdfas", 45),
          ("capEqpEdfasgc", 46),
          ("capEqpEdfadgc", 47),
          ("capEqpRaman", 48),
          ("capEqp4tcc2g5", 49),
          ("capEqp4tcc2g5d", 50),
          ("capEqp4tcc10gd", 51),
          ("capEqp4tcc10gc", 52),
          ("capEqpWcc10gd", 53),
          ("capEqpWcc10gc", 54),
          ("capEqpWcc2g71N", 55),
          ("capEqpWcc2g7d", 56),
          ("capEqp2tcm2g5", 57),
          ("capEqp2tca2g5", 58),
          ("capEqp8tca10gd", 59),
          ("capEqp8tca10gc", 60),
          ("capEqpWca10gd", 61),
          ("capEqpWca10gc", 62),
          ("capEqp4tca4gd", 63),
          ("capEqp4tca4gc", 64),
          ("capEqpwca2g5", 65),
          ("capEqp4tca1g3d", 66),
          ("capEqp4tca1g3c", 67),
          ("capEqp8tce2g5d", 68),
          ("capEqp8tce2g5c", 69),
          ("capEqpWcelsd", 70),
          ("capEqpWcelsc", 71),
          ("capEqpVsm", 72),
          ("capEqpRsmolm", 73),
          ("capEqpRsmsf", 74),
          ("capEqpOscm", 75),
          ("capEqp2oscm", 76),
          ("capEqpDrm", 77),
          ("capEqpXfpG", 78),
          ("capEqpsfpd", 79),
          ("capEqpSfpc", 80),
          ("capEqpSfpg", 81),
          ("capEqpSfpe", 82),
          ("capEqpSh1hudcm", 83),
          ("capEqpCustomc", 84),
          ("capEqpCustomd", 85),
          ("capEqpPsu1hudc", 86),
          ("capEqpWcc2g7c", 87),
          ("capEqp1csmuEwD", 88),
          ("capEqp1csmuG", 89),
          ("capEqp3BsmC", 90),
          ("capEqp2Tca2g5s", 91),
          ("capEqp8Csmuc", 92),
          ("capEqpEdfaDgcb", 93),
          ("capEqpOscm2n", 94),
          ("capEqp4Tcc10gtd", 95),
          ("capEqp4Tca4g", 96),
          ("capEqpDcg", 97),
          ("capEqp2Tcm2g5d", 98),
          ("capEqp2Tcm2g5c", 99),
          ("capEqpWcm2g5d", 100),
          ("capEqpWcm2g5c", 101),
          ("capEqpEdfmSgc", 102),
          ("capEqpF2kDemiV2", 103),
          ("capEqpPsm", 104),
          ("capEqpNcu2e", 105),
          ("capEqp8TceGl2g5d", 106),
          ("capEqp8TceGl2g5c", 107),
          ("capEqpDcf1hu", 108),
          ("capEqp10tcc10gtd", 109),
          ("capEqp10tcc10gd", 110),
          ("capEqp10tcc10gc", 111),
          ("capEqp16csmSfd", 112),
          ("capEqpOsfmSf", 113),
          ("capEqp2clsmSfd", 114),
          ("capEqp3bsmEwc", 115),
          ("capEqpEdfaSgcb", 116),
          ("capEqpEdfaDgcv", 117),
          ("capEqpWcc10gtd", 118),
          ("capEqp2csmuEwc", 119),
          ("capEqpEroadmDc", 120),
          ("capEqpScuS", 122),
          ("capEqp4opcm", 123),
          ("capEqpUtm", 124))
    )


class FspR7FalseTrue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("false", 1),
          ("true", 2))
    )



class Grade(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("gradeA", 1),
          ("gradeB", 2),
          ("gradeGdps", 3),
          ("gradeC", 4))
    )



class LoopConfig(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("noLoop", 1),
          ("lineLoop", 2),
          ("inwardLoop", 3))
    )



class LoopConfigCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNoLoop", 1),
          ("capLineLoop", 2),
          ("capInwardLoop", 3))
    )


class OhTerminationLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("phys", 1),
          ("otnOtu", 2),
          ("otnOdu", 3),
          ("otnOpu", 4),
          ("sonetSection", 5),
          ("sonetLine", 6),
          ("sonetPath", 7),
          ("none", 8))
    )



class OhTerminationLevelCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capPhys", 1),
          ("capOtnOtu", 2),
          ("capOtnOdu", 3),
          ("capOtnOpu", 4),
          ("capSonetSection", 5),
          ("capSonetLine", 6),
          ("capSonetPath", 7),
          ("capNone", 8))
    )


class OtnPayloadType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7,
              8,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ifType10GbE", 3),
          ("ifTypeOc192", 4),
          ("ifTypeOc48", 5),
          ("ifTypeStm16", 6),
          ("ifTypeStm64", 7),
          ("ifType10GFC", 8),
          ("ifTypeF9953", 15),
          ("ifTypeF10312", 16),
          ("ifTypeF10518", 17),
          ("ifTypeF2488", 18))
    )



class OtnPayloadTypeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capIfType10GbE", 3),
          ("capIfTypeOc192", 4),
          ("capIfTypeOc48", 5),
          ("capIfTypeStm16", 6),
          ("capIfTypeStm64", 7),
          ("capIfType10GFC", 8),
          ("capIfTypeF9953", 15),
          ("capIfTypeF10312", 16),
          ("capIfTypeF10518", 17),
          ("capIfTypeF2488", 18))
    )


class OtnTcmLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6),
          ("disabled", 7))
    )



class OtnTcmLevelCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capTcm1", 1),
          ("capTcm2", 2),
          ("capTcm3", 3),
          ("capTcm4", 4),
          ("capTcm5", 5),
          ("capTcm6", 6),
          ("capDisabled", 7))
    )


class ProtectionMech(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("pathProtection", 1),
          ("channelCardProtection", 2),
          ("channelProtection", 3),
          ("versatileSwitchedProtection", 4))
    )



class ProtectionMechCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capPathProtection", 1),
          ("capChannelCardProtection", 2),
          ("capChannelProtection", 3),
          ("capVersatileSwitchedProtection", 4))
    )


class RestoreActivation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notRestore", 1),
          ("restoreFromStdBy", 2),
          ("restoreToFactory", 3),
          ("restoreFromEqpt", 4),
          ("acceptDatabase", 5))
    )



class ServiceAffecting(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("nsa", 1),
          ("sa", 2),
          ("saActivate", 3),
          ("saInstall", 4))
    )



class SonetSectSigDegThres(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ber10exp5", 1),
          ("ber10exp6", 2),
          ("ber10exp7", 3),
          ("ber10exp8", 4),
          ("ber10exp9", 5))
    )



class SonetSectSigDegThresCaps(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("capBer10exp5", 1),
          ("capBer10exp6", 2),
          ("capBer10exp7", 3),
          ("capBer10exp8", 4),
          ("capBer10exp9", 5))
    )



class SonetTimingSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("loopTiming", 1),
          ("internal", 2))
    )



class SonetTimingSourceCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capLoopTiming", 1),
          ("capInternal", 2))
    )


class SonetTraceForm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("form64CRLF", 1),
          ("form16CRC7", 2),
          ("form1Byte", 3))
    )



class SonetTraceFormCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capForm64CRLF", 1),
          ("capForm16CRC7", 2),
          ("capForm1Byte", 3))
    )


class SonetVcBundleAllocation(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class SonetVcBundleAllocationCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("vc1", 0),
          ("vc2", 1),
          ("vc3", 2),
          ("vc4", 3),
          ("vc5", 4),
          ("vc6", 5),
          ("vc7", 6),
          ("vc8", 7),
          ("vc9", 8),
          ("vc10", 9),
          ("vc11", 10),
          ("vc12", 11),
          ("vc13", 12),
          ("vc14", 13),
          ("vc15", 14),
          ("vc16", 15),
          ("vc17", 16),
          ("vc18", 17),
          ("vc19", 18),
          ("vc20", 19),
          ("vc21", 20),
          ("vc22", 21),
          ("vc23", 22),
          ("vc24", 23),
          ("vc25", 24),
          ("vc26", 25),
          ("vc27", 26),
          ("vc28", 27),
          ("vc29", 28),
          ("vc30", 29),
          ("vc31", 30),
          ("vc32", 31),
          ("vc33", 32),
          ("vc34", 33),
          ("vc35", 34),
          ("vc36", 35),
          ("vc37", 36),
          ("vc38", 37),
          ("vc39", 38),
          ("vc40", 39),
          ("vc41", 40),
          ("vc42", 41),
          ("vc43", 42),
          ("vc44", 43),
          ("vc45", 44),
          ("vc46", 45),
          ("vc47", 46),
          ("vc48", 47),
          ("vc49", 48),
          ("vc50", 49),
          ("vc51", 50),
          ("vc52", 51),
          ("vc53", 52),
          ("vc54", 53),
          ("vc55", 54),
          ("vc56", 55),
          ("vc57", 56),
          ("vc58", 57),
          ("vc59", 58),
          ("vc60", 59),
          ("vc61", 60),
          ("vc62", 61),
          ("vc63", 62),
          ("vc64", 63))
    )


class TimMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("disabled", 1),
          ("enableAisDisabled", 2))
    )



class TimModeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capDisabled", 1),
          ("capEnableAisDisabled", 2))
    )


class VirtualContainerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("vc4Type", 1),
          ("vc3Au4Type", 2),
          ("sts1", 3),
          ("sts3c", 4),
          ("vs1", 5),
          ("vs2c", 6))
    )



class VirtualContainerTypeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capVc4Type", 1),
          ("capVc3Au4Type", 2),
          ("capSts1", 3),
          ("capSts3c", 4),
          ("capVs1", 5),
          ("capVs2c", 6))
    )


# MIB Managed Objects in the order of their OIDs

_TransportStandards_ObjectIdentity = ObjectIdentity
transportStandards = _TransportStandards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4)
)
_Sonet_ObjectIdentity = ObjectIdentity
sonet = _Sonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1)
)
_SonetConfig_ObjectIdentity = ObjectIdentity
sonetConfig = _SonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1)
)
_SonetSectionConfigTable_Object = MibTable
sonetSectionConfigTable = _SonetSectionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonetSectionConfigTable.setStatus("current")
_SonetSectionConfigEntry_Object = MibTableRow
sonetSectionConfigEntry = _SonetSectionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1)
)
sonetSectionConfigEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionConfigEntry.setStatus("current")
_SonetSectionConfigTimingSource_Type = SonetTimingSource
_SonetSectionConfigTimingSource_Object = MibTableColumn
sonetSectionConfigTimingSource = _SonetSectionConfigTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 1),
    _SonetSectionConfigTimingSource_Type()
)
sonetSectionConfigTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTimingSource.setStatus("current")


class _SonetSectionConfigSignalDegradeThreshhold_Type(Unsigned32):
    """Custom type sonetSectionConfigSignalDegradeThreshhold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonetSectionConfigSignalDegradeThreshhold_Type.__name__ = "Unsigned32"
_SonetSectionConfigSignalDegradeThreshhold_Object = MibTableColumn
sonetSectionConfigSignalDegradeThreshhold = _SonetSectionConfigSignalDegradeThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 2),
    _SonetSectionConfigSignalDegradeThreshhold_Type()
)
sonetSectionConfigSignalDegradeThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradeThreshhold.setStatus("current")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradeThreshhold.setUnits("%")


class _SonetSectionConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type sonetSectionConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SonetSectionConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_SonetSectionConfigSignalDegradePeriod_Object = MibTableColumn
sonetSectionConfigSignalDegradePeriod = _SonetSectionConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 3),
    _SonetSectionConfigSignalDegradePeriod_Type()
)
sonetSectionConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    sonetSectionConfigSignalDegradePeriod.setUnits("s")
_SonetSectionConfigTraceForm_Type = SonetTraceForm
_SonetSectionConfigTraceForm_Object = MibTableColumn
sonetSectionConfigTraceForm = _SonetSectionConfigTraceForm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 4),
    _SonetSectionConfigTraceForm_Type()
)
sonetSectionConfigTraceForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTraceForm.setStatus("current")


class _SonetSectionConfigTraceExpected_Type(OctetString):
    """Custom type sonetSectionConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(62, 62),
    )
    fixed_length = 62


_SonetSectionConfigTraceExpected_Type.__name__ = "OctetString"
_SonetSectionConfigTraceExpected_Object = MibTableColumn
sonetSectionConfigTraceExpected = _SonetSectionConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 5),
    _SonetSectionConfigTraceExpected_Type()
)
sonetSectionConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTraceExpected.setStatus("current")


class _SonetSectionConfigTraceTransmit_Type(OctetString):
    """Custom type sonetSectionConfigTraceTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(62, 62),
    )
    fixed_length = 62


_SonetSectionConfigTraceTransmit_Type.__name__ = "OctetString"
_SonetSectionConfigTraceTransmit_Object = MibTableColumn
sonetSectionConfigTraceTransmit = _SonetSectionConfigTraceTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 6),
    _SonetSectionConfigTraceTransmit_Type()
)
sonetSectionConfigTraceTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTraceTransmit.setStatus("current")
_SonetSectionConfigTimMode_Type = TimMode
_SonetSectionConfigTimMode_Object = MibTableColumn
sonetSectionConfigTimMode = _SonetSectionConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 7),
    _SonetSectionConfigTimMode_Type()
)
sonetSectionConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionConfigTimMode.setStatus("current")
_SonetSectionDataTable_Object = MibTable
sonetSectionDataTable = _SonetSectionDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonetSectionDataTable.setStatus("current")
_SonetSectionDataEntry_Object = MibTableRow
sonetSectionDataEntry = _SonetSectionDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1)
)
sonetSectionDataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    sonetSectionDataEntry.setStatus("current")


class _SonetSectionDataTraceReceived_Type(OctetString):
    """Custom type sonetSectionDataTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(62, 62),
    )
    fixed_length = 62


_SonetSectionDataTraceReceived_Type.__name__ = "OctetString"
_SonetSectionDataTraceReceived_Object = MibTableColumn
sonetSectionDataTraceReceived = _SonetSectionDataTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1, 1),
    _SonetSectionDataTraceReceived_Type()
)
sonetSectionDataTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionDataTraceReceived.setStatus("current")
_Otn_ObjectIdentity = ObjectIdentity
otn = _Otn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2)
)
_OtuConfig_ObjectIdentity = ObjectIdentity
otuConfig = _OtuConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1)
)
_OtuSectionConfigTable_Object = MibTable
otuSectionConfigTable = _OtuSectionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    otuSectionConfigTable.setStatus("current")
_OtuSectionConfigEntry_Object = MibTableRow
otuSectionConfigEntry = _OtuSectionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1)
)
otuSectionConfigEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    otuSectionConfigEntry.setStatus("current")


class _OtuSectionConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type otuSectionConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OtuSectionConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OtuSectionConfigSignalDegradeThreshold_Object = MibTableColumn
otuSectionConfigSignalDegradeThreshold = _OtuSectionConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 1),
    _OtuSectionConfigSignalDegradeThreshold_Type()
)
otuSectionConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradeThreshold.setUnits("%")


class _OtuSectionConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type otuSectionConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OtuSectionConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OtuSectionConfigSignalDegradePeriod_Object = MibTableColumn
otuSectionConfigSignalDegradePeriod = _OtuSectionConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 2),
    _OtuSectionConfigSignalDegradePeriod_Type()
)
otuSectionConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    otuSectionConfigSignalDegradePeriod.setUnits("s")
_OtuSectionConfigPayload_Type = OtnPayloadType
_OtuSectionConfigPayload_Object = MibTableColumn
otuSectionConfigPayload = _OtuSectionConfigPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 3),
    _OtuSectionConfigPayload_Type()
)
otuSectionConfigPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigPayload.setStatus("current")
_OtuSectionConfigStuffing_Type = EnableState
_OtuSectionConfigStuffing_Object = MibTableColumn
otuSectionConfigStuffing = _OtuSectionConfigStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 4),
    _OtuSectionConfigStuffing_Type()
)
otuSectionConfigStuffing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigStuffing.setStatus("current")


class _OtuSectionConfigTraceExpected_Type(OctetString):
    """Custom type otuSectionConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OtuSectionConfigTraceExpected_Type.__name__ = "OctetString"
_OtuSectionConfigTraceExpected_Object = MibTableColumn
otuSectionConfigTraceExpected = _OtuSectionConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 5),
    _OtuSectionConfigTraceExpected_Type()
)
otuSectionConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceExpected.setStatus("current")


class _OtuSectionConfigTraceTransmitSapi_Type(OctetString):
    """Custom type otuSectionConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OtuSectionConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OtuSectionConfigTraceTransmitSapi_Object = MibTableColumn
otuSectionConfigTraceTransmitSapi = _OtuSectionConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 6),
    _OtuSectionConfigTraceTransmitSapi_Type()
)
otuSectionConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceTransmitSapi.setStatus("current")


class _OtuSectionConfigTraceTransmitDapi_Type(OctetString):
    """Custom type otuSectionConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OtuSectionConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OtuSectionConfigTraceTransmitDapi_Object = MibTableColumn
otuSectionConfigTraceTransmitDapi = _OtuSectionConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 7),
    _OtuSectionConfigTraceTransmitDapi_Type()
)
otuSectionConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceTransmitDapi.setStatus("current")


class _OtuSectionConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type otuSectionConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OtuSectionConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OtuSectionConfigTraceTransmitOpsp_Object = MibTableColumn
otuSectionConfigTraceTransmitOpsp = _OtuSectionConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 8),
    _OtuSectionConfigTraceTransmitOpsp_Type()
)
otuSectionConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTraceTransmitOpsp.setStatus("current")
_OtuSectionConfigTimMode_Type = TimMode
_OtuSectionConfigTimMode_Object = MibTableColumn
otuSectionConfigTimMode = _OtuSectionConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 9),
    _OtuSectionConfigTimMode_Type()
)
otuSectionConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuSectionConfigTimMode.setStatus("current")
_OtuSectionDataTable_Object = MibTable
otuSectionDataTable = _OtuSectionDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    otuSectionDataTable.setStatus("current")
_OtuSectionDataEntry_Object = MibTableRow
otuSectionDataEntry = _OtuSectionDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1)
)
otuSectionDataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    otuSectionDataEntry.setStatus("current")
_OtuSectionDataResultingTotalBitrate_Type = Unsigned32
_OtuSectionDataResultingTotalBitrate_Object = MibTableColumn
otuSectionDataResultingTotalBitrate = _OtuSectionDataResultingTotalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 1),
    _OtuSectionDataResultingTotalBitrate_Type()
)
otuSectionDataResultingTotalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataResultingTotalBitrate.setStatus("current")
if mibBuilder.loadTexts:
    otuSectionDataResultingTotalBitrate.setUnits("Mbit/s")


class _OtuSectionDataTraceReceivedSapi_Type(OctetString):
    """Custom type otuSectionDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OtuSectionDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OtuSectionDataTraceReceivedSapi_Object = MibTableColumn
otuSectionDataTraceReceivedSapi = _OtuSectionDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 2),
    _OtuSectionDataTraceReceivedSapi_Type()
)
otuSectionDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataTraceReceivedSapi.setStatus("current")


class _OtuSectionDataTraceReceivedDapi_Type(OctetString):
    """Custom type otuSectionDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OtuSectionDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OtuSectionDataTraceReceivedDapi_Object = MibTableColumn
otuSectionDataTraceReceivedDapi = _OtuSectionDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 3),
    _OtuSectionDataTraceReceivedDapi_Type()
)
otuSectionDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataTraceReceivedDapi.setStatus("current")


class _OtuSectionDataTraceReceivedOpsp_Type(OctetString):
    """Custom type otuSectionDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OtuSectionDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OtuSectionDataTraceReceivedOpsp_Object = MibTableColumn
otuSectionDataTraceReceivedOpsp = _OtuSectionDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 4),
    _OtuSectionDataTraceReceivedOpsp_Type()
)
otuSectionDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuSectionDataTraceReceivedOpsp.setStatus("current")
_OduConfig_ObjectIdentity = ObjectIdentity
oduConfig = _OduConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2)
)
_OduSectionConfigTable_Object = MibTable
oduSectionConfigTable = _OduSectionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oduSectionConfigTable.setStatus("current")
_OduSectionConfigEntry_Object = MibTableRow
oduSectionConfigEntry = _OduSectionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1)
)
oduSectionConfigEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduSectionConfigEntry.setStatus("current")


class _OduSectionConfigSignalDegradeThres_Type(Integer32):
    """Custom type oduSectionConfigSignalDegradeThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduSectionConfigSignalDegradeThres_Type.__name__ = "Integer32"
_OduSectionConfigSignalDegradeThres_Object = MibTableColumn
oduSectionConfigSignalDegradeThres = _OduSectionConfigSignalDegradeThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 1),
    _OduSectionConfigSignalDegradeThres_Type()
)
oduSectionConfigSignalDegradeThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradeThres.setStatus("current")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradeThres.setUnits("%")


class _OduSectionConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduSectionConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduSectionConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduSectionConfigSignalDegradePeriod_Object = MibTableColumn
oduSectionConfigSignalDegradePeriod = _OduSectionConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 2),
    _OduSectionConfigSignalDegradePeriod_Type()
)
oduSectionConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduSectionConfigSignalDegradePeriod.setUnits("s")


class _OduSectionConfigTraceExpected_Type(OctetString):
    """Custom type oduSectionConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduSectionConfigTraceExpected_Type.__name__ = "OctetString"
_OduSectionConfigTraceExpected_Object = MibTableColumn
oduSectionConfigTraceExpected = _OduSectionConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 3),
    _OduSectionConfigTraceExpected_Type()
)
oduSectionConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceExpected.setStatus("current")


class _OduSectionConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduSectionConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduSectionConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduSectionConfigTraceTransmitSapi_Object = MibTableColumn
oduSectionConfigTraceTransmitSapi = _OduSectionConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 4),
    _OduSectionConfigTraceTransmitSapi_Type()
)
oduSectionConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceTransmitSapi.setStatus("current")


class _OduSectionConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduSectionConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduSectionConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduSectionConfigTraceTransmitDapi_Object = MibTableColumn
oduSectionConfigTraceTransmitDapi = _OduSectionConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 5),
    _OduSectionConfigTraceTransmitDapi_Type()
)
oduSectionConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceTransmitDapi.setStatus("current")


class _OduSectionConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduSectionConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduSectionConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduSectionConfigTraceTransmitOpsp_Object = MibTableColumn
oduSectionConfigTraceTransmitOpsp = _OduSectionConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 6),
    _OduSectionConfigTraceTransmitOpsp_Type()
)
oduSectionConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTraceTransmitOpsp.setStatus("current")
_OduSectionConfigTimMode_Type = TimMode
_OduSectionConfigTimMode_Object = MibTableColumn
oduSectionConfigTimMode = _OduSectionConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 7),
    _OduSectionConfigTimMode_Type()
)
oduSectionConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduSectionConfigTimMode.setStatus("current")
_OduSectionDataTable_Object = MibTable
oduSectionDataTable = _OduSectionDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oduSectionDataTable.setStatus("current")
_OduSectionDataEntry_Object = MibTableRow
oduSectionDataEntry = _OduSectionDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1)
)
oduSectionDataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduSectionDataEntry.setStatus("current")


class _OduSectionDataTraceReceivedSapi_Type(OctetString):
    """Custom type oduSectionDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduSectionDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduSectionDataTraceReceivedSapi_Object = MibTableColumn
oduSectionDataTraceReceivedSapi = _OduSectionDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 1),
    _OduSectionDataTraceReceivedSapi_Type()
)
oduSectionDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduSectionDataTraceReceivedSapi.setStatus("current")


class _OduSectionDataTraceReceivedDapi_Type(OctetString):
    """Custom type oduSectionDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduSectionDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduSectionDataTraceReceivedDapi_Object = MibTableColumn
oduSectionDataTraceReceivedDapi = _OduSectionDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 2),
    _OduSectionDataTraceReceivedDapi_Type()
)
oduSectionDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduSectionDataTraceReceivedDapi.setStatus("current")


class _OduSectionDataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduSectionDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduSectionDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduSectionDataTraceReceivedOpsp_Object = MibTableColumn
oduSectionDataTraceReceivedOpsp = _OduSectionDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 3),
    _OduSectionDataTraceReceivedOpsp_Type()
)
oduSectionDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduSectionDataTraceReceivedOpsp.setStatus("current")
_OduTcmAConfigTable_Object = MibTable
oduTcmAConfigTable = _OduTcmAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    oduTcmAConfigTable.setStatus("current")
_OduTcmAConfigEntry_Object = MibTableRow
oduTcmAConfigEntry = _OduTcmAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1)
)
oduTcmAConfigEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmAConfigEntry.setStatus("current")


class _OduTcmAConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type oduTcmAConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduTcmAConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OduTcmAConfigSignalDegradeThreshold_Object = MibTableColumn
oduTcmAConfigSignalDegradeThreshold = _OduTcmAConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 1),
    _OduTcmAConfigSignalDegradeThreshold_Type()
)
oduTcmAConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradeThreshold.setUnits("%")


class _OduTcmAConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduTcmAConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduTcmAConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduTcmAConfigSignalDegradePeriod_Object = MibTableColumn
oduTcmAConfigSignalDegradePeriod = _OduTcmAConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 2),
    _OduTcmAConfigSignalDegradePeriod_Type()
)
oduTcmAConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmAConfigSignalDegradePeriod.setUnits("s")
_OduTcmAConfigTcmLevel_Type = OtnTcmLevel
_OduTcmAConfigTcmLevel_Object = MibTableColumn
oduTcmAConfigTcmLevel = _OduTcmAConfigTcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 3),
    _OduTcmAConfigTcmLevel_Type()
)
oduTcmAConfigTcmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTcmLevel.setStatus("current")


class _OduTcmAConfigTraceExpected_Type(OctetString):
    """Custom type oduTcmAConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmAConfigTraceExpected_Type.__name__ = "OctetString"
_OduTcmAConfigTraceExpected_Object = MibTableColumn
oduTcmAConfigTraceExpected = _OduTcmAConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 4),
    _OduTcmAConfigTraceExpected_Type()
)
oduTcmAConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceExpected.setStatus("current")


class _OduTcmAConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduTcmAConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmAConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduTcmAConfigTraceTransmitSapi_Object = MibTableColumn
oduTcmAConfigTraceTransmitSapi = _OduTcmAConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 5),
    _OduTcmAConfigTraceTransmitSapi_Type()
)
oduTcmAConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceTransmitSapi.setStatus("current")


class _OduTcmAConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduTcmAConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmAConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduTcmAConfigTraceTransmitDapi_Object = MibTableColumn
oduTcmAConfigTraceTransmitDapi = _OduTcmAConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 6),
    _OduTcmAConfigTraceTransmitDapi_Type()
)
oduTcmAConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceTransmitDapi.setStatus("current")


class _OduTcmAConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduTcmAConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduTcmAConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduTcmAConfigTraceTransmitOpsp_Object = MibTableColumn
oduTcmAConfigTraceTransmitOpsp = _OduTcmAConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 7),
    _OduTcmAConfigTraceTransmitOpsp_Type()
)
oduTcmAConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTraceTransmitOpsp.setStatus("current")
_OduTcmAConfigTimMode_Type = TimMode
_OduTcmAConfigTimMode_Object = MibTableColumn
oduTcmAConfigTimMode = _OduTcmAConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 8),
    _OduTcmAConfigTimMode_Type()
)
oduTcmAConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmAConfigTimMode.setStatus("current")
_OduTcmBConfigTable_Object = MibTable
oduTcmBConfigTable = _OduTcmBConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    oduTcmBConfigTable.setStatus("current")
_OduTcmBConfigEntry_Object = MibTableRow
oduTcmBConfigEntry = _OduTcmBConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1)
)
oduTcmBConfigEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmBConfigEntry.setStatus("current")


class _OduTcmBConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type oduTcmBConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduTcmBConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OduTcmBConfigSignalDegradeThreshold_Object = MibTableColumn
oduTcmBConfigSignalDegradeThreshold = _OduTcmBConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 1),
    _OduTcmBConfigSignalDegradeThreshold_Type()
)
oduTcmBConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradeThreshold.setUnits("%")


class _OduTcmBConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduTcmBConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduTcmBConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduTcmBConfigSignalDegradePeriod_Object = MibTableColumn
oduTcmBConfigSignalDegradePeriod = _OduTcmBConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 2),
    _OduTcmBConfigSignalDegradePeriod_Type()
)
oduTcmBConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmBConfigSignalDegradePeriod.setUnits("s")
_OduTcmBConfigTcmLevel_Type = OtnTcmLevel
_OduTcmBConfigTcmLevel_Object = MibTableColumn
oduTcmBConfigTcmLevel = _OduTcmBConfigTcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 3),
    _OduTcmBConfigTcmLevel_Type()
)
oduTcmBConfigTcmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTcmLevel.setStatus("current")


class _OduTcmBConfigTraceExpected_Type(OctetString):
    """Custom type oduTcmBConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmBConfigTraceExpected_Type.__name__ = "OctetString"
_OduTcmBConfigTraceExpected_Object = MibTableColumn
oduTcmBConfigTraceExpected = _OduTcmBConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 4),
    _OduTcmBConfigTraceExpected_Type()
)
oduTcmBConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceExpected.setStatus("current")


class _OduTcmBConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduTcmBConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmBConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduTcmBConfigTraceTransmitSapi_Object = MibTableColumn
oduTcmBConfigTraceTransmitSapi = _OduTcmBConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 5),
    _OduTcmBConfigTraceTransmitSapi_Type()
)
oduTcmBConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceTransmitSapi.setStatus("current")


class _OduTcmBConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduTcmBConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmBConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduTcmBConfigTraceTransmitDapi_Object = MibTableColumn
oduTcmBConfigTraceTransmitDapi = _OduTcmBConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 6),
    _OduTcmBConfigTraceTransmitDapi_Type()
)
oduTcmBConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceTransmitDapi.setStatus("current")


class _OduTcmBConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduTcmBConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduTcmBConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduTcmBConfigTraceTransmitOpsp_Object = MibTableColumn
oduTcmBConfigTraceTransmitOpsp = _OduTcmBConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 7),
    _OduTcmBConfigTraceTransmitOpsp_Type()
)
oduTcmBConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTraceTransmitOpsp.setStatus("current")
_OduTcmBConfigTimMode_Type = TimMode
_OduTcmBConfigTimMode_Object = MibTableColumn
oduTcmBConfigTimMode = _OduTcmBConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 8),
    _OduTcmBConfigTimMode_Type()
)
oduTcmBConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmBConfigTimMode.setStatus("current")
_OduTcmCConfigTable_Object = MibTable
oduTcmCConfigTable = _OduTcmCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5)
)
if mibBuilder.loadTexts:
    oduTcmCConfigTable.setStatus("current")
_OduTcmCConfigEntry_Object = MibTableRow
oduTcmCConfigEntry = _OduTcmCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1)
)
oduTcmCConfigEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmCConfigEntry.setStatus("current")


class _OduTcmCConfigSignalDegradeThreshold_Type(Integer32):
    """Custom type oduTcmCConfigSignalDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduTcmCConfigSignalDegradeThreshold_Type.__name__ = "Integer32"
_OduTcmCConfigSignalDegradeThreshold_Object = MibTableColumn
oduTcmCConfigSignalDegradeThreshold = _OduTcmCConfigSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 1),
    _OduTcmCConfigSignalDegradeThreshold_Type()
)
oduTcmCConfigSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradeThreshold.setUnits("%")


class _OduTcmCConfigSignalDegradePeriod_Type(Unsigned32):
    """Custom type oduTcmCConfigSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduTcmCConfigSignalDegradePeriod_Type.__name__ = "Unsigned32"
_OduTcmCConfigSignalDegradePeriod_Object = MibTableColumn
oduTcmCConfigSignalDegradePeriod = _OduTcmCConfigSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 2),
    _OduTcmCConfigSignalDegradePeriod_Type()
)
oduTcmCConfigSignalDegradePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    oduTcmCConfigSignalDegradePeriod.setUnits("s")
_OduTcmCConfigTcmLevel_Type = OtnTcmLevel
_OduTcmCConfigTcmLevel_Object = MibTableColumn
oduTcmCConfigTcmLevel = _OduTcmCConfigTcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 3),
    _OduTcmCConfigTcmLevel_Type()
)
oduTcmCConfigTcmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTcmLevel.setStatus("current")


class _OduTcmCConfigTraceExpected_Type(OctetString):
    """Custom type oduTcmCConfigTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmCConfigTraceExpected_Type.__name__ = "OctetString"
_OduTcmCConfigTraceExpected_Object = MibTableColumn
oduTcmCConfigTraceExpected = _OduTcmCConfigTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 4),
    _OduTcmCConfigTraceExpected_Type()
)
oduTcmCConfigTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceExpected.setStatus("current")


class _OduTcmCConfigTraceTransmitSapi_Type(OctetString):
    """Custom type oduTcmCConfigTraceTransmitSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmCConfigTraceTransmitSapi_Type.__name__ = "OctetString"
_OduTcmCConfigTraceTransmitSapi_Object = MibTableColumn
oduTcmCConfigTraceTransmitSapi = _OduTcmCConfigTraceTransmitSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 5),
    _OduTcmCConfigTraceTransmitSapi_Type()
)
oduTcmCConfigTraceTransmitSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceTransmitSapi.setStatus("current")


class _OduTcmCConfigTraceTransmitDapi_Type(OctetString):
    """Custom type oduTcmCConfigTraceTransmitDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmCConfigTraceTransmitDapi_Type.__name__ = "OctetString"
_OduTcmCConfigTraceTransmitDapi_Object = MibTableColumn
oduTcmCConfigTraceTransmitDapi = _OduTcmCConfigTraceTransmitDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 6),
    _OduTcmCConfigTraceTransmitDapi_Type()
)
oduTcmCConfigTraceTransmitDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceTransmitDapi.setStatus("current")


class _OduTcmCConfigTraceTransmitOpsp_Type(OctetString):
    """Custom type oduTcmCConfigTraceTransmitOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduTcmCConfigTraceTransmitOpsp_Type.__name__ = "OctetString"
_OduTcmCConfigTraceTransmitOpsp_Object = MibTableColumn
oduTcmCConfigTraceTransmitOpsp = _OduTcmCConfigTraceTransmitOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 7),
    _OduTcmCConfigTraceTransmitOpsp_Type()
)
oduTcmCConfigTraceTransmitOpsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTraceTransmitOpsp.setStatus("current")
_OduTcmCConfigTimMode_Type = TimMode
_OduTcmCConfigTimMode_Object = MibTableColumn
oduTcmCConfigTimMode = _OduTcmCConfigTimMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 8),
    _OduTcmCConfigTimMode_Type()
)
oduTcmCConfigTimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduTcmCConfigTimMode.setStatus("current")
_OduTcmADataTable_Object = MibTable
oduTcmADataTable = _OduTcmADataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6)
)
if mibBuilder.loadTexts:
    oduTcmADataTable.setStatus("current")
_OduTcmADataEntry_Object = MibTableRow
oduTcmADataEntry = _OduTcmADataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1)
)
oduTcmADataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmADataEntry.setStatus("current")


class _OduTcmADataTraceReceivedSapi_Type(OctetString):
    """Custom type oduTcmADataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmADataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduTcmADataTraceReceivedSapi_Object = MibTableColumn
oduTcmADataTraceReceivedSapi = _OduTcmADataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 1),
    _OduTcmADataTraceReceivedSapi_Type()
)
oduTcmADataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmADataTraceReceivedSapi.setStatus("current")


class _OduTcmADataTraceReceivedDapi_Type(OctetString):
    """Custom type oduTcmADataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmADataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduTcmADataTraceReceivedDapi_Object = MibTableColumn
oduTcmADataTraceReceivedDapi = _OduTcmADataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 2),
    _OduTcmADataTraceReceivedDapi_Type()
)
oduTcmADataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmADataTraceReceivedDapi.setStatus("current")


class _OduTcmADataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduTcmADataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduTcmADataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduTcmADataTraceReceivedOpsp_Object = MibTableColumn
oduTcmADataTraceReceivedOpsp = _OduTcmADataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 3),
    _OduTcmADataTraceReceivedOpsp_Type()
)
oduTcmADataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmADataTraceReceivedOpsp.setStatus("current")
_OduTcmBDataTable_Object = MibTable
oduTcmBDataTable = _OduTcmBDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7)
)
if mibBuilder.loadTexts:
    oduTcmBDataTable.setStatus("current")
_OduTcmBDataEntry_Object = MibTableRow
oduTcmBDataEntry = _OduTcmBDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1)
)
oduTcmBDataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmBDataEntry.setStatus("current")


class _OduTcmBDataTraceReceivedSapi_Type(OctetString):
    """Custom type oduTcmBDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmBDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduTcmBDataTraceReceivedSapi_Object = MibTableColumn
oduTcmBDataTraceReceivedSapi = _OduTcmBDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 1),
    _OduTcmBDataTraceReceivedSapi_Type()
)
oduTcmBDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmBDataTraceReceivedSapi.setStatus("current")


class _OduTcmBDataTraceReceivedDapi_Type(OctetString):
    """Custom type oduTcmBDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmBDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduTcmBDataTraceReceivedDapi_Object = MibTableColumn
oduTcmBDataTraceReceivedDapi = _OduTcmBDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 2),
    _OduTcmBDataTraceReceivedDapi_Type()
)
oduTcmBDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmBDataTraceReceivedDapi.setStatus("current")


class _OduTcmBDataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduTcmBDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduTcmBDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduTcmBDataTraceReceivedOpsp_Object = MibTableColumn
oduTcmBDataTraceReceivedOpsp = _OduTcmBDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 3),
    _OduTcmBDataTraceReceivedOpsp_Type()
)
oduTcmBDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmBDataTraceReceivedOpsp.setStatus("current")
_OduTcmCDataTable_Object = MibTable
oduTcmCDataTable = _OduTcmCDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8)
)
if mibBuilder.loadTexts:
    oduTcmCDataTable.setStatus("current")
_OduTcmCDataEntry_Object = MibTableRow
oduTcmCDataEntry = _OduTcmCDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1)
)
oduTcmCDataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    oduTcmCDataEntry.setStatus("current")


class _OduTcmCDataTraceReceivedSapi_Type(OctetString):
    """Custom type oduTcmCDataTraceReceivedSapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmCDataTraceReceivedSapi_Type.__name__ = "OctetString"
_OduTcmCDataTraceReceivedSapi_Object = MibTableColumn
oduTcmCDataTraceReceivedSapi = _OduTcmCDataTraceReceivedSapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 1),
    _OduTcmCDataTraceReceivedSapi_Type()
)
oduTcmCDataTraceReceivedSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmCDataTraceReceivedSapi.setStatus("current")


class _OduTcmCDataTraceReceivedDapi_Type(OctetString):
    """Custom type oduTcmCDataTraceReceivedDapi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_OduTcmCDataTraceReceivedDapi_Type.__name__ = "OctetString"
_OduTcmCDataTraceReceivedDapi_Object = MibTableColumn
oduTcmCDataTraceReceivedDapi = _OduTcmCDataTraceReceivedDapi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 2),
    _OduTcmCDataTraceReceivedDapi_Type()
)
oduTcmCDataTraceReceivedDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmCDataTraceReceivedDapi.setStatus("current")


class _OduTcmCDataTraceReceivedOpsp_Type(OctetString):
    """Custom type oduTcmCDataTraceReceivedOpsp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_OduTcmCDataTraceReceivedOpsp_Type.__name__ = "OctetString"
_OduTcmCDataTraceReceivedOpsp_Object = MibTableColumn
oduTcmCDataTraceReceivedOpsp = _OduTcmCDataTraceReceivedOpsp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 3),
    _OduTcmCDataTraceReceivedOpsp_Type()
)
oduTcmCDataTraceReceivedOpsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTcmCDataTraceReceivedOpsp.setStatus("current")
_InventoryMib_ObjectIdentity = ObjectIdentity
inventoryMib = _InventoryMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5)
)
_InventoryTable_Object = MibTable
inventoryTable = _InventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    inventoryTable.setStatus("current")
_InventoryEntry_Object = MibTableRow
inventoryEntry = _InventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1)
)
inventoryEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    inventoryEntry.setStatus("current")
_InventoryUnitName_Type = SnmpAdminString
_InventoryUnitName_Object = MibTableColumn
inventoryUnitName = _InventoryUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 1),
    _InventoryUnitName_Type()
)
inventoryUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryUnitName.setStatus("current")
_InventoryFirmwarePackageRev_Type = SnmpAdminString
_InventoryFirmwarePackageRev_Object = MibTableColumn
inventoryFirmwarePackageRev = _InventoryFirmwarePackageRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 2),
    _InventoryFirmwarePackageRev_Type()
)
inventoryFirmwarePackageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryFirmwarePackageRev.setStatus("current")
_InventoryHardwareRev_Type = SnmpAdminString
_InventoryHardwareRev_Object = MibTableColumn
inventoryHardwareRev = _InventoryHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 3),
    _InventoryHardwareRev_Type()
)
inventoryHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryHardwareRev.setStatus("current")
_InventorySoftwareRev_Type = SnmpAdminString
_InventorySoftwareRev_Object = MibTableColumn
inventorySoftwareRev = _InventorySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 4),
    _InventorySoftwareRev_Type()
)
inventorySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySoftwareRev.setStatus("current")
_InventoryFpgaRev_Type = SnmpAdminString
_InventoryFpgaRev_Object = MibTableColumn
inventoryFpgaRev = _InventoryFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 5),
    _InventoryFpgaRev_Type()
)
inventoryFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryFpgaRev.setStatus("current")
_InventorySerialNum_Type = SnmpAdminString
_InventorySerialNum_Object = MibTableColumn
inventorySerialNum = _InventorySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 6),
    _InventorySerialNum_Type()
)
inventorySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySerialNum.setStatus("current")
_InventoryPartnumber_Type = SnmpAdminString
_InventoryPartnumber_Object = MibTableColumn
inventoryPartnumber = _InventoryPartnumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 7),
    _InventoryPartnumber_Type()
)
inventoryPartnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryPartnumber.setStatus("current")
_InventoryCleiCode_Type = SnmpAdminString
_InventoryCleiCode_Object = MibTableColumn
inventoryCleiCode = _InventoryCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 8),
    _InventoryCleiCode_Type()
)
inventoryCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryCleiCode.setStatus("current")
_InventoryVendorId_Type = SnmpAdminString
_InventoryVendorId_Object = MibTableColumn
inventoryVendorId = _InventoryVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 9),
    _InventoryVendorId_Type()
)
inventoryVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryVendorId.setStatus("current")
_InventoryType_Type = EntityType
_InventoryType_Object = MibTableColumn
inventoryType = _InventoryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 10),
    _InventoryType_Type()
)
inventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryType.setStatus("current")
_EntityTable_Object = MibTable
entityTable = _EntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2)
)
if mibBuilder.loadTexts:
    entityTable.setStatus("current")
_EntityEntry_Object = MibTableRow
entityEntry = _EntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1)
)
entityEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    entityEntry.setStatus("current")
_EntityIndex_Type = EntityIndex
_EntityIndex_Object = MibTableColumn
entityIndex = _EntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 1),
    _EntityIndex_Type()
)
entityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    entityIndex.setStatus("current")
_EntityContainedIn_Type = EntityIndex
_EntityContainedIn_Object = MibTableColumn
entityContainedIn = _EntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 2),
    _EntityContainedIn_Type()
)
entityContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityContainedIn.setStatus("current")
_EntityClass_Type = EntityClass
_EntityClass_Object = MibTableColumn
entityClass = _EntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 3),
    _EntityClass_Type()
)
entityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityClass.setStatus("current")


class _EntityClassInstanceNumber_Type(Integer32):
    """Custom type entityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_EntityClassInstanceNumber_Type.__name__ = "Integer32"
_EntityClassInstanceNumber_Object = MibTableColumn
entityClassInstanceNumber = _EntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 4),
    _EntityClassInstanceNumber_Type()
)
entityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityClassInstanceNumber.setStatus("current")
_EntityIndexAid_Type = SnmpAdminString
_EntityIndexAid_Object = MibTableColumn
entityIndexAid = _EntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 5),
    _EntityIndexAid_Type()
)
entityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityIndexAid.setStatus("current")
_EntityType_Type = EntityType
_EntityType_Object = MibTableColumn
entityType = _EntityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 6),
    _EntityType_Type()
)
entityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityType.setStatus("current")
_EntityAssignmentState_Type = AssignmentState
_EntityAssignmentState_Object = MibTableColumn
entityAssignmentState = _EntityAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 7),
    _EntityAssignmentState_Type()
)
entityAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityAssignmentState.setStatus("current")
_EntityEquipmentState_Type = EquipmentState
_EntityEquipmentState_Object = MibTableColumn
entityEquipmentState = _EntityEquipmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 8),
    _EntityEquipmentState_Type()
)
entityEquipmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityEquipmentState.setStatus("current")
_ContainsTable_Object = MibTable
containsTable = _ContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3)
)
if mibBuilder.loadTexts:
    containsTable.setStatus("current")
_ContainsEntry_Object = MibTableRow
containsEntry = _ContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1)
)
containsEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
    (0, "ADVANEW-MIB", "containsIndex"),
)
if mibBuilder.loadTexts:
    containsEntry.setStatus("current")
_ContainsIndex_Type = EntityIndex
_ContainsIndex_Object = MibTableColumn
containsIndex = _ContainsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1, 1),
    _ContainsIndex_Type()
)
containsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containsIndex.setStatus("current")
_UpdateBackupRestoreMib_ObjectIdentity = ObjectIdentity
updateBackupRestoreMib = _UpdateBackupRestoreMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6)
)
_SwAdmin_ObjectIdentity = ObjectIdentity
swAdmin = _SwAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1)
)
_SwDbFileTable_Object = MibTable
swDbFileTable = _SwDbFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    swDbFileTable.setStatus("current")
_SwDbFileEntry_Object = MibTableRow
swDbFileEntry = _SwDbFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1)
)
swDbFileEntry.setIndexNames(
    (0, "ADVANEW-MIB", "swDbFileIndex"),
)
if mibBuilder.loadTexts:
    swDbFileEntry.setStatus("current")
_SwDbFileIndex_Type = EntityIndex
_SwDbFileIndex_Object = MibTableColumn
swDbFileIndex = _SwDbFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 1),
    _SwDbFileIndex_Type()
)
swDbFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDbFileIndex.setStatus("current")
_SwDbFileArea_Type = FileArea
_SwDbFileArea_Object = MibTableColumn
swDbFileArea = _SwDbFileArea_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 2),
    _SwDbFileArea_Type()
)
swDbFileArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileArea.setStatus("current")
_SwDbFileType_Type = FileType
_SwDbFileType_Object = MibTableColumn
swDbFileType = _SwDbFileType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 3),
    _SwDbFileType_Type()
)
swDbFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileType.setStatus("current")
_SwDbFileSize_Type = Unsigned32
_SwDbFileSize_Object = MibTableColumn
swDbFileSize = _SwDbFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 4),
    _SwDbFileSize_Type()
)
swDbFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileSize.setStatus("current")
if mibBuilder.loadTexts:
    swDbFileSize.setUnits("Byte")
_SwDbFileCreationTime_Type = DateAndTime
_SwDbFileCreationTime_Object = MibTableColumn
swDbFileCreationTime = _SwDbFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 5),
    _SwDbFileCreationTime_Type()
)
swDbFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileCreationTime.setStatus("current")
_SwDbFileVersion_Type = SnmpAdminString
_SwDbFileVersion_Object = MibTableColumn
swDbFileVersion = _SwDbFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 6),
    _SwDbFileVersion_Type()
)
swDbFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileVersion.setStatus("current")
_SwDbFileGrade_Type = Grade
_SwDbFileGrade_Object = MibTableColumn
swDbFileGrade = _SwDbFileGrade_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 7),
    _SwDbFileGrade_Type()
)
swDbFileGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileGrade.setStatus("current")
_SwDbFileComment_Type = SnmpAdminString
_SwDbFileComment_Object = MibTableColumn
swDbFileComment = _SwDbFileComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 8),
    _SwDbFileComment_Type()
)
swDbFileComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDbFileComment.setStatus("current")
_SwDbFileFileName_Type = SnmpAdminString
_SwDbFileFileName_Object = MibTableColumn
swDbFileFileName = _SwDbFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 9),
    _SwDbFileFileName_Type()
)
swDbFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbFileFileName.setStatus("current")
_SwDbFileRowStatus_Type = RowStatus
_SwDbFileRowStatus_Object = MibTableColumn
swDbFileRowStatus = _SwDbFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 10),
    _SwDbFileRowStatus_Type()
)
swDbFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDbFileRowStatus.setStatus("current")
_FwDataTable_Object = MibTable
fwDataTable = _FwDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    fwDataTable.setStatus("current")
_FwDataEntry_Object = MibTableRow
fwDataEntry = _FwDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1)
)
fwDataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "entityIndex"),
)
if mibBuilder.loadTexts:
    fwDataEntry.setStatus("current")
_FwDataNewVersion_Type = SnmpAdminString
_FwDataNewVersion_Object = MibTableColumn
fwDataNewVersion = _FwDataNewVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 1),
    _FwDataNewVersion_Type()
)
fwDataNewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataNewVersion.setStatus("current")
_FwDataStandbyVersion_Type = SnmpAdminString
_FwDataStandbyVersion_Object = MibTableColumn
fwDataStandbyVersion = _FwDataStandbyVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 2),
    _FwDataStandbyVersion_Type()
)
fwDataStandbyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataStandbyVersion.setStatus("current")
_FwDataServiceImpairment_Type = ServiceAffecting
_FwDataServiceImpairment_Object = MibTableColumn
fwDataServiceImpairment = _FwDataServiceImpairment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 3),
    _FwDataServiceImpairment_Type()
)
fwDataServiceImpairment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataServiceImpairment.setStatus("current")
_FwDataBootStatus_Type = BootState
_FwDataBootStatus_Object = MibTableColumn
fwDataBootStatus = _FwDataBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 4),
    _FwDataBootStatus_Type()
)
fwDataBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDataBootStatus.setStatus("current")
_EqpFwUpgradeRequest_Type = CommandEqpt
_EqpFwUpgradeRequest_Object = MibScalar
eqpFwUpgradeRequest = _EqpFwUpgradeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 10),
    _EqpFwUpgradeRequest_Type()
)
eqpFwUpgradeRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwUpgradeRequest.setStatus("current")
_EqpFwServiceImpairment_Type = ServiceAffecting
_EqpFwServiceImpairment_Object = MibScalar
eqpFwServiceImpairment = _EqpFwServiceImpairment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 11),
    _EqpFwServiceImpairment_Type()
)
eqpFwServiceImpairment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwServiceImpairment.setStatus("current")
_EqpFwNextEqpForUpdate_Type = EntityIndex
_EqpFwNextEqpForUpdate_Object = MibScalar
eqpFwNextEqpForUpdate = _EqpFwNextEqpForUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 12),
    _EqpFwNextEqpForUpdate_Type()
)
eqpFwNextEqpForUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwNextEqpForUpdate.setStatus("current")
_EqpFwEqpType_Type = FspR7EquipmentType
_EqpFwEqpType_Object = MibScalar
eqpFwEqpType = _EqpFwEqpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 13),
    _EqpFwEqpType_Type()
)
eqpFwEqpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqpFwEqpType.setStatus("current")
_EqpFwNcuServerBusy_Type = FspR7FalseTrue
_EqpFwNcuServerBusy_Object = MibScalar
eqpFwNcuServerBusy = _EqpFwNcuServerBusy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 14),
    _EqpFwNcuServerBusy_Type()
)
eqpFwNcuServerBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqpFwNcuServerBusy.setStatus("current")
_EqpFwEqpServerBusy_Type = FspR7FalseTrue
_EqpFwEqpServerBusy_Object = MibScalar
eqpFwEqpServerBusy = _EqpFwEqpServerBusy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 15),
    _EqpFwEqpServerBusy_Type()
)
eqpFwEqpServerBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqpFwEqpServerBusy.setStatus("current")
_UpdateEqpt_Type = Unsigned32
_UpdateEqpt_Object = MibScalar
updateEqpt = _UpdateEqpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 16),
    _UpdateEqpt_Type()
)
updateEqpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateEqpt.setStatus("current")
_InstalledEqpt_Type = Unsigned32
_InstalledEqpt_Object = MibScalar
installedEqpt = _InstalledEqpt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 17),
    _InstalledEqpt_Type()
)
installedEqpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedEqpt.setStatus("current")
_DbAdmin_ObjectIdentity = ObjectIdentity
dbAdmin = _DbAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2)
)
_NeRestoreConfig_Type = RestoreActivation
_NeRestoreConfig_Object = MibScalar
neRestoreConfig = _NeRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 1),
    _NeRestoreConfig_Type()
)
neRestoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neRestoreConfig.setStatus("current")
_SwDbDataTable_Object = MibTable
swDbDataTable = _SwDbDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2)
)
if mibBuilder.loadTexts:
    swDbDataTable.setStatus("current")
_SwDbDataEntry_Object = MibTableRow
swDbDataEntry = _SwDbDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1)
)
swDbDataEntry.setIndexNames(
    (0, "ADVANEW-MIB", "swDbDataIndex"),
)
if mibBuilder.loadTexts:
    swDbDataEntry.setStatus("current")
_SwDbDataIndex_Type = EntityIndex
_SwDbDataIndex_Object = MibTableColumn
swDbDataIndex = _SwDbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 1),
    _SwDbDataIndex_Type()
)
swDbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDbDataIndex.setStatus("current")
_SwDbDataArea_Type = FileArea
_SwDbDataArea_Object = MibTableColumn
swDbDataArea = _SwDbDataArea_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 2),
    _SwDbDataArea_Type()
)
swDbDataArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataArea.setStatus("current")
_SwDbDataProgramVersion_Type = SnmpAdminString
_SwDbDataProgramVersion_Object = MibTableColumn
swDbDataProgramVersion = _SwDbDataProgramVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 3),
    _SwDbDataProgramVersion_Type()
)
swDbDataProgramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataProgramVersion.setStatus("current")
_SwDbDataDatabaseVersion_Type = SnmpAdminString
_SwDbDataDatabaseVersion_Object = MibTableColumn
swDbDataDatabaseVersion = _SwDbDataDatabaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 4),
    _SwDbDataDatabaseVersion_Type()
)
swDbDataDatabaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataDatabaseVersion.setStatus("current")
_SwDbDataActivationTime_Type = DateAndTime
_SwDbDataActivationTime_Object = MibTableColumn
swDbDataActivationTime = _SwDbDataActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 5),
    _SwDbDataActivationTime_Type()
)
swDbDataActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataActivationTime.setStatus("current")
_SwDbDataRestoreConfig_Type = RestoreActivation
_SwDbDataRestoreConfig_Object = MibTableColumn
swDbDataRestoreConfig = _SwDbDataRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 6),
    _SwDbDataRestoreConfig_Type()
)
swDbDataRestoreConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDbDataRestoreConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVANEW-MIB",
    **{"ApsDirection": ApsDirection,
       "ApsHoldoffTime": ApsHoldoffTime,
       "ApsHoldoffTimeCaps": ApsHoldoffTimeCaps,
       "ApsRevertMode": ApsRevertMode,
       "ApsRevertModeCaps": ApsRevertModeCaps,
       "ApsType": ApsType,
       "AssignmentState": AssignmentState,
       "BootState": BootState,
       "ClockDataRate": ClockDataRate,
       "CommandEqpt": CommandEqpt,
       "EnableStateCaps": EnableStateCaps,
       "EntityClass": EntityClass,
       "EntityIndex": EntityIndex,
       "EntityType": EntityType,
       "EquipmentState": EquipmentState,
       "EthDuplexMode": EthDuplexMode,
       "EthDuplexModeCaps": EthDuplexModeCaps,
       "FileArea": FileArea,
       "FileType": FileType,
       "FspR7EquipmentType": FspR7EquipmentType,
       "FspR7EquipmentTypeCaps": FspR7EquipmentTypeCaps,
       "FspR7FalseTrue": FspR7FalseTrue,
       "Grade": Grade,
       "LoopConfig": LoopConfig,
       "LoopConfigCaps": LoopConfigCaps,
       "OhTerminationLevel": OhTerminationLevel,
       "OhTerminationLevelCaps": OhTerminationLevelCaps,
       "OtnPayloadType": OtnPayloadType,
       "OtnPayloadTypeCaps": OtnPayloadTypeCaps,
       "OtnTcmLevel": OtnTcmLevel,
       "OtnTcmLevelCaps": OtnTcmLevelCaps,
       "ProtectionMech": ProtectionMech,
       "ProtectionMechCaps": ProtectionMechCaps,
       "RestoreActivation": RestoreActivation,
       "ServiceAffecting": ServiceAffecting,
       "SonetSectSigDegThres": SonetSectSigDegThres,
       "SonetSectSigDegThresCaps": SonetSectSigDegThresCaps,
       "SonetTimingSource": SonetTimingSource,
       "SonetTimingSourceCaps": SonetTimingSourceCaps,
       "SonetTraceForm": SonetTraceForm,
       "SonetTraceFormCaps": SonetTraceFormCaps,
       "SonetVcBundleAllocation": SonetVcBundleAllocation,
       "SonetVcBundleAllocationCaps": SonetVcBundleAllocationCaps,
       "TimMode": TimMode,
       "TimModeCaps": TimModeCaps,
       "VirtualContainerType": VirtualContainerType,
       "VirtualContainerTypeCaps": VirtualContainerTypeCaps,
       "transportStandards": transportStandards,
       "sonet": sonet,
       "sonetConfig": sonetConfig,
       "sonetSectionConfigTable": sonetSectionConfigTable,
       "sonetSectionConfigEntry": sonetSectionConfigEntry,
       "sonetSectionConfigTimingSource": sonetSectionConfigTimingSource,
       "sonetSectionConfigSignalDegradeThreshhold": sonetSectionConfigSignalDegradeThreshhold,
       "sonetSectionConfigSignalDegradePeriod": sonetSectionConfigSignalDegradePeriod,
       "sonetSectionConfigTraceForm": sonetSectionConfigTraceForm,
       "sonetSectionConfigTraceExpected": sonetSectionConfigTraceExpected,
       "sonetSectionConfigTraceTransmit": sonetSectionConfigTraceTransmit,
       "sonetSectionConfigTimMode": sonetSectionConfigTimMode,
       "sonetSectionDataTable": sonetSectionDataTable,
       "sonetSectionDataEntry": sonetSectionDataEntry,
       "sonetSectionDataTraceReceived": sonetSectionDataTraceReceived,
       "otn": otn,
       "otuConfig": otuConfig,
       "otuSectionConfigTable": otuSectionConfigTable,
       "otuSectionConfigEntry": otuSectionConfigEntry,
       "otuSectionConfigSignalDegradeThreshold": otuSectionConfigSignalDegradeThreshold,
       "otuSectionConfigSignalDegradePeriod": otuSectionConfigSignalDegradePeriod,
       "otuSectionConfigPayload": otuSectionConfigPayload,
       "otuSectionConfigStuffing": otuSectionConfigStuffing,
       "otuSectionConfigTraceExpected": otuSectionConfigTraceExpected,
       "otuSectionConfigTraceTransmitSapi": otuSectionConfigTraceTransmitSapi,
       "otuSectionConfigTraceTransmitDapi": otuSectionConfigTraceTransmitDapi,
       "otuSectionConfigTraceTransmitOpsp": otuSectionConfigTraceTransmitOpsp,
       "otuSectionConfigTimMode": otuSectionConfigTimMode,
       "otuSectionDataTable": otuSectionDataTable,
       "otuSectionDataEntry": otuSectionDataEntry,
       "otuSectionDataResultingTotalBitrate": otuSectionDataResultingTotalBitrate,
       "otuSectionDataTraceReceivedSapi": otuSectionDataTraceReceivedSapi,
       "otuSectionDataTraceReceivedDapi": otuSectionDataTraceReceivedDapi,
       "otuSectionDataTraceReceivedOpsp": otuSectionDataTraceReceivedOpsp,
       "oduConfig": oduConfig,
       "oduSectionConfigTable": oduSectionConfigTable,
       "oduSectionConfigEntry": oduSectionConfigEntry,
       "oduSectionConfigSignalDegradeThres": oduSectionConfigSignalDegradeThres,
       "oduSectionConfigSignalDegradePeriod": oduSectionConfigSignalDegradePeriod,
       "oduSectionConfigTraceExpected": oduSectionConfigTraceExpected,
       "oduSectionConfigTraceTransmitSapi": oduSectionConfigTraceTransmitSapi,
       "oduSectionConfigTraceTransmitDapi": oduSectionConfigTraceTransmitDapi,
       "oduSectionConfigTraceTransmitOpsp": oduSectionConfigTraceTransmitOpsp,
       "oduSectionConfigTimMode": oduSectionConfigTimMode,
       "oduSectionDataTable": oduSectionDataTable,
       "oduSectionDataEntry": oduSectionDataEntry,
       "oduSectionDataTraceReceivedSapi": oduSectionDataTraceReceivedSapi,
       "oduSectionDataTraceReceivedDapi": oduSectionDataTraceReceivedDapi,
       "oduSectionDataTraceReceivedOpsp": oduSectionDataTraceReceivedOpsp,
       "oduTcmAConfigTable": oduTcmAConfigTable,
       "oduTcmAConfigEntry": oduTcmAConfigEntry,
       "oduTcmAConfigSignalDegradeThreshold": oduTcmAConfigSignalDegradeThreshold,
       "oduTcmAConfigSignalDegradePeriod": oduTcmAConfigSignalDegradePeriod,
       "oduTcmAConfigTcmLevel": oduTcmAConfigTcmLevel,
       "oduTcmAConfigTraceExpected": oduTcmAConfigTraceExpected,
       "oduTcmAConfigTraceTransmitSapi": oduTcmAConfigTraceTransmitSapi,
       "oduTcmAConfigTraceTransmitDapi": oduTcmAConfigTraceTransmitDapi,
       "oduTcmAConfigTraceTransmitOpsp": oduTcmAConfigTraceTransmitOpsp,
       "oduTcmAConfigTimMode": oduTcmAConfigTimMode,
       "oduTcmBConfigTable": oduTcmBConfigTable,
       "oduTcmBConfigEntry": oduTcmBConfigEntry,
       "oduTcmBConfigSignalDegradeThreshold": oduTcmBConfigSignalDegradeThreshold,
       "oduTcmBConfigSignalDegradePeriod": oduTcmBConfigSignalDegradePeriod,
       "oduTcmBConfigTcmLevel": oduTcmBConfigTcmLevel,
       "oduTcmBConfigTraceExpected": oduTcmBConfigTraceExpected,
       "oduTcmBConfigTraceTransmitSapi": oduTcmBConfigTraceTransmitSapi,
       "oduTcmBConfigTraceTransmitDapi": oduTcmBConfigTraceTransmitDapi,
       "oduTcmBConfigTraceTransmitOpsp": oduTcmBConfigTraceTransmitOpsp,
       "oduTcmBConfigTimMode": oduTcmBConfigTimMode,
       "oduTcmCConfigTable": oduTcmCConfigTable,
       "oduTcmCConfigEntry": oduTcmCConfigEntry,
       "oduTcmCConfigSignalDegradeThreshold": oduTcmCConfigSignalDegradeThreshold,
       "oduTcmCConfigSignalDegradePeriod": oduTcmCConfigSignalDegradePeriod,
       "oduTcmCConfigTcmLevel": oduTcmCConfigTcmLevel,
       "oduTcmCConfigTraceExpected": oduTcmCConfigTraceExpected,
       "oduTcmCConfigTraceTransmitSapi": oduTcmCConfigTraceTransmitSapi,
       "oduTcmCConfigTraceTransmitDapi": oduTcmCConfigTraceTransmitDapi,
       "oduTcmCConfigTraceTransmitOpsp": oduTcmCConfigTraceTransmitOpsp,
       "oduTcmCConfigTimMode": oduTcmCConfigTimMode,
       "oduTcmADataTable": oduTcmADataTable,
       "oduTcmADataEntry": oduTcmADataEntry,
       "oduTcmADataTraceReceivedSapi": oduTcmADataTraceReceivedSapi,
       "oduTcmADataTraceReceivedDapi": oduTcmADataTraceReceivedDapi,
       "oduTcmADataTraceReceivedOpsp": oduTcmADataTraceReceivedOpsp,
       "oduTcmBDataTable": oduTcmBDataTable,
       "oduTcmBDataEntry": oduTcmBDataEntry,
       "oduTcmBDataTraceReceivedSapi": oduTcmBDataTraceReceivedSapi,
       "oduTcmBDataTraceReceivedDapi": oduTcmBDataTraceReceivedDapi,
       "oduTcmBDataTraceReceivedOpsp": oduTcmBDataTraceReceivedOpsp,
       "oduTcmCDataTable": oduTcmCDataTable,
       "oduTcmCDataEntry": oduTcmCDataEntry,
       "oduTcmCDataTraceReceivedSapi": oduTcmCDataTraceReceivedSapi,
       "oduTcmCDataTraceReceivedDapi": oduTcmCDataTraceReceivedDapi,
       "oduTcmCDataTraceReceivedOpsp": oduTcmCDataTraceReceivedOpsp,
       "inventoryMib": inventoryMib,
       "inventoryTable": inventoryTable,
       "inventoryEntry": inventoryEntry,
       "inventoryUnitName": inventoryUnitName,
       "inventoryFirmwarePackageRev": inventoryFirmwarePackageRev,
       "inventoryHardwareRev": inventoryHardwareRev,
       "inventorySoftwareRev": inventorySoftwareRev,
       "inventoryFpgaRev": inventoryFpgaRev,
       "inventorySerialNum": inventorySerialNum,
       "inventoryPartnumber": inventoryPartnumber,
       "inventoryCleiCode": inventoryCleiCode,
       "inventoryVendorId": inventoryVendorId,
       "inventoryType": inventoryType,
       "entityTable": entityTable,
       "entityEntry": entityEntry,
       "entityIndex": entityIndex,
       "entityContainedIn": entityContainedIn,
       "entityClass": entityClass,
       "entityClassInstanceNumber": entityClassInstanceNumber,
       "entityIndexAid": entityIndexAid,
       "entityType": entityType,
       "entityAssignmentState": entityAssignmentState,
       "entityEquipmentState": entityEquipmentState,
       "containsTable": containsTable,
       "containsEntry": containsEntry,
       "containsIndex": containsIndex,
       "updateBackupRestoreMib": updateBackupRestoreMib,
       "swAdmin": swAdmin,
       "swDbFileTable": swDbFileTable,
       "swDbFileEntry": swDbFileEntry,
       "swDbFileIndex": swDbFileIndex,
       "swDbFileArea": swDbFileArea,
       "swDbFileType": swDbFileType,
       "swDbFileSize": swDbFileSize,
       "swDbFileCreationTime": swDbFileCreationTime,
       "swDbFileVersion": swDbFileVersion,
       "swDbFileGrade": swDbFileGrade,
       "swDbFileComment": swDbFileComment,
       "swDbFileFileName": swDbFileFileName,
       "swDbFileRowStatus": swDbFileRowStatus,
       "fwDataTable": fwDataTable,
       "fwDataEntry": fwDataEntry,
       "fwDataNewVersion": fwDataNewVersion,
       "fwDataStandbyVersion": fwDataStandbyVersion,
       "fwDataServiceImpairment": fwDataServiceImpairment,
       "fwDataBootStatus": fwDataBootStatus,
       "eqpFwUpgradeRequest": eqpFwUpgradeRequest,
       "eqpFwServiceImpairment": eqpFwServiceImpairment,
       "eqpFwNextEqpForUpdate": eqpFwNextEqpForUpdate,
       "eqpFwEqpType": eqpFwEqpType,
       "eqpFwNcuServerBusy": eqpFwNcuServerBusy,
       "eqpFwEqpServerBusy": eqpFwEqpServerBusy,
       "updateEqpt": updateEqpt,
       "installedEqpt": installedEqpt,
       "dbAdmin": dbAdmin,
       "neRestoreConfig": neRestoreConfig,
       "swDbDataTable": swDbDataTable,
       "swDbDataEntry": swDbDataEntry,
       "swDbDataIndex": swDbDataIndex,
       "swDbDataArea": swDbDataArea,
       "swDbDataProgramVersion": swDbDataProgramVersion,
       "swDbDataDatabaseVersion": swDbDataDatabaseVersion,
       "swDbDataActivationTime": swDbDataActivationTime,
       "swDbDataRestoreConfig": swDbDataRestoreConfig,
       "advaNewMIB": advaNewMIB}
)
