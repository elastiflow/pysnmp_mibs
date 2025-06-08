# SNMP MIB module (Fsp_II_Fsp_2000_R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/Fsp_II_Fsp_2000_R1-MIB.mib
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



class Fsp_II_2k_SlotNumberRange(TextualConvention, Integer32):
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
_Fsp_II_2k_ObjectIdentity = ObjectIdentity
fsp_II_2k = _Fsp_II_2k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3)
)
_Fsp_II_2k_Main_ObjectIdentity = ObjectIdentity
fsp_II_2k_Main = _Fsp_II_2k_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1)
)
_Fsp_II_2k_Housing_ObjectIdentity = ObjectIdentity
fsp_II_2k_Housing = _Fsp_II_2k_Housing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1)
)
_Fsp_II_2k_Manufacturer_Type = DisplayString
_Fsp_II_2k_Manufacturer_Object = MibScalar
fsp_II_2k_Manufacturer = _Fsp_II_2k_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 1),
    _Fsp_II_2k_Manufacturer_Type()
)
fsp_II_2k_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_Manufacturer.setStatus("mandatory")
_Fsp_II_2k_MainType_Type = DisplayString
_Fsp_II_2k_MainType_Object = MibScalar
fsp_II_2k_MainType = _Fsp_II_2k_MainType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 2),
    _Fsp_II_2k_MainType_Type()
)
fsp_II_2k_MainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainType.setStatus("mandatory")
_Fsp_II_2k_MainSerialNumber_Type = DisplayString
_Fsp_II_2k_MainSerialNumber_Object = MibScalar
fsp_II_2k_MainSerialNumber = _Fsp_II_2k_MainSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 3),
    _Fsp_II_2k_MainSerialNumber_Type()
)
fsp_II_2k_MainSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainSerialNumber.setStatus("mandatory")
_Fsp_II_2k_MainHardwareVersion_Type = DisplayString
_Fsp_II_2k_MainHardwareVersion_Object = MibScalar
fsp_II_2k_MainHardwareVersion = _Fsp_II_2k_MainHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 4),
    _Fsp_II_2k_MainHardwareVersion_Type()
)
fsp_II_2k_MainHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainHardwareVersion.setStatus("mandatory")
_Fsp_II_2k_MainSoftwareVersion_Type = DisplayString
_Fsp_II_2k_MainSoftwareVersion_Object = MibScalar
fsp_II_2k_MainSoftwareVersion = _Fsp_II_2k_MainSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 5),
    _Fsp_II_2k_MainSoftwareVersion_Type()
)
fsp_II_2k_MainSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainSoftwareVersion.setStatus("mandatory")
_Fsp_II_2k_MainBusMessages_Type = Integer32
_Fsp_II_2k_MainBusMessages_Object = MibScalar
fsp_II_2k_MainBusMessages = _Fsp_II_2k_MainBusMessages_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 6),
    _Fsp_II_2k_MainBusMessages_Type()
)
fsp_II_2k_MainBusMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainBusMessages.setStatus("mandatory")
_Fsp_II_2k_MainBusErrors_Type = Integer32
_Fsp_II_2k_MainBusErrors_Object = MibScalar
fsp_II_2k_MainBusErrors = _Fsp_II_2k_MainBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 7),
    _Fsp_II_2k_MainBusErrors_Type()
)
fsp_II_2k_MainBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainBusErrors.setStatus("mandatory")


class _Fsp_II_2k_MainLastEvent_Type(Integer32):
    """Custom type fsp_II_2k_MainLastEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp_II_2k_MainLastEvent_Type.__name__ = "Integer32"
_Fsp_II_2k_MainLastEvent_Object = MibScalar
fsp_II_2k_MainLastEvent = _Fsp_II_2k_MainLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 8),
    _Fsp_II_2k_MainLastEvent_Type()
)
fsp_II_2k_MainLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLastEvent.setStatus("mandatory")
_Fsp_II_2k_MainMotd_Type = DisplayString
_Fsp_II_2k_MainMotd_Object = MibScalar
fsp_II_2k_MainMotd = _Fsp_II_2k_MainMotd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 9),
    _Fsp_II_2k_MainMotd_Type()
)
fsp_II_2k_MainMotd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainMotd.setStatus("mandatory")
_Fsp_II_2k_MainTrapsinkTable_Object = MibTable
fsp_II_2k_MainTrapsinkTable = _Fsp_II_2k_MainTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fsp_II_2k_MainTrapsinkTable.setStatus("mandatory")
_Fsp_II_2k_MainTrapsinkEntry_Object = MibTableRow
fsp_II_2k_MainTrapsinkEntry = _Fsp_II_2k_MainTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1)
)
fsp_II_2k_MainTrapsinkEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_MainTrapsinkNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_MainTrapsinkEntry.setStatus("mandatory")


class _Fsp_II_2k_MainTrapsinkNumber_Type(Integer32):
    """Custom type fsp_II_2k_MainTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsp_II_2k_MainTrapsinkNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_MainTrapsinkNumber_Object = MibTableColumn
fsp_II_2k_MainTrapsinkNumber = _Fsp_II_2k_MainTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 1),
    _Fsp_II_2k_MainTrapsinkNumber_Type()
)
fsp_II_2k_MainTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainTrapsinkNumber.setStatus("mandatory")
_Fsp_II_2k_MainTrapsinkAddress_Type = DisplayString
_Fsp_II_2k_MainTrapsinkAddress_Object = MibTableColumn
fsp_II_2k_MainTrapsinkAddress = _Fsp_II_2k_MainTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 2),
    _Fsp_II_2k_MainTrapsinkAddress_Type()
)
fsp_II_2k_MainTrapsinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainTrapsinkAddress.setStatus("mandatory")
_Fsp_II_2k_MainTrapsinkCommunity_Type = DisplayString
_Fsp_II_2k_MainTrapsinkCommunity_Object = MibTableColumn
fsp_II_2k_MainTrapsinkCommunity = _Fsp_II_2k_MainTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 3),
    _Fsp_II_2k_MainTrapsinkCommunity_Type()
)
fsp_II_2k_MainTrapsinkCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainTrapsinkCommunity.setStatus("mandatory")


class _Fsp_II_2k_MainTrapsinkPriority_Type(Integer32):
    """Custom type fsp_II_2k_MainTrapsinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Fsp_II_2k_MainTrapsinkPriority_Type.__name__ = "Integer32"
_Fsp_II_2k_MainTrapsinkPriority_Object = MibTableColumn
fsp_II_2k_MainTrapsinkPriority = _Fsp_II_2k_MainTrapsinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 4),
    _Fsp_II_2k_MainTrapsinkPriority_Type()
)
fsp_II_2k_MainTrapsinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainTrapsinkPriority.setStatus("mandatory")
_Fsp_II_2k_MainLogfileTable_Object = MibTable
fsp_II_2k_MainLogfileTable = _Fsp_II_2k_MainLogfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    fsp_II_2k_MainLogfileTable.setStatus("mandatory")
_Fsp_II_2k_MainLogfileEntry_Object = MibTableRow
fsp_II_2k_MainLogfileEntry = _Fsp_II_2k_MainLogfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1)
)
fsp_II_2k_MainLogfileEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_MainLogfileNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_MainLogfileEntry.setStatus("mandatory")


class _Fsp_II_2k_MainLogfileNumber_Type(Integer32):
    """Custom type fsp_II_2k_MainLogfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Fsp_II_2k_MainLogfileNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_MainLogfileNumber_Object = MibTableColumn
fsp_II_2k_MainLogfileNumber = _Fsp_II_2k_MainLogfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 1),
    _Fsp_II_2k_MainLogfileNumber_Type()
)
fsp_II_2k_MainLogfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLogfileNumber.setStatus("mandatory")
_Fsp_II_2k_MainLogfileName_Type = DisplayString
_Fsp_II_2k_MainLogfileName_Object = MibTableColumn
fsp_II_2k_MainLogfileName = _Fsp_II_2k_MainLogfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 2),
    _Fsp_II_2k_MainLogfileName_Type()
)
fsp_II_2k_MainLogfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLogfileName.setStatus("mandatory")
_Fsp_II_2k_MainLogfileSize_Type = Integer32
_Fsp_II_2k_MainLogfileSize_Object = MibTableColumn
fsp_II_2k_MainLogfileSize = _Fsp_II_2k_MainLogfileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 3),
    _Fsp_II_2k_MainLogfileSize_Type()
)
fsp_II_2k_MainLogfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLogfileSize.setStatus("mandatory")


class _Fsp_II_2k_MainLogfilePriority_Type(Integer32):
    """Custom type fsp_II_2k_MainLogfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Fsp_II_2k_MainLogfilePriority_Type.__name__ = "Integer32"
_Fsp_II_2k_MainLogfilePriority_Object = MibTableColumn
fsp_II_2k_MainLogfilePriority = _Fsp_II_2k_MainLogfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 4),
    _Fsp_II_2k_MainLogfilePriority_Type()
)
fsp_II_2k_MainLogfilePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLogfilePriority.setStatus("mandatory")


class _Fsp_II_2k_MainProtocolVersion_Type(Integer32):
    """Custom type fsp_II_2k_MainProtocolVersion based on Integer32"""
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


_Fsp_II_2k_MainProtocolVersion_Type.__name__ = "Integer32"
_Fsp_II_2k_MainProtocolVersion_Object = MibScalar
fsp_II_2k_MainProtocolVersion = _Fsp_II_2k_MainProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 12),
    _Fsp_II_2k_MainProtocolVersion_Type()
)
fsp_II_2k_MainProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainProtocolVersion.setStatus("mandatory")


class _Fsp_II_2k_MainSystemVersion_Type(Integer32):
    """Custom type fsp_II_2k_MainSystemVersion based on Integer32"""
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
          ("fsp1", 2),
          ("fsp2", 3),
          ("fsp2000", 4))
    )


_Fsp_II_2k_MainSystemVersion_Type.__name__ = "Integer32"
_Fsp_II_2k_MainSystemVersion_Object = MibScalar
fsp_II_2k_MainSystemVersion = _Fsp_II_2k_MainSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 13),
    _Fsp_II_2k_MainSystemVersion_Type()
)
fsp_II_2k_MainSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainSystemVersion.setStatus("mandatory")
_Fsp_II_2k_MainConfigMismatch_Type = Integer32
_Fsp_II_2k_MainConfigMismatch_Object = MibScalar
fsp_II_2k_MainConfigMismatch = _Fsp_II_2k_MainConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 14),
    _Fsp_II_2k_MainConfigMismatch_Type()
)
fsp_II_2k_MainConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainConfigMismatch.setStatus("mandatory")


class _Fsp_II_2k_MainLastAuthFailSource_Type(Integer32):
    """Custom type fsp_II_2k_MainLastAuthFailSource based on Integer32"""
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


_Fsp_II_2k_MainLastAuthFailSource_Type.__name__ = "Integer32"
_Fsp_II_2k_MainLastAuthFailSource_Object = MibScalar
fsp_II_2k_MainLastAuthFailSource = _Fsp_II_2k_MainLastAuthFailSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 15),
    _Fsp_II_2k_MainLastAuthFailSource_Type()
)
fsp_II_2k_MainLastAuthFailSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLastAuthFailSource.setStatus("mandatory")
_Fsp_II_2k_MainLastAuthFailDescription_Type = DisplayString
_Fsp_II_2k_MainLastAuthFailDescription_Object = MibScalar
fsp_II_2k_MainLastAuthFailDescription = _Fsp_II_2k_MainLastAuthFailDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 16),
    _Fsp_II_2k_MainLastAuthFailDescription_Type()
)
fsp_II_2k_MainLastAuthFailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLastAuthFailDescription.setStatus("mandatory")
_Fsp_II_2k_SlotTable_Object = MibTable
fsp_II_2k_SlotTable = _Fsp_II_2k_SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fsp_II_2k_SlotTable.setStatus("mandatory")
_Fsp_II_2k_SlotEntry_Object = MibTableRow
fsp_II_2k_SlotEntry = _Fsp_II_2k_SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1)
)
fsp_II_2k_SlotEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_SlotEntry.setStatus("mandatory")
_Fsp_II_2k_SlotNumber_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_SlotNumber_Object = MibTableColumn
fsp_II_2k_SlotNumber = _Fsp_II_2k_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 1),
    _Fsp_II_2k_SlotNumber_Type()
)
fsp_II_2k_SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SlotNumber.setStatus("mandatory")
_Fsp_II_2k_Type_Type = DisplayString
_Fsp_II_2k_Type_Object = MibTableColumn
fsp_II_2k_Type = _Fsp_II_2k_Type_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 2),
    _Fsp_II_2k_Type_Type()
)
fsp_II_2k_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_Type.setStatus("mandatory")


class _Fsp_II_2k_SlotTypeNumber_Type(Integer32):
    """Custom type fsp_II_2k_SlotTypeNumber based on Integer32"""
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
          ("fsp_II_2k_Converter", 1),
          ("fsp_I_Converter", 2),
          ("fsp_I_EthernetConverter", 3),
          ("fsp_II_2k_2_5GBitConverter", 5),
          ("fsp_II_2k_TRL_Converter", 7),
          ("fsp_II_2k_4PortTDMCard", 10),
          ("fsp_II_2k_HotStandby_Converter", 13),
          ("fsp_II_2k_4PortTDMCard_MC", 14),
          ("fsp_II_2k_8PortTDMCard_MC", 20),
          ("nemi", 32),
          ("demi", 33),
          ("fsp_II_2k_EthernetHubCard", 39),
          ("switch", 64),
          ("fsp_II_2k_RSM_OSC", 66),
          ("fsp_II_2k_RSM", 67),
          ("fsp_II_2k_OSC_single", 68),
          ("fsp_II_2k_SingleFiberSwitch", 69),
          ("fsp_II_2k_MUX_DMX", 136),
          ("fsp_II_2k_MUX", 137),
          ("fsp_II_2k_DMX", 138),
          ("fsp_II_2k_BSM", 139),
          ("other", 255))
    )


_Fsp_II_2k_SlotTypeNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_SlotTypeNumber_Object = MibTableColumn
fsp_II_2k_SlotTypeNumber = _Fsp_II_2k_SlotTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 3),
    _Fsp_II_2k_SlotTypeNumber_Type()
)
fsp_II_2k_SlotTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SlotTypeNumber.setStatus("mandatory")
_Fsp_II_2k_SerialNumber_Type = DisplayString
_Fsp_II_2k_SerialNumber_Object = MibTableColumn
fsp_II_2k_SerialNumber = _Fsp_II_2k_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 4),
    _Fsp_II_2k_SerialNumber_Type()
)
fsp_II_2k_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SerialNumber.setStatus("mandatory")
_Fsp_II_2k_HardwareVersion_Type = DisplayString
_Fsp_II_2k_HardwareVersion_Object = MibTableColumn
fsp_II_2k_HardwareVersion = _Fsp_II_2k_HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 5),
    _Fsp_II_2k_HardwareVersion_Type()
)
fsp_II_2k_HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_HardwareVersion.setStatus("mandatory")
_Fsp_II_2k_SoftwareVersion_Type = DisplayString
_Fsp_II_2k_SoftwareVersion_Object = MibTableColumn
fsp_II_2k_SoftwareVersion = _Fsp_II_2k_SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 6),
    _Fsp_II_2k_SoftwareVersion_Type()
)
fsp_II_2k_SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SoftwareVersion.setStatus("mandatory")
_Fsp_II_2k_Temperature_Type = Integer32
_Fsp_II_2k_Temperature_Object = MibTableColumn
fsp_II_2k_Temperature = _Fsp_II_2k_Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 7),
    _Fsp_II_2k_Temperature_Type()
)
fsp_II_2k_Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_Temperature.setStatus("mandatory")
_Fsp_II_2k_BoardVoltage_Type = Integer32
_Fsp_II_2k_BoardVoltage_Object = MibTableColumn
fsp_II_2k_BoardVoltage = _Fsp_II_2k_BoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 8),
    _Fsp_II_2k_BoardVoltage_Type()
)
fsp_II_2k_BoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_BoardVoltage.setStatus("mandatory")
_Fsp_II_2k_DetailInfo_Type = ObjectIdentifier
_Fsp_II_2k_DetailInfo_Object = MibTableColumn
fsp_II_2k_DetailInfo = _Fsp_II_2k_DetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 9),
    _Fsp_II_2k_DetailInfo_Type()
)
fsp_II_2k_DetailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_DetailInfo.setStatus("mandatory")


class _Fsp_II_2k_EPLDVersion_Type(Integer32):
    """Custom type fsp_II_2k_EPLDVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsp_II_2k_EPLDVersion_Type.__name__ = "Integer32"
_Fsp_II_2k_EPLDVersion_Object = MibTableColumn
fsp_II_2k_EPLDVersion = _Fsp_II_2k_EPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 10),
    _Fsp_II_2k_EPLDVersion_Type()
)
fsp_II_2k_EPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EPLDVersion.setStatus("mandatory")
_Fsp_II_2k_CustomerLabel_Type = DisplayString
_Fsp_II_2k_CustomerLabel_Object = MibTableColumn
fsp_II_2k_CustomerLabel = _Fsp_II_2k_CustomerLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 11),
    _Fsp_II_2k_CustomerLabel_Type()
)
fsp_II_2k_CustomerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_CustomerLabel.setStatus("mandatory")
_Fsp_II_2k_ProductionVersion_Type = DisplayString
_Fsp_II_2k_ProductionVersion_Object = MibTableColumn
fsp_II_2k_ProductionVersion = _Fsp_II_2k_ProductionVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 12),
    _Fsp_II_2k_ProductionVersion_Type()
)
fsp_II_2k_ProductionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ProductionVersion.setStatus("mandatory")


class _Fsp_II_2k_SlotSubType_Type(Integer32):
    """Custom type fsp_II_2k_SlotSubType based on Integer32"""
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


_Fsp_II_2k_SlotSubType_Type.__name__ = "Integer32"
_Fsp_II_2k_SlotSubType_Object = MibTableColumn
fsp_II_2k_SlotSubType = _Fsp_II_2k_SlotSubType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 13),
    _Fsp_II_2k_SlotSubType_Type()
)
fsp_II_2k_SlotSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SlotSubType.setStatus("mandatory")
_Fsp_II_2k_SlotAlias_Type = DisplayString
_Fsp_II_2k_SlotAlias_Object = MibTableColumn
fsp_II_2k_SlotAlias = _Fsp_II_2k_SlotAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 14),
    _Fsp_II_2k_SlotAlias_Type()
)
fsp_II_2k_SlotAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SlotAlias.setStatus("mandatory")
_Fsp_II_2k_SlotComment_Type = DisplayString
_Fsp_II_2k_SlotComment_Object = MibTableColumn
fsp_II_2k_SlotComment = _Fsp_II_2k_SlotComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 15),
    _Fsp_II_2k_SlotComment_Type()
)
fsp_II_2k_SlotComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SlotComment.setStatus("mandatory")
_Fsp_II_2k_PSTable_Object = MibTable
fsp_II_2k_PSTable = _Fsp_II_2k_PSTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    fsp_II_2k_PSTable.setStatus("mandatory")
_Fsp_II_2k_PSEntry_Object = MibTableRow
fsp_II_2k_PSEntry = _Fsp_II_2k_PSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1)
)
fsp_II_2k_PSEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_PSNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_PSEntry.setStatus("mandatory")


class _Fsp_II_2k_PSNumber_Type(Integer32):
    """Custom type fsp_II_2k_PSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsp_II_2k_PSNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_PSNumber_Object = MibTableColumn
fsp_II_2k_PSNumber = _Fsp_II_2k_PSNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 1),
    _Fsp_II_2k_PSNumber_Type()
)
fsp_II_2k_PSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_PSNumber.setStatus("mandatory")


class _Fsp_II_2k_PSOn_Type(Integer32):
    """Custom type fsp_II_2k_PSOn based on Integer32"""
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


_Fsp_II_2k_PSOn_Type.__name__ = "Integer32"
_Fsp_II_2k_PSOn_Object = MibTableColumn
fsp_II_2k_PSOn = _Fsp_II_2k_PSOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 2),
    _Fsp_II_2k_PSOn_Type()
)
fsp_II_2k_PSOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_PSOn.setStatus("mandatory")
_Fsp_II_2k_FanTable_Object = MibTable
fsp_II_2k_FanTable = _Fsp_II_2k_FanTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    fsp_II_2k_FanTable.setStatus("mandatory")
_Fsp_II_2k_FanEntry_Object = MibTableRow
fsp_II_2k_FanEntry = _Fsp_II_2k_FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1)
)
fsp_II_2k_FanEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_FanNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_FanEntry.setStatus("mandatory")


class _Fsp_II_2k_FanNumber_Type(Integer32):
    """Custom type fsp_II_2k_FanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Fsp_II_2k_FanNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_FanNumber_Object = MibTableColumn
