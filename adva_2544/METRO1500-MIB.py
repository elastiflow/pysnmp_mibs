# SNMP MIB module (METRO1500-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/METRO1500-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class Metro1500SlotNumberRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Adva_ObjectIdentity = ObjectIdentity
adva = _Adva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1)
)
_Metro1500_ObjectIdentity = ObjectIdentity
metro1500 = _Metro1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3)
)
_Metro1500Main_ObjectIdentity = ObjectIdentity
metro1500Main = _Metro1500Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1)
)
_Metro1500Housing_ObjectIdentity = ObjectIdentity
metro1500Housing = _Metro1500Housing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1)
)
_Metro1500Manufacturer_Type = DisplayString
_Metro1500Manufacturer_Object = MibScalar
metro1500Manufacturer = _Metro1500Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 1),
    _Metro1500Manufacturer_Type()
)
metro1500Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500Manufacturer.setStatus("mandatory")
_Metro1500MainType_Type = DisplayString
_Metro1500MainType_Object = MibScalar
metro1500MainType = _Metro1500MainType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 2),
    _Metro1500MainType_Type()
)
metro1500MainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainType.setStatus("mandatory")
_Metro1500MainSerialNumber_Type = DisplayString
_Metro1500MainSerialNumber_Object = MibScalar
metro1500MainSerialNumber = _Metro1500MainSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 3),
    _Metro1500MainSerialNumber_Type()
)
metro1500MainSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainSerialNumber.setStatus("mandatory")
_Metro1500MainHardwareVersion_Type = DisplayString
_Metro1500MainHardwareVersion_Object = MibScalar
metro1500MainHardwareVersion = _Metro1500MainHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 4),
    _Metro1500MainHardwareVersion_Type()
)
metro1500MainHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainHardwareVersion.setStatus("mandatory")
_Metro1500MainSoftwareVersion_Type = DisplayString
_Metro1500MainSoftwareVersion_Object = MibScalar
metro1500MainSoftwareVersion = _Metro1500MainSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 5),
    _Metro1500MainSoftwareVersion_Type()
)
metro1500MainSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainSoftwareVersion.setStatus("mandatory")
_Metro1500MainBusMessages_Type = Integer32
_Metro1500MainBusMessages_Object = MibScalar
metro1500MainBusMessages = _Metro1500MainBusMessages_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 6),
    _Metro1500MainBusMessages_Type()
)
metro1500MainBusMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainBusMessages.setStatus("mandatory")
_Metro1500MainBusErrors_Type = Integer32
_Metro1500MainBusErrors_Object = MibScalar
metro1500MainBusErrors = _Metro1500MainBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 7),
    _Metro1500MainBusErrors_Type()
)
metro1500MainBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainBusErrors.setStatus("mandatory")


class _Metro1500MainLastEvent_Type(Integer32):
    """Custom type metro1500MainLastEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Metro1500MainLastEvent_Type.__name__ = "Integer32"
_Metro1500MainLastEvent_Object = MibScalar
metro1500MainLastEvent = _Metro1500MainLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 8),
    _Metro1500MainLastEvent_Type()
)
metro1500MainLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLastEvent.setStatus("mandatory")
_Metro1500MainMotd_Type = DisplayString
_Metro1500MainMotd_Object = MibScalar
metro1500MainMotd = _Metro1500MainMotd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 9),
    _Metro1500MainMotd_Type()
)
metro1500MainMotd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainMotd.setStatus("mandatory")
_Metro1500MainTrapsinkTable_Object = MibTable
metro1500MainTrapsinkTable = _Metro1500MainTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    metro1500MainTrapsinkTable.setStatus("mandatory")
_Metro1500MainTrapsinkEntry_Object = MibTableRow
metro1500MainTrapsinkEntry = _Metro1500MainTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1)
)
metro1500MainTrapsinkEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500MainTrapsinkNumber"),
)
if mibBuilder.loadTexts:
    metro1500MainTrapsinkEntry.setStatus("mandatory")


class _Metro1500MainTrapsinkNumber_Type(Integer32):
    """Custom type metro1500MainTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Metro1500MainTrapsinkNumber_Type.__name__ = "Integer32"
_Metro1500MainTrapsinkNumber_Object = MibTableColumn
metro1500MainTrapsinkNumber = _Metro1500MainTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 1),
    _Metro1500MainTrapsinkNumber_Type()
)
metro1500MainTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkNumber.setStatus("mandatory")
_Metro1500MainTrapsinkAddress_Type = DisplayString
_Metro1500MainTrapsinkAddress_Object = MibTableColumn
metro1500MainTrapsinkAddress = _Metro1500MainTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 2),
    _Metro1500MainTrapsinkAddress_Type()
)
metro1500MainTrapsinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkAddress.setStatus("mandatory")
_Metro1500MainTrapsinkCommunity_Type = DisplayString
_Metro1500MainTrapsinkCommunity_Object = MibTableColumn
metro1500MainTrapsinkCommunity = _Metro1500MainTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 3),
    _Metro1500MainTrapsinkCommunity_Type()
)
metro1500MainTrapsinkCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkCommunity.setStatus("mandatory")


class _Metro1500MainTrapsinkPriority_Type(Integer32):
    """Custom type metro1500MainTrapsinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Metro1500MainTrapsinkPriority_Type.__name__ = "Integer32"
_Metro1500MainTrapsinkPriority_Object = MibTableColumn
metro1500MainTrapsinkPriority = _Metro1500MainTrapsinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 4),
    _Metro1500MainTrapsinkPriority_Type()
)
metro1500MainTrapsinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkPriority.setStatus("mandatory")
_Metro1500MainLogfileTable_Object = MibTable
metro1500MainLogfileTable = _Metro1500MainLogfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    metro1500MainLogfileTable.setStatus("mandatory")
_Metro1500MainLogfileEntry_Object = MibTableRow
metro1500MainLogfileEntry = _Metro1500MainLogfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1)
)
metro1500MainLogfileEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500MainLogfileNumber"),
)
if mibBuilder.loadTexts:
    metro1500MainLogfileEntry.setStatus("mandatory")


class _Metro1500MainLogfileNumber_Type(Integer32):
    """Custom type metro1500MainLogfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Metro1500MainLogfileNumber_Type.__name__ = "Integer32"
_Metro1500MainLogfileNumber_Object = MibTableColumn
metro1500MainLogfileNumber = _Metro1500MainLogfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 1),
    _Metro1500MainLogfileNumber_Type()
)
metro1500MainLogfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfileNumber.setStatus("mandatory")
_Metro1500MainLogfileName_Type = DisplayString
_Metro1500MainLogfileName_Object = MibTableColumn
metro1500MainLogfileName = _Metro1500MainLogfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 2),
    _Metro1500MainLogfileName_Type()
)
metro1500MainLogfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfileName.setStatus("mandatory")
_Metro1500MainLogfileSize_Type = Integer32
_Metro1500MainLogfileSize_Object = MibTableColumn
metro1500MainLogfileSize = _Metro1500MainLogfileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 3),
    _Metro1500MainLogfileSize_Type()
)
metro1500MainLogfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfileSize.setStatus("mandatory")


class _Metro1500MainLogfilePriority_Type(Integer32):
    """Custom type metro1500MainLogfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Metro1500MainLogfilePriority_Type.__name__ = "Integer32"
_Metro1500MainLogfilePriority_Object = MibTableColumn
metro1500MainLogfilePriority = _Metro1500MainLogfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 4),
    _Metro1500MainLogfilePriority_Type()
)
metro1500MainLogfilePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfilePriority.setStatus("mandatory")


class _Metro1500MainProtocolVersion_Type(Integer32):
    """Custom type metro1500MainProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_Metro1500MainProtocolVersion_Type.__name__ = "Integer32"
_Metro1500MainProtocolVersion_Object = MibScalar
metro1500MainProtocolVersion = _Metro1500MainProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 12),
    _Metro1500MainProtocolVersion_Type()
)
metro1500MainProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainProtocolVersion.setStatus("mandatory")


class _Metro1500MainSystemVersion_Type(Integer32):
    """Custom type metro1500MainSystemVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknownSystem", 1),
          ("metro1000", 2),
          ("metro1500", 3),
          ("metro2000", 4))
    )


_Metro1500MainSystemVersion_Type.__name__ = "Integer32"
_Metro1500MainSystemVersion_Object = MibScalar
metro1500MainSystemVersion = _Metro1500MainSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 13),
    _Metro1500MainSystemVersion_Type()
)
metro1500MainSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainSystemVersion.setStatus("mandatory")
_Metro1500MainConfigMismatch_Type = Integer32
_Metro1500MainConfigMismatch_Object = MibScalar
metro1500MainConfigMismatch = _Metro1500MainConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 14),
    _Metro1500MainConfigMismatch_Type()
)
metro1500MainConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainConfigMismatch.setStatus("mandatory")


class _Metro1500MainLastAuthFailSource_Type(Integer32):
    """Custom type metro1500MainLastAuthFailSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("snmp_agent", 1),
          ("login_cmd", 2),
          ("su_cmd", 3),
          ("no_fail", 4))
    )


_Metro1500MainLastAuthFailSource_Type.__name__ = "Integer32"
_Metro1500MainLastAuthFailSource_Object = MibScalar
metro1500MainLastAuthFailSource = _Metro1500MainLastAuthFailSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 15),
    _Metro1500MainLastAuthFailSource_Type()
)
metro1500MainLastAuthFailSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLastAuthFailSource.setStatus("mandatory")
_Metro1500MainLastAuthFailDescription_Type = DisplayString
_Metro1500MainLastAuthFailDescription_Object = MibScalar
metro1500MainLastAuthFailDescription = _Metro1500MainLastAuthFailDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 16),
    _Metro1500MainLastAuthFailDescription_Type()
)
metro1500MainLastAuthFailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLastAuthFailDescription.setStatus("mandatory")
_Metro1500SlotTable_Object = MibTable
metro1500SlotTable = _Metro1500SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    metro1500SlotTable.setStatus("mandatory")
_Metro1500SlotEntry_Object = MibTableRow
metro1500SlotEntry = _Metro1500SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1)
)
metro1500SlotEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500SlotNumber"),
)
if mibBuilder.loadTexts:
    metro1500SlotEntry.setStatus("mandatory")
_Metro1500SlotNumber_Type = Metro1500SlotNumberRange
_Metro1500SlotNumber_Object = MibTableColumn
metro1500SlotNumber = _Metro1500SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 1),
    _Metro1500SlotNumber_Type()
)
metro1500SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SlotNumber.setStatus("mandatory")
_Metro1500Type_Type = DisplayString
_Metro1500Type_Object = MibTableColumn
metro1500Type = _Metro1500Type_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 2),
    _Metro1500Type_Type()
)
metro1500Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500Type.setStatus("mandatory")


class _Metro1500SlotTypeNumber_Type(Integer32):
    """Custom type metro1500SlotTypeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              7,
              10,
              13,
              14,
              20,
              32,
              33,
              39,
              64,
              66,
              67,
              68,
              69,
              136,
              137,
              138,
              139,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hotStandbyConverter", 0),
          ("metro1500Converter", 1),
          ("metro1000Converter", 2),
          ("metro1000EthernetConverter", 3),
          ("metro1500-2_5GBitConverter", 5),
          ("metro1500TRL_Converter", 7),
          ("metro1500-4PortTDMCard", 10),
          ("metro1500HotStandby_Converter", 13),
          ("metro1500-4PortTDMCard_MC", 14),
          ("metro15008PortTDMCard_MC", 20),
          ("nemi", 32),
          ("demi", 33),
          ("metro1500EthernetHubCard", 39),
          ("switch", 64),
          ("metro1500RSM_OSC", 66),
          ("metro1500RSM", 67),
          ("metro1500OSC_single", 68),
          ("metro1500SingleFiberSwitch", 69),
          ("metro1500MUX_DMX", 136),
          ("metro1500MUX", 137),
          ("metro1500DMX", 138),
          ("metro1500BSM", 139),
          ("other", 255))
    )


_Metro1500SlotTypeNumber_Type.__name__ = "Integer32"
_Metro1500SlotTypeNumber_Object = MibTableColumn
metro1500SlotTypeNumber = _Metro1500SlotTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 3),
    _Metro1500SlotTypeNumber_Type()
)
metro1500SlotTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SlotTypeNumber.setStatus("mandatory")
_Metro1500SerialNumber_Type = DisplayString
_Metro1500SerialNumber_Object = MibTableColumn
metro1500SerialNumber = _Metro1500SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 4),
    _Metro1500SerialNumber_Type()
)
metro1500SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SerialNumber.setStatus("mandatory")
_Metro1500HardwareVersion_Type = DisplayString
_Metro1500HardwareVersion_Object = MibTableColumn
metro1500HardwareVersion = _Metro1500HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 5),
    _Metro1500HardwareVersion_Type()
)
metro1500HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500HardwareVersion.setStatus("mandatory")
_Metro1500SoftwareVersion_Type = DisplayString
_Metro1500SoftwareVersion_Object = MibTableColumn
metro1500SoftwareVersion = _Metro1500SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 6),
    _Metro1500SoftwareVersion_Type()
)
metro1500SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SoftwareVersion.setStatus("mandatory")
_Metro1500Temperature_Type = Integer32
_Metro1500Temperature_Object = MibTableColumn
metro1500Temperature = _Metro1500Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 7),
    _Metro1500Temperature_Type()
)
metro1500Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500Temperature.setStatus("mandatory")
_Metro1500BoardVoltage_Type = Integer32
_Metro1500BoardVoltage_Object = MibTableColumn
metro1500BoardVoltage = _Metro1500BoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 8),
    _Metro1500BoardVoltage_Type()
)
metro1500BoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500BoardVoltage.setStatus("mandatory")
_Metro1500DetailInfo_Type = ObjectIdentifier
_Metro1500DetailInfo_Object = MibTableColumn
metro1500DetailInfo = _Metro1500DetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 9),
    _Metro1500DetailInfo_Type()
)
metro1500DetailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500DetailInfo.setStatus("mandatory")


class _Metro1500EPLDVersion_Type(Integer32):
    """Custom type metro1500EPLDVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Metro1500EPLDVersion_Type.__name__ = "Integer32"
_Metro1500EPLDVersion_Object = MibTableColumn
metro1500EPLDVersion = _Metro1500EPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 10),
    _Metro1500EPLDVersion_Type()
)
metro1500EPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EPLDVersion.setStatus("mandatory")
_Metro1500CustomerLabel_Type = DisplayString
_Metro1500CustomerLabel_Object = MibTableColumn
metro1500CustomerLabel = _Metro1500CustomerLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 11),
    _Metro1500CustomerLabel_Type()
)
metro1500CustomerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500CustomerLabel.setStatus("mandatory")
_Metro1500ProductionVersion_Type = DisplayString
_Metro1500ProductionVersion_Object = MibTableColumn
metro1500ProductionVersion = _Metro1500ProductionVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 12),
    _Metro1500ProductionVersion_Type()
)
metro1500ProductionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ProductionVersion.setStatus("mandatory")


class _Metro1500SlotSubType_Type(Integer32):
    """Custom type metro1500SlotSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("couplingLink", 2),
          ("regeneratorCapable", 3))
    )


_Metro1500SlotSubType_Type.__name__ = "Integer32"
_Metro1500SlotSubType_Object = MibTableColumn
metro1500SlotSubType = _Metro1500SlotSubType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 13),
    _Metro1500SlotSubType_Type()
)
metro1500SlotSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SlotSubType.setStatus("mandatory")
_Metro1500SlotAlias_Type = DisplayString
_Metro1500SlotAlias_Object = MibTableColumn
metro1500SlotAlias = _Metro1500SlotAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 14),
    _Metro1500SlotAlias_Type()
)
metro1500SlotAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SlotAlias.setStatus("mandatory")
_Metro1500SlotComment_Type = DisplayString
_Metro1500SlotComment_Object = MibTableColumn
metro1500SlotComment = _Metro1500SlotComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 15),
    _Metro1500SlotComment_Type()
)
metro1500SlotComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SlotComment.setStatus("mandatory")
_Metro1500PSTable_Object = MibTable
metro1500PSTable = _Metro1500PSTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    metro1500PSTable.setStatus("mandatory")
_Metro1500PSEntry_Object = MibTableRow
metro1500PSEntry = _Metro1500PSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1)
)
metro1500PSEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500PSNumber"),
)
if mibBuilder.loadTexts:
    metro1500PSEntry.setStatus("mandatory")


class _Metro1500PSNumber_Type(Integer32):
    """Custom type metro1500PSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Metro1500PSNumber_Type.__name__ = "Integer32"
_Metro1500PSNumber_Object = MibTableColumn
metro1500PSNumber = _Metro1500PSNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 1),
    _Metro1500PSNumber_Type()
)
metro1500PSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500PSNumber.setStatus("mandatory")


class _Metro1500PSOn_Type(Integer32):
    """Custom type metro1500PSOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500PSOn_Type.__name__ = "Integer32"
_Metro1500PSOn_Object = MibTableColumn
metro1500PSOn = _Metro1500PSOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 2),
    _Metro1500PSOn_Type()
)
metro1500PSOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500PSOn.setStatus("mandatory")
_Metro1500FanTable_Object = MibTable
metro1500FanTable = _Metro1500FanTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    metro1500FanTable.setStatus("mandatory")
_Metro1500FanEntry_Object = MibTableRow
metro1500FanEntry = _Metro1500FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1)
)
metro1500FanEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500FanNumber"),
)
if mibBuilder.loadTexts:
    metro1500FanEntry.setStatus("mandatory")


class _Metro1500FanNumber_Type(Integer32):
    """Custom type metro1500FanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Metro1500FanNumber_Type.__name__ = "Integer32"
_Metro1500FanNumber_Object = MibTableColumn
metro1500FanNumber = _Metro1500FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 1),
    _Metro1500FanNumber_Type()
)
metro1500FanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500FanNumber.setStatus("mandatory")


