# SNMP MIB module (Fsp_II-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/Fsp_II-MIB.mib
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
_Fsp_II_ObjectIdentity = ObjectIdentity
fsp_II = _Fsp_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3)
)
_Fsp_II_Main_ObjectIdentity = ObjectIdentity
fsp_II_Main = _Fsp_II_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1)
)
_Fsp_II_Housing_ObjectIdentity = ObjectIdentity
fsp_II_Housing = _Fsp_II_Housing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1)
)
_Fsp_II_Manufacturer_Type = DisplayString
_Fsp_II_Manufacturer_Object = MibScalar
fsp_II_Manufacturer = _Fsp_II_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 1),
    _Fsp_II_Manufacturer_Type()
)
fsp_II_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_Manufacturer.setStatus("mandatory")
_Fsp_II_MainType_Type = DisplayString
_Fsp_II_MainType_Object = MibScalar
fsp_II_MainType = _Fsp_II_MainType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 2),
    _Fsp_II_MainType_Type()
)
fsp_II_MainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainType.setStatus("mandatory")
_Fsp_II_MainSerialNumber_Type = DisplayString
_Fsp_II_MainSerialNumber_Object = MibScalar
fsp_II_MainSerialNumber = _Fsp_II_MainSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 3),
    _Fsp_II_MainSerialNumber_Type()
)
fsp_II_MainSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainSerialNumber.setStatus("mandatory")
_Fsp_II_MainHardwareVersion_Type = DisplayString
_Fsp_II_MainHardwareVersion_Object = MibScalar
fsp_II_MainHardwareVersion = _Fsp_II_MainHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 4),
    _Fsp_II_MainHardwareVersion_Type()
)
fsp_II_MainHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainHardwareVersion.setStatus("mandatory")
_Fsp_II_MainSoftwareVersion_Type = DisplayString
_Fsp_II_MainSoftwareVersion_Object = MibScalar
fsp_II_MainSoftwareVersion = _Fsp_II_MainSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 5),
    _Fsp_II_MainSoftwareVersion_Type()
)
fsp_II_MainSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainSoftwareVersion.setStatus("mandatory")
_Fsp_II_MainBusMessages_Type = Integer32
_Fsp_II_MainBusMessages_Object = MibScalar
fsp_II_MainBusMessages = _Fsp_II_MainBusMessages_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 6),
    _Fsp_II_MainBusMessages_Type()
)
fsp_II_MainBusMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainBusMessages.setStatus("mandatory")
_Fsp_II_MainBusErrors_Type = Integer32
_Fsp_II_MainBusErrors_Object = MibScalar
fsp_II_MainBusErrors = _Fsp_II_MainBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 7),
    _Fsp_II_MainBusErrors_Type()
)
fsp_II_MainBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainBusErrors.setStatus("mandatory")


class _Fsp_II_MainLastEvent_Type(Integer32):
    """Custom type fsp_II_MainLastEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp_II_MainLastEvent_Type.__name__ = "Integer32"
_Fsp_II_MainLastEvent_Object = MibScalar
fsp_II_MainLastEvent = _Fsp_II_MainLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 8),
    _Fsp_II_MainLastEvent_Type()
)
fsp_II_MainLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainLastEvent.setStatus("mandatory")
_Fsp_II_MainMotd_Type = DisplayString
_Fsp_II_MainMotd_Object = MibScalar
fsp_II_MainMotd = _Fsp_II_MainMotd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 9),
    _Fsp_II_MainMotd_Type()
)
fsp_II_MainMotd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainMotd.setStatus("mandatory")
_Fsp_II_MainTrapsinkTable_Object = MibTable
fsp_II_MainTrapsinkTable = _Fsp_II_MainTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fsp_II_MainTrapsinkTable.setStatus("mandatory")
_Fsp_II_MainTrapsinkEntry_Object = MibTableRow
fsp_II_MainTrapsinkEntry = _Fsp_II_MainTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1)
)
fsp_II_MainTrapsinkEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_MainTrapsinkNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_MainTrapsinkEntry.setStatus("mandatory")


class _Fsp_II_MainTrapsinkNumber_Type(Integer32):
    """Custom type fsp_II_MainTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsp_II_MainTrapsinkNumber_Type.__name__ = "Integer32"
_Fsp_II_MainTrapsinkNumber_Object = MibTableColumn
fsp_II_MainTrapsinkNumber = _Fsp_II_MainTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 1),
    _Fsp_II_MainTrapsinkNumber_Type()
)
fsp_II_MainTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainTrapsinkNumber.setStatus("mandatory")
_Fsp_II_MainTrapsinkAddress_Type = DisplayString
_Fsp_II_MainTrapsinkAddress_Object = MibTableColumn
fsp_II_MainTrapsinkAddress = _Fsp_II_MainTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 2),
    _Fsp_II_MainTrapsinkAddress_Type()
)
fsp_II_MainTrapsinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainTrapsinkAddress.setStatus("mandatory")
_Fsp_II_MainTrapsinkCommunity_Type = DisplayString
_Fsp_II_MainTrapsinkCommunity_Object = MibTableColumn
fsp_II_MainTrapsinkCommunity = _Fsp_II_MainTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 3),
    _Fsp_II_MainTrapsinkCommunity_Type()
)
fsp_II_MainTrapsinkCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainTrapsinkCommunity.setStatus("mandatory")


class _Fsp_II_MainTrapsinkPriority_Type(Integer32):
    """Custom type fsp_II_MainTrapsinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Fsp_II_MainTrapsinkPriority_Type.__name__ = "Integer32"
_Fsp_II_MainTrapsinkPriority_Object = MibTableColumn
fsp_II_MainTrapsinkPriority = _Fsp_II_MainTrapsinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 4),
    _Fsp_II_MainTrapsinkPriority_Type()
)
fsp_II_MainTrapsinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainTrapsinkPriority.setStatus("mandatory")
_Fsp_II_MainLogfileTable_Object = MibTable
fsp_II_MainLogfileTable = _Fsp_II_MainLogfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    fsp_II_MainLogfileTable.setStatus("mandatory")
_Fsp_II_MainLogfileEntry_Object = MibTableRow
fsp_II_MainLogfileEntry = _Fsp_II_MainLogfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1)
)
fsp_II_MainLogfileEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_MainLogfileNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_MainLogfileEntry.setStatus("mandatory")


class _Fsp_II_MainLogfileNumber_Type(Integer32):
    """Custom type fsp_II_MainLogfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Fsp_II_MainLogfileNumber_Type.__name__ = "Integer32"
_Fsp_II_MainLogfileNumber_Object = MibTableColumn
fsp_II_MainLogfileNumber = _Fsp_II_MainLogfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 1),
    _Fsp_II_MainLogfileNumber_Type()
)
fsp_II_MainLogfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainLogfileNumber.setStatus("mandatory")
_Fsp_II_MainLogfileName_Type = DisplayString
_Fsp_II_MainLogfileName_Object = MibTableColumn
fsp_II_MainLogfileName = _Fsp_II_MainLogfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 2),
    _Fsp_II_MainLogfileName_Type()
)
fsp_II_MainLogfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainLogfileName.setStatus("mandatory")
_Fsp_II_MainLogfileSize_Type = Integer32
_Fsp_II_MainLogfileSize_Object = MibTableColumn
fsp_II_MainLogfileSize = _Fsp_II_MainLogfileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 3),
    _Fsp_II_MainLogfileSize_Type()
)
fsp_II_MainLogfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainLogfileSize.setStatus("mandatory")


class _Fsp_II_MainLogfilePriority_Type(Integer32):
    """Custom type fsp_II_MainLogfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Fsp_II_MainLogfilePriority_Type.__name__ = "Integer32"
_Fsp_II_MainLogfilePriority_Object = MibTableColumn
fsp_II_MainLogfilePriority = _Fsp_II_MainLogfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 4),
    _Fsp_II_MainLogfilePriority_Type()
)
fsp_II_MainLogfilePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_MainLogfilePriority.setStatus("mandatory")
_Fsp_II_SlotTable_Object = MibTable
fsp_II_SlotTable = _Fsp_II_SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fsp_II_SlotTable.setStatus("mandatory")
_Fsp_II_SlotEntry_Object = MibTableRow
fsp_II_SlotEntry = _Fsp_II_SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1)
)
fsp_II_SlotEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_SlotNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_SlotEntry.setStatus("mandatory")


class _Fsp_II_SlotNumber_Type(Integer32):
    """Custom type fsp_II_SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Fsp_II_SlotNumber_Type.__name__ = "Integer32"
_Fsp_II_SlotNumber_Object = MibTableColumn
fsp_II_SlotNumber = _Fsp_II_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 1),
    _Fsp_II_SlotNumber_Type()
)
fsp_II_SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SlotNumber.setStatus("mandatory")
_Fsp_II_Type_Type = DisplayString
_Fsp_II_Type_Object = MibTableColumn
fsp_II_Type = _Fsp_II_Type_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 2),
    _Fsp_II_Type_Type()
)
fsp_II_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_Type.setStatus("mandatory")


class _Fsp_II_SlotTypeNumber_Type(Integer32):
    """Custom type fsp_II_SlotTypeNumber based on Integer32"""
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
              32,
              33,
              39,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hotStandbyConverter", 0),
          ("fsp_II_Converter", 1),
          ("fsp_I_Converter", 2),
          ("fsp_I_EthernetConverter", 3),
          ("fsp_II_2_5GBitConverter", 5),
          ("fsp_II_TRL_Converter", 7),
          ("fsp_II_4PortTDMCard", 10),
          ("nemi", 32),
          ("demi", 33),
          ("fsp_II_EthernetHubCard", 39),
          ("switch", 64),
          ("other", 255))
    )


