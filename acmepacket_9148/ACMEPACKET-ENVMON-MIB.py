# SNMP MIB module (ACMEPACKET-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/ACMEPACKET-ENVMON-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApHardwareModuleFamily,
 ApPhyPortType,
 ApPresence,
 ApRedundancyState) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApHardwareModuleFamily",
    "ApPhyPortType",
    "ApPresence",
    "ApRedundancyState")

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
 iso) = mibBuilder.importSymbols(
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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apEnvMonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3)
)
if mibBuilder.loadTexts:
    apEnvMonModule.setRevisions(
        ("2012-07-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ApEnvMonState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("normal", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5),
          ("shutdown", 6),
          ("notPresent", 7),
          ("notFunctioning", 8),
          ("unknown", 9))
    )



# MIB Managed Objects in the order of their OIDs

_ApEnvMonObjects_ObjectIdentity = ObjectIdentity
apEnvMonObjects = _ApEnvMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1)
)
_ApEnvMonI2CState_Type = ApEnvMonState
_ApEnvMonI2CState_Object = MibScalar
apEnvMonI2CState = _ApEnvMonI2CState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 1),
    _ApEnvMonI2CState_Type()
)
apEnvMonI2CState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonI2CState.setStatus("current")
_ApEnvMonVoltageObjects_ObjectIdentity = ObjectIdentity
apEnvMonVoltageObjects = _ApEnvMonVoltageObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2)
)
_ApEnvMonVoltageStatusTable_Object = MibTable
apEnvMonVoltageStatusTable = _ApEnvMonVoltageStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apEnvMonVoltageStatusTable.setStatus("current")
_ApEnvMonVoltageStatusEntry_Object = MibTableRow
apEnvMonVoltageStatusEntry = _ApEnvMonVoltageStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1)
)
apEnvMonVoltageStatusEntry.setIndexNames(
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusIndex"),
)
if mibBuilder.loadTexts:
    apEnvMonVoltageStatusEntry.setStatus("current")


class _ApEnvMonVoltageStatusIndex_Type(Integer32):
    """Custom type apEnvMonVoltageStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApEnvMonVoltageStatusIndex_Type.__name__ = "Integer32"
_ApEnvMonVoltageStatusIndex_Object = MibTableColumn
apEnvMonVoltageStatusIndex = _ApEnvMonVoltageStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 1),
    _ApEnvMonVoltageStatusIndex_Type()
)
apEnvMonVoltageStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apEnvMonVoltageStatusIndex.setStatus("current")


class _ApEnvMonVoltageStatusType_Type(Integer32):
    """Custom type apEnvMonVoltageStatusType based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              40,
              41,
              42,
              43,
              50,
              51,
              52,
              53,
              60,
              61,
              62,
              70,
              71,
              72,
              80,
              81,
              82,
              83,
              84,
              85)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("v2p5", 1),
          ("v3p3", 2),
          ("v5", 3),
          ("cpu", 4),
          ("v1", 5),
          ("v1p1", 6),
          ("v1p15", 7),
          ("v1p2", 8),
          ("v1p212", 9),
          ("v1p25", 10),
          ("v1p3", 11),
          ("v1p5", 12),
          ("v1p8", 13),
          ("v2p6", 14),
          ("v3p3aux", 15),
          ("sd5MainV0p9", 20),
          ("sd5MainV1p0", 21),
          ("sd5MainV1p2", 22),
          ("sd5MainV1p5", 23),
          ("sd5MainV1p8", 24),
          ("sd5MainV2p5", 25),
          ("sd5MainV3p3", 26),
          ("sd5MainV5p0", 27),
          ("sd5PhyV0p9", 30),
          ("sd5PhyV1p0", 31),
          ("sd5PhyV1p1", 32),
          ("sd5PhyV1p2", 33),
          ("sd5PhyV1p5", 34),
          ("sd5PhyV1p8", 35),
          ("sd5PhyV2p5", 36),
          ("sd5PhyV3p3", 37),
          ("sd5MgmtV1p0", 40),
          ("sd5MgmtV1p8", 41),
          ("sd5MgmtV3p3", 42),
          ("sd5MgmtV5p0", 43),
          ("sd5Cav0Pol0", 50),
          ("sd5Cav0Pol1", 51),
          ("sd5Cav1Pol0", 52),
          ("sd5Cav1Pol1", 53),
          ("sd5FlexV1p0", 60),
          ("sd5FlexV1p2", 61),
          ("sd5FlexV1p8", 62),
          ("sd5TighV1p2", 70),
          ("sd5TighV3p3", 71),
          ("sd5TighV1p05", 72),
          ("sd5TcmPol0", 80),
          ("sd5TcmPol1", 81),
          ("sd5TcmPol2", 82),
          ("sd5TcmPol3", 83),
          ("sd5TcmPol4", 84),
          ("sd5TcmPol5", 85))
    )


_ApEnvMonVoltageStatusType_Type.__name__ = "Integer32"
_ApEnvMonVoltageStatusType_Object = MibTableColumn
apEnvMonVoltageStatusType = _ApEnvMonVoltageStatusType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 2),
    _ApEnvMonVoltageStatusType_Type()
)
apEnvMonVoltageStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonVoltageStatusType.setStatus("current")