class _Metro1500FanOn_Type(Integer32):
    """Custom type metro1500FanOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500FanOn_Type.__name__ = "Integer32"
_Metro1500FanOn_Object = MibTableColumn
metro1500FanOn = _Metro1500FanOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 2),
    _Metro1500FanOn_Type()
)
metro1500FanOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500FanOn.setStatus("mandatory")
_Metro1500Converter_ObjectIdentity = ObjectIdentity
metro1500Converter = _Metro1500Converter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5)
)
_Metro1500ConverterTable_Object = MibTable
metro1500ConverterTable = _Metro1500ConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    metro1500ConverterTable.setStatus("mandatory")
_Metro1500ConverterEntry_Object = MibTableRow
metro1500ConverterEntry = _Metro1500ConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1)
)
metro1500ConverterEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500ConverterNumber"),
)
if mibBuilder.loadTexts:
    metro1500ConverterEntry.setStatus("mandatory")
_Metro1500ConverterNumber_Type = Metro1500SlotNumberRange
_Metro1500ConverterNumber_Object = MibTableColumn
metro1500ConverterNumber = _Metro1500ConverterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 1),
    _Metro1500ConverterNumber_Type()
)
metro1500ConverterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ConverterNumber.setStatus("mandatory")


class _Metro1500RxLoc_Type(Integer32):
    """Custom type metro1500RxLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500RxLoc_Type.__name__ = "Integer32"
_Metro1500RxLoc_Object = MibTableColumn
metro1500RxLoc = _Metro1500RxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 2),
    _Metro1500RxLoc_Type()
)
metro1500RxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RxLoc.setStatus("mandatory")


class _Metro1500TxLoc_Type(Integer32):
    """Custom type metro1500TxLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TxLoc_Type.__name__ = "Integer32"
_Metro1500TxLoc_Object = MibTableColumn
metro1500TxLoc = _Metro1500TxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 3),
    _Metro1500TxLoc_Type()
)
metro1500TxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxLoc.setStatus("mandatory")


class _Metro1500TxLocC_Type(Integer32):
    """Custom type metro1500TxLocC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Metro1500TxLocC_Type.__name__ = "Integer32"
_Metro1500TxLocC_Object = MibTableColumn
metro1500TxLocC = _Metro1500TxLocC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 4),
    _Metro1500TxLocC_Type()
)
metro1500TxLocC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxLocC.setStatus("mandatory")


class _Metro1500TxLocTemp_Type(Integer32):
    """Custom type metro1500TxLocTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Metro1500TxLocTemp_Type.__name__ = "Integer32"
_Metro1500TxLocTemp_Object = MibTableColumn
metro1500TxLocTemp = _Metro1500TxLocTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 5),
    _Metro1500TxLocTemp_Type()
)
metro1500TxLocTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxLocTemp.setStatus("mandatory")


class _Metro1500RxRem_Type(Integer32):
    """Custom type metro1500RxRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500RxRem_Type.__name__ = "Integer32"
_Metro1500RxRem_Object = MibTableColumn
metro1500RxRem = _Metro1500RxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 6),
    _Metro1500RxRem_Type()
)
metro1500RxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RxRem.setStatus("mandatory")


class _Metro1500TxRem_Type(Integer32):
    """Custom type metro1500TxRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TxRem_Type.__name__ = "Integer32"
_Metro1500TxRem_Object = MibTableColumn
metro1500TxRem = _Metro1500TxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 7),
    _Metro1500TxRem_Type()
)
metro1500TxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxRem.setStatus("mandatory")


class _Metro1500TxRemC_Type(Integer32):
    """Custom type metro1500TxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Metro1500TxRemC_Type.__name__ = "Integer32"
_Metro1500TxRemC_Object = MibTableColumn
metro1500TxRemC = _Metro1500TxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 8),
    _Metro1500TxRemC_Type()
)
metro1500TxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxRemC.setStatus("mandatory")


class _Metro1500TxRemTemp_Type(Integer32):
    """Custom type metro1500TxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Metro1500TxRemTemp_Type.__name__ = "Integer32"
_Metro1500TxRemTemp_Object = MibTableColumn
metro1500TxRemTemp = _Metro1500TxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 9),
    _Metro1500TxRemTemp_Type()
)
metro1500TxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxRemTemp.setStatus("mandatory")


class _Metro1500RxRem2_Type(Integer32):
    """Custom type metro1500RxRem2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500RxRem2_Type.__name__ = "Integer32"
_Metro1500RxRem2_Object = MibTableColumn
metro1500RxRem2 = _Metro1500RxRem2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 10),
    _Metro1500RxRem2_Type()
)
metro1500RxRem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RxRem2.setStatus("mandatory")


class _Metro1500ClockState_Type(Integer32):
    """Custom type metro1500ClockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("fail", 3))
    )


_Metro1500ClockState_Type.__name__ = "Integer32"
_Metro1500ClockState_Object = MibTableColumn
metro1500ClockState = _Metro1500ClockState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 11),
    _Metro1500ClockState_Type()
)
metro1500ClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ClockState.setStatus("mandatory")
_Metro1500ClockFreq_Type = Integer32
_Metro1500ClockFreq_Object = MibTableColumn
metro1500ClockFreq = _Metro1500ClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 12),
    _Metro1500ClockFreq_Type()
)
metro1500ClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ClockFreq.setStatus("mandatory")


class _Metro1500LocLoop_Type(Integer32):
    """Custom type metro1500LocLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500LocLoop_Type.__name__ = "Integer32"
_Metro1500LocLoop_Object = MibTableColumn
metro1500LocLoop = _Metro1500LocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 13),
    _Metro1500LocLoop_Type()
)
metro1500LocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500LocLoop.setStatus("mandatory")


class _Metro1500RemLoop_Type(Integer32):
    """Custom type metro1500RemLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500RemLoop_Type.__name__ = "Integer32"
_Metro1500RemLoop_Object = MibTableColumn
metro1500RemLoop = _Metro1500RemLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 14),
    _Metro1500RemLoop_Type()
)
metro1500RemLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RemLoop.setStatus("mandatory")


class _Metro1500ClockType_Type(Integer32):
    """Custom type metro1500ClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              9,
              11,
              12,
              18,
              21,
              22,
              31,
              32,
              41,
              42,
              51,
              52,
              61,
              62,
              71,
              72,
              75,
              76,
              81,
              82,
              255)
        )
    )
    namedValues = NamedValues(
        *(("multiClockLSModule", 1),
          ("multiClockLS", 2),
          ("multiClockFCGbE", 3),
          ("multiClockOCxGbE", 5),
          ("multiClockOCxFC", 7),
          ("multiClockOCxGbEFC", 9),
          ("multiClockFCGbEOnBoard", 11),
          ("multiClockFC", 12),
          ("multiClock3LS", 18),
          ("fixedClock125MbpsModule", 21),
          ("fixedClock125Mbps", 22),
          ("fixedClock155MbpsModule", 31),
          ("fixedClock155Mbps", 32),
          ("fixedClock200MbpsModule", 41),
          ("fixedClock200Mbps", 42),
          ("fixedClock266MbpsModule", 51),
          ("fixedClock266Mbps", 52),
          ("fixedClock622MbpsModule", 61),
          ("fixedClock622Mbps", 62),
          ("fixedClock1062MbpsModule", 71),
          ("fixedClock1062Mbps", 72),
          ("fixedClock1250MbpsModule", 75),
          ("fixedClock1250Mbps", 76),
          ("fixedClock2500MbpsModule", 81),
          ("fixedClock2500Mbps", 82),
          ("other", 255))
    )


_Metro1500ClockType_Type.__name__ = "Integer32"
_Metro1500ClockType_Object = MibTableColumn
metro1500ClockType = _Metro1500ClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 15),
    _Metro1500ClockType_Type()
)
metro1500ClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ClockType.setStatus("mandatory")


class _Metro1500HotStandby_ActiveLine_Type(Integer32):
    """Custom type metro1500HotStandby_ActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineA", 1),
          ("lineB", 2),
          ("invalid", 3))
    )


_Metro1500HotStandby_ActiveLine_Type.__name__ = "Integer32"
_Metro1500HotStandby_ActiveLine_Object = MibTableColumn
metro1500HotStandby_ActiveLine = _Metro1500HotStandby_ActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 16),
    _Metro1500HotStandby_ActiveLine_Type()
)
metro1500HotStandby_ActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500HotStandby_ActiveLine.setStatus("mandatory")


class _Metro1500HotStandby_LineLocked_Type(Integer32):
    """Custom type metro1500HotStandby_LineLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("locked", 2),
          ("invalid", 3))
    )


_Metro1500HotStandby_LineLocked_Type.__name__ = "Integer32"
_Metro1500HotStandby_LineLocked_Object = MibTableColumn
metro1500HotStandby_LineLocked = _Metro1500HotStandby_LineLocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 17),
    _Metro1500HotStandby_LineLocked_Type()
)
metro1500HotStandby_LineLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500HotStandby_LineLocked.setStatus("mandatory")
_Metro1500LocalConnector_Type = DisplayString
_Metro1500LocalConnector_Object = MibTableColumn
metro1500LocalConnector = _Metro1500LocalConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 18),
    _Metro1500LocalConnector_Type()
)
metro1500LocalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500LocalConnector.setStatus("mandatory")
_Metro1500LocalLaserType_Type = DisplayString
_Metro1500LocalLaserType_Object = MibTableColumn
metro1500LocalLaserType = _Metro1500LocalLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 19),
    _Metro1500LocalLaserType_Type()
)
metro1500LocalLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500LocalLaserType.setStatus("mandatory")
_Metro1500RemoteConnector_Type = DisplayString
_Metro1500RemoteConnector_Object = MibTableColumn
metro1500RemoteConnector = _Metro1500RemoteConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 20),
    _Metro1500RemoteConnector_Type()
)
metro1500RemoteConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RemoteConnector.setStatus("mandatory")
_Metro1500RemoteLaserType_Type = DisplayString
_Metro1500RemoteLaserType_Object = MibTableColumn
metro1500RemoteLaserType = _Metro1500RemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 21),
    _Metro1500RemoteLaserType_Type()
)
metro1500RemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RemoteLaserType.setStatus("mandatory")
_Metro1500ConverterType_Type = DisplayString
_Metro1500ConverterType_Object = MibTableColumn
metro1500ConverterType = _Metro1500ConverterType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 22),
    _Metro1500ConverterType_Type()
)
metro1500ConverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ConverterType.setStatus("mandatory")
_Metro1500ClockRecovery_Type = DisplayString
_Metro1500ClockRecovery_Object = MibTableColumn
metro1500ClockRecovery = _Metro1500ClockRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 23),
    _Metro1500ClockRecovery_Type()
)
metro1500ClockRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ClockRecovery.setStatus("mandatory")
_Metro1500SupportedDataRateTransparent_Type = DisplayString
_Metro1500SupportedDataRateTransparent_Object = MibTableColumn
metro1500SupportedDataRateTransparent = _Metro1500SupportedDataRateTransparent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 24),
    _Metro1500SupportedDataRateTransparent_Type()
)
metro1500SupportedDataRateTransparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SupportedDataRateTransparent.setStatus("mandatory")
_Metro1500SupportedDataRateClocked_Type = DisplayString
_Metro1500SupportedDataRateClocked_Object = MibTableColumn
metro1500SupportedDataRateClocked = _Metro1500SupportedDataRateClocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 25),
    _Metro1500SupportedDataRateClocked_Type()
)
metro1500SupportedDataRateClocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SupportedDataRateClocked.setStatus("mandatory")


class _Metro1500ChannelNumber_Type(Integer32):
    """Custom type metro1500ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Metro1500ChannelNumber_Type.__name__ = "Integer32"
_Metro1500ChannelNumber_Object = MibTableColumn
metro1500ChannelNumber = _Metro1500ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 26),
    _Metro1500ChannelNumber_Type()
)
metro1500ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ChannelNumber.setStatus("mandatory")


class _Metro1500RemoteClockState_Type(Integer32):
    """Custom type metro1500RemoteClockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("sync", 2),
          ("noSync", 3))
    )


_Metro1500RemoteClockState_Type.__name__ = "Integer32"
_Metro1500RemoteClockState_Object = MibTableColumn
metro1500RemoteClockState = _Metro1500RemoteClockState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 27),
    _Metro1500RemoteClockState_Type()
)
metro1500RemoteClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RemoteClockState.setStatus("mandatory")


class _Metro1500RemoteClockState2_Type(Integer32):
    """Custom type metro1500RemoteClockState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("sync", 2),
          ("noSync", 3))
    )


_Metro1500RemoteClockState2_Type.__name__ = "Integer32"
_Metro1500RemoteClockState2_Object = MibTableColumn
metro1500RemoteClockState2 = _Metro1500RemoteClockState2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 28),
    _Metro1500RemoteClockState2_Type()
)
metro1500RemoteClockState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RemoteClockState2.setStatus("mandatory")


class _Metro1500RegeneratorMode_Type(Integer32):
    """Custom type metro1500RegeneratorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("on", 2),
          ("off", 3))
    )


_Metro1500RegeneratorMode_Type.__name__ = "Integer32"
_Metro1500RegeneratorMode_Object = MibTableColumn
metro1500RegeneratorMode = _Metro1500RegeneratorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 29),
    _Metro1500RegeneratorMode_Type()
)
metro1500RegeneratorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RegeneratorMode.setStatus("mandatory")
_Metro1500Switch_ObjectIdentity = ObjectIdentity
metro1500Switch = _Metro1500Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10)
)
_Metro1500SwitchTable_Object = MibTable
metro1500SwitchTable = _Metro1500SwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    metro1500SwitchTable.setStatus("mandatory")
_Metro1500SwitchEntry_Object = MibTableRow
metro1500SwitchEntry = _Metro1500SwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1)
)
metro1500SwitchEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500SwitchNumber"),
)
if mibBuilder.loadTexts:
    metro1500SwitchEntry.setStatus("mandatory")
_Metro1500SwitchNumber_Type = Metro1500SlotNumberRange
_Metro1500SwitchNumber_Object = MibTableColumn
metro1500SwitchNumber = _Metro1500SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 1),
    _Metro1500SwitchNumber_Type()
)
metro1500SwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchNumber.setStatus("mandatory")


class _Metro1500SwitchLine_Type(Integer32):
    """Custom type metro1500SwitchLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineA", 1),
          ("lineB", 2))
    )


_Metro1500SwitchLine_Type.__name__ = "Integer32"
_Metro1500SwitchLine_Object = MibTableColumn
metro1500SwitchLine = _Metro1500SwitchLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 2),
    _Metro1500SwitchLine_Type()
)
metro1500SwitchLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLine.setStatus("mandatory")


class _Metro1500SwitchMode_Type(Integer32):
    """Custom type metro1500SwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("locked", 2))
    )


_Metro1500SwitchMode_Type.__name__ = "Integer32"
_Metro1500SwitchMode_Object = MibTableColumn
metro1500SwitchMode = _Metro1500SwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 3),
    _Metro1500SwitchMode_Type()
)
metro1500SwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchMode.setStatus("mandatory")


class _Metro1500SwitchLaserOn_Type(Integer32):
    """Custom type metro1500SwitchLaserOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500SwitchLaserOn_Type.__name__ = "Integer32"
_Metro1500SwitchLaserOn_Object = MibTableColumn
metro1500SwitchLaserOn = _Metro1500SwitchLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 4),
    _Metro1500SwitchLaserOn_Type()
)
metro1500SwitchLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLaserOn.setStatus("mandatory")


class _Metro1500SwitchLineAavail_Type(Integer32):
    """Custom type metro1500SwitchLineAavail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_Metro1500SwitchLineAavail_Type.__name__ = "Integer32"
_Metro1500SwitchLineAavail_Object = MibTableColumn
metro1500SwitchLineAavail = _Metro1500SwitchLineAavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 5),
    _Metro1500SwitchLineAavail_Type()
)
metro1500SwitchLineAavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLineAavail.setStatus("mandatory")


class _Metro1500SwitchLineBavail_Type(Integer32):
    """Custom type metro1500SwitchLineBavail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_Metro1500SwitchLineBavail_Type.__name__ = "Integer32"
_Metro1500SwitchLineBavail_Object = MibTableColumn
metro1500SwitchLineBavail = _Metro1500SwitchLineBavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 6),
    _Metro1500SwitchLineBavail_Type()
)
metro1500SwitchLineBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLineBavail.setStatus("mandatory")


class _Metro1500SwitchAutoLaserShutdown_Type(Integer32):
    """Custom type metro1500SwitchAutoLaserShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("on", 2),
          ("off", 3))
    )


_Metro1500SwitchAutoLaserShutdown_Type.__name__ = "Integer32"
_Metro1500SwitchAutoLaserShutdown_Object = MibTableColumn
metro1500SwitchAutoLaserShutdown = _Metro1500SwitchAutoLaserShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 7),
    _Metro1500SwitchAutoLaserShutdown_Type()
)
metro1500SwitchAutoLaserShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchAutoLaserShutdown.setStatus("mandatory")
_Metro1500SwitchConnector_Type = DisplayString
_Metro1500SwitchConnector_Object = MibTableColumn
metro1500SwitchConnector = _Metro1500SwitchConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 10),
    _Metro1500SwitchConnector_Type()
)
metro1500SwitchConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchConnector.setStatus("mandatory")
_Metro1500SwitchRemoteLaserType_Type = DisplayString
_Metro1500SwitchRemoteLaserType_Object = MibTableColumn
metro1500SwitchRemoteLaserType = _Metro1500SwitchRemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 11),
    _Metro1500SwitchRemoteLaserType_Type()
)
metro1500SwitchRemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchRemoteLaserType.setStatus("mandatory")
_Metro1500RSM_OSC_ObjectIdentity = ObjectIdentity
metro1500RSM_OSC = _Metro1500RSM_OSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11)
)
_Metro1500RSM_Table_Object = MibTable
metro1500RSM_Table = _Metro1500RSM_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1)
)
if mibBuilder.loadTexts:
    metro1500RSM_Table.setStatus("mandatory")
_Metro1500RSM_Entry_Object = MibTableRow
metro1500RSM_Entry = _Metro1500RSM_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1)
)
metro1500RSM_Entry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500RSM_Number"),
)
if mibBuilder.loadTexts:
    metro1500RSM_Entry.setStatus("mandatory")
_Metro1500RSM_Number_Type = Metro1500SlotNumberRange
_Metro1500RSM_Number_Object = MibTableColumn
metro1500RSM_Number = _Metro1500RSM_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 1),
    _Metro1500RSM_Number_Type()
)
metro1500RSM_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_Number.setStatus("mandatory")


class _Metro1500RSM_Line_Type(Integer32):
    """Custom type metro1500RSM_Line based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineA", 1),
          ("lineB", 2))
    )


_Metro1500RSM_Line_Type.__name__ = "Integer32"
_Metro1500RSM_Line_Object = MibTableColumn
metro1500RSM_Line = _Metro1500RSM_Line_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 2),
    _Metro1500RSM_Line_Type()
)
metro1500RSM_Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_Line.setStatus("mandatory")


class _Metro1500RSM_Mode_Type(Integer32):
    """Custom type metro1500RSM_Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("locked", 2))
    )