_Fsp_II_SlotTypeNumber_Type.__name__ = "Integer32"
_Fsp_II_SlotTypeNumber_Object = MibTableColumn
fsp_II_SlotTypeNumber = _Fsp_II_SlotTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 3),
    _Fsp_II_SlotTypeNumber_Type()
)
fsp_II_SlotTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SlotTypeNumber.setStatus("mandatory")
_Fsp_II_SerialNumber_Type = DisplayString
_Fsp_II_SerialNumber_Object = MibTableColumn
fsp_II_SerialNumber = _Fsp_II_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 4),
    _Fsp_II_SerialNumber_Type()
)
fsp_II_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SerialNumber.setStatus("mandatory")
_Fsp_II_HardwareVersion_Type = DisplayString
_Fsp_II_HardwareVersion_Object = MibTableColumn
fsp_II_HardwareVersion = _Fsp_II_HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 5),
    _Fsp_II_HardwareVersion_Type()
)
fsp_II_HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_HardwareVersion.setStatus("mandatory")
_Fsp_II_SoftwareVersion_Type = DisplayString
_Fsp_II_SoftwareVersion_Object = MibTableColumn
fsp_II_SoftwareVersion = _Fsp_II_SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 6),
    _Fsp_II_SoftwareVersion_Type()
)
fsp_II_SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SoftwareVersion.setStatus("mandatory")
_Fsp_II_Temperature_Type = Integer32
_Fsp_II_Temperature_Object = MibTableColumn
fsp_II_Temperature = _Fsp_II_Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 7),
    _Fsp_II_Temperature_Type()
)
fsp_II_Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_Temperature.setStatus("mandatory")
_Fsp_II_BoardVoltage_Type = Integer32
_Fsp_II_BoardVoltage_Object = MibTableColumn
fsp_II_BoardVoltage = _Fsp_II_BoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 8),
    _Fsp_II_BoardVoltage_Type()
)
fsp_II_BoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_BoardVoltage.setStatus("mandatory")
_Fsp_II_DetailInfo_Type = ObjectIdentifier
_Fsp_II_DetailInfo_Object = MibTableColumn
fsp_II_DetailInfo = _Fsp_II_DetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 9),
    _Fsp_II_DetailInfo_Type()
)
fsp_II_DetailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_DetailInfo.setStatus("mandatory")


class _Fsp_II_EPLDVersion_Type(Integer32):
    """Custom type fsp_II_EPLDVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsp_II_EPLDVersion_Type.__name__ = "Integer32"
_Fsp_II_EPLDVersion_Object = MibTableColumn
fsp_II_EPLDVersion = _Fsp_II_EPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 10),
    _Fsp_II_EPLDVersion_Type()
)
fsp_II_EPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EPLDVersion.setStatus("mandatory")
_Fsp_II_PSTable_Object = MibTable
fsp_II_PSTable = _Fsp_II_PSTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    fsp_II_PSTable.setStatus("mandatory")
_Fsp_II_PSEntry_Object = MibTableRow
fsp_II_PSEntry = _Fsp_II_PSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1)
)
fsp_II_PSEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_PSNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_PSEntry.setStatus("mandatory")


class _Fsp_II_PSNumber_Type(Integer32):
    """Custom type fsp_II_PSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Fsp_II_PSNumber_Type.__name__ = "Integer32"
_Fsp_II_PSNumber_Object = MibTableColumn
fsp_II_PSNumber = _Fsp_II_PSNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 1),
    _Fsp_II_PSNumber_Type()
)
fsp_II_PSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_PSNumber.setStatus("mandatory")


class _Fsp_II_PSOn_Type(Integer32):
    """Custom type fsp_II_PSOn based on Integer32"""
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


_Fsp_II_PSOn_Type.__name__ = "Integer32"
_Fsp_II_PSOn_Object = MibTableColumn
fsp_II_PSOn = _Fsp_II_PSOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 2),
    _Fsp_II_PSOn_Type()
)
fsp_II_PSOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_PSOn.setStatus("mandatory")
_Fsp_II_FanTable_Object = MibTable
fsp_II_FanTable = _Fsp_II_FanTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    fsp_II_FanTable.setStatus("mandatory")
_Fsp_II_FanEntry_Object = MibTableRow
fsp_II_FanEntry = _Fsp_II_FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1)
)
fsp_II_FanEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_FanNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_FanEntry.setStatus("mandatory")


class _Fsp_II_FanNumber_Type(Integer32):
    """Custom type fsp_II_FanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Fsp_II_FanNumber_Type.__name__ = "Integer32"
_Fsp_II_FanNumber_Object = MibTableColumn
fsp_II_FanNumber = _Fsp_II_FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 1),
    _Fsp_II_FanNumber_Type()
)
fsp_II_FanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_FanNumber.setStatus("mandatory")


class _Fsp_II_FanOn_Type(Integer32):
    """Custom type fsp_II_FanOn based on Integer32"""
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


_Fsp_II_FanOn_Type.__name__ = "Integer32"
_Fsp_II_FanOn_Object = MibTableColumn
fsp_II_FanOn = _Fsp_II_FanOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 2),
    _Fsp_II_FanOn_Type()
)
fsp_II_FanOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_FanOn.setStatus("mandatory")
_Fsp_II_Converter_ObjectIdentity = ObjectIdentity
fsp_II_Converter = _Fsp_II_Converter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5)
)
_Fsp_II_ConverterTable_Object = MibTable
fsp_II_ConverterTable = _Fsp_II_ConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    fsp_II_ConverterTable.setStatus("mandatory")
_Fsp_II_ConverterEntry_Object = MibTableRow
fsp_II_ConverterEntry = _Fsp_II_ConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1)
)
fsp_II_ConverterEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_ConverterNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_ConverterEntry.setStatus("mandatory")
_Fsp_II_ConverterNumber_Type = Integer32
_Fsp_II_ConverterNumber_Object = MibTableColumn
fsp_II_ConverterNumber = _Fsp_II_ConverterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 1),
    _Fsp_II_ConverterNumber_Type()
)
fsp_II_ConverterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_ConverterNumber.setStatus("mandatory")


class _Fsp_II_RxLoc_Type(Integer32):
    """Custom type fsp_II_RxLoc based on Integer32"""
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


_Fsp_II_RxLoc_Type.__name__ = "Integer32"
_Fsp_II_RxLoc_Object = MibTableColumn
fsp_II_RxLoc = _Fsp_II_RxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 2),
    _Fsp_II_RxLoc_Type()
)
fsp_II_RxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_RxLoc.setStatus("mandatory")


class _Fsp_II_TxLoc_Type(Integer32):
    """Custom type fsp_II_TxLoc based on Integer32"""
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


_Fsp_II_TxLoc_Type.__name__ = "Integer32"
_Fsp_II_TxLoc_Object = MibTableColumn
fsp_II_TxLoc = _Fsp_II_TxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 3),
    _Fsp_II_TxLoc_Type()
)
fsp_II_TxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TxLoc.setStatus("mandatory")


class _Fsp_II_TxLocC_Type(Integer32):
    """Custom type fsp_II_TxLocC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fsp_II_TxLocC_Type.__name__ = "Integer32"
_Fsp_II_TxLocC_Object = MibTableColumn
fsp_II_TxLocC = _Fsp_II_TxLocC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 4),
    _Fsp_II_TxLocC_Type()
)
fsp_II_TxLocC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TxLocC.setStatus("mandatory")


class _Fsp_II_TxLocTemp_Type(Integer32):
    """Custom type fsp_II_TxLocTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Fsp_II_TxLocTemp_Type.__name__ = "Integer32"
_Fsp_II_TxLocTemp_Object = MibTableColumn
fsp_II_TxLocTemp = _Fsp_II_TxLocTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 5),
    _Fsp_II_TxLocTemp_Type()
)
fsp_II_TxLocTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TxLocTemp.setStatus("mandatory")


class _Fsp_II_RxRem_Type(Integer32):
    """Custom type fsp_II_RxRem based on Integer32"""
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


_Fsp_II_RxRem_Type.__name__ = "Integer32"
_Fsp_II_RxRem_Object = MibTableColumn
fsp_II_RxRem = _Fsp_II_RxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 6),
    _Fsp_II_RxRem_Type()
)
fsp_II_RxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_RxRem.setStatus("mandatory")


class _Fsp_II_TxRem_Type(Integer32):
    """Custom type fsp_II_TxRem based on Integer32"""
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


_Fsp_II_TxRem_Type.__name__ = "Integer32"
_Fsp_II_TxRem_Object = MibTableColumn
fsp_II_TxRem = _Fsp_II_TxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 7),
    _Fsp_II_TxRem_Type()
)
fsp_II_TxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TxRem.setStatus("mandatory")


class _Fsp_II_TxRemC_Type(Integer32):
    """Custom type fsp_II_TxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fsp_II_TxRemC_Type.__name__ = "Integer32"
_Fsp_II_TxRemC_Object = MibTableColumn
fsp_II_TxRemC = _Fsp_II_TxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 8),
    _Fsp_II_TxRemC_Type()
)
fsp_II_TxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TxRemC.setStatus("mandatory")


class _Fsp_II_TxRemTemp_Type(Integer32):
    """Custom type fsp_II_TxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Fsp_II_TxRemTemp_Type.__name__ = "Integer32"
_Fsp_II_TxRemTemp_Object = MibTableColumn
fsp_II_TxRemTemp = _Fsp_II_TxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 9),
    _Fsp_II_TxRemTemp_Type()
)
fsp_II_TxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TxRemTemp.setStatus("mandatory")


class _Fsp_II_RxRem2_Type(Integer32):
    """Custom type fsp_II_RxRem2 based on Integer32"""
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


_Fsp_II_RxRem2_Type.__name__ = "Integer32"
_Fsp_II_RxRem2_Object = MibTableColumn
fsp_II_RxRem2 = _Fsp_II_RxRem2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 10),
    _Fsp_II_RxRem2_Type()
)
fsp_II_RxRem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_RxRem2.setStatus("mandatory")


class _Fsp_II_ClockState_Type(Integer32):
    """Custom type fsp_II_ClockState based on Integer32"""
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


_Fsp_II_ClockState_Type.__name__ = "Integer32"
_Fsp_II_ClockState_Object = MibTableColumn
fsp_II_ClockState = _Fsp_II_ClockState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 11),
    _Fsp_II_ClockState_Type()
)
fsp_II_ClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_ClockState.setStatus("mandatory")
_Fsp_II_ClockFreq_Type = Integer32
_Fsp_II_ClockFreq_Object = MibTableColumn
fsp_II_ClockFreq = _Fsp_II_ClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 12),
    _Fsp_II_ClockFreq_Type()
)
fsp_II_ClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_ClockFreq.setStatus("mandatory")


class _Fsp_II_LocLoop_Type(Integer32):
    """Custom type fsp_II_LocLoop based on Integer32"""
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


_Fsp_II_LocLoop_Type.__name__ = "Integer32"
_Fsp_II_LocLoop_Object = MibTableColumn
fsp_II_LocLoop = _Fsp_II_LocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 13),
    _Fsp_II_LocLoop_Type()
)
fsp_II_LocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_LocLoop.setStatus("mandatory")


class _Fsp_II_RemLoop_Type(Integer32):
    """Custom type fsp_II_RemLoop based on Integer32"""
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


_Fsp_II_RemLoop_Type.__name__ = "Integer32"
_Fsp_II_RemLoop_Object = MibTableColumn
fsp_II_RemLoop = _Fsp_II_RemLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 14),
    _Fsp_II_RemLoop_Type()
)
fsp_II_RemLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_RemLoop.setStatus("mandatory")


class _Fsp_II_ClockType_Type(Integer32):
    """Custom type fsp_II_ClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              9,
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


