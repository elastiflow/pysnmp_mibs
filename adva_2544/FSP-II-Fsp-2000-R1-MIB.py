# SNMP MIB module (FSP-II-Fsp-2000-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FSP-II-Fsp-2000-R1-MIB.mib
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-MainTrapsinkNumber"),
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-MainLogfileNumber"),
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
        *(("snmp-agent", 1),
          ("login-cmd", 2),
          ("su-cmd", 3),
          ("no-fail", 4))
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
_Fsp_II_2k_MainLastAuthFailDescr_Type = DisplayString
_Fsp_II_2k_MainLastAuthFailDescr_Object = MibScalar
fsp_II_2k_MainLastAuthFailDescr = _Fsp_II_2k_MainLastAuthFailDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 16),
    _Fsp_II_2k_MainLastAuthFailDescr_Type()
)
fsp_II_2k_MainLastAuthFailDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_MainLastAuthFailDescr.setStatus("mandatory")
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_SlotEntry.setStatus("mandatory")


class _Fsp_II_2k_SlotNumber_Type(Integer32):
    """Custom type fsp_II_2k_SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_SlotNumber_Type.__name__ = "Integer32"
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
            *(1,
              2,
              3,
              5,
              7,
              10,
              13,
              14,
              18,
              19,
              20,
              21,
              24,
              25,
              32,
              33,
              39,
              42,
              43,
              64,
              66,
              67,
              68,
              69,
              73,
              74,
              136,
              137,
              138,
              139,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fsp-II-2k-Converter", 1),
          ("fsp-I-Converter", 2),
          ("fsp-I-EthernetConverter", 3),
          ("fsp-II-2k-2-5GBitConverter", 5),
          ("fsp-II-2k-TRL-Converter", 7),
          ("fsp-II-2k-4PortTDMCard", 10),
          ("fsp-II-2k-HotStandby-Converter", 13),
          ("fsp-II-2k-4PortTDMCard-MC", 14),
          ("fsp-II-2k-EDFA", 18),
          ("fsp-II-2k-ConverterEWS", 19),
          ("fsp-II-2k-8PortTDMCard-MC", 20),
          ("fsp-II-2k-2PortTDMCard-MC", 21),
          ("fsp-II-2k-ConverterEWS-PL", 24),
          ("fsp-II-2k-2PortTDMCard-MC-PL", 25),
          ("nemi", 32),
          ("demi", 33),
          ("fsp-II-2k-EthHubCard", 39),
          ("nemi-v2", 42),
          ("demi-v2", 43),
          ("switch", 64),
          ("fsp-II-2k-RSM-OSC", 66),
          ("fsp-II-2k-RSM", 67),
          ("fsp-II-2k-OSC-single", 68),
          ("fsp-II-2k-SingleFiberSwitch", 69),
          ("fsp-II-2k-RSM-OLM", 73),
          ("fsp-II-2k-RSM-OLM-OSC", 74),
          ("fsp-II-2k-MUX-DMX", 136),
          ("fsp-II-2k-MUX", 137),
          ("fsp-II-2k-DMX", 138),
          ("fsp-II-2k-BSM", 139),
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-PSNumber"),
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-FanNumber"),
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-ConverterNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_ConverterEntry.setStatus("mandatory")


class _Fsp_II_2k_ConverterNumber_Type(Integer32):
    """Custom type fsp_II_2k_ConverterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_ConverterNumber_Type.__name__ = "Integer32"
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
              130,
              250,
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
          ("multiClock2HS", 130),
          ("genericClock", 250),
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
_Fsp_II_2k_SupDataRateTransp_Type = DisplayString
_Fsp_II_2k_SupDataRateTransp_Object = MibTableColumn
fsp_II_2k_SupDataRateTransp = _Fsp_II_2k_SupDataRateTransp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 24),
    _Fsp_II_2k_SupDataRateTransp_Type()
)
fsp_II_2k_SupDataRateTransp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SupDataRateTransp.setStatus("mandatory")
_Fsp_II_2k_SupDataRateClocked_Type = DisplayString
_Fsp_II_2k_SupDataRateClocked_Object = MibTableColumn
fsp_II_2k_SupDataRateClocked = _Fsp_II_2k_SupDataRateClocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 25),
    _Fsp_II_2k_SupDataRateClocked_Type()
)
fsp_II_2k_SupDataRateClocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SupDataRateClocked.setStatus("mandatory")


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
_Fsp_II_2k_ClockGenericTable_Object = MibTable
fsp_II_2k_ClockGenericTable = _Fsp_II_2k_ClockGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockGenericTable.setStatus("mandatory")
_Fsp_II_2k_ClockGenericEntry_Object = MibTableRow
fsp_II_2k_ClockGenericEntry = _Fsp_II_2k_ClockGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 2, 1)
)
fsp_II_2k_ClockGenericEntry.setIndexNames(
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-ConverterNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockGenericEntry.setStatus("mandatory")


class _Fsp_II_2k_ClockGenericFreq_Type(Integer32):
    """Custom type fsp_II_2k_ClockGenericFreq based on Integer32"""
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
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mb125", 2),
          ("mb155", 3),
          ("mb200", 4),
          ("mb266", 5),
          ("mb270", 6),
          ("mb622", 7),
          ("mb1062", 8),
          ("mb1244", 9),
          ("mb1250", 10),
          ("mb2125", 11),
          ("mb2488", 12),
          ("mb2500", 13),
          ("mb9953", 14),
          ("mb10312", 15),
          ("mb1062cl", 25),
          ("mb2125cl", 26))
    )


_Fsp_II_2k_ClockGenericFreq_Type.__name__ = "Integer32"
_Fsp_II_2k_ClockGenericFreq_Object = MibTableColumn
fsp_II_2k_ClockGenericFreq = _Fsp_II_2k_ClockGenericFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 2, 1, 1),
    _Fsp_II_2k_ClockGenericFreq_Type()
)
fsp_II_2k_ClockGenericFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ClockGenericFreq.setStatus("mandatory")
_Fsp_II_2k_ClockGenericType_Type = Integer32
_Fsp_II_2k_ClockGenericType_Object = MibTableColumn
fsp_II_2k_ClockGenericType = _Fsp_II_2k_ClockGenericType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 2, 1, 2),
    _Fsp_II_2k_ClockGenericType_Type()
)
fsp_II_2k_ClockGenericType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_ClockGenericType.setStatus("mandatory")
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SwitchNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchEntry.setStatus("mandatory")


class _Fsp_II_2k_SwitchNumber_Type(Integer32):
    """Custom type fsp_II_2k_SwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_SwitchNumber_Type.__name__ = "Integer32"
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


class _Fsp_II_2k_SwitchALS_Type(Integer32):
    """Custom type fsp_II_2k_SwitchALS based on Integer32"""
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


_Fsp_II_2k_SwitchALS_Type.__name__ = "Integer32"
_Fsp_II_2k_SwitchALS_Object = MibTableColumn
fsp_II_2k_SwitchALS = _Fsp_II_2k_SwitchALS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 7),
    _Fsp_II_2k_SwitchALS_Type()
)
fsp_II_2k_SwitchALS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_SwitchALS.setStatus("mandatory")
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-RSM-Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_Entry.setStatus("mandatory")


class _Fsp_II_2k_RSM_Number_Type(Integer32):
    """Custom type fsp_II_2k_RSM_Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_RSM_Number_Type.__name__ = "Integer32"
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-OSC-Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_OSC_Entry.setStatus("mandatory")


class _Fsp_II_2k_OSC_Number_Type(Integer32):
    """Custom type fsp_II_2k_OSC_Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_OSC_Number_Type.__name__ = "Integer32"
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
_Fsp_II_2k_OLM_Table_Object = MibTable
fsp_II_2k_OLM_Table = _Fsp_II_2k_OLM_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3)
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_Table.setStatus("mandatory")
_Fsp_II_2k_OLM_Entry_Object = MibTableRow
fsp_II_2k_OLM_Entry = _Fsp_II_2k_OLM_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1)
)
fsp_II_2k_OLM_Entry.setIndexNames(
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-OLM-Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_Entry.setStatus("mandatory")


class _Fsp_II_2k_OLM_Number_Type(Integer32):
    """Custom type fsp_II_2k_OLM_Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_OLM_Number_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_Number_Object = MibTableColumn
fsp_II_2k_OLM_Number = _Fsp_II_2k_OLM_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 1),
    _Fsp_II_2k_OLM_Number_Type()
)
fsp_II_2k_OLM_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_Number.setStatus("mandatory")


class _Fsp_II_2k_OLM_SwitchOver_Type(Integer32):
    """Custom type fsp_II_2k_OLM_SwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oip", 1),
          ("loss", 2))
    )


_Fsp_II_2k_OLM_SwitchOver_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_SwitchOver_Object = MibTableColumn
fsp_II_2k_OLM_SwitchOver = _Fsp_II_2k_OLM_SwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 2),
    _Fsp_II_2k_OLM_SwitchOver_Type()
)
fsp_II_2k_OLM_SwitchOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_SwitchOver.setStatus("mandatory")


class _Fsp_II_2k_OLM_Threshold_Type(Integer32):
    """Custom type fsp_II_2k_OLM_Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Fsp_II_2k_OLM_Threshold_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_Threshold_Object = MibTableColumn
fsp_II_2k_OLM_Threshold = _Fsp_II_2k_OLM_Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 3),
    _Fsp_II_2k_OLM_Threshold_Type()
)
fsp_II_2k_OLM_Threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_Threshold.setStatus("mandatory")


class _Fsp_II_2k_OLM_Hysteresis_Type(Integer32):
    """Custom type fsp_II_2k_OLM_Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Fsp_II_2k_OLM_Hysteresis_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_Hysteresis_Object = MibTableColumn
fsp_II_2k_OLM_Hysteresis = _Fsp_II_2k_OLM_Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 4),
    _Fsp_II_2k_OLM_Hysteresis_Type()
)
fsp_II_2k_OLM_Hysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_Hysteresis.setStatus("mandatory")


class _Fsp_II_2k_OLM_HighAlarmLevel_Type(Integer32):
    """Custom type fsp_II_2k_OLM_HighAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Fsp_II_2k_OLM_HighAlarmLevel_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_HighAlarmLevel_Object = MibTableColumn
fsp_II_2k_OLM_HighAlarmLevel = _Fsp_II_2k_OLM_HighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 5),
    _Fsp_II_2k_OLM_HighAlarmLevel_Type()
)
fsp_II_2k_OLM_HighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_HighAlarmLevel.setStatus("mandatory")


class _Fsp_II_2k_OLM_LowAlarmLevel_Type(Integer32):
    """Custom type fsp_II_2k_OLM_LowAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Fsp_II_2k_OLM_LowAlarmLevel_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_LowAlarmLevel_Object = MibTableColumn
fsp_II_2k_OLM_LowAlarmLevel = _Fsp_II_2k_OLM_LowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 6),
    _Fsp_II_2k_OLM_LowAlarmLevel_Type()
)
fsp_II_2k_OLM_LowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LowAlarmLevel.setStatus("mandatory")


class _Fsp_II_2k_OLM_LineAttAT_Type(Integer32):
    """Custom type fsp_II_2k_OLM_LineAttAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
        ValueRangeConstraint(999, 999),
    )


_Fsp_II_2k_OLM_LineAttAT_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_LineAttAT_Object = MibTableColumn
fsp_II_2k_OLM_LineAttAT = _Fsp_II_2k_OLM_LineAttAT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 7),
    _Fsp_II_2k_OLM_LineAttAT_Type()
)
fsp_II_2k_OLM_LineAttAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttAT.setStatus("mandatory")


class _Fsp_II_2k_OLM_LineAttAR_Type(Integer32):
    """Custom type fsp_II_2k_OLM_LineAttAR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Fsp_II_2k_OLM_LineAttAR_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_LineAttAR_Object = MibTableColumn
fsp_II_2k_OLM_LineAttAR = _Fsp_II_2k_OLM_LineAttAR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 8),
    _Fsp_II_2k_OLM_LineAttAR_Type()
)
fsp_II_2k_OLM_LineAttAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttAR.setStatus("mandatory")


class _Fsp_II_2k_OLM_LineAttBT_Type(Integer32):
    """Custom type fsp_II_2k_OLM_LineAttBT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Fsp_II_2k_OLM_LineAttBT_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_LineAttBT_Object = MibTableColumn
fsp_II_2k_OLM_LineAttBT = _Fsp_II_2k_OLM_LineAttBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 9),
    _Fsp_II_2k_OLM_LineAttBT_Type()
)
fsp_II_2k_OLM_LineAttBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBT.setStatus("mandatory")


class _Fsp_II_2k_OLM_LineAttBR_Type(Integer32):
    """Custom type fsp_II_2k_OLM_LineAttBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Fsp_II_2k_OLM_LineAttBR_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_LineAttBR_Object = MibTableColumn
fsp_II_2k_OLM_LineAttBR = _Fsp_II_2k_OLM_LineAttBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 10),
    _Fsp_II_2k_OLM_LineAttBR_Type()
)
fsp_II_2k_OLM_LineAttBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBR.setStatus("mandatory")


class _Fsp_II_2k_OLM_OIP_StateA_Type(Integer32):
    """Custom type fsp_II_2k_OLM_OIP_StateA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_Fsp_II_2k_OLM_OIP_StateA_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_OIP_StateA_Object = MibTableColumn
fsp_II_2k_OLM_OIP_StateA = _Fsp_II_2k_OLM_OIP_StateA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 11),
    _Fsp_II_2k_OLM_OIP_StateA_Type()
)
fsp_II_2k_OLM_OIP_StateA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_OIP_StateA.setStatus("mandatory")


class _Fsp_II_2k_OLM_OIP_StateB_Type(Integer32):
    """Custom type fsp_II_2k_OLM_OIP_StateB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_Fsp_II_2k_OLM_OIP_StateB_Type.__name__ = "Integer32"
_Fsp_II_2k_OLM_OIP_StateB_Object = MibTableColumn
fsp_II_2k_OLM_OIP_StateB = _Fsp_II_2k_OLM_OIP_StateB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 11, 3, 1, 12),
    _Fsp_II_2k_OLM_OIP_StateB_Type()
)
fsp_II_2k_OLM_OIP_StateB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_OIP_StateB.setStatus("mandatory")
_Fsp_II_2k_EthHub_ObjectIdentity = ObjectIdentity
fsp_II_2k_EthHub = _Fsp_II_2k_EthHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14)
)
_Fsp_II_2k_EthHubTable_Object = MibTable
fsp_II_2k_EthHubTable = _Fsp_II_2k_EthHubTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubTable.setStatus("mandatory")
_Fsp_II_2k_EthHubEntry_Object = MibTableRow
fsp_II_2k_EthHubEntry = _Fsp_II_2k_EthHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1)
)
fsp_II_2k_EthHubEntry.setIndexNames(
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-EthHubNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubEntry.setStatus("mandatory")


class _Fsp_II_2k_EthHubNumber_Type(Integer32):
    """Custom type fsp_II_2k_EthHubNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_EthHubNumber_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubNumber_Object = MibTableColumn