_Metro1500RSM_Mode_Type.__name__ = "Integer32"
_Metro1500RSM_Mode_Object = MibTableColumn
metro1500RSM_Mode = _Metro1500RSM_Mode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 3),
    _Metro1500RSM_Mode_Type()
)
metro1500RSM_Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_Mode.setStatus("mandatory")


class _Metro1500RSM_LaserOn_Type(Integer32):
    """Custom type metro1500RSM_LaserOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500RSM_LaserOn_Type.__name__ = "Integer32"
_Metro1500RSM_LaserOn_Object = MibTableColumn
metro1500RSM_LaserOn = _Metro1500RSM_LaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 4),
    _Metro1500RSM_LaserOn_Type()
)
metro1500RSM_LaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_LaserOn.setStatus("mandatory")


class _Metro1500RSM_LineAavail_Type(Integer32):
    """Custom type metro1500RSM_LineAavail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_Metro1500RSM_LineAavail_Type.__name__ = "Integer32"
_Metro1500RSM_LineAavail_Object = MibTableColumn
metro1500RSM_LineAavail = _Metro1500RSM_LineAavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 5),
    _Metro1500RSM_LineAavail_Type()
)
metro1500RSM_LineAavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_LineAavail.setStatus("mandatory")


class _Metro1500RSM_LineBavail_Type(Integer32):
    """Custom type metro1500RSM_LineBavail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_Metro1500RSM_LineBavail_Type.__name__ = "Integer32"
_Metro1500RSM_LineBavail_Object = MibTableColumn
metro1500RSM_LineBavail = _Metro1500RSM_LineBavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 6),
    _Metro1500RSM_LineBavail_Type()
)
metro1500RSM_LineBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_LineBavail.setStatus("mandatory")


class _Metro1500RSM_Control_Type(Integer32):
    """Custom type metro1500RSM_Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500RSM_Control_Type.__name__ = "Integer32"
_Metro1500RSM_Control_Object = MibTableColumn
metro1500RSM_Control = _Metro1500RSM_Control_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 7),
    _Metro1500RSM_Control_Type()
)
metro1500RSM_Control.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_Control.setStatus("mandatory")
_Metro1500RSM_Connector_Type = DisplayString
_Metro1500RSM_Connector_Object = MibTableColumn
metro1500RSM_Connector = _Metro1500RSM_Connector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 8),
    _Metro1500RSM_Connector_Type()
)
metro1500RSM_Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_Connector.setStatus("mandatory")
_Metro1500RSM_RemoteLaserType_Type = DisplayString
_Metro1500RSM_RemoteLaserType_Object = MibTableColumn
metro1500RSM_RemoteLaserType = _Metro1500RSM_RemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 9),
    _Metro1500RSM_RemoteLaserType_Type()
)
metro1500RSM_RemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RSM_RemoteLaserType.setStatus("mandatory")
_Metro1500OSC_Table_Object = MibTable
metro1500OSC_Table = _Metro1500OSC_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2)
)
if mibBuilder.loadTexts:
    metro1500OSC_Table.setStatus("mandatory")
_Metro1500OSC_Entry_Object = MibTableRow
metro1500OSC_Entry = _Metro1500OSC_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1)
)
metro1500OSC_Entry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500OSC_Number"),
)
if mibBuilder.loadTexts:
    metro1500OSC_Entry.setStatus("mandatory")
_Metro1500OSC_Number_Type = Metro1500SlotNumberRange
_Metro1500OSC_Number_Object = MibTableColumn
metro1500OSC_Number = _Metro1500OSC_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 1),
    _Metro1500OSC_Number_Type()
)
metro1500OSC_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_Number.setStatus("mandatory")


class _Metro1500OSC_LaserOn_Type(Integer32):
    """Custom type metro1500OSC_LaserOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500OSC_LaserOn_Type.__name__ = "Integer32"
_Metro1500OSC_LaserOn_Object = MibTableColumn
metro1500OSC_LaserOn = _Metro1500OSC_LaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 2),
    _Metro1500OSC_LaserOn_Type()
)
metro1500OSC_LaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_LaserOn.setStatus("mandatory")


class _Metro1500OSC_P1_fail_Type(Integer32):
    """Custom type metro1500OSC_P1_fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2))
    )


_Metro1500OSC_P1_fail_Type.__name__ = "Integer32"
_Metro1500OSC_P1_fail_Object = MibTableColumn
metro1500OSC_P1_fail = _Metro1500OSC_P1_fail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 3),
    _Metro1500OSC_P1_fail_Type()
)
metro1500OSC_P1_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_P1_fail.setStatus("mandatory")


class _Metro1500OSC_P2_fail_Type(Integer32):
    """Custom type metro1500OSC_P2_fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2))
    )


_Metro1500OSC_P2_fail_Type.__name__ = "Integer32"
_Metro1500OSC_P2_fail_Object = MibTableColumn
metro1500OSC_P2_fail = _Metro1500OSC_P2_fail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 4),
    _Metro1500OSC_P2_fail_Type()
)
metro1500OSC_P2_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_P2_fail.setStatus("mandatory")


class _Metro1500OSC_PortEnable1_Type(Integer32):
    """Custom type metro1500OSC_PortEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500OSC_PortEnable1_Type.__name__ = "Integer32"
_Metro1500OSC_PortEnable1_Object = MibTableColumn
metro1500OSC_PortEnable1 = _Metro1500OSC_PortEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 10),
    _Metro1500OSC_PortEnable1_Type()
)
metro1500OSC_PortEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortEnable1.setStatus("mandatory")


class _Metro1500OSC_PortSpeed1_Type(Integer32):
    """Custom type metro1500OSC_PortSpeed1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2))
    )


_Metro1500OSC_PortSpeed1_Type.__name__ = "Integer32"
_Metro1500OSC_PortSpeed1_Object = MibTableColumn
metro1500OSC_PortSpeed1 = _Metro1500OSC_PortSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 11),
    _Metro1500OSC_PortSpeed1_Type()
)
metro1500OSC_PortSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortSpeed1.setStatus("mandatory")


class _Metro1500OSC_PortDuplex1_Type(Integer32):
    """Custom type metro1500OSC_PortDuplex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_Metro1500OSC_PortDuplex1_Type.__name__ = "Integer32"
_Metro1500OSC_PortDuplex1_Object = MibTableColumn
metro1500OSC_PortDuplex1 = _Metro1500OSC_PortDuplex1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 12),
    _Metro1500OSC_PortDuplex1_Type()
)
metro1500OSC_PortDuplex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortDuplex1.setStatus("mandatory")


class _Metro1500OSC_PortAutoneg1_Type(Integer32):
    """Custom type metro1500OSC_PortAutoneg1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500OSC_PortAutoneg1_Type.__name__ = "Integer32"
_Metro1500OSC_PortAutoneg1_Object = MibTableColumn
metro1500OSC_PortAutoneg1 = _Metro1500OSC_PortAutoneg1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 13),
    _Metro1500OSC_PortAutoneg1_Type()
)
metro1500OSC_PortAutoneg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortAutoneg1.setStatus("mandatory")


class _Metro1500OSC_PortPolarity1_Type(Integer32):
    """Custom type metro1500OSC_PortPolarity1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500OSC_PortPolarity1_Type.__name__ = "Integer32"
_Metro1500OSC_PortPolarity1_Object = MibTableColumn
metro1500OSC_PortPolarity1 = _Metro1500OSC_PortPolarity1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 14),
    _Metro1500OSC_PortPolarity1_Type()
)
metro1500OSC_PortPolarity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortPolarity1.setStatus("mandatory")


class _Metro1500OSC_PortLinkStatus1_Type(Integer32):
    """Custom type metro1500OSC_PortLinkStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500OSC_PortLinkStatus1_Type.__name__ = "Integer32"
_Metro1500OSC_PortLinkStatus1_Object = MibTableColumn
metro1500OSC_PortLinkStatus1 = _Metro1500OSC_PortLinkStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 15),
    _Metro1500OSC_PortLinkStatus1_Type()
)
metro1500OSC_PortLinkStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortLinkStatus1.setStatus("mandatory")


class _Metro1500OSC_PortEnable2_Type(Integer32):
    """Custom type metro1500OSC_PortEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500OSC_PortEnable2_Type.__name__ = "Integer32"
_Metro1500OSC_PortEnable2_Object = MibTableColumn
metro1500OSC_PortEnable2 = _Metro1500OSC_PortEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 20),
    _Metro1500OSC_PortEnable2_Type()
)
metro1500OSC_PortEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortEnable2.setStatus("mandatory")


class _Metro1500OSC_PortSpeed2_Type(Integer32):
    """Custom type metro1500OSC_PortSpeed2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2))
    )


_Metro1500OSC_PortSpeed2_Type.__name__ = "Integer32"
_Metro1500OSC_PortSpeed2_Object = MibTableColumn
metro1500OSC_PortSpeed2 = _Metro1500OSC_PortSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 21),
    _Metro1500OSC_PortSpeed2_Type()
)
metro1500OSC_PortSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortSpeed2.setStatus("mandatory")


class _Metro1500OSC_PortDuplex2_Type(Integer32):
    """Custom type metro1500OSC_PortDuplex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_Metro1500OSC_PortDuplex2_Type.__name__ = "Integer32"
_Metro1500OSC_PortDuplex2_Object = MibTableColumn
metro1500OSC_PortDuplex2 = _Metro1500OSC_PortDuplex2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 22),
    _Metro1500OSC_PortDuplex2_Type()
)
metro1500OSC_PortDuplex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortDuplex2.setStatus("mandatory")


class _Metro1500OSC_PortAutoneg2_Type(Integer32):
    """Custom type metro1500OSC_PortAutoneg2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500OSC_PortAutoneg2_Type.__name__ = "Integer32"
_Metro1500OSC_PortAutoneg2_Object = MibTableColumn
metro1500OSC_PortAutoneg2 = _Metro1500OSC_PortAutoneg2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 23),
    _Metro1500OSC_PortAutoneg2_Type()
)
metro1500OSC_PortAutoneg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortAutoneg2.setStatus("mandatory")


class _Metro1500OSC_PortPolarity2_Type(Integer32):
    """Custom type metro1500OSC_PortPolarity2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500OSC_PortPolarity2_Type.__name__ = "Integer32"
_Metro1500OSC_PortPolarity2_Object = MibTableColumn
metro1500OSC_PortPolarity2 = _Metro1500OSC_PortPolarity2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 24),
    _Metro1500OSC_PortPolarity2_Type()
)
metro1500OSC_PortPolarity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortPolarity2.setStatus("mandatory")


class _Metro1500OSC_PortLinkStatus2_Type(Integer32):
    """Custom type metro1500OSC_PortLinkStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500OSC_PortLinkStatus2_Type.__name__ = "Integer32"
_Metro1500OSC_PortLinkStatus2_Object = MibTableColumn
metro1500OSC_PortLinkStatus2 = _Metro1500OSC_PortLinkStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 25),
    _Metro1500OSC_PortLinkStatus2_Type()
)
metro1500OSC_PortLinkStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortLinkStatus2.setStatus("mandatory")


class _Metro1500OSC_PortEnable3_Type(Integer32):
    """Custom type metro1500OSC_PortEnable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500OSC_PortEnable3_Type.__name__ = "Integer32"
_Metro1500OSC_PortEnable3_Object = MibTableColumn
metro1500OSC_PortEnable3 = _Metro1500OSC_PortEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 30),
    _Metro1500OSC_PortEnable3_Type()
)
metro1500OSC_PortEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortEnable3.setStatus("mandatory")


class _Metro1500OSC_PortSpeed3_Type(Integer32):
    """Custom type metro1500OSC_PortSpeed3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2))
    )


_Metro1500OSC_PortSpeed3_Type.__name__ = "Integer32"
_Metro1500OSC_PortSpeed3_Object = MibTableColumn
metro1500OSC_PortSpeed3 = _Metro1500OSC_PortSpeed3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 31),
    _Metro1500OSC_PortSpeed3_Type()
)
metro1500OSC_PortSpeed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortSpeed3.setStatus("mandatory")


class _Metro1500OSC_PortDuplex3_Type(Integer32):
    """Custom type metro1500OSC_PortDuplex3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_Metro1500OSC_PortDuplex3_Type.__name__ = "Integer32"
_Metro1500OSC_PortDuplex3_Object = MibTableColumn
metro1500OSC_PortDuplex3 = _Metro1500OSC_PortDuplex3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 32),
    _Metro1500OSC_PortDuplex3_Type()
)
metro1500OSC_PortDuplex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortDuplex3.setStatus("mandatory")


class _Metro1500OSC_PortAutoneg3_Type(Integer32):
    """Custom type metro1500OSC_PortAutoneg3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500OSC_PortAutoneg3_Type.__name__ = "Integer32"
_Metro1500OSC_PortAutoneg3_Object = MibTableColumn
metro1500OSC_PortAutoneg3 = _Metro1500OSC_PortAutoneg3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 33),
    _Metro1500OSC_PortAutoneg3_Type()
)
metro1500OSC_PortAutoneg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortAutoneg3.setStatus("mandatory")


class _Metro1500OSC_PortPolarity3_Type(Integer32):
    """Custom type metro1500OSC_PortPolarity3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500OSC_PortPolarity3_Type.__name__ = "Integer32"
_Metro1500OSC_PortPolarity3_Object = MibTableColumn
metro1500OSC_PortPolarity3 = _Metro1500OSC_PortPolarity3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 34),
    _Metro1500OSC_PortPolarity3_Type()
)
metro1500OSC_PortPolarity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortPolarity3.setStatus("mandatory")


class _Metro1500OSC_PortLinkStatus3_Type(Integer32):
    """Custom type metro1500OSC_PortLinkStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500OSC_PortLinkStatus3_Type.__name__ = "Integer32"
_Metro1500OSC_PortLinkStatus3_Object = MibTableColumn
metro1500OSC_PortLinkStatus3 = _Metro1500OSC_PortLinkStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 35),
    _Metro1500OSC_PortLinkStatus3_Type()
)
metro1500OSC_PortLinkStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortLinkStatus3.setStatus("mandatory")


class _Metro1500OSC_PortEnable4_Type(Integer32):
    """Custom type metro1500OSC_PortEnable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500OSC_PortEnable4_Type.__name__ = "Integer32"
_Metro1500OSC_PortEnable4_Object = MibTableColumn
metro1500OSC_PortEnable4 = _Metro1500OSC_PortEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 40),
    _Metro1500OSC_PortEnable4_Type()
)
metro1500OSC_PortEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortEnable4.setStatus("mandatory")


class _Metro1500OSC_PortSpeed4_Type(Integer32):
    """Custom type metro1500OSC_PortSpeed4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2))
    )


_Metro1500OSC_PortSpeed4_Type.__name__ = "Integer32"
_Metro1500OSC_PortSpeed4_Object = MibTableColumn
metro1500OSC_PortSpeed4 = _Metro1500OSC_PortSpeed4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 41),
    _Metro1500OSC_PortSpeed4_Type()
)
metro1500OSC_PortSpeed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortSpeed4.setStatus("mandatory")


class _Metro1500OSC_PortDuplex4_Type(Integer32):
    """Custom type metro1500OSC_PortDuplex4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_Metro1500OSC_PortDuplex4_Type.__name__ = "Integer32"
_Metro1500OSC_PortDuplex4_Object = MibTableColumn
metro1500OSC_PortDuplex4 = _Metro1500OSC_PortDuplex4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 42),
    _Metro1500OSC_PortDuplex4_Type()
)
metro1500OSC_PortDuplex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortDuplex4.setStatus("mandatory")


class _Metro1500OSC_PortAutoneg4_Type(Integer32):
    """Custom type metro1500OSC_PortAutoneg4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500OSC_PortAutoneg4_Type.__name__ = "Integer32"
_Metro1500OSC_PortAutoneg4_Object = MibTableColumn
metro1500OSC_PortAutoneg4 = _Metro1500OSC_PortAutoneg4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 43),
    _Metro1500OSC_PortAutoneg4_Type()
)
metro1500OSC_PortAutoneg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortAutoneg4.setStatus("mandatory")


class _Metro1500OSC_PortPolarity4_Type(Integer32):
    """Custom type metro1500OSC_PortPolarity4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500OSC_PortPolarity4_Type.__name__ = "Integer32"
_Metro1500OSC_PortPolarity4_Object = MibTableColumn
metro1500OSC_PortPolarity4 = _Metro1500OSC_PortPolarity4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 44),
    _Metro1500OSC_PortPolarity4_Type()
)
metro1500OSC_PortPolarity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortPolarity4.setStatus("mandatory")


class _Metro1500OSC_PortLinkStatus4_Type(Integer32):
    """Custom type metro1500OSC_PortLinkStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500OSC_PortLinkStatus4_Type.__name__ = "Integer32"
_Metro1500OSC_PortLinkStatus4_Object = MibTableColumn
metro1500OSC_PortLinkStatus4 = _Metro1500OSC_PortLinkStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 45),
    _Metro1500OSC_PortLinkStatus4_Type()
)
metro1500OSC_PortLinkStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortLinkStatus4.setStatus("mandatory")


class _Metro1500OSC_PortEnable5_Type(Integer32):
    """Custom type metro1500OSC_PortEnable5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500OSC_PortEnable5_Type.__name__ = "Integer32"
_Metro1500OSC_PortEnable5_Object = MibTableColumn
metro1500OSC_PortEnable5 = _Metro1500OSC_PortEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 50),
    _Metro1500OSC_PortEnable5_Type()
)
metro1500OSC_PortEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortEnable5.setStatus("mandatory")


class _Metro1500OSC_PortSpeed5_Type(Integer32):
    """Custom type metro1500OSC_PortSpeed5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2))
    )


_Metro1500OSC_PortSpeed5_Type.__name__ = "Integer32"
_Metro1500OSC_PortSpeed5_Object = MibTableColumn
metro1500OSC_PortSpeed5 = _Metro1500OSC_PortSpeed5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 51),
    _Metro1500OSC_PortSpeed5_Type()
)
metro1500OSC_PortSpeed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortSpeed5.setStatus("mandatory")


class _Metro1500OSC_PortDuplex5_Type(Integer32):
    """Custom type metro1500OSC_PortDuplex5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_Metro1500OSC_PortDuplex5_Type.__name__ = "Integer32"