_Fsp_II_ClockType_Type.__name__ = "Integer32"
_Fsp_II_ClockType_Object = MibTableColumn
fsp_II_ClockType = _Fsp_II_ClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 15),
    _Fsp_II_ClockType_Type()
)
fsp_II_ClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_ClockType.setStatus("mandatory")
_Fsp_II_Switch_ObjectIdentity = ObjectIdentity
fsp_II_Switch = _Fsp_II_Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10)
)
_Fsp_II_SwitchTable_Object = MibTable
fsp_II_SwitchTable = _Fsp_II_SwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    fsp_II_SwitchTable.setStatus("mandatory")
_Fsp_II_SwitchEntry_Object = MibTableRow
fsp_II_SwitchEntry = _Fsp_II_SwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1)
)
fsp_II_SwitchEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_SwitchNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_SwitchEntry.setStatus("mandatory")
_Fsp_II_SwitchNumber_Type = Integer32
_Fsp_II_SwitchNumber_Object = MibTableColumn
fsp_II_SwitchNumber = _Fsp_II_SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 1),
    _Fsp_II_SwitchNumber_Type()
)
fsp_II_SwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SwitchNumber.setStatus("mandatory")


class _Fsp_II_SwitchLine_Type(Integer32):
    """Custom type fsp_II_SwitchLine based on Integer32"""
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


_Fsp_II_SwitchLine_Type.__name__ = "Integer32"
_Fsp_II_SwitchLine_Object = MibTableColumn
fsp_II_SwitchLine = _Fsp_II_SwitchLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 2),
    _Fsp_II_SwitchLine_Type()
)
fsp_II_SwitchLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SwitchLine.setStatus("mandatory")


class _Fsp_II_SwitchMode_Type(Integer32):
    """Custom type fsp_II_SwitchMode based on Integer32"""
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


_Fsp_II_SwitchMode_Type.__name__ = "Integer32"
_Fsp_II_SwitchMode_Object = MibTableColumn
fsp_II_SwitchMode = _Fsp_II_SwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 3),
    _Fsp_II_SwitchMode_Type()
)
fsp_II_SwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SwitchMode.setStatus("mandatory")


class _Fsp_II_SwitchLaserOn_Type(Integer32):
    """Custom type fsp_II_SwitchLaserOn based on Integer32"""
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


_Fsp_II_SwitchLaserOn_Type.__name__ = "Integer32"
_Fsp_II_SwitchLaserOn_Object = MibTableColumn
fsp_II_SwitchLaserOn = _Fsp_II_SwitchLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 4),
    _Fsp_II_SwitchLaserOn_Type()
)
fsp_II_SwitchLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SwitchLaserOn.setStatus("mandatory")


class _Fsp_II_SwitchLineAavail_Type(Integer32):
    """Custom type fsp_II_SwitchLineAavail based on Integer32"""
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


_Fsp_II_SwitchLineAavail_Type.__name__ = "Integer32"
_Fsp_II_SwitchLineAavail_Object = MibTableColumn
fsp_II_SwitchLineAavail = _Fsp_II_SwitchLineAavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 5),
    _Fsp_II_SwitchLineAavail_Type()
)
fsp_II_SwitchLineAavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SwitchLineAavail.setStatus("mandatory")


class _Fsp_II_SwitchLineBavail_Type(Integer32):
    """Custom type fsp_II_SwitchLineBavail based on Integer32"""
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


_Fsp_II_SwitchLineBavail_Type.__name__ = "Integer32"
_Fsp_II_SwitchLineBavail_Object = MibTableColumn
fsp_II_SwitchLineBavail = _Fsp_II_SwitchLineBavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 6),
    _Fsp_II_SwitchLineBavail_Type()
)
fsp_II_SwitchLineBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_SwitchLineBavail.setStatus("mandatory")
_Fsp_II_EthernetHub_ObjectIdentity = ObjectIdentity
fsp_II_EthernetHub = _Fsp_II_EthernetHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14)
)
_Fsp_II_EthernetHubTable_Object = MibTable
fsp_II_EthernetHubTable = _Fsp_II_EthernetHubTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1)
)
if mibBuilder.loadTexts:
    fsp_II_EthernetHubTable.setStatus("mandatory")
_Fsp_II_EthernetHubEntry_Object = MibTableRow
fsp_II_EthernetHubEntry = _Fsp_II_EthernetHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1)
)
fsp_II_EthernetHubEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_EthernetHubNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_EthernetHubEntry.setStatus("mandatory")
_Fsp_II_EthernetHubNumber_Type = Integer32
_Fsp_II_EthernetHubNumber_Object = MibTableColumn
fsp_II_EthernetHubNumber = _Fsp_II_EthernetHubNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 1),
    _Fsp_II_EthernetHubNumber_Type()
)
fsp_II_EthernetHubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubNumber.setStatus("mandatory")


class _Fsp_II_EthernetHubPortEnable1_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortEnable1 based on Integer32"""
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


_Fsp_II_EthernetHubPortEnable1_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortEnable1_Object = MibTableColumn
fsp_II_EthernetHubPortEnable1 = _Fsp_II_EthernetHubPortEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 10),
    _Fsp_II_EthernetHubPortEnable1_Type()
)
fsp_II_EthernetHubPortEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortEnable1.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPartitionStatus1_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPartitionStatus1 based on Integer32"""
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


_Fsp_II_EthernetHubPortPartitionStatus1_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPartitionStatus1_Object = MibTableColumn
fsp_II_EthernetHubPortPartitionStatus1 = _Fsp_II_EthernetHubPortPartitionStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 11),
    _Fsp_II_EthernetHubPortPartitionStatus1_Type()
)
fsp_II_EthernetHubPortPartitionStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPartitionStatus1.setStatus("mandatory")


class _Fsp_II_EthernetHubPortLinkStatus1_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortLinkStatus1 based on Integer32"""
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


_Fsp_II_EthernetHubPortLinkStatus1_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortLinkStatus1_Object = MibTableColumn
fsp_II_EthernetHubPortLinkStatus1 = _Fsp_II_EthernetHubPortLinkStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 12),
    _Fsp_II_EthernetHubPortLinkStatus1_Type()
)
fsp_II_EthernetHubPortLinkStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortLinkStatus1.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPolarity1_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPolarity1 based on Integer32"""
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


_Fsp_II_EthernetHubPortPolarity1_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPolarity1_Object = MibTableColumn
fsp_II_EthernetHubPortPolarity1 = _Fsp_II_EthernetHubPortPolarity1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 13),
    _Fsp_II_EthernetHubPortPolarity1_Type()
)
fsp_II_EthernetHubPortPolarity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPolarity1.setStatus("mandatory")


class _Fsp_II_EthernetHubPortEnable2_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortEnable2 based on Integer32"""
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


_Fsp_II_EthernetHubPortEnable2_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortEnable2_Object = MibTableColumn
fsp_II_EthernetHubPortEnable2 = _Fsp_II_EthernetHubPortEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 20),
    _Fsp_II_EthernetHubPortEnable2_Type()
)
fsp_II_EthernetHubPortEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortEnable2.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPartitionStatus2_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPartitionStatus2 based on Integer32"""
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


_Fsp_II_EthernetHubPortPartitionStatus2_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPartitionStatus2_Object = MibTableColumn
fsp_II_EthernetHubPortPartitionStatus2 = _Fsp_II_EthernetHubPortPartitionStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 21),
    _Fsp_II_EthernetHubPortPartitionStatus2_Type()
)
fsp_II_EthernetHubPortPartitionStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPartitionStatus2.setStatus("mandatory")


class _Fsp_II_EthernetHubPortLinkStatus2_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortLinkStatus2 based on Integer32"""
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


_Fsp_II_EthernetHubPortLinkStatus2_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortLinkStatus2_Object = MibTableColumn
fsp_II_EthernetHubPortLinkStatus2 = _Fsp_II_EthernetHubPortLinkStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 22),
    _Fsp_II_EthernetHubPortLinkStatus2_Type()
)
fsp_II_EthernetHubPortLinkStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortLinkStatus2.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPolarity2_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPolarity2 based on Integer32"""
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


_Fsp_II_EthernetHubPortPolarity2_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPolarity2_Object = MibTableColumn
fsp_II_EthernetHubPortPolarity2 = _Fsp_II_EthernetHubPortPolarity2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 23),
    _Fsp_II_EthernetHubPortPolarity2_Type()
)
fsp_II_EthernetHubPortPolarity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPolarity2.setStatus("mandatory")


class _Fsp_II_EthernetHubPortEnable3_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortEnable3 based on Integer32"""
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


_Fsp_II_EthernetHubPortEnable3_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortEnable3_Object = MibTableColumn
fsp_II_EthernetHubPortEnable3 = _Fsp_II_EthernetHubPortEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 30),
    _Fsp_II_EthernetHubPortEnable3_Type()
)
fsp_II_EthernetHubPortEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortEnable3.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPartitionStatus3_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPartitionStatus3 based on Integer32"""
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