fsp_II_2k_EthHubNumber = _Fsp_II_2k_EthHubNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 1),
    _Fsp_II_2k_EthHubNumber_Type()
)
fsp_II_2k_EthHubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubNumber.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortEnable1_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortEnable1 based on Integer32"""
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


_Fsp_II_2k_EthHubPortEnable1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortEnable1_Object = MibTableColumn
fsp_II_2k_EthHubPortEnable1 = _Fsp_II_2k_EthHubPortEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 10),
    _Fsp_II_2k_EthHubPortEnable1_Type()
)
fsp_II_2k_EthHubPortEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortEnable1.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPartStatus1_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPartStatus1 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPartStatus1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPartStatus1_Object = MibTableColumn
fsp_II_2k_EthHubPortPartStatus1 = _Fsp_II_2k_EthHubPortPartStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 11),
    _Fsp_II_2k_EthHubPortPartStatus1_Type()
)
fsp_II_2k_EthHubPortPartStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPartStatus1.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortLinkStatus1_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortLinkStatus1 based on Integer32"""
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


_Fsp_II_2k_EthHubPortLinkStatus1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortLinkStatus1_Object = MibTableColumn
fsp_II_2k_EthHubPortLinkStatus1 = _Fsp_II_2k_EthHubPortLinkStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 12),
    _Fsp_II_2k_EthHubPortLinkStatus1_Type()
)
fsp_II_2k_EthHubPortLinkStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortLinkStatus1.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPolarity1_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPolarity1 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPolarity1_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPolarity1_Object = MibTableColumn
fsp_II_2k_EthHubPortPolarity1 = _Fsp_II_2k_EthHubPortPolarity1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 13),
    _Fsp_II_2k_EthHubPortPolarity1_Type()
)
fsp_II_2k_EthHubPortPolarity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPolarity1.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortEnable2_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortEnable2 based on Integer32"""
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


_Fsp_II_2k_EthHubPortEnable2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortEnable2_Object = MibTableColumn
fsp_II_2k_EthHubPortEnable2 = _Fsp_II_2k_EthHubPortEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 20),
    _Fsp_II_2k_EthHubPortEnable2_Type()
)
fsp_II_2k_EthHubPortEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortEnable2.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPartStatus2_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPartStatus2 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPartStatus2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPartStatus2_Object = MibTableColumn
fsp_II_2k_EthHubPortPartStatus2 = _Fsp_II_2k_EthHubPortPartStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 21),
    _Fsp_II_2k_EthHubPortPartStatus2_Type()
)
fsp_II_2k_EthHubPortPartStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPartStatus2.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortLinkStatus2_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortLinkStatus2 based on Integer32"""
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


_Fsp_II_2k_EthHubPortLinkStatus2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortLinkStatus2_Object = MibTableColumn
fsp_II_2k_EthHubPortLinkStatus2 = _Fsp_II_2k_EthHubPortLinkStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 22),
    _Fsp_II_2k_EthHubPortLinkStatus2_Type()
)
fsp_II_2k_EthHubPortLinkStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortLinkStatus2.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPolarity2_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPolarity2 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPolarity2_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPolarity2_Object = MibTableColumn
fsp_II_2k_EthHubPortPolarity2 = _Fsp_II_2k_EthHubPortPolarity2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 23),
    _Fsp_II_2k_EthHubPortPolarity2_Type()
)
fsp_II_2k_EthHubPortPolarity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPolarity2.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortEnable3_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortEnable3 based on Integer32"""
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


_Fsp_II_2k_EthHubPortEnable3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortEnable3_Object = MibTableColumn
fsp_II_2k_EthHubPortEnable3 = _Fsp_II_2k_EthHubPortEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 30),
    _Fsp_II_2k_EthHubPortEnable3_Type()
)
fsp_II_2k_EthHubPortEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortEnable3.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPartStatus3_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPartStatus3 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPartStatus3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPartStatus3_Object = MibTableColumn
fsp_II_2k_EthHubPortPartStatus3 = _Fsp_II_2k_EthHubPortPartStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 31),
    _Fsp_II_2k_EthHubPortPartStatus3_Type()
)
fsp_II_2k_EthHubPortPartStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPartStatus3.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortLinkStatus3_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortLinkStatus3 based on Integer32"""
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


_Fsp_II_2k_EthHubPortLinkStatus3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortLinkStatus3_Object = MibTableColumn
fsp_II_2k_EthHubPortLinkStatus3 = _Fsp_II_2k_EthHubPortLinkStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 32),
    _Fsp_II_2k_EthHubPortLinkStatus3_Type()
)
fsp_II_2k_EthHubPortLinkStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortLinkStatus3.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPolarity3_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPolarity3 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPolarity3_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPolarity3_Object = MibTableColumn
fsp_II_2k_EthHubPortPolarity3 = _Fsp_II_2k_EthHubPortPolarity3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 33),
    _Fsp_II_2k_EthHubPortPolarity3_Type()
)
fsp_II_2k_EthHubPortPolarity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPolarity3.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortEnable4_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortEnable4 based on Integer32"""
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


_Fsp_II_2k_EthHubPortEnable4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortEnable4_Object = MibTableColumn
fsp_II_2k_EthHubPortEnable4 = _Fsp_II_2k_EthHubPortEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 40),
    _Fsp_II_2k_EthHubPortEnable4_Type()
)
fsp_II_2k_EthHubPortEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortEnable4.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPartStatus4_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPartStatus4 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPartStatus4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPartStatus4_Object = MibTableColumn
fsp_II_2k_EthHubPortPartStatus4 = _Fsp_II_2k_EthHubPortPartStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 41),
    _Fsp_II_2k_EthHubPortPartStatus4_Type()
)
fsp_II_2k_EthHubPortPartStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPartStatus4.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortLinkStatus4_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortLinkStatus4 based on Integer32"""
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


_Fsp_II_2k_EthHubPortLinkStatus4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortLinkStatus4_Object = MibTableColumn
fsp_II_2k_EthHubPortLinkStatus4 = _Fsp_II_2k_EthHubPortLinkStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 42),
    _Fsp_II_2k_EthHubPortLinkStatus4_Type()
)
fsp_II_2k_EthHubPortLinkStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortLinkStatus4.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPolarity4_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPolarity4 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPolarity4_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPolarity4_Object = MibTableColumn
fsp_II_2k_EthHubPortPolarity4 = _Fsp_II_2k_EthHubPortPolarity4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 43),
    _Fsp_II_2k_EthHubPortPolarity4_Type()
)
fsp_II_2k_EthHubPortPolarity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPolarity4.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortEnable5_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortEnable5 based on Integer32"""
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


_Fsp_II_2k_EthHubPortEnable5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortEnable5_Object = MibTableColumn
fsp_II_2k_EthHubPortEnable5 = _Fsp_II_2k_EthHubPortEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 50),
    _Fsp_II_2k_EthHubPortEnable5_Type()
)
fsp_II_2k_EthHubPortEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortEnable5.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPartStatus5_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPartStatus5 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPartStatus5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPartStatus5_Object = MibTableColumn
fsp_II_2k_EthHubPortPartStatus5 = _Fsp_II_2k_EthHubPortPartStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 51),
    _Fsp_II_2k_EthHubPortPartStatus5_Type()
)
fsp_II_2k_EthHubPortPartStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPartStatus5.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortLinkStatus5_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortLinkStatus5 based on Integer32"""
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


_Fsp_II_2k_EthHubPortLinkStatus5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortLinkStatus5_Object = MibTableColumn
fsp_II_2k_EthHubPortLinkStatus5 = _Fsp_II_2k_EthHubPortLinkStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 52),
    _Fsp_II_2k_EthHubPortLinkStatus5_Type()
)
fsp_II_2k_EthHubPortLinkStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortLinkStatus5.setStatus("mandatory")


class _Fsp_II_2k_EthHubPortPolarity5_Type(Integer32):
    """Custom type fsp_II_2k_EthHubPortPolarity5 based on Integer32"""
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


_Fsp_II_2k_EthHubPortPolarity5_Type.__name__ = "Integer32"
_Fsp_II_2k_EthHubPortPolarity5_Object = MibTableColumn
fsp_II_2k_EthHubPortPolarity5 = _Fsp_II_2k_EthHubPortPolarity5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 53),
    _Fsp_II_2k_EthHubPortPolarity5_Type()
)
fsp_II_2k_EthHubPortPolarity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EthHubPortPolarity5.setStatus("mandatory")
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-TDMNumber"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMEntry.setStatus("mandatory")


class _Fsp_II_2k_TDMNumber_Type(Integer32):
    """Custom type fsp_II_2k_TDMNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_TDMNumber_Type.__name__ = "Integer32"
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notApplicable", 3))
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


class _Fsp_II_2k_TDMRemLoop_Type(Integer32):
    """Custom type fsp_II_2k_TDMRemLoop based on Integer32"""
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
          ("notApplicable", 3))
    )


_Fsp_II_2k_TDMRemLoop_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMRemLoop_Object = MibTableColumn
fsp_II_2k_TDMRemLoop = _Fsp_II_2k_TDMRemLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 11),
    _Fsp_II_2k_TDMRemLoop_Type()
)
fsp_II_2k_TDMRemLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRemLoop.setStatus("mandatory")


class _Fsp_II_2k_TDMLocInst1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst1 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst1_Object = MibTableColumn
fsp_II_2k_TDMLocInst1 = _Fsp_II_2k_TDMLocInst1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 20),
    _Fsp_II_2k_TDMLocInst1_Type()
)
fsp_II_2k_TDMLocInst1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable1 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable1_Object = MibTableColumn
fsp_II_2k_TDMLocEnable1 = _Fsp_II_2k_TDMLocEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 21),
    _Fsp_II_2k_TDMLocEnable1_Type()
)
fsp_II_2k_TDMLocEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx1 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx1_Object = MibTableColumn
fsp_II_2k_TDMLocRx1 = _Fsp_II_2k_TDMLocRx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 22),
    _Fsp_II_2k_TDMLocRx1_Type()
)
fsp_II_2k_TDMLocRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx1 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx1_Object = MibTableColumn
fsp_II_2k_TDMLocTx1 = _Fsp_II_2k_TDMLocTx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 23),
    _Fsp_II_2k_TDMLocTx1_Type()
)
fsp_II_2k_TDMLocTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData1 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData1_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData1 = _Fsp_II_2k_TDMLocRemoteData1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 24),
    _Fsp_II_2k_TDMLocRemoteData1_Type()
)
fsp_II_2k_TDMLocRemoteData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData1.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency1_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency1_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency1 = _Fsp_II_2k_TDMLocClockFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 25),
    _Fsp_II_2k_TDMLocClockFrequency1_Type()
)
fsp_II_2k_TDMLocClockFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError1 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError1_Object = MibTableColumn
fsp_II_2k_TDMLocClockError1 = _Fsp_II_2k_TDMLocClockError1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 26),
    _Fsp_II_2k_TDMLocClockError1_Type()
)
fsp_II_2k_TDMLocClockError1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocLoop1_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocLoop1 based on Integer32"""
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


_Fsp_II_2k_TDMLocLoop1_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocLoop1_Object = MibTableColumn
fsp_II_2k_TDMLocLoop1 = _Fsp_II_2k_TDMLocLoop1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 27),
    _Fsp_II_2k_TDMLocLoop1_Type()
)
fsp_II_2k_TDMLocLoop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocLoop1.setStatus("mandatory")