_Metro1500OSC_PortDuplex5_Object = MibTableColumn
metro1500OSC_PortDuplex5 = _Metro1500OSC_PortDuplex5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 52),
    _Metro1500OSC_PortDuplex5_Type()
)
metro1500OSC_PortDuplex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortDuplex5.setStatus("mandatory")


class _Metro1500OSC_PortAutoneg5_Type(Integer32):
    """Custom type metro1500OSC_PortAutoneg5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500OSC_PortAutoneg5_Type.__name__ = "Integer32"
_Metro1500OSC_PortAutoneg5_Object = MibTableColumn
metro1500OSC_PortAutoneg5 = _Metro1500OSC_PortAutoneg5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 53),
    _Metro1500OSC_PortAutoneg5_Type()
)
metro1500OSC_PortAutoneg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortAutoneg5.setStatus("mandatory")


class _Metro1500OSC_PortPolarity5_Type(Integer32):
    """Custom type metro1500OSC_PortPolarity5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500OSC_PortPolarity5_Type.__name__ = "Integer32"
_Metro1500OSC_PortPolarity5_Object = MibTableColumn
metro1500OSC_PortPolarity5 = _Metro1500OSC_PortPolarity5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 54),
    _Metro1500OSC_PortPolarity5_Type()
)
metro1500OSC_PortPolarity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortPolarity5.setStatus("mandatory")


class _Metro1500OSC_PortLinkStatus5_Type(Integer32):
    """Custom type metro1500OSC_PortLinkStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500OSC_PortLinkStatus5_Type.__name__ = "Integer32"
_Metro1500OSC_PortLinkStatus5_Object = MibTableColumn
metro1500OSC_PortLinkStatus5 = _Metro1500OSC_PortLinkStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 55),
    _Metro1500OSC_PortLinkStatus5_Type()
)
metro1500OSC_PortLinkStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortLinkStatus5.setStatus("mandatory")


class _Metro1500OSC_PortEnable6_Type(Integer32):
    """Custom type metro1500OSC_PortEnable6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500OSC_PortEnable6_Type.__name__ = "Integer32"
_Metro1500OSC_PortEnable6_Object = MibTableColumn
metro1500OSC_PortEnable6 = _Metro1500OSC_PortEnable6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 60),
    _Metro1500OSC_PortEnable6_Type()
)
metro1500OSC_PortEnable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortEnable6.setStatus("mandatory")


class _Metro1500OSC_PortSpeed6_Type(Integer32):
    """Custom type metro1500OSC_PortSpeed6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2))
    )


_Metro1500OSC_PortSpeed6_Type.__name__ = "Integer32"
_Metro1500OSC_PortSpeed6_Object = MibTableColumn
metro1500OSC_PortSpeed6 = _Metro1500OSC_PortSpeed6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 61),
    _Metro1500OSC_PortSpeed6_Type()
)
metro1500OSC_PortSpeed6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortSpeed6.setStatus("mandatory")


class _Metro1500OSC_PortDuplex6_Type(Integer32):
    """Custom type metro1500OSC_PortDuplex6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_Metro1500OSC_PortDuplex6_Type.__name__ = "Integer32"
_Metro1500OSC_PortDuplex6_Object = MibTableColumn
metro1500OSC_PortDuplex6 = _Metro1500OSC_PortDuplex6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 62),
    _Metro1500OSC_PortDuplex6_Type()
)
metro1500OSC_PortDuplex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortDuplex6.setStatus("mandatory")


class _Metro1500OSC_PortLinkStatus6_Type(Integer32):
    """Custom type metro1500OSC_PortLinkStatus6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("signal", 2),
          ("noSignal", 3))
    )


_Metro1500OSC_PortLinkStatus6_Type.__name__ = "Integer32"
_Metro1500OSC_PortLinkStatus6_Object = MibTableColumn
metro1500OSC_PortLinkStatus6 = _Metro1500OSC_PortLinkStatus6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 65),
    _Metro1500OSC_PortLinkStatus6_Type()
)
metro1500OSC_PortLinkStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_PortLinkStatus6.setStatus("mandatory")
_Metro1500OSC_Connector_Type = DisplayString
_Metro1500OSC_Connector_Object = MibTableColumn
metro1500OSC_Connector = _Metro1500OSC_Connector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 70),
    _Metro1500OSC_Connector_Type()
)
metro1500OSC_Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_Connector.setStatus("mandatory")
_Metro1500OSC_RemoteLaserType_Type = DisplayString
_Metro1500OSC_RemoteLaserType_Object = MibTableColumn
metro1500OSC_RemoteLaserType = _Metro1500OSC_RemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 71),
    _Metro1500OSC_RemoteLaserType_Type()
)
metro1500OSC_RemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500OSC_RemoteLaserType.setStatus("mandatory")
_Metro1500EthernetHub_ObjectIdentity = ObjectIdentity
metro1500EthernetHub = _Metro1500EthernetHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14)
)
_Metro1500EthernetHubTable_Object = MibTable
metro1500EthernetHubTable = _Metro1500EthernetHubTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1)
)
if mibBuilder.loadTexts:
    metro1500EthernetHubTable.setStatus("mandatory")
_Metro1500EthernetHubEntry_Object = MibTableRow
metro1500EthernetHubEntry = _Metro1500EthernetHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1)
)
metro1500EthernetHubEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500EthernetHubNumber"),
)
if mibBuilder.loadTexts:
    metro1500EthernetHubEntry.setStatus("mandatory")
_Metro1500EthernetHubNumber_Type = Metro1500SlotNumberRange
_Metro1500EthernetHubNumber_Object = MibTableColumn
metro1500EthernetHubNumber = _Metro1500EthernetHubNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 1),
    _Metro1500EthernetHubNumber_Type()
)
metro1500EthernetHubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubNumber.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable1_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500EthernetHubPortEnable1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable1_Object = MibTableColumn
metro1500EthernetHubPortEnable1 = _Metro1500EthernetHubPortEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 10),
    _Metro1500EthernetHubPortEnable1_Type()
)
metro1500EthernetHubPortEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable1.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus1_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partitioned", 1),
          ("notPartitioned", 2))
    )


_Metro1500EthernetHubPortPartitionStatus1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus1_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus1 = _Metro1500EthernetHubPortPartitionStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 11),
    _Metro1500EthernetHubPortPartitionStatus1_Type()
)
metro1500EthernetHubPortPartitionStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus1.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus1_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus1_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus1 = _Metro1500EthernetHubPortLinkStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 12),
    _Metro1500EthernetHubPortLinkStatus1_Type()
)
metro1500EthernetHubPortLinkStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus1.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity1_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500EthernetHubPortPolarity1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity1_Object = MibTableColumn
metro1500EthernetHubPortPolarity1 = _Metro1500EthernetHubPortPolarity1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 13),
    _Metro1500EthernetHubPortPolarity1_Type()
)
metro1500EthernetHubPortPolarity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity1.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable2_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500EthernetHubPortEnable2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable2_Object = MibTableColumn
metro1500EthernetHubPortEnable2 = _Metro1500EthernetHubPortEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 20),
    _Metro1500EthernetHubPortEnable2_Type()
)
metro1500EthernetHubPortEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable2.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus2_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partitioned", 1),
          ("notPartitioned", 2))
    )


_Metro1500EthernetHubPortPartitionStatus2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus2_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus2 = _Metro1500EthernetHubPortPartitionStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 21),
    _Metro1500EthernetHubPortPartitionStatus2_Type()
)
metro1500EthernetHubPortPartitionStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus2.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus2_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus2_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus2 = _Metro1500EthernetHubPortLinkStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 22),
    _Metro1500EthernetHubPortLinkStatus2_Type()
)
metro1500EthernetHubPortLinkStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus2.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity2_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500EthernetHubPortPolarity2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity2_Object = MibTableColumn
metro1500EthernetHubPortPolarity2 = _Metro1500EthernetHubPortPolarity2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 23),
    _Metro1500EthernetHubPortPolarity2_Type()
)
metro1500EthernetHubPortPolarity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity2.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable3_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500EthernetHubPortEnable3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable3_Object = MibTableColumn
metro1500EthernetHubPortEnable3 = _Metro1500EthernetHubPortEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 30),
    _Metro1500EthernetHubPortEnable3_Type()
)
metro1500EthernetHubPortEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable3.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus3_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partitioned", 1),
          ("notPartitioned", 2))
    )


_Metro1500EthernetHubPortPartitionStatus3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus3_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus3 = _Metro1500EthernetHubPortPartitionStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 31),
    _Metro1500EthernetHubPortPartitionStatus3_Type()
)
metro1500EthernetHubPortPartitionStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus3.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus3_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus3_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus3 = _Metro1500EthernetHubPortLinkStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 32),
    _Metro1500EthernetHubPortLinkStatus3_Type()
)
metro1500EthernetHubPortLinkStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus3.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity3_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500EthernetHubPortPolarity3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity3_Object = MibTableColumn
metro1500EthernetHubPortPolarity3 = _Metro1500EthernetHubPortPolarity3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 33),
    _Metro1500EthernetHubPortPolarity3_Type()
)
metro1500EthernetHubPortPolarity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity3.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable4_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500EthernetHubPortEnable4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable4_Object = MibTableColumn
metro1500EthernetHubPortEnable4 = _Metro1500EthernetHubPortEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 40),
    _Metro1500EthernetHubPortEnable4_Type()
)
metro1500EthernetHubPortEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable4.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus4_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partitioned", 1),
          ("notPartitioned", 2))
    )


_Metro1500EthernetHubPortPartitionStatus4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus4_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus4 = _Metro1500EthernetHubPortPartitionStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 41),
    _Metro1500EthernetHubPortPartitionStatus4_Type()
)
metro1500EthernetHubPortPartitionStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus4.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus4_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus4_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus4 = _Metro1500EthernetHubPortLinkStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 42),
    _Metro1500EthernetHubPortLinkStatus4_Type()
)
metro1500EthernetHubPortLinkStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus4.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity4_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500EthernetHubPortPolarity4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity4_Object = MibTableColumn
metro1500EthernetHubPortPolarity4 = _Metro1500EthernetHubPortPolarity4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 43),
    _Metro1500EthernetHubPortPolarity4_Type()
)
metro1500EthernetHubPortPolarity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity4.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable5_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Metro1500EthernetHubPortEnable5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable5_Object = MibTableColumn
metro1500EthernetHubPortEnable5 = _Metro1500EthernetHubPortEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 50),
    _Metro1500EthernetHubPortEnable5_Type()
)
metro1500EthernetHubPortEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable5.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus5_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partitioned", 1),
          ("notPartitioned", 2))
    )


_Metro1500EthernetHubPortPartitionStatus5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus5_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus5 = _Metro1500EthernetHubPortPartitionStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 51),
    _Metro1500EthernetHubPortPartitionStatus5_Type()
)
metro1500EthernetHubPortPartitionStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus5.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus5_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus5_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus5 = _Metro1500EthernetHubPortLinkStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 52),
    _Metro1500EthernetHubPortLinkStatus5_Type()
)
metro1500EthernetHubPortLinkStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus5.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity5_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("positive", 1),
          ("negative", 2))
    )


_Metro1500EthernetHubPortPolarity5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity5_Object = MibTableColumn
metro1500EthernetHubPortPolarity5 = _Metro1500EthernetHubPortPolarity5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 53),
    _Metro1500EthernetHubPortPolarity5_Type()
)
metro1500EthernetHubPortPolarity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity5.setStatus("mandatory")
_Metro1500TDM_ObjectIdentity = ObjectIdentity
metro1500TDM = _Metro1500TDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15)
)
_Metro1500TDMTable_Object = MibTable
metro1500TDMTable = _Metro1500TDMTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1)
)
if mibBuilder.loadTexts:
    metro1500TDMTable.setStatus("mandatory")
_Metro1500TDMEntry_Object = MibTableRow
metro1500TDMEntry = _Metro1500TDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1)
)
metro1500TDMEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500TDMNumber"),
)
if mibBuilder.loadTexts:
    metro1500TDMEntry.setStatus("mandatory")
_Metro1500TDMNumber_Type = Metro1500SlotNumberRange
_Metro1500TDMNumber_Object = MibTableColumn
metro1500TDMNumber = _Metro1500TDMNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 1),
    _Metro1500TDMNumber_Type()
)
metro1500TDMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMNumber.setStatus("mandatory")


class _Metro1500TDMRxRem_Type(Integer32):
    """Custom type metro1500TDMRxRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMRxRem_Type.__name__ = "Integer32"
_Metro1500TDMRxRem_Object = MibTableColumn
metro1500TDMRxRem = _Metro1500TDMRxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 4),
    _Metro1500TDMRxRem_Type()
)
metro1500TDMRxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMRxRem.setStatus("mandatory")


class _Metro1500TDMRxSync_Type(Integer32):
    """Custom type metro1500TDMRxSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync", 1),
          ("noSync", 2))
    )


_Metro1500TDMRxSync_Type.__name__ = "Integer32"
_Metro1500TDMRxSync_Object = MibTableColumn
metro1500TDMRxSync = _Metro1500TDMRxSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 5),
    _Metro1500TDMRxSync_Type()
)
metro1500TDMRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMRxSync.setStatus("mandatory")


class _Metro1500TDMTxRem_Type(Integer32):
    """Custom type metro1500TDMTxRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMTxRem_Type.__name__ = "Integer32"
_Metro1500TDMTxRem_Object = MibTableColumn
metro1500TDMTxRem = _Metro1500TDMTxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 6),
    _Metro1500TDMTxRem_Type()
)
metro1500TDMTxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMTxRem.setStatus("mandatory")


class _Metro1500TDMTxRemC_Type(Integer32):
    """Custom type metro1500TDMTxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Metro1500TDMTxRemC_Type.__name__ = "Integer32"
_Metro1500TDMTxRemC_Object = MibTableColumn
metro1500TDMTxRemC = _Metro1500TDMTxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 7),
    _Metro1500TDMTxRemC_Type()
)
metro1500TDMTxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMTxRemC.setStatus("mandatory")


class _Metro1500TDMTxRemTemp_Type(Integer32):
    """Custom type metro1500TDMTxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Metro1500TDMTxRemTemp_Type.__name__ = "Integer32"
_Metro1500TDMTxRemTemp_Object = MibTableColumn
metro1500TDMTxRemTemp = _Metro1500TDMTxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 8),
    _Metro1500TDMTxRemTemp_Type()
)
metro1500TDMTxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMTxRemTemp.setStatus("mandatory")


class _Metro1500TDMLocLoop_Type(Integer32):
    """Custom type metro1500TDMLocLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocLoop_Type.__name__ = "Integer32"
_Metro1500TDMLocLoop_Object = MibTableColumn
metro1500TDMLocLoop = _Metro1500TDMLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 9),
    _Metro1500TDMLocLoop_Type()
)
metro1500TDMLocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocLoop.setStatus("mandatory")


class _Metro1500TDMClockType_Type(Integer32):
    """Custom type metro1500TDMClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(18,
              42,
              255)
        )
    )
    namedValues = NamedValues(
        *(("multiClock3LS", 18),
          ("fixedClock200Mbps", 42),
          ("other", 255))
    )


_Metro1500TDMClockType_Type.__name__ = "Integer32"
_Metro1500TDMClockType_Object = MibTableColumn
metro1500TDMClockType = _Metro1500TDMClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 10),
    _Metro1500TDMClockType_Type()
)
metro1500TDMClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMClockType.setStatus("mandatory")


class _Metro1500TDMLocModuleInst1_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst1_Object = MibTableColumn
metro1500TDMLocModuleInst1 = _Metro1500TDMLocModuleInst1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 20),
    _Metro1500TDMLocModuleInst1_Type()
)
metro1500TDMLocModuleInst1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst1.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable1_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable1_Object = MibTableColumn
metro1500TDMLocModuleEnable1 = _Metro1500TDMLocModuleEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 21),
    _Metro1500TDMLocModuleEnable1_Type()
)
metro1500TDMLocModuleEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable1.setStatus("mandatory")


class _Metro1500TDMLocModuleRx1_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx1_Object = MibTableColumn
metro1500TDMLocModuleRx1 = _Metro1500TDMLocModuleRx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 22),
    _Metro1500TDMLocModuleRx1_Type()
)
metro1500TDMLocModuleRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx1.setStatus("mandatory")


class _Metro1500TDMLocModuleTx1_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx1_Object = MibTableColumn
metro1500TDMLocModuleTx1 = _Metro1500TDMLocModuleTx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 23),
    _Metro1500TDMLocModuleTx1_Type()
)
metro1500TDMLocModuleTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx1.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData1_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData1_Object = MibTableColumn
metro1500TDMLocModuleRemoteData1 = _Metro1500TDMLocModuleRemoteData1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 24),
    _Metro1500TDMLocModuleRemoteData1_Type()
)
metro1500TDMLocModuleRemoteData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData1.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency1_Type = Integer32
_Metro1500TDMLocModuleClockFrequency1_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency1 = _Metro1500TDMLocModuleClockFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 25),
    _Metro1500TDMLocModuleClockFrequency1_Type()
)
metro1500TDMLocModuleClockFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency1.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError1_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError1_Object = MibTableColumn
metro1500TDMLocModuleClockError1 = _Metro1500TDMLocModuleClockError1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 26),
    _Metro1500TDMLocModuleClockError1_Type()
)
metro1500TDMLocModuleClockError1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError1.setStatus("mandatory")


class _Metro1500TDMLocModuleInst2_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst2_Object = MibTableColumn
metro1500TDMLocModuleInst2 = _Metro1500TDMLocModuleInst2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 30),
    _Metro1500TDMLocModuleInst2_Type()
)
metro1500TDMLocModuleInst2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst2.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable2_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable2_Object = MibTableColumn
metro1500TDMLocModuleEnable2 = _Metro1500TDMLocModuleEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 31),
    _Metro1500TDMLocModuleEnable2_Type()
)
metro1500TDMLocModuleEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable2.setStatus("mandatory")


class _Metro1500TDMLocModuleRx2_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx2_Object = MibTableColumn
metro1500TDMLocModuleRx2 = _Metro1500TDMLocModuleRx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 32),
    _Metro1500TDMLocModuleRx2_Type()
)
metro1500TDMLocModuleRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx2.setStatus("mandatory")