_Fsp_II_EthernetHubPortPartitionStatus3_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPartitionStatus3_Object = MibTableColumn
fsp_II_EthernetHubPortPartitionStatus3 = _Fsp_II_EthernetHubPortPartitionStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 31),
    _Fsp_II_EthernetHubPortPartitionStatus3_Type()
)
fsp_II_EthernetHubPortPartitionStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPartitionStatus3.setStatus("mandatory")


class _Fsp_II_EthernetHubPortLinkStatus3_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortLinkStatus3 based on Integer32"""
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


_Fsp_II_EthernetHubPortLinkStatus3_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortLinkStatus3_Object = MibTableColumn
fsp_II_EthernetHubPortLinkStatus3 = _Fsp_II_EthernetHubPortLinkStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 32),
    _Fsp_II_EthernetHubPortLinkStatus3_Type()
)
fsp_II_EthernetHubPortLinkStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortLinkStatus3.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPolarity3_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPolarity3 based on Integer32"""
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


_Fsp_II_EthernetHubPortPolarity3_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPolarity3_Object = MibTableColumn
fsp_II_EthernetHubPortPolarity3 = _Fsp_II_EthernetHubPortPolarity3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 33),
    _Fsp_II_EthernetHubPortPolarity3_Type()
)
fsp_II_EthernetHubPortPolarity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPolarity3.setStatus("mandatory")


class _Fsp_II_EthernetHubPortEnable4_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortEnable4 based on Integer32"""
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


_Fsp_II_EthernetHubPortEnable4_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortEnable4_Object = MibTableColumn
fsp_II_EthernetHubPortEnable4 = _Fsp_II_EthernetHubPortEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 40),
    _Fsp_II_EthernetHubPortEnable4_Type()
)
fsp_II_EthernetHubPortEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortEnable4.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPartitionStatus4_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPartitionStatus4 based on Integer32"""
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


_Fsp_II_EthernetHubPortPartitionStatus4_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPartitionStatus4_Object = MibTableColumn
fsp_II_EthernetHubPortPartitionStatus4 = _Fsp_II_EthernetHubPortPartitionStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 41),
    _Fsp_II_EthernetHubPortPartitionStatus4_Type()
)
fsp_II_EthernetHubPortPartitionStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPartitionStatus4.setStatus("mandatory")


class _Fsp_II_EthernetHubPortLinkStatus4_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortLinkStatus4 based on Integer32"""
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


_Fsp_II_EthernetHubPortLinkStatus4_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortLinkStatus4_Object = MibTableColumn
fsp_II_EthernetHubPortLinkStatus4 = _Fsp_II_EthernetHubPortLinkStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 42),
    _Fsp_II_EthernetHubPortLinkStatus4_Type()
)
fsp_II_EthernetHubPortLinkStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortLinkStatus4.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPolarity4_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPolarity4 based on Integer32"""
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


_Fsp_II_EthernetHubPortPolarity4_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPolarity4_Object = MibTableColumn
fsp_II_EthernetHubPortPolarity4 = _Fsp_II_EthernetHubPortPolarity4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 43),
    _Fsp_II_EthernetHubPortPolarity4_Type()
)
fsp_II_EthernetHubPortPolarity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPolarity4.setStatus("mandatory")


class _Fsp_II_EthernetHubPortEnable5_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortEnable5 based on Integer32"""
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


_Fsp_II_EthernetHubPortEnable5_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortEnable5_Object = MibTableColumn
fsp_II_EthernetHubPortEnable5 = _Fsp_II_EthernetHubPortEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 50),
    _Fsp_II_EthernetHubPortEnable5_Type()
)
fsp_II_EthernetHubPortEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortEnable5.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPartitionStatus5_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPartitionStatus5 based on Integer32"""
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


_Fsp_II_EthernetHubPortPartitionStatus5_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPartitionStatus5_Object = MibTableColumn
fsp_II_EthernetHubPortPartitionStatus5 = _Fsp_II_EthernetHubPortPartitionStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 51),
    _Fsp_II_EthernetHubPortPartitionStatus5_Type()
)
fsp_II_EthernetHubPortPartitionStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPartitionStatus5.setStatus("mandatory")


class _Fsp_II_EthernetHubPortLinkStatus5_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortLinkStatus5 based on Integer32"""
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


_Fsp_II_EthernetHubPortLinkStatus5_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortLinkStatus5_Object = MibTableColumn
fsp_II_EthernetHubPortLinkStatus5 = _Fsp_II_EthernetHubPortLinkStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 52),
    _Fsp_II_EthernetHubPortLinkStatus5_Type()
)
fsp_II_EthernetHubPortLinkStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortLinkStatus5.setStatus("mandatory")


class _Fsp_II_EthernetHubPortPolarity5_Type(Integer32):
    """Custom type fsp_II_EthernetHubPortPolarity5 based on Integer32"""
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


_Fsp_II_EthernetHubPortPolarity5_Type.__name__ = "Integer32"
_Fsp_II_EthernetHubPortPolarity5_Object = MibTableColumn
fsp_II_EthernetHubPortPolarity5 = _Fsp_II_EthernetHubPortPolarity5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 53),
    _Fsp_II_EthernetHubPortPolarity5_Type()
)
fsp_II_EthernetHubPortPolarity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_EthernetHubPortPolarity5.setStatus("mandatory")
_Fsp_II_TDM_ObjectIdentity = ObjectIdentity
fsp_II_TDM = _Fsp_II_TDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15)
)
_Fsp_II_TDMTable_Object = MibTable
fsp_II_TDMTable = _Fsp_II_TDMTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1)
)
if mibBuilder.loadTexts:
    fsp_II_TDMTable.setStatus("mandatory")
_Fsp_II_TDMEntry_Object = MibTableRow
fsp_II_TDMEntry = _Fsp_II_TDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1)
)
fsp_II_TDMEntry.setIndexNames(
    (0, "Fsp_II-MIB", "fsp_II_TDMNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_TDMEntry.setStatus("mandatory")
_Fsp_II_TDMNumber_Type = Integer32
_Fsp_II_TDMNumber_Object = MibTableColumn
fsp_II_TDMNumber = _Fsp_II_TDMNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 1),
    _Fsp_II_TDMNumber_Type()
)
fsp_II_TDMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMNumber.setStatus("mandatory")


class _Fsp_II_TDMRxRem_Type(Integer32):
    """Custom type fsp_II_TDMRxRem based on Integer32"""
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


_Fsp_II_TDMRxRem_Type.__name__ = "Integer32"
_Fsp_II_TDMRxRem_Object = MibTableColumn
fsp_II_TDMRxRem = _Fsp_II_TDMRxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 4),
    _Fsp_II_TDMRxRem_Type()
)
fsp_II_TDMRxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMRxRem.setStatus("mandatory")


class _Fsp_II_TDMRxSync_Type(Integer32):
    """Custom type fsp_II_TDMRxSync based on Integer32"""
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


_Fsp_II_TDMRxSync_Type.__name__ = "Integer32"
_Fsp_II_TDMRxSync_Object = MibTableColumn
fsp_II_TDMRxSync = _Fsp_II_TDMRxSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 5),
    _Fsp_II_TDMRxSync_Type()
)
fsp_II_TDMRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMRxSync.setStatus("mandatory")


class _Fsp_II_TDMTxRem_Type(Integer32):
    """Custom type fsp_II_TDMTxRem based on Integer32"""
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


_Fsp_II_TDMTxRem_Type.__name__ = "Integer32"
_Fsp_II_TDMTxRem_Object = MibTableColumn
fsp_II_TDMTxRem = _Fsp_II_TDMTxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 6),
    _Fsp_II_TDMTxRem_Type()
)
fsp_II_TDMTxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMTxRem.setStatus("mandatory")


class _Fsp_II_TDMTxRemC_Type(Integer32):
    """Custom type fsp_II_TDMTxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fsp_II_TDMTxRemC_Type.__name__ = "Integer32"
_Fsp_II_TDMTxRemC_Object = MibTableColumn
fsp_II_TDMTxRemC = _Fsp_II_TDMTxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 7),
    _Fsp_II_TDMTxRemC_Type()
)
fsp_II_TDMTxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMTxRemC.setStatus("mandatory")


class _Fsp_II_TDMTxRemTemp_Type(Integer32):
    """Custom type fsp_II_TDMTxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Fsp_II_TDMTxRemTemp_Type.__name__ = "Integer32"
_Fsp_II_TDMTxRemTemp_Object = MibTableColumn
fsp_II_TDMTxRemTemp = _Fsp_II_TDMTxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 8),
    _Fsp_II_TDMTxRemTemp_Type()
)
fsp_II_TDMTxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMTxRemTemp.setStatus("mandatory")


class _Fsp_II_TDMLocLoop_Type(Integer32):
    """Custom type fsp_II_TDMLocLoop based on Integer32"""
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


_Fsp_II_TDMLocLoop_Type.__name__ = "Integer32"
_Fsp_II_TDMLocLoop_Object = MibTableColumn
fsp_II_TDMLocLoop = _Fsp_II_TDMLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 9),
    _Fsp_II_TDMLocLoop_Type()
)
fsp_II_TDMLocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocLoop.setStatus("mandatory")


class _Fsp_II_TDMLocModuleInst1_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleInst1 based on Integer32"""
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


_Fsp_II_TDMLocModuleInst1_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleInst1_Object = MibTableColumn
fsp_II_TDMLocModuleInst1 = _Fsp_II_TDMLocModuleInst1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 20),
    _Fsp_II_TDMLocModuleInst1_Type()
)
fsp_II_TDMLocModuleInst1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleInst1.setStatus("mandatory")


class _Fsp_II_TDMLocModuleEnable1_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleEnable1 based on Integer32"""
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


_Fsp_II_TDMLocModuleEnable1_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleEnable1_Object = MibTableColumn
fsp_II_TDMLocModuleEnable1 = _Fsp_II_TDMLocModuleEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 21),
    _Fsp_II_TDMLocModuleEnable1_Type()
)
fsp_II_TDMLocModuleEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleEnable1.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRx1_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRx1 based on Integer32"""
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