fsp_II_2k_FanNumber = _Fsp_II_2k_FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 1),
    _Fsp_II_2k_FanNumber_Type()
)
fsp_II_2k_FanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_FanNumber.setStatus("mandatory")


class _Fsp_II_2k_FanOn_Type(Integer32):
    """Custom type fsp_II_2k_FanOn based on Integer32"""
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


_Fsp_II_2k_FanOn_Type.__name__ = "Integer32"
_Fsp_II_2k_FanOn_Object = MibTableColumn
fsp_II_2k_FanOn = _Fsp_II_2k_FanOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 2),
    _Fsp_II_2k_FanOn_Type()
)
fsp_II_2k_FanOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_FanOn.setStatus("mandatory")
_Fsp_II_2k_Converter_ObjectIdentity = ObjectIdentity
fsp_II_2k_Converter = _Fsp_II_2k_Converter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5)
)
_Fsp_II_2k_ConverterTable_Object = MibTable
fsp_II_2k_ConverterTable = _Fsp_II_2k_ConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_ConverterTable.setStatus("mandatory")
_Fsp_II_2k_ConverterEntry_Object = MibTableRow
fsp_II_2k_ConverterEntry = _Fsp_II_2k_ConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1)
)
fsp_II_2k_ConverterEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_ConverterNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_ConverterEntry.setStatus("mandatory")
_Fsp_II_2k_ConverterNumber_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_ConverterNumber_Object = MibTableColumn
fsp_II_2k_ConverterNumber = _Fsp_II_2k_ConverterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 1),
    _Fsp_II_2k_ConverterNumber_Type()
)
fsp_II_2k_ConverterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ConverterNumber.setStatus("mandatory")


class _Fsp_II_2k_RxLoc_Type(Integer32):
    """Custom type fsp_II_2k_RxLoc based on Integer32"""
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


_Fsp_II_2k_RxLoc_Type.__name__ = "Integer32"
_Fsp_II_2k_RxLoc_Object = MibTableColumn
fsp_II_2k_RxLoc = _Fsp_II_2k_RxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 2),
    _Fsp_II_2k_RxLoc_Type()
)
fsp_II_2k_RxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RxLoc.setStatus("mandatory")


class _Fsp_II_2k_TxLoc_Type(Integer32):
    """Custom type fsp_II_2k_TxLoc based on Integer32"""
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


_Fsp_II_2k_TxLoc_Type.__name__ = "Integer32"
_Fsp_II_2k_TxLoc_Object = MibTableColumn
fsp_II_2k_TxLoc = _Fsp_II_2k_TxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 3),
    _Fsp_II_2k_TxLoc_Type()
)
fsp_II_2k_TxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TxLoc.setStatus("mandatory")


class _Fsp_II_2k_TxLocC_Type(Integer32):
    """Custom type fsp_II_2k_TxLocC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fsp_II_2k_TxLocC_Type.__name__ = "Integer32"
_Fsp_II_2k_TxLocC_Object = MibTableColumn
fsp_II_2k_TxLocC = _Fsp_II_2k_TxLocC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 4),
    _Fsp_II_2k_TxLocC_Type()
)
fsp_II_2k_TxLocC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TxLocC.setStatus("mandatory")


class _Fsp_II_2k_TxLocTemp_Type(Integer32):
    """Custom type fsp_II_2k_TxLocTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Fsp_II_2k_TxLocTemp_Type.__name__ = "Integer32"
_Fsp_II_2k_TxLocTemp_Object = MibTableColumn
fsp_II_2k_TxLocTemp = _Fsp_II_2k_TxLocTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 5),
    _Fsp_II_2k_TxLocTemp_Type()
)
fsp_II_2k_TxLocTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TxLocTemp.setStatus("mandatory")


class _Fsp_II_2k_RxRem_Type(Integer32):
    """Custom type fsp_II_2k_RxRem based on Integer32"""
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


_Fsp_II_2k_RxRem_Type.__name__ = "Integer32"
_Fsp_II_2k_RxRem_Object = MibTableColumn
fsp_II_2k_RxRem = _Fsp_II_2k_RxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 6),
    _Fsp_II_2k_RxRem_Type()
)
fsp_II_2k_RxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RxRem.setStatus("mandatory")


class _Fsp_II_2k_TxRem_Type(Integer32):
    """Custom type fsp_II_2k_TxRem based on Integer32"""
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


_Fsp_II_2k_TxRem_Type.__name__ = "Integer32"
_Fsp_II_2k_TxRem_Object = MibTableColumn
fsp_II_2k_TxRem = _Fsp_II_2k_TxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 7),
    _Fsp_II_2k_TxRem_Type()
)
fsp_II_2k_TxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TxRem.setStatus("mandatory")


class _Fsp_II_2k_TxRemC_Type(Integer32):
    """Custom type fsp_II_2k_TxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fsp_II_2k_TxRemC_Type.__name__ = "Integer32"
_Fsp_II_2k_TxRemC_Object = MibTableColumn
fsp_II_2k_TxRemC = _Fsp_II_2k_TxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 8),
    _Fsp_II_2k_TxRemC_Type()
)
fsp_II_2k_TxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TxRemC.setStatus("mandatory")


class _Fsp_II_2k_TxRemTemp_Type(Integer32):
    """Custom type fsp_II_2k_TxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Fsp_II_2k_TxRemTemp_Type.__name__ = "Integer32"
_Fsp_II_2k_TxRemTemp_Object = MibTableColumn
fsp_II_2k_TxRemTemp = _Fsp_II_2k_TxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 9),
    _Fsp_II_2k_TxRemTemp_Type()
)
fsp_II_2k_TxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TxRemTemp.setStatus("mandatory")


class _Fsp_II_2k_RxRem2_Type(Integer32):
    """Custom type fsp_II_2k_RxRem2 based on Integer32"""
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


_Fsp_II_2k_RxRem2_Type.__name__ = "Integer32"
_Fsp_II_2k_RxRem2_Object = MibTableColumn
fsp_II_2k_RxRem2 = _Fsp_II_2k_RxRem2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 10),
    _Fsp_II_2k_RxRem2_Type()
)
fsp_II_2k_RxRem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RxRem2.setStatus("mandatory")


class _Fsp_II_2k_ClockState_Type(Integer32):
    """Custom type fsp_II_2k_ClockState based on Integer32"""
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


_Fsp_II_2k_ClockState_Type.__name__ = "Integer32"
_Fsp_II_2k_ClockState_Object = MibTableColumn
fsp_II_2k_ClockState = _Fsp_II_2k_ClockState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 11),
    _Fsp_II_2k_ClockState_Type()
)
fsp_II_2k_ClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ClockState.setStatus("mandatory")
_Fsp_II_2k_ClockFreq_Type = Integer32
_Fsp_II_2k_ClockFreq_Object = MibTableColumn
fsp_II_2k_ClockFreq = _Fsp_II_2k_ClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 12),
    _Fsp_II_2k_ClockFreq_Type()
)
fsp_II_2k_ClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ClockFreq.setStatus("mandatory")


class _Fsp_II_2k_LocLoop_Type(Integer32):
    """Custom type fsp_II_2k_LocLoop based on Integer32"""
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


_Fsp_II_2k_LocLoop_Type.__name__ = "Integer32"
_Fsp_II_2k_LocLoop_Object = MibTableColumn
fsp_II_2k_LocLoop = _Fsp_II_2k_LocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 13),
    _Fsp_II_2k_LocLoop_Type()
)
fsp_II_2k_LocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_LocLoop.setStatus("mandatory")


class _Fsp_II_2k_RemLoop_Type(Integer32):
    """Custom type fsp_II_2k_RemLoop based on Integer32"""
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


_Fsp_II_2k_RemLoop_Type.__name__ = "Integer32"
_Fsp_II_2k_RemLoop_Object = MibTableColumn
fsp_II_2k_RemLoop = _Fsp_II_2k_RemLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 14),
    _Fsp_II_2k_RemLoop_Type()
)
fsp_II_2k_RemLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RemLoop.setStatus("mandatory")


class _Fsp_II_2k_ClockType_Type(Integer32):
    """Custom type fsp_II_2k_ClockType based on Integer32"""
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


_Fsp_II_2k_ClockType_Type.__name__ = "Integer32"
_Fsp_II_2k_ClockType_Object = MibTableColumn
fsp_II_2k_ClockType = _Fsp_II_2k_ClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 15),
    _Fsp_II_2k_ClockType_Type()
)
fsp_II_2k_ClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ClockType.setStatus("mandatory")


class _Fsp_II_2k_HotStandby_ActiveLine_Type(Integer32):
    """Custom type fsp_II_2k_HotStandby_ActiveLine based on Integer32"""
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


_Fsp_II_2k_HotStandby_ActiveLine_Type.__name__ = "Integer32"
_Fsp_II_2k_HotStandby_ActiveLine_Object = MibTableColumn
fsp_II_2k_HotStandby_ActiveLine = _Fsp_II_2k_HotStandby_ActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 16),
    _Fsp_II_2k_HotStandby_ActiveLine_Type()
)
fsp_II_2k_HotStandby_ActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_ActiveLine.setStatus("mandatory")


class _Fsp_II_2k_HotStandby_LineLocked_Type(Integer32):
    """Custom type fsp_II_2k_HotStandby_LineLocked based on Integer32"""
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


_Fsp_II_2k_HotStandby_LineLocked_Type.__name__ = "Integer32"
_Fsp_II_2k_HotStandby_LineLocked_Object = MibTableColumn
fsp_II_2k_HotStandby_LineLocked = _Fsp_II_2k_HotStandby_LineLocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 17),
    _Fsp_II_2k_HotStandby_LineLocked_Type()
)
fsp_II_2k_HotStandby_LineLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_LineLocked.setStatus("mandatory")
_Fsp_II_2k_LocalConnector_Type = DisplayString
_Fsp_II_2k_LocalConnector_Object = MibTableColumn
fsp_II_2k_LocalConnector = _Fsp_II_2k_LocalConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 18),
    _Fsp_II_2k_LocalConnector_Type()
)
fsp_II_2k_LocalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_LocalConnector.setStatus("mandatory")
_Fsp_II_2k_LocalLaserType_Type = DisplayString
_Fsp_II_2k_LocalLaserType_Object = MibTableColumn
fsp_II_2k_LocalLaserType = _Fsp_II_2k_LocalLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 19),
    _Fsp_II_2k_LocalLaserType_Type()
)
fsp_II_2k_LocalLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_LocalLaserType.setStatus("mandatory")
_Fsp_II_2k_RemoteConnector_Type = DisplayString
_Fsp_II_2k_RemoteConnector_Object = MibTableColumn
fsp_II_2k_RemoteConnector = _Fsp_II_2k_RemoteConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 20),
    _Fsp_II_2k_RemoteConnector_Type()
)
fsp_II_2k_RemoteConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteConnector.setStatus("mandatory")
_Fsp_II_2k_RemoteLaserType_Type = DisplayString
_Fsp_II_2k_RemoteLaserType_Object = MibTableColumn
fsp_II_2k_RemoteLaserType = _Fsp_II_2k_RemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 21),
    _Fsp_II_2k_RemoteLaserType_Type()
)
fsp_II_2k_RemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteLaserType.setStatus("mandatory")
_Fsp_II_2k_ConverterType_Type = DisplayString
_Fsp_II_2k_ConverterType_Object = MibTableColumn
fsp_II_2k_ConverterType = _Fsp_II_2k_ConverterType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 22),
    _Fsp_II_2k_ConverterType_Type()
)
fsp_II_2k_ConverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ConverterType.setStatus("mandatory")
_Fsp_II_2k_ClockRecovery_Type = DisplayString
_Fsp_II_2k_ClockRecovery_Object = MibTableColumn
fsp_II_2k_ClockRecovery = _Fsp_II_2k_ClockRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 23),
    _Fsp_II_2k_ClockRecovery_Type()
)
fsp_II_2k_ClockRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ClockRecovery.setStatus("mandatory")
_Fsp_II_2k_SupportedDataRateTransparent_Type = DisplayString
_Fsp_II_2k_SupportedDataRateTransparent_Object = MibTableColumn
fsp_II_2k_SupportedDataRateTransparent = _Fsp_II_2k_SupportedDataRateTransparent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 24),
    _Fsp_II_2k_SupportedDataRateTransparent_Type()
)
fsp_II_2k_SupportedDataRateTransparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SupportedDataRateTransparent.setStatus("mandatory")
_Fsp_II_2k_SupportedDataRateClocked_Type = DisplayString
_Fsp_II_2k_SupportedDataRateClocked_Object = MibTableColumn
fsp_II_2k_SupportedDataRateClocked = _Fsp_II_2k_SupportedDataRateClocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 25),
    _Fsp_II_2k_SupportedDataRateClocked_Type()
)
fsp_II_2k_SupportedDataRateClocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SupportedDataRateClocked.setStatus("mandatory")