class _Metro1500TDMLocModuleTx2_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx2_Object = MibTableColumn
metro1500TDMLocModuleTx2 = _Metro1500TDMLocModuleTx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 33),
    _Metro1500TDMLocModuleTx2_Type()
)
metro1500TDMLocModuleTx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx2.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData2_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData2_Object = MibTableColumn
metro1500TDMLocModuleRemoteData2 = _Metro1500TDMLocModuleRemoteData2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 34),
    _Metro1500TDMLocModuleRemoteData2_Type()
)
metro1500TDMLocModuleRemoteData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData2.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency2_Type = Integer32
_Metro1500TDMLocModuleClockFrequency2_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency2 = _Metro1500TDMLocModuleClockFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 35),
    _Metro1500TDMLocModuleClockFrequency2_Type()
)
metro1500TDMLocModuleClockFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency2.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError2_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError2_Object = MibTableColumn
metro1500TDMLocModuleClockError2 = _Metro1500TDMLocModuleClockError2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 36),
    _Metro1500TDMLocModuleClockError2_Type()
)
metro1500TDMLocModuleClockError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError2.setStatus("mandatory")


class _Metro1500TDMLocModuleInst3_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst3_Object = MibTableColumn
metro1500TDMLocModuleInst3 = _Metro1500TDMLocModuleInst3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 40),
    _Metro1500TDMLocModuleInst3_Type()
)
metro1500TDMLocModuleInst3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst3.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable3_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable3_Object = MibTableColumn
metro1500TDMLocModuleEnable3 = _Metro1500TDMLocModuleEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 41),
    _Metro1500TDMLocModuleEnable3_Type()
)
metro1500TDMLocModuleEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable3.setStatus("mandatory")


class _Metro1500TDMLocModuleRx3_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx3_Object = MibTableColumn
metro1500TDMLocModuleRx3 = _Metro1500TDMLocModuleRx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 42),
    _Metro1500TDMLocModuleRx3_Type()
)
metro1500TDMLocModuleRx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx3.setStatus("mandatory")


class _Metro1500TDMLocModuleTx3_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx3_Object = MibTableColumn
metro1500TDMLocModuleTx3 = _Metro1500TDMLocModuleTx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 43),
    _Metro1500TDMLocModuleTx3_Type()
)
metro1500TDMLocModuleTx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx3.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData3_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData3_Object = MibTableColumn
metro1500TDMLocModuleRemoteData3 = _Metro1500TDMLocModuleRemoteData3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 44),
    _Metro1500TDMLocModuleRemoteData3_Type()
)
metro1500TDMLocModuleRemoteData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData3.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency3_Type = Integer32
_Metro1500TDMLocModuleClockFrequency3_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency3 = _Metro1500TDMLocModuleClockFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 45),
    _Metro1500TDMLocModuleClockFrequency3_Type()
)
metro1500TDMLocModuleClockFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency3.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError3_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError3_Object = MibTableColumn
metro1500TDMLocModuleClockError3 = _Metro1500TDMLocModuleClockError3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 46),
    _Metro1500TDMLocModuleClockError3_Type()
)
metro1500TDMLocModuleClockError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError3.setStatus("mandatory")


class _Metro1500TDMLocModuleInst4_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst4_Object = MibTableColumn
metro1500TDMLocModuleInst4 = _Metro1500TDMLocModuleInst4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 50),
    _Metro1500TDMLocModuleInst4_Type()
)
metro1500TDMLocModuleInst4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst4.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable4_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable4_Object = MibTableColumn
metro1500TDMLocModuleEnable4 = _Metro1500TDMLocModuleEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 51),
    _Metro1500TDMLocModuleEnable4_Type()
)
metro1500TDMLocModuleEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable4.setStatus("mandatory")


class _Metro1500TDMLocModuleRx4_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx4_Object = MibTableColumn
metro1500TDMLocModuleRx4 = _Metro1500TDMLocModuleRx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 52),
    _Metro1500TDMLocModuleRx4_Type()
)
metro1500TDMLocModuleRx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx4.setStatus("mandatory")


class _Metro1500TDMLocModuleTx4_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx4_Object = MibTableColumn
metro1500TDMLocModuleTx4 = _Metro1500TDMLocModuleTx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 53),
    _Metro1500TDMLocModuleTx4_Type()
)
metro1500TDMLocModuleTx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx4.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData4_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData4_Object = MibTableColumn
metro1500TDMLocModuleRemoteData4 = _Metro1500TDMLocModuleRemoteData4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 54),
    _Metro1500TDMLocModuleRemoteData4_Type()
)
metro1500TDMLocModuleRemoteData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData4.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency4_Type = Integer32
_Metro1500TDMLocModuleClockFrequency4_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency4 = _Metro1500TDMLocModuleClockFrequency4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 55),
    _Metro1500TDMLocModuleClockFrequency4_Type()
)
metro1500TDMLocModuleClockFrequency4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency4.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError4_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError4_Object = MibTableColumn
metro1500TDMLocModuleClockError4 = _Metro1500TDMLocModuleClockError4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 56),
    _Metro1500TDMLocModuleClockError4_Type()
)
metro1500TDMLocModuleClockError4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError4.setStatus("mandatory")
_Metro1500TDMLocalConnector_Type = DisplayString
_Metro1500TDMLocalConnector_Object = MibTableColumn
metro1500TDMLocalConnector = _Metro1500TDMLocalConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 60),
    _Metro1500TDMLocalConnector_Type()
)
metro1500TDMLocalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocalConnector.setStatus("mandatory")
_Metro1500TDMLocalLaserType_Type = DisplayString
_Metro1500TDMLocalLaserType_Object = MibTableColumn
metro1500TDMLocalLaserType = _Metro1500TDMLocalLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 61),
    _Metro1500TDMLocalLaserType_Type()
)
metro1500TDMLocalLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocalLaserType.setStatus("mandatory")
_Metro1500TDMRemoteConnector_Type = DisplayString
_Metro1500TDMRemoteConnector_Object = MibTableColumn
metro1500TDMRemoteConnector = _Metro1500TDMRemoteConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 62),
    _Metro1500TDMRemoteConnector_Type()
)
metro1500TDMRemoteConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMRemoteConnector.setStatus("mandatory")
_Metro1500TDMRemoteLaserType_Type = DisplayString
_Metro1500TDMRemoteLaserType_Object = MibTableColumn
metro1500TDMRemoteLaserType = _Metro1500TDMRemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 63),
    _Metro1500TDMRemoteLaserType_Type()
)
metro1500TDMRemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMRemoteLaserType.setStatus("mandatory")
_Metro1500TDMConverterType_Type = DisplayString
_Metro1500TDMConverterType_Object = MibTableColumn
metro1500TDMConverterType = _Metro1500TDMConverterType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 64),
    _Metro1500TDMConverterType_Type()
)
metro1500TDMConverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMConverterType.setStatus("mandatory")
_Metro1500TDMClockRecovery_Type = DisplayString
_Metro1500TDMClockRecovery_Object = MibTableColumn
metro1500TDMClockRecovery = _Metro1500TDMClockRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 65),
    _Metro1500TDMClockRecovery_Type()
)
metro1500TDMClockRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMClockRecovery.setStatus("mandatory")
_Metro1500TDMDataRateRange_Type = DisplayString
_Metro1500TDMDataRateRange_Object = MibTableColumn
metro1500TDMDataRateRange = _Metro1500TDMDataRateRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 66),
    _Metro1500TDMDataRateRange_Type()
)
metro1500TDMDataRateRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMDataRateRange.setStatus("mandatory")
_Metro1500TDMClockFreqRange_Type = DisplayString
_Metro1500TDMClockFreqRange_Object = MibTableColumn
metro1500TDMClockFreqRange = _Metro1500TDMClockFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 67),
    _Metro1500TDMClockFreqRange_Type()
)
metro1500TDMClockFreqRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMClockFreqRange.setStatus("mandatory")


class _Metro1500TDMChannelNumber_Type(Integer32):
    """Custom type metro1500TDMChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Metro1500TDMChannelNumber_Type.__name__ = "Integer32"
_Metro1500TDMChannelNumber_Object = MibTableColumn
metro1500TDMChannelNumber = _Metro1500TDMChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 68),
    _Metro1500TDMChannelNumber_Type()
)
metro1500TDMChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMChannelNumber.setStatus("mandatory")


class _Metro1500TDMLocModuleInst5_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst5_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst5_Object = MibTableColumn
metro1500TDMLocModuleInst5 = _Metro1500TDMLocModuleInst5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 70),
    _Metro1500TDMLocModuleInst5_Type()
)
metro1500TDMLocModuleInst5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst5.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable5_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable5_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable5_Object = MibTableColumn
metro1500TDMLocModuleEnable5 = _Metro1500TDMLocModuleEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 71),
    _Metro1500TDMLocModuleEnable5_Type()
)
metro1500TDMLocModuleEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable5.setStatus("mandatory")


class _Metro1500TDMLocModuleRx5_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx5_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx5_Object = MibTableColumn
metro1500TDMLocModuleRx5 = _Metro1500TDMLocModuleRx5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 72),
    _Metro1500TDMLocModuleRx5_Type()
)
metro1500TDMLocModuleRx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx5.setStatus("mandatory")


class _Metro1500TDMLocModuleTx5_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx5_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx5_Object = MibTableColumn
metro1500TDMLocModuleTx5 = _Metro1500TDMLocModuleTx5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 73),
    _Metro1500TDMLocModuleTx5_Type()
)
metro1500TDMLocModuleTx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx5.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData5_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData5_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData5_Object = MibTableColumn
metro1500TDMLocModuleRemoteData5 = _Metro1500TDMLocModuleRemoteData5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 74),
    _Metro1500TDMLocModuleRemoteData5_Type()
)
metro1500TDMLocModuleRemoteData5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData5.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency5_Type = Integer32
_Metro1500TDMLocModuleClockFrequency5_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency5 = _Metro1500TDMLocModuleClockFrequency5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 75),
    _Metro1500TDMLocModuleClockFrequency5_Type()
)
metro1500TDMLocModuleClockFrequency5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency5.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError5_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError5_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError5_Object = MibTableColumn
metro1500TDMLocModuleClockError5 = _Metro1500TDMLocModuleClockError5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 76),
    _Metro1500TDMLocModuleClockError5_Type()
)
metro1500TDMLocModuleClockError5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError5.setStatus("mandatory")


class _Metro1500TDMLocModuleInst6_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst6_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst6_Object = MibTableColumn
metro1500TDMLocModuleInst6 = _Metro1500TDMLocModuleInst6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 80),
    _Metro1500TDMLocModuleInst6_Type()
)
metro1500TDMLocModuleInst6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst6.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable6_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable6_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable6_Object = MibTableColumn
metro1500TDMLocModuleEnable6 = _Metro1500TDMLocModuleEnable6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 81),
    _Metro1500TDMLocModuleEnable6_Type()
)
metro1500TDMLocModuleEnable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable6.setStatus("mandatory")


class _Metro1500TDMLocModuleRx6_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx6_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx6_Object = MibTableColumn
metro1500TDMLocModuleRx6 = _Metro1500TDMLocModuleRx6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 82),
    _Metro1500TDMLocModuleRx6_Type()
)
metro1500TDMLocModuleRx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx6.setStatus("mandatory")


class _Metro1500TDMLocModuleTx6_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx6_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx6_Object = MibTableColumn
metro1500TDMLocModuleTx6 = _Metro1500TDMLocModuleTx6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 83),
    _Metro1500TDMLocModuleTx6_Type()
)
metro1500TDMLocModuleTx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx6.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData6_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData6_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData6_Object = MibTableColumn
metro1500TDMLocModuleRemoteData6 = _Metro1500TDMLocModuleRemoteData6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 84),
    _Metro1500TDMLocModuleRemoteData6_Type()
)
metro1500TDMLocModuleRemoteData6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData6.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency6_Type = Integer32
_Metro1500TDMLocModuleClockFrequency6_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency6 = _Metro1500TDMLocModuleClockFrequency6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 85),
    _Metro1500TDMLocModuleClockFrequency6_Type()
)
metro1500TDMLocModuleClockFrequency6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency6.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError6_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError6_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError6_Object = MibTableColumn
metro1500TDMLocModuleClockError6 = _Metro1500TDMLocModuleClockError6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 86),
    _Metro1500TDMLocModuleClockError6_Type()
)
metro1500TDMLocModuleClockError6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError6.setStatus("mandatory")


class _Metro1500TDMLocModuleInst7_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst7_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst7_Object = MibTableColumn
metro1500TDMLocModuleInst7 = _Metro1500TDMLocModuleInst7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 90),
    _Metro1500TDMLocModuleInst7_Type()
)
metro1500TDMLocModuleInst7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst7.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable7_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable7_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable7_Object = MibTableColumn
metro1500TDMLocModuleEnable7 = _Metro1500TDMLocModuleEnable7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 91),
    _Metro1500TDMLocModuleEnable7_Type()
)
metro1500TDMLocModuleEnable7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable7.setStatus("mandatory")


class _Metro1500TDMLocModuleRx7_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx7_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx7_Object = MibTableColumn
metro1500TDMLocModuleRx7 = _Metro1500TDMLocModuleRx7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 92),
    _Metro1500TDMLocModuleRx7_Type()
)
metro1500TDMLocModuleRx7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx7.setStatus("mandatory")


class _Metro1500TDMLocModuleTx7_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx7_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx7_Object = MibTableColumn
metro1500TDMLocModuleTx7 = _Metro1500TDMLocModuleTx7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 93),
    _Metro1500TDMLocModuleTx7_Type()
)
metro1500TDMLocModuleTx7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx7.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData7_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData7_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData7_Object = MibTableColumn
metro1500TDMLocModuleRemoteData7 = _Metro1500TDMLocModuleRemoteData7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 94),
    _Metro1500TDMLocModuleRemoteData7_Type()
)
metro1500TDMLocModuleRemoteData7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData7.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency7_Type = Integer32
_Metro1500TDMLocModuleClockFrequency7_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency7 = _Metro1500TDMLocModuleClockFrequency7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 95),
    _Metro1500TDMLocModuleClockFrequency7_Type()
)
metro1500TDMLocModuleClockFrequency7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency7.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError7_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError7_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError7_Object = MibTableColumn
metro1500TDMLocModuleClockError7 = _Metro1500TDMLocModuleClockError7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 96),
    _Metro1500TDMLocModuleClockError7_Type()
)
metro1500TDMLocModuleClockError7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError7.setStatus("mandatory")


class _Metro1500TDMLocModuleInst8_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst8_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst8_Object = MibTableColumn
metro1500TDMLocModuleInst8 = _Metro1500TDMLocModuleInst8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 100),
    _Metro1500TDMLocModuleInst8_Type()
)
metro1500TDMLocModuleInst8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst8.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable8_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable8_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable8_Object = MibTableColumn
metro1500TDMLocModuleEnable8 = _Metro1500TDMLocModuleEnable8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 101),
    _Metro1500TDMLocModuleEnable8_Type()
)
metro1500TDMLocModuleEnable8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable8.setStatus("mandatory")


class _Metro1500TDMLocModuleRx8_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Metro1500TDMLocModuleRx8_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx8_Object = MibTableColumn
metro1500TDMLocModuleRx8 = _Metro1500TDMLocModuleRx8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 102),
    _Metro1500TDMLocModuleRx8_Type()
)
metro1500TDMLocModuleRx8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx8.setStatus("mandatory")


class _Metro1500TDMLocModuleTx8_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_Metro1500TDMLocModuleTx8_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx8_Object = MibTableColumn
metro1500TDMLocModuleTx8 = _Metro1500TDMLocModuleTx8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 103),
    _Metro1500TDMLocModuleTx8_Type()
)
metro1500TDMLocModuleTx8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx8.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData8_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData8_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData8_Object = MibTableColumn
metro1500TDMLocModuleRemoteData8 = _Metro1500TDMLocModuleRemoteData8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 104),
    _Metro1500TDMLocModuleRemoteData8_Type()
)
metro1500TDMLocModuleRemoteData8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData8.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency8_Type = Integer32
_Metro1500TDMLocModuleClockFrequency8_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency8 = _Metro1500TDMLocModuleClockFrequency8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 105),
    _Metro1500TDMLocModuleClockFrequency8_Type()
)
metro1500TDMLocModuleClockFrequency8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency8.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError8_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError8_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError8_Object = MibTableColumn
metro1500TDMLocModuleClockError8 = _Metro1500TDMLocModuleClockError8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 106),
    _Metro1500TDMLocModuleClockError8_Type()
)
metro1500TDMLocModuleClockError8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError8.setStatus("mandatory")
_Metro1500MUX_DMX_ObjectIdentity = ObjectIdentity
metro1500MUX_DMX = _Metro1500MUX_DMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30)
)
_Metro1500MUX_DMX_Table_Object = MibTable
metro1500MUX_DMX_Table = _Metro1500MUX_DMX_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1)
)
if mibBuilder.loadTexts:
    metro1500MUX_DMX_Table.setStatus("mandatory")
_Metro1500MUX_DMX_Entry_Object = MibTableRow
metro1500MUX_DMX_Entry = _Metro1500MUX_DMX_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1)
)
metro1500MUX_DMX_Entry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500MUX_DMX_Number"),
)
if mibBuilder.loadTexts:
    metro1500MUX_DMX_Entry.setStatus("mandatory")
_Metro1500MUX_DMX_Number_Type = Metro1500SlotNumberRange
_Metro1500MUX_DMX_Number_Object = MibTableColumn
metro1500MUX_DMX_Number = _Metro1500MUX_DMX_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 1),
    _Metro1500MUX_DMX_Number_Type()
)
metro1500MUX_DMX_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MUX_DMX_Number.setStatus("mandatory")


class _Metro1500MUX_DMX_WDMType_Type(Integer32):
    """Custom type metro1500MUX_DMX_WDMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mux", 1),
          ("dmux", 2),
          ("mux_dmux", 3),
          ("mux_dmux_hotstandby", 4))
    )


_Metro1500MUX_DMX_WDMType_Type.__name__ = "Integer32"
_Metro1500MUX_DMX_WDMType_Object = MibTableColumn
metro1500MUX_DMX_WDMType = _Metro1500MUX_DMX_WDMType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 2),
    _Metro1500MUX_DMX_WDMType_Type()
)
metro1500MUX_DMX_WDMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MUX_DMX_WDMType.setStatus("mandatory")