_Fsp_II_TDMLocModuleRx1_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRx1_Object = MibTableColumn
fsp_II_TDMLocModuleRx1 = _Fsp_II_TDMLocModuleRx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 22),
    _Fsp_II_TDMLocModuleRx1_Type()
)
fsp_II_TDMLocModuleRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRx1.setStatus("mandatory")


class _Fsp_II_TDMLocModuleTx1_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleTx1 based on Integer32"""
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


_Fsp_II_TDMLocModuleTx1_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleTx1_Object = MibTableColumn
fsp_II_TDMLocModuleTx1 = _Fsp_II_TDMLocModuleTx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 23),
    _Fsp_II_TDMLocModuleTx1_Type()
)
fsp_II_TDMLocModuleTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleTx1.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRemoteData1_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRemoteData1 based on Integer32"""
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


_Fsp_II_TDMLocModuleRemoteData1_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRemoteData1_Object = MibTableColumn
fsp_II_TDMLocModuleRemoteData1 = _Fsp_II_TDMLocModuleRemoteData1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 24),
    _Fsp_II_TDMLocModuleRemoteData1_Type()
)
fsp_II_TDMLocModuleRemoteData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRemoteData1.setStatus("mandatory")
_Fsp_II_TDMLocModuleClockFrequency1_Type = Integer32
_Fsp_II_TDMLocModuleClockFrequency1_Object = MibTableColumn
fsp_II_TDMLocModuleClockFrequency1 = _Fsp_II_TDMLocModuleClockFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 25),
    _Fsp_II_TDMLocModuleClockFrequency1_Type()
)
fsp_II_TDMLocModuleClockFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockFrequency1.setStatus("mandatory")


class _Fsp_II_TDMLocModuleClockError1_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleClockError1 based on Integer32"""
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


_Fsp_II_TDMLocModuleClockError1_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleClockError1_Object = MibTableColumn
fsp_II_TDMLocModuleClockError1 = _Fsp_II_TDMLocModuleClockError1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 26),
    _Fsp_II_TDMLocModuleClockError1_Type()
)
fsp_II_TDMLocModuleClockError1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockError1.setStatus("mandatory")


class _Fsp_II_TDMLocModuleInst2_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleInst2 based on Integer32"""
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


_Fsp_II_TDMLocModuleInst2_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleInst2_Object = MibTableColumn
fsp_II_TDMLocModuleInst2 = _Fsp_II_TDMLocModuleInst2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 30),
    _Fsp_II_TDMLocModuleInst2_Type()
)
fsp_II_TDMLocModuleInst2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleInst2.setStatus("mandatory")


class _Fsp_II_TDMLocModuleEnable2_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleEnable2 based on Integer32"""
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


_Fsp_II_TDMLocModuleEnable2_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleEnable2_Object = MibTableColumn
fsp_II_TDMLocModuleEnable2 = _Fsp_II_TDMLocModuleEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 31),
    _Fsp_II_TDMLocModuleEnable2_Type()
)
fsp_II_TDMLocModuleEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleEnable2.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRx2_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRx2 based on Integer32"""
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


_Fsp_II_TDMLocModuleRx2_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRx2_Object = MibTableColumn
fsp_II_TDMLocModuleRx2 = _Fsp_II_TDMLocModuleRx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 32),
    _Fsp_II_TDMLocModuleRx2_Type()
)
fsp_II_TDMLocModuleRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRx2.setStatus("mandatory")


class _Fsp_II_TDMLocModuleTx2_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleTx2 based on Integer32"""
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


_Fsp_II_TDMLocModuleTx2_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleTx2_Object = MibTableColumn
fsp_II_TDMLocModuleTx2 = _Fsp_II_TDMLocModuleTx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 33),
    _Fsp_II_TDMLocModuleTx2_Type()
)
fsp_II_TDMLocModuleTx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleTx2.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRemoteData2_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRemoteData2 based on Integer32"""
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


_Fsp_II_TDMLocModuleRemoteData2_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRemoteData2_Object = MibTableColumn
fsp_II_TDMLocModuleRemoteData2 = _Fsp_II_TDMLocModuleRemoteData2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 34),
    _Fsp_II_TDMLocModuleRemoteData2_Type()
)
fsp_II_TDMLocModuleRemoteData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRemoteData2.setStatus("mandatory")
_Fsp_II_TDMLocModuleClockFrequency2_Type = Integer32
_Fsp_II_TDMLocModuleClockFrequency2_Object = MibTableColumn
fsp_II_TDMLocModuleClockFrequency2 = _Fsp_II_TDMLocModuleClockFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 35),
    _Fsp_II_TDMLocModuleClockFrequency2_Type()
)
fsp_II_TDMLocModuleClockFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockFrequency2.setStatus("mandatory")


class _Fsp_II_TDMLocModuleClockError2_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleClockError2 based on Integer32"""
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


_Fsp_II_TDMLocModuleClockError2_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleClockError2_Object = MibTableColumn
fsp_II_TDMLocModuleClockError2 = _Fsp_II_TDMLocModuleClockError2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 36),
    _Fsp_II_TDMLocModuleClockError2_Type()
)
fsp_II_TDMLocModuleClockError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockError2.setStatus("mandatory")


class _Fsp_II_TDMLocModuleInst3_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleInst3 based on Integer32"""
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


_Fsp_II_TDMLocModuleInst3_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleInst3_Object = MibTableColumn
fsp_II_TDMLocModuleInst3 = _Fsp_II_TDMLocModuleInst3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 40),
    _Fsp_II_TDMLocModuleInst3_Type()
)
fsp_II_TDMLocModuleInst3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleInst3.setStatus("mandatory")


class _Fsp_II_TDMLocModuleEnable3_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleEnable3 based on Integer32"""
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


_Fsp_II_TDMLocModuleEnable3_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleEnable3_Object = MibTableColumn
fsp_II_TDMLocModuleEnable3 = _Fsp_II_TDMLocModuleEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 41),
    _Fsp_II_TDMLocModuleEnable3_Type()
)
fsp_II_TDMLocModuleEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleEnable3.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRx3_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRx3 based on Integer32"""
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


_Fsp_II_TDMLocModuleRx3_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRx3_Object = MibTableColumn
fsp_II_TDMLocModuleRx3 = _Fsp_II_TDMLocModuleRx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 42),
    _Fsp_II_TDMLocModuleRx3_Type()
)
fsp_II_TDMLocModuleRx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRx3.setStatus("mandatory")


class _Fsp_II_TDMLocModuleTx3_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleTx3 based on Integer32"""
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


_Fsp_II_TDMLocModuleTx3_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleTx3_Object = MibTableColumn
fsp_II_TDMLocModuleTx3 = _Fsp_II_TDMLocModuleTx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 43),
    _Fsp_II_TDMLocModuleTx3_Type()
)
fsp_II_TDMLocModuleTx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleTx3.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRemoteData3_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRemoteData3 based on Integer32"""
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


_Fsp_II_TDMLocModuleRemoteData3_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRemoteData3_Object = MibTableColumn
fsp_II_TDMLocModuleRemoteData3 = _Fsp_II_TDMLocModuleRemoteData3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 44),
    _Fsp_II_TDMLocModuleRemoteData3_Type()
)
fsp_II_TDMLocModuleRemoteData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRemoteData3.setStatus("mandatory")
_Fsp_II_TDMLocModuleClockFrequency3_Type = Integer32
_Fsp_II_TDMLocModuleClockFrequency3_Object = MibTableColumn
fsp_II_TDMLocModuleClockFrequency3 = _Fsp_II_TDMLocModuleClockFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 45),
    _Fsp_II_TDMLocModuleClockFrequency3_Type()
)
fsp_II_TDMLocModuleClockFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockFrequency3.setStatus("mandatory")


class _Fsp_II_TDMLocModuleClockError3_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleClockError3 based on Integer32"""
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


_Fsp_II_TDMLocModuleClockError3_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleClockError3_Object = MibTableColumn
fsp_II_TDMLocModuleClockError3 = _Fsp_II_TDMLocModuleClockError3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 46),
    _Fsp_II_TDMLocModuleClockError3_Type()
)
fsp_II_TDMLocModuleClockError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockError3.setStatus("mandatory")


class _Fsp_II_TDMLocModuleInst4_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleInst4 based on Integer32"""
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


_Fsp_II_TDMLocModuleInst4_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleInst4_Object = MibTableColumn
fsp_II_TDMLocModuleInst4 = _Fsp_II_TDMLocModuleInst4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 50),
    _Fsp_II_TDMLocModuleInst4_Type()
)
fsp_II_TDMLocModuleInst4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleInst4.setStatus("mandatory")


class _Fsp_II_TDMLocModuleEnable4_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleEnable4 based on Integer32"""
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


_Fsp_II_TDMLocModuleEnable4_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleEnable4_Object = MibTableColumn
fsp_II_TDMLocModuleEnable4 = _Fsp_II_TDMLocModuleEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 51),
    _Fsp_II_TDMLocModuleEnable4_Type()
)
fsp_II_TDMLocModuleEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleEnable4.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRx4_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRx4 based on Integer32"""
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


_Fsp_II_TDMLocModuleRx4_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRx4_Object = MibTableColumn
fsp_II_TDMLocModuleRx4 = _Fsp_II_TDMLocModuleRx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 52),
    _Fsp_II_TDMLocModuleRx4_Type()
)
fsp_II_TDMLocModuleRx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRx4.setStatus("mandatory")


class _Fsp_II_TDMLocModuleTx4_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleTx4 based on Integer32"""
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


_Fsp_II_TDMLocModuleTx4_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleTx4_Object = MibTableColumn
fsp_II_TDMLocModuleTx4 = _Fsp_II_TDMLocModuleTx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 53),
    _Fsp_II_TDMLocModuleTx4_Type()
)
fsp_II_TDMLocModuleTx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleTx4.setStatus("mandatory")


class _Fsp_II_TDMLocModuleRemoteData4_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleRemoteData4 based on Integer32"""
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