class _Fsp_II_2k_TDMLocInst2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst2 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst2_Object = MibTableColumn
fsp_II_2k_TDMLocInst2 = _Fsp_II_2k_TDMLocInst2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 30),
    _Fsp_II_2k_TDMLocInst2_Type()
)
fsp_II_2k_TDMLocInst2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable2 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable2_Object = MibTableColumn
fsp_II_2k_TDMLocEnable2 = _Fsp_II_2k_TDMLocEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 31),
    _Fsp_II_2k_TDMLocEnable2_Type()
)
fsp_II_2k_TDMLocEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx2 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx2_Object = MibTableColumn
fsp_II_2k_TDMLocRx2 = _Fsp_II_2k_TDMLocRx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 32),
    _Fsp_II_2k_TDMLocRx2_Type()
)
fsp_II_2k_TDMLocRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx2 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx2_Object = MibTableColumn
fsp_II_2k_TDMLocTx2 = _Fsp_II_2k_TDMLocTx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 33),
    _Fsp_II_2k_TDMLocTx2_Type()
)
fsp_II_2k_TDMLocTx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData2 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData2_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData2 = _Fsp_II_2k_TDMLocRemoteData2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 34),
    _Fsp_II_2k_TDMLocRemoteData2_Type()
)
fsp_II_2k_TDMLocRemoteData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData2.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency2_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency2_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency2 = _Fsp_II_2k_TDMLocClockFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 35),
    _Fsp_II_2k_TDMLocClockFrequency2_Type()
)
fsp_II_2k_TDMLocClockFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError2 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError2_Object = MibTableColumn
fsp_II_2k_TDMLocClockError2 = _Fsp_II_2k_TDMLocClockError2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 36),
    _Fsp_II_2k_TDMLocClockError2_Type()
)
fsp_II_2k_TDMLocClockError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocLoop2_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocLoop2 based on Integer32"""
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


_Fsp_II_2k_TDMLocLoop2_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocLoop2_Object = MibTableColumn
fsp_II_2k_TDMLocLoop2 = _Fsp_II_2k_TDMLocLoop2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 37),
    _Fsp_II_2k_TDMLocLoop2_Type()
)
fsp_II_2k_TDMLocLoop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocLoop2.setStatus("mandatory")


class _Fsp_II_2k_TDMLocInst3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst3 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst3_Object = MibTableColumn
fsp_II_2k_TDMLocInst3 = _Fsp_II_2k_TDMLocInst3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 40),
    _Fsp_II_2k_TDMLocInst3_Type()
)
fsp_II_2k_TDMLocInst3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable3 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable3_Object = MibTableColumn
fsp_II_2k_TDMLocEnable3 = _Fsp_II_2k_TDMLocEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 41),
    _Fsp_II_2k_TDMLocEnable3_Type()
)
fsp_II_2k_TDMLocEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx3 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx3_Object = MibTableColumn
fsp_II_2k_TDMLocRx3 = _Fsp_II_2k_TDMLocRx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 42),
    _Fsp_II_2k_TDMLocRx3_Type()
)
fsp_II_2k_TDMLocRx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx3 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx3_Object = MibTableColumn
fsp_II_2k_TDMLocTx3 = _Fsp_II_2k_TDMLocTx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 43),
    _Fsp_II_2k_TDMLocTx3_Type()
)
fsp_II_2k_TDMLocTx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData3 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData3_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData3 = _Fsp_II_2k_TDMLocRemoteData3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 44),
    _Fsp_II_2k_TDMLocRemoteData3_Type()
)
fsp_II_2k_TDMLocRemoteData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData3.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency3_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency3_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency3 = _Fsp_II_2k_TDMLocClockFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 45),
    _Fsp_II_2k_TDMLocClockFrequency3_Type()
)
fsp_II_2k_TDMLocClockFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError3_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError3 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError3_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError3_Object = MibTableColumn
fsp_II_2k_TDMLocClockError3 = _Fsp_II_2k_TDMLocClockError3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 46),
    _Fsp_II_2k_TDMLocClockError3_Type()
)
fsp_II_2k_TDMLocClockError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError3.setStatus("mandatory")


class _Fsp_II_2k_TDMLocInst4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst4 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst4_Object = MibTableColumn
fsp_II_2k_TDMLocInst4 = _Fsp_II_2k_TDMLocInst4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 50),
    _Fsp_II_2k_TDMLocInst4_Type()
)
fsp_II_2k_TDMLocInst4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable4 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable4_Object = MibTableColumn
fsp_II_2k_TDMLocEnable4 = _Fsp_II_2k_TDMLocEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 51),
    _Fsp_II_2k_TDMLocEnable4_Type()
)
fsp_II_2k_TDMLocEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx4 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx4_Object = MibTableColumn
fsp_II_2k_TDMLocRx4 = _Fsp_II_2k_TDMLocRx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 52),
    _Fsp_II_2k_TDMLocRx4_Type()
)
fsp_II_2k_TDMLocRx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx4 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx4_Object = MibTableColumn
fsp_II_2k_TDMLocTx4 = _Fsp_II_2k_TDMLocTx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 53),
    _Fsp_II_2k_TDMLocTx4_Type()
)
fsp_II_2k_TDMLocTx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData4 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData4_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData4 = _Fsp_II_2k_TDMLocRemoteData4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 54),
    _Fsp_II_2k_TDMLocRemoteData4_Type()
)
fsp_II_2k_TDMLocRemoteData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData4.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency4_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency4_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency4 = _Fsp_II_2k_TDMLocClockFrequency4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 55),
    _Fsp_II_2k_TDMLocClockFrequency4_Type()
)
fsp_II_2k_TDMLocClockFrequency4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency4.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError4_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError4 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError4_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError4_Object = MibTableColumn
fsp_II_2k_TDMLocClockError4 = _Fsp_II_2k_TDMLocClockError4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 56),
    _Fsp_II_2k_TDMLocClockError4_Type()
)
fsp_II_2k_TDMLocClockError4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError4.setStatus("mandatory")
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


class _Fsp_II_2k_TDMLocInst5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst5 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst5_Object = MibTableColumn
fsp_II_2k_TDMLocInst5 = _Fsp_II_2k_TDMLocInst5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 70),
    _Fsp_II_2k_TDMLocInst5_Type()
)
fsp_II_2k_TDMLocInst5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable5 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable5_Object = MibTableColumn
fsp_II_2k_TDMLocEnable5 = _Fsp_II_2k_TDMLocEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 71),
    _Fsp_II_2k_TDMLocEnable5_Type()
)
fsp_II_2k_TDMLocEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx5 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx5_Object = MibTableColumn
fsp_II_2k_TDMLocRx5 = _Fsp_II_2k_TDMLocRx5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 72),
    _Fsp_II_2k_TDMLocRx5_Type()
)
fsp_II_2k_TDMLocRx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx5 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx5_Object = MibTableColumn
fsp_II_2k_TDMLocTx5 = _Fsp_II_2k_TDMLocTx5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 73),
    _Fsp_II_2k_TDMLocTx5_Type()
)
fsp_II_2k_TDMLocTx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData5 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData5_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData5 = _Fsp_II_2k_TDMLocRemoteData5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 74),
    _Fsp_II_2k_TDMLocRemoteData5_Type()
)
fsp_II_2k_TDMLocRemoteData5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData5.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency5_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency5_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency5 = _Fsp_II_2k_TDMLocClockFrequency5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 75),
    _Fsp_II_2k_TDMLocClockFrequency5_Type()
)
fsp_II_2k_TDMLocClockFrequency5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError5_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError5 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError5_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError5_Object = MibTableColumn
fsp_II_2k_TDMLocClockError5 = _Fsp_II_2k_TDMLocClockError5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 76),
    _Fsp_II_2k_TDMLocClockError5_Type()
)
fsp_II_2k_TDMLocClockError5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError5.setStatus("mandatory")


class _Fsp_II_2k_TDMLocInst6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst6 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst6_Object = MibTableColumn
fsp_II_2k_TDMLocInst6 = _Fsp_II_2k_TDMLocInst6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 80),
    _Fsp_II_2k_TDMLocInst6_Type()
)
fsp_II_2k_TDMLocInst6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable6 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable6_Object = MibTableColumn
fsp_II_2k_TDMLocEnable6 = _Fsp_II_2k_TDMLocEnable6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 81),
    _Fsp_II_2k_TDMLocEnable6_Type()
)
fsp_II_2k_TDMLocEnable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx6 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx6_Object = MibTableColumn
fsp_II_2k_TDMLocRx6 = _Fsp_II_2k_TDMLocRx6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 82),
    _Fsp_II_2k_TDMLocRx6_Type()
)
fsp_II_2k_TDMLocRx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx6 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx6_Object = MibTableColumn
fsp_II_2k_TDMLocTx6 = _Fsp_II_2k_TDMLocTx6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 83),
    _Fsp_II_2k_TDMLocTx6_Type()
)
fsp_II_2k_TDMLocTx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData6 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData6_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData6 = _Fsp_II_2k_TDMLocRemoteData6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 84),
    _Fsp_II_2k_TDMLocRemoteData6_Type()
)
fsp_II_2k_TDMLocRemoteData6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData6.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency6_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency6_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency6 = _Fsp_II_2k_TDMLocClockFrequency6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 85),
    _Fsp_II_2k_TDMLocClockFrequency6_Type()
)
fsp_II_2k_TDMLocClockFrequency6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError6_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError6 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError6_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError6_Object = MibTableColumn
fsp_II_2k_TDMLocClockError6 = _Fsp_II_2k_TDMLocClockError6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 86),
    _Fsp_II_2k_TDMLocClockError6_Type()
)
fsp_II_2k_TDMLocClockError6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError6.setStatus("mandatory")


class _Fsp_II_2k_TDMLocInst7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst7 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst7_Object = MibTableColumn
fsp_II_2k_TDMLocInst7 = _Fsp_II_2k_TDMLocInst7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 90),
    _Fsp_II_2k_TDMLocInst7_Type()
)
fsp_II_2k_TDMLocInst7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable7 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable7_Object = MibTableColumn
fsp_II_2k_TDMLocEnable7 = _Fsp_II_2k_TDMLocEnable7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 91),
    _Fsp_II_2k_TDMLocEnable7_Type()
)
fsp_II_2k_TDMLocEnable7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx7 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx7_Object = MibTableColumn
fsp_II_2k_TDMLocRx7 = _Fsp_II_2k_TDMLocRx7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 92),
    _Fsp_II_2k_TDMLocRx7_Type()
)
fsp_II_2k_TDMLocRx7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx7 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx7_Object = MibTableColumn
fsp_II_2k_TDMLocTx7 = _Fsp_II_2k_TDMLocTx7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 93),
    _Fsp_II_2k_TDMLocTx7_Type()
)
fsp_II_2k_TDMLocTx7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData7 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData7_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData7 = _Fsp_II_2k_TDMLocRemoteData7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 94),
    _Fsp_II_2k_TDMLocRemoteData7_Type()
)
fsp_II_2k_TDMLocRemoteData7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData7.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency7_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency7_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency7 = _Fsp_II_2k_TDMLocClockFrequency7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 95),
    _Fsp_II_2k_TDMLocClockFrequency7_Type()
)
fsp_II_2k_TDMLocClockFrequency7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError7_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError7 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError7_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError7_Object = MibTableColumn
fsp_II_2k_TDMLocClockError7 = _Fsp_II_2k_TDMLocClockError7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 96),
    _Fsp_II_2k_TDMLocClockError7_Type()
)
fsp_II_2k_TDMLocClockError7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError7.setStatus("mandatory")


class _Fsp_II_2k_TDMLocInst8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocInst8 based on Integer32"""
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


_Fsp_II_2k_TDMLocInst8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocInst8_Object = MibTableColumn
fsp_II_2k_TDMLocInst8 = _Fsp_II_2k_TDMLocInst8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 100),
    _Fsp_II_2k_TDMLocInst8_Type()
)
fsp_II_2k_TDMLocInst8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocInst8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocEnable8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocEnable8 based on Integer32"""
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


_Fsp_II_2k_TDMLocEnable8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocEnable8_Object = MibTableColumn
fsp_II_2k_TDMLocEnable8 = _Fsp_II_2k_TDMLocEnable8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 101),
    _Fsp_II_2k_TDMLocEnable8_Type()
)
fsp_II_2k_TDMLocEnable8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnable8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRx8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRx8 based on Integer32"""
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


_Fsp_II_2k_TDMLocRx8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRx8_Object = MibTableColumn
fsp_II_2k_TDMLocRx8 = _Fsp_II_2k_TDMLocRx8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 102),
    _Fsp_II_2k_TDMLocRx8_Type()
)
fsp_II_2k_TDMLocRx8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRx8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocTx8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocTx8 based on Integer32"""
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


_Fsp_II_2k_TDMLocTx8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocTx8_Object = MibTableColumn
fsp_II_2k_TDMLocTx8 = _Fsp_II_2k_TDMLocTx8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 103),
    _Fsp_II_2k_TDMLocTx8_Type()
)
fsp_II_2k_TDMLocTx8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocTx8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocRemoteData8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocRemoteData8 based on Integer32"""
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


_Fsp_II_2k_TDMLocRemoteData8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocRemoteData8_Object = MibTableColumn
fsp_II_2k_TDMLocRemoteData8 = _Fsp_II_2k_TDMLocRemoteData8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 104),
    _Fsp_II_2k_TDMLocRemoteData8_Type()
)
fsp_II_2k_TDMLocRemoteData8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRemoteData8.setStatus("mandatory")
_Fsp_II_2k_TDMLocClockFrequency8_Type = Integer32
_Fsp_II_2k_TDMLocClockFrequency8_Object = MibTableColumn
fsp_II_2k_TDMLocClockFrequency8 = _Fsp_II_2k_TDMLocClockFrequency8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 105),
    _Fsp_II_2k_TDMLocClockFrequency8_Type()
)
fsp_II_2k_TDMLocClockFrequency8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFrequency8.setStatus("mandatory")


class _Fsp_II_2k_TDMLocClockError8_Type(Integer32):
    """Custom type fsp_II_2k_TDMLocClockError8 based on Integer32"""
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


_Fsp_II_2k_TDMLocClockError8_Type.__name__ = "Integer32"
_Fsp_II_2k_TDMLocClockError8_Object = MibTableColumn
fsp_II_2k_TDMLocClockError8 = _Fsp_II_2k_TDMLocClockError8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 106),
    _Fsp_II_2k_TDMLocClockError8_Type()
)
fsp_II_2k_TDMLocClockError8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockError8.setStatus("mandatory")
_Fsp_II_2k_EDFA_ObjectIdentity = ObjectIdentity
fsp_II_2k_EDFA = _Fsp_II_2k_EDFA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16)
)
_Fsp_II_2k_EDFA_Table_Object = MibTable
fsp_II_2k_EDFA_Table = _Fsp_II_2k_EDFA_Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1)
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Table.setStatus("mandatory")
_Fsp_II_2k_EDFA_Entry_Object = MibTableRow
fsp_II_2k_EDFA_Entry = _Fsp_II_2k_EDFA_Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1)
)
fsp_II_2k_EDFA_Entry.setIndexNames(
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-EDFA-Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Entry.setStatus("mandatory")


class _Fsp_II_2k_EDFA_Number_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_EDFA_Number_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_Number_Object = MibTableColumn
fsp_II_2k_EDFA_Number = _Fsp_II_2k_EDFA_Number_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 1),
    _Fsp_II_2k_EDFA_Number_Type()
)
fsp_II_2k_EDFA_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Number.setStatus("mandatory")


class _Fsp_II_2k_EDFA_Band_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_Band based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("cband", 2),
          ("lband", 3))
    )


_Fsp_II_2k_EDFA_Band_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_Band_Object = MibTableColumn
fsp_II_2k_EDFA_Band = _Fsp_II_2k_EDFA_Band_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 2),
    _Fsp_II_2k_EDFA_Band_Type()
)
fsp_II_2k_EDFA_Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Band.setStatus("mandatory")
_Fsp_II_2k_EDFA_OIP_Type = Integer32
_Fsp_II_2k_EDFA_OIP_Object = MibTableColumn
fsp_II_2k_EDFA_OIP = _Fsp_II_2k_EDFA_OIP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 3),
    _Fsp_II_2k_EDFA_OIP_Type()
)
fsp_II_2k_EDFA_OIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OIP.setStatus("mandatory")


class _Fsp_II_2k_EDFA_OIP_State_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_OIP_State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2),
          ("too-high", 3))
    )


_Fsp_II_2k_EDFA_OIP_State_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_OIP_State_Object = MibTableColumn
fsp_II_2k_EDFA_OIP_State = _Fsp_II_2k_EDFA_OIP_State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 4),
    _Fsp_II_2k_EDFA_OIP_State_Type()
)
fsp_II_2k_EDFA_OIP_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OIP_State.setStatus("mandatory")
_Fsp_II_2k_EDFA_IfMod_Temp_Type = Integer32
_Fsp_II_2k_EDFA_IfMod_Temp_Object = MibTableColumn
fsp_II_2k_EDFA_IfMod_Temp = _Fsp_II_2k_EDFA_IfMod_Temp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 5),
    _Fsp_II_2k_EDFA_IfMod_Temp_Type()
)
fsp_II_2k_EDFA_IfMod_Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_IfMod_Temp.setStatus("mandatory")


class _Fsp_II_2k_EDFA_IfMod_TempState_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_IfMod_TempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("ooR", 2))
    )


_Fsp_II_2k_EDFA_IfMod_TempState_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_IfMod_TempState_Object = MibTableColumn
fsp_II_2k_EDFA_IfMod_TempState = _Fsp_II_2k_EDFA_IfMod_TempState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 6),
    _Fsp_II_2k_EDFA_IfMod_TempState_Type()
)
fsp_II_2k_EDFA_IfMod_TempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_IfMod_TempState.setStatus("mandatory")