class _Metro1500MUX_DMX_Scheme_Type(Integer32):
    """Custom type metro1500MUX_DMX_Scheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cwdm_r1", 1),
          ("cwdm_r2", 2),
          ("dwdm_r1", 3),
          ("dwdm_r2", 4))
    )


_Metro1500MUX_DMX_Scheme_Type.__name__ = "Integer32"
_Metro1500MUX_DMX_Scheme_Object = MibTableColumn
metro1500MUX_DMX_Scheme = _Metro1500MUX_DMX_Scheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 3),
    _Metro1500MUX_DMX_Scheme_Type()
)
metro1500MUX_DMX_Scheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MUX_DMX_Scheme.setStatus("mandatory")


class _Metro1500MUX_DMX_ChannelRange_Type(Integer32):
    """Custom type metro1500MUX_DMX_ChannelRange based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("channel1to4", 1),
          ("channel5to8", 2),
          ("channel9to12", 3),
          ("channel13to16", 4),
          ("channel17to20", 5),
          ("channel21to24", 6),
          ("channel25to28", 7),
          ("channel29to32", 8),
          ("channel1to8", 9),
          ("channel9to16", 10),
          ("channel17to24", 11),
          ("channel25to32", 12),
          ("channel_M1to4_D17to20", 13),
          ("channel_M5to8_D21to24", 14),
          ("channel_M9to12_D25to28", 15),
          ("channel_M13to16_D29to32", 16),
          ("channel_M17to20_D1to4", 17),
          ("channel_M21to24_D5to8", 18),
          ("channel_M25to28_D9to12", 19),
          ("channel_M29to32_D13to16", 20))
    )


_Metro1500MUX_DMX_ChannelRange_Type.__name__ = "Integer32"
_Metro1500MUX_DMX_ChannelRange_Object = MibTableColumn
metro1500MUX_DMX_ChannelRange = _Metro1500MUX_DMX_ChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 4),
    _Metro1500MUX_DMX_ChannelRange_Type()
)
metro1500MUX_DMX_ChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MUX_DMX_ChannelRange.setStatus("mandatory")
_Metro1500MUX_DMX_Connector_Type = DisplayString
_Metro1500MUX_DMX_Connector_Object = MibTableColumn
metro1500MUX_DMX_Connector = _Metro1500MUX_DMX_Connector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 5),
    _Metro1500MUX_DMX_Connector_Type()
)
metro1500MUX_DMX_Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MUX_DMX_Connector.setStatus("mandatory")
_Metro1500MUX_DMX_UpgradePort_Type = DisplayString
_Metro1500MUX_DMX_UpgradePort_Object = MibTableColumn
metro1500MUX_DMX_UpgradePort = _Metro1500MUX_DMX_UpgradePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 6),
    _Metro1500MUX_DMX_UpgradePort_Type()
)
metro1500MUX_DMX_UpgradePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MUX_DMX_UpgradePort.setStatus("mandatory")
_Metro1500BSM_ObjectIdentity = ObjectIdentity
metro1500BSM = _Metro1500BSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31)
)
_Metro1500BSM_Table_Object = MibTable
metro1500BSM_Table = _Metro1500BSM_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1)
)
if mibBuilder.loadTexts:
    metro1500BSM_Table.setStatus("mandatory")
_Metro1500BSM_Entry_Object = MibTableRow
metro1500BSM_Entry = _Metro1500BSM_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1)
)
metro1500BSM_Entry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500BSM_Number"),
)
if mibBuilder.loadTexts:
    metro1500BSM_Entry.setStatus("mandatory")
_Metro1500BSM_Number_Type = Metro1500SlotNumberRange
_Metro1500BSM_Number_Object = MibTableColumn
metro1500BSM_Number = _Metro1500BSM_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 1),
    _Metro1500BSM_Number_Type()
)
metro1500BSM_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500BSM_Number.setStatus("mandatory")


class _Metro1500BSM_Scheme_Type(Integer32):
    """Custom type metro1500BSM_Scheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dwdm_r1", 1),
          ("dwdm_r2", 2))
    )


_Metro1500BSM_Scheme_Type.__name__ = "Integer32"
_Metro1500BSM_Scheme_Object = MibTableColumn
metro1500BSM_Scheme = _Metro1500BSM_Scheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 2),
    _Metro1500BSM_Scheme_Type()
)
metro1500BSM_Scheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500BSM_Scheme.setStatus("mandatory")


class _Metro1500BSM_BandRange_Type(Integer32):
    """Custom type metro1500BSM_BandRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bandLC1to4", 1),
          ("bandLC1_3_5_7", 2),
          ("bandC1to4", 3),
          ("bandL5to8", 4),
          ("band_MC1to4_DL5to8", 5),
          ("band_ML5to8_DC1to4", 6))
    )


_Metro1500BSM_BandRange_Type.__name__ = "Integer32"
_Metro1500BSM_BandRange_Object = MibTableColumn
metro1500BSM_BandRange = _Metro1500BSM_BandRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 3),
    _Metro1500BSM_BandRange_Type()
)
metro1500BSM_BandRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500BSM_BandRange.setStatus("mandatory")
_Metro1500BSM_ConnectorType_Type = DisplayString
_Metro1500BSM_ConnectorType_Object = MibTableColumn
metro1500BSM_ConnectorType = _Metro1500BSM_ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 4),
    _Metro1500BSM_ConnectorType_Type()
)
metro1500BSM_ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500BSM_ConnectorType.setStatus("mandatory")
_Metro1500Trap_ObjectIdentity = ObjectIdentity
metro1500Trap = _Metro1500Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100)
)

# Managed Objects groups


# Notification objects

metro1500HardwareAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 1)
)
metro1500HardwareAdded.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HardwareAdded.setStatus(
        ""
    )

metro1500HardwareDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 2)
)
metro1500HardwareDeleted.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HardwareDeleted.setStatus(
        ""
    )

metro1500PSNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 3)
)
metro1500PSNotFail.setObjects(
    ("METRO1500-MIB", "metro1500PSNumber")
)
if mibBuilder.loadTexts:
    metro1500PSNotFail.setStatus(
        ""
    )

metro1500PSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 4)
)
metro1500PSFail.setObjects(
    ("METRO1500-MIB", "metro1500PSNumber")
)
if mibBuilder.loadTexts:
    metro1500PSFail.setStatus(
        ""
    )

metro1500FanNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 5)
)
metro1500FanNotFail.setObjects(
    ("METRO1500-MIB", "metro1500FanNumber")
)
if mibBuilder.loadTexts:
    metro1500FanNotFail.setStatus(
        ""
    )

metro1500FanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 6)
)
metro1500FanFail.setObjects(
    ("METRO1500-MIB", "metro1500FanNumber")
)
if mibBuilder.loadTexts:
    metro1500FanFail.setStatus(
        ""
    )

metro1500BusNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 7)
)
if mibBuilder.loadTexts:
    metro1500BusNotFail.setStatus(
        ""
    )

metro1500BusFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 8)
)
if mibBuilder.loadTexts:
    metro1500BusFail.setStatus(
        ""
    )

metro1500ConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 9)
)
if mibBuilder.loadTexts:
    metro1500ConfigMismatch.setStatus(
        ""
    )

metro1500RxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 20)
)
metro1500RxLocOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxLocOn.setStatus(
        ""
    )

metro1500RxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 21)
)
metro1500RxLocOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxLocOff.setStatus(
        ""
    )

metro1500TxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 22)
)
metro1500TxLocOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxLocOn.setStatus(
        ""
    )

metro1500TxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 23)
)
metro1500TxLocOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxLocOff.setStatus(
        ""
    )

metro1500RxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 24)
)
metro1500RxRemOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRemOn.setStatus(
        ""
    )

metro1500RxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 25)
)
metro1500RxRemOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRemOff.setStatus(
        ""
    )

metro1500TxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 26)
)
metro1500TxRemOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRemOn.setStatus(
        ""
    )

metro1500TxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 27)
)
metro1500TxRemOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRemOff.setStatus(
        ""
    )

metro1500RxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 28)
)
metro1500RxRem2On.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRem2On.setStatus(
        ""
    )

metro1500RxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 29)
)
metro1500RxRem2Off.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRem2Off.setStatus(
        ""
    )

metro1500TxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 30)
)
metro1500TxRem2On.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRem2On.setStatus(
        ""
    )

metro1500TxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 31)
)
metro1500TxRem2Off.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRem2Off.setStatus(
        ""
    )

metro1500ClockNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 32)
)
metro1500ClockNoFail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500ClockNoFail.setStatus(
        ""
    )

metro1500ClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 33)
)
metro1500ClockFail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500ClockFail.setStatus(
        ""
    )

metro1500ClockChangeFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 34)
)
metro1500ClockChangeFrequency.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500ClockChangeFrequency.setStatus(
        ""
    )

metro1500LocLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 35)
)
metro1500LocLoopOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500LocLoopOn.setStatus(
        ""
    )

metro1500LocLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 36)
)
metro1500LocLoopOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500LocLoopOff.setStatus(
        ""
    )

metro1500RemLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 37)
)
metro1500RemLoopOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemLoopOn.setStatus(
        ""
    )

metro1500RemLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 38)
)
metro1500RemLoopOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemLoopOff.setStatus(
        ""
    )

metro1500switchReferenceLaserOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 40)
)
metro1500switchReferenceLaserOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchReferenceLaserOn.setStatus(
        ""
    )

metro1500switchReferenceLaserOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 41)
)
metro1500switchReferenceLaserOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchReferenceLaserOff.setStatus(
        ""
    )

metro1500switchToA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 42)
)
metro1500switchToA.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchToA.setStatus(
        ""
    )

metro1500switchToB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 43)
)
metro1500switchToB.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchToB.setStatus(
        ""
    )

metro1500switchAutomatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 44)
)
metro1500switchAutomatic.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchAutomatic.setStatus(
        ""
    )

metro1500switchLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 45)
)
metro1500switchLocked.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLocked.setStatus(
        ""
    )

metro1500switchLineAavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 46)
)
metro1500switchLineAavail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineAavail.setStatus(
        ""
    )

metro1500switchLineANotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 47)
)
metro1500switchLineANotAvail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineANotAvail.setStatus(
        ""
    )

metro1500switchLineBavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 48)
)
metro1500switchLineBavail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineBavail.setStatus(
        ""
    )

metro1500switchLineBNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 49)
)
metro1500switchLineBNotAvail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineBNotAvail.setStatus(
        ""
    )

metro1500repeatedMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 50)
)
metro1500repeatedMessage.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500repeatedMessage.setStatus(
        ""
    )

metro1500INNCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 51)
)
if mibBuilder.loadTexts:
    metro1500INNCDown.setStatus(
        ""
    )

metro1500INNCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 52)
)
if mibBuilder.loadTexts:
    metro1500INNCUp.setStatus(
        ""
    )

metro1500switchAutoLaserShutdownOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 53)
)
metro1500switchAutoLaserShutdownOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchAutoLaserShutdownOn.setStatus(
        ""
    )

metro1500switchAutoLaserShutdownOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 54)
)
metro1500switchAutoLaserShutdownOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchAutoLaserShutdownOff.setStatus(
        ""
    )

metro1500NEMIAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 55)
)
metro1500NEMIAuthFail.setObjects(
      *(("METRO1500-MIB", "metro1500MainLastAuthFailSource"),
        ("METRO1500-MIB", "metro1500MainLastAuthFailDescription"))
)
if mibBuilder.loadTexts:
    metro1500NEMIAuthFail.setStatus(
        ""
    )

metro1500EthernetPortEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 60)
)
metro1500EthernetPortEnable.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortEnable.setStatus(
        ""
    )

metro1500EthernetPortDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 61)
)
metro1500EthernetPortDisable.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortDisable.setStatus(
        ""
    )

metro1500EthernetPortPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 62)
)
metro1500EthernetPortPartitioned.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortPartitioned.setStatus(
        ""
    )

metro1500EthernetPortNotPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 63)
)
metro1500EthernetPortNotPartitioned.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortNotPartitioned.setStatus(
        ""
    )

metro1500EthernetPortLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 64)
)
metro1500EthernetPortLinkPulses.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortLinkPulses.setStatus(
        ""
    )

metro1500EthernetPortNoLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 65)
)
metro1500EthernetPortNoLinkPulses.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortNoLinkPulses.setStatus(
        ""
    )

metro1500TDMRemoteSyncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 70)
)
metro1500TDMRemoteSyncLoss.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMRemoteSyncLoss.setStatus(
        ""
    )

metro1500TDMRemoteSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 71)
)
metro1500TDMRemoteSync.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMRemoteSync.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 72)
)
metro1500TDMLocModuleEnabled1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled1.setStatus(
        ""
    )

metro1500TDMLocModuleDisable1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 73)
)
metro1500TDMLocModuleDisable1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable1.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 74)
)
metro1500TDMLocModuleEnabled2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled2.setStatus(
        ""
    )

metro1500TDMLocModuleDisable2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 75)
)
metro1500TDMLocModuleDisable2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable2.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 76)
)
metro1500TDMLocModuleEnabled3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled3.setStatus(
        ""
    )

metro1500TDMLocModuleDisable3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 77)
)
metro1500TDMLocModuleDisable3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable3.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 78)
)
metro1500TDMLocModuleEnabled4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled4.setStatus(
        ""
    )

metro1500TDMLocModuleDisable4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 79)
)
metro1500TDMLocModuleDisable4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable4.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 80)
)
metro1500TDMLocModuleEnabled5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled5.setStatus(
        ""
    )

metro1500TDMLocModuleDisable5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 81)
)
metro1500TDMLocModuleDisable5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable5.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 82)
)
metro1500TDMLocModuleEnabled6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled6.setStatus(
        ""
    )

metro1500TDMLocModuleDisable6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 83)
)
metro1500TDMLocModuleDisable6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable6.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 84)
)
metro1500TDMLocModuleEnabled7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled7.setStatus(
        ""
    )

metro1500TDMLocModuleDisable7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 85)
)
metro1500TDMLocModuleDisable7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable7.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 86)
)
metro1500TDMLocModuleEnabled8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled8.setStatus(
        ""
    )

metro1500TDMLocModuleDisable8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 87)
)
metro1500TDMLocModuleDisable8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable8.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 88)
)
metro1500TDMLocModuleRxOn1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn1.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 89)
)
metro1500TDMLocModuleRxOff1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff1.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 90)
)
metro1500TDMLocModuleRxOn2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn2.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 91)
)
metro1500TDMLocModuleRxOff2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff2.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 92)
)
metro1500TDMLocModuleRxOn3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn3.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 93)
)
metro1500TDMLocModuleRxOff3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff3.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 94)
)
metro1500TDMLocModuleRxOn4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn4.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 95)
)
metro1500TDMLocModuleRxOff4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff4.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 96)
)
metro1500TDMLocModuleRxOn5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn5.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 97)
)
metro1500TDMLocModuleRxOff5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff5.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 98)
)
metro1500TDMLocModuleRxOn6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn6.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 99)
)
metro1500TDMLocModuleRxOff6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff6.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 100)
)
metro1500TDMLocModuleRxOn7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn7.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 101)
)
metro1500TDMLocModuleRxOff7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff7.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 102)
)
metro1500TDMLocModuleRxOn8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn8.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 103)
)
metro1500TDMLocModuleRxOff8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff8.setStatus(
        ""
    )

metro1500TDMLocModuleData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 104)
)
metro1500TDMLocModuleData1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData1.setStatus(
        ""
    )

metro1500TDMLocModuleNoData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 105)
)
metro1500TDMLocModuleNoData1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData1.setStatus(
        ""
    )

metro1500TDMLocModuleData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 106)
)
metro1500TDMLocModuleData2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData2.setStatus(
        ""
    )

metro1500TDMLocModuleNoData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 107)
)
metro1500TDMLocModuleNoData2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData2.setStatus(
        ""
    )

metro1500TDMLocModuleData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 108)
)
metro1500TDMLocModuleData3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData3.setStatus(
        ""
    )

metro1500TDMLocModuleNoData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 109)
)
metro1500TDMLocModuleNoData3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData3.setStatus(
        ""
    )

metro1500TDMLocModuleData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 110)
)
metro1500TDMLocModuleData4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData4.setStatus(
        ""
    )

metro1500TDMLocModuleNoData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 111)
)
metro1500TDMLocModuleNoData4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData4.setStatus(
        ""
    )

metro1500TDMLocModuleData5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 112)
)
metro1500TDMLocModuleData5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData5.setStatus(
        ""
    )

metro1500TDMLocModuleNoData5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 113)
)
metro1500TDMLocModuleNoData5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData5.setStatus(
        ""
    )

metro1500TDMLocModuleData6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 114)
)
metro1500TDMLocModuleData6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData6.setStatus(
        ""
    )

metro1500TDMLocModuleNoData6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 115)
)
metro1500TDMLocModuleNoData6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData6.setStatus(
        ""
    )

metro1500TDMLocModuleData7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 116)
)
metro1500TDMLocModuleData7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData7.setStatus(
        ""
    )

metro1500TDMLocModuleNoData7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 117)
)
metro1500TDMLocModuleNoData7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData7.setStatus(
        ""
    )

metro1500TDMLocModuleData8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 118)
)
metro1500TDMLocModuleData8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData8.setStatus(
        ""
    )

metro1500TDMLocModuleNoData8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 119)
)
metro1500TDMLocModuleNoData8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData8.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 120)
)
metro1500TDMLocModuleClockFail1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail1.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 121)
)
metro1500TDMLocModuleClockNoFail1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail1.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 122)
)
metro1500TDMLocModuleClockFail2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail2.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 123)
)
metro1500TDMLocModuleClockNoFail2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail2.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 124)
)
metro1500TDMLocModuleClockFail3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail3.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 125)
)
metro1500TDMLocModuleClockNoFail3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail3.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 126)
)
metro1500TDMLocModuleClockFail4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail4.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 127)
)
metro1500TDMLocModuleClockNoFail4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail4.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 128)
)
metro1500TDMLocModuleClockFail5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail5.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 129)
)
metro1500TDMLocModuleClockNoFail5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail5.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 130)
)
metro1500TDMLocModuleClockFail6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail6.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 131)
)
metro1500TDMLocModuleClockNoFail6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail6.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 132)
)
metro1500TDMLocModuleClockFail7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail7.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 133)
)
metro1500TDMLocModuleClockNoFail7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail7.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 134)
)
metro1500TDMLocModuleClockFail8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail8.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 135)
)
metro1500TDMLocModuleClockNoFail8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail8.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 136)
)
metro1500TDMLocModuleClockChange1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange1.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 137)
)
metro1500TDMLocModuleClockChange2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange2.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 138)
)
metro1500TDMLocModuleClockChange3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange3.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 139)
)
metro1500TDMLocModuleClockChange4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange4.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 140)
)
metro1500TDMLocModuleClockChange5.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange5.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 141)
)
metro1500TDMLocModuleClockChange6.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange6.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 142)
)
metro1500TDMLocModuleClockChange7.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange7.setStatus(
        ""
    )