class _Fsp_II_2k_ChannelNumber_Type(Integer32):
    """Custom type fsp_II_2k_ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsp_II_2k_ChannelNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_ChannelNumber_Object = MibTableColumn
fsp_II_2k_ChannelNumber = _Fsp_II_2k_ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 26),
    _Fsp_II_2k_ChannelNumber_Type()
)
fsp_II_2k_ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ChannelNumber.setStatus("mandatory")


class _Fsp_II_2k_RemoteClockState_Type(Integer32):
    """Custom type fsp_II_2k_RemoteClockState based on Integer32"""
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


_Fsp_II_2k_RemoteClockState_Type.__name__ = "Integer32"
_Fsp_II_2k_RemoteClockState_Object = MibTableColumn
fsp_II_2k_RemoteClockState = _Fsp_II_2k_RemoteClockState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 27),
    _Fsp_II_2k_RemoteClockState_Type()
)
fsp_II_2k_RemoteClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClockState.setStatus("mandatory")


class _Fsp_II_2k_RemoteClockState2_Type(Integer32):
    """Custom type fsp_II_2k_RemoteClockState2 based on Integer32"""
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


_Fsp_II_2k_RemoteClockState2_Type.__name__ = "Integer32"
_Fsp_II_2k_RemoteClockState2_Object = MibTableColumn
fsp_II_2k_RemoteClockState2 = _Fsp_II_2k_RemoteClockState2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 28),
    _Fsp_II_2k_RemoteClockState2_Type()
)
fsp_II_2k_RemoteClockState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClockState2.setStatus("mandatory")


class _Fsp_II_2k_RegeneratorMode_Type(Integer32):
    """Custom type fsp_II_2k_RegeneratorMode based on Integer32"""
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


_Fsp_II_2k_RegeneratorMode_Type.__name__ = "Integer32"
_Fsp_II_2k_RegeneratorMode_Object = MibTableColumn
fsp_II_2k_RegeneratorMode = _Fsp_II_2k_RegeneratorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 29),
    _Fsp_II_2k_RegeneratorMode_Type()
)
fsp_II_2k_RegeneratorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RegeneratorMode.setStatus("mandatory")
_Fsp_II_2k_Switch_ObjectIdentity = ObjectIdentity
fsp_II_2k_Switch = _Fsp_II_2k_Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10)
)
_Fsp_II_2k_SwitchTable_Object = MibTable
fsp_II_2k_SwitchTable = _Fsp_II_2k_SwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchTable.setStatus("mandatory")
_Fsp_II_2k_SwitchEntry_Object = MibTableRow
fsp_II_2k_SwitchEntry = _Fsp_II_2k_SwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1)
)
fsp_II_2k_SwitchEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SwitchNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchEntry.setStatus("mandatory")
_Fsp_II_2k_SwitchNumber_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_SwitchNumber_Object = MibTableColumn
fsp_II_2k_SwitchNumber = _Fsp_II_2k_SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 1),
    _Fsp_II_2k_SwitchNumber_Type()
)
fsp_II_2k_SwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchNumber.setStatus("mandatory")


class _Fsp_II_2k_SwitchLine_Type(Integer32):
    """Custom type fsp_II_2k_SwitchLine based on Integer32"""
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


_Fsp_II_2k_SwitchLine_Type.__name__ = "Integer32"
_Fsp_II_2k_SwitchLine_Object = MibTableColumn
fsp_II_2k_SwitchLine = _Fsp_II_2k_SwitchLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 2),
    _Fsp_II_2k_SwitchLine_Type()
)
fsp_II_2k_SwitchLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchLine.setStatus("mandatory")


class _Fsp_II_2k_SwitchMode_Type(Integer32):
    """Custom type fsp_II_2k_SwitchMode based on Integer32"""
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


_Fsp_II_2k_SwitchMode_Type.__name__ = "Integer32"
_Fsp_II_2k_SwitchMode_Object = MibTableColumn
fsp_II_2k_SwitchMode = _Fsp_II_2k_SwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 3),
    _Fsp_II_2k_SwitchMode_Type()
)
fsp_II_2k_SwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchMode.setStatus("mandatory")


class _Fsp_II_2k_SwitchLaserOn_Type(Integer32):
    """Custom type fsp_II_2k_SwitchLaserOn based on Integer32"""
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


_Fsp_II_2k_SwitchLaserOn_Type.__name__ = "Integer32"
_Fsp_II_2k_SwitchLaserOn_Object = MibTableColumn
fsp_II_2k_SwitchLaserOn = _Fsp_II_2k_SwitchLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 4),
    _Fsp_II_2k_SwitchLaserOn_Type()
)
fsp_II_2k_SwitchLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchLaserOn.setStatus("mandatory")


class _Fsp_II_2k_SwitchLineAavail_Type(Integer32):
    """Custom type fsp_II_2k_SwitchLineAavail based on Integer32"""
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


_Fsp_II_2k_SwitchLineAavail_Type.__name__ = "Integer32"
_Fsp_II_2k_SwitchLineAavail_Object = MibTableColumn
fsp_II_2k_SwitchLineAavail = _Fsp_II_2k_SwitchLineAavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 5),
    _Fsp_II_2k_SwitchLineAavail_Type()
)
fsp_II_2k_SwitchLineAavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchLineAavail.setStatus("mandatory")


class _Fsp_II_2k_SwitchLineBavail_Type(Integer32):
    """Custom type fsp_II_2k_SwitchLineBavail based on Integer32"""
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


_Fsp_II_2k_SwitchLineBavail_Type.__name__ = "Integer32"
_Fsp_II_2k_SwitchLineBavail_Object = MibTableColumn
fsp_II_2k_SwitchLineBavail = _Fsp_II_2k_SwitchLineBavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 6),
    _Fsp_II_2k_SwitchLineBavail_Type()
)
fsp_II_2k_SwitchLineBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchLineBavail.setStatus("mandatory")


class _Fsp_II_2k_SwitchAutoLaserShutdown_Type(Integer32):
    """Custom type fsp_II_2k_SwitchAutoLaserShutdown based on Integer32"""
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


_Fsp_II_2k_SwitchAutoLaserShutdown_Type.__name__ = "Integer32"
_Fsp_II_2k_SwitchAutoLaserShutdown_Object = MibTableColumn
fsp_II_2k_SwitchAutoLaserShutdown = _Fsp_II_2k_SwitchAutoLaserShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 7),
    _Fsp_II_2k_SwitchAutoLaserShutdown_Type()
)
fsp_II_2k_SwitchAutoLaserShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchAutoLaserShutdown.setStatus("mandatory")
_Fsp_II_2k_SwitchConnector_Type = DisplayString
_Fsp_II_2k_SwitchConnector_Object = MibTableColumn
fsp_II_2k_SwitchConnector = _Fsp_II_2k_SwitchConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 10),
    _Fsp_II_2k_SwitchConnector_Type()
)
fsp_II_2k_SwitchConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchConnector.setStatus("mandatory")
_Fsp_II_2k_SwitchRemoteLaserType_Type = DisplayString
_Fsp_II_2k_SwitchRemoteLaserType_Object = MibTableColumn
fsp_II_2k_SwitchRemoteLaserType = _Fsp_II_2k_SwitchRemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 11),
    _Fsp_II_2k_SwitchRemoteLaserType_Type()
)
fsp_II_2k_SwitchRemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchRemoteLaserType.setStatus("mandatory")
_Fsp_II_2k_RSM_OSC_ObjectIdentity = ObjectIdentity
fsp_II_2k_RSM_OSC = _Fsp_II_2k_RSM_OSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11)
)
_Fsp_II_2k_RSM_Table_Object = MibTable
fsp_II_2k_RSM_Table = _Fsp_II_2k_RSM_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Table.setStatus("mandatory")
_Fsp_II_2k_RSM_Entry_Object = MibTableRow
fsp_II_2k_RSM_Entry = _Fsp_II_2k_RSM_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1)
)
fsp_II_2k_RSM_Entry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_RSM_Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Entry.setStatus("mandatory")
_Fsp_II_2k_RSM_Number_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_RSM_Number_Object = MibTableColumn
fsp_II_2k_RSM_Number = _Fsp_II_2k_RSM_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 1),
    _Fsp_II_2k_RSM_Number_Type()
)
fsp_II_2k_RSM_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Number.setStatus("mandatory")


class _Fsp_II_2k_RSM_Line_Type(Integer32):
    """Custom type fsp_II_2k_RSM_Line based on Integer32"""
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


_Fsp_II_2k_RSM_Line_Type.__name__ = "Integer32"
_Fsp_II_2k_RSM_Line_Object = MibTableColumn
fsp_II_2k_RSM_Line = _Fsp_II_2k_RSM_Line_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 2),
    _Fsp_II_2k_RSM_Line_Type()
)
fsp_II_2k_RSM_Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Line.setStatus("mandatory")


class _Fsp_II_2k_RSM_Mode_Type(Integer32):
    """Custom type fsp_II_2k_RSM_Mode based on Integer32"""
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


_Fsp_II_2k_RSM_Mode_Type.__name__ = "Integer32"
_Fsp_II_2k_RSM_Mode_Object = MibTableColumn
fsp_II_2k_RSM_Mode = _Fsp_II_2k_RSM_Mode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 3),
    _Fsp_II_2k_RSM_Mode_Type()
)
fsp_II_2k_RSM_Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Mode.setStatus("mandatory")


class _Fsp_II_2k_RSM_LaserOn_Type(Integer32):
    """Custom type fsp_II_2k_RSM_LaserOn based on Integer32"""
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


_Fsp_II_2k_RSM_LaserOn_Type.__name__ = "Integer32"
_Fsp_II_2k_RSM_LaserOn_Object = MibTableColumn
fsp_II_2k_RSM_LaserOn = _Fsp_II_2k_RSM_LaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 4),
    _Fsp_II_2k_RSM_LaserOn_Type()
)
fsp_II_2k_RSM_LaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_LaserOn.setStatus("mandatory")


class _Fsp_II_2k_RSM_LineAavail_Type(Integer32):
    """Custom type fsp_II_2k_RSM_LineAavail based on Integer32"""
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


_Fsp_II_2k_RSM_LineAavail_Type.__name__ = "Integer32"
_Fsp_II_2k_RSM_LineAavail_Object = MibTableColumn
fsp_II_2k_RSM_LineAavail = _Fsp_II_2k_RSM_LineAavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 5),
    _Fsp_II_2k_RSM_LineAavail_Type()
)
fsp_II_2k_RSM_LineAavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_LineAavail.setStatus("mandatory")


class _Fsp_II_2k_RSM_LineBavail_Type(Integer32):
    """Custom type fsp_II_2k_RSM_LineBavail based on Integer32"""
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


_Fsp_II_2k_RSM_LineBavail_Type.__name__ = "Integer32"
_Fsp_II_2k_RSM_LineBavail_Object = MibTableColumn
fsp_II_2k_RSM_LineBavail = _Fsp_II_2k_RSM_LineBavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 6),
    _Fsp_II_2k_RSM_LineBavail_Type()
)
fsp_II_2k_RSM_LineBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_LineBavail.setStatus("mandatory")


class _Fsp_II_2k_RSM_Control_Type(Integer32):
    """Custom type fsp_II_2k_RSM_Control based on Integer32"""
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


_Fsp_II_2k_RSM_Control_Type.__name__ = "Integer32"
_Fsp_II_2k_RSM_Control_Object = MibTableColumn
fsp_II_2k_RSM_Control = _Fsp_II_2k_RSM_Control_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 7),
    _Fsp_II_2k_RSM_Control_Type()
)
fsp_II_2k_RSM_Control.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Control.setStatus("mandatory")
_Fsp_II_2k_RSM_Connector_Type = DisplayString
_Fsp_II_2k_RSM_Connector_Object = MibTableColumn
fsp_II_2k_RSM_Connector = _Fsp_II_2k_RSM_Connector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 8),
    _Fsp_II_2k_RSM_Connector_Type()
)
fsp_II_2k_RSM_Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Connector.setStatus("mandatory")
_Fsp_II_2k_RSM_RemoteLaserType_Type = DisplayString
_Fsp_II_2k_RSM_RemoteLaserType_Object = MibTableColumn
fsp_II_2k_RSM_RemoteLaserType = _Fsp_II_2k_RSM_RemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 1, 1, 9),
    _Fsp_II_2k_RSM_RemoteLaserType_Type()
)
fsp_II_2k_RSM_RemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_RemoteLaserType.setStatus("mandatory")
_Fsp_II_2k_OSC_Table_Object = MibTable
fsp_II_2k_OSC_Table = _Fsp_II_2k_OSC_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2)
)
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_Table.setStatus("mandatory")
_Fsp_II_2k_OSC_Entry_Object = MibTableRow
fsp_II_2k_OSC_Entry = _Fsp_II_2k_OSC_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1)
)
fsp_II_2k_OSC_Entry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_OSC_Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_Entry.setStatus("mandatory")
_Fsp_II_2k_OSC_Number_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_OSC_Number_Object = MibTableColumn
fsp_II_2k_OSC_Number = _Fsp_II_2k_OSC_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 1),
    _Fsp_II_2k_OSC_Number_Type()
)
fsp_II_2k_OSC_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_Number.setStatus("mandatory")


class _Fsp_II_2k_OSC_LaserOn_Type(Integer32):
    """Custom type fsp_II_2k_OSC_LaserOn based on Integer32"""
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


_Fsp_II_2k_OSC_LaserOn_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_LaserOn_Object = MibTableColumn
fsp_II_2k_OSC_LaserOn = _Fsp_II_2k_OSC_LaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 2),
    _Fsp_II_2k_OSC_LaserOn_Type()
)
fsp_II_2k_OSC_LaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_LaserOn.setStatus("mandatory")


class _Fsp_II_2k_OSC_P1_fail_Type(Integer32):
    """Custom type fsp_II_2k_OSC_P1_fail based on Integer32"""
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


_Fsp_II_2k_OSC_P1_fail_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_P1_fail_Object = MibTableColumn
fsp_II_2k_OSC_P1_fail = _Fsp_II_2k_OSC_P1_fail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 3),
    _Fsp_II_2k_OSC_P1_fail_Type()
)
fsp_II_2k_OSC_P1_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_P1_fail.setStatus("mandatory")


class _Fsp_II_2k_OSC_P2_fail_Type(Integer32):
    """Custom type fsp_II_2k_OSC_P2_fail based on Integer32"""
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


_Fsp_II_2k_OSC_P2_fail_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_P2_fail_Object = MibTableColumn
fsp_II_2k_OSC_P2_fail = _Fsp_II_2k_OSC_P2_fail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 4),
    _Fsp_II_2k_OSC_P2_fail_Type()
)
fsp_II_2k_OSC_P2_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_P2_fail.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortEnable1_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortEnable1 based on Integer32"""
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


_Fsp_II_2k_OSC_PortEnable1_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortEnable1_Object = MibTableColumn
fsp_II_2k_OSC_PortEnable1 = _Fsp_II_2k_OSC_PortEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 10),
    _Fsp_II_2k_OSC_PortEnable1_Type()
)
fsp_II_2k_OSC_PortEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortEnable1.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortSpeed1_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortSpeed1 based on Integer32"""
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


_Fsp_II_2k_OSC_PortSpeed1_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortSpeed1_Object = MibTableColumn
fsp_II_2k_OSC_PortSpeed1 = _Fsp_II_2k_OSC_PortSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 11),
    _Fsp_II_2k_OSC_PortSpeed1_Type()
)
fsp_II_2k_OSC_PortSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortSpeed1.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortDuplex1_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortDuplex1 based on Integer32"""
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


_Fsp_II_2k_OSC_PortDuplex1_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortDuplex1_Object = MibTableColumn
fsp_II_2k_OSC_PortDuplex1 = _Fsp_II_2k_OSC_PortDuplex1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 12),
    _Fsp_II_2k_OSC_PortDuplex1_Type()
)
fsp_II_2k_OSC_PortDuplex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortDuplex1.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortAutoneg1_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortAutoneg1 based on Integer32"""
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


_Fsp_II_2k_OSC_PortAutoneg1_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortAutoneg1_Object = MibTableColumn
fsp_II_2k_OSC_PortAutoneg1 = _Fsp_II_2k_OSC_PortAutoneg1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 13),
    _Fsp_II_2k_OSC_PortAutoneg1_Type()
)
fsp_II_2k_OSC_PortAutoneg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortAutoneg1.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortPolarity1_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortPolarity1 based on Integer32"""
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


_Fsp_II_2k_OSC_PortPolarity1_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortPolarity1_Object = MibTableColumn
fsp_II_2k_OSC_PortPolarity1 = _Fsp_II_2k_OSC_PortPolarity1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 14),
    _Fsp_II_2k_OSC_PortPolarity1_Type()
)
fsp_II_2k_OSC_PortPolarity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortPolarity1.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortLinkStatus1_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortLinkStatus1 based on Integer32"""
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


_Fsp_II_2k_OSC_PortLinkStatus1_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortLinkStatus1_Object = MibTableColumn
fsp_II_2k_OSC_PortLinkStatus1 = _Fsp_II_2k_OSC_PortLinkStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 15),
    _Fsp_II_2k_OSC_PortLinkStatus1_Type()
)
fsp_II_2k_OSC_PortLinkStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortLinkStatus1.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortEnable2_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortEnable2 based on Integer32"""
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


_Fsp_II_2k_OSC_PortEnable2_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortEnable2_Object = MibTableColumn
fsp_II_2k_OSC_PortEnable2 = _Fsp_II_2k_OSC_PortEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 20),
    _Fsp_II_2k_OSC_PortEnable2_Type()
)
fsp_II_2k_OSC_PortEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortEnable2.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortSpeed2_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortSpeed2 based on Integer32"""
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


_Fsp_II_2k_OSC_PortSpeed2_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortSpeed2_Object = MibTableColumn
fsp_II_2k_OSC_PortSpeed2 = _Fsp_II_2k_OSC_PortSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 21),
    _Fsp_II_2k_OSC_PortSpeed2_Type()
)
fsp_II_2k_OSC_PortSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortSpeed2.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortDuplex2_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortDuplex2 based on Integer32"""
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


_Fsp_II_2k_OSC_PortDuplex2_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortDuplex2_Object = MibTableColumn
fsp_II_2k_OSC_PortDuplex2 = _Fsp_II_2k_OSC_PortDuplex2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 22),
    _Fsp_II_2k_OSC_PortDuplex2_Type()
)
fsp_II_2k_OSC_PortDuplex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortDuplex2.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortAutoneg2_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortAutoneg2 based on Integer32"""
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


_Fsp_II_2k_OSC_PortAutoneg2_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortAutoneg2_Object = MibTableColumn
fsp_II_2k_OSC_PortAutoneg2 = _Fsp_II_2k_OSC_PortAutoneg2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 23),
    _Fsp_II_2k_OSC_PortAutoneg2_Type()
)
fsp_II_2k_OSC_PortAutoneg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortAutoneg2.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortPolarity2_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortPolarity2 based on Integer32"""
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


_Fsp_II_2k_OSC_PortPolarity2_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortPolarity2_Object = MibTableColumn
fsp_II_2k_OSC_PortPolarity2 = _Fsp_II_2k_OSC_PortPolarity2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 24),
    _Fsp_II_2k_OSC_PortPolarity2_Type()
)
fsp_II_2k_OSC_PortPolarity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortPolarity2.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortLinkStatus2_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortLinkStatus2 based on Integer32"""
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


_Fsp_II_2k_OSC_PortLinkStatus2_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortLinkStatus2_Object = MibTableColumn
fsp_II_2k_OSC_PortLinkStatus2 = _Fsp_II_2k_OSC_PortLinkStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 25),
    _Fsp_II_2k_OSC_PortLinkStatus2_Type()
)
fsp_II_2k_OSC_PortLinkStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortLinkStatus2.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortEnable3_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortEnable3 based on Integer32"""
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


_Fsp_II_2k_OSC_PortEnable3_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortEnable3_Object = MibTableColumn
fsp_II_2k_OSC_PortEnable3 = _Fsp_II_2k_OSC_PortEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 30),
    _Fsp_II_2k_OSC_PortEnable3_Type()
)
fsp_II_2k_OSC_PortEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortEnable3.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortSpeed3_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortSpeed3 based on Integer32"""
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


_Fsp_II_2k_OSC_PortSpeed3_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortSpeed3_Object = MibTableColumn
fsp_II_2k_OSC_PortSpeed3 = _Fsp_II_2k_OSC_PortSpeed3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 31),
    _Fsp_II_2k_OSC_PortSpeed3_Type()
)
fsp_II_2k_OSC_PortSpeed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortSpeed3.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortDuplex3_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortDuplex3 based on Integer32"""
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


_Fsp_II_2k_OSC_PortDuplex3_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortDuplex3_Object = MibTableColumn
fsp_II_2k_OSC_PortDuplex3 = _Fsp_II_2k_OSC_PortDuplex3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 32),
    _Fsp_II_2k_OSC_PortDuplex3_Type()
)
fsp_II_2k_OSC_PortDuplex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortDuplex3.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortAutoneg3_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortAutoneg3 based on Integer32"""
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


_Fsp_II_2k_OSC_PortAutoneg3_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortAutoneg3_Object = MibTableColumn
fsp_II_2k_OSC_PortAutoneg3 = _Fsp_II_2k_OSC_PortAutoneg3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 33),
    _Fsp_II_2k_OSC_PortAutoneg3_Type()
)
fsp_II_2k_OSC_PortAutoneg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortAutoneg3.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortPolarity3_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortPolarity3 based on Integer32"""
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


_Fsp_II_2k_OSC_PortPolarity3_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortPolarity3_Object = MibTableColumn
fsp_II_2k_OSC_PortPolarity3 = _Fsp_II_2k_OSC_PortPolarity3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 34),
    _Fsp_II_2k_OSC_PortPolarity3_Type()
)
fsp_II_2k_OSC_PortPolarity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortPolarity3.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortLinkStatus3_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortLinkStatus3 based on Integer32"""
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


_Fsp_II_2k_OSC_PortLinkStatus3_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortLinkStatus3_Object = MibTableColumn
fsp_II_2k_OSC_PortLinkStatus3 = _Fsp_II_2k_OSC_PortLinkStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 35),
    _Fsp_II_2k_OSC_PortLinkStatus3_Type()
)
fsp_II_2k_OSC_PortLinkStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortLinkStatus3.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortEnable4_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortEnable4 based on Integer32"""
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


_Fsp_II_2k_OSC_PortEnable4_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortEnable4_Object = MibTableColumn
fsp_II_2k_OSC_PortEnable4 = _Fsp_II_2k_OSC_PortEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 40),
    _Fsp_II_2k_OSC_PortEnable4_Type()
)
fsp_II_2k_OSC_PortEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortEnable4.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortSpeed4_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortSpeed4 based on Integer32"""
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


_Fsp_II_2k_OSC_PortSpeed4_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortSpeed4_Object = MibTableColumn
fsp_II_2k_OSC_PortSpeed4 = _Fsp_II_2k_OSC_PortSpeed4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 41),
    _Fsp_II_2k_OSC_PortSpeed4_Type()
)
fsp_II_2k_OSC_PortSpeed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortSpeed4.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortDuplex4_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortDuplex4 based on Integer32"""
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


_Fsp_II_2k_OSC_PortDuplex4_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortDuplex4_Object = MibTableColumn
fsp_II_2k_OSC_PortDuplex4 = _Fsp_II_2k_OSC_PortDuplex4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 42),
    _Fsp_II_2k_OSC_PortDuplex4_Type()
)
fsp_II_2k_OSC_PortDuplex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortDuplex4.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortAutoneg4_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortAutoneg4 based on Integer32"""
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


_Fsp_II_2k_OSC_PortAutoneg4_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortAutoneg4_Object = MibTableColumn
fsp_II_2k_OSC_PortAutoneg4 = _Fsp_II_2k_OSC_PortAutoneg4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 43),
    _Fsp_II_2k_OSC_PortAutoneg4_Type()
)
fsp_II_2k_OSC_PortAutoneg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortAutoneg4.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortPolarity4_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortPolarity4 based on Integer32"""
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


_Fsp_II_2k_OSC_PortPolarity4_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortPolarity4_Object = MibTableColumn
fsp_II_2k_OSC_PortPolarity4 = _Fsp_II_2k_OSC_PortPolarity4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 44),
    _Fsp_II_2k_OSC_PortPolarity4_Type()
)
fsp_II_2k_OSC_PortPolarity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortPolarity4.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortLinkStatus4_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortLinkStatus4 based on Integer32"""
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


_Fsp_II_2k_OSC_PortLinkStatus4_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortLinkStatus4_Object = MibTableColumn
fsp_II_2k_OSC_PortLinkStatus4 = _Fsp_II_2k_OSC_PortLinkStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 45),
    _Fsp_II_2k_OSC_PortLinkStatus4_Type()
)
fsp_II_2k_OSC_PortLinkStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortLinkStatus4.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortEnable5_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortEnable5 based on Integer32"""
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


_Fsp_II_2k_OSC_PortEnable5_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortEnable5_Object = MibTableColumn
fsp_II_2k_OSC_PortEnable5 = _Fsp_II_2k_OSC_PortEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 50),
    _Fsp_II_2k_OSC_PortEnable5_Type()
)
fsp_II_2k_OSC_PortEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortEnable5.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortSpeed5_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortSpeed5 based on Integer32"""
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


_Fsp_II_2k_OSC_PortSpeed5_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortSpeed5_Object = MibTableColumn
fsp_II_2k_OSC_PortSpeed5 = _Fsp_II_2k_OSC_PortSpeed5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 51),
    _Fsp_II_2k_OSC_PortSpeed5_Type()
)
fsp_II_2k_OSC_PortSpeed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortSpeed5.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortDuplex5_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortDuplex5 based on Integer32"""
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


_Fsp_II_2k_OSC_PortDuplex5_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortDuplex5_Object = MibTableColumn
fsp_II_2k_OSC_PortDuplex5 = _Fsp_II_2k_OSC_PortDuplex5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 52),
    _Fsp_II_2k_OSC_PortDuplex5_Type()
)
fsp_II_2k_OSC_PortDuplex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortDuplex5.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortAutoneg5_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortAutoneg5 based on Integer32"""
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


_Fsp_II_2k_OSC_PortAutoneg5_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortAutoneg5_Object = MibTableColumn
fsp_II_2k_OSC_PortAutoneg5 = _Fsp_II_2k_OSC_PortAutoneg5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 53),
    _Fsp_II_2k_OSC_PortAutoneg5_Type()
)
fsp_II_2k_OSC_PortAutoneg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortAutoneg5.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortPolarity5_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortPolarity5 based on Integer32"""
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