class _Fsp_II_2k_EDFA_Pump_TxState_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_Pump_TxState based on Integer32"""
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


_Fsp_II_2k_EDFA_Pump_TxState_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_Pump_TxState_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_TxState = _Fsp_II_2k_EDFA_Pump_TxState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 7),
    _Fsp_II_2k_EDFA_Pump_TxState_Type()
)
fsp_II_2k_EDFA_Pump_TxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TxState.setStatus("mandatory")
_Fsp_II_2k_EDFA_Pump_Power_Type = Integer32
_Fsp_II_2k_EDFA_Pump_Power_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_Power = _Fsp_II_2k_EDFA_Pump_Power_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 8),
    _Fsp_II_2k_EDFA_Pump_Power_Type()
)
fsp_II_2k_EDFA_Pump_Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_Power.setStatus("mandatory")
_Fsp_II_2k_EDFA_Pump_PowerMax_Type = Integer32
_Fsp_II_2k_EDFA_Pump_PowerMax_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_PowerMax = _Fsp_II_2k_EDFA_Pump_PowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 9),
    _Fsp_II_2k_EDFA_Pump_PowerMax_Type()
)
fsp_II_2k_EDFA_Pump_PowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_PowerMax.setStatus("mandatory")
_Fsp_II_2k_EDFA_Pump_PowerConf_Type = Integer32
_Fsp_II_2k_EDFA_Pump_PowerConf_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_PowerConf = _Fsp_II_2k_EDFA_Pump_PowerConf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 10),
    _Fsp_II_2k_EDFA_Pump_PowerConf_Type()
)
fsp_II_2k_EDFA_Pump_PowerConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_PowerConf.setStatus("mandatory")
_Fsp_II_2k_EDFA_Pump_Temp_Type = Integer32
_Fsp_II_2k_EDFA_Pump_Temp_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_Temp = _Fsp_II_2k_EDFA_Pump_Temp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 11),
    _Fsp_II_2k_EDFA_Pump_Temp_Type()
)
fsp_II_2k_EDFA_Pump_Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_Temp.setStatus("mandatory")


class _Fsp_II_2k_EDFA_Pump_TempState_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_Pump_TempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("ooR", 2))
    )


_Fsp_II_2k_EDFA_Pump_TempState_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_Pump_TempState_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_TempState = _Fsp_II_2k_EDFA_Pump_TempState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 12),
    _Fsp_II_2k_EDFA_Pump_TempState_Type()
)
fsp_II_2k_EDFA_Pump_TempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TempState.setStatus("mandatory")
_Fsp_II_2k_EDFA_Pump_Current_Type = Integer32
_Fsp_II_2k_EDFA_Pump_Current_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_Current = _Fsp_II_2k_EDFA_Pump_Current_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 13),
    _Fsp_II_2k_EDFA_Pump_Current_Type()
)
fsp_II_2k_EDFA_Pump_Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_Current.setStatus("mandatory")


class _Fsp_II_2k_EDFA_Pump_CurrState_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_Pump_CurrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("eoL", 2))
    )


_Fsp_II_2k_EDFA_Pump_CurrState_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_Pump_CurrState_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_CurrState = _Fsp_II_2k_EDFA_Pump_CurrState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 14),
    _Fsp_II_2k_EDFA_Pump_CurrState_Type()
)
fsp_II_2k_EDFA_Pump_CurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_CurrState.setStatus("mandatory")
_Fsp_II_2k_EDFA_Pump_TECCurrent_Type = Integer32
_Fsp_II_2k_EDFA_Pump_TECCurrent_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_TECCurrent = _Fsp_II_2k_EDFA_Pump_TECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 15),
    _Fsp_II_2k_EDFA_Pump_TECCurrent_Type()
)
fsp_II_2k_EDFA_Pump_TECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TECCurrent.setStatus("mandatory")


class _Fsp_II_2k_EDFA_Pump_TECState_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_Pump_TECState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("eoL", 2))
    )


_Fsp_II_2k_EDFA_Pump_TECState_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_Pump_TECState_Object = MibTableColumn
fsp_II_2k_EDFA_Pump_TECState = _Fsp_II_2k_EDFA_Pump_TECState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 16),
    _Fsp_II_2k_EDFA_Pump_TECState_Type()
)
fsp_II_2k_EDFA_Pump_TECState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TECState.setStatus("mandatory")
_Fsp_II_2k_EDFA_OOP_Type = Integer32
_Fsp_II_2k_EDFA_OOP_Object = MibTableColumn
fsp_II_2k_EDFA_OOP = _Fsp_II_2k_EDFA_OOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 17),
    _Fsp_II_2k_EDFA_OOP_Type()
)
fsp_II_2k_EDFA_OOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OOP.setStatus("mandatory")


class _Fsp_II_2k_EDFA_OOP_State_Type(Integer32):
    """Custom type fsp_II_2k_EDFA_OOP_State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2),
          ("too-low", 3))
    )


_Fsp_II_2k_EDFA_OOP_State_Type.__name__ = "Integer32"
_Fsp_II_2k_EDFA_OOP_State_Object = MibTableColumn
fsp_II_2k_EDFA_OOP_State = _Fsp_II_2k_EDFA_OOP_State_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 16, 1, 1, 18),
    _Fsp_II_2k_EDFA_OOP_State_Type()
)
fsp_II_2k_EDFA_OOP_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OOP_State.setStatus("mandatory")
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-MUX-DMX-Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_MUX_DMX_Entry.setStatus("mandatory")


class _Fsp_II_2k_MUX_DMX_Number_Type(Integer32):
    """Custom type fsp_II_2k_MUX_DMX_Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_MUX_DMX_Number_Type.__name__ = "Integer32"
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
          ("mux-dmux", 3),
          ("mux-dmux-hotstandby", 4))
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
        *(("cwdm-r1", 1),
          ("cwdm-r2", 2),
          ("dwdm-r1", 3),
          ("dwdm-r2", 4))
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
          ("channel-M1to4-D17to20", 13),
          ("channel-M5to8-D21to24", 14),
          ("channel-M9to12-D25to28", 15),
          ("channel-M13to16-D29to32", 16),
          ("channel-M17to20-D1to4", 17),
          ("channel-M21to24-D5to8", 18),
          ("channel-M25to28-D9to12", 19),
          ("channel-M29to32-D13to16", 20))
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
    (0, "FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-BSM-Number"),
)
if mibBuilder.loadTexts:
    fsp_II_2k_BSM_Entry.setStatus("mandatory")


class _Fsp_II_2k_BSM_Number_Type(Integer32):
    """Custom type fsp_II_2k_BSM_Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Fsp_II_2k_BSM_Number_Type.__name__ = "Integer32"
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
        *(("dwdm-r1", 1),
          ("dwdm-r2", 2))
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
          ("bandLC1-3-5-7", 2),
          ("bandC1to4", 3),
          ("bandL5to8", 4),
          ("band-MC1to4-DL5to8", 5),
          ("band-ML5to8-DC1to4", 6))
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
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HardwareAdded.setStatus(
        ""
    )

fsp_II_2k_HardwareDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 2)
)
fsp_II_2k_HardwareDeleted.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HardwareDeleted.setStatus(
        ""
    )

fsp_II_2k_PSNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 3)
)
fsp_II_2k_PSNotFail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-PSNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_PSNotFail.setStatus(
        ""
    )

fsp_II_2k_PSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 4)
)
fsp_II_2k_PSFail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-PSNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_PSFail.setStatus(
        ""
    )

fsp_II_2k_FanNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 5)
)
fsp_II_2k_FanNotFail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-FanNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_FanNotFail.setStatus(
        ""
    )

fsp_II_2k_FanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 6)
)
fsp_II_2k_FanFail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-FanNumber")
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
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxLocOn.setStatus(
        ""
    )

fsp_II_2k_RxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 21)
)
fsp_II_2k_RxLocOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxLocOff.setStatus(
        ""
    )

fsp_II_2k_TxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 22)
)
fsp_II_2k_TxLocOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxLocOn.setStatus(
        ""
    )

fsp_II_2k_TxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 23)
)
fsp_II_2k_TxLocOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxLocOff.setStatus(
        ""
    )

fsp_II_2k_RxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 24)
)
fsp_II_2k_RxRemOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRemOn.setStatus(
        ""
    )

fsp_II_2k_RxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 25)
)
fsp_II_2k_RxRemOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRemOff.setStatus(
        ""
    )

fsp_II_2k_TxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 26)
)
fsp_II_2k_TxRemOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRemOn.setStatus(
        ""
    )

fsp_II_2k_TxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 27)
)
fsp_II_2k_TxRemOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRemOff.setStatus(
        ""
    )

fsp_II_2k_RxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 28)
)
fsp_II_2k_RxRem2On.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRem2On.setStatus(
        ""
    )

fsp_II_2k_RxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 29)
)
fsp_II_2k_RxRem2Off.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RxRem2Off.setStatus(
        ""
    )

fsp_II_2k_TxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 30)
)
fsp_II_2k_TxRem2On.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRem2On.setStatus(
        ""
    )

fsp_II_2k_TxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 31)
)
fsp_II_2k_TxRem2Off.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TxRem2Off.setStatus(
        ""
    )

fsp_II_2k_ClockNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 32)
)
fsp_II_2k_ClockNoFail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockNoFail.setStatus(
        ""
    )

fsp_II_2k_ClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 33)
)
fsp_II_2k_ClockFail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockFail.setStatus(
        ""
    )

fsp_II_2k_ClockChangeFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 34)
)
fsp_II_2k_ClockChangeFrequency.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_ClockChangeFrequency.setStatus(
        ""
    )

fsp_II_2k_LocLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 35)
)
fsp_II_2k_LocLoopOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_LocLoopOn.setStatus(
        ""
    )

fsp_II_2k_LocLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 36)
)
fsp_II_2k_LocLoopOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_LocLoopOff.setStatus(
        ""
    )

fsp_II_2k_RemLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 37)
)
fsp_II_2k_RemLoopOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemLoopOn.setStatus(
        ""
    )

fsp_II_2k_RemLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 38)
)
fsp_II_2k_RemLoopOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemLoopOff.setStatus(
        ""
    )

fsp_II_2k_switchRefLaserOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 40)
)
fsp_II_2k_switchRefLaserOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchRefLaserOn.setStatus(
        ""
    )

fsp_II_2k_switchRefLaserOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 41)
)
fsp_II_2k_switchRefLaserOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchRefLaserOff.setStatus(
        ""
    )

fsp_II_2k_switchToA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 42)
)
fsp_II_2k_switchToA.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchToA.setStatus(
        ""
    )

fsp_II_2k_switchToB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 43)
)
fsp_II_2k_switchToB.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchToB.setStatus(
        ""
    )

fsp_II_2k_switchAutomatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 44)
)
fsp_II_2k_switchAutomatic.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchAutomatic.setStatus(
        ""
    )

fsp_II_2k_switchLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 45)
)
fsp_II_2k_switchLocked.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLocked.setStatus(
        ""
    )

fsp_II_2k_switchLineAavailAgain = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 46)
)
fsp_II_2k_switchLineAavailAgain.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineAavailAgain.setStatus(
        ""
    )

fsp_II_2k_switchLineANotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 47)
)
fsp_II_2k_switchLineANotAvail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineANotAvail.setStatus(
        ""
    )

fsp_II_2k_switchLineBavailAgain = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 48)
)
fsp_II_2k_switchLineBavailAgain.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineBavailAgain.setStatus(
        ""
    )

fsp_II_2k_switchLineBNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 49)
)
fsp_II_2k_switchLineBNotAvail.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchLineBNotAvail.setStatus(
        ""
    )

fsp_II_2k_repeatedMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 50)
)
fsp_II_2k_repeatedMessage.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
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

fsp_II_2k_switchALSOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 53)
)
fsp_II_2k_switchALSOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchALSOn.setStatus(
        ""
    )

fsp_II_2k_switchALSOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 54)
)
fsp_II_2k_switchALSOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_switchALSOff.setStatus(
        ""
    )

fsp_II_2k_NEMIAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 55)
)
fsp_II_2k_NEMIAuthFail.setObjects(
      *(("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-MainLastAuthFailSource"),
        ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-MainLastAuthFailDescr"))
)
if mibBuilder.loadTexts:
    fsp_II_2k_NEMIAuthFail.setStatus(
        ""
    )

fsp_II_2k_EthPortEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 60)
)
fsp_II_2k_EthPortEnable.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortEnable.setStatus(
        ""
    )

fsp_II_2k_EthPortDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 61)
)
fsp_II_2k_EthPortDisable.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortDisable.setStatus(
        ""
    )

fsp_II_2k_EthPortPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 62)
)
fsp_II_2k_EthPortPartitioned.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortPartitioned.setStatus(
        ""
    )

fsp_II_2k_EthPortNotPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 63)
)
fsp_II_2k_EthPortNotPartitioned.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortNotPartitioned.setStatus(
        ""
    )

fsp_II_2k_EthPortLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 64)
)
fsp_II_2k_EthPortLinkPulses.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortLinkPulses.setStatus(
        ""
    )

fsp_II_2k_EthPortNoLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 65)
)
fsp_II_2k_EthPortNoLinkPulses.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortNoLinkPulses.setStatus(
        ""
    )

fsp_II_2k_TDMRemoteSyncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 70)
)
fsp_II_2k_TDMRemoteSyncLoss.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRemoteSyncLoss.setStatus(
        ""
    )

fsp_II_2k_TDMRemoteSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 71)
)
fsp_II_2k_TDMRemoteSync.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMRemoteSync.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 72)
)
fsp_II_2k_TDMLocEnabled1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled1.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 73)
)
fsp_II_2k_TDMLocDisable1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable1.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 74)
)
fsp_II_2k_TDMLocEnabled2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled2.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 75)
)
fsp_II_2k_TDMLocDisable2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable2.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 76)
)
fsp_II_2k_TDMLocEnabled3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled3.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 77)
)
fsp_II_2k_TDMLocDisable3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable3.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 78)
)
fsp_II_2k_TDMLocEnabled4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled4.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 79)
)
fsp_II_2k_TDMLocDisable4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable4.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 80)
)
fsp_II_2k_TDMLocEnabled5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled5.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 81)
)
fsp_II_2k_TDMLocDisable5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable5.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 82)
)
fsp_II_2k_TDMLocEnabled6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled6.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 83)
)
fsp_II_2k_TDMLocDisable6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable6.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 84)
)
fsp_II_2k_TDMLocEnabled7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled7.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 85)
)
fsp_II_2k_TDMLocDisable7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable7.setStatus(
        ""
    )

fsp_II_2k_TDMLocEnabled8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 86)
)
fsp_II_2k_TDMLocEnabled8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocEnabled8.setStatus(
        ""
    )

fsp_II_2k_TDMLocDisable8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 87)
)
fsp_II_2k_TDMLocDisable8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocDisable8.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 88)
)
fsp_II_2k_TDMLocRxOn1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn1.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 89)
)
fsp_II_2k_TDMLocRxOff1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff1.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 90)
)
fsp_II_2k_TDMLocRxOn2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn2.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 91)
)
fsp_II_2k_TDMLocRxOff2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff2.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 92)
)
fsp_II_2k_TDMLocRxOn3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn3.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 93)
)
fsp_II_2k_TDMLocRxOff3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff3.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 94)
)
fsp_II_2k_TDMLocRxOn4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn4.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 95)
)
fsp_II_2k_TDMLocRxOff4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff4.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 96)
)
fsp_II_2k_TDMLocRxOn5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn5.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 97)
)
fsp_II_2k_TDMLocRxOff5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff5.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 98)
)
fsp_II_2k_TDMLocRxOn6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn6.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 99)
)
fsp_II_2k_TDMLocRxOff6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff6.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 100)
)
fsp_II_2k_TDMLocRxOn7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn7.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 101)
)
fsp_II_2k_TDMLocRxOff7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff7.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOn8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 102)
)
fsp_II_2k_TDMLocRxOn8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOn8.setStatus(
        ""
    )