class _ApEnvMonVoltageStatusDescr_Type(DisplayString):
    """Custom type apEnvMonVoltageStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApEnvMonVoltageStatusDescr_Type.__name__ = "DisplayString"
_ApEnvMonVoltageStatusDescr_Object = MibTableColumn
apEnvMonVoltageStatusDescr = _ApEnvMonVoltageStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 3),
    _ApEnvMonVoltageStatusDescr_Type()
)
apEnvMonVoltageStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonVoltageStatusDescr.setStatus("current")
_ApEnvMonVoltageStatusValue_Type = Integer32
_ApEnvMonVoltageStatusValue_Object = MibTableColumn
apEnvMonVoltageStatusValue = _ApEnvMonVoltageStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 4),
    _ApEnvMonVoltageStatusValue_Type()
)
apEnvMonVoltageStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonVoltageStatusValue.setStatus("current")
if mibBuilder.loadTexts:
    apEnvMonVoltageStatusValue.setUnits("millivolts")
_ApEnvMonVoltageState_Type = ApEnvMonState
_ApEnvMonVoltageState_Object = MibTableColumn
apEnvMonVoltageState = _ApEnvMonVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 5),
    _ApEnvMonVoltageState_Type()
)
apEnvMonVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonVoltageState.setStatus("current")
_ApEnvMonVoltageSlotID_Type = Integer32
_ApEnvMonVoltageSlotID_Object = MibTableColumn
apEnvMonVoltageSlotID = _ApEnvMonVoltageSlotID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 6),
    _ApEnvMonVoltageSlotID_Type()
)
apEnvMonVoltageSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonVoltageSlotID.setStatus("current")
_ApEnvMonVoltageSlotType_Type = ApHardwareModuleFamily
_ApEnvMonVoltageSlotType_Object = MibTableColumn
apEnvMonVoltageSlotType = _ApEnvMonVoltageSlotType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 2, 1, 1, 7),
    _ApEnvMonVoltageSlotType_Type()
)
apEnvMonVoltageSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonVoltageSlotType.setStatus("current")
_ApEnvMonTemperatureObjects_ObjectIdentity = ObjectIdentity
apEnvMonTemperatureObjects = _ApEnvMonTemperatureObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3)
)
_ApEnvMonTemperatureStatusTable_Object = MibTable
apEnvMonTemperatureStatusTable = _ApEnvMonTemperatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    apEnvMonTemperatureStatusTable.setStatus("current")
_ApEnvMonTemperatureStatusEntry_Object = MibTableRow
apEnvMonTemperatureStatusEntry = _ApEnvMonTemperatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1)
)
apEnvMonTemperatureStatusEntry.setIndexNames(
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusIndex"),
)
if mibBuilder.loadTexts:
    apEnvMonTemperatureStatusEntry.setStatus("current")


class _ApEnvMonTemperatureStatusIndex_Type(Integer32):
    """Custom type apEnvMonTemperatureStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApEnvMonTemperatureStatusIndex_Type.__name__ = "Integer32"
_ApEnvMonTemperatureStatusIndex_Object = MibTableColumn
apEnvMonTemperatureStatusIndex = _ApEnvMonTemperatureStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 1),
    _ApEnvMonTemperatureStatusIndex_Type()
)
apEnvMonTemperatureStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apEnvMonTemperatureStatusIndex.setStatus("current")


class _ApEnvMonTemperatureStatusType_Type(Integer32):
    """Custom type apEnvMonTemperatureStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              20,
              21,
              22,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
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
              63)
        )
    )
    namedValues = NamedValues(
        *(("ds1624sMain", 1),
          ("ds1624sCPU", 2),
          ("lm84", 3),
          ("lm75", 4),
          ("lm75Main", 5),
          ("lm75Cpu", 6),
          ("lm75Phy", 7),
          ("sd5MainCpu", 10),
          ("sd5MainLI", 11),
          ("sd5MainRI", 12),
          ("sd5MainLE", 13),
          ("sd5MainRE", 14),
          ("sd5MainPlx", 15),
          ("sd5MainPcie", 16),
          ("sd5MainPsa", 17),
          ("sd5MainPsb", 18),
          ("sd5Tigh", 20),
          ("sd5Flex", 21),
          ("sd5Mgmt", 22),
          ("sd5PhyCav0", 30),
          ("sd5PhyCav1", 31),
          ("sd5PhyTemp0", 32),
          ("sd5PhyTemp1", 33),
          ("sd5PhyTemp2", 34),
          ("sd5PhyTemp3", 35),
          ("sd5PhyTemp4", 36),
          ("sd5PhyTemp5", 37),
          ("sd5PhyTcm0", 40),
          ("sd5PhyTcm1", 41),
          ("sd5PhyTcm2", 42),
          ("sd5PhyTcm3", 43),
          ("sd5PhyTcm4", 44),
          ("sd5PhyTcm5", 45),
          ("sd5PhyTcm6", 46),
          ("sd5PhyTcm7", 47),
          ("sd5PhyTcm8", 48),
          ("sd5PhyTcm9", 49),
          ("sd5PhyTcm10", 50),
          ("sd5PhyTcm11", 51),
          ("sd5PhyTcm12", 52),
          ("sd5PhyTcm13", 53),
          ("sd5PhyTcm14", 54),
          ("sd5PhyTcm15", 55),
          ("sd5PhyTcm16", 56),
          ("sd5PhyTcm17", 57),
          ("sd5PhyTcm18", 58),
          ("sd5PhyTcm19", 59),
          ("sd5PhyTcm20", 60),
          ("sd5PhyTcm21", 61),
          ("sd5PhyTcm22", 62),
          ("sd5PhyTcm23", 63))
    )


_ApEnvMonTemperatureStatusType_Type.__name__ = "Integer32"
_ApEnvMonTemperatureStatusType_Object = MibTableColumn
apEnvMonTemperatureStatusType = _ApEnvMonTemperatureStatusType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 2),
    _ApEnvMonTemperatureStatusType_Type()
)
apEnvMonTemperatureStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonTemperatureStatusType.setStatus("current")


class _ApEnvMonTemperatureStatusDescr_Type(DisplayString):
    """Custom type apEnvMonTemperatureStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApEnvMonTemperatureStatusDescr_Type.__name__ = "DisplayString"