_Fsp_II_2k_OSC_PortPolarity5_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortPolarity5_Object = MibTableColumn
fsp_II_2k_OSC_PortPolarity5 = _Fsp_II_2k_OSC_PortPolarity5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 54),
    _Fsp_II_2k_OSC_PortPolarity5_Type()
)
fsp_II_2k_OSC_PortPolarity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortPolarity5.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortLinkStatus5_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortLinkStatus5 based on Integer32"""
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


_Fsp_II_2k_OSC_PortLinkStatus5_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortLinkStatus5_Object = MibTableColumn
fsp_II_2k_OSC_PortLinkStatus5 = _Fsp_II_2k_OSC_PortLinkStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 55),
    _Fsp_II_2k_OSC_PortLinkStatus5_Type()
)
fsp_II_2k_OSC_PortLinkStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortLinkStatus5.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortEnable6_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortEnable6 based on Integer32"""
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


_Fsp_II_2k_OSC_PortEnable6_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortEnable6_Object = MibTableColumn
fsp_II_2k_OSC_PortEnable6 = _Fsp_II_2k_OSC_PortEnable6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 60),
    _Fsp_II_2k_OSC_PortEnable6_Type()
)
fsp_II_2k_OSC_PortEnable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortEnable6.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortSpeed6_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortSpeed6 based on Integer32"""
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


_Fsp_II_2k_OSC_PortSpeed6_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortSpeed6_Object = MibTableColumn
fsp_II_2k_OSC_PortSpeed6 = _Fsp_II_2k_OSC_PortSpeed6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 61),
    _Fsp_II_2k_OSC_PortSpeed6_Type()
)
fsp_II_2k_OSC_PortSpeed6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortSpeed6.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortDuplex6_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortDuplex6 based on Integer32"""
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


_Fsp_II_2k_OSC_PortDuplex6_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortDuplex6_Object = MibTableColumn
fsp_II_2k_OSC_PortDuplex6 = _Fsp_II_2k_OSC_PortDuplex6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 62),
    _Fsp_II_2k_OSC_PortDuplex6_Type()
)
fsp_II_2k_OSC_PortDuplex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortDuplex6.setStatus("mandatory")


class _Fsp_II_2k_OSC_PortLinkStatus6_Type(Integer32):
    """Custom type fsp_II_2k_OSC_PortLinkStatus6 based on Integer32"""
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


_Fsp_II_2k_OSC_PortLinkStatus6_Type.__name__ = "Integer32"
_Fsp_II_2k_OSC_PortLinkStatus6_Object = MibTableColumn
fsp_II_2k_OSC_PortLinkStatus6 = _Fsp_II_2k_OSC_PortLinkStatus6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 65),
    _Fsp_II_2k_OSC_PortLinkStatus6_Type()
)
fsp_II_2k_OSC_PortLinkStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_PortLinkStatus6.setStatus("mandatory")
_Fsp_II_2k_OSC_Connector_Type = DisplayString
_Fsp_II_2k_OSC_Connector_Object = MibTableColumn
fsp_II_2k_OSC_Connector = _Fsp_II_2k_OSC_Connector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 70),
    _Fsp_II_2k_OSC_Connector_Type()
)
fsp_II_2k_OSC_Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_Connector.setStatus("mandatory")
_Fsp_II_2k_OSC_RemoteLaserType_Type = DisplayString
_Fsp_II_2k_OSC_RemoteLaserType_Object = MibTableColumn
fsp_II_2k_OSC_RemoteLaserType = _Fsp_II_2k_OSC_RemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 2, 1, 71),
    _Fsp_II_2k_OSC_RemoteLaserType_Type()
)
fsp_II_2k_OSC_RemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_RemoteLaserType.setStatus("mandatory")
_Fsp_II_2k_EthernetHub_ObjectIdentity = ObjectIdentity
fsp_II_2k_EthernetHub = _Fsp_II_2k_EthernetHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14)
)
_Fsp_II_2k_EthernetHubTable_Object = MibTable
fsp_II_2k_EthernetHubTable = _Fsp_II_2k_EthernetHubTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubTable.setStatus("mandatory")
_Fsp_II_2k_EthernetHubEntry_Object = MibTableRow
fsp_II_2k_EthernetHubEntry = _Fsp_II_2k_EthernetHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1)
)
fsp_II_2k_EthernetHubEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_EthernetHubNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubEntry.setStatus("mandatory")
_Fsp_II_2k_EthernetHubNumber_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_EthernetHubNumber_Object = MibTableColumn
fsp_II_2k_EthernetHubNumber = _Fsp_II_2k_EthernetHubNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 1),
    _Fsp_II_2k_EthernetHubNumber_Type()
)
fsp_II_2k_EthernetHubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubNumber.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortEnable1_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortEnable1 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortEnable1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortEnable1_Object = MibTableColumn
fsp_II_2k_EthernetHubPortEnable1 = _Fsp_II_2k_EthernetHubPortEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 10),
    _Fsp_II_2k_EthernetHubPortEnable1_Type()
)
fsp_II_2k_EthernetHubPortEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortEnable1.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPartitionStatus1_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPartitionStatus1 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPartitionStatus1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPartitionStatus1_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPartitionStatus1 = _Fsp_II_2k_EthernetHubPortPartitionStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 11),
    _Fsp_II_2k_EthernetHubPortPartitionStatus1_Type()
)
fsp_II_2k_EthernetHubPortPartitionStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPartitionStatus1.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortLinkStatus1_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortLinkStatus1 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortLinkStatus1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortLinkStatus1_Object = MibTableColumn
fsp_II_2k_EthernetHubPortLinkStatus1 = _Fsp_II_2k_EthernetHubPortLinkStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 12),
    _Fsp_II_2k_EthernetHubPortLinkStatus1_Type()
)
fsp_II_2k_EthernetHubPortLinkStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortLinkStatus1.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPolarity1_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPolarity1 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPolarity1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPolarity1_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPolarity1 = _Fsp_II_2k_EthernetHubPortPolarity1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 13),
    _Fsp_II_2k_EthernetHubPortPolarity1_Type()
)
fsp_II_2k_EthernetHubPortPolarity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPolarity1.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortEnable2_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortEnable2 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortEnable2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortEnable2_Object = MibTableColumn
fsp_II_2k_EthernetHubPortEnable2 = _Fsp_II_2k_EthernetHubPortEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 20),
    _Fsp_II_2k_EthernetHubPortEnable2_Type()
)
fsp_II_2k_EthernetHubPortEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortEnable2.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPartitionStatus2_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPartitionStatus2 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPartitionStatus2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPartitionStatus2_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPartitionStatus2 = _Fsp_II_2k_EthernetHubPortPartitionStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 21),
    _Fsp_II_2k_EthernetHubPortPartitionStatus2_Type()
)
fsp_II_2k_EthernetHubPortPartitionStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPartitionStatus2.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortLinkStatus2_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortLinkStatus2 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortLinkStatus2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortLinkStatus2_Object = MibTableColumn
fsp_II_2k_EthernetHubPortLinkStatus2 = _Fsp_II_2k_EthernetHubPortLinkStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 22),
    _Fsp_II_2k_EthernetHubPortLinkStatus2_Type()
)
fsp_II_2k_EthernetHubPortLinkStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortLinkStatus2.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPolarity2_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPolarity2 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPolarity2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPolarity2_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPolarity2 = _Fsp_II_2k_EthernetHubPortPolarity2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 23),
    _Fsp_II_2k_EthernetHubPortPolarity2_Type()
)
fsp_II_2k_EthernetHubPortPolarity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPolarity2.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortEnable3_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortEnable3 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortEnable3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortEnable3_Object = MibTableColumn
fsp_II_2k_EthernetHubPortEnable3 = _Fsp_II_2k_EthernetHubPortEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 30),
    _Fsp_II_2k_EthernetHubPortEnable3_Type()
)
fsp_II_2k_EthernetHubPortEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortEnable3.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPartitionStatus3_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPartitionStatus3 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPartitionStatus3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPartitionStatus3_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPartitionStatus3 = _Fsp_II_2k_EthernetHubPortPartitionStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 31),
    _Fsp_II_2k_EthernetHubPortPartitionStatus3_Type()
)
fsp_II_2k_EthernetHubPortPartitionStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPartitionStatus3.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortLinkStatus3_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortLinkStatus3 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortLinkStatus3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortLinkStatus3_Object = MibTableColumn
fsp_II_2k_EthernetHubPortLinkStatus3 = _Fsp_II_2k_EthernetHubPortLinkStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 32),
    _Fsp_II_2k_EthernetHubPortLinkStatus3_Type()
)
fsp_II_2k_EthernetHubPortLinkStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortLinkStatus3.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPolarity3_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPolarity3 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPolarity3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPolarity3_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPolarity3 = _Fsp_II_2k_EthernetHubPortPolarity3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 33),
    _Fsp_II_2k_EthernetHubPortPolarity3_Type()
)
fsp_II_2k_EthernetHubPortPolarity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPolarity3.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortEnable4_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortEnable4 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortEnable4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortEnable4_Object = MibTableColumn
fsp_II_2k_EthernetHubPortEnable4 = _Fsp_II_2k_EthernetHubPortEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 40),
    _Fsp_II_2k_EthernetHubPortEnable4_Type()
)
fsp_II_2k_EthernetHubPortEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortEnable4.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPartitionStatus4_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPartitionStatus4 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPartitionStatus4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPartitionStatus4_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPartitionStatus4 = _Fsp_II_2k_EthernetHubPortPartitionStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 41),
    _Fsp_II_2k_EthernetHubPortPartitionStatus4_Type()
)
fsp_II_2k_EthernetHubPortPartitionStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPartitionStatus4.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortLinkStatus4_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortLinkStatus4 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortLinkStatus4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortLinkStatus4_Object = MibTableColumn
fsp_II_2k_EthernetHubPortLinkStatus4 = _Fsp_II_2k_EthernetHubPortLinkStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 42),
    _Fsp_II_2k_EthernetHubPortLinkStatus4_Type()
)
fsp_II_2k_EthernetHubPortLinkStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortLinkStatus4.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPolarity4_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPolarity4 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPolarity4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPolarity4_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPolarity4 = _Fsp_II_2k_EthernetHubPortPolarity4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 43),
    _Fsp_II_2k_EthernetHubPortPolarity4_Type()
)
fsp_II_2k_EthernetHubPortPolarity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPolarity4.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortEnable5_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortEnable5 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortEnable5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortEnable5_Object = MibTableColumn
fsp_II_2k_EthernetHubPortEnable5 = _Fsp_II_2k_EthernetHubPortEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 50),
    _Fsp_II_2k_EthernetHubPortEnable5_Type()
)
fsp_II_2k_EthernetHubPortEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortEnable5.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPartitionStatus5_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPartitionStatus5 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPartitionStatus5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPartitionStatus5_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPartitionStatus5 = _Fsp_II_2k_EthernetHubPortPartitionStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 51),
    _Fsp_II_2k_EthernetHubPortPartitionStatus5_Type()
)
fsp_II_2k_EthernetHubPortPartitionStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPartitionStatus5.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortLinkStatus5_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortLinkStatus5 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortLinkStatus5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortLinkStatus5_Object = MibTableColumn
fsp_II_2k_EthernetHubPortLinkStatus5 = _Fsp_II_2k_EthernetHubPortLinkStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 52),
    _Fsp_II_2k_EthernetHubPortLinkStatus5_Type()
)
fsp_II_2k_EthernetHubPortLinkStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortLinkStatus5.setStatus("mandatory")


class _Fsp_II_2k_EthernetHubPortPolarity5_Type(Integer32):
    """Custom type fsp_II_2k_EthernetHubPortPolarity5 based on Integer32"""
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


_Fsp_II_2k_EthernetHubPortPolarity5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthernetHubPortPolarity5_Object = MibTableColumn
fsp_II_2k_EthernetHubPortPolarity5 = _Fsp_II_2k_EthernetHubPortPolarity5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 53),
    _Fsp_II_2k_EthernetHubPortPolarity5_Type()
)
fsp_II_2k_EthernetHubPortPolarity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetHubPortPolarity5.setStatus("mandatory")
_Fsp_II_2k_TDM_ObjectIdentity = ObjectIdentity
fsp_II_2k_TDM = _Fsp_II_2k_TDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15)
)
_Fsp_II_2k_TDMTable_Object = MibTable
fsp_II_2k_TDMTable = _Fsp_II_2k_TDMTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMTable.setStatus("mandatory")
_Fsp_II_2k_TDMEntry_Object = MibTableRow
fsp_II_2k_TDMEntry = _Fsp_II_2k_TDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1)
)
fsp_II_2k_TDMEntry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_TDMNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMEntry.setStatus("mandatory")
_Fsp_II_2k_TDMNumber_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_TDMNumber_Object = MibTableColumn
fsp_II_2k_TDMNumber = _Fsp_II_2k_TDMNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 1),
    _Fsp_II_2k_TDMNumber_Type()
)
fsp_II_2k_TDMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMNumber.setStatus("mandatory")


class _Fsp_II_2k_TDMRxRem_Type(Integer32):
    """Custom type fsp_II_2k_TDMRxRem based on Integer32"""
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


_Fsp_II_2k_TDMRxRem_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMRxRem_Object = MibTableColumn
fsp_II_2k_TDMRxRem = _Fsp_II_2k_TDMRxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 4),
    _Fsp_II_2k_TDMRxRem_Type()
)
fsp_II_2k_TDMRxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRxRem.setStatus("mandatory")


class _Fsp_II_2k_TDMRxSync_Type(Integer32):
    """Custom type fsp_II_2k_TDMRxSync based on Integer32"""
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


_Fsp_II_2k_TDMRxSync_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMRxSync_Object = MibTableColumn
fsp_II_2k_TDMRxSync = _Fsp_II_2k_TDMRxSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 5),
    _Fsp_II_2k_TDMRxSync_Type()
)
fsp_II_2k_TDMRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRxSync.setStatus("mandatory")


class _Fsp_II_2k_TDMTxRem_Type(Integer32):
    """Custom type fsp_II_2k_TDMTxRem based on Integer32"""
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


_Fsp_II_2k_TDMTxRem_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMTxRem_Object = MibTableColumn
fsp_II_2k_TDMTxRem = _Fsp_II_2k_TDMTxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 6),
    _Fsp_II_2k_TDMTxRem_Type()
)
fsp_II_2k_TDMTxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMTxRem.setStatus("mandatory")


class _Fsp_II_2k_TDMTxRemC_Type(Integer32):
    """Custom type fsp_II_2k_TDMTxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fsp_II_2k_TDMTxRemC_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMTxRemC_Object = MibTableColumn
fsp_II_2k_TDMTxRemC = _Fsp_II_2k_TDMTxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 7),
    _Fsp_II_2k_TDMTxRemC_Type()
)
fsp_II_2k_TDMTxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMTxRemC.setStatus("mandatory")


class _Fsp_II_2k_TDMTxRemTemp_Type(Integer32):
    """Custom type fsp_II_2k_TDMTxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Fsp_II_2k_TDMTxRemTemp_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMTxRemTemp_Object = MibTableColumn
fsp_II_2k_TDMTxRemTemp = _Fsp_II_2k_TDMTxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 8),
    _Fsp_II_2k_TDMTxRemTemp_Type()
)
fsp_II_2k_TDMTxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMTxRemTemp.setStatus("mandatory")