metro1500TDMLocModuleClockChange8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 143)
)
metro1500TDMLocModuleClockChange8.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockChange8.setStatus(
        ""
    )

metro1500RemoteClockNoSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 170)
)
metro1500RemoteClockNoSync.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemoteClockNoSync.setStatus(
        ""
    )

metro1500RemoteClockSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 171)
)
metro1500RemoteClockSync.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemoteClockSync.setStatus(
        ""
    )

metro1500RemoteClock2NoSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 172)
)
metro1500RemoteClock2NoSync.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemoteClock2NoSync.setStatus(
        ""
    )

metro1500RemoteClock2Sync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 173)
)
metro1500RemoteClock2Sync.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemoteClock2Sync.setStatus(
        ""
    )

metro1500RegeneratorModeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 180)
)
metro1500RegeneratorModeOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RegeneratorModeOn.setStatus(
        ""
    )

metro1500RegeneratorModeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 181)
)
metro1500RegeneratorModeOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RegeneratorModeOff.setStatus(
        ""
    )

metro1500RSM_OSC_OSCOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 210)
)
metro1500RSM_OSC_OSCOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RSM_OSC_OSCOn.setStatus(
        ""
    )

metro1500RSM_OSC_OSCOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 211)
)
metro1500RSM_OSC_OSCOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RSM_OSC_OSCOff.setStatus(
        ""
    )

metro1500EthernetPortSpeed10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 220)
)
metro1500EthernetPortSpeed10.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortSpeed10.setStatus(
        ""
    )

metro1500EthernetPortSpeed100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 221)
)
metro1500EthernetPortSpeed100.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortSpeed100.setStatus(
        ""
    )

metro1500EthernetPortDuplexHalf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 222)
)
metro1500EthernetPortDuplexHalf.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortDuplexHalf.setStatus(
        ""
    )

metro1500EthernetPortDuplexFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 223)
)
metro1500EthernetPortDuplexFull.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortDuplexFull.setStatus(
        ""
    )

metro1500EthernetPortAutonegotiationOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 224)
)
metro1500EthernetPortAutonegotiationOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortAutonegotiationOn.setStatus(
        ""
    )

metro1500EthernetPortAutonegotiationOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 225)
)
metro1500EthernetPortAutonegotiationOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortAutonegotiationOff.setStatus(
        ""
    )

metro1500EthernetPortPolarityPositive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 226)
)
metro1500EthernetPortPolarityPositive.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortPolarityPositive.setStatus(
        ""
    )

metro1500EthernetPortPolarityNegative = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 227)
)
metro1500EthernetPortPolarityNegative.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetPortPolarityNegative.setStatus(
        ""
    )

metro1500HotStandby_Change2LineA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 240)
)
metro1500HotStandby_Change2LineA.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HotStandby_Change2LineA.setStatus(
        ""
    )

metro1500HotStandby_Change2LineB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 241)
)
metro1500HotStandby_Change2LineB.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HotStandby_Change2LineB.setStatus(
        ""
    )

metro1500HotStandby_Locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 242)
)
metro1500HotStandby_Locked.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HotStandby_Locked.setStatus(
        ""
    )