_ApEnvMonTemperatureStatusDescr_Object = MibTableColumn
apEnvMonTemperatureStatusDescr = _ApEnvMonTemperatureStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 3),
    _ApEnvMonTemperatureStatusDescr_Type()
)
apEnvMonTemperatureStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonTemperatureStatusDescr.setStatus("current")
_ApEnvMonTemperatureStatusValue_Type = Integer32
_ApEnvMonTemperatureStatusValue_Object = MibTableColumn
apEnvMonTemperatureStatusValue = _ApEnvMonTemperatureStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 4),
    _ApEnvMonTemperatureStatusValue_Type()
)
apEnvMonTemperatureStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonTemperatureStatusValue.setStatus("current")
if mibBuilder.loadTexts:
    apEnvMonTemperatureStatusValue.setUnits("degrees Celsius")
_ApEnvMonTemperatureState_Type = ApEnvMonState
_ApEnvMonTemperatureState_Object = MibTableColumn
apEnvMonTemperatureState = _ApEnvMonTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 5),
    _ApEnvMonTemperatureState_Type()
)
apEnvMonTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonTemperatureState.setStatus("current")
_ApEnvMonTemperatureSlotID_Type = Integer32
_ApEnvMonTemperatureSlotID_Object = MibTableColumn
apEnvMonTemperatureSlotID = _ApEnvMonTemperatureSlotID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 6),
    _ApEnvMonTemperatureSlotID_Type()
)
apEnvMonTemperatureSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonTemperatureSlotID.setStatus("current")
_ApEnvMonTemperatureSlotType_Type = ApHardwareModuleFamily
_ApEnvMonTemperatureSlotType_Object = MibTableColumn
apEnvMonTemperatureSlotType = _ApEnvMonTemperatureSlotType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 3, 1, 1, 7),
    _ApEnvMonTemperatureSlotType_Type()
)
apEnvMonTemperatureSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonTemperatureSlotType.setStatus("current")
_ApEnvMonFanObjects_ObjectIdentity = ObjectIdentity
apEnvMonFanObjects = _ApEnvMonFanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4)
)
_ApEnvMonFanStatusTable_Object = MibTable
apEnvMonFanStatusTable = _ApEnvMonFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    apEnvMonFanStatusTable.setStatus("current")
_ApEnvMonFanStatusEntry_Object = MibTableRow
apEnvMonFanStatusEntry = _ApEnvMonFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1)
)
apEnvMonFanStatusEntry.setIndexNames(
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusIndex"),
)
if mibBuilder.loadTexts:
    apEnvMonFanStatusEntry.setStatus("current")


class _ApEnvMonFanStatusIndex_Type(Integer32):
    """Custom type apEnvMonFanStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApEnvMonFanStatusIndex_Type.__name__ = "Integer32"
_ApEnvMonFanStatusIndex_Object = MibTableColumn
apEnvMonFanStatusIndex = _ApEnvMonFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 1),
    _ApEnvMonFanStatusIndex_Type()
)
apEnvMonFanStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apEnvMonFanStatusIndex.setStatus("current")


class _ApEnvMonFanStatusType_Type(Integer32):
    """Custom type apEnvMonFanStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              11,
              12,
              13,
              14,
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
              35)
        )
    )
    namedValues = NamedValues(
        *(("left", 0),
          ("middle", 1),
          ("right", 2),
          ("slot", 3),
          ("fan1", 11),
          ("fan2", 12),
          ("fan3", 13),
          ("fan4", 14),
          ("mainFan1", 21),
          ("mainFan2", 22),
          ("mainFan3", 23),
          ("mainFan4", 24),
          ("mainFan5", 25),
          ("flx1Fan1", 26),
          ("flx1Fan2", 27),
          ("flx1Fan3", 28),
          ("flx1Fan4", 29),
          ("flx1Fan5", 30),
          ("flx2Fan1", 31),
          ("flx2Fan2", 32),
          ("flx2Fan3", 33),
          ("flx2Fan4", 34),
          ("flx2Fan5", 35))
    )


_ApEnvMonFanStatusType_Type.__name__ = "Integer32"
_ApEnvMonFanStatusType_Object = MibTableColumn
apEnvMonFanStatusType = _ApEnvMonFanStatusType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 2),
    _ApEnvMonFanStatusType_Type()
)
apEnvMonFanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonFanStatusType.setStatus("current")