class _Fsp_II_2k_TDMLocLoop_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocLoop based on Integer32"""
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


_Fsp_II_2k_TDMLocLoop_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocLoop_Object = MibTableColumn
fsp_II_2k_TDMLocLoop = _Fsp_II_2k_TDMLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 9),
    _Fsp_II_2k_TDMLocLoop_Type()
)
fsp_II_2k_TDMLocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocLoop.setStatus("mandatory")


class _Fsp_II_2k_TDMClockType_Type(Integer32):
    """Custom type fsp_II_2k_TDMClockType based on Integer32"""
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


_Fsp_II_2k_TDMClockType_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMClockType_Object = MibTableColumn
fsp_II_2k_TDMClockType = _Fsp_II_2k_TDMClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 10),
    _Fsp_II_2k_TDMClockType_Type()
)
fsp_II_2k_TDMClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMClockType.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst1 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst1_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst1 = _Fsp_II_2k_TDMLocModuleInst1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 20),
    _Fsp_II_2k_TDMLocModuleInst1_Type()
)
fsp_II_2k_TDMLocModuleInst1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable1 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable1_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable1 = _Fsp_II_2k_TDMLocModuleEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 21),
    _Fsp_II_2k_TDMLocModuleEnable1_Type()
)
fsp_II_2k_TDMLocModuleEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx1 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx1_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx1 = _Fsp_II_2k_TDMLocModuleRx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 22),
    _Fsp_II_2k_TDMLocModuleRx1_Type()
)
fsp_II_2k_TDMLocModuleRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx1 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx1_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx1 = _Fsp_II_2k_TDMLocModuleTx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 23),
    _Fsp_II_2k_TDMLocModuleTx1_Type()
)
fsp_II_2k_TDMLocModuleTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData1 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData1_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData1 = _Fsp_II_2k_TDMLocModuleRemoteData1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 24),
    _Fsp_II_2k_TDMLocModuleRemoteData1_Type()
)
fsp_II_2k_TDMLocModuleRemoteData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData1.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency1_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency1_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency1 = _Fsp_II_2k_TDMLocModuleClockFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 25),
    _Fsp_II_2k_TDMLocModuleClockFrequency1_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError1 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError1_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError1 = _Fsp_II_2k_TDMLocModuleClockError1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 26),
    _Fsp_II_2k_TDMLocModuleClockError1_Type()
)
fsp_II_2k_TDMLocModuleClockError1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst2 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst2_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst2 = _Fsp_II_2k_TDMLocModuleInst2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 30),
    _Fsp_II_2k_TDMLocModuleInst2_Type()
)
fsp_II_2k_TDMLocModuleInst2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable2 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable2_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable2 = _Fsp_II_2k_TDMLocModuleEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 31),
    _Fsp_II_2k_TDMLocModuleEnable2_Type()
)
fsp_II_2k_TDMLocModuleEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx2 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx2_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx2 = _Fsp_II_2k_TDMLocModuleRx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 32),
    _Fsp_II_2k_TDMLocModuleRx2_Type()
)
fsp_II_2k_TDMLocModuleRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx2 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx2_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx2 = _Fsp_II_2k_TDMLocModuleTx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 33),
    _Fsp_II_2k_TDMLocModuleTx2_Type()
)
fsp_II_2k_TDMLocModuleTx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData2 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData2_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData2 = _Fsp_II_2k_TDMLocModuleRemoteData2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 34),
    _Fsp_II_2k_TDMLocModuleRemoteData2_Type()
)
fsp_II_2k_TDMLocModuleRemoteData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData2.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency2_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency2_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency2 = _Fsp_II_2k_TDMLocModuleClockFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 35),
    _Fsp_II_2k_TDMLocModuleClockFrequency2_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError2 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError2_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError2 = _Fsp_II_2k_TDMLocModuleClockError2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 36),
    _Fsp_II_2k_TDMLocModuleClockError2_Type()
)
fsp_II_2k_TDMLocModuleClockError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst3 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst3_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst3 = _Fsp_II_2k_TDMLocModuleInst3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 40),
    _Fsp_II_2k_TDMLocModuleInst3_Type()
)
fsp_II_2k_TDMLocModuleInst3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable3 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable3_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable3 = _Fsp_II_2k_TDMLocModuleEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 41),
    _Fsp_II_2k_TDMLocModuleEnable3_Type()
)
fsp_II_2k_TDMLocModuleEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx3 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx3_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx3 = _Fsp_II_2k_TDMLocModuleRx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 42),
    _Fsp_II_2k_TDMLocModuleRx3_Type()
)
fsp_II_2k_TDMLocModuleRx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx3 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx3_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx3 = _Fsp_II_2k_TDMLocModuleTx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 43),
    _Fsp_II_2k_TDMLocModuleTx3_Type()
)
fsp_II_2k_TDMLocModuleTx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData3 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData3_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData3 = _Fsp_II_2k_TDMLocModuleRemoteData3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 44),
    _Fsp_II_2k_TDMLocModuleRemoteData3_Type()
)
fsp_II_2k_TDMLocModuleRemoteData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData3.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency3_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency3_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency3 = _Fsp_II_2k_TDMLocModuleClockFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 45),
    _Fsp_II_2k_TDMLocModuleClockFrequency3_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError3 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError3_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError3 = _Fsp_II_2k_TDMLocModuleClockError3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 46),
    _Fsp_II_2k_TDMLocModuleClockError3_Type()
)
fsp_II_2k_TDMLocModuleClockError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst4 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst4_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst4 = _Fsp_II_2k_TDMLocModuleInst4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 50),
    _Fsp_II_2k_TDMLocModuleInst4_Type()
)
fsp_II_2k_TDMLocModuleInst4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable4 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable4_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable4 = _Fsp_II_2k_TDMLocModuleEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 51),
    _Fsp_II_2k_TDMLocModuleEnable4_Type()
)
fsp_II_2k_TDMLocModuleEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx4 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx4_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx4 = _Fsp_II_2k_TDMLocModuleRx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 52),
    _Fsp_II_2k_TDMLocModuleRx4_Type()
)
fsp_II_2k_TDMLocModuleRx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx4 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx4_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx4 = _Fsp_II_2k_TDMLocModuleTx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 53),
    _Fsp_II_2k_TDMLocModuleTx4_Type()
)
fsp_II_2k_TDMLocModuleTx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData4 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData4_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData4 = _Fsp_II_2k_TDMLocModuleRemoteData4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 54),
    _Fsp_II_2k_TDMLocModuleRemoteData4_Type()
)
fsp_II_2k_TDMLocModuleRemoteData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData4.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency4_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency4_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency4 = _Fsp_II_2k_TDMLocModuleClockFrequency4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 55),
    _Fsp_II_2k_TDMLocModuleClockFrequency4_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError4 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError4_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError4 = _Fsp_II_2k_TDMLocModuleClockError4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 56),
    _Fsp_II_2k_TDMLocModuleClockError4_Type()
)
fsp_II_2k_TDMLocModuleClockError4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError4.setStatus("mandatory")
_Fsp_II_2k_TDMLocalConnector_Type = DisplayString
_Fsp_II_2k_TDMLocalConnector_Object = MibTableColumn
fsp_II_2k_TDMLocalConnector = _Fsp_II_2k_TDMLocalConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 60),
    _Fsp_II_2k_TDMLocalConnector_Type()
)
fsp_II_2k_TDMLocalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocalConnector.setStatus("mandatory")
_Fsp_II_2k_TDMLocalLaserType_Type = DisplayString
_Fsp_II_2k_TDMLocalLaserType_Object = MibTableColumn
fsp_II_2k_TDMLocalLaserType = _Fsp_II_2k_TDMLocalLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 61),
    _Fsp_II_2k_TDMLocalLaserType_Type()
)
fsp_II_2k_TDMLocalLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocalLaserType.setStatus("mandatory")
_Fsp_II_2k_TDMRemoteConnector_Type = DisplayString
_Fsp_II_2k_TDMRemoteConnector_Object = MibTableColumn
fsp_II_2k_TDMRemoteConnector = _Fsp_II_2k_TDMRemoteConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 62),
    _Fsp_II_2k_TDMRemoteConnector_Type()
)
fsp_II_2k_TDMRemoteConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRemoteConnector.setStatus("mandatory")
_Fsp_II_2k_TDMRemoteLaserType_Type = DisplayString
_Fsp_II_2k_TDMRemoteLaserType_Object = MibTableColumn
fsp_II_2k_TDMRemoteLaserType = _Fsp_II_2k_TDMRemoteLaserType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 63),
    _Fsp_II_2k_TDMRemoteLaserType_Type()
)
fsp_II_2k_TDMRemoteLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRemoteLaserType.setStatus("mandatory")
_Fsp_II_2k_TDMConverterType_Type = DisplayString
_Fsp_II_2k_TDMConverterType_Object = MibTableColumn
fsp_II_2k_TDMConverterType = _Fsp_II_2k_TDMConverterType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 64),
    _Fsp_II_2k_TDMConverterType_Type()
)
fsp_II_2k_TDMConverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMConverterType.setStatus("mandatory")
_Fsp_II_2k_TDMClockRecovery_Type = DisplayString
_Fsp_II_2k_TDMClockRecovery_Object = MibTableColumn
fsp_II_2k_TDMClockRecovery = _Fsp_II_2k_TDMClockRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 65),
    _Fsp_II_2k_TDMClockRecovery_Type()
)
fsp_II_2k_TDMClockRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMClockRecovery.setStatus("mandatory")
_Fsp_II_2k_TDMDataRateRange_Type = DisplayString
_Fsp_II_2k_TDMDataRateRange_Object = MibTableColumn
fsp_II_2k_TDMDataRateRange = _Fsp_II_2k_TDMDataRateRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 66),
    _Fsp_II_2k_TDMDataRateRange_Type()
)
fsp_II_2k_TDMDataRateRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMDataRateRange.setStatus("mandatory")
_Fsp_II_2k_TDMClockFreqRange_Type = DisplayString
_Fsp_II_2k_TDMClockFreqRange_Object = MibTableColumn
fsp_II_2k_TDMClockFreqRange = _Fsp_II_2k_TDMClockFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 67),
    _Fsp_II_2k_TDMClockFreqRange_Type()
)
fsp_II_2k_TDMClockFreqRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMClockFreqRange.setStatus("mandatory")


class _Fsp_II_2k_TDMChannelNumber_Type(Integer32):
    """Custom type fsp_II_2k_TDMChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsp_II_2k_TDMChannelNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMChannelNumber_Object = MibTableColumn