fsp_II_2k_TDMLocRxOff8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 103)
)
fsp_II_2k_TDMLocRxOff8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocRxOff8.setStatus(
        ""
    )

fsp_II_2k_TDMLocData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 104)
)
fsp_II_2k_TDMLocData1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData1.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 105)
)
fsp_II_2k_TDMLocNoData1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData1.setStatus(
        ""
    )

fsp_II_2k_TDMLocData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 106)
)
fsp_II_2k_TDMLocData2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData2.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 107)
)
fsp_II_2k_TDMLocNoData2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData2.setStatus(
        ""
    )

fsp_II_2k_TDMLocData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 108)
)
fsp_II_2k_TDMLocData3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData3.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 109)
)
fsp_II_2k_TDMLocNoData3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData3.setStatus(
        ""
    )

fsp_II_2k_TDMLocData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 110)
)
fsp_II_2k_TDMLocData4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData4.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 111)
)
fsp_II_2k_TDMLocNoData4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData4.setStatus(
        ""
    )

fsp_II_2k_TDMLocData5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 112)
)
fsp_II_2k_TDMLocData5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData5.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 113)
)
fsp_II_2k_TDMLocNoData5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData5.setStatus(
        ""
    )

fsp_II_2k_TDMLocData6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 114)
)
fsp_II_2k_TDMLocData6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData6.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 115)
)
fsp_II_2k_TDMLocNoData6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData6.setStatus(
        ""
    )

fsp_II_2k_TDMLocData7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 116)
)
fsp_II_2k_TDMLocData7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData7.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 117)
)
fsp_II_2k_TDMLocNoData7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData7.setStatus(
        ""
    )

fsp_II_2k_TDMLocData8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 118)
)
fsp_II_2k_TDMLocData8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocData8.setStatus(
        ""
    )

fsp_II_2k_TDMLocNoData8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 119)
)
fsp_II_2k_TDMLocNoData8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocNoData8.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 120)
)
fsp_II_2k_TDMLocClockFail1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail1.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 121)
)
fsp_II_2k_TDMLocClockNoFail1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail1.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 122)
)
fsp_II_2k_TDMLocClockFail2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail2.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 123)
)
fsp_II_2k_TDMLocClockNoFail2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail2.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 124)
)
fsp_II_2k_TDMLocClockFail3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail3.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 125)
)
fsp_II_2k_TDMLocClockNoFail3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail3.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 126)
)
fsp_II_2k_TDMLocClockFail4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail4.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 127)
)
fsp_II_2k_TDMLocClockNoFail4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail4.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 128)
)
fsp_II_2k_TDMLocClockFail5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail5.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 129)
)
fsp_II_2k_TDMLocClockNoFail5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail5.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 130)
)
fsp_II_2k_TDMLocClockFail6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail6.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 131)
)
fsp_II_2k_TDMLocClockNoFail6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail6.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 132)
)
fsp_II_2k_TDMLocClockFail7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail7.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 133)
)
fsp_II_2k_TDMLocClockNoFail7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail7.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockFail8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 134)
)
fsp_II_2k_TDMLocClockFail8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockFail8.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockNoFail8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 135)
)
fsp_II_2k_TDMLocClockNoFail8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockNoFail8.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 136)
)
fsp_II_2k_TDMLocClockChange1.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange1.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 137)
)
fsp_II_2k_TDMLocClockChange2.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange2.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 138)
)
fsp_II_2k_TDMLocClockChange3.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange3.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 139)
)
fsp_II_2k_TDMLocClockChange4.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange4.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 140)
)
fsp_II_2k_TDMLocClockChange5.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange5.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 141)
)
fsp_II_2k_TDMLocClockChange6.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange6.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 142)
)
fsp_II_2k_TDMLocClockChange7.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange7.setStatus(
        ""
    )

fsp_II_2k_TDMLocClockChange8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 143)
)
fsp_II_2k_TDMLocClockChange8.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_TDMLocClockChange8.setStatus(
        ""
    )

fsp_II_2k_RemoteClockNoSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 170)
)
fsp_II_2k_RemoteClockNoSync.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClockNoSync.setStatus(
        ""
    )

fsp_II_2k_RemoteClockSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 171)
)
fsp_II_2k_RemoteClockSync.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClockSync.setStatus(
        ""
    )

fsp_II_2k_RemoteClock2NoSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 172)
)
fsp_II_2k_RemoteClock2NoSync.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClock2NoSync.setStatus(
        ""
    )

fsp_II_2k_RemoteClock2Sync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 173)
)
fsp_II_2k_RemoteClock2Sync.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RemoteClock2Sync.setStatus(
        ""
    )

fsp_II_2k_RegeneratorModeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 180)
)
fsp_II_2k_RegeneratorModeOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RegeneratorModeOn.setStatus(
        ""
    )

fsp_II_2k_RegeneratorModeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 181)
)
fsp_II_2k_RegeneratorModeOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RegeneratorModeOff.setStatus(
        ""
    )

fsp_II_2k_RSM_OSC_OSCOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 210)
)
fsp_II_2k_RSM_OSC_OSCOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_OSC_OSCOn.setStatus(
        ""
    )

fsp_II_2k_RSM_OSC_OSCOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 211)
)
fsp_II_2k_RSM_OSC_OSCOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_RSM_OSC_OSCOff.setStatus(
        ""
    )

fsp_II_2k_EthPortSpeed10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 220)
)
fsp_II_2k_EthPortSpeed10.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortSpeed10.setStatus(
        ""
    )

fsp_II_2k_EthPortSpeed100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 221)
)
fsp_II_2k_EthPortSpeed100.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortSpeed100.setStatus(
        ""
    )

fsp_II_2k_EthPortDuplexHalf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 222)
)
fsp_II_2k_EthPortDuplexHalf.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortDuplexHalf.setStatus(
        ""
    )

fsp_II_2k_EthPortDuplexFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 223)
)
fsp_II_2k_EthPortDuplexFull.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortDuplexFull.setStatus(
        ""
    )

fsp_II_2k_EthPortAutonegOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 224)
)
fsp_II_2k_EthPortAutonegOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortAutonegOn.setStatus(
        ""
    )

fsp_II_2k_EthPortAutonegOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 225)
)
fsp_II_2k_EthPortAutonegOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortAutonegOff.setStatus(
        ""
    )

fsp_II_2k_EthPortPolarityPos = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 226)
)
fsp_II_2k_EthPortPolarityPos.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortPolarityPos.setStatus(
        ""
    )

fsp_II_2k_EthPortPolarityNeg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 227)
)
fsp_II_2k_EthPortPolarityNeg.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EthPortPolarityNeg.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Change2A = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 240)
)
fsp_II_2k_HotStandby_Change2A.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Change2A.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Change2B = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 241)
)
fsp_II_2k_HotStandby_Change2B.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Change2B.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 242)
)
fsp_II_2k_HotStandby_Locked.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Locked.setStatus(
        ""
    )

fsp_II_2k_HotStandby_Automatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 243)
)
fsp_II_2k_HotStandby_Automatic.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_HotStandby_Automatic.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttATToHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 250)
)
fsp_II_2k_OLM_LineAttATToHigh.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttATToHigh.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttATToLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 251)
)
fsp_II_2k_OLM_LineAttATToLow.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttATToLow.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttATNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 252)
)
fsp_II_2k_OLM_LineAttATNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttATNormal.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttARToHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 253)
)
fsp_II_2k_OLM_LineAttARToHigh.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttARToHigh.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttARToLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 254)
)
fsp_II_2k_OLM_LineAttARToLow.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttARToLow.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttARNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 255)
)
fsp_II_2k_OLM_LineAttARNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttARNormal.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttBTToHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 256)
)
fsp_II_2k_OLM_LineAttBTToHigh.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBTToHigh.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttBTToLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 257)
)
fsp_II_2k_OLM_LineAttBTToLow.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBTToLow.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttBTNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 258)
)
fsp_II_2k_OLM_LineAttBTNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBTNormal.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttBRToHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 259)
)
fsp_II_2k_OLM_LineAttBRToHigh.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBRToHigh.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttBRToLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 260)
)
fsp_II_2k_OLM_LineAttBRToLow.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBRToLow.setStatus(
        ""
    )

fsp_II_2k_OLM_LineAttBRNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 261)
)
fsp_II_2k_OLM_LineAttBRNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_OLM_LineAttBRNormal.setStatus(
        ""
    )

fsp_II_2k_EDFA_OIP_Loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 280)
)
fsp_II_2k_EDFA_OIP_Loss.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OIP_Loss.setStatus(
        ""
    )

fsp_II_2k_EDFA_OIP_High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 281)
)
fsp_II_2k_EDFA_OIP_High.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OIP_High.setStatus(
        ""
    )

fsp_II_2k_EDFA_OIP_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 282)
)
fsp_II_2k_EDFA_OIP_Normal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OIP_Normal.setStatus(
        ""
    )

fsp_II_2k_EDFA_IfMod_TempOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 283)
)
fsp_II_2k_EDFA_IfMod_TempOoR.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_IfMod_TempOoR.setStatus(
        ""
    )

fsp_II_2k_EDFA_IfMod_TempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 284)
)
fsp_II_2k_EDFA_IfMod_TempNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_IfMod_TempNormal.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_TxOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 285)
)
fsp_II_2k_EDFA_Pump_TxOff.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TxOff.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_TxOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 286)
)
fsp_II_2k_EDFA_Pump_TxOn.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TxOn.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_TempOoR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 287)
)
fsp_II_2k_EDFA_Pump_TempOoR.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TempOoR.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_TempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 288)
)
fsp_II_2k_EDFA_Pump_TempNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TempNormal.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_CurrentEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 289)
)
fsp_II_2k_EDFA_Pump_CurrentEoL.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_CurrentEoL.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_CurrNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 290)
)
fsp_II_2k_EDFA_Pump_CurrNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_CurrNormal.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_TECEoL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 291)
)
fsp_II_2k_EDFA_Pump_TECEoL.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TECEoL.setStatus(
        ""
    )

fsp_II_2k_EDFA_Pump_TECNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 292)
)
fsp_II_2k_EDFA_Pump_TECNormal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_Pump_TECNormal.setStatus(
        ""
    )

fsp_II_2k_EDFA_OOP_Loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 293)
)
fsp_II_2k_EDFA_OOP_Loss.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OOP_Loss.setStatus(
        ""
    )

fsp_II_2k_EDFA_OOP_Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 294)
)
fsp_II_2k_EDFA_OOP_Normal.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OOP_Normal.setStatus(
        ""
    )