class _ApEnvMonFanStatusDescr_Type(DisplayString):
    """Custom type apEnvMonFanStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApEnvMonFanStatusDescr_Type.__name__ = "DisplayString"
_ApEnvMonFanStatusDescr_Object = MibTableColumn
apEnvMonFanStatusDescr = _ApEnvMonFanStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 3),
    _ApEnvMonFanStatusDescr_Type()
)
apEnvMonFanStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonFanStatusDescr.setStatus("current")
_ApEnvMonFanStatusValue_Type = Gauge32
_ApEnvMonFanStatusValue_Object = MibTableColumn
apEnvMonFanStatusValue = _ApEnvMonFanStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 4),
    _ApEnvMonFanStatusValue_Type()
)
apEnvMonFanStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonFanStatusValue.setStatus("current")
if mibBuilder.loadTexts:
    apEnvMonFanStatusValue.setUnits("%")
_ApEnvMonFanState_Type = ApEnvMonState
_ApEnvMonFanState_Object = MibTableColumn
apEnvMonFanState = _ApEnvMonFanState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 5),
    _ApEnvMonFanState_Type()
)
apEnvMonFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonFanState.setStatus("current")
_ApEnvMonFanSlotID_Type = Integer32
_ApEnvMonFanSlotID_Object = MibTableColumn
apEnvMonFanSlotID = _ApEnvMonFanSlotID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 4, 1, 1, 6),
    _ApEnvMonFanSlotID_Type()
)
apEnvMonFanSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonFanSlotID.setStatus("current")
_ApEnvMonPowerSupplyObjects_ObjectIdentity = ObjectIdentity
apEnvMonPowerSupplyObjects = _ApEnvMonPowerSupplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5)
)
_ApEnvMonPowerSupplyStatusTable_Object = MibTable
apEnvMonPowerSupplyStatusTable = _ApEnvMonPowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    apEnvMonPowerSupplyStatusTable.setStatus("current")
_ApEnvMonPowerSupplyStatusEntry_Object = MibTableRow
apEnvMonPowerSupplyStatusEntry = _ApEnvMonPowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1)
)
apEnvMonPowerSupplyStatusEntry.setIndexNames(
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyStatusIndex"),
)
if mibBuilder.loadTexts:
    apEnvMonPowerSupplyStatusEntry.setStatus("current")


class _ApEnvMonPowerSupplyStatusIndex_Type(Integer32):
    """Custom type apEnvMonPowerSupplyStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApEnvMonPowerSupplyStatusIndex_Type.__name__ = "Integer32"
_ApEnvMonPowerSupplyStatusIndex_Object = MibTableColumn
apEnvMonPowerSupplyStatusIndex = _ApEnvMonPowerSupplyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 1),
    _ApEnvMonPowerSupplyStatusIndex_Type()
)
apEnvMonPowerSupplyStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apEnvMonPowerSupplyStatusIndex.setStatus("current")


class _ApEnvMonPowerSupplyStatusType_Type(Integer32):
    """Custom type apEnvMonPowerSupplyStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("left", 0),
          ("right", 1),
          ("slot", 3))
    )


_ApEnvMonPowerSupplyStatusType_Type.__name__ = "Integer32"
_ApEnvMonPowerSupplyStatusType_Object = MibTableColumn
apEnvMonPowerSupplyStatusType = _ApEnvMonPowerSupplyStatusType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 2),
    _ApEnvMonPowerSupplyStatusType_Type()
)
apEnvMonPowerSupplyStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonPowerSupplyStatusType.setStatus("current")


class _ApEnvMonPowerSupplyStatusDescr_Type(DisplayString):
    """Custom type apEnvMonPowerSupplyStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApEnvMonPowerSupplyStatusDescr_Type.__name__ = "DisplayString"
_ApEnvMonPowerSupplyStatusDescr_Object = MibTableColumn
apEnvMonPowerSupplyStatusDescr = _ApEnvMonPowerSupplyStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 3),
    _ApEnvMonPowerSupplyStatusDescr_Type()
)
apEnvMonPowerSupplyStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonPowerSupplyStatusDescr.setStatus("current")
_ApEnvMonPowerSupplyState_Type = ApEnvMonState
_ApEnvMonPowerSupplyState_Object = MibTableColumn
apEnvMonPowerSupplyState = _ApEnvMonPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 5, 1, 1, 4),
    _ApEnvMonPowerSupplyState_Type()
)
apEnvMonPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonPowerSupplyState.setStatus("current")
_ApEnvMonPhyCardObjects_ObjectIdentity = ObjectIdentity
apEnvMonPhyCardObjects = _ApEnvMonPhyCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6)
)
_ApEnvMonPhyCardStatusTable_Object = MibTable
apEnvMonPhyCardStatusTable = _ApEnvMonPhyCardStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    apEnvMonPhyCardStatusTable.setStatus("deprecated")
_ApEnvMonPhyCardStatusEntry_Object = MibTableRow
apEnvMonPhyCardStatusEntry = _ApEnvMonPhyCardStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1)
)
apEnvMonPhyCardStatusEntry.setIndexNames(
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardStatusIndex"),
)
if mibBuilder.loadTexts:
    apEnvMonPhyCardStatusEntry.setStatus("deprecated")


class _ApEnvMonPhyCardStatusIndex_Type(Integer32):
    """Custom type apEnvMonPhyCardStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApEnvMonPhyCardStatusIndex_Type.__name__ = "Integer32"
_ApEnvMonPhyCardStatusIndex_Object = MibTableColumn
apEnvMonPhyCardStatusIndex = _ApEnvMonPhyCardStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 1),
    _ApEnvMonPhyCardStatusIndex_Type()
)
apEnvMonPhyCardStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apEnvMonPhyCardStatusIndex.setStatus("deprecated")


class _ApEnvMonPhyCardStatusType_Type(Integer32):
    """Custom type apEnvMonPhyCardStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("left", 0),
          ("right", 1),
          ("slot", 3))
    )


_ApEnvMonPhyCardStatusType_Type.__name__ = "Integer32"
_ApEnvMonPhyCardStatusType_Object = MibTableColumn
apEnvMonPhyCardStatusType = _ApEnvMonPhyCardStatusType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 2),
    _ApEnvMonPhyCardStatusType_Type()
)
apEnvMonPhyCardStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonPhyCardStatusType.setStatus("deprecated")