fsp_II_2k_TDMChannelNumber = _Fsp_II_2k_TDMChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 68),
    _Fsp_II_2k_TDMChannelNumber_Type()
)
fsp_II_2k_TDMChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMChannelNumber.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst5 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst5_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst5 = _Fsp_II_2k_TDMLocModuleInst5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 70),
    _Fsp_II_2k_TDMLocModuleInst5_Type()
)
fsp_II_2k_TDMLocModuleInst5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable5 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable5_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable5 = _Fsp_II_2k_TDMLocModuleEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 71),
    _Fsp_II_2k_TDMLocModuleEnable5_Type()
)
fsp_II_2k_TDMLocModuleEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx5 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx5_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx5 = _Fsp_II_2k_TDMLocModuleRx5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 72),
    _Fsp_II_2k_TDMLocModuleRx5_Type()
)
fsp_II_2k_TDMLocModuleRx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx5 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx5_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx5 = _Fsp_II_2k_TDMLocModuleTx5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 73),
    _Fsp_II_2k_TDMLocModuleTx5_Type()
)
fsp_II_2k_TDMLocModuleTx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData5 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData5_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData5 = _Fsp_II_2k_TDMLocModuleRemoteData5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 74),
    _Fsp_II_2k_TDMLocModuleRemoteData5_Type()
)
fsp_II_2k_TDMLocModuleRemoteData5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData5.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency5_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency5_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency5 = _Fsp_II_2k_TDMLocModuleClockFrequency5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 75),
    _Fsp_II_2k_TDMLocModuleClockFrequency5_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError5 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError5_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError5 = _Fsp_II_2k_TDMLocModuleClockError5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 76),
    _Fsp_II_2k_TDMLocModuleClockError5_Type()
)
fsp_II_2k_TDMLocModuleClockError5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst6 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst6_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst6 = _Fsp_II_2k_TDMLocModuleInst6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 80),
    _Fsp_II_2k_TDMLocModuleInst6_Type()
)
fsp_II_2k_TDMLocModuleInst6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable6 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable6_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable6 = _Fsp_II_2k_TDMLocModuleEnable6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 81),
    _Fsp_II_2k_TDMLocModuleEnable6_Type()
)
fsp_II_2k_TDMLocModuleEnable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx6 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx6_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx6 = _Fsp_II_2k_TDMLocModuleRx6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 82),
    _Fsp_II_2k_TDMLocModuleRx6_Type()
)
fsp_II_2k_TDMLocModuleRx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx6 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx6_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx6 = _Fsp_II_2k_TDMLocModuleTx6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 83),
    _Fsp_II_2k_TDMLocModuleTx6_Type()
)
fsp_II_2k_TDMLocModuleTx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData6 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData6_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData6 = _Fsp_II_2k_TDMLocModuleRemoteData6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 84),
    _Fsp_II_2k_TDMLocModuleRemoteData6_Type()
)
fsp_II_2k_TDMLocModuleRemoteData6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData6.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency6_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency6_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency6 = _Fsp_II_2k_TDMLocModuleClockFrequency6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 85),
    _Fsp_II_2k_TDMLocModuleClockFrequency6_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError6 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError6_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError6 = _Fsp_II_2k_TDMLocModuleClockError6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 86),
    _Fsp_II_2k_TDMLocModuleClockError6_Type()
)
fsp_II_2k_TDMLocModuleClockError6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst7 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst7_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst7 = _Fsp_II_2k_TDMLocModuleInst7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 90),
    _Fsp_II_2k_TDMLocModuleInst7_Type()
)
fsp_II_2k_TDMLocModuleInst7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable7 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable7_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable7 = _Fsp_II_2k_TDMLocModuleEnable7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 91),
    _Fsp_II_2k_TDMLocModuleEnable7_Type()
)
fsp_II_2k_TDMLocModuleEnable7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx7 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx7_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx7 = _Fsp_II_2k_TDMLocModuleRx7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 92),
    _Fsp_II_2k_TDMLocModuleRx7_Type()
)
fsp_II_2k_TDMLocModuleRx7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx7 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx7_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx7 = _Fsp_II_2k_TDMLocModuleTx7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 93),
    _Fsp_II_2k_TDMLocModuleTx7_Type()
)
fsp_II_2k_TDMLocModuleTx7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData7 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData7_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData7 = _Fsp_II_2k_TDMLocModuleRemoteData7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 94),
    _Fsp_II_2k_TDMLocModuleRemoteData7_Type()
)
fsp_II_2k_TDMLocModuleRemoteData7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData7.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency7_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency7_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency7 = _Fsp_II_2k_TDMLocModuleClockFrequency7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 95),
    _Fsp_II_2k_TDMLocModuleClockFrequency7_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError7 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError7_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError7 = _Fsp_II_2k_TDMLocModuleClockError7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 96),
    _Fsp_II_2k_TDMLocModuleClockError7_Type()
)
fsp_II_2k_TDMLocModuleClockError7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleInst8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleInst8 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleInst8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleInst8_Object = MibTableColumn
fsp_II_2k_TDMLocModuleInst8 = _Fsp_II_2k_TDMLocModuleInst8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 100),
    _Fsp_II_2k_TDMLocModuleInst8_Type()
)
fsp_II_2k_TDMLocModuleInst8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleInst8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleEnable8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleEnable8 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleEnable8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleEnable8_Object = MibTableColumn
fsp_II_2k_TDMLocModuleEnable8 = _Fsp_II_2k_TDMLocModuleEnable8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 101),
    _Fsp_II_2k_TDMLocModuleEnable8_Type()
)
fsp_II_2k_TDMLocModuleEnable8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnable8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRx8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRx8 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRx8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRx8_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRx8 = _Fsp_II_2k_TDMLocModuleRx8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 102),
    _Fsp_II_2k_TDMLocModuleRx8_Type()
)
fsp_II_2k_TDMLocModuleRx8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRx8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleTx8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleTx8 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleTx8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleTx8_Object = MibTableColumn
fsp_II_2k_TDMLocModuleTx8 = _Fsp_II_2k_TDMLocModuleTx8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 103),
    _Fsp_II_2k_TDMLocModuleTx8_Type()
)
fsp_II_2k_TDMLocModuleTx8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleTx8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleRemoteData8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleRemoteData8 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleRemoteData8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleRemoteData8_Object = MibTableColumn
fsp_II_2k_TDMLocModuleRemoteData8 = _Fsp_II_2k_TDMLocModuleRemoteData8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 104),
    _Fsp_II_2k_TDMLocModuleRemoteData8_Type()
)
fsp_II_2k_TDMLocModuleRemoteData8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRemoteData8.setStatus("mandatory")
_Fsp_II_2k_TDMLocModuleClockFrequency8_Type = Integer32
_Fsp_II_2k_TDMLocModuleClockFrequency8_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockFrequency8 = _Fsp_II_2k_TDMLocModuleClockFrequency8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 105),
    _Fsp_II_2k_TDMLocModuleClockFrequency8_Type()
)
fsp_II_2k_TDMLocModuleClockFrequency8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFrequency8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocModuleClockError8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocModuleClockError8 based on Integer32"""
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


_Fsp_II_2k_TDMLocModuleClockError8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocModuleClockError8_Object = MibTableColumn
fsp_II_2k_TDMLocModuleClockError8 = _Fsp_II_2k_TDMLocModuleClockError8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 106),
    _Fsp_II_2k_TDMLocModuleClockError8_Type()
)
fsp_II_2k_TDMLocModuleClockError8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockError8.setStatus("mandatory")
_Fsp_II_2k_MUX_DMX_ObjectIdentity = ObjectIdentity
fsp_II_2k_MUX_DMX = _Fsp_II_2k_MUX_DMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30)
)
_Fsp_II_2k_MUX_DMX_Table_Object = MibTable
fsp_II_2k_MUX_DMX_Table = _Fsp_II_2k_MUX_DMX_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_Table.setStatus("mandatory")
_Fsp_II_2k_MUX_DMX_Entry_Object = MibTableRow
fsp_II_2k_MUX_DMX_Entry = _Fsp_II_2k_MUX_DMX_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1)
)
fsp_II_2k_MUX_DMX_Entry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_MUX_DMX_Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_Entry.setStatus("mandatory")
_Fsp_II_2k_MUX_DMX_Number_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_MUX_DMX_Number_Object = MibTableColumn
fsp_II_2k_MUX_DMX_Number = _Fsp_II_2k_MUX_DMX_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 1),
    _Fsp_II_2k_MUX_DMX_Number_Type()
)
fsp_II_2k_MUX_DMX_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_Number.setStatus("mandatory")


class _Fsp_II_2k_MUX_DMX_WDMType_Type(Integer32):
    """Custom type fsp_II_2k_MUX_DMX_WDMType based on Integer32"""
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


_Fsp_II_2k_MUX_DMX_WDMType_Type.__name__ = "Integer32"
_Fsp_II_2k_MUX_DMX_WDMType_Object = MibTableColumn
fsp_II_2k_MUX_DMX_WDMType = _Fsp_II_2k_MUX_DMX_WDMType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 2),
    _Fsp_II_2k_MUX_DMX_WDMType_Type()
)
fsp_II_2k_MUX_DMX_WDMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_WDMType.setStatus("mandatory")


class _Fsp_II_2k_MUX_DMX_Scheme_Type(Integer32):
    """Custom type fsp_II_2k_MUX_DMX_Scheme based on Integer32"""
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


_Fsp_II_2k_MUX_DMX_Scheme_Type.__name__ = "Integer32"
_Fsp_II_2k_MUX_DMX_Scheme_Object = MibTableColumn
fsp_II_2k_MUX_DMX_Scheme = _Fsp_II_2k_MUX_DMX_Scheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 3),
    _Fsp_II_2k_MUX_DMX_Scheme_Type()
)
fsp_II_2k_MUX_DMX_Scheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_Scheme.setStatus("mandatory")


class _Fsp_II_2k_MUX_DMX_ChannelRange_Type(Integer32):
    """Custom type fsp_II_2k_MUX_DMX_ChannelRange based on Integer32"""
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


_Fsp_II_2k_MUX_DMX_ChannelRange_Type.__name__ = "Integer32"
_Fsp_II_2k_MUX_DMX_ChannelRange_Object = MibTableColumn
fsp_II_2k_MUX_DMX_ChannelRange = _Fsp_II_2k_MUX_DMX_ChannelRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 4),
    _Fsp_II_2k_MUX_DMX_ChannelRange_Type()
)
fsp_II_2k_MUX_DMX_ChannelRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_ChannelRange.setStatus("mandatory")
_Fsp_II_2k_MUX_DMX_Connector_Type = DisplayString
_Fsp_II_2k_MUX_DMX_Connector_Object = MibTableColumn
fsp_II_2k_MUX_DMX_Connector = _Fsp_II_2k_MUX_DMX_Connector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 5),
    _Fsp_II_2k_MUX_DMX_Connector_Type()
)
fsp_II_2k_MUX_DMX_Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_Connector.setStatus("mandatory")
_Fsp_II_2k_MUX_DMX_UpgradePort_Type = DisplayString
_Fsp_II_2k_MUX_DMX_UpgradePort_Object = MibTableColumn
fsp_II_2k_MUX_DMX_UpgradePort = _Fsp_II_2k_MUX_DMX_UpgradePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 30, 1, 1, 6),
    _Fsp_II_2k_MUX_DMX_UpgradePort_Type()
)
fsp_II_2k_MUX_DMX_UpgradePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_UpgradePort.setStatus("mandatory")
_Fsp_II_2k_BSM_ObjectIdentity = ObjectIdentity
fsp_II_2k_BSM = _Fsp_II_2k_BSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31)
)
_Fsp_II_2k_BSM_Table_Object = MibTable
fsp_II_2k_BSM_Table = _Fsp_II_2k_BSM_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_BSM_Table.setStatus("mandatory")
_Fsp_II_2k_BSM_Entry_Object = MibTableRow
fsp_II_2k_BSM_Entry = _Fsp_II_2k_BSM_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1)
)
fsp_II_2k_BSM_Entry.setIndexNames(
    (0, "Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_BSM_Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_BSM_Entry.setStatus("mandatory")
_Fsp_II_2k_BSM_Number_Type = Fsp_II_2k_SlotNumberRange
_Fsp_II_2k_BSM_Number_Object = MibTableColumn
fsp_II_2k_BSM_Number = _Fsp_II_2k_BSM_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 1),
    _Fsp_II_2k_BSM_Number_Type()
)
fsp_II_2k_BSM_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_BSM_Number.setStatus("mandatory")


class _Fsp_II_2k_BSM_Scheme_Type(Integer32):
    """Custom type fsp_II_2k_BSM_Scheme based on Integer32"""
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


_Fsp_II_2k_BSM_Scheme_Type.__name__ = "Integer32"
_Fsp_II_2k_BSM_Scheme_Object = MibTableColumn
fsp_II_2k_BSM_Scheme = _Fsp_II_2k_BSM_Scheme_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 2),
    _Fsp_II_2k_BSM_Scheme_Type()
)
fsp_II_2k_BSM_Scheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_BSM_Scheme.setStatus("mandatory")


class _Fsp_II_2k_BSM_BandRange_Type(Integer32):
    """Custom type fsp_II_2k_BSM_BandRange based on Integer32"""
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


_Fsp_II_2k_BSM_BandRange_Type.__name__ = "Integer32"
_Fsp_II_2k_BSM_BandRange_Object = MibTableColumn
fsp_II_2k_BSM_BandRange = _Fsp_II_2k_BSM_BandRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 3),
    _Fsp_II_2k_BSM_BandRange_Type()
)
fsp_II_2k_BSM_BandRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_BSM_BandRange.setStatus("mandatory")
_Fsp_II_2k_BSM_ConnectorType_Type = DisplayString
_Fsp_II_2k_BSM_ConnectorType_Object = MibTableColumn
fsp_II_2k_BSM_ConnectorType = _Fsp_II_2k_BSM_ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 31, 1, 1, 4),
    _Fsp_II_2k_BSM_ConnectorType_Type()
)
fsp_II_2k_BSM_ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_BSM_ConnectorType.setStatus("mandatory")
_Fsp_II_2k_Trap_ObjectIdentity = ObjectIdentity
fsp_II_2k_Trap = _Fsp_II_2k_Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100)
)

# Managed Objects groups


# Notification objects

fsp_II_2k_HardwareAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 1)
)
fsp_II_2k_HardwareAdded.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HardwareAdded.setStatus(
        ""
    )

fsp_II_2k_HardwareDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 2)
)
fsp_II_2k_HardwareDeleted.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HardwareDeleted.setStatus(
        ""
    )

fsp_II_2k_PSNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 3)
)
fsp_II_2k_PSNotFail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_PSNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_PSNotFail.setStatus(
        ""
    )

fsp_II_2k_PSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 4)
)
fsp_II_2k_PSFail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_PSNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_PSFail.setStatus(
        ""
    )

fsp_II_2k_FanNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 5)
)
fsp_II_2k_FanNotFail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_FanNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_FanNotFail.setStatus(
        ""
    )

fsp_II_2k_FanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 6)
)
fsp_II_2k_FanFail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_FanNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_FanFail.setStatus(
        ""
    )

fsp_II_2k_BusNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 7)
)
if mibBuilder.loadTexts:
    fsp_II_2k_BusNotFail.setStatus(
        ""
    )

fsp_II_2k_BusFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 8)
)
if mibBuilder.loadTexts:
    fsp_II_2k_BusFail.setStatus(
        ""
    )

fsp_II_2k_ConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 9)
)
if mibBuilder.loadTexts:
    fsp_II_2k_ConfigMismatch.setStatus(
        ""
    )

fsp_II_2k_RxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 20)
)
fsp_II_2k_RxLocOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxLocOn.setStatus(
        ""
    )

fsp_II_2k_RxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 21)
)
fsp_II_2k_RxLocOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxLocOff.setStatus(
        ""
    )

fsp_II_2k_TxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 22)
)
fsp_II_2k_TxLocOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxLocOn.setStatus(
        ""
    )

fsp_II_2k_TxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 23)
)
fsp_II_2k_TxLocOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxLocOff.setStatus(
        ""
    )

fsp_II_2k_RxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 24)
)
fsp_II_2k_RxRemOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRemOn.setStatus(
        ""
    )

fsp_II_2k_RxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 25)
)
fsp_II_2k_RxRemOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRemOff.setStatus(
        ""
    )

fsp_II_2k_TxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 26)
)
fsp_II_2k_TxRemOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRemOn.setStatus(
        ""
    )

fsp_II_2k_TxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 27)
)
fsp_II_2k_TxRemOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRemOff.setStatus(
        ""
    )

fsp_II_2k_RxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 28)
)
fsp_II_2k_RxRem2On.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRem2On.setStatus(
        ""
    )

fsp_II_2k_RxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 29)
)
fsp_II_2k_RxRem2Off.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRem2Off.setStatus(
        ""
    )

fsp_II_2k_TxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 30)
)
fsp_II_2k_TxRem2On.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRem2On.setStatus(
        ""
    )

fsp_II_2k_TxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 31)
)
fsp_II_2k_TxRem2Off.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRem2Off.setStatus(
        ""
    )

fsp_II_2k_ClockNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 32)
)
fsp_II_2k_ClockNoFail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockNoFail.setStatus(
        ""
    )

fsp_II_2k_ClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 33)
)
fsp_II_2k_ClockFail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockFail.setStatus(
        ""
    )

fsp_II_2k_ClockChangeFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 34)
)
fsp_II_2k_ClockChangeFrequency.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockChangeFrequency.setStatus(
        ""
    )

fsp_II_2k_LocLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 35)
)
fsp_II_2k_LocLoopOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_LocLoopOn.setStatus(
        ""
    )

fsp_II_2k_LocLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 36)
)
fsp_II_2k_LocLoopOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_LocLoopOff.setStatus(
        ""
    )

fsp_II_2k_RemLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 37)
)
fsp_II_2k_RemLoopOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemLoopOn.setStatus(
        ""
    )

fsp_II_2k_RemLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 38)
)
fsp_II_2k_RemLoopOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemLoopOff.setStatus(
        ""
    )

fsp_II_2k_switchReferenceLaserOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 40)
)
fsp_II_2k_switchReferenceLaserOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchReferenceLaserOn.setStatus(
        ""
    )

fsp_II_2k_switchReferenceLaserOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 41)
)
fsp_II_2k_switchReferenceLaserOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchReferenceLaserOff.setStatus(
        ""
    )

fsp_II_2k_switchToA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 42)
)
fsp_II_2k_switchToA.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchToA.setStatus(
        ""
    )

fsp_II_2k_switchToB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 43)
)
fsp_II_2k_switchToB.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchToB.setStatus(
        ""
    )

fsp_II_2k_switchAutomatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 44)
)
fsp_II_2k_switchAutomatic.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchAutomatic.setStatus(
        ""
    )

fsp_II_2k_switchLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 45)
)
fsp_II_2k_switchLocked.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLocked.setStatus(
        ""
    )

fsp_II_2k_switchLineAavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 46)
)
fsp_II_2k_switchLineAavail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineAavail.setStatus(
        ""
    )

fsp_II_2k_switchLineANotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 47)
)
fsp_II_2k_switchLineANotAvail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineANotAvail.setStatus(
        ""
    )

fsp_II_2k_switchLineBavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 48)
)
fsp_II_2k_switchLineBavail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineBavail.setStatus(
        ""
    )

fsp_II_2k_switchLineBNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 49)
)
fsp_II_2k_switchLineBNotAvail.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineBNotAvail.setStatus(
        ""
    )

fsp_II_2k_repeatedMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 50)
)
fsp_II_2k_repeatedMessage.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_repeatedMessage.setStatus(
        ""
    )

fsp_II_2k_INNCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 51)
)
if mibBuilder.loadTexts:
    fsp_II_2k_INNCDown.setStatus(
        ""
    )

fsp_II_2k_INNCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 52)
)
if mibBuilder.loadTexts:
    fsp_II_2k_INNCUp.setStatus(
        ""
    )

fsp_II_2k_switchAutoLaserShutdownOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 53)
)
fsp_II_2k_switchAutoLaserShutdownOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchAutoLaserShutdownOn.setStatus(
        ""
    )

fsp_II_2k_switchAutoLaserShutdownOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 54)
)
fsp_II_2k_switchAutoLaserShutdownOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchAutoLaserShutdownOff.setStatus(
        ""
    )

fsp_II_2k_NEMIAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 55)
)
fsp_II_2k_NEMIAuthFail.setObjects(
      *(("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_MainLastAuthFailSource"),
        ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_MainLastAuthFailDescription"))
)
if mibBuilder.loadTexts:
    fsp_II_2k_NEMIAuthFail.setStatus(
        ""
    )

fsp_II_2k_EthernetPortEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 60)
)
fsp_II_2k_EthernetPortEnable.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortEnable.setStatus(
        ""
    )

fsp_II_2k_EthernetPortDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 61)
)
fsp_II_2k_EthernetPortDisable.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortDisable.setStatus(
        ""
    )

fsp_II_2k_EthernetPortPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 62)
)
fsp_II_2k_EthernetPortPartitioned.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortPartitioned.setStatus(
        ""
    )

fsp_II_2k_EthernetPortNotPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 63)
)
fsp_II_2k_EthernetPortNotPartitioned.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortNotPartitioned.setStatus(
        ""
    )

fsp_II_2k_EthernetPortLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 64)
)
fsp_II_2k_EthernetPortLinkPulses.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortLinkPulses.setStatus(
        ""
    )

fsp_II_2k_EthernetPortNoLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 65)
)
fsp_II_2k_EthernetPortNoLinkPulses.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortNoLinkPulses.setStatus(
        ""
    )

fsp_II_2k_TDMRemoteSyncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 70)
)
fsp_II_2k_TDMRemoteSyncLoss.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRemoteSyncLoss.setStatus(
        ""
    )

fsp_II_2k_TDMRemoteSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 71)
)
fsp_II_2k_TDMRemoteSync.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRemoteSync.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 72)
)
fsp_II_2k_TDMLocModuleEnabled1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 73)
)
fsp_II_2k_TDMLocModuleDisable1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 74)
)
fsp_II_2k_TDMLocModuleEnabled2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 75)
)
fsp_II_2k_TDMLocModuleDisable2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 76)
)
fsp_II_2k_TDMLocModuleEnabled3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 77)
)
fsp_II_2k_TDMLocModuleDisable3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 78)
)
fsp_II_2k_TDMLocModuleEnabled4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 79)
)
fsp_II_2k_TDMLocModuleDisable4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 80)
)
fsp_II_2k_TDMLocModuleEnabled5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 81)
)
fsp_II_2k_TDMLocModuleDisable5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 82)
)
fsp_II_2k_TDMLocModuleEnabled6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 83)
)
fsp_II_2k_TDMLocModuleDisable6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 84)
)
fsp_II_2k_TDMLocModuleEnabled7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 85)
)
fsp_II_2k_TDMLocModuleDisable7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleEnabled8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 86)
)
fsp_II_2k_TDMLocModuleEnabled8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleEnabled8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleDisable8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 87)
)
fsp_II_2k_TDMLocModuleDisable8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleDisable8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 88)
)
fsp_II_2k_TDMLocModuleRxOn1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 89)
)
fsp_II_2k_TDMLocModuleRxOff1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 90)
)
fsp_II_2k_TDMLocModuleRxOn2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 91)
)
fsp_II_2k_TDMLocModuleRxOff2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 92)
)
fsp_II_2k_TDMLocModuleRxOn3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 93)
)
fsp_II_2k_TDMLocModuleRxOff3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 94)
)
fsp_II_2k_TDMLocModuleRxOn4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 95)
)
fsp_II_2k_TDMLocModuleRxOff4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 96)
)
fsp_II_2k_TDMLocModuleRxOn5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 97)
)
fsp_II_2k_TDMLocModuleRxOff5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 98)
)
fsp_II_2k_TDMLocModuleRxOn6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 99)
)
fsp_II_2k_TDMLocModuleRxOff6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 100)
)
fsp_II_2k_TDMLocModuleRxOn7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 101)
)
fsp_II_2k_TDMLocModuleRxOff7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOn8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 102)
)
fsp_II_2k_TDMLocModuleRxOn8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOn8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleRxOff8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 103)
)
fsp_II_2k_TDMLocModuleRxOff8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleRxOff8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 104)
)
fsp_II_2k_TDMLocModuleData1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 105)
)
fsp_II_2k_TDMLocModuleNoData1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 106)
)
fsp_II_2k_TDMLocModuleData2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 107)
)
fsp_II_2k_TDMLocModuleNoData2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 108)
)
fsp_II_2k_TDMLocModuleData3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 109)
)
fsp_II_2k_TDMLocModuleNoData3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 110)
)
fsp_II_2k_TDMLocModuleData4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 111)
)
fsp_II_2k_TDMLocModuleNoData4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 112)
)
fsp_II_2k_TDMLocModuleData5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 113)
)
fsp_II_2k_TDMLocModuleNoData5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 114)
)
fsp_II_2k_TDMLocModuleData6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 115)
)
fsp_II_2k_TDMLocModuleNoData6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 116)
)
fsp_II_2k_TDMLocModuleData7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 117)
)
fsp_II_2k_TDMLocModuleNoData7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleData8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 118)
)
fsp_II_2k_TDMLocModuleData8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleData8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleNoData8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 119)
)
fsp_II_2k_TDMLocModuleNoData8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleNoData8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 120)
)
fsp_II_2k_TDMLocModuleClockFail1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 121)
)
fsp_II_2k_TDMLocModuleClockNoFail1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 122)
)
fsp_II_2k_TDMLocModuleClockFail2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 123)
)
fsp_II_2k_TDMLocModuleClockNoFail2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 124)
)
fsp_II_2k_TDMLocModuleClockFail3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 125)
)
fsp_II_2k_TDMLocModuleClockNoFail3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 126)
)
fsp_II_2k_TDMLocModuleClockFail4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 127)
)
fsp_II_2k_TDMLocModuleClockNoFail4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 128)
)
fsp_II_2k_TDMLocModuleClockFail5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 129)
)
fsp_II_2k_TDMLocModuleClockNoFail5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 130)
)
fsp_II_2k_TDMLocModuleClockFail6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 131)
)
fsp_II_2k_TDMLocModuleClockNoFail6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 132)
)
fsp_II_2k_TDMLocModuleClockFail7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 133)
)
fsp_II_2k_TDMLocModuleClockNoFail7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockFail8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 134)
)
fsp_II_2k_TDMLocModuleClockFail8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockFail8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockNoFail8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 135)
)
fsp_II_2k_TDMLocModuleClockNoFail8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockNoFail8.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 136)
)
fsp_II_2k_TDMLocModuleClockChange1.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange1.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 137)
)
fsp_II_2k_TDMLocModuleClockChange2.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange2.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 138)
)
fsp_II_2k_TDMLocModuleClockChange3.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange3.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 139)
)
fsp_II_2k_TDMLocModuleClockChange4.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange4.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 140)
)
fsp_II_2k_TDMLocModuleClockChange5.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange5.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 141)
)
fsp_II_2k_TDMLocModuleClockChange6.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange6.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 142)
)
fsp_II_2k_TDMLocModuleClockChange7.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange7.setStatus(
        ""
    )

fsp_II_2k_TDMLocModuleClockChange8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 143)
)
fsp_II_2k_TDMLocModuleClockChange8.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocModuleClockChange8.setStatus(
        ""
    )

fsp_II_2k_RemoteClockNoSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 170)
)
fsp_II_2k_RemoteClockNoSync.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClockNoSync.setStatus(
        ""
    )

fsp_II_2k_RemoteClockSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 171)
)
fsp_II_2k_RemoteClockSync.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClockSync.setStatus(
        ""
    )

fsp_II_2k_RemoteClock2NoSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 172)
)
fsp_II_2k_RemoteClock2NoSync.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClock2NoSync.setStatus(
        ""
    )

fsp_II_2k_RemoteClock2Sync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 173)
)
fsp_II_2k_RemoteClock2Sync.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClock2Sync.setStatus(
        ""
    )

fsp_II_2k_RegeneratorModeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 180)
)
fsp_II_2k_RegeneratorModeOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RegeneratorModeOn.setStatus(
        ""
    )

fsp_II_2k_RegeneratorModeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 181)
)
fsp_II_2k_RegeneratorModeOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RegeneratorModeOff.setStatus(
        ""
    )

fsp_II_2k_RSM_OSC_OSCOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 210)
)
fsp_II_2k_RSM_OSC_OSCOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_OSC_OSCOn.setStatus(
        ""
    )

fsp_II_2k_RSM_OSC_OSCOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 211)
)
fsp_II_2k_RSM_OSC_OSCOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_OSC_OSCOff.setStatus(
        ""
    )

fsp_II_2k_EthernetPortSpeed10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 220)
)
fsp_II_2k_EthernetPortSpeed10.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortSpeed10.setStatus(
        ""
    )

fsp_II_2k_EthernetPortSpeed100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 221)
)
fsp_II_2k_EthernetPortSpeed100.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortSpeed100.setStatus(
        ""
    )

fsp_II_2k_EthernetPortDuplexHalf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 222)
)
fsp_II_2k_EthernetPortDuplexHalf.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortDuplexHalf.setStatus(
        ""
    )

fsp_II_2k_EthernetPortDuplexFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 223)
)
fsp_II_2k_EthernetPortDuplexFull.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortDuplexFull.setStatus(
        ""
    )

fsp_II_2k_EthernetPortAutonegotiationOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 224)
)
fsp_II_2k_EthernetPortAutonegotiationOn.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortAutonegotiationOn.setStatus(
        ""
    )

fsp_II_2k_EthernetPortAutonegotiationOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 225)
)
fsp_II_2k_EthernetPortAutonegotiationOff.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortAutonegotiationOff.setStatus(
        ""
    )

fsp_II_2k_EthernetPortPolarityPositive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 226)
)
fsp_II_2k_EthernetPortPolarityPositive.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortPolarityPositive.setStatus(
        ""
    )

fsp_II_2k_EthernetPortPolarityNegative = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 227)
)
fsp_II_2k_EthernetPortPolarityNegative.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthernetPortPolarityNegative.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Change2LineA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 240)
)
fsp_II_2k_HotStandby_Change2LineA.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Change2LineA.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Change2LineB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 241)
)
fsp_II_2k_HotStandby_Change2LineB.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Change2LineB.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 242)
)
fsp_II_2k_HotStandby_Locked.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Locked.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Automatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 243)
)
fsp_II_2k_HotStandby_Automatic.setObjects(
    ("Fsp_II_Fsp_2000_R1-MIB", "fsp_II_2k_SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Automatic.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fsp_II_Fsp_2000_R1-MIB",
    **{"Fsp_II_2k_SlotNumberRange": Fsp_II_2k_SlotNumberRange,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "adva": adva,
       "products": products,
       "fsp_II_2k": fsp_II_2k,
       "fsp_II_2k_Main": fsp_II_2k_Main,
       "fsp_II_2k_Housing": fsp_II_2k_Housing,
       "fsp_II_2k_Manufacturer": fsp_II_2k_Manufacturer,
       "fsp_II_2k_MainType": fsp_II_2k_MainType,
       "fsp_II_2k_MainSerialNumber": fsp_II_2k_MainSerialNumber,
       "fsp_II_2k_MainHardwareVersion": fsp_II_2k_MainHardwareVersion,
       "fsp_II_2k_MainSoftwareVersion": fsp_II_2k_MainSoftwareVersion,
       "fsp_II_2k_MainBusMessages": fsp_II_2k_MainBusMessages,
       "fsp_II_2k_MainBusErrors": fsp_II_2k_MainBusErrors,
       "fsp_II_2k_MainLastEvent": fsp_II_2k_MainLastEvent,
       "fsp_II_2k_MainMotd": fsp_II_2k_MainMotd,
       "fsp_II_2k_MainTrapsinkTable": fsp_II_2k_MainTrapsinkTable,
       "fsp_II_2k_MainTrapsinkEntry": fsp_II_2k_MainTrapsinkEntry,
       "fsp_II_2k_MainTrapsinkNumber": fsp_II_2k_MainTrapsinkNumber,
       "fsp_II_2k_MainTrapsinkAddress": fsp_II_2k_MainTrapsinkAddress,
       "fsp_II_2k_MainTrapsinkCommunity": fsp_II_2k_MainTrapsinkCommunity,
       "fsp_II_2k_MainTrapsinkPriority": fsp_II_2k_MainTrapsinkPriority,
       "fsp_II_2k_MainLogfileTable": fsp_II_2k_MainLogfileTable,
       "fsp_II_2k_MainLogfileEntry": fsp_II_2k_MainLogfileEntry,
       "fsp_II_2k_MainLogfileNumber": fsp_II_2k_MainLogfileNumber,
       "fsp_II_2k_MainLogfileName": fsp_II_2k_MainLogfileName,
       "fsp_II_2k_MainLogfileSize": fsp_II_2k_MainLogfileSize,
       "fsp_II_2k_MainLogfilePriority": fsp_II_2k_MainLogfilePriority,
       "fsp_II_2k_MainProtocolVersion": fsp_II_2k_MainProtocolVersion,
       "fsp_II_2k_MainSystemVersion": fsp_II_2k_MainSystemVersion,
       "fsp_II_2k_MainConfigMismatch": fsp_II_2k_MainConfigMismatch,
       "fsp_II_2k_MainLastAuthFailSource": fsp_II_2k_MainLastAuthFailSource,
       "fsp_II_2k_MainLastAuthFailDescription": fsp_II_2k_MainLastAuthFailDescription,
       "fsp_II_2k_SlotTable": fsp_II_2k_SlotTable,
       "fsp_II_2k_SlotEntry": fsp_II_2k_SlotEntry,
       "fsp_II_2k_SlotNumber": fsp_II_2k_SlotNumber,
       "fsp_II_2k_Type": fsp_II_2k_Type,
       "fsp_II_2k_SlotTypeNumber": fsp_II_2k_SlotTypeNumber,
       "fsp_II_2k_SerialNumber": fsp_II_2k_SerialNumber,
       "fsp_II_2k_HardwareVersion": fsp_II_2k_HardwareVersion,
       "fsp_II_2k_SoftwareVersion": fsp_II_2k_SoftwareVersion,
       "fsp_II_2k_Temperature": fsp_II_2k_Temperature,
       "fsp_II_2k_BoardVoltage": fsp_II_2k_BoardVoltage,
       "fsp_II_2k_DetailInfo": fsp_II_2k_DetailInfo,
       "fsp_II_2k_EPLDVersion": fsp_II_2k_EPLDVersion,
       "fsp_II_2k_CustomerLabel": fsp_II_2k_CustomerLabel,
       "fsp_II_2k_ProductionVersion": fsp_II_2k_ProductionVersion,
       "fsp_II_2k_SlotSubType": fsp_II_2k_SlotSubType,
       "fsp_II_2k_SlotAlias": fsp_II_2k_SlotAlias,
       "fsp_II_2k_SlotComment": fsp_II_2k_SlotComment,
       "fsp_II_2k_PSTable": fsp_II_2k_PSTable,
       "fsp_II_2k_PSEntry": fsp_II_2k_PSEntry,
       "fsp_II_2k_PSNumber": fsp_II_2k_PSNumber,
       "fsp_II_2k_PSOn": fsp_II_2k_PSOn,
       "fsp_II_2k_FanTable": fsp_II_2k_FanTable,
       "fsp_II_2k_FanEntry": fsp_II_2k_FanEntry,
       "fsp_II_2k_FanNumber": fsp_II_2k_FanNumber,
       "fsp_II_2k_FanOn": fsp_II_2k_FanOn,
       "fsp_II_2k_Converter": fsp_II_2k_Converter,
       "fsp_II_2k_ConverterTable": fsp_II_2k_ConverterTable,
       "fsp_II_2k_ConverterEntry": fsp_II_2k_ConverterEntry,
       "fsp_II_2k_ConverterNumber": fsp_II_2k_ConverterNumber,
       "fsp_II_2k_RxLoc": fsp_II_2k_RxLoc,
       "fsp_II_2k_TxLoc": fsp_II_2k_TxLoc,
       "fsp_II_2k_TxLocC": fsp_II_2k_TxLocC,
       "fsp_II_2k_TxLocTemp": fsp_II_2k_TxLocTemp,
       "fsp_II_2k_RxRem": fsp_II_2k_RxRem,
       "fsp_II_2k_TxRem": fsp_II_2k_TxRem,
       "fsp_II_2k_TxRemC": fsp_II_2k_TxRemC,
       "fsp_II_2k_TxRemTemp": fsp_II_2k_TxRemTemp,
       "fsp_II_2k_RxRem2": fsp_II_2k_RxRem2,
       "fsp_II_2k_ClockState": fsp_II_2k_ClockState,
       "fsp_II_2k_ClockFreq": fsp_II_2k_ClockFreq,
       "fsp_II_2k_LocLoop": fsp_II_2k_LocLoop,
       "fsp_II_2k_RemLoop": fsp_II_2k_RemLoop,
       "fsp_II_2k_ClockType": fsp_II_2k_ClockType,
       "fsp_II_2k_HotStandby_ActiveLine": fsp_II_2k_HotStandby_ActiveLine,
       "fsp_II_2k_HotStandby_LineLocked": fsp_II_2k_HotStandby_LineLocked,
       "fsp_II_2k_LocalConnector": fsp_II_2k_LocalConnector,
       "fsp_II_2k_LocalLaserType": fsp_II_2k_LocalLaserType,
       "fsp_II_2k_RemoteConnector": fsp_II_2k_RemoteConnector,
       "fsp_II_2k_RemoteLaserType": fsp_II_2k_RemoteLaserType,
       "fsp_II_2k_ConverterType": fsp_II_2k_ConverterType,
       "fsp_II_2k_ClockRecovery": fsp_II_2k_ClockRecovery,
       "fsp_II_2k_SupportedDataRateTransparent": fsp_II_2k_SupportedDataRateTransparent,
       "fsp_II_2k_SupportedDataRateClocked": fsp_II_2k_SupportedDataRateClocked,
       "fsp_II_2k_ChannelNumber": fsp_II_2k_ChannelNumber,
       "fsp_II_2k_RemoteClockState": fsp_II_2k_RemoteClockState,
       "fsp_II_2k_RemoteClockState2": fsp_II_2k_RemoteClockState2,
       "fsp_II_2k_RegeneratorMode": fsp_II_2k_RegeneratorMode,
       "fsp_II_2k_Switch": fsp_II_2k_Switch,
       "fsp_II_2k_SwitchTable": fsp_II_2k_SwitchTable,
       "fsp_II_2k_SwitchEntry": fsp_II_2k_SwitchEntry,
       "fsp_II_2k_SwitchNumber": fsp_II_2k_SwitchNumber,
       "fsp_II_2k_SwitchLine": fsp_II_2k_SwitchLine,
       "fsp_II_2k_SwitchMode": fsp_II_2k_SwitchMode,
       "fsp_II_2k_SwitchLaserOn": fsp_II_2k_SwitchLaserOn,
       "fsp_II_2k_SwitchLineAavail": fsp_II_2k_SwitchLineAavail,
       "fsp_II_2k_SwitchLineBavail": fsp_II_2k_SwitchLineBavail,
       "fsp_II_2k_SwitchAutoLaserShutdown": fsp_II_2k_SwitchAutoLaserShutdown,
       "fsp_II_2k_SwitchConnector": fsp_II_2k_SwitchConnector,
       "fsp_II_2k_SwitchRemoteLaserType": fsp_II_2k_SwitchRemoteLaserType,
       "fsp_II_2k_RSM_OSC": fsp_II_2k_RSM_OSC,
       "fsp_II_2k_RSM_Table": fsp_II_2k_RSM_Table,
       "fsp_II_2k_RSM_Entry": fsp_II_2k_RSM_Entry,
       "fsp_II_2k_RSM_Number": fsp_II_2k_RSM_Number,
       "fsp_II_2k_RSM_Line": fsp_II_2k_RSM_Line,
       "fsp_II_2k_RSM_Mode": fsp_II_2k_RSM_Mode,
       "fsp_II_2k_RSM_LaserOn": fsp_II_2k_RSM_LaserOn,
       "fsp_II_2k_RSM_LineAavail": fsp_II_2k_RSM_LineAavail,
       "fsp_II_2k_RSM_LineBavail": fsp_II_2k_RSM_LineBavail,
       "fsp_II_2k_RSM_Control": fsp_II_2k_RSM_Control,
       "fsp_II_2k_RSM_Connector": fsp_II_2k_RSM_Connector,
       "fsp_II_2k_RSM_RemoteLaserType": fsp_II_2k_RSM_RemoteLaserType,
       "fsp_II_2k_OSC_Table": fsp_II_2k_OSC_Table,
       "fsp_II_2k_OSC_Entry": fsp_II_2k_OSC_Entry,
       "fsp_II_2k_OSC_Number": fsp_II_2k_OSC_Number,
       "fsp_II_2k_OSC_LaserOn": fsp_II_2k_OSC_LaserOn,
       "fsp_II_2k_OSC_P1_fail": fsp_II_2k_OSC_P1_fail,
       "fsp_II_2k_OSC_P2_fail": fsp_II_2k_OSC_P2_fail,
       "fsp_II_2k_OSC_PortEnable1": fsp_II_2k_OSC_PortEnable1,
       "fsp_II_2k_OSC_PortSpeed1": fsp_II_2k_OSC_PortSpeed1,
       "fsp_II_2k_OSC_PortDuplex1": fsp_II_2k_OSC_PortDuplex1,
       "fsp_II_2k_OSC_PortAutoneg1": fsp_II_2k_OSC_PortAutoneg1,
       "fsp_II_2k_OSC_PortPolarity1": fsp_II_2k_OSC_PortPolarity1,
       "fsp_II_2k_OSC_PortLinkStatus1": fsp_II_2k_OSC_PortLinkStatus1,
       "fsp_II_2k_OSC_PortEnable2": fsp_II_2k_OSC_PortEnable2,
       "fsp_II_2k_OSC_PortSpeed2": fsp_II_2k_OSC_PortSpeed2,
       "fsp_II_2k_OSC_PortDuplex2": fsp_II_2k_OSC_PortDuplex2,
       "fsp_II_2k_OSC_PortAutoneg2": fsp_II_2k_OSC_PortAutoneg2,
       "fsp_II_2k_OSC_PortPolarity2": fsp_II_2k_OSC_PortPolarity2,
       "fsp_II_2k_OSC_PortLinkStatus2": fsp_II_2k_OSC_PortLinkStatus2,
       "fsp_II_2k_OSC_PortEnable3": fsp_II_2k_OSC_PortEnable3,
       "fsp_II_2k_OSC_PortSpeed3": fsp_II_2k_OSC_PortSpeed3,
       "fsp_II_2k_OSC_PortDuplex3": fsp_II_2k_OSC_PortDuplex3,
       "fsp_II_2k_OSC_PortAutoneg3": fsp_II_2k_OSC_PortAutoneg3,
       "fsp_II_2k_OSC_PortPolarity3": fsp_II_2k_OSC_PortPolarity3,
       "fsp_II_2k_OSC_PortLinkStatus3": fsp_II_2k_OSC_PortLinkStatus3,
       "fsp_II_2k_OSC_PortEnable4": fsp_II_2k_OSC_PortEnable4,
       "fsp_II_2k_OSC_PortSpeed4": fsp_II_2k_OSC_PortSpeed4,
       "fsp_II_2k_OSC_PortDuplex4": fsp_II_2k_OSC_PortDuplex4,
       "fsp_II_2k_OSC_PortAutoneg4": fsp_II_2k_OSC_PortAutoneg4,
       "fsp_II_2k_OSC_PortPolarity4": fsp_II_2k_OSC_PortPolarity4,
       "fsp_II_2k_OSC_PortLinkStatus4": fsp_II_2k_OSC_PortLinkStatus4,
       "fsp_II_2k_OSC_PortEnable5": fsp_II_2k_OSC_PortEnable5,
       "fsp_II_2k_OSC_PortSpeed5": fsp_II_2k_OSC_PortSpeed5,
       "fsp_II_2k_OSC_PortDuplex5": fsp_II_2k_OSC_PortDuplex5,
       "fsp_II_2k_OSC_PortAutoneg5": fsp_II_2k_OSC_PortAutoneg5,
       "fsp_II_2k_OSC_PortPolarity5": fsp_II_2k_OSC_PortPolarity5,
       "fsp_II_2k_OSC_PortLinkStatus5": fsp_II_2k_OSC_PortLinkStatus5,
       "fsp_II_2k_OSC_PortEnable6": fsp_II_2k_OSC_PortEnable6,
       "fsp_II_2k_OSC_PortSpeed6": fsp_II_2k_OSC_PortSpeed6,
       "fsp_II_2k_OSC_PortDuplex6": fsp_II_2k_OSC_PortDuplex6,
       "fsp_II_2k_OSC_PortLinkStatus6": fsp_II_2k_OSC_PortLinkStatus6,
       "fsp_II_2k_OSC_Connector": fsp_II_2k_OSC_Connector,
       "fsp_II_2k_OSC_RemoteLaserType": fsp_II_2k_OSC_RemoteLaserType,
       "fsp_II_2k_EthernetHub": fsp_II_2k_EthernetHub,
       "fsp_II_2k_EthernetHubTable": fsp_II_2k_EthernetHubTable,
       "fsp_II_2k_EthernetHubEntry": fsp_II_2k_EthernetHubEntry,
       "fsp_II_2k_EthernetHubNumber": fsp_II_2k_EthernetHubNumber,
       "fsp_II_2k_EthernetHubPortEnable1": fsp_II_2k_EthernetHubPortEnable1,
       "fsp_II_2k_EthernetHubPortPartitionStatus1": fsp_II_2k_EthernetHubPortPartitionStatus1,
       "fsp_II_2k_EthernetHubPortLinkStatus1": fsp_II_2k_EthernetHubPortLinkStatus1,
       "fsp_II_2k_EthernetHubPortPolarity1": fsp_II_2k_EthernetHubPortPolarity1,
       "fsp_II_2k_EthernetHubPortEnable2": fsp_II_2k_EthernetHubPortEnable2,
       "fsp_II_2k_EthernetHubPortPartitionStatus2": fsp_II_2k_EthernetHubPortPartitionStatus2,
       "fsp_II_2k_EthernetHubPortLinkStatus2": fsp_II_2k_EthernetHubPortLinkStatus2,
       "fsp_II_2k_EthernetHubPortPolarity2": fsp_II_2k_EthernetHubPortPolarity2,
       "fsp_II_2k_EthernetHubPortEnable3": fsp_II_2k_EthernetHubPortEnable3,
       "fsp_II_2k_EthernetHubPortPartitionStatus3": fsp_II_2k_EthernetHubPortPartitionStatus3,
       "fsp_II_2k_EthernetHubPortLinkStatus3": fsp_II_2k_EthernetHubPortLinkStatus3,
       "fsp_II_2k_EthernetHubPortPolarity3": fsp_II_2k_EthernetHubPortPolarity3,
       "fsp_II_2k_EthernetHubPortEnable4": fsp_II_2k_EthernetHubPortEnable4,
       "fsp_II_2k_EthernetHubPortPartitionStatus4": fsp_II_2k_EthernetHubPortPartitionStatus4,
       "fsp_II_2k_EthernetHubPortLinkStatus4": fsp_II_2k_EthernetHubPortLinkStatus4,
       "fsp_II_2k_EthernetHubPortPolarity4": fsp_II_2k_EthernetHubPortPolarity4,
       "fsp_II_2k_EthernetHubPortEnable5": fsp_II_2k_EthernetHubPortEnable5,
       "fsp_II_2k_EthernetHubPortPartitionStatus5": fsp_II_2k_EthernetHubPortPartitionStatus5,
       "fsp_II_2k_EthernetHubPortLinkStatus5": fsp_II_2k_EthernetHubPortLinkStatus5,
       "fsp_II_2k_EthernetHubPortPolarity5": fsp_II_2k_EthernetHubPortPolarity5,
       "fsp_II_2k_TDM": fsp_II_2k_TDM,
       "fsp_II_2k_TDMTable": fsp_II_2k_TDMTable,
       "fsp_II_2k_TDMEntry": fsp_II_2k_TDMEntry,
       "fsp_II_2k_TDMNumber": fsp_II_2k_TDMNumber,
       "fsp_II_2k_TDMRxRem": fsp_II_2k_TDMRxRem,
       "fsp_II_2k_TDMRxSync": fsp_II_2k_TDMRxSync,
       "fsp_II_2k_TDMTxRem": fsp_II_2k_TDMTxRem,
       "fsp_II_2k_TDMTxRemC": fsp_II_2k_TDMTxRemC,
       "fsp_II_2k_TDMTxRemTemp": fsp_II_2k_TDMTxRemTemp,
       "fsp_II_2k_TDMLocLoop": fsp_II_2k_TDMLocLoop,
       "fsp_II_2k_TDMClockType": fsp_II_2k_TDMClockType,
       "fsp_II_2k_TDMLocModuleInst1": fsp_II_2k_TDMLocModuleInst1,
       "fsp_II_2k_TDMLocModuleEnable1": fsp_II_2k_TDMLocModuleEnable1,
       "fsp_II_2k_TDMLocModuleRx1": fsp_II_2k_TDMLocModuleRx1,
       "fsp_II_2k_TDMLocModuleTx1": fsp_II_2k_TDMLocModuleTx1,
       "fsp_II_2k_TDMLocModuleRemoteData1": fsp_II_2k_TDMLocModuleRemoteData1,
       "fsp_II_2k_TDMLocModuleClockFrequency1": fsp_II_2k_TDMLocModuleClockFrequency1,
       "fsp_II_2k_TDMLocModuleClockError1": fsp_II_2k_TDMLocModuleClockError1,
       "fsp_II_2k_TDMLocModuleInst2": fsp_II_2k_TDMLocModuleInst2,
       "fsp_II_2k_TDMLocModuleEnable2": fsp_II_2k_TDMLocModuleEnable2,
       "fsp_II_2k_TDMLocModuleRx2": fsp_II_2k_TDMLocModuleRx2,
       "fsp_II_2k_TDMLocModuleTx2": fsp_II_2k_TDMLocModuleTx2,
       "fsp_II_2k_TDMLocModuleRemoteData2": fsp_II_2k_TDMLocModuleRemoteData2,
       "fsp_II_2k_TDMLocModuleClockFrequency2": fsp_II_2k_TDMLocModuleClockFrequency2,
       "fsp_II_2k_TDMLocModuleClockError2": fsp_II_2k_TDMLocModuleClockError2,
       "fsp_II_2k_TDMLocModuleInst3": fsp_II_2k_TDMLocModuleInst3,
       "fsp_II_2k_TDMLocModuleEnable3": fsp_II_2k_TDMLocModuleEnable3,
       "fsp_II_2k_TDMLocModuleRx3": fsp_II_2k_TDMLocModuleRx3,
       "fsp_II_2k_TDMLocModuleTx3": fsp_II_2k_TDMLocModuleTx3,
       "fsp_II_2k_TDMLocModuleRemoteData3": fsp_II_2k_TDMLocModuleRemoteData3,
       "fsp_II_2k_TDMLocModuleClockFrequency3": fsp_II_2k_TDMLocModuleClockFrequency3,
       "fsp_II_2k_TDMLocModuleClockError3": fsp_II_2k_TDMLocModuleClockError3,
       "fsp_II_2k_TDMLocModuleInst4": fsp_II_2k_TDMLocModuleInst4,
       "fsp_II_2k_TDMLocModuleEnable4": fsp_II_2k_TDMLocModuleEnable4,
       "fsp_II_2k_TDMLocModuleRx4": fsp_II_2k_TDMLocModuleRx4,
       "fsp_II_2k_TDMLocModuleTx4": fsp_II_2k_TDMLocModuleTx4,
       "fsp_II_2k_TDMLocModuleRemoteData4": fsp_II_2k_TDMLocModuleRemoteData4,
       "fsp_II_2k_TDMLocModuleClockFrequency4": fsp_II_2k_TDMLocModuleClockFrequency4,
       "fsp_II_2k_TDMLocModuleClockError4": fsp_II_2k_TDMLocModuleClockError4,
       "fsp_II_2k_TDMLocalConnector": fsp_II_2k_TDMLocalConnector,
       "fsp_II_2k_TDMLocalLaserType": fsp_II_2k_TDMLocalLaserType,
       "fsp_II_2k_TDMRemoteConnector": fsp_II_2k_TDMRemoteConnector,
       "fsp_II_2k_TDMRemoteLaserType": fsp_II_2k_TDMRemoteLaserType,
       "fsp_II_2k_TDMConverterType": fsp_II_2k_TDMConverterType,
       "fsp_II_2k_TDMClockRecovery": fsp_II_2k_TDMClockRecovery,
       "fsp_II_2k_TDMDataRateRange": fsp_II_2k_TDMDataRateRange,
       "fsp_II_2k_TDMClockFreqRange": fsp_II_2k_TDMClockFreqRange,
       "fsp_II_2k_TDMChannelNumber": fsp_II_2k_TDMChannelNumber,
       "fsp_II_2k_TDMLocModuleInst5": fsp_II_2k_TDMLocModuleInst5,
       "fsp_II_2k_TDMLocModuleEnable5": fsp_II_2k_TDMLocModuleEnable5,
       "fsp_II_2k_TDMLocModuleRx5": fsp_II_2k_TDMLocModuleRx5,
       "fsp_II_2k_TDMLocModuleTx5": fsp_II_2k_TDMLocModuleTx5,
       "fsp_II_2k_TDMLocModuleRemoteData5": fsp_II_2k_TDMLocModuleRemoteData5,
       "fsp_II_2k_TDMLocModuleClockFrequency5": fsp_II_2k_TDMLocModuleClockFrequency5,
       "fsp_II_2k_TDMLocModuleClockError5": fsp_II_2k_TDMLocModuleClockError5,
       "fsp_II_2k_TDMLocModuleInst6": fsp_II_2k_TDMLocModuleInst6,
       "fsp_II_2k_TDMLocModuleEnable6": fsp_II_2k_TDMLocModuleEnable6,
       "fsp_II_2k_TDMLocModuleRx6": fsp_II_2k_TDMLocModuleRx6,
       "fsp_II_2k_TDMLocModuleTx6": fsp_II_2k_TDMLocModuleTx6,
       "fsp_II_2k_TDMLocModuleRemoteData6": fsp_II_2k_TDMLocModuleRemoteData6,
       "fsp_II_2k_TDMLocModuleClockFrequency6": fsp_II_2k_TDMLocModuleClockFrequency6,
       "fsp_II_2k_TDMLocModuleClockError6": fsp_II_2k_TDMLocModuleClockError6,
       "fsp_II_2k_TDMLocModuleInst7": fsp_II_2k_TDMLocModuleInst7,
       "fsp_II_2k_TDMLocModuleEnable7": fsp_II_2k_TDMLocModuleEnable7,
       "fsp_II_2k_TDMLocModuleRx7": fsp_II_2k_TDMLocModuleRx7,
       "fsp_II_2k_TDMLocModuleTx7": fsp_II_2k_TDMLocModuleTx7,
       "fsp_II_2k_TDMLocModuleRemoteData7": fsp_II_2k_TDMLocModuleRemoteData7,
       "fsp_II_2k_TDMLocModuleClockFrequency7": fsp_II_2k_TDMLocModuleClockFrequency7,
       "fsp_II_2k_TDMLocModuleClockError7": fsp_II_2k_TDMLocModuleClockError7,
       "fsp_II_2k_TDMLocModuleInst8": fsp_II_2k_TDMLocModuleInst8,
       "fsp_II_2k_TDMLocModuleEnable8": fsp_II_2k_TDMLocModuleEnable8,
       "fsp_II_2k_TDMLocModuleRx8": fsp_II_2k_TDMLocModuleRx8,
       "fsp_II_2k_TDMLocModuleTx8": fsp_II_2k_TDMLocModuleTx8,
       "fsp_II_2k_TDMLocModuleRemoteData8": fsp_II_2k_TDMLocModuleRemoteData8,
       "fsp_II_2k_TDMLocModuleClockFrequency8": fsp_II_2k_TDMLocModuleClockFrequency8,
       "fsp_II_2k_TDMLocModuleClockError8": fsp_II_2k_TDMLocModuleClockError8,
       "fsp_II_2k_MUX_DMX": fsp_II_2k_MUX_DMX,
       "fsp_II_2k_MUX_DMX_Table": fsp_II_2k_MUX_DMX_Table,
       "fsp_II_2k_MUX_DMX_Entry": fsp_II_2k_MUX_DMX_Entry,
       "fsp_II_2k_MUX_DMX_Number": fsp_II_2k_MUX_DMX_Number,
       "fsp_II_2k_MUX_DMX_WDMType": fsp_II_2k_MUX_DMX_WDMType,
       "fsp_II_2k_MUX_DMX_Scheme": fsp_II_2k_MUX_DMX_Scheme,
       "fsp_II_2k_MUX_DMX_ChannelRange": fsp_II_2k_MUX_DMX_ChannelRange,
       "fsp_II_2k_MUX_DMX_Connector": fsp_II_2k_MUX_DMX_Connector,
       "fsp_II_2k_MUX_DMX_UpgradePort": fsp_II_2k_MUX_DMX_UpgradePort,
       "fsp_II_2k_BSM": fsp_II_2k_BSM,
       "fsp_II_2k_BSM_Table": fsp_II_2k_BSM_Table,
       "fsp_II_2k_BSM_Entry": fsp_II_2k_BSM_Entry,
       "fsp_II_2k_BSM_Number": fsp_II_2k_BSM_Number,
       "fsp_II_2k_BSM_Scheme": fsp_II_2k_BSM_Scheme,
       "fsp_II_2k_BSM_BandRange": fsp_II_2k_BSM_BandRange,
       "fsp_II_2k_BSM_ConnectorType": fsp_II_2k_BSM_ConnectorType,
       "fsp_II_2k_Trap": fsp_II_2k_Trap,
       "fsp_II_2k_HardwareAdded": fsp_II_2k_HardwareAdded,
       "fsp_II_2k_HardwareDeleted": fsp_II_2k_HardwareDeleted,
       "fsp_II_2k_PSNotFail": fsp_II_2k_PSNotFail,
       "fsp_II_2k_PSFail": fsp_II_2k_PSFail,
       "fsp_II_2k_FanNotFail": fsp_II_2k_FanNotFail,
       "fsp_II_2k_FanFail": fsp_II_2k_FanFail,
       "fsp_II_2k_BusNotFail": fsp_II_2k_BusNotFail,
       "fsp_II_2k_BusFail": fsp_II_2k_BusFail,
       "fsp_II_2k_ConfigMismatch": fsp_II_2k_ConfigMismatch,
       "fsp_II_2k_RxLocOn": fsp_II_2k_RxLocOn,
       "fsp_II_2k_RxLocOff": fsp_II_2k_RxLocOff,
       "fsp_II_2k_TxLocOn": fsp_II_2k_TxLocOn,
       "fsp_II_2k_TxLocOff": fsp_II_2k_TxLocOff,
       "fsp_II_2k_RxRemOn": fsp_II_2k_RxRemOn,
       "fsp_II_2k_RxRemOff": fsp_II_2k_RxRemOff,
       "fsp_II_2k_TxRemOn": fsp_II_2k_TxRemOn,
       "fsp_II_2k_TxRemOff": fsp_II_2k_TxRemOff,
       "fsp_II_2k_RxRem2On": fsp_II_2k_RxRem2On,
       "fsp_II_2k_RxRem2Off": fsp_II_2k_RxRem2Off,
       "fsp_II_2k_TxRem2On": fsp_II_2k_TxRem2On,
       "fsp_II_2k_TxRem2Off": fsp_II_2k_TxRem2Off,
       "fsp_II_2k_ClockNoFail": fsp_II_2k_ClockNoFail,
       "fsp_II_2k_ClockFail": fsp_II_2k_ClockFail,
       "fsp_II_2k_ClockChangeFrequency": fsp_II_2k_ClockChangeFrequency,
       "fsp_II_2k_LocLoopOn": fsp_II_2k_LocLoopOn,
       "fsp_II_2k_LocLoopOff": fsp_II_2k_LocLoopOff,
       "fsp_II_2k_RemLoopOn": fsp_II_2k_RemLoopOn,
       "fsp_II_2k_RemLoopOff": fsp_II_2k_RemLoopOff,
       "fsp_II_2k_switchReferenceLaserOn": fsp_II_2k_switchReferenceLaserOn,
       "fsp_II_2k_switchReferenceLaserOff": fsp_II_2k_switchReferenceLaserOff,
       "fsp_II_2k_switchToA": fsp_II_2k_switchToA,
       "fsp_II_2k_switchToB": fsp_II_2k_switchToB,
       "fsp_II_2k_switchAutomatic": fsp_II_2k_switchAutomatic,
       "fsp_II_2k_switchLocked": fsp_II_2k_switchLocked,
       "fsp_II_2k_switchLineAavail": fsp_II_2k_switchLineAavail,
       "fsp_II_2k_switchLineANotAvail": fsp_II_2k_switchLineANotAvail,
       "fsp_II_2k_switchLineBavail": fsp_II_2k_switchLineBavail,
       "fsp_II_2k_switchLineBNotAvail": fsp_II_2k_switchLineBNotAvail,
       "fsp_II_2k_repeatedMessage": fsp_II_2k_repeatedMessage,
       "fsp_II_2k_INNCDown": fsp_II_2k_INNCDown,
       "fsp_II_2k_INNCUp": fsp_II_2k_INNCUp,
       "fsp_II_2k_switchAutoLaserShutdownOn": fsp_II_2k_switchAutoLaserShutdownOn,
       "fsp_II_2k_switchAutoLaserShutdownOff": fsp_II_2k_switchAutoLaserShutdownOff,
       "fsp_II_2k_NEMIAuthFail": fsp_II_2k_NEMIAuthFail,
       "fsp_II_2k_EthernetPortEnable": fsp_II_2k_EthernetPortEnable,
       "fsp_II_2k_EthernetPortDisable": fsp_II_2k_EthernetPortDisable,
       "fsp_II_2k_EthernetPortPartitioned": fsp_II_2k_EthernetPortPartitioned,
       "fsp_II_2k_EthernetPortNotPartitioned": fsp_II_2k_EthernetPortNotPartitioned,
       "fsp_II_2k_EthernetPortLinkPulses": fsp_II_2k_EthernetPortLinkPulses,
       "fsp_II_2k_EthernetPortNoLinkPulses": fsp_II_2k_EthernetPortNoLinkPulses,
       "fsp_II_2k_TDMRemoteSyncLoss": fsp_II_2k_TDMRemoteSyncLoss,
       "fsp_II_2k_TDMRemoteSync": fsp_II_2k_TDMRemoteSync,
       "fsp_II_2k_TDMLocModuleEnabled1": fsp_II_2k_TDMLocModuleEnabled1,
       "fsp_II_2k_TDMLocModuleDisable1": fsp_II_2k_TDMLocModuleDisable1,
       "fsp_II_2k_TDMLocModuleEnabled2": fsp_II_2k_TDMLocModuleEnabled2,
       "fsp_II_2k_TDMLocModuleDisable2": fsp_II_2k_TDMLocModuleDisable2,
       "fsp_II_2k_TDMLocModuleEnabled3": fsp_II_2k_TDMLocModuleEnabled3,
       "fsp_II_2k_TDMLocModuleDisable3": fsp_II_2k_TDMLocModuleDisable3,
       "fsp_II_2k_TDMLocModuleEnabled4": fsp_II_2k_TDMLocModuleEnabled4,
       "fsp_II_2k_TDMLocModuleDisable4": fsp_II_2k_TDMLocModuleDisable4,
       "fsp_II_2k_TDMLocModuleEnabled5": fsp_II_2k_TDMLocModuleEnabled5,
       "fsp_II_2k_TDMLocModuleDisable5": fsp_II_2k_TDMLocModuleDisable5,
       "fsp_II_2k_TDMLocModuleEnabled6": fsp_II_2k_TDMLocModuleEnabled6,
       "fsp_II_2k_TDMLocModuleDisable6": fsp_II_2k_TDMLocModuleDisable6,
       "fsp_II_2k_TDMLocModuleEnabled7": fsp_II_2k_TDMLocModuleEnabled7,
       "fsp_II_2k_TDMLocModuleDisable7": fsp_II_2k_TDMLocModuleDisable7,
       "fsp_II_2k_TDMLocModuleEnabled8": fsp_II_2k_TDMLocModuleEnabled8,
       "fsp_II_2k_TDMLocModuleDisable8": fsp_II_2k_TDMLocModuleDisable8,
       "fsp_II_2k_TDMLocModuleRxOn1": fsp_II_2k_TDMLocModuleRxOn1,
       "fsp_II_2k_TDMLocModuleRxOff1": fsp_II_2k_TDMLocModuleRxOff1,
       "fsp_II_2k_TDMLocModuleRxOn2": fsp_II_2k_TDMLocModuleRxOn2,
       "fsp_II_2k_TDMLocModuleRxOff2": fsp_II_2k_TDMLocModuleRxOff2,
       "fsp_II_2k_TDMLocModuleRxOn3": fsp_II_2k_TDMLocModuleRxOn3,
       "fsp_II_2k_TDMLocModuleRxOff3": fsp_II_2k_TDMLocModuleRxOff3,
       "fsp_II_2k_TDMLocModuleRxOn4": fsp_II_2k_TDMLocModuleRxOn4,
       "fsp_II_2k_TDMLocModuleRxOff4": fsp_II_2k_TDMLocModuleRxOff4,
       "fsp_II_2k_TDMLocModuleRxOn5": fsp_II_2k_TDMLocModuleRxOn5,
       "fsp_II_2k_TDMLocModuleRxOff5": fsp_II_2k_TDMLocModuleRxOff5,
       "fsp_II_2k_TDMLocModuleRxOn6": fsp_II_2k_TDMLocModuleRxOn6,
       "fsp_II_2k_TDMLocModuleRxOff6": fsp_II_2k_TDMLocModuleRxOff6,
       "fsp_II_2k_TDMLocModuleRxOn7": fsp_II_2k_TDMLocModuleRxOn7,
       "fsp_II_2k_TDMLocModuleRxOff7": fsp_II_2k_TDMLocModuleRxOff7,
       "fsp_II_2k_TDMLocModuleRxOn8": fsp_II_2k_TDMLocModuleRxOn8,
       "fsp_II_2k_TDMLocModuleRxOff8": fsp_II_2k_TDMLocModuleRxOff8,
       "fsp_II_2k_TDMLocModuleData1": fsp_II_2k_TDMLocModuleData1,
       "fsp_II_2k_TDMLocModuleNoData1": fsp_II_2k_TDMLocModuleNoData1,
       "fsp_II_2k_TDMLocModuleData2": fsp_II_2k_TDMLocModuleData2,
       "fsp_II_2k_TDMLocModuleNoData2": fsp_II_2k_TDMLocModuleNoData2,
       "fsp_II_2k_TDMLocModuleData3": fsp_II_2k_TDMLocModuleData3,
       "fsp_II_2k_TDMLocModuleNoData3": fsp_II_2k_TDMLocModuleNoData3,
       "fsp_II_2k_TDMLocModuleData4": fsp_II_2k_TDMLocModuleData4,
       "fsp_II_2k_TDMLocModuleNoData4": fsp_II_2k_TDMLocModuleNoData4,
       "fsp_II_2k_TDMLocModuleData5": fsp_II_2k_TDMLocModuleData5,
       "fsp_II_2k_TDMLocModuleNoData5": fsp_II_2k_TDMLocModuleNoData5,
       "fsp_II_2k_TDMLocModuleData6": fsp_II_2k_TDMLocModuleData6,
       "fsp_II_2k_TDMLocModuleNoData6": fsp_II_2k_TDMLocModuleNoData6,
       "fsp_II_2k_TDMLocModuleData7": fsp_II_2k_TDMLocModuleData7,
       "fsp_II_2k_TDMLocModuleNoData7": fsp_II_2k_TDMLocModuleNoData7,
       "fsp_II_2k_TDMLocModuleData8": fsp_II_2k_TDMLocModuleData8,
       "fsp_II_2k_TDMLocModuleNoData8": fsp_II_2k_TDMLocModuleNoData8,
       "fsp_II_2k_TDMLocModuleClockFail1": fsp_II_2k_TDMLocModuleClockFail1,
       "fsp_II_2k_TDMLocModuleClockNoFail1": fsp_II_2k_TDMLocModuleClockNoFail1,
       "fsp_II_2k_TDMLocModuleClockFail2": fsp_II_2k_TDMLocModuleClockFail2,
       "fsp_II_2k_TDMLocModuleClockNoFail2": fsp_II_2k_TDMLocModuleClockNoFail2,
       "fsp_II_2k_TDMLocModuleClockFail3": fsp_II_2k_TDMLocModuleClockFail3,
       "fsp_II_2k_TDMLocModuleClockNoFail3": fsp_II_2k_TDMLocModuleClockNoFail3,
       "fsp_II_2k_TDMLocModuleClockFail4": fsp_II_2k_TDMLocModuleClockFail4,
       "fsp_II_2k_TDMLocModuleClockNoFail4": fsp_II_2k_TDMLocModuleClockNoFail4,
       "fsp_II_2k_TDMLocModuleClockFail5": fsp_II_2k_TDMLocModuleClockFail5,
       "fsp_II_2k_TDMLocModuleClockNoFail5": fsp_II_2k_TDMLocModuleClockNoFail5,
       "fsp_II_2k_TDMLocModuleClockFail6": fsp_II_2k_TDMLocModuleClockFail6,
       "fsp_II_2k_TDMLocModuleClockNoFail6": fsp_II_2k_TDMLocModuleClockNoFail6,
       "fsp_II_2k_TDMLocModuleClockFail7": fsp_II_2k_TDMLocModuleClockFail7,
       "fsp_II_2k_TDMLocModuleClockNoFail7": fsp_II_2k_TDMLocModuleClockNoFail7,
       "fsp_II_2k_TDMLocModuleClockFail8": fsp_II_2k_TDMLocModuleClockFail8,
       "fsp_II_2k_TDMLocModuleClockNoFail8": fsp_II_2k_TDMLocModuleClockNoFail8,
       "fsp_II_2k_TDMLocModuleClockChange1": fsp_II_2k_TDMLocModuleClockChange1,
       "fsp_II_2k_TDMLocModuleClockChange2": fsp_II_2k_TDMLocModuleClockChange2,
       "fsp_II_2k_TDMLocModuleClockChange3": fsp_II_2k_TDMLocModuleClockChange3,
       "fsp_II_2k_TDMLocModuleClockChange4": fsp_II_2k_TDMLocModuleClockChange4,
       "fsp_II_2k_TDMLocModuleClockChange5": fsp_II_2k_TDMLocModuleClockChange5,
       "fsp_II_2k_TDMLocModuleClockChange6": fsp_II_2k_TDMLocModuleClockChange6,
       "fsp_II_2k_TDMLocModuleClockChange7": fsp_II_2k_TDMLocModuleClockChange7,
       "fsp_II_2k_TDMLocModuleClockChange8": fsp_II_2k_TDMLocModuleClockChange8,
       "fsp_II_2k_RemoteClockNoSync": fsp_II_2k_RemoteClockNoSync,
       "fsp_II_2k_RemoteClockSync": fsp_II_2k_RemoteClockSync,
       "fsp_II_2k_RemoteClock2NoSync": fsp_II_2k_RemoteClock2NoSync,
       "fsp_II_2k_RemoteClock2Sync": fsp_II_2k_RemoteClock2Sync,
       "fsp_II_2k_RegeneratorModeOn": fsp_II_2k_RegeneratorModeOn,
       "fsp_II_2k_RegeneratorModeOff": fsp_II_2k_RegeneratorModeOff,
       "fsp_II_2k_RSM_OSC_OSCOn": fsp_II_2k_RSM_OSC_OSCOn,
       "fsp_II_2k_RSM_OSC_OSCOff": fsp_II_2k_RSM_OSC_OSCOff,
       "fsp_II_2k_EthernetPortSpeed10": fsp_II_2k_EthernetPortSpeed10,
       "fsp_II_2k_EthernetPortSpeed100": fsp_II_2k_EthernetPortSpeed100,
       "fsp_II_2k_EthernetPortDuplexHalf": fsp_II_2k_EthernetPortDuplexHalf,
       "fsp_II_2k_EthernetPortDuplexFull": fsp_II_2k_EthernetPortDuplexFull,
       "fsp_II_2k_EthernetPortAutonegotiationOn": fsp_II_2k_EthernetPortAutonegotiationOn,
       "fsp_II_2k_EthernetPortAutonegotiationOff": fsp_II_2k_EthernetPortAutonegotiationOff,
       "fsp_II_2k_EthernetPortPolarityPositive": fsp_II_2k_EthernetPortPolarityPositive,
       "fsp_II_2k_EthernetPortPolarityNegative": fsp_II_2k_EthernetPortPolarityNegative,
       "fsp_II_2k_HotStandby_Change2LineA": fsp_II_2k_HotStandby_Change2LineA,
       "fsp_II_2k_HotStandby_Change2LineB": fsp_II_2k_HotStandby_Change2LineB,
       "fsp_II_2k_HotStandby_Locked": fsp_II_2k_HotStandby_Locked,
       "fsp_II_2k_HotStandby_Automatic": fsp_II_2k_HotStandby_Automatic}
)