fsp_II_2k_EDFA_OOP_Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 295)
)
fsp_II_2k_EDFA_OOP_Low.setObjects(
    ("FSP-II-Fsp-2000-R1-MIB", "fsp-II-2k-SlotNumber")
)
if mibBuilder.loadTexts:
    fsp_II_2k_EDFA_OOP_Low.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSP-II-Fsp-2000-R1-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "adva": adva,
       "products": products,
       "fsp-II-2k": fsp_II_2k,
       "fsp-II-2k-Main": fsp_II_2k_Main,
       "fsp-II-2k-Housing": fsp_II_2k_Housing,
       "fsp-II-2k-Manufacturer": fsp_II_2k_Manufacturer,
       "fsp-II-2k-MainType": fsp_II_2k_MainType,
       "fsp-II-2k-MainSerialNumber": fsp_II_2k_MainSerialNumber,
       "fsp-II-2k-MainHardwareVersion": fsp_II_2k_MainHardwareVersion,
       "fsp-II-2k-MainSoftwareVersion": fsp_II_2k_MainSoftwareVersion,
       "fsp-II-2k-MainBusMessages": fsp_II_2k_MainBusMessages,
       "fsp-II-2k-MainBusErrors": fsp_II_2k_MainBusErrors,
       "fsp-II-2k-MainLastEvent": fsp_II_2k_MainLastEvent,
       "fsp-II-2k-MainMotd": fsp_II_2k_MainMotd,
       "fsp-II-2k-MainTrapsinkTable": fsp_II_2k_MainTrapsinkTable,
       "fsp-II-2k-MainTrapsinkEntry": fsp_II_2k_MainTrapsinkEntry,
       "fsp-II-2k-MainTrapsinkNumber": fsp_II_2k_MainTrapsinkNumber,
       "fsp-II-2k-MainTrapsinkAddress": fsp_II_2k_MainTrapsinkAddress,
       "fsp-II-2k-MainTrapsinkCommunity": fsp_II_2k_MainTrapsinkCommunity,
       "fsp-II-2k-MainTrapsinkPriority": fsp_II_2k_MainTrapsinkPriority,
       "fsp-II-2k-MainLogfileTable": fsp_II_2k_MainLogfileTable,
       "fsp-II-2k-MainLogfileEntry": fsp_II_2k_MainLogfileEntry,
       "fsp-II-2k-MainLogfileNumber": fsp_II_2k_MainLogfileNumber,
       "fsp-II-2k-MainLogfileName": fsp_II_2k_MainLogfileName,
       "fsp-II-2k-MainLogfileSize": fsp_II_2k_MainLogfileSize,
       "fsp-II-2k-MainLogfilePriority": fsp_II_2k_MainLogfilePriority,
       "fsp-II-2k-MainProtocolVersion": fsp_II_2k_MainProtocolVersion,
       "fsp-II-2k-MainSystemVersion": fsp_II_2k_MainSystemVersion,
       "fsp-II-2k-MainConfigMismatch": fsp_II_2k_MainConfigMismatch,
       "fsp-II-2k-MainLastAuthFailSource": fsp_II_2k_MainLastAuthFailSource,
       "fsp-II-2k-MainLastAuthFailDescr": fsp_II_2k_MainLastAuthFailDescr,
       "fsp-II-2k-SlotTable": fsp_II_2k_SlotTable,
       "fsp-II-2k-SlotEntry": fsp_II_2k_SlotEntry,
       "fsp-II-2k-SlotNumber": fsp_II_2k_SlotNumber,
       "fsp-II-2k-Type": fsp_II_2k_Type,
       "fsp-II-2k-SlotTypeNumber": fsp_II_2k_SlotTypeNumber,
       "fsp-II-2k-SerialNumber": fsp_II_2k_SerialNumber,
       "fsp-II-2k-HardwareVersion": fsp_II_2k_HardwareVersion,
       "fsp-II-2k-SoftwareVersion": fsp_II_2k_SoftwareVersion,
       "fsp-II-2k-Temperature": fsp_II_2k_Temperature,
       "fsp-II-2k-BoardVoltage": fsp_II_2k_BoardVoltage,
       "fsp-II-2k-DetailInfo": fsp_II_2k_DetailInfo,
       "fsp-II-2k-EPLDVersion": fsp_II_2k_EPLDVersion,
       "fsp-II-2k-CustomerLabel": fsp_II_2k_CustomerLabel,
       "fsp-II-2k-ProductionVersion": fsp_II_2k_ProductionVersion,
       "fsp-II-2k-SlotSubType": fsp_II_2k_SlotSubType,
       "fsp-II-2k-SlotAlias": fsp_II_2k_SlotAlias,
       "fsp-II-2k-SlotComment": fsp_II_2k_SlotComment,
       "fsp-II-2k-PSTable": fsp_II_2k_PSTable,
       "fsp-II-2k-PSEntry": fsp_II_2k_PSEntry,
       "fsp-II-2k-PSNumber": fsp_II_2k_PSNumber,
       "fsp-II-2k-PSOn": fsp_II_2k_PSOn,
       "fsp-II-2k-FanTable": fsp_II_2k_FanTable,
       "fsp-II-2k-FanEntry": fsp_II_2k_FanEntry,
       "fsp-II-2k-FanNumber": fsp_II_2k_FanNumber,
       "fsp-II-2k-FanOn": fsp_II_2k_FanOn,
       "fsp-II-2k-Converter": fsp_II_2k_Converter,
       "fsp-II-2k-ConverterTable": fsp_II_2k_ConverterTable,
       "fsp-II-2k-ConverterEntry": fsp_II_2k_ConverterEntry,
       "fsp-II-2k-ConverterNumber": fsp_II_2k_ConverterNumber,
       "fsp-II-2k-RxLoc": fsp_II_2k_RxLoc,
       "fsp-II-2k-TxLoc": fsp_II_2k_TxLoc,
       "fsp-II-2k-TxLocC": fsp_II_2k_TxLocC,
       "fsp-II-2k-TxLocTemp": fsp_II_2k_TxLocTemp,
       "fsp-II-2k-RxRem": fsp_II_2k_RxRem,
       "fsp-II-2k-TxRem": fsp_II_2k_TxRem,
       "fsp-II-2k-TxRemC": fsp_II_2k_TxRemC,
       "fsp-II-2k-TxRemTemp": fsp_II_2k_TxRemTemp,
       "fsp-II-2k-RxRem2": fsp_II_2k_RxRem2,
       "fsp-II-2k-ClockState": fsp_II_2k_ClockState,
       "fsp-II-2k-ClockFreq": fsp_II_2k_ClockFreq,
       "fsp-II-2k-LocLoop": fsp_II_2k_LocLoop,
       "fsp-II-2k-RemLoop": fsp_II_2k_RemLoop,
       "fsp-II-2k-ClockType": fsp_II_2k_ClockType,
       "fsp-II-2k-HotStandby-ActiveLine": fsp_II_2k_HotStandby_ActiveLine,
       "fsp-II-2k-HotStandby-LineLocked": fsp_II_2k_HotStandby_LineLocked,
       "fsp-II-2k-LocalConnector": fsp_II_2k_LocalConnector,
       "fsp-II-2k-LocalLaserType": fsp_II_2k_LocalLaserType,
       "fsp-II-2k-RemoteConnector": fsp_II_2k_RemoteConnector,
       "fsp-II-2k-RemoteLaserType": fsp_II_2k_RemoteLaserType,
       "fsp-II-2k-ConverterType": fsp_II_2k_ConverterType,
       "fsp-II-2k-ClockRecovery": fsp_II_2k_ClockRecovery,
       "fsp-II-2k-SupDataRateTransp": fsp_II_2k_SupDataRateTransp,
       "fsp-II-2k-SupDataRateClocked": fsp_II_2k_SupDataRateClocked,
       "fsp-II-2k-ChannelNumber": fsp_II_2k_ChannelNumber,
       "fsp-II-2k-RemoteClockState": fsp_II_2k_RemoteClockState,
       "fsp-II-2k-RemoteClockState2": fsp_II_2k_RemoteClockState2,
       "fsp-II-2k-RegeneratorMode": fsp_II_2k_RegeneratorMode,
       "fsp-II-2k-ClockGenericTable": fsp_II_2k_ClockGenericTable,
       "fsp-II-2k-ClockGenericEntry": fsp_II_2k_ClockGenericEntry,
       "fsp-II-2k-ClockGenericFreq": fsp_II_2k_ClockGenericFreq,
       "fsp-II-2k-ClockGenericType": fsp_II_2k_ClockGenericType,
       "fsp-II-2k-Switch": fsp_II_2k_Switch,
       "fsp-II-2k-SwitchTable": fsp_II_2k_SwitchTable,
       "fsp-II-2k-SwitchEntry": fsp_II_2k_SwitchEntry,
       "fsp-II-2k-SwitchNumber": fsp_II_2k_SwitchNumber,
       "fsp-II-2k-SwitchLine": fsp_II_2k_SwitchLine,
       "fsp-II-2k-SwitchMode": fsp_II_2k_SwitchMode,
       "fsp-II-2k-SwitchLaserOn": fsp_II_2k_SwitchLaserOn,
       "fsp-II-2k-SwitchLineAavail": fsp_II_2k_SwitchLineAavail,
       "fsp-II-2k-SwitchLineBavail": fsp_II_2k_SwitchLineBavail,
       "fsp-II-2k-SwitchALS": fsp_II_2k_SwitchALS,
       "fsp-II-2k-SwitchConnector": fsp_II_2k_SwitchConnector,
       "fsp-II-2k-SwitchRemoteLaserType": fsp_II_2k_SwitchRemoteLaserType,
       "fsp-II-2k-RSM-OSC": fsp_II_2k_RSM_OSC,
       "fsp-II-2k-RSM-Table": fsp_II_2k_RSM_Table,
       "fsp-II-2k-RSM-Entry": fsp_II_2k_RSM_Entry,
       "fsp-II-2k-RSM-Number": fsp_II_2k_RSM_Number,
       "fsp-II-2k-RSM-Line": fsp_II_2k_RSM_Line,
       "fsp-II-2k-RSM-Mode": fsp_II_2k_RSM_Mode,
       "fsp-II-2k-RSM-LaserOn": fsp_II_2k_RSM_LaserOn,
       "fsp-II-2k-RSM-LineAavail": fsp_II_2k_RSM_LineAavail,
       "fsp-II-2k-RSM-LineBavail": fsp_II_2k_RSM_LineBavail,
       "fsp-II-2k-RSM-Control": fsp_II_2k_RSM_Control,
       "fsp-II-2k-RSM-Connector": fsp_II_2k_RSM_Connector,
       "fsp-II-2k-RSM-RemoteLaserType": fsp_II_2k_RSM_RemoteLaserType,
       "fsp-II-2k-OSC-Table": fsp_II_2k_OSC_Table,
       "fsp-II-2k-OSC-Entry": fsp_II_2k_OSC_Entry,
       "fsp-II-2k-OSC-Number": fsp_II_2k_OSC_Number,
       "fsp-II-2k-OSC-LaserOn": fsp_II_2k_OSC_LaserOn,
       "fsp-II-2k-OSC-P1-fail": fsp_II_2k_OSC_P1_fail,
       "fsp-II-2k-OSC-P2-fail": fsp_II_2k_OSC_P2_fail,
       "fsp-II-2k-OSC-PortEnable1": fsp_II_2k_OSC_PortEnable1,
       "fsp-II-2k-OSC-PortSpeed1": fsp_II_2k_OSC_PortSpeed1,
       "fsp-II-2k-OSC-PortDuplex1": fsp_II_2k_OSC_PortDuplex1,
       "fsp-II-2k-OSC-PortAutoneg1": fsp_II_2k_OSC_PortAutoneg1,
       "fsp-II-2k-OSC-PortPolarity1": fsp_II_2k_OSC_PortPolarity1,
       "fsp-II-2k-OSC-PortLinkStatus1": fsp_II_2k_OSC_PortLinkStatus1,
       "fsp-II-2k-OSC-PortEnable2": fsp_II_2k_OSC_PortEnable2,
       "fsp-II-2k-OSC-PortSpeed2": fsp_II_2k_OSC_PortSpeed2,
       "fsp-II-2k-OSC-PortDuplex2": fsp_II_2k_OSC_PortDuplex2,
       "fsp-II-2k-OSC-PortAutoneg2": fsp_II_2k_OSC_PortAutoneg2,
       "fsp-II-2k-OSC-PortPolarity2": fsp_II_2k_OSC_PortPolarity2,
       "fsp-II-2k-OSC-PortLinkStatus2": fsp_II_2k_OSC_PortLinkStatus2,
       "fsp-II-2k-OSC-PortEnable3": fsp_II_2k_OSC_PortEnable3,
       "fsp-II-2k-OSC-PortSpeed3": fsp_II_2k_OSC_PortSpeed3,
       "fsp-II-2k-OSC-PortDuplex3": fsp_II_2k_OSC_PortDuplex3,
       "fsp-II-2k-OSC-PortAutoneg3": fsp_II_2k_OSC_PortAutoneg3,
       "fsp-II-2k-OSC-PortPolarity3": fsp_II_2k_OSC_PortPolarity3,
       "fsp-II-2k-OSC-PortLinkStatus3": fsp_II_2k_OSC_PortLinkStatus3,
       "fsp-II-2k-OSC-PortEnable4": fsp_II_2k_OSC_PortEnable4,
       "fsp-II-2k-OSC-PortSpeed4": fsp_II_2k_OSC_PortSpeed4,
       "fsp-II-2k-OSC-PortDuplex4": fsp_II_2k_OSC_PortDuplex4,
       "fsp-II-2k-OSC-PortAutoneg4": fsp_II_2k_OSC_PortAutoneg4,
       "fsp-II-2k-OSC-PortPolarity4": fsp_II_2k_OSC_PortPolarity4,
       "fsp-II-2k-OSC-PortLinkStatus4": fsp_II_2k_OSC_PortLinkStatus4,
       "fsp-II-2k-OSC-PortEnable5": fsp_II_2k_OSC_PortEnable5,
       "fsp-II-2k-OSC-PortSpeed5": fsp_II_2k_OSC_PortSpeed5,
       "fsp-II-2k-OSC-PortDuplex5": fsp_II_2k_OSC_PortDuplex5,
       "fsp-II-2k-OSC-PortAutoneg5": fsp_II_2k_OSC_PortAutoneg5,
       "fsp-II-2k-OSC-PortPolarity5": fsp_II_2k_OSC_PortPolarity5,
       "fsp-II-2k-OSC-PortLinkStatus5": fsp_II_2k_OSC_PortLinkStatus5,
       "fsp-II-2k-OSC-PortEnable6": fsp_II_2k_OSC_PortEnable6,
       "fsp-II-2k-OSC-PortSpeed6": fsp_II_2k_OSC_PortSpeed6,
       "fsp-II-2k-OSC-PortDuplex6": fsp_II_2k_OSC_PortDuplex6,
       "fsp-II-2k-OSC-PortLinkStatus6": fsp_II_2k_OSC_PortLinkStatus6,
       "fsp-II-2k-OSC-Connector": fsp_II_2k_OSC_Connector,
       "fsp-II-2k-OSC-RemoteLaserType": fsp_II_2k_OSC_RemoteLaserType,
       "fsp-II-2k-OLM-Table": fsp_II_2k_OLM_Table,
       "fsp-II-2k-OLM-Entry": fsp_II_2k_OLM_Entry,
       "fsp-II-2k-OLM-Number": fsp_II_2k_OLM_Number,
       "fsp-II-2k-OLM-SwitchOver": fsp_II_2k_OLM_SwitchOver,
       "fsp-II-2k-OLM-Threshold": fsp_II_2k_OLM_Threshold,
       "fsp-II-2k-OLM-Hysteresis": fsp_II_2k_OLM_Hysteresis,
       "fsp-II-2k-OLM-HighAlarmLevel": fsp_II_2k_OLM_HighAlarmLevel,
       "fsp-II-2k-OLM-LowAlarmLevel": fsp_II_2k_OLM_LowAlarmLevel,
       "fsp-II-2k-OLM-LineAttAT": fsp_II_2k_OLM_LineAttAT,
       "fsp-II-2k-OLM-LineAttAR": fsp_II_2k_OLM_LineAttAR,
       "fsp-II-2k-OLM-LineAttBT": fsp_II_2k_OLM_LineAttBT,
       "fsp-II-2k-OLM-LineAttBR": fsp_II_2k_OLM_LineAttBR,
       "fsp-II-2k-OLM-OIP-StateA": fsp_II_2k_OLM_OIP_StateA,
       "fsp-II-2k-OLM-OIP-StateB": fsp_II_2k_OLM_OIP_StateB,
       "fsp-II-2k-EthHub": fsp_II_2k_EthHub,
       "fsp-II-2k-EthHubTable": fsp_II_2k_EthHubTable,
       "fsp-II-2k-EthHubEntry": fsp_II_2k_EthHubEntry,
       "fsp-II-2k-EthHubNumber": fsp_II_2k_EthHubNumber,
       "fsp-II-2k-EthHubPortEnable1": fsp_II_2k_EthHubPortEnable1,
       "fsp-II-2k-EthHubPortPartStatus1": fsp_II_2k_EthHubPortPartStatus1,
       "fsp-II-2k-EthHubPortLinkStatus1": fsp_II_2k_EthHubPortLinkStatus1,
       "fsp-II-2k-EthHubPortPolarity1": fsp_II_2k_EthHubPortPolarity1,
       "fsp-II-2k-EthHubPortEnable2": fsp_II_2k_EthHubPortEnable2,
       "fsp-II-2k-EthHubPortPartStatus2": fsp_II_2k_EthHubPortPartStatus2,
       "fsp-II-2k-EthHubPortLinkStatus2": fsp_II_2k_EthHubPortLinkStatus2,
       "fsp-II-2k-EthHubPortPolarity2": fsp_II_2k_EthHubPortPolarity2,
       "fsp-II-2k-EthHubPortEnable3": fsp_II_2k_EthHubPortEnable3,
       "fsp-II-2k-EthHubPortPartStatus3": fsp_II_2k_EthHubPortPartStatus3,
       "fsp-II-2k-EthHubPortLinkStatus3": fsp_II_2k_EthHubPortLinkStatus3,
       "fsp-II-2k-EthHubPortPolarity3": fsp_II_2k_EthHubPortPolarity3,
       "fsp-II-2k-EthHubPortEnable4": fsp_II_2k_EthHubPortEnable4,
       "fsp-II-2k-EthHubPortPartStatus4": fsp_II_2k_EthHubPortPartStatus4,
       "fsp-II-2k-EthHubPortLinkStatus4": fsp_II_2k_EthHubPortLinkStatus4,
       "fsp-II-2k-EthHubPortPolarity4": fsp_II_2k_EthHubPortPolarity4,
       "fsp-II-2k-EthHubPortEnable5": fsp_II_2k_EthHubPortEnable5,
       "fsp-II-2k-EthHubPortPartStatus5": fsp_II_2k_EthHubPortPartStatus5,
       "fsp-II-2k-EthHubPortLinkStatus5": fsp_II_2k_EthHubPortLinkStatus5,
       "fsp-II-2k-EthHubPortPolarity5": fsp_II_2k_EthHubPortPolarity5,
       "fsp-II-2k-TDM": fsp_II_2k_TDM,
       "fsp-II-2k-TDMTable": fsp_II_2k_TDMTable,
       "fsp-II-2k-TDMEntry": fsp_II_2k_TDMEntry,
       "fsp-II-2k-TDMNumber": fsp_II_2k_TDMNumber,
       "fsp-II-2k-TDMRxRem": fsp_II_2k_TDMRxRem,
       "fsp-II-2k-TDMRxSync": fsp_II_2k_TDMRxSync,
       "fsp-II-2k-TDMTxRem": fsp_II_2k_TDMTxRem,
       "fsp-II-2k-TDMTxRemC": fsp_II_2k_TDMTxRemC,
       "fsp-II-2k-TDMTxRemTemp": fsp_II_2k_TDMTxRemTemp,
       "fsp-II-2k-TDMLocLoop": fsp_II_2k_TDMLocLoop,
       "fsp-II-2k-TDMClockType": fsp_II_2k_TDMClockType,
       "fsp-II-2k-TDMRemLoop": fsp_II_2k_TDMRemLoop,
       "fsp-II-2k-TDMLocInst1": fsp_II_2k_TDMLocInst1,
       "fsp-II-2k-TDMLocEnable1": fsp_II_2k_TDMLocEnable1,
       "fsp-II-2k-TDMLocRx1": fsp_II_2k_TDMLocRx1,
       "fsp-II-2k-TDMLocTx1": fsp_II_2k_TDMLocTx1,
       "fsp-II-2k-TDMLocRemoteData1": fsp_II_2k_TDMLocRemoteData1,
       "fsp-II-2k-TDMLocClockFrequency1": fsp_II_2k_TDMLocClockFrequency1,
       "fsp-II-2k-TDMLocClockError1": fsp_II_2k_TDMLocClockError1,
       "fsp-II-2k-TDMLocLoop1": fsp_II_2k_TDMLocLoop1,
       "fsp-II-2k-TDMLocInst2": fsp_II_2k_TDMLocInst2,
       "fsp-II-2k-TDMLocEnable2": fsp_II_2k_TDMLocEnable2,
       "fsp-II-2k-TDMLocRx2": fsp_II_2k_TDMLocRx2,
       "fsp-II-2k-TDMLocTx2": fsp_II_2k_TDMLocTx2,
       "fsp-II-2k-TDMLocRemoteData2": fsp_II_2k_TDMLocRemoteData2,
       "fsp-II-2k-TDMLocClockFrequency2": fsp_II_2k_TDMLocClockFrequency2,
       "fsp-II-2k-TDMLocClockError2": fsp_II_2k_TDMLocClockError2,
       "fsp-II-2k-TDMLocLoop2": fsp_II_2k_TDMLocLoop2,
       "fsp-II-2k-TDMLocInst3": fsp_II_2k_TDMLocInst3,
       "fsp-II-2k-TDMLocEnable3": fsp_II_2k_TDMLocEnable3,
       "fsp-II-2k-TDMLocRx3": fsp_II_2k_TDMLocRx3,
       "fsp-II-2k-TDMLocTx3": fsp_II_2k_TDMLocTx3,
       "fsp-II-2k-TDMLocRemoteData3": fsp_II_2k_TDMLocRemoteData3,
       "fsp-II-2k-TDMLocClockFrequency3": fsp_II_2k_TDMLocClockFrequency3,
       "fsp-II-2k-TDMLocClockError3": fsp_II_2k_TDMLocClockError3,
       "fsp-II-2k-TDMLocInst4": fsp_II_2k_TDMLocInst4,
       "fsp-II-2k-TDMLocEnable4": fsp_II_2k_TDMLocEnable4,
       "fsp-II-2k-TDMLocRx4": fsp_II_2k_TDMLocRx4,
       "fsp-II-2k-TDMLocTx4": fsp_II_2k_TDMLocTx4,
       "fsp-II-2k-TDMLocRemoteData4": fsp_II_2k_TDMLocRemoteData4,
       "fsp-II-2k-TDMLocClockFrequency4": fsp_II_2k_TDMLocClockFrequency4,
       "fsp-II-2k-TDMLocClockError4": fsp_II_2k_TDMLocClockError4,
       "fsp-II-2k-TDMLocalConnector": fsp_II_2k_TDMLocalConnector,
       "fsp-II-2k-TDMLocalLaserType": fsp_II_2k_TDMLocalLaserType,
       "fsp-II-2k-TDMRemoteConnector": fsp_II_2k_TDMRemoteConnector,
       "fsp-II-2k-TDMRemoteLaserType": fsp_II_2k_TDMRemoteLaserType,
       "fsp-II-2k-TDMConverterType": fsp_II_2k_TDMConverterType,
       "fsp-II-2k-TDMClockRecovery": fsp_II_2k_TDMClockRecovery,
       "fsp-II-2k-TDMDataRateRange": fsp_II_2k_TDMDataRateRange,
       "fsp-II-2k-TDMClockFreqRange": fsp_II_2k_TDMClockFreqRange,
       "fsp-II-2k-TDMChannelNumber": fsp_II_2k_TDMChannelNumber,
       "fsp-II-2k-TDMLocInst5": fsp_II_2k_TDMLocInst5,
       "fsp-II-2k-TDMLocEnable5": fsp_II_2k_TDMLocEnable5,
       "fsp-II-2k-TDMLocRx5": fsp_II_2k_TDMLocRx5,
       "fsp-II-2k-TDMLocTx5": fsp_II_2k_TDMLocTx5,
       "fsp-II-2k-TDMLocRemoteData5": fsp_II_2k_TDMLocRemoteData5,
       "fsp-II-2k-TDMLocClockFrequency5": fsp_II_2k_TDMLocClockFrequency5,
       "fsp-II-2k-TDMLocClockError5": fsp_II_2k_TDMLocClockError5,
       "fsp-II-2k-TDMLocInst6": fsp_II_2k_TDMLocInst6,
       "fsp-II-2k-TDMLocEnable6": fsp_II_2k_TDMLocEnable6,
       "fsp-II-2k-TDMLocRx6": fsp_II_2k_TDMLocRx6,
       "fsp-II-2k-TDMLocTx6": fsp_II_2k_TDMLocTx6,
       "fsp-II-2k-TDMLocRemoteData6": fsp_II_2k_TDMLocRemoteData6,
       "fsp-II-2k-TDMLocClockFrequency6": fsp_II_2k_TDMLocClockFrequency6,
       "fsp-II-2k-TDMLocClockError6": fsp_II_2k_TDMLocClockError6,
       "fsp-II-2k-TDMLocInst7": fsp_II_2k_TDMLocInst7,
       "fsp-II-2k-TDMLocEnable7": fsp_II_2k_TDMLocEnable7,
       "fsp-II-2k-TDMLocRx7": fsp_II_2k_TDMLocRx7,
       "fsp-II-2k-TDMLocTx7": fsp_II_2k_TDMLocTx7,
       "fsp-II-2k-TDMLocRemoteData7": fsp_II_2k_TDMLocRemoteData7,
       "fsp-II-2k-TDMLocClockFrequency7": fsp_II_2k_TDMLocClockFrequency7,
       "fsp-II-2k-TDMLocClockError7": fsp_II_2k_TDMLocClockError7,
       "fsp-II-2k-TDMLocInst8": fsp_II_2k_TDMLocInst8,
       "fsp-II-2k-TDMLocEnable8": fsp_II_2k_TDMLocEnable8,
       "fsp-II-2k-TDMLocRx8": fsp_II_2k_TDMLocRx8,
       "fsp-II-2k-TDMLocTx8": fsp_II_2k_TDMLocTx8,
       "fsp-II-2k-TDMLocRemoteData8": fsp_II_2k_TDMLocRemoteData8,
       "fsp-II-2k-TDMLocClockFrequency8": fsp_II_2k_TDMLocClockFrequency8,
       "fsp-II-2k-TDMLocClockError8": fsp_II_2k_TDMLocClockError8,
       "fsp-II-2k-EDFA": fsp_II_2k_EDFA,
       "fsp-II-2k-EDFA-Table": fsp_II_2k_EDFA_Table,
       "fsp-II-2k-EDFA-Entry": fsp_II_2k_EDFA_Entry,
       "fsp-II-2k-EDFA-Number": fsp_II_2k_EDFA_Number,
       "fsp-II-2k-EDFA-Band": fsp_II_2k_EDFA_Band,
       "fsp-II-2k-EDFA-OIP": fsp_II_2k_EDFA_OIP,
       "fsp-II-2k-EDFA-OIP-State": fsp_II_2k_EDFA_OIP_State,
       "fsp-II-2k-EDFA-IfMod-Temp": fsp_II_2k_EDFA_IfMod_Temp,
       "fsp-II-2k-EDFA-IfMod-TempState": fsp_II_2k_EDFA_IfMod_TempState,
       "fsp-II-2k-EDFA-Pump-TxState": fsp_II_2k_EDFA_Pump_TxState,
       "fsp-II-2k-EDFA-Pump-Power": fsp_II_2k_EDFA_Pump_Power,
       "fsp-II-2k-EDFA-Pump-PowerMax": fsp_II_2k_EDFA_Pump_PowerMax,
       "fsp-II-2k-EDFA-Pump-PowerConf": fsp_II_2k_EDFA_Pump_PowerConf,
       "fsp-II-2k-EDFA-Pump-Temp": fsp_II_2k_EDFA_Pump_Temp,
       "fsp-II-2k-EDFA-Pump-TempState": fsp_II_2k_EDFA_Pump_TempState,
       "fsp-II-2k-EDFA-Pump-Current": fsp_II_2k_EDFA_Pump_Current,
       "fsp-II-2k-EDFA-Pump-CurrState": fsp_II_2k_EDFA_Pump_CurrState,
       "fsp-II-2k-EDFA-Pump-TECCurrent": fsp_II_2k_EDFA_Pump_TECCurrent,
       "fsp-II-2k-EDFA-Pump-TECState": fsp_II_2k_EDFA_Pump_TECState,
       "fsp-II-2k-EDFA-OOP": fsp_II_2k_EDFA_OOP,
       "fsp-II-2k-EDFA-OOP-State": fsp_II_2k_EDFA_OOP_State,
       "fsp-II-2k-MUX-DMX": fsp_II_2k_MUX_DMX,
       "fsp-II-2k-MUX-DMX-Table": fsp_II_2k_MUX_DMX_Table,
       "fsp-II-2k-MUX-DMX-Entry": fsp_II_2k_MUX_DMX_Entry,
       "fsp-II-2k-MUX-DMX-Number": fsp_II_2k_MUX_DMX_Number,
       "fsp-II-2k-MUX-DMX-WDMType": fsp_II_2k_MUX_DMX_WDMType,
       "fsp-II-2k-MUX-DMX-Scheme": fsp_II_2k_MUX_DMX_Scheme,
       "fsp-II-2k-MUX-DMX-ChannelRange": fsp_II_2k_MUX_DMX_ChannelRange,
       "fsp-II-2k-MUX-DMX-Connector": fsp_II_2k_MUX_DMX_Connector,
       "fsp-II-2k-MUX-DMX-UpgradePort": fsp_II_2k_MUX_DMX_UpgradePort,
       "fsp-II-2k-BSM": fsp_II_2k_BSM,
       "fsp-II-2k-BSM-Table": fsp_II_2k_BSM_Table,
       "fsp-II-2k-BSM-Entry": fsp_II_2k_BSM_Entry,
       "fsp-II-2k-BSM-Number": fsp_II_2k_BSM_Number,
       "fsp-II-2k-BSM-Scheme": fsp_II_2k_BSM_Scheme,
       "fsp-II-2k-BSM-BandRange": fsp_II_2k_BSM_BandRange,
       "fsp-II-2k-BSM-ConnectorType": fsp_II_2k_BSM_ConnectorType,
       "fsp-II-2k-Trap": fsp_II_2k_Trap,
       "fsp-II-2k-HardwareAdded": fsp_II_2k_HardwareAdded,
       "fsp-II-2k-HardwareDeleted": fsp_II_2k_HardwareDeleted,
       "fsp-II-2k-PSNotFail": fsp_II_2k_PSNotFail,
       "fsp-II-2k-PSFail": fsp_II_2k_PSFail,
       "fsp-II-2k-FanNotFail": fsp_II_2k_FanNotFail,
       "fsp-II-2k-FanFail": fsp_II_2k_FanFail,
       "fsp-II-2k-BusNotFail": fsp_II_2k_BusNotFail,
       "fsp-II-2k-BusFail": fsp_II_2k_BusFail,
       "fsp-II-2k-ConfigMismatch": fsp_II_2k_ConfigMismatch,
       "fsp-II-2k-RxLocOn": fsp_II_2k_RxLocOn,
       "fsp-II-2k-RxLocOff": fsp_II_2k_RxLocOff,
       "fsp-II-2k-TxLocOn": fsp_II_2k_TxLocOn,
       "fsp-II-2k-TxLocOff": fsp_II_2k_TxLocOff,
       "fsp-II-2k-RxRemOn": fsp_II_2k_RxRemOn,
       "fsp-II-2k-RxRemOff": fsp_II_2k_RxRemOff,
       "fsp-II-2k-TxRemOn": fsp_II_2k_TxRemOn,
       "fsp-II-2k-TxRemOff": fsp_II_2k_TxRemOff,
       "fsp-II-2k-RxRem2On": fsp_II_2k_RxRem2On,
       "fsp-II-2k-RxRem2Off": fsp_II_2k_RxRem2Off,
       "fsp-II-2k-TxRem2On": fsp_II_2k_TxRem2On,
       "fsp-II-2k-TxRem2Off": fsp_II_2k_TxRem2Off,
       "fsp-II-2k-ClockNoFail": fsp_II_2k_ClockNoFail,
       "fsp-II-2k-ClockFail": fsp_II_2k_ClockFail,
       "fsp-II-2k-ClockChangeFrequency": fsp_II_2k_ClockChangeFrequency,
       "fsp-II-2k-LocLoopOn": fsp_II_2k_LocLoopOn,
       "fsp-II-2k-LocLoopOff": fsp_II_2k_LocLoopOff,
       "fsp-II-2k-RemLoopOn": fsp_II_2k_RemLoopOn,
       "fsp-II-2k-RemLoopOff": fsp_II_2k_RemLoopOff,
       "fsp-II-2k-switchRefLaserOn": fsp_II_2k_switchRefLaserOn,
       "fsp-II-2k-switchRefLaserOff": fsp_II_2k_switchRefLaserOff,
       "fsp-II-2k-switchToA": fsp_II_2k_switchToA,
       "fsp-II-2k-switchToB": fsp_II_2k_switchToB,
       "fsp-II-2k-switchAutomatic": fsp_II_2k_switchAutomatic,
       "fsp-II-2k-switchLocked": fsp_II_2k_switchLocked,
       "fsp-II-2k-switchLineAavailAgain": fsp_II_2k_switchLineAavailAgain,
       "fsp-II-2k-switchLineANotAvail": fsp_II_2k_switchLineANotAvail,
       "fsp-II-2k-switchLineBavailAgain": fsp_II_2k_switchLineBavailAgain,
       "fsp-II-2k-switchLineBNotAvail": fsp_II_2k_switchLineBNotAvail,
       "fsp-II-2k-repeatedMessage": fsp_II_2k_repeatedMessage,
       "fsp-II-2k-INNCDown": fsp_II_2k_INNCDown,
       "fsp-II-2k-INNCUp": fsp_II_2k_INNCUp,
       "fsp-II-2k-switchALSOn": fsp_II_2k_switchALSOn,
       "fsp-II-2k-switchALSOff": fsp_II_2k_switchALSOff,
       "fsp-II-2k-NEMIAuthFail": fsp_II_2k_NEMIAuthFail,
       "fsp-II-2k-EthPortEnable": fsp_II_2k_EthPortEnable,
       "fsp-II-2k-EthPortDisable": fsp_II_2k_EthPortDisable,
       "fsp-II-2k-EthPortPartitioned": fsp_II_2k_EthPortPartitioned,
       "fsp-II-2k-EthPortNotPartitioned": fsp_II_2k_EthPortNotPartitioned,
       "fsp-II-2k-EthPortLinkPulses": fsp_II_2k_EthPortLinkPulses,
       "fsp-II-2k-EthPortNoLinkPulses": fsp_II_2k_EthPortNoLinkPulses,
       "fsp-II-2k-TDMRemoteSyncLoss": fsp_II_2k_TDMRemoteSyncLoss,
       "fsp-II-2k-TDMRemoteSync": fsp_II_2k_TDMRemoteSync,
       "fsp-II-2k-TDMLocEnabled1": fsp_II_2k_TDMLocEnabled1,
       "fsp-II-2k-TDMLocDisable1": fsp_II_2k_TDMLocDisable1,
       "fsp-II-2k-TDMLocEnabled2": fsp_II_2k_TDMLocEnabled2,
       "fsp-II-2k-TDMLocDisable2": fsp_II_2k_TDMLocDisable2,
       "fsp-II-2k-TDMLocEnabled3": fsp_II_2k_TDMLocEnabled3,
       "fsp-II-2k-TDMLocDisable3": fsp_II_2k_TDMLocDisable3,
       "fsp-II-2k-TDMLocEnabled4": fsp_II_2k_TDMLocEnabled4,
       "fsp-II-2k-TDMLocDisable4": fsp_II_2k_TDMLocDisable4,
       "fsp-II-2k-TDMLocEnabled5": fsp_II_2k_TDMLocEnabled5,
       "fsp-II-2k-TDMLocDisable5": fsp_II_2k_TDMLocDisable5,
       "fsp-II-2k-TDMLocEnabled6": fsp_II_2k_TDMLocEnabled6,
       "fsp-II-2k-TDMLocDisable6": fsp_II_2k_TDMLocDisable6,
       "fsp-II-2k-TDMLocEnabled7": fsp_II_2k_TDMLocEnabled7,
       "fsp-II-2k-TDMLocDisable7": fsp_II_2k_TDMLocDisable7,
       "fsp-II-2k-TDMLocEnabled8": fsp_II_2k_TDMLocEnabled8,
       "fsp-II-2k-TDMLocDisable8": fsp_II_2k_TDMLocDisable8,
       "fsp-II-2k-TDMLocRxOn1": fsp_II_2k_TDMLocRxOn1,
       "fsp-II-2k-TDMLocRxOff1": fsp_II_2k_TDMLocRxOff1,
       "fsp-II-2k-TDMLocRxOn2": fsp_II_2k_TDMLocRxOn2,
       "fsp-II-2k-TDMLocRxOff2": fsp_II_2k_TDMLocRxOff2,
       "fsp-II-2k-TDMLocRxOn3": fsp_II_2k_TDMLocRxOn3,
       "fsp-II-2k-TDMLocRxOff3": fsp_II_2k_TDMLocRxOff3,
       "fsp-II-2k-TDMLocRxOn4": fsp_II_2k_TDMLocRxOn4,
       "fsp-II-2k-TDMLocRxOff4": fsp_II_2k_TDMLocRxOff4,
       "fsp-II-2k-TDMLocRxOn5": fsp_II_2k_TDMLocRxOn5,
       "fsp-II-2k-TDMLocRxOff5": fsp_II_2k_TDMLocRxOff5,
       "fsp-II-2k-TDMLocRxOn6": fsp_II_2k_TDMLocRxOn6,
       "fsp-II-2k-TDMLocRxOff6": fsp_II_2k_TDMLocRxOff6,
       "fsp-II-2k-TDMLocRxOn7": fsp_II_2k_TDMLocRxOn7,
       "fsp-II-2k-TDMLocRxOff7": fsp_II_2k_TDMLocRxOff7,
       "fsp-II-2k-TDMLocRxOn8": fsp_II_2k_TDMLocRxOn8,
       "fsp-II-2k-TDMLocRxOff8": fsp_II_2k_TDMLocRxOff8,
       "fsp-II-2k-TDMLocData1": fsp_II_2k_TDMLocData1,
       "fsp-II-2k-TDMLocNoData1": fsp_II_2k_TDMLocNoData1,
       "fsp-II-2k-TDMLocData2": fsp_II_2k_TDMLocData2,
       "fsp-II-2k-TDMLocNoData2": fsp_II_2k_TDMLocNoData2,
       "fsp-II-2k-TDMLocData3": fsp_II_2k_TDMLocData3,
       "fsp-II-2k-TDMLocNoData3": fsp_II_2k_TDMLocNoData3,
       "fsp-II-2k-TDMLocData4": fsp_II_2k_TDMLocData4,
       "fsp-II-2k-TDMLocNoData4": fsp_II_2k_TDMLocNoData4,
       "fsp-II-2k-TDMLocData5": fsp_II_2k_TDMLocData5,
       "fsp-II-2k-TDMLocNoData5": fsp_II_2k_TDMLocNoData5,
       "fsp-II-2k-TDMLocData6": fsp_II_2k_TDMLocData6,
       "fsp-II-2k-TDMLocNoData6": fsp_II_2k_TDMLocNoData6,
       "fsp-II-2k-TDMLocData7": fsp_II_2k_TDMLocData7,
       "fsp-II-2k-TDMLocNoData7": fsp_II_2k_TDMLocNoData7,
       "fsp-II-2k-TDMLocData8": fsp_II_2k_TDMLocData8,
       "fsp-II-2k-TDMLocNoData8": fsp_II_2k_TDMLocNoData8,
       "fsp-II-2k-TDMLocClockFail1": fsp_II_2k_TDMLocClockFail1,
       "fsp-II-2k-TDMLocClockNoFail1": fsp_II_2k_TDMLocClockNoFail1,
       "fsp-II-2k-TDMLocClockFail2": fsp_II_2k_TDMLocClockFail2,
       "fsp-II-2k-TDMLocClockNoFail2": fsp_II_2k_TDMLocClockNoFail2,
       "fsp-II-2k-TDMLocClockFail3": fsp_II_2k_TDMLocClockFail3,
       "fsp-II-2k-TDMLocClockNoFail3": fsp_II_2k_TDMLocClockNoFail3,
       "fsp-II-2k-TDMLocClockFail4": fsp_II_2k_TDMLocClockFail4,
       "fsp-II-2k-TDMLocClockNoFail4": fsp_II_2k_TDMLocClockNoFail4,
       "fsp-II-2k-TDMLocClockFail5": fsp_II_2k_TDMLocClockFail5,
       "fsp-II-2k-TDMLocClockNoFail5": fsp_II_2k_TDMLocClockNoFail5,
       "fsp-II-2k-TDMLocClockFail6": fsp_II_2k_TDMLocClockFail6,
       "fsp-II-2k-TDMLocClockNoFail6": fsp_II_2k_TDMLocClockNoFail6,
       "fsp-II-2k-TDMLocClockFail7": fsp_II_2k_TDMLocClockFail7,
       "fsp-II-2k-TDMLocClockNoFail7": fsp_II_2k_TDMLocClockNoFail7,
       "fsp-II-2k-TDMLocClockFail8": fsp_II_2k_TDMLocClockFail8,
       "fsp-II-2k-TDMLocClockNoFail8": fsp_II_2k_TDMLocClockNoFail8,
       "fsp-II-2k-TDMLocClockChange1": fsp_II_2k_TDMLocClockChange1,
       "fsp-II-2k-TDMLocClockChange2": fsp_II_2k_TDMLocClockChange2,
       "fsp-II-2k-TDMLocClockChange3": fsp_II_2k_TDMLocClockChange3,
       "fsp-II-2k-TDMLocClockChange4": fsp_II_2k_TDMLocClockChange4,
       "fsp-II-2k-TDMLocClockChange5": fsp_II_2k_TDMLocClockChange5,
       "fsp-II-2k-TDMLocClockChange6": fsp_II_2k_TDMLocClockChange6,
       "fsp-II-2k-TDMLocClockChange7": fsp_II_2k_TDMLocClockChange7,
       "fsp-II-2k-TDMLocClockChange8": fsp_II_2k_TDMLocClockChange8,
       "fsp-II-2k-RemoteClockNoSync": fsp_II_2k_RemoteClockNoSync,
       "fsp-II-2k-RemoteClockSync": fsp_II_2k_RemoteClockSync,
       "fsp-II-2k-RemoteClock2NoSync": fsp_II_2k_RemoteClock2NoSync,
       "fsp-II-2k-RemoteClock2Sync": fsp_II_2k_RemoteClock2Sync,
       "fsp-II-2k-RegeneratorModeOn": fsp_II_2k_RegeneratorModeOn,
       "fsp-II-2k-RegeneratorModeOff": fsp_II_2k_RegeneratorModeOff,
       "fsp-II-2k-RSM-OSC-OSCOn": fsp_II_2k_RSM_OSC_OSCOn,
       "fsp-II-2k-RSM-OSC-OSCOff": fsp_II_2k_RSM_OSC_OSCOff,
       "fsp-II-2k-EthPortSpeed10": fsp_II_2k_EthPortSpeed10,
       "fsp-II-2k-EthPortSpeed100": fsp_II_2k_EthPortSpeed100,
       "fsp-II-2k-EthPortDuplexHalf": fsp_II_2k_EthPortDuplexHalf,
       "fsp-II-2k-EthPortDuplexFull": fsp_II_2k_EthPortDuplexFull,
       "fsp-II-2k-EthPortAutonegOn": fsp_II_2k_EthPortAutonegOn,
       "fsp-II-2k-EthPortAutonegOff": fsp_II_2k_EthPortAutonegOff,
       "fsp-II-2k-EthPortPolarityPos": fsp_II_2k_EthPortPolarityPos,
       "fsp-II-2k-EthPortPolarityNeg": fsp_II_2k_EthPortPolarityNeg,
       "fsp-II-2k-HotStandby-Change2A": fsp_II_2k_HotStandby_Change2A,
       "fsp-II-2k-HotStandby-Change2B": fsp_II_2k_HotStandby_Change2B,
       "fsp-II-2k-HotStandby-Locked": fsp_II_2k_HotStandby_Locked,
       "fsp-II-2k-HotStandby-Automatic": fsp_II_2k_HotStandby_Automatic,
       "fsp-II-2k-OLM-LineAttATToHigh": fsp_II_2k_OLM_LineAttATToHigh,
       "fsp-II-2k-OLM-LineAttATToLow": fsp_II_2k_OLM_LineAttATToLow,
       "fsp-II-2k-OLM-LineAttATNormal": fsp_II_2k_OLM_LineAttATNormal,
       "fsp-II-2k-OLM-LineAttARToHigh": fsp_II_2k_OLM_LineAttARToHigh,
       "fsp-II-2k-OLM-LineAttARToLow": fsp_II_2k_OLM_LineAttARToLow,
       "fsp-II-2k-OLM-LineAttARNormal": fsp_II_2k_OLM_LineAttARNormal,
       "fsp-II-2k-OLM-LineAttBTToHigh": fsp_II_2k_OLM_LineAttBTToHigh,
       "fsp-II-2k-OLM-LineAttBTToLow": fsp_II_2k_OLM_LineAttBTToLow,
       "fsp-II-2k-OLM-LineAttBTNormal": fsp_II_2k_OLM_LineAttBTNormal,
       "fsp-II-2k-OLM-LineAttBRToHigh": fsp_II_2k_OLM_LineAttBRToHigh,
       "fsp-II-2k-OLM-LineAttBRToLow": fsp_II_2k_OLM_LineAttBRToLow,
       "fsp-II-2k-OLM-LineAttBRNormal": fsp_II_2k_OLM_LineAttBRNormal,
       "fsp-II-2k-EDFA-OIP-Loss": fsp_II_2k_EDFA_OIP_Loss,
       "fsp-II-2k-EDFA-OIP-High": fsp_II_2k_EDFA_OIP_High,
       "fsp-II-2k-EDFA-OIP-Normal": fsp_II_2k_EDFA_OIP_Normal,
       "fsp-II-2k-EDFA-IfMod-TempOoR": fsp_II_2k_EDFA_IfMod_TempOoR,
       "fsp-II-2k-EDFA-IfMod-TempNormal": fsp_II_2k_EDFA_IfMod_TempNormal,
       "fsp-II-2k-EDFA-Pump-TxOff": fsp_II_2k_EDFA_Pump_TxOff,
       "fsp-II-2k-EDFA-Pump-TxOn": fsp_II_2k_EDFA_Pump_TxOn,
       "fsp-II-2k-EDFA-Pump-TempOoR": fsp_II_2k_EDFA_Pump_TempOoR,
       "fsp-II-2k-EDFA-Pump-TempNormal": fsp_II_2k_EDFA_Pump_TempNormal,
       "fsp-II-2k-EDFA-Pump-CurrentEoL": fsp_II_2k_EDFA_Pump_CurrentEoL,
       "fsp-II-2k-EDFA-Pump-CurrNormal": fsp_II_2k_EDFA_Pump_CurrNormal,
       "fsp-II-2k-EDFA-Pump-TECEoL": fsp_II_2k_EDFA_Pump_TECEoL,
       "fsp-II-2k-EDFA-Pump-TECNormal": fsp_II_2k_EDFA_Pump_TECNormal,
       "fsp-II-2k-EDFA-OOP-Loss": fsp_II_2k_EDFA_OOP_Loss,
       "fsp-II-2k-EDFA-OOP-Normal": fsp_II_2k_EDFA_OOP_Normal,
       "fsp-II-2k-EDFA-OOP-Low": fsp_II_2k_EDFA_OOP_Low}
)