_Fsp_II_TDMLocModuleRemoteData4_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleRemoteData4_Object = MibTableColumn
fsp_II_TDMLocModuleRemoteData4 = _Fsp_II_TDMLocModuleRemoteData4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 54),
    _Fsp_II_TDMLocModuleRemoteData4_Type()
)
fsp_II_TDMLocModuleRemoteData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleRemoteData4.setStatus("mandatory")
_Fsp_II_TDMLocModuleClockFrequency4_Type = Integer32
_Fsp_II_TDMLocModuleClockFrequency4_Object = MibTableColumn
fsp_II_TDMLocModuleClockFrequency4 = _Fsp_II_TDMLocModuleClockFrequency4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 55),
    _Fsp_II_TDMLocModuleClockFrequency4_Type()
)
fsp_II_TDMLocModuleClockFrequency4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockFrequency4.setStatus("mandatory")


class _Fsp_II_TDMLocModuleClockError4_Type(Integer32):
    """Custom type fsp_II_TDMLocModuleClockError4 based on Integer32"""
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


_Fsp_II_TDMLocModuleClockError4_Type.__name__ = "Integer32"
_Fsp_II_TDMLocModuleClockError4_Object = MibTableColumn
fsp_II_TDMLocModuleClockError4 = _Fsp_II_TDMLocModuleClockError4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 56),
    _Fsp_II_TDMLocModuleClockError4_Type()
)
fsp_II_TDMLocModuleClockError4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_TDMLocModuleClockError4.setStatus("mandatory")
_Fsp_II_Trap_ObjectIdentity = ObjectIdentity
fsp_II_Trap = _Fsp_II_Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100)
)

# Managed Objects groups


# Notification objects

fspIIHardwareAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 1)
)
fspIIHardwareAdded.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIHardwareAdded.setStatus(
        ""
    )

fspIIHardwareDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 2)
)
fspIIHardwareDeleted.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIHardwareDeleted.setStatus(
        ""
    )

fspIIPSNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 3)
)
fspIIPSNotFail.setObjects(
    ("Fsp_II-MIB", "fsp_II_PSNumber")
)
if mibBuilder.loadTexts:
    fspIIPSNotFail.setStatus(
        ""
    )

fspIIPSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 4)
)
fspIIPSFail.setObjects(
    ("Fsp_II-MIB", "fsp_II_PSNumber")
)
if mibBuilder.loadTexts:
    fspIIPSFail.setStatus(
        ""
    )

fspIIFanNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 5)
)
fspIIFanNotFail.setObjects(
    ("Fsp_II-MIB", "fsp_II_FanNumber")
)
if mibBuilder.loadTexts:
    fspIIFanNotFail.setStatus(
        ""
    )

fspIIFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 6)
)
fspIIFanFail.setObjects(
    ("Fsp_II-MIB", "fsp_II_FanNumber")
)
if mibBuilder.loadTexts:
    fspIIFanFail.setStatus(
        ""
    )

fspIIBusNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 7)
)
if mibBuilder.loadTexts:
    fspIIBusNotFail.setStatus(
        ""
    )

fspIIBusFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 8)
)
if mibBuilder.loadTexts:
    fspIIBusFail.setStatus(
        ""
    )

fspIIRxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 20)
)
fspIIRxLocOn.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRxLocOn.setStatus(
        ""
    )

fspIIRxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 21)
)
fspIIRxLocOff.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRxLocOff.setStatus(
        ""
    )

fspIITxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 22)
)
fspIITxLocOn.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITxLocOn.setStatus(
        ""
    )

fspIITxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 23)
)
fspIITxLocOff.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITxLocOff.setStatus(
        ""
    )

fspIIRxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 24)
)
fspIIRxRemOn.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRxRemOn.setStatus(
        ""
    )

fspIIRxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 25)
)
fspIIRxRemOff.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRxRemOff.setStatus(
        ""
    )

fspIITxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 26)
)
fspIITxRemOn.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITxRemOn.setStatus(
        ""
    )

fspIITxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 27)
)
fspIITxRemOff.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITxRemOff.setStatus(
        ""
    )

fspIIRxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 28)
)
fspIIRxRem2On.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRxRem2On.setStatus(
        ""
    )

fspIIRxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 29)
)
fspIIRxRem2Off.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRxRem2Off.setStatus(
        ""
    )

fspIITxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 30)
)
fspIITxRem2On.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITxRem2On.setStatus(
        ""
    )

fspIITxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 31)
)
fspIITxRem2Off.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITxRem2Off.setStatus(
        ""
    )

fspIIClockNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 32)
)
fspIIClockNoFail.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIClockNoFail.setStatus(
        ""
    )

fspIIClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 33)
)
fspIIClockFail.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIClockFail.setStatus(
        ""
    )

fspIIClockChangeFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 34)
)
fspIIClockChangeFrequency.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIClockChangeFrequency.setStatus(
        ""
    )

fspIILocLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 35)
)
fspIILocLoopOn.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIILocLoopOn.setStatus(
        ""
    )

fspIILocLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 36)
)
fspIILocLoopOff.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIILocLoopOff.setStatus(
        ""
    )

fspIIRemLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 37)
)
fspIIRemLoopOn.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRemLoopOn.setStatus(
        ""
    )

fspIIRemLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 38)
)
fspIIRemLoopOff.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIRemLoopOff.setStatus(
        ""
    )

fspIIswitchReferenceLaserOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 40)
)
fspIIswitchReferenceLaserOn.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchReferenceLaserOn.setStatus(
        ""
    )

fspIIswitchReferenceLaserOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 41)
)
fspIIswitchReferenceLaserOff.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchReferenceLaserOff.setStatus(
        ""
    )

fspIIswitchToA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 42)
)
fspIIswitchToA.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchToA.setStatus(
        ""
    )

fspIIswitchToB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 43)
)
fspIIswitchToB.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchToB.setStatus(
        ""
    )

fspIIswitchAutomatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 44)
)
fspIIswitchAutomatic.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchAutomatic.setStatus(
        ""
    )

fspIIswitchLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 45)
)
fspIIswitchLocked.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchLocked.setStatus(
        ""
    )

fspIIswitchLineAavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 46)
)
fspIIswitchLineAavail.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchLineAavail.setStatus(
        ""
    )

fspIIswitchLineANotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 47)
)
fspIIswitchLineANotAvail.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchLineANotAvail.setStatus(
        ""
    )

fspIIswitchLineBavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 48)
)
fspIIswitchLineBavail.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchLineBavail.setStatus(
        ""
    )

fspIIswitchLineBNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 49)
)
fspIIswitchLineBNotAvail.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIswitchLineBNotAvail.setStatus(
        ""
    )

fspIIrepeatedMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 50)
)
fspIIrepeatedMessage.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIrepeatedMessage.setStatus(
        ""
    )

fspIIINNCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 51)
)
if mibBuilder.loadTexts:
    fspIIINNCDown.setStatus(
        ""
    )

fspIIINNCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 52)
)
if mibBuilder.loadTexts:
    fspIIINNCUp.setStatus(
        ""
    )

fspIIEthernetHubPortEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 60)
)
fspIIEthernetHubPortEnable.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIEthernetHubPortEnable.setStatus(
        ""
    )

fspIIEthernetHubPortDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 61)
)
fspIIEthernetHubPortDisable.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIEthernetHubPortDisable.setStatus(
        ""
    )

fspIIEthernetHubPortPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 62)
)
fspIIEthernetHubPortPartitioned.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIEthernetHubPortPartitioned.setStatus(
        ""
    )

fspIIEthernetHubPortNotPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 63)
)
fspIIEthernetHubPortNotPartitioned.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIEthernetHubPortNotPartitioned.setStatus(
        ""
    )

fspIIEthernetHubPortLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 64)
)
fspIIEthernetHubPortLinkPulses.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIEthernetHubPortLinkPulses.setStatus(
        ""
    )

fspIIEthernetHubPortNoLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 65)
)
fspIIEthernetHubPortNoLinkPulses.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIIEthernetHubPortNoLinkPulses.setStatus(
        ""
    )

fspIITDMRemoteSyncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 70)
)
fspIITDMRemoteSyncLoss.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMRemoteSyncLoss.setStatus(
        ""
    )

fspIITDMRemoteSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 71)
)
fspIITDMRemoteSync.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMRemoteSync.setStatus(
        ""
    )

fspIITDMLocModuleEnable1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 72)
)
fspIITDMLocModuleEnable1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleEnable1.setStatus(
        ""
    )

fspIITDMLocModuleDisable1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 73)
)
fspIITDMLocModuleDisable1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleDisable1.setStatus(
        ""
    )

fspIITDMLocModuleEnable2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 74)
)
fspIITDMLocModuleEnable2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleEnable2.setStatus(
        ""
    )

fspIITDMLocModuleDisable2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 75)
)
fspIITDMLocModuleDisable2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleDisable2.setStatus(
        ""
    )

fspIITDMLocModuleEnable3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 76)
)
fspIITDMLocModuleEnable3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleEnable3.setStatus(
        ""
    )

fspIITDMLocModuleDisable3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 77)
)
fspIITDMLocModuleDisable3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleDisable3.setStatus(
        ""
    )

fspIITDMLocModuleEnable4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 78)
)
fspIITDMLocModuleEnable4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleEnable4.setStatus(
        ""
    )

fspIITDMLocModuleDisable4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 79)
)
fspIITDMLocModuleDisable4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleDisable4.setStatus(
        ""
    )

fspIITDMLocModuleRxOn1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 88)
)
fspIITDMLocModuleRxOn1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOn1.setStatus(
        ""
    )

fspIITDMLocModuleRxOff1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 89)
)
fspIITDMLocModuleRxOff1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOff1.setStatus(
        ""
    )

fspIITDMLocModuleRxOn2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 90)
)
fspIITDMLocModuleRxOn2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOn2.setStatus(
        ""
    )

fspIITDMLocModuleRxOff2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 91)
)
fspIITDMLocModuleRxOff2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOff2.setStatus(
        ""
    )

fspIITDMLocModuleRxOn3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 92)
)
fspIITDMLocModuleRxOn3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOn3.setStatus(
        ""
    )

fspIITDMLocModuleRxOff3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 93)
)
fspIITDMLocModuleRxOff3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOff3.setStatus(
        ""
    )