class _ApEnvMonPhyCardStatusDescr_Type(DisplayString):
    """Custom type apEnvMonPhyCardStatusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApEnvMonPhyCardStatusDescr_Type.__name__ = "DisplayString"
_ApEnvMonPhyCardStatusDescr_Object = MibTableColumn
apEnvMonPhyCardStatusDescr = _ApEnvMonPhyCardStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 3),
    _ApEnvMonPhyCardStatusDescr_Type()
)
apEnvMonPhyCardStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonPhyCardStatusDescr.setStatus("deprecated")
_ApEnvMonPhyCardState_Type = ApEnvMonState
_ApEnvMonPhyCardState_Object = MibTableColumn
apEnvMonPhyCardState = _ApEnvMonPhyCardState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 6, 1, 1, 4),
    _ApEnvMonPhyCardState_Type()
)
apEnvMonPhyCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonPhyCardState.setStatus("deprecated")
_ApEnvMonCardObjects_ObjectIdentity = ObjectIdentity
apEnvMonCardObjects = _ApEnvMonCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7)
)
_ApEnvMonCardTable_Object = MibTable
apEnvMonCardTable = _ApEnvMonCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    apEnvMonCardTable.setStatus("current")
_ApEnvMonCardEntry_Object = MibTableRow
apEnvMonCardEntry = _ApEnvMonCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1)
)
apEnvMonCardEntry.setIndexNames(
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"),
)
if mibBuilder.loadTexts:
    apEnvMonCardEntry.setStatus("current")
_ApEnvMonCardSlot_Type = Integer32
_ApEnvMonCardSlot_Object = MibTableColumn
apEnvMonCardSlot = _ApEnvMonCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 1),
    _ApEnvMonCardSlot_Type()
)
apEnvMonCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCardSlot.setStatus("current")
_ApEnvMonCardType_Type = ApHardwareModuleFamily
_ApEnvMonCardType_Object = MibTableColumn
apEnvMonCardType = _ApEnvMonCardType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 2),
    _ApEnvMonCardType_Type()
)
apEnvMonCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCardType.setStatus("current")
_ApEnvMonCardDescr_Type = DisplayString
_ApEnvMonCardDescr_Object = MibTableColumn
apEnvMonCardDescr = _ApEnvMonCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 3),
    _ApEnvMonCardDescr_Type()
)
apEnvMonCardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCardDescr.setStatus("current")
_ApEnvMonCardHealthScore_Type = Integer32
_ApEnvMonCardHealthScore_Object = MibTableColumn
apEnvMonCardHealthScore = _ApEnvMonCardHealthScore_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 4),
    _ApEnvMonCardHealthScore_Type()
)
apEnvMonCardHealthScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCardHealthScore.setStatus("current")
_ApEnvMonCardState_Type = ApEnvMonState
_ApEnvMonCardState_Object = MibTableColumn
apEnvMonCardState = _ApEnvMonCardState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 5),
    _ApEnvMonCardState_Type()
)
apEnvMonCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCardState.setStatus("current")
_ApEnvMonCardRedundancy_Type = ApRedundancyState
_ApEnvMonCardRedundancy_Object = MibTableColumn
apEnvMonCardRedundancy = _ApEnvMonCardRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 1, 1, 6),
    _ApEnvMonCardRedundancy_Type()
)
apEnvMonCardRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCardRedundancy.setStatus("current")
_ApEnvMonCpuCoreTable_Object = MibTable
apEnvMonCpuCoreTable = _ApEnvMonCpuCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    apEnvMonCpuCoreTable.setStatus("current")
_ApEnvMonCpuCoreEntry_Object = MibTableRow
apEnvMonCpuCoreEntry = _ApEnvMonCpuCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1)
)
apEnvMonCpuCoreEntry.setIndexNames(
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"),
    (0, "ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreIndex"),
)
if mibBuilder.loadTexts:
    apEnvMonCpuCoreEntry.setStatus("current")
_ApEnvMonCpuCoreIndex_Type = Integer32
_ApEnvMonCpuCoreIndex_Object = MibTableColumn
apEnvMonCpuCoreIndex = _ApEnvMonCpuCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 1),
    _ApEnvMonCpuCoreIndex_Type()
)
apEnvMonCpuCoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreIndex.setStatus("current")
_ApEnvMonCpuCoreDescr_Type = DisplayString
_ApEnvMonCpuCoreDescr_Object = MibTableColumn
apEnvMonCpuCoreDescr = _ApEnvMonCpuCoreDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 2),
    _ApEnvMonCpuCoreDescr_Type()
)
apEnvMonCpuCoreDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreDescr.setStatus("current")
_ApEnvMonCpuCoreUsage_Type = Gauge32
_ApEnvMonCpuCoreUsage_Object = MibTableColumn
apEnvMonCpuCoreUsage = _ApEnvMonCpuCoreUsage_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 3),
    _ApEnvMonCpuCoreUsage_Type()
)
apEnvMonCpuCoreUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreUsage.setStatus("current")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreUsage.setUnits("%")


class _ApEnvMonCpuCoreState_Type(Integer32):
    """Custom type apEnvMonCpuCoreState based on Integer32"""
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
              101,
              102,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              401,
              402,
              403,
              404,
              405,
              406)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("present", 1),
          ("booting", 2),
          ("registered", 3),
          ("readywait", 4),
          ("ready", 5),
          ("bootTimeout", 6),
          ("registerTimeout", 7),
          ("manifestTimeout", 8),
          ("readyTimeout", 9),
          ("healthWait", 101),
          ("healthRcvd", 102),
          ("becomingActive", 201),
          ("becomingStandby", 202),
          ("becomingOOS", 203),
          ("active", 204),
          ("standby", 205),
          ("oos", 206),
          ("activeTimeout", 207),
          ("standbyTimeout", 208),
          ("oosTimeout", 209),
          ("resetting", 401),
          ("reset", 402),
          ("resetTimeout", 403),
          ("shuttingDown", 404),
          ("shutOff", 405),
          ("shutdownTimeout", 406))
    )


_ApEnvMonCpuCoreState_Type.__name__ = "Integer32"
_ApEnvMonCpuCoreState_Object = MibTableColumn
apEnvMonCpuCoreState = _ApEnvMonCpuCoreState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 4),
    _ApEnvMonCpuCoreState_Type()
)
apEnvMonCpuCoreState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreState.setStatus("current")
_ApEnvMonCpuCoreRamDescr_Type = DisplayString
_ApEnvMonCpuCoreRamDescr_Object = MibTableColumn
apEnvMonCpuCoreRamDescr = _ApEnvMonCpuCoreRamDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 5),
    _ApEnvMonCpuCoreRamDescr_Type()
)
apEnvMonCpuCoreRamDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreRamDescr.setStatus("current")
_ApEnvMonCpuCoreRamUsage_Type = Gauge32
_ApEnvMonCpuCoreRamUsage_Object = MibTableColumn
apEnvMonCpuCoreRamUsage = _ApEnvMonCpuCoreRamUsage_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 1, 7, 2, 1, 6),
    _ApEnvMonCpuCoreRamUsage_Type()
)
apEnvMonCpuCoreRamUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreRamUsage.setStatus("current")
if mibBuilder.loadTexts:
    apEnvMonCpuCoreRamUsage.setUnits("%")
_ApEnvMonMIBNotificationEnables_ObjectIdentity = ObjectIdentity
apEnvMonMIBNotificationEnables = _ApEnvMonMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 2)
)
_ApEnvMonEnableStatChangeNotif_Type = TruthValue
_ApEnvMonEnableStatChangeNotif_Object = MibScalar
apEnvMonEnableStatChangeNotif = _ApEnvMonEnableStatChangeNotif_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 2, 1),
    _ApEnvMonEnableStatChangeNotif_Type()
)
apEnvMonEnableStatChangeNotif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEnvMonEnableStatChangeNotif.setStatus("current")
_ApEnvMonNotificationObjects_ObjectIdentity = ObjectIdentity
apEnvMonNotificationObjects = _ApEnvMonNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3)
)
_ApEnvMonTrapInstance_Type = ObjectIdentifier
_ApEnvMonTrapInstance_Object = MibScalar
apEnvMonTrapInstance = _ApEnvMonTrapInstance_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 1),
    _ApEnvMonTrapInstance_Type()
)
apEnvMonTrapInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapInstance.setStatus("current")
_ApEnvMonTrapPreviousState_Type = ApEnvMonState
_ApEnvMonTrapPreviousState_Object = MibScalar
apEnvMonTrapPreviousState = _ApEnvMonTrapPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 2),
    _ApEnvMonTrapPreviousState_Type()
)
apEnvMonTrapPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapPreviousState.setStatus("current")
_ApEnvMonTrapCurrentState_Type = ApEnvMonState
_ApEnvMonTrapCurrentState_Object = MibScalar
apEnvMonTrapCurrentState = _ApEnvMonTrapCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 3),
    _ApEnvMonTrapCurrentState_Type()
)
apEnvMonTrapCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapCurrentState.setStatus("current")
_ApEnvMonTrapSlotID_Type = Integer32
_ApEnvMonTrapSlotID_Object = MibScalar
apEnvMonTrapSlotID = _ApEnvMonTrapSlotID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 4),
    _ApEnvMonTrapSlotID_Type()
)
apEnvMonTrapSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapSlotID.setStatus("current")
_ApEnvMonTrapSlotType_Type = ApHardwareModuleFamily
_ApEnvMonTrapSlotType_Object = MibScalar
apEnvMonTrapSlotType = _ApEnvMonTrapSlotType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 5),
    _ApEnvMonTrapSlotType_Type()
)
apEnvMonTrapSlotType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapSlotType.setStatus("current")
_ApEnvMonTrapPortType_Type = ApPhyPortType
_ApEnvMonTrapPortType_Object = MibScalar
apEnvMonTrapPortType = _ApEnvMonTrapPortType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 6),
    _ApEnvMonTrapPortType_Type()
)
apEnvMonTrapPortType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapPortType.setStatus("current")
_ApEnvMonTrapPresence_Type = ApPresence
_ApEnvMonTrapPresence_Object = MibScalar
apEnvMonTrapPresence = _ApEnvMonTrapPresence_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 7),
    _ApEnvMonTrapPresence_Type()
)
apEnvMonTrapPresence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapPresence.setStatus("current")
_ApEnvMonTrapPortID_Type = Integer32
_ApEnvMonTrapPortID_Object = MibScalar
apEnvMonTrapPortID = _ApEnvMonTrapPortID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 3, 8),
    _ApEnvMonTrapPortID_Type()
)
apEnvMonTrapPortID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEnvMonTrapPortID.setStatus("current")
_ApEnvMonMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
apEnvMonMIBNotificationPrefix = _ApEnvMonMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 4)
)
_ApEnvMonMIBNotifications_ObjectIdentity = ObjectIdentity
apEnvMonMIBNotifications = _ApEnvMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0)
)
_ApEnvMonMIBConformance_ObjectIdentity = ObjectIdentity
apEnvMonMIBConformance = _ApEnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5)
)
_ApEnvMonMIBCompliances_ObjectIdentity = ObjectIdentity
apEnvMonMIBCompliances = _ApEnvMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 1)
)
_ApEnvMonMIBGroups_ObjectIdentity = ObjectIdentity
apEnvMonMIBGroups = _ApEnvMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2)
)

# Managed Objects groups

apEnvMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 1)
)
apEnvMonGroup.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonI2CState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageStatusValue"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureStatusValue"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanStatusValue"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyStatusType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyStatusDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonPowerSupplyState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardStatusType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardStatusDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonPhyCardState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonEnableStatChangeNotif"))
)
if mibBuilder.loadTexts:
    apEnvMonGroup.setStatus("current")

apEnvMonExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 4)
)
apEnvMonExtGroup.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageSlotID"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageSlotType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureSlotID"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTemperatureSlotType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonFanSlotID"))
)
if mibBuilder.loadTexts:
    apEnvMonExtGroup.setStatus("current")

apEnvMonCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 5)
)
apEnvMonCardGroup.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardHealthScore"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardRedundancy"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreIndex"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreUsage"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreRamDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCpuCoreRamUsage"))
)
if mibBuilder.loadTexts:
    apEnvMonCardGroup.setStatus("current")

apEnvMonCardOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 9)
)
apEnvMonCardOnlyGroup.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonCardSlot"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardDescr"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardHealthScore"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonCardRedundancy"))
)
if mibBuilder.loadTexts:
    apEnvMonCardOnlyGroup.setStatus("current")


# Notification objects

apEnvMonI2CFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 1)
)
if mibBuilder.loadTexts:
    apEnvMonI2CFailNotification.setStatus(
        "current"
    )

apEnvMonStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 2)
)
apEnvMonStatusChangeNotification.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapInstance"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPreviousState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapCurrentState"))
)
if mibBuilder.loadTexts:
    apEnvMonStatusChangeNotification.setStatus(
        "current"
    )

apEnvMonTempChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 3)
)
apEnvMonTempChangeNotification.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotID"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPreviousState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapCurrentState"))
)
if mibBuilder.loadTexts:
    apEnvMonTempChangeNotification.setStatus(
        "current"
    )

apEnvMonVoltageChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 4)
)
apEnvMonVoltageChangeNotification.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotID"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPreviousState"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapCurrentState"))
)
if mibBuilder.loadTexts:
    apEnvMonVoltageChangeNotification.setStatus(
        "current"
    )

apEnvMonPortChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 4, 0, 5)
)
apEnvMonPortChangeNotification.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPortType"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPresence"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapSlotID"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonTrapPortID"))
)
if mibBuilder.loadTexts:
    apEnvMonPortChangeNotification.setStatus(
        "current"
    )


# Notifications groups

apEnvMonNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 3)
)
apEnvMonNotifyGroup.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonStatusChangeNotification"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonI2CFailNotification"))
)
if mibBuilder.loadTexts:
    apEnvMonNotifyGroup.setStatus(
        "current"
    )

apEnvMonExtNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 6)
)
apEnvMonExtNotifyGroup.setObjects(
      *(("ACMEPACKET-ENVMON-MIB", "apEnvMonTempChangeNotification"),
        ("ACMEPACKET-ENVMON-MIB", "apEnvMonVoltageChangeNotification"))
)
if mibBuilder.loadTexts:
    apEnvMonExtNotifyGroup.setStatus(
        "current"
    )

apEnvMonPortNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 7)
)
apEnvMonPortNotifyGroup.setObjects(
    ("ACMEPACKET-ENVMON-MIB", "apEnvMonPortChangeNotification")
)
if mibBuilder.loadTexts:
    apEnvMonPortNotifyGroup.setStatus(
        "current"
    )

apEnvMonTempNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 3, 5, 2, 8)
)
apEnvMonTempNotifyGroup.setObjects(
    ("ACMEPACKET-ENVMON-MIB", "apEnvMonTempChangeNotification")
)
if mibBuilder.loadTexts:
    apEnvMonTempNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACMEPACKET-ENVMON-MIB",
    **{"ApEnvMonState": ApEnvMonState,
       "apEnvMonModule": apEnvMonModule,
       "apEnvMonObjects": apEnvMonObjects,
       "apEnvMonI2CState": apEnvMonI2CState,
       "apEnvMonVoltageObjects": apEnvMonVoltageObjects,
       "apEnvMonVoltageStatusTable": apEnvMonVoltageStatusTable,
       "apEnvMonVoltageStatusEntry": apEnvMonVoltageStatusEntry,
       "apEnvMonVoltageStatusIndex": apEnvMonVoltageStatusIndex,
       "apEnvMonVoltageStatusType": apEnvMonVoltageStatusType,
       "apEnvMonVoltageStatusDescr": apEnvMonVoltageStatusDescr,
       "apEnvMonVoltageStatusValue": apEnvMonVoltageStatusValue,
       "apEnvMonVoltageState": apEnvMonVoltageState,
       "apEnvMonVoltageSlotID": apEnvMonVoltageSlotID,
       "apEnvMonVoltageSlotType": apEnvMonVoltageSlotType,
       "apEnvMonTemperatureObjects": apEnvMonTemperatureObjects,
       "apEnvMonTemperatureStatusTable": apEnvMonTemperatureStatusTable,
       "apEnvMonTemperatureStatusEntry": apEnvMonTemperatureStatusEntry,
       "apEnvMonTemperatureStatusIndex": apEnvMonTemperatureStatusIndex,
       "apEnvMonTemperatureStatusType": apEnvMonTemperatureStatusType,
       "apEnvMonTemperatureStatusDescr": apEnvMonTemperatureStatusDescr,
       "apEnvMonTemperatureStatusValue": apEnvMonTemperatureStatusValue,
       "apEnvMonTemperatureState": apEnvMonTemperatureState,
       "apEnvMonTemperatureSlotID": apEnvMonTemperatureSlotID,
       "apEnvMonTemperatureSlotType": apEnvMonTemperatureSlotType,
       "apEnvMonFanObjects": apEnvMonFanObjects,
       "apEnvMonFanStatusTable": apEnvMonFanStatusTable,
       "apEnvMonFanStatusEntry": apEnvMonFanStatusEntry,
       "apEnvMonFanStatusIndex": apEnvMonFanStatusIndex,
       "apEnvMonFanStatusType": apEnvMonFanStatusType,
       "apEnvMonFanStatusDescr": apEnvMonFanStatusDescr,
       "apEnvMonFanStatusValue": apEnvMonFanStatusValue,
       "apEnvMonFanState": apEnvMonFanState,
       "apEnvMonFanSlotID": apEnvMonFanSlotID,
       "apEnvMonPowerSupplyObjects": apEnvMonPowerSupplyObjects,
       "apEnvMonPowerSupplyStatusTable": apEnvMonPowerSupplyStatusTable,
       "apEnvMonPowerSupplyStatusEntry": apEnvMonPowerSupplyStatusEntry,
       "apEnvMonPowerSupplyStatusIndex": apEnvMonPowerSupplyStatusIndex,
       "apEnvMonPowerSupplyStatusType": apEnvMonPowerSupplyStatusType,
       "apEnvMonPowerSupplyStatusDescr": apEnvMonPowerSupplyStatusDescr,
       "apEnvMonPowerSupplyState": apEnvMonPowerSupplyState,
       "apEnvMonPhyCardObjects": apEnvMonPhyCardObjects,
       "apEnvMonPhyCardStatusTable": apEnvMonPhyCardStatusTable,
       "apEnvMonPhyCardStatusEntry": apEnvMonPhyCardStatusEntry,
       "apEnvMonPhyCardStatusIndex": apEnvMonPhyCardStatusIndex,
       "apEnvMonPhyCardStatusType": apEnvMonPhyCardStatusType,
       "apEnvMonPhyCardStatusDescr": apEnvMonPhyCardStatusDescr,
       "apEnvMonPhyCardState": apEnvMonPhyCardState,
       "apEnvMonCardObjects": apEnvMonCardObjects,
       "apEnvMonCardTable": apEnvMonCardTable,
       "apEnvMonCardEntry": apEnvMonCardEntry,
       "apEnvMonCardSlot": apEnvMonCardSlot,
       "apEnvMonCardType": apEnvMonCardType,
       "apEnvMonCardDescr": apEnvMonCardDescr,
       "apEnvMonCardHealthScore": apEnvMonCardHealthScore,
       "apEnvMonCardState": apEnvMonCardState,
       "apEnvMonCardRedundancy": apEnvMonCardRedundancy,
       "apEnvMonCpuCoreTable": apEnvMonCpuCoreTable,
       "apEnvMonCpuCoreEntry": apEnvMonCpuCoreEntry,
       "apEnvMonCpuCoreIndex": apEnvMonCpuCoreIndex,
       "apEnvMonCpuCoreDescr": apEnvMonCpuCoreDescr,
       "apEnvMonCpuCoreUsage": apEnvMonCpuCoreUsage,
       "apEnvMonCpuCoreState": apEnvMonCpuCoreState,
       "apEnvMonCpuCoreRamDescr": apEnvMonCpuCoreRamDescr,
       "apEnvMonCpuCoreRamUsage": apEnvMonCpuCoreRamUsage,
       "apEnvMonMIBNotificationEnables": apEnvMonMIBNotificationEnables,
       "apEnvMonEnableStatChangeNotif": apEnvMonEnableStatChangeNotif,
       "apEnvMonNotificationObjects": apEnvMonNotificationObjects,
       "apEnvMonTrapInstance": apEnvMonTrapInstance,
       "apEnvMonTrapPreviousState": apEnvMonTrapPreviousState,
       "apEnvMonTrapCurrentState": apEnvMonTrapCurrentState,
       "apEnvMonTrapSlotID": apEnvMonTrapSlotID,
       "apEnvMonTrapSlotType": apEnvMonTrapSlotType,
       "apEnvMonTrapPortType": apEnvMonTrapPortType,
       "apEnvMonTrapPresence": apEnvMonTrapPresence,
       "apEnvMonTrapPortID": apEnvMonTrapPortID,
       "apEnvMonMIBNotificationPrefix": apEnvMonMIBNotificationPrefix,
       "apEnvMonMIBNotifications": apEnvMonMIBNotifications,
       "apEnvMonI2CFailNotification": apEnvMonI2CFailNotification,
       "apEnvMonStatusChangeNotification": apEnvMonStatusChangeNotification,
       "apEnvMonTempChangeNotification": apEnvMonTempChangeNotification,
       "apEnvMonVoltageChangeNotification": apEnvMonVoltageChangeNotification,
       "apEnvMonPortChangeNotification": apEnvMonPortChangeNotification,
       "apEnvMonMIBConformance": apEnvMonMIBConformance,
       "apEnvMonMIBCompliances": apEnvMonMIBCompliances,
       "apEnvMonMIBGroups": apEnvMonMIBGroups,
       "apEnvMonGroup": apEnvMonGroup,
       "apEnvMonNotifyGroup": apEnvMonNotifyGroup,
       "apEnvMonExtGroup": apEnvMonExtGroup,
       "apEnvMonCardGroup": apEnvMonCardGroup,
       "apEnvMonExtNotifyGroup": apEnvMonExtNotifyGroup,
       "apEnvMonPortNotifyGroup": apEnvMonPortNotifyGroup,
       "apEnvMonTempNotifyGroup": apEnvMonTempNotifyGroup,
       "apEnvMonCardOnlyGroup": apEnvMonCardOnlyGroup}
)