metro1500HotStandby_Automatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 243)
)
metro1500HotStandby_Automatic.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HotStandby_Automatic.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "METRO1500-MIB",
    **{"Metro1500SlotNumberRange": Metro1500SlotNumberRange,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "adva": adva,
       "products": products,
       "metro1500": metro1500,
       "metro1500Main": metro1500Main,
       "metro1500Housing": metro1500Housing,
       "metro1500Manufacturer": metro1500Manufacturer,
       "metro1500MainType": metro1500MainType,
       "metro1500MainSerialNumber": metro1500MainSerialNumber,
       "metro1500MainHardwareVersion": metro1500MainHardwareVersion,
       "metro1500MainSoftwareVersion": metro1500MainSoftwareVersion,
       "metro1500MainBusMessages": metro1500MainBusMessages,
       "metro1500MainBusErrors": metro1500MainBusErrors,
       "metro1500MainLastEvent": metro1500MainLastEvent,
       "metro1500MainMotd": metro1500MainMotd,
       "metro1500MainTrapsinkTable": metro1500MainTrapsinkTable,
       "metro1500MainTrapsinkEntry": metro1500MainTrapsinkEntry,
       "metro1500MainTrapsinkNumber": metro1500MainTrapsinkNumber,
       "metro1500MainTrapsinkAddress": metro1500MainTrapsinkAddress,
       "metro1500MainTrapsinkCommunity": metro1500MainTrapsinkCommunity,
       "metro1500MainTrapsinkPriority": metro1500MainTrapsinkPriority,
       "metro1500MainLogfileTable": metro1500MainLogfileTable,
       "metro1500MainLogfileEntry": metro1500MainLogfileEntry,
       "metro1500MainLogfileNumber": metro1500MainLogfileNumber,
       "metro1500MainLogfileName": metro1500MainLogfileName,
       "metro1500MainLogfileSize": metro1500MainLogfileSize,
       "metro1500MainLogfilePriority": metro1500MainLogfilePriority,
       "metro1500MainProtocolVersion": metro1500MainProtocolVersion,
       "metro1500MainSystemVersion": metro1500MainSystemVersion,
       "metro1500MainConfigMismatch": metro1500MainConfigMismatch,
       "metro1500MainLastAuthFailSource": metro1500MainLastAuthFailSource,
       "metro1500MainLastAuthFailDescription": metro1500MainLastAuthFailDescription,
       "metro1500SlotTable": metro1500SlotTable,
       "metro1500SlotEntry": metro1500SlotEntry,
       "metro1500SlotNumber": metro1500SlotNumber,
       "metro1500Type": metro1500Type,
       "metro1500SlotTypeNumber": metro1500SlotTypeNumber,
       "metro1500SerialNumber": metro1500SerialNumber,
       "metro1500HardwareVersion": metro1500HardwareVersion,
       "metro1500SoftwareVersion": metro1500SoftwareVersion,
       "metro1500Temperature": metro1500Temperature,
       "metro1500BoardVoltage": metro1500BoardVoltage,
       "metro1500DetailInfo": metro1500DetailInfo,
       "metro1500EPLDVersion": metro1500EPLDVersion,
       "metro1500CustomerLabel": metro1500CustomerLabel,
       "metro1500ProductionVersion": metro1500ProductionVersion,
       "metro1500SlotSubType": metro1500SlotSubType,
       "metro1500SlotAlias": metro1500SlotAlias,
       "metro1500SlotComment": metro1500SlotComment,
       "metro1500PSTable": metro1500PSTable,
       "metro1500PSEntry": metro1500PSEntry,
       "metro1500PSNumber": metro1500PSNumber,
       "metro1500PSOn": metro1500PSOn,
       "metro1500FanTable": metro1500FanTable,
       "metro1500FanEntry": metro1500FanEntry,
       "metro1500FanNumber": metro1500FanNumber,
       "metro1500FanOn": metro1500FanOn,
       "metro1500Converter": metro1500Converter,
       "metro1500ConverterTable": metro1500ConverterTable,
       "metro1500ConverterEntry": metro1500ConverterEntry,
       "metro1500ConverterNumber": metro1500ConverterNumber,
       "metro1500RxLoc": metro1500RxLoc,
       "metro1500TxLoc": metro1500TxLoc,
       "metro1500TxLocC": metro1500TxLocC,
       "metro1500TxLocTemp": metro1500TxLocTemp,
       "metro1500RxRem": metro1500RxRem,
       "metro1500TxRem": metro1500TxRem,
       "metro1500TxRemC": metro1500TxRemC,
       "metro1500TxRemTemp": metro1500TxRemTemp,
       "metro1500RxRem2": metro1500RxRem2,
       "metro1500ClockState": metro1500ClockState,
       "metro1500ClockFreq": metro1500ClockFreq,
       "metro1500LocLoop": metro1500LocLoop,
       "metro1500RemLoop": metro1500RemLoop,
       "metro1500ClockType": metro1500ClockType,
       "metro1500HotStandby_ActiveLine": metro1500HotStandby_ActiveLine,
       "metro1500HotStandby_LineLocked": metro1500HotStandby_LineLocked,
       "metro1500LocalConnector": metro1500LocalConnector,
       "metro1500LocalLaserType": metro1500LocalLaserType,
       "metro1500RemoteConnector": metro1500RemoteConnector,
       "metro1500RemoteLaserType": metro1500RemoteLaserType,
       "metro1500ConverterType": metro1500ConverterType,
       "metro1500ClockRecovery": metro1500ClockRecovery,
       "metro1500SupportedDataRateTransparent": metro1500SupportedDataRateTransparent,
       "metro1500SupportedDataRateClocked": metro1500SupportedDataRateClocked,
       "metro1500ChannelNumber": metro1500ChannelNumber,
       "metro1500RemoteClockState": metro1500RemoteClockState,
       "metro1500RemoteClockState2": metro1500RemoteClockState2,
       "metro1500RegeneratorMode": metro1500RegeneratorMode,
       "metro1500Switch": metro1500Switch,
       "metro1500SwitchTable": metro1500SwitchTable,
       "metro1500SwitchEntry": metro1500SwitchEntry,
       "metro1500SwitchNumber": metro1500SwitchNumber,
       "metro1500SwitchLine": metro1500SwitchLine,
       "metro1500SwitchMode": metro1500SwitchMode,
       "metro1500SwitchLaserOn": metro1500SwitchLaserOn,
       "metro1500SwitchLineAavail": metro1500SwitchLineAavail,
       "metro1500SwitchLineBavail": metro1500SwitchLineBavail,
       "metro1500SwitchAutoLaserShutdown": metro1500SwitchAutoLaserShutdown,
       "metro1500SwitchConnector": metro1500SwitchConnector,
       "metro1500SwitchRemoteLaserType": metro1500SwitchRemoteLaserType,
       "metro1500RSM_OSC": metro1500RSM_OSC,
       "metro1500RSM_Table": metro1500RSM_Table,
       "metro1500RSM_Entry": metro1500RSM_Entry,
       "metro1500RSM_Number": metro1500RSM_Number,
       "metro1500RSM_Line": metro1500RSM_Line,
       "metro1500RSM_Mode": metro1500RSM_Mode,
       "metro1500RSM_LaserOn": metro1500RSM_LaserOn,
       "metro1500RSM_LineAavail": metro1500RSM_LineAavail,
       "metro1500RSM_LineBavail": metro1500RSM_LineBavail,
       "metro1500RSM_Control": metro1500RSM_Control,
       "metro1500RSM_Connector": metro1500RSM_Connector,
       "metro1500RSM_RemoteLaserType": metro1500RSM_RemoteLaserType,
       "metro1500OSC_Table": metro1500OSC_Table,
       "metro1500OSC_Entry": metro1500OSC_Entry,
       "metro1500OSC_Number": metro1500OSC_Number,
       "metro1500OSC_LaserOn": metro1500OSC_LaserOn,
       "metro1500OSC_P1_fail": metro1500OSC_P1_fail,
       "metro1500OSC_P2_fail": metro1500OSC_P2_fail,
       "metro1500OSC_PortEnable1": metro1500OSC_PortEnable1,
       "metro1500OSC_PortSpeed1": metro1500OSC_PortSpeed1,
       "metro1500OSC_PortDuplex1": metro1500OSC_PortDuplex1,
       "metro1500OSC_PortAutoneg1": metro1500OSC_PortAutoneg1,
       "metro1500OSC_PortPolarity1": metro1500OSC_PortPolarity1,
       "metro1500OSC_PortLinkStatus1": metro1500OSC_PortLinkStatus1,
       "metro1500OSC_PortEnable2": metro1500OSC_PortEnable2,
       "metro1500OSC_PortSpeed2": metro1500OSC_PortSpeed2,
       "metro1500OSC_PortDuplex2": metro1500OSC_PortDuplex2,
       "metro1500OSC_PortAutoneg2": metro1500OSC_PortAutoneg2,
       "metro1500OSC_PortPolarity2": metro1500OSC_PortPolarity2,
       "metro1500OSC_PortLinkStatus2": metro1500OSC_PortLinkStatus2,
       "metro1500OSC_PortEnable3": metro1500OSC_PortEnable3,
       "metro1500OSC_PortSpeed3": metro1500OSC_PortSpeed3,
       "metro1500OSC_PortDuplex3": metro1500OSC_PortDuplex3,
       "metro1500OSC_PortAutoneg3": metro1500OSC_PortAutoneg3,
       "metro1500OSC_PortPolarity3": metro1500OSC_PortPolarity3,
       "metro1500OSC_PortLinkStatus3": metro1500OSC_PortLinkStatus3,
       "metro1500OSC_PortEnable4": metro1500OSC_PortEnable4,
       "metro1500OSC_PortSpeed4": metro1500OSC_PortSpeed4,
       "metro1500OSC_PortDuplex4": metro1500OSC_PortDuplex4,
       "metro1500OSC_PortAutoneg4": metro1500OSC_PortAutoneg4,
       "metro1500OSC_PortPolarity4": metro1500OSC_PortPolarity4,
       "metro1500OSC_PortLinkStatus4": metro1500OSC_PortLinkStatus4,
       "metro1500OSC_PortEnable5": metro1500OSC_PortEnable5,
       "metro1500OSC_PortSpeed5": metro1500OSC_PortSpeed5,
       "metro1500OSC_PortDuplex5": metro1500OSC_PortDuplex5,
       "metro1500OSC_PortAutoneg5": metro1500OSC_PortAutoneg5,
       "metro1500OSC_PortPolarity5": metro1500OSC_PortPolarity5,
       "metro1500OSC_PortLinkStatus5": metro1500OSC_PortLinkStatus5,
       "metro1500OSC_PortEnable6": metro1500OSC_PortEnable6,
       "metro1500OSC_PortSpeed6": metro1500OSC_PortSpeed6,
       "metro1500OSC_PortDuplex6": metro1500OSC_PortDuplex6,
       "metro1500OSC_PortLinkStatus6": metro1500OSC_PortLinkStatus6,
       "metro1500OSC_Connector": metro1500OSC_Connector,
       "metro1500OSC_RemoteLaserType": metro1500OSC_RemoteLaserType,
       "metro1500EthernetHub": metro1500EthernetHub,
       "metro1500EthernetHubTable": metro1500EthernetHubTable,
       "metro1500EthernetHubEntry": metro1500EthernetHubEntry,
       "metro1500EthernetHubNumber": metro1500EthernetHubNumber,
       "metro1500EthernetHubPortEnable1": metro1500EthernetHubPortEnable1,
       "metro1500EthernetHubPortPartitionStatus1": metro1500EthernetHubPortPartitionStatus1,
       "metro1500EthernetHubPortLinkStatus1": metro1500EthernetHubPortLinkStatus1,
       "metro1500EthernetHubPortPolarity1": metro1500EthernetHubPortPolarity1,
       "metro1500EthernetHubPortEnable2": metro1500EthernetHubPortEnable2,
       "metro1500EthernetHubPortPartitionStatus2": metro1500EthernetHubPortPartitionStatus2,
       "metro1500EthernetHubPortLinkStatus2": metro1500EthernetHubPortLinkStatus2,
       "metro1500EthernetHubPortPolarity2": metro1500EthernetHubPortPolarity2,
       "metro1500EthernetHubPortEnable3": metro1500EthernetHubPortEnable3,
       "metro1500EthernetHubPortPartitionStatus3": metro1500EthernetHubPortPartitionStatus3,
       "metro1500EthernetHubPortLinkStatus3": metro1500EthernetHubPortLinkStatus3,
       "metro1500EthernetHubPortPolarity3": metro1500EthernetHubPortPolarity3,
       "metro1500EthernetHubPortEnable4": metro1500EthernetHubPortEnable4,
       "metro1500EthernetHubPortPartitionStatus4": metro1500EthernetHubPortPartitionStatus4,
       "metro1500EthernetHubPortLinkStatus4": metro1500EthernetHubPortLinkStatus4,
       "metro1500EthernetHubPortPolarity4": metro1500EthernetHubPortPolarity4,
       "metro1500EthernetHubPortEnable5": metro1500EthernetHubPortEnable5,
       "metro1500EthernetHubPortPartitionStatus5": metro1500EthernetHubPortPartitionStatus5,
       "metro1500EthernetHubPortLinkStatus5": metro1500EthernetHubPortLinkStatus5,
       "metro1500EthernetHubPortPolarity5": metro1500EthernetHubPortPolarity5,
       "metro1500TDM": metro1500TDM,
       "metro1500TDMTable": metro1500TDMTable,
       "metro1500TDMEntry": metro1500TDMEntry,
       "metro1500TDMNumber": metro1500TDMNumber,
       "metro1500TDMRxRem": metro1500TDMRxRem,
       "metro1500TDMRxSync": metro1500TDMRxSync,
       "metro1500TDMTxRem": metro1500TDMTxRem,
       "metro1500TDMTxRemC": metro1500TDMTxRemC,
       "metro1500TDMTxRemTemp": metro1500TDMTxRemTemp,
       "metro1500TDMLocLoop": metro1500TDMLocLoop,
       "metro1500TDMClockType": metro1500TDMClockType,
       "metro1500TDMLocModuleInst1": metro1500TDMLocModuleInst1,
       "metro1500TDMLocModuleEnable1": metro1500TDMLocModuleEnable1,
       "metro1500TDMLocModuleRx1": metro1500TDMLocModuleRx1,
       "metro1500TDMLocModuleTx1": metro1500TDMLocModuleTx1,
       "metro1500TDMLocModuleRemoteData1": metro1500TDMLocModuleRemoteData1,
       "metro1500TDMLocModuleClockFrequency1": metro1500TDMLocModuleClockFrequency1,
       "metro1500TDMLocModuleClockError1": metro1500TDMLocModuleClockError1,
       "metro1500TDMLocModuleInst2": metro1500TDMLocModuleInst2,
       "metro1500TDMLocModuleEnable2": metro1500TDMLocModuleEnable2,
       "metro1500TDMLocModuleRx2": metro1500TDMLocModuleRx2,
       "metro1500TDMLocModuleTx2": metro1500TDMLocModuleTx2,
       "metro1500TDMLocModuleRemoteData2": metro1500TDMLocModuleRemoteData2,
       "metro1500TDMLocModuleClockFrequency2": metro1500TDMLocModuleClockFrequency2,
       "metro1500TDMLocModuleClockError2": metro1500TDMLocModuleClockError2,
       "metro1500TDMLocModuleInst3": metro1500TDMLocModuleInst3,
       "metro1500TDMLocModuleEnable3": metro1500TDMLocModuleEnable3,
       "metro1500TDMLocModuleRx3": metro1500TDMLocModuleRx3,
       "metro1500TDMLocModuleTx3": metro1500TDMLocModuleTx3,
       "metro1500TDMLocModuleRemoteData3": metro1500TDMLocModuleRemoteData3,
       "metro1500TDMLocModuleClockFrequency3": metro1500TDMLocModuleClockFrequency3,
       "metro1500TDMLocModuleClockError3": metro1500TDMLocModuleClockError3,
       "metro1500TDMLocModuleInst4": metro1500TDMLocModuleInst4,
       "metro1500TDMLocModuleEnable4": metro1500TDMLocModuleEnable4,
       "metro1500TDMLocModuleRx4": metro1500TDMLocModuleRx4,
       "metro1500TDMLocModuleTx4": metro1500TDMLocModuleTx4,
       "metro1500TDMLocModuleRemoteData4": metro1500TDMLocModuleRemoteData4,
       "metro1500TDMLocModuleClockFrequency4": metro1500TDMLocModuleClockFrequency4,
       "metro1500TDMLocModuleClockError4": metro1500TDMLocModuleClockError4,
       "metro1500TDMLocalConnector": metro1500TDMLocalConnector,
       "metro1500TDMLocalLaserType": metro1500TDMLocalLaserType,
       "metro1500TDMRemoteConnector": metro1500TDMRemoteConnector,
       "metro1500TDMRemoteLaserType": metro1500TDMRemoteLaserType,
       "metro1500TDMConverterType": metro1500TDMConverterType,
       "metro1500TDMClockRecovery": metro1500TDMClockRecovery,
       "metro1500TDMDataRateRange": metro1500TDMDataRateRange,
       "metro1500TDMClockFreqRange": metro1500TDMClockFreqRange,
       "metro1500TDMChannelNumber": metro1500TDMChannelNumber,
       "metro1500TDMLocModuleInst5": metro1500TDMLocModuleInst5,
       "metro1500TDMLocModuleEnable5": metro1500TDMLocModuleEnable5,
       "metro1500TDMLocModuleRx5": metro1500TDMLocModuleRx5,
       "metro1500TDMLocModuleTx5": metro1500TDMLocModuleTx5,
       "metro1500TDMLocModuleRemoteData5": metro1500TDMLocModuleRemoteData5,
       "metro1500TDMLocModuleClockFrequency5": metro1500TDMLocModuleClockFrequency5,
       "metro1500TDMLocModuleClockError5": metro1500TDMLocModuleClockError5,
       "metro1500TDMLocModuleInst6": metro1500TDMLocModuleInst6,
       "metro1500TDMLocModuleEnable6": metro1500TDMLocModuleEnable6,
       "metro1500TDMLocModuleRx6": metro1500TDMLocModuleRx6,
       "metro1500TDMLocModuleTx6": metro1500TDMLocModuleTx6,
       "metro1500TDMLocModuleRemoteData6": metro1500TDMLocModuleRemoteData6,
       "metro1500TDMLocModuleClockFrequency6": metro1500TDMLocModuleClockFrequency6,
       "metro1500TDMLocModuleClockError6": metro1500TDMLocModuleClockError6,
       "metro1500TDMLocModuleInst7": metro1500TDMLocModuleInst7,
       "metro1500TDMLocModuleEnable7": metro1500TDMLocModuleEnable7,
       "metro1500TDMLocModuleRx7": metro1500TDMLocModuleRx7,
       "metro1500TDMLocModuleTx7": metro1500TDMLocModuleTx7,
       "metro1500TDMLocModuleRemoteData7": metro1500TDMLocModuleRemoteData7,
       "metro1500TDMLocModuleClockFrequency7": metro1500TDMLocModuleClockFrequency7,
       "metro1500TDMLocModuleClockError7": metro1500TDMLocModuleClockError7,
       "metro1500TDMLocModuleInst8": metro1500TDMLocModuleInst8,
       "metro1500TDMLocModuleEnable8": metro1500TDMLocModuleEnable8,
       "metro1500TDMLocModuleRx8": metro1500TDMLocModuleRx8,
       "metro1500TDMLocModuleTx8": metro1500TDMLocModuleTx8,
       "metro1500TDMLocModuleRemoteData8": metro1500TDMLocModuleRemoteData8,
       "metro1500TDMLocModuleClockFrequency8": metro1500TDMLocModuleClockFrequency8,
       "metro1500TDMLocModuleClockError8": metro1500TDMLocModuleClockError8,
       "metro1500MUX_DMX": metro1500MUX_DMX,
       "metro1500MUX_DMX_Table": metro1500MUX_DMX_Table,
       "metro1500MUX_DMX_Entry": metro1500MUX_DMX_Entry,
       "metro1500MUX_DMX_Number": metro1500MUX_DMX_Number,
       "metro1500MUX_DMX_WDMType": metro1500MUX_DMX_WDMType,
       "metro1500MUX_DMX_Scheme": metro1500MUX_DMX_Scheme,
       "metro1500MUX_DMX_ChannelRange": metro1500MUX_DMX_ChannelRange,
       "metro1500MUX_DMX_Connector": metro1500MUX_DMX_Connector,
       "metro1500MUX_DMX_UpgradePort": metro1500MUX_DMX_UpgradePort,
       "metro1500BSM": metro1500BSM,
       "metro1500BSM_Table": metro1500BSM_Table,
       "metro1500BSM_Entry": metro1500BSM_Entry,
       "metro1500BSM_Number": metro1500BSM_Number,
       "metro1500BSM_Scheme": metro1500BSM_Scheme,
       "metro1500BSM_BandRange": metro1500BSM_BandRange,
       "metro1500BSM_ConnectorType": metro1500BSM_ConnectorType,
       "metro1500Trap": metro1500Trap,
       "metro1500HardwareAdded": metro1500HardwareAdded,
       "metro1500HardwareDeleted": metro1500HardwareDeleted,
       "metro1500PSNotFail": metro1500PSNotFail,
       "metro1500PSFail": metro1500PSFail,
       "metro1500FanNotFail": metro1500FanNotFail,
       "metro1500FanFail": metro1500FanFail,
       "metro1500BusNotFail": metro1500BusNotFail,
       "metro1500BusFail": metro1500BusFail,
       "metro1500ConfigMismatch": metro1500ConfigMismatch,
       "metro1500RxLocOn": metro1500RxLocOn,
       "metro1500RxLocOff": metro1500RxLocOff,
       "metro1500TxLocOn": metro1500TxLocOn,
       "metro1500TxLocOff": metro1500TxLocOff,
       "metro1500RxRemOn": metro1500RxRemOn,
       "metro1500RxRemOff": metro1500RxRemOff,
       "metro1500TxRemOn": metro1500TxRemOn,
       "metro1500TxRemOff": metro1500TxRemOff,
       "metro1500RxRem2On": metro1500RxRem2On,
       "metro1500RxRem2Off": metro1500RxRem2Off,
       "metro1500TxRem2On": metro1500TxRem2On,
       "metro1500TxRem2Off": metro1500TxRem2Off,
       "metro1500ClockNoFail": metro1500ClockNoFail,
       "metro1500ClockFail": metro1500ClockFail,
       "metro1500ClockChangeFrequency": metro1500ClockChangeFrequency,
       "metro1500LocLoopOn": metro1500LocLoopOn,
       "metro1500LocLoopOff": metro1500LocLoopOff,
       "metro1500RemLoopOn": metro1500RemLoopOn,
       "metro1500RemLoopOff": metro1500RemLoopOff,
       "metro1500switchReferenceLaserOn": metro1500switchReferenceLaserOn,
       "metro1500switchReferenceLaserOff": metro1500switchReferenceLaserOff,
       "metro1500switchToA": metro1500switchToA,
       "metro1500switchToB": metro1500switchToB,
       "metro1500switchAutomatic": metro1500switchAutomatic,
       "metro1500switchLocked": metro1500switchLocked,
       "metro1500switchLineAavail": metro1500switchLineAavail,
       "metro1500switchLineANotAvail": metro1500switchLineANotAvail,
       "metro1500switchLineBavail": metro1500switchLineBavail,
       "metro1500switchLineBNotAvail": metro1500switchLineBNotAvail,
       "metro1500repeatedMessage": metro1500repeatedMessage,
       "metro1500INNCDown": metro1500INNCDown,
       "metro1500INNCUp": metro1500INNCUp,
       "metro1500switchAutoLaserShutdownOn": metro1500switchAutoLaserShutdownOn,
       "metro1500switchAutoLaserShutdownOff": metro1500switchAutoLaserShutdownOff,
       "metro1500NEMIAuthFail": metro1500NEMIAuthFail,
       "metro1500EthernetPortEnable": metro1500EthernetPortEnable,
       "metro1500EthernetPortDisable": metro1500EthernetPortDisable,
       "metro1500EthernetPortPartitioned": metro1500EthernetPortPartitioned,
       "metro1500EthernetPortNotPartitioned": metro1500EthernetPortNotPartitioned,
       "metro1500EthernetPortLinkPulses": metro1500EthernetPortLinkPulses,
       "metro1500EthernetPortNoLinkPulses": metro1500EthernetPortNoLinkPulses,
       "metro1500TDMRemoteSyncLoss": metro1500TDMRemoteSyncLoss,
       "metro1500TDMRemoteSync": metro1500TDMRemoteSync,
       "metro1500TDMLocModuleEnabled1": metro1500TDMLocModuleEnabled1,
       "metro1500TDMLocModuleDisable1": metro1500TDMLocModuleDisable1,
       "metro1500TDMLocModuleEnabled2": metro1500TDMLocModuleEnabled2,
       "metro1500TDMLocModuleDisable2": metro1500TDMLocModuleDisable2,
       "metro1500TDMLocModuleEnabled3": metro1500TDMLocModuleEnabled3,
       "metro1500TDMLocModuleDisable3": metro1500TDMLocModuleDisable3,
       "metro1500TDMLocModuleEnabled4": metro1500TDMLocModuleEnabled4,
       "metro1500TDMLocModuleDisable4": metro1500TDMLocModuleDisable4,
       "metro1500TDMLocModuleEnabled5": metro1500TDMLocModuleEnabled5,
       "metro1500TDMLocModuleDisable5": metro1500TDMLocModuleDisable5,
       "metro1500TDMLocModuleEnabled6": metro1500TDMLocModuleEnabled6,
       "metro1500TDMLocModuleDisable6": metro1500TDMLocModuleDisable6,
       "metro1500TDMLocModuleEnabled7": metro1500TDMLocModuleEnabled7,
       "metro1500TDMLocModuleDisable7": metro1500TDMLocModuleDisable7,
       "metro1500TDMLocModuleEnabled8": metro1500TDMLocModuleEnabled8,
       "metro1500TDMLocModuleDisable8": metro1500TDMLocModuleDisable8,
       "metro1500TDMLocModuleRxOn1": metro1500TDMLocModuleRxOn1,
       "metro1500TDMLocModuleRxOff1": metro1500TDMLocModuleRxOff1,
       "metro1500TDMLocModuleRxOn2": metro1500TDMLocModuleRxOn2,
       "metro1500TDMLocModuleRxOff2": metro1500TDMLocModuleRxOff2,
       "metro1500TDMLocModuleRxOn3": metro1500TDMLocModuleRxOn3,
       "metro1500TDMLocModuleRxOff3": metro1500TDMLocModuleRxOff3,
       "metro1500TDMLocModuleRxOn4": metro1500TDMLocModuleRxOn4,
       "metro1500TDMLocModuleRxOff4": metro1500TDMLocModuleRxOff4,
       "metro1500TDMLocModuleRxOn5": metro1500TDMLocModuleRxOn5,
       "metro1500TDMLocModuleRxOff5": metro1500TDMLocModuleRxOff5,
       "metro1500TDMLocModuleRxOn6": metro1500TDMLocModuleRxOn6,
       "metro1500TDMLocModuleRxOff6": metro1500TDMLocModuleRxOff6,
       "metro1500TDMLocModuleRxOn7": metro1500TDMLocModuleRxOn7,
       "metro1500TDMLocModuleRxOff7": metro1500TDMLocModuleRxOff7,
       "metro1500TDMLocModuleRxOn8": metro1500TDMLocModuleRxOn8,
       "metro1500TDMLocModuleRxOff8": metro1500TDMLocModuleRxOff8,
       "metro1500TDMLocModuleData1": metro1500TDMLocModuleData1,
       "metro1500TDMLocModuleNoData1": metro1500TDMLocModuleNoData1,
       "metro1500TDMLocModuleData2": metro1500TDMLocModuleData2,
       "metro1500TDMLocModuleNoData2": metro1500TDMLocModuleNoData2,
       "metro1500TDMLocModuleData3": metro1500TDMLocModuleData3,
       "metro1500TDMLocModuleNoData3": metro1500TDMLocModuleNoData3,
       "metro1500TDMLocModuleData4": metro1500TDMLocModuleData4,
       "metro1500TDMLocModuleNoData4": metro1500TDMLocModuleNoData4,
       "metro1500TDMLocModuleData5": metro1500TDMLocModuleData5,
       "metro1500TDMLocModuleNoData5": metro1500TDMLocModuleNoData5,
       "metro1500TDMLocModuleData6": metro1500TDMLocModuleData6,
       "metro1500TDMLocModuleNoData6": metro1500TDMLocModuleNoData6,
       "metro1500TDMLocModuleData7": metro1500TDMLocModuleData7,
       "metro1500TDMLocModuleNoData7": metro1500TDMLocModuleNoData7,
       "metro1500TDMLocModuleData8": metro1500TDMLocModuleData8,
       "metro1500TDMLocModuleNoData8": metro1500TDMLocModuleNoData8,
       "metro1500TDMLocModuleClockFail1": metro1500TDMLocModuleClockFail1,
       "metro1500TDMLocModuleClockNoFail1": metro1500TDMLocModuleClockNoFail1,
       "metro1500TDMLocModuleClockFail2": metro1500TDMLocModuleClockFail2,
       "metro1500TDMLocModuleClockNoFail2": metro1500TDMLocModuleClockNoFail2,
       "metro1500TDMLocModuleClockFail3": metro1500TDMLocModuleClockFail3,
       "metro1500TDMLocModuleClockNoFail3": metro1500TDMLocModuleClockNoFail3,
       "metro1500TDMLocModuleClockFail4": metro1500TDMLocModuleClockFail4,
       "metro1500TDMLocModuleClockNoFail4": metro1500TDMLocModuleClockNoFail4,
       "metro1500TDMLocModuleClockFail5": metro1500TDMLocModuleClockFail5,
       "metro1500TDMLocModuleClockNoFail5": metro1500TDMLocModuleClockNoFail5,
       "metro1500TDMLocModuleClockFail6": metro1500TDMLocModuleClockFail6,
       "metro1500TDMLocModuleClockNoFail6": metro1500TDMLocModuleClockNoFail6,
       "metro1500TDMLocModuleClockFail7": metro1500TDMLocModuleClockFail7,
       "metro1500TDMLocModuleClockNoFail7": metro1500TDMLocModuleClockNoFail7,
       "metro1500TDMLocModuleClockFail8": metro1500TDMLocModuleClockFail8,
       "metro1500TDMLocModuleClockNoFail8": metro1500TDMLocModuleClockNoFail8,
       "metro1500TDMLocModuleClockChange1": metro1500TDMLocModuleClockChange1,
       "metro1500TDMLocModuleClockChange2": metro1500TDMLocModuleClockChange2,
       "metro1500TDMLocModuleClockChange3": metro1500TDMLocModuleClockChange3,
       "metro1500TDMLocModuleClockChange4": metro1500TDMLocModuleClockChange4,
       "metro1500TDMLocModuleClockChange5": metro1500TDMLocModuleClockChange5,
       "metro1500TDMLocModuleClockChange6": metro1500TDMLocModuleClockChange6,
       "metro1500TDMLocModuleClockChange7": metro1500TDMLocModuleClockChange7,
       "metro1500TDMLocModuleClockChange8": metro1500TDMLocModuleClockChange8,
       "metro1500RemoteClockNoSync": metro1500RemoteClockNoSync,
       "metro1500RemoteClockSync": metro1500RemoteClockSync,
       "metro1500RemoteClock2NoSync": metro1500RemoteClock2NoSync,
       "metro1500RemoteClock2Sync": metro1500RemoteClock2Sync,
       "metro1500RegeneratorModeOn": metro1500RegeneratorModeOn,
       "metro1500RegeneratorModeOff": metro1500RegeneratorModeOff,
       "metro1500RSM_OSC_OSCOn": metro1500RSM_OSC_OSCOn,
       "metro1500RSM_OSC_OSCOff": metro1500RSM_OSC_OSCOff,
       "metro1500EthernetPortSpeed10": metro1500EthernetPortSpeed10,
       "metro1500EthernetPortSpeed100": metro1500EthernetPortSpeed100,
       "metro1500EthernetPortDuplexHalf": metro1500EthernetPortDuplexHalf,
       "metro1500EthernetPortDuplexFull": metro1500EthernetPortDuplexFull,
       "metro1500EthernetPortAutonegotiationOn": metro1500EthernetPortAutonegotiationOn,
       "metro1500EthernetPortAutonegotiationOff": metro1500EthernetPortAutonegotiationOff,
       "metro1500EthernetPortPolarityPositive": metro1500EthernetPortPolarityPositive,
       "metro1500EthernetPortPolarityNegative": metro1500EthernetPortPolarityNegative,
       "metro1500HotStandby_Change2LineA": metro1500HotStandby_Change2LineA,
       "metro1500HotStandby_Change2LineB": metro1500HotStandby_Change2LineB,
       "metro1500HotStandby_Locked": metro1500HotStandby_Locked,
       "metro1500HotStandby_Automatic": metro1500HotStandby_Automatic}
)