fspIITDMLocModuleRxOn4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 94)
)
fspIITDMLocModuleRxOn4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOn4.setStatus(
        ""
    )

fspIITDMLocModuleRxOff4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 95)
)
fspIITDMLocModuleRxOff4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleRxOff4.setStatus(
        ""
    )

fspIITDMLocModuleData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 104)
)
fspIITDMLocModuleData1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleData1.setStatus(
        ""
    )

fspIITDMLocModuleNoData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 105)
)
fspIITDMLocModuleNoData1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleNoData1.setStatus(
        ""
    )

fspIITDMLocModuleData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 106)
)
fspIITDMLocModuleData2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleData2.setStatus(
        ""
    )

fspIITDMLocModuleNoData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 107)
)
fspIITDMLocModuleNoData2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleNoData2.setStatus(
        ""
    )

fspIITDMLocModuleData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 108)
)
fspIITDMLocModuleData3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleData3.setStatus(
        ""
    )

fspIITDMLocModuleNoData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 109)
)
fspIITDMLocModuleNoData3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleNoData3.setStatus(
        ""
    )

fspIITDMLocModuleData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 110)
)
fspIITDMLocModuleData4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleData4.setStatus(
        ""
    )

fspIITDMLocModuleNoData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 111)
)
fspIITDMLocModuleNoData4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleNoData4.setStatus(
        ""
    )

fspIITDMLocModuleClockFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 120)
)
fspIITDMLocModuleClockFail1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockFail1.setStatus(
        ""
    )

fspIITDMLocModuleClockNoFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 121)
)
fspIITDMLocModuleClockNoFail1.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockNoFail1.setStatus(
        ""
    )

fspIITDMLocModuleClockFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 122)
)
fspIITDMLocModuleClockFail2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockFail2.setStatus(
        ""
    )

fspIITDMLocModuleClockNoFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 123)
)
fspIITDMLocModuleClockNoFail2.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockNoFail2.setStatus(
        ""
    )

fspIITDMLocModuleClockFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 124)
)
fspIITDMLocModuleClockFail3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockFail3.setStatus(
        ""
    )

fspIITDMLocModuleClockNoFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 125)
)
fspIITDMLocModuleClockNoFail3.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockNoFail3.setStatus(
        ""
    )

fspIITDMLocModuleClockFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 126)
)
fspIITDMLocModuleClockFail4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockFail4.setStatus(
        ""
    )

fspIITDMLocModuleClockNoFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 127)
)
fspIITDMLocModuleClockNoFail4.setObjects(
    ("Fsp_II-MIB", "fsp_II_SlotNumber")
)
if mibBuilder.loadTexts:
    fspIITDMLocModuleClockNoFail4.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fsp_II-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "adva": adva,
       "products": products,
       "fsp_II": fsp_II,
       "fsp_II_Main": fsp_II_Main,
       "fsp_II_Housing": fsp_II_Housing,
       "fsp_II_Manufacturer": fsp_II_Manufacturer,
       "fsp_II_MainType": fsp_II_MainType,
       "fsp_II_MainSerialNumber": fsp_II_MainSerialNumber,
       "fsp_II_MainHardwareVersion": fsp_II_MainHardwareVersion,
       "fsp_II_MainSoftwareVersion": fsp_II_MainSoftwareVersion,
       "fsp_II_MainBusMessages": fsp_II_MainBusMessages,
       "fsp_II_MainBusErrors": fsp_II_MainBusErrors,
       "fsp_II_MainLastEvent": fsp_II_MainLastEvent,
       "fsp_II_MainMotd": fsp_II_MainMotd,
       "fsp_II_MainTrapsinkTable": fsp_II_MainTrapsinkTable,
       "fsp_II_MainTrapsinkEntry": fsp_II_MainTrapsinkEntry,
       "fsp_II_MainTrapsinkNumber": fsp_II_MainTrapsinkNumber,
       "fsp_II_MainTrapsinkAddress": fsp_II_MainTrapsinkAddress,
       "fsp_II_MainTrapsinkCommunity": fsp_II_MainTrapsinkCommunity,
       "fsp_II_MainTrapsinkPriority": fsp_II_MainTrapsinkPriority,
       "fsp_II_MainLogfileTable": fsp_II_MainLogfileTable,
       "fsp_II_MainLogfileEntry": fsp_II_MainLogfileEntry,
       "fsp_II_MainLogfileNumber": fsp_II_MainLogfileNumber,
       "fsp_II_MainLogfileName": fsp_II_MainLogfileName,
       "fsp_II_MainLogfileSize": fsp_II_MainLogfileSize,
       "fsp_II_MainLogfilePriority": fsp_II_MainLogfilePriority,
       "fsp_II_SlotTable": fsp_II_SlotTable,
       "fsp_II_SlotEntry": fsp_II_SlotEntry,
       "fsp_II_SlotNumber": fsp_II_SlotNumber,
       "fsp_II_Type": fsp_II_Type,
       "fsp_II_SlotTypeNumber": fsp_II_SlotTypeNumber,
       "fsp_II_SerialNumber": fsp_II_SerialNumber,
       "fsp_II_HardwareVersion": fsp_II_HardwareVersion,
       "fsp_II_SoftwareVersion": fsp_II_SoftwareVersion,
       "fsp_II_Temperature": fsp_II_Temperature,
       "fsp_II_BoardVoltage": fsp_II_BoardVoltage,
       "fsp_II_DetailInfo": fsp_II_DetailInfo,
       "fsp_II_EPLDVersion": fsp_II_EPLDVersion,
       "fsp_II_PSTable": fsp_II_PSTable,
       "fsp_II_PSEntry": fsp_II_PSEntry,
       "fsp_II_PSNumber": fsp_II_PSNumber,
       "fsp_II_PSOn": fsp_II_PSOn,
       "fsp_II_FanTable": fsp_II_FanTable,
       "fsp_II_FanEntry": fsp_II_FanEntry,
       "fsp_II_FanNumber": fsp_II_FanNumber,
       "fsp_II_FanOn": fsp_II_FanOn,
       "fsp_II_Converter": fsp_II_Converter,
       "fsp_II_ConverterTable": fsp_II_ConverterTable,
       "fsp_II_ConverterEntry": fsp_II_ConverterEntry,
       "fsp_II_ConverterNumber": fsp_II_ConverterNumber,
       "fsp_II_RxLoc": fsp_II_RxLoc,
       "fsp_II_TxLoc": fsp_II_TxLoc,
       "fsp_II_TxLocC": fsp_II_TxLocC,
       "fsp_II_TxLocTemp": fsp_II_TxLocTemp,
       "fsp_II_RxRem": fsp_II_RxRem,
       "fsp_II_TxRem": fsp_II_TxRem,
       "fsp_II_TxRemC": fsp_II_TxRemC,
       "fsp_II_TxRemTemp": fsp_II_TxRemTemp,
       "fsp_II_RxRem2": fsp_II_RxRem2,
       "fsp_II_ClockState": fsp_II_ClockState,
       "fsp_II_ClockFreq": fsp_II_ClockFreq,
       "fsp_II_LocLoop": fsp_II_LocLoop,
       "fsp_II_RemLoop": fsp_II_RemLoop,
       "fsp_II_ClockType": fsp_II_ClockType,
       "fsp_II_Switch": fsp_II_Switch,
       "fsp_II_SwitchTable": fsp_II_SwitchTable,
       "fsp_II_SwitchEntry": fsp_II_SwitchEntry,
       "fsp_II_SwitchNumber": fsp_II_SwitchNumber,
       "fsp_II_SwitchLine": fsp_II_SwitchLine,
       "fsp_II_SwitchMode": fsp_II_SwitchMode,
       "fsp_II_SwitchLaserOn": fsp_II_SwitchLaserOn,
       "fsp_II_SwitchLineAavail": fsp_II_SwitchLineAavail,
       "fsp_II_SwitchLineBavail": fsp_II_SwitchLineBavail,
       "fsp_II_EthernetHub": fsp_II_EthernetHub,
       "fsp_II_EthernetHubTable": fsp_II_EthernetHubTable,
       "fsp_II_EthernetHubEntry": fsp_II_EthernetHubEntry,
       "fsp_II_EthernetHubNumber": fsp_II_EthernetHubNumber,
       "fsp_II_EthernetHubPortEnable1": fsp_II_EthernetHubPortEnable1,
       "fsp_II_EthernetHubPortPartitionStatus1": fsp_II_EthernetHubPortPartitionStatus1,
       "fsp_II_EthernetHubPortLinkStatus1": fsp_II_EthernetHubPortLinkStatus1,
       "fsp_II_EthernetHubPortPolarity1": fsp_II_EthernetHubPortPolarity1,
       "fsp_II_EthernetHubPortEnable2": fsp_II_EthernetHubPortEnable2,
       "fsp_II_EthernetHubPortPartitionStatus2": fsp_II_EthernetHubPortPartitionStatus2,
       "fsp_II_EthernetHubPortLinkStatus2": fsp_II_EthernetHubPortLinkStatus2,
       "fsp_II_EthernetHubPortPolarity2": fsp_II_EthernetHubPortPolarity2,
       "fsp_II_EthernetHubPortEnable3": fsp_II_EthernetHubPortEnable3,
       "fsp_II_EthernetHubPortPartitionStatus3": fsp_II_EthernetHubPortPartitionStatus3,
       "fsp_II_EthernetHubPortLinkStatus3": fsp_II_EthernetHubPortLinkStatus3,
       "fsp_II_EthernetHubPortPolarity3": fsp_II_EthernetHubPortPolarity3,
       "fsp_II_EthernetHubPortEnable4": fsp_II_EthernetHubPortEnable4,
       "fsp_II_EthernetHubPortPartitionStatus4": fsp_II_EthernetHubPortPartitionStatus4,
       "fsp_II_EthernetHubPortLinkStatus4": fsp_II_EthernetHubPortLinkStatus4,
       "fsp_II_EthernetHubPortPolarity4": fsp_II_EthernetHubPortPolarity4,
       "fsp_II_EthernetHubPortEnable5": fsp_II_EthernetHubPortEnable5,
       "fsp_II_EthernetHubPortPartitionStatus5": fsp_II_EthernetHubPortPartitionStatus5,
       "fsp_II_EthernetHubPortLinkStatus5": fsp_II_EthernetHubPortLinkStatus5,
       "fsp_II_EthernetHubPortPolarity5": fsp_II_EthernetHubPortPolarity5,
       "fsp_II_TDM": fsp_II_TDM,
       "fsp_II_TDMTable": fsp_II_TDMTable,
       "fsp_II_TDMEntry": fsp_II_TDMEntry,
       "fsp_II_TDMNumber": fsp_II_TDMNumber,
       "fsp_II_TDMRxRem": fsp_II_TDMRxRem,
       "fsp_II_TDMRxSync": fsp_II_TDMRxSync,
       "fsp_II_TDMTxRem": fsp_II_TDMTxRem,
       "fsp_II_TDMTxRemC": fsp_II_TDMTxRemC,
       "fsp_II_TDMTxRemTemp": fsp_II_TDMTxRemTemp,
       "fsp_II_TDMLocLoop": fsp_II_TDMLocLoop,
       "fsp_II_TDMLocModuleInst1": fsp_II_TDMLocModuleInst1,
       "fsp_II_TDMLocModuleEnable1": fsp_II_TDMLocModuleEnable1,
       "fsp_II_TDMLocModuleRx1": fsp_II_TDMLocModuleRx1,
       "fsp_II_TDMLocModuleTx1": fsp_II_TDMLocModuleTx1,
       "fsp_II_TDMLocModuleRemoteData1": fsp_II_TDMLocModuleRemoteData1,
       "fsp_II_TDMLocModuleClockFrequency1": fsp_II_TDMLocModuleClockFrequency1,
       "fsp_II_TDMLocModuleClockError1": fsp_II_TDMLocModuleClockError1,
       "fsp_II_TDMLocModuleInst2": fsp_II_TDMLocModuleInst2,
       "fsp_II_TDMLocModuleEnable2": fsp_II_TDMLocModuleEnable2,
       "fsp_II_TDMLocModuleRx2": fsp_II_TDMLocModuleRx2,
       "fsp_II_TDMLocModuleTx2": fsp_II_TDMLocModuleTx2,
       "fsp_II_TDMLocModuleRemoteData2": fsp_II_TDMLocModuleRemoteData2,
       "fsp_II_TDMLocModuleClockFrequency2": fsp_II_TDMLocModuleClockFrequency2,
       "fsp_II_TDMLocModuleClockError2": fsp_II_TDMLocModuleClockError2,
       "fsp_II_TDMLocModuleInst3": fsp_II_TDMLocModuleInst3,
       "fsp_II_TDMLocModuleEnable3": fsp_II_TDMLocModuleEnable3,
       "fsp_II_TDMLocModuleRx3": fsp_II_TDMLocModuleRx3,
       "fsp_II_TDMLocModuleTx3": fsp_II_TDMLocModuleTx3,
       "fsp_II_TDMLocModuleRemoteData3": fsp_II_TDMLocModuleRemoteData3,
       "fsp_II_TDMLocModuleClockFrequency3": fsp_II_TDMLocModuleClockFrequency3,
       "fsp_II_TDMLocModuleClockError3": fsp_II_TDMLocModuleClockError3,
       "fsp_II_TDMLocModuleInst4": fsp_II_TDMLocModuleInst4,
       "fsp_II_TDMLocModuleEnable4": fsp_II_TDMLocModuleEnable4,
       "fsp_II_TDMLocModuleRx4": fsp_II_TDMLocModuleRx4,
       "fsp_II_TDMLocModuleTx4": fsp_II_TDMLocModuleTx4,
       "fsp_II_TDMLocModuleRemoteData4": fsp_II_TDMLocModuleRemoteData4,
       "fsp_II_TDMLocModuleClockFrequency4": fsp_II_TDMLocModuleClockFrequency4,
       "fsp_II_TDMLocModuleClockError4": fsp_II_TDMLocModuleClockError4,
       "fsp_II_Trap": fsp_II_Trap,
       "fspIIHardwareAdded": fspIIHardwareAdded,
       "fspIIHardwareDeleted": fspIIHardwareDeleted,
       "fspIIPSNotFail": fspIIPSNotFail,
       "fspIIPSFail": fspIIPSFail,
       "fspIIFanNotFail": fspIIFanNotFail,
       "fspIIFanFail": fspIIFanFail,
       "fspIIBusNotFail": fspIIBusNotFail,
       "fspIIBusFail": fspIIBusFail,
       "fspIIRxLocOn": fspIIRxLocOn,
       "fspIIRxLocOff": fspIIRxLocOff,
       "fspIITxLocOn": fspIITxLocOn,
       "fspIITxLocOff": fspIITxLocOff,
       "fspIIRxRemOn": fspIIRxRemOn,
       "fspIIRxRemOff": fspIIRxRemOff,
       "fspIITxRemOn": fspIITxRemOn,
       "fspIITxRemOff": fspIITxRemOff,
       "fspIIRxRem2On": fspIIRxRem2On,
       "fspIIRxRem2Off": fspIIRxRem2Off,
       "fspIITxRem2On": fspIITxRem2On,
       "fspIITxRem2Off": fspIITxRem2Off,
       "fspIIClockNoFail": fspIIClockNoFail,
       "fspIIClockFail": fspIIClockFail,
       "fspIIClockChangeFrequency": fspIIClockChangeFrequency,
       "fspIILocLoopOn": fspIILocLoopOn,
       "fspIILocLoopOff": fspIILocLoopOff,
       "fspIIRemLoopOn": fspIIRemLoopOn,
       "fspIIRemLoopOff": fspIIRemLoopOff,
       "fspIIswitchReferenceLaserOn": fspIIswitchReferenceLaserOn,
       "fspIIswitchReferenceLaserOff": fspIIswitchReferenceLaserOff,
       "fspIIswitchToA": fspIIswitchToA,
       "fspIIswitchToB": fspIIswitchToB,
       "fspIIswitchAutomatic": fspIIswitchAutomatic,
       "fspIIswitchLocked": fspIIswitchLocked,
       "fspIIswitchLineAavail": fspIIswitchLineAavail,
       "fspIIswitchLineANotAvail": fspIIswitchLineANotAvail,
       "fspIIswitchLineBavail": fspIIswitchLineBavail,
       "fspIIswitchLineBNotAvail": fspIIswitchLineBNotAvail,
       "fspIIrepeatedMessage": fspIIrepeatedMessage,
       "fspIIINNCDown": fspIIINNCDown,
       "fspIIINNCUp": fspIIINNCUp,
       "fspIIEthernetHubPortEnable": fspIIEthernetHubPortEnable,
       "fspIIEthernetHubPortDisable": fspIIEthernetHubPortDisable,
       "fspIIEthernetHubPortPartitioned": fspIIEthernetHubPortPartitioned,
       "fspIIEthernetHubPortNotPartitioned": fspIIEthernetHubPortNotPartitioned,
       "fspIIEthernetHubPortLinkPulses": fspIIEthernetHubPortLinkPulses,
       "fspIIEthernetHubPortNoLinkPulses": fspIIEthernetHubPortNoLinkPulses,
       "fspIITDMRemoteSyncLoss": fspIITDMRemoteSyncLoss,
       "fspIITDMRemoteSync": fspIITDMRemoteSync,
       "fspIITDMLocModuleEnable1": fspIITDMLocModuleEnable1,
       "fspIITDMLocModuleDisable1": fspIITDMLocModuleDisable1,
       "fspIITDMLocModuleEnable2": fspIITDMLocModuleEnable2,
       "fspIITDMLocModuleDisable2": fspIITDMLocModuleDisable2,
       "fspIITDMLocModuleEnable3": fspIITDMLocModuleEnable3,
       "fspIITDMLocModuleDisable3": fspIITDMLocModuleDisable3,
       "fspIITDMLocModuleEnable4": fspIITDMLocModuleEnable4,
       "fspIITDMLocModuleDisable4": fspIITDMLocModuleDisable4,
       "fspIITDMLocModuleRxOn1": fspIITDMLocModuleRxOn1,
       "fspIITDMLocModuleRxOff1": fspIITDMLocModuleRxOff1,
       "fspIITDMLocModuleRxOn2": fspIITDMLocModuleRxOn2,
       "fspIITDMLocModuleRxOff2": fspIITDMLocModuleRxOff2,
       "fspIITDMLocModuleRxOn3": fspIITDMLocModuleRxOn3,
       "fspIITDMLocModuleRxOff3": fspIITDMLocModuleRxOff3,
       "fspIITDMLocModuleRxOn4": fspIITDMLocModuleRxOn4,
       "fspIITDMLocModuleRxOff4": fspIITDMLocModuleRxOff4,
       "fspIITDMLocModuleData1": fspIITDMLocModuleData1,
       "fspIITDMLocModuleNoData1": fspIITDMLocModuleNoData1,
       "fspIITDMLocModuleData2": fspIITDMLocModuleData2,
       "fspIITDMLocModuleNoData2": fspIITDMLocModuleNoData2,
       "fspIITDMLocModuleData3": fspIITDMLocModuleData3,
       "fspIITDMLocModuleNoData3": fspIITDMLocModuleNoData3,
       "fspIITDMLocModuleData4": fspIITDMLocModuleData4,
       "fspIITDMLocModuleNoData4": fspIITDMLocModuleNoData4,
       "fspIITDMLocModuleClockFail1": fspIITDMLocModuleClockFail1,
       "fspIITDMLocModuleClockNoFail1": fspIITDMLocModuleClockNoFail1,
       "fspIITDMLocModuleClockFail2": fspIITDMLocModuleClockFail2,
       "fspIITDMLocModuleClockNoFail2": fspIITDMLocModuleClockNoFail2,
       "fspIITDMLocModuleClockFail3": fspIITDMLocModuleClockFail3,
       "fspIITDMLocModuleClockNoFail3": fspIITDMLocModuleClockNoFail3,
       "fspIITDMLocModuleClockFail4": fspIITDMLocModuleClockFail4,
       "fspIITDMLocModuleClockNoFail4": fspIITDMLocModuleClockNoFail4}
)
