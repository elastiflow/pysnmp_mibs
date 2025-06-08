# SNMP MIB module (SCLESFE-MIB-ARKENSCC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scle_51435/SCLESFE-MIB-ARKENSCC.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:56:56 2025
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

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

(sclesfe,) = mibBuilder.importSymbols(
    "SCLESFE-MIB",
    "sclesfe")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

arkenscc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3)
)
if mibBuilder.loadTexts:
    arkenscc.setRevisions(
        ("2021-07-05 11:44",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EventDate(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1dT1d:1d:1d,1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class UTF8String(TextualConvention, OctetString):
    status = "current"
    displayHint = "65535t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



class Unsigned64(TextualConvention, Counter64):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1)
)


class _Type_Type(UTF8String):
    """Custom type type based on UTF8String"""
    defaultValue = OctetString("arkenscc")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Type_Type.__name__ = "UTF8String"
_Type_Object = MibScalar
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 1),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("current")


class _Manufacturer_Type(UTF8String):
    """Custom type manufacturer based on UTF8String"""
    defaultValue = OctetString("SCLE-SFE")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Manufacturer_Type.__name__ = "UTF8String"
_Manufacturer_Object = MibScalar
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 2),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")


class _Name_Type(UTF8String):
    """Custom type name based on UTF8String"""
    defaultValue = OctetString("Nom par defaut")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Name_Type.__name__ = "UTF8String"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 3),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _EqOGISPrefix_Type(UTF8String):
    """Custom type eqOGISPrefix based on UTF8String"""
    defaultValue = OctetString("0.0/0.0")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqOGISPrefix_Type.__name__ = "UTF8String"
_EqOGISPrefix_Object = MibScalar
eqOGISPrefix = _EqOGISPrefix_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 4),
    _EqOGISPrefix_Type()
)
eqOGISPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqOGISPrefix.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 5),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_IpRF_Type = InetAddressIPv4
_IpRF_Object = MibScalar
ipRF = _IpRF_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 6),
    _IpRF_Type()
)
ipRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRF.setStatus("current")
_IpRS_Type = InetAddressIPv4
_IpRS_Object = MibScalar
ipRS = _IpRS_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 7),
    _IpRS_Type()
)
ipRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRS.setStatus("current")


class _VersionLog_Type(UTF8String):
    """Custom type versionLog based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VersionLog_Type.__name__ = "UTF8String"
_VersionLog_Object = MibScalar
versionLog = _VersionLog_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 8),
    _VersionLog_Type()
)
versionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionLog.setStatus("current")


class _VersionProd_Type(UTF8String):
    """Custom type versionProd based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VersionProd_Type.__name__ = "UTF8String"
_VersionProd_Object = MibScalar
versionProd = _VersionProd_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 9),
    _VersionProd_Type()
)
versionProd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionProd.setStatus("current")


class _VersionSousProd_Type(UTF8String):
    """Custom type versionSousProd based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VersionSousProd_Type.__name__ = "UTF8String"
_VersionSousProd_Object = MibScalar
versionSousProd = _VersionSousProd_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 1, 10),
    _VersionSousProd_Type()
)
versionSousProd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionSousProd.setStatus("current")
_Devices_ObjectIdentity = ObjectIdentity
devices = _Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2)
)
_ElementTable_Object = MibTable
elementTable = _ElementTable_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2)
)
if mibBuilder.loadTexts:
    elementTable.setStatus("current")
_ElementEntry_Object = MibTableRow
elementEntry = _ElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1)
)
elementEntry.setIndexNames(
    (0, "SCLESFE-MIB-ARKENSCC", "elementIndex"),
)
if mibBuilder.loadTexts:
    elementEntry.setStatus("current")


class _ElementIndex_Type(Integer32):
    """Custom type elementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElementIndex_Type.__name__ = "Integer32"
_ElementIndex_Object = MibTableColumn
elementIndex = _ElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 1),
    _ElementIndex_Type()
)
elementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elementIndex.setStatus("current")


class _ElementOGISSuffix_Type(UTF8String):
    """Custom type elementOGISSuffix based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ElementOGISSuffix_Type.__name__ = "UTF8String"
_ElementOGISSuffix_Object = MibTableColumn
elementOGISSuffix = _ElementOGISSuffix_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 2),
    _ElementOGISSuffix_Type()
)
elementOGISSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementOGISSuffix.setStatus("current")


class _ElementVersion_Type(UTF8String):
    """Custom type elementVersion based on UTF8String"""
    defaultValue = OctetString("?")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ElementVersion_Type.__name__ = "UTF8String"
_ElementVersion_Object = MibTableColumn
elementVersion = _ElementVersion_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 3),
    _ElementVersion_Type()
)
elementVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementVersion.setStatus("current")


class _ElementDetail_Type(UTF8String):
    """Custom type elementDetail based on UTF8String"""
    defaultValue = OctetString("Valeur par defaut")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ElementDetail_Type.__name__ = "UTF8String"
_ElementDetail_Object = MibTableColumn
elementDetail = _ElementDetail_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 4),
    _ElementDetail_Type()
)
elementDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementDetail.setStatus("current")


class _ElementStatus_Type(Integer32):
    """Custom type elementStatus based on Integer32"""
    defaultValue = 1

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
        *(("nonConfigure", 1),
          ("nonFonctionnel", 2),
          ("fonctionnel", 3),
          ("nonApplicable", 4))
    )


_ElementStatus_Type.__name__ = "Integer32"
_ElementStatus_Object = MibTableColumn
elementStatus = _ElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 5),
    _ElementStatus_Type()
)
elementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementStatus.setStatus("current")


class _ElementName_Type(UTF8String):
    """Custom type elementName based on UTF8String"""
    defaultValue = OctetString("Valeur par defaut")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ElementName_Type.__name__ = "UTF8String"
_ElementName_Object = MibTableColumn
elementName = _ElementName_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 6),
    _ElementName_Type()
)
elementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementName.setStatus("current")


class _ElementUpdVersion_Type(UTF8String):
    """Custom type elementUpdVersion based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ElementUpdVersion_Type.__name__ = "UTF8String"
_ElementUpdVersion_Object = MibTableColumn
elementUpdVersion = _ElementUpdVersion_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 10),
    _ElementUpdVersion_Type()
)
elementUpdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementUpdVersion.setStatus("current")


class _ElementUpdDetail_Type(UTF8String):
    """Custom type elementUpdDetail based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ElementUpdDetail_Type.__name__ = "UTF8String"
_ElementUpdDetail_Object = MibTableColumn
elementUpdDetail = _ElementUpdDetail_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 11),
    _ElementUpdDetail_Type()
)
elementUpdDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementUpdDetail.setStatus("current")


class _ElementUpdWaiting_Type(Integer32):
    """Custom type elementUpdWaiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("priseEnCompte", 1),
          ("redemarrage", 2),
          ("aucun", 3))
    )


_ElementUpdWaiting_Type.__name__ = "Integer32"
_ElementUpdWaiting_Object = MibTableColumn
elementUpdWaiting = _ElementUpdWaiting_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 2, 1, 12),
    _ElementUpdWaiting_Type()
)
elementUpdWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementUpdWaiting.setStatus("current")
_NicTable_Object = MibTable
nicTable = _NicTable_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3)
)
if mibBuilder.loadTexts:
    nicTable.setStatus("current")
_NicEntry_Object = MibTableRow
nicEntry = _NicEntry_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1)
)
nicEntry.setIndexNames(
    (0, "SCLESFE-MIB-ARKENSCC", "nicIndex"),
)
if mibBuilder.loadTexts:
    nicEntry.setStatus("current")


class _NicIndex_Type(Integer32):
    """Custom type nicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NicIndex_Type.__name__ = "Integer32"
_NicIndex_Object = MibTableColumn
nicIndex = _NicIndex_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1, 1),
    _NicIndex_Type()
)
nicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nicIndex.setStatus("current")


class _NicName_Type(UTF8String):
    """Custom type nicName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NicName_Type.__name__ = "UTF8String"
_NicName_Object = MibTableColumn
nicName = _NicName_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1, 2),
    _NicName_Type()
)
nicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicName.setStatus("current")


class _NicDetail_Type(UTF8String):
    """Custom type nicDetail based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NicDetail_Type.__name__ = "UTF8String"
_NicDetail_Object = MibTableColumn
nicDetail = _NicDetail_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1, 3),
    _NicDetail_Type()
)
nicDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDetail.setStatus("current")
_NicMAC_Type = MacAddress
_NicMAC_Object = MibTableColumn
nicMAC = _NicMAC_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1, 4),
    _NicMAC_Type()
)
nicMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicMAC.setStatus("current")


class _NicStatus_Type(Integer32):
    """Custom type nicStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("cableNonBranche", 2),
          ("fonctionnel", 3))
    )


_NicStatus_Type.__name__ = "Integer32"
_NicStatus_Object = MibTableColumn
nicStatus = _NicStatus_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1, 5),
    _NicStatus_Type()
)
nicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicStatus.setStatus("current")
_NicIPoper_Type = InetAddressIPv4
_NicIPoper_Object = MibTableColumn
nicIPoper = _NicIPoper_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1, 6),
    _NicIPoper_Type()
)
nicIPoper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicIPoper.setStatus("current")
_NicIPmaint_Type = InetAddressIPv4
_NicIPmaint_Object = MibTableColumn
nicIPmaint = _NicIPmaint_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 3, 1, 7),
    _NicIPmaint_Type()
)
nicIPmaint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicIPmaint.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3)
)


class _State_Type(Integer32):
    """Custom type state based on Integer32"""
    defaultValue = 1

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
        *(("nonConfigure", 1),
          ("nonFonctionnel", 2),
          ("fonctionnel", 3),
          ("nonApplicable", 4))
    )


_State_Type.__name__ = "Integer32"
_State_Object = MibScalar
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 2),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("current")
_Temperatures_ObjectIdentity = ObjectIdentity
temperatures = _Temperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 3)
)


class _CpuTemp_Type(Integer32):
    """Custom type cpuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpuTemp_Type.__name__ = "Integer32"
_CpuTemp_Object = MibScalar
cpuTemp = _CpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 3, 1),
    _CpuTemp_Type()
)
cpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemp.setStatus("current")
if mibBuilder.loadTexts:
    cpuTemp.setUnits("?C")


class _CardTemp_Type(Integer32):
    """Custom type cardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CardTemp_Type.__name__ = "Integer32"
_CardTemp_Object = MibScalar
cardTemp = _CardTemp_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 3, 2),
    _CardTemp_Type()
)
cardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTemp.setStatus("current")
if mibBuilder.loadTexts:
    cardTemp.setUnits("?C")
_UsageLevels_ObjectIdentity = ObjectIdentity
usageLevels = _UsageLevels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 4)
)


class _CpuLevel_Type(Integer32):
    """Custom type cpuLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuLevel_Type.__name__ = "Integer32"
_CpuLevel_Object = MibScalar
cpuLevel = _CpuLevel_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 4, 1),
    _CpuLevel_Type()
)
cpuLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLevel.setStatus("current")
if mibBuilder.loadTexts:
    cpuLevel.setUnits("%")


class _MemLevel_Type(Integer32):
    """Custom type memLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MemLevel_Type.__name__ = "Integer32"
_MemLevel_Object = MibScalar
memLevel = _MemLevel_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 4, 2),
    _MemLevel_Type()
)
memLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memLevel.setStatus("current")
if mibBuilder.loadTexts:
    memLevel.setUnits("%")


class _Cpu2level_Type(Integer32):
    """Custom type cpu2level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cpu2level_Type.__name__ = "Integer32"
_Cpu2level_Object = MibScalar
cpu2level = _Cpu2level_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 4, 100),
    _Cpu2level_Type()
)
cpu2level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu2level.setStatus("current")
if mibBuilder.loadTexts:
    cpu2level.setUnits("%")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 5)
)
_StorageFree_Type = Unsigned64
_StorageFree_Object = MibScalar
storageFree = _StorageFree_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 5, 1),
    _StorageFree_Type()
)
storageFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageFree.setStatus("current")
if mibBuilder.loadTexts:
    storageFree.setUnits("B")
_StorageFTPFree_Type = Unsigned64
_StorageFTPFree_Object = MibScalar
storageFTPFree = _StorageFTPFree_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 5, 2),
    _StorageFTPFree_Type()
)
storageFTPFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageFTPFree.setStatus("current")
if mibBuilder.loadTexts:
    storageFTPFree.setUnits("B")


class _StorageFreePct_Type(Integer32):
    """Custom type storageFreePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StorageFreePct_Type.__name__ = "Integer32"
_StorageFreePct_Object = MibScalar
storageFreePct = _StorageFreePct_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 5, 3),
    _StorageFreePct_Type()
)
storageFreePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageFreePct.setStatus("current")
if mibBuilder.loadTexts:
    storageFreePct.setUnits("%")


class _StorageFTPFreePct_Type(Integer32):
    """Custom type storageFTPFreePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StorageFTPFreePct_Type.__name__ = "Integer32"
_StorageFTPFreePct_Object = MibScalar
storageFTPFreePct = _StorageFTPFreePct_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 5, 4),
    _StorageFTPFreePct_Type()
)
storageFTPFreePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageFTPFreePct.setStatus("current")
if mibBuilder.loadTexts:
    storageFTPFreePct.setUnits("%")
_Dates_ObjectIdentity = ObjectIdentity
dates = _Dates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 6)
)
_CurrentDate_Type = DateAndTime
_CurrentDate_Object = MibScalar
currentDate = _CurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 6, 1),
    _CurrentDate_Type()
)
currentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDate.setStatus("current")
_DateMajFW_Type = DateAndTime
_DateMajFW_Object = MibScalar
dateMajFW = _DateMajFW_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 6, 2),
    _DateMajFW_Type()
)
dateMajFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateMajFW.setStatus("current")
_DateMajConf_Type = DateAndTime
_DateMajConf_Object = MibScalar
dateMajConf = _DateMajConf_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 6, 3),
    _DateMajConf_Type()
)
dateMajConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateMajConf.setStatus("current")
_DateRedem_Type = Unsigned32
_DateRedem_Object = MibScalar
dateRedem = _DateRedem_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 6, 4),
    _DateRedem_Type()
)
dateRedem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateRedem.setStatus("current")
_Errors_ObjectIdentity = ObjectIdentity
errors = _Errors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11)
)
_Critical_ObjectIdentity = ObjectIdentity
critical = _Critical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1)
)


class _NbCritical_Type(Integer32):
    """Custom type nbCritical based on Integer32"""
    defaultValue = 0


_NbCritical_Type.__name__ = "Integer32"
_NbCritical_Object = MibScalar
nbCritical = _NbCritical_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 2),
    _NbCritical_Type()
)
nbCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbCritical.setStatus("current")
_CriticalTable_Object = MibTable
criticalTable = _CriticalTable_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 3)
)
if mibBuilder.loadTexts:
    criticalTable.setStatus("current")
_CriticalEntry_Object = MibTableRow
criticalEntry = _CriticalEntry_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 3, 1)
)
criticalEntry.setIndexNames(
    (0, "SCLESFE-MIB-ARKENSCC", "criticalIndex"),
)
if mibBuilder.loadTexts:
    criticalEntry.setStatus("current")


class _CriticalIndex_Type(Integer32):
    """Custom type criticalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CriticalIndex_Type.__name__ = "Integer32"
_CriticalIndex_Object = MibTableColumn
criticalIndex = _CriticalIndex_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 3, 1, 1),
    _CriticalIndex_Type()
)
criticalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    criticalIndex.setStatus("current")


class _CriticalDetail_Type(UTF8String):
    """Custom type criticalDetail based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CriticalDetail_Type.__name__ = "UTF8String"
_CriticalDetail_Object = MibTableColumn
criticalDetail = _CriticalDetail_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 3, 1, 2),
    _CriticalDetail_Type()
)
criticalDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticalDetail.setStatus("current")


class _CriticalOGISSuffix_Type(UTF8String):
    """Custom type criticalOGISSuffix based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CriticalOGISSuffix_Type.__name__ = "UTF8String"
_CriticalOGISSuffix_Object = MibTableColumn
criticalOGISSuffix = _CriticalOGISSuffix_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 3, 1, 3),
    _CriticalOGISSuffix_Type()
)
criticalOGISSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticalOGISSuffix.setStatus("current")
_CriticalTime_Type = EventDate
_CriticalTime_Object = MibTableColumn
criticalTime = _CriticalTime_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 3, 1, 4),
    _CriticalTime_Type()
)
criticalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticalTime.setStatus("current")
_Warning_ObjectIdentity = ObjectIdentity
warning = _Warning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2)
)


class _NbWarning_Type(Integer32):
    """Custom type nbWarning based on Integer32"""
    defaultValue = 0


_NbWarning_Type.__name__ = "Integer32"
_NbWarning_Object = MibScalar
nbWarning = _NbWarning_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 2),
    _NbWarning_Type()
)
nbWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbWarning.setStatus("current")
_WarningTable_Object = MibTable
warningTable = _WarningTable_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 3)
)
if mibBuilder.loadTexts:
    warningTable.setStatus("current")
_WarningEntry_Object = MibTableRow
warningEntry = _WarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 3, 1)
)
warningEntry.setIndexNames(
    (0, "SCLESFE-MIB-ARKENSCC", "warningIndex"),
)
if mibBuilder.loadTexts:
    warningEntry.setStatus("current")


class _WarningIndex_Type(Integer32):
    """Custom type warningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WarningIndex_Type.__name__ = "Integer32"
_WarningIndex_Object = MibTableColumn
warningIndex = _WarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 3, 1, 1),
    _WarningIndex_Type()
)
warningIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    warningIndex.setStatus("current")


class _WarningDetail_Type(UTF8String):
    """Custom type warningDetail based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WarningDetail_Type.__name__ = "UTF8String"
_WarningDetail_Object = MibTableColumn
warningDetail = _WarningDetail_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 3, 1, 2),
    _WarningDetail_Type()
)
warningDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningDetail.setStatus("current")


class _WarningOGISSuffix_Type(UTF8String):
    """Custom type warningOGISSuffix based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WarningOGISSuffix_Type.__name__ = "UTF8String"
_WarningOGISSuffix_Object = MibTableColumn
warningOGISSuffix = _WarningOGISSuffix_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 3, 1, 3),
    _WarningOGISSuffix_Type()
)
warningOGISSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningOGISSuffix.setStatus("current")
_WarningTime_Type = EventDate
_WarningTime_Object = MibTableColumn
warningTime = _WarningTime_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 3, 1, 4),
    _WarningTime_Type()
)
warningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningTime.setStatus("current")


class _AmsPresence_Type(Integer32):
    """Custom type amsPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AmsPresence_Type.__name__ = "Integer32"
_AmsPresence_Object = MibScalar
amsPresence = _AmsPresence_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 17),
    _AmsPresence_Type()
)
amsPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsPresence.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150)
)
_TmSrc_Type = InetAddressIPv4
_TmSrc_Object = MibScalar
tmSrc = _TmSrc_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 1),
    _TmSrc_Type()
)
tmSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmSrc.setStatus("current")


class _TmSrcTyp_Type(Integer32):
    """Custom type tmSrcTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("sntp", 2))
    )


_TmSrcTyp_Type.__name__ = "Integer32"
_TmSrcTyp_Object = MibScalar
tmSrcTyp = _TmSrcTyp_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 2),
    _TmSrcTyp_Type()
)
tmSrcTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmSrcTyp.setStatus("current")


class _TmSyn_Type(Integer32):
    """Custom type tmSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalAreaClock", 1),
          ("localAreaClock", 2),
          ("globalAreaClock", 3))
    )


_TmSyn_Type.__name__ = "Integer32"
_TmSyn_Object = MibScalar
tmSyn = _TmSyn_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 3),
    _TmSyn_Type()
)
tmSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmSyn.setStatus("current")
_TmAcc_Type = Integer32
_TmAcc_Object = MibScalar
tmAcc = _TmAcc_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 4),
    _TmAcc_Type()
)
tmAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmAcc.setStatus("current")
_TmChSt1_Type = TruthValue
_TmChSt1_Object = MibScalar
tmChSt1 = _TmChSt1_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 5),
    _TmChSt1_Type()
)
tmChSt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmChSt1.setStatus("current")
_TmChSt2_Type = TruthValue
_TmChSt2_Object = MibScalar
tmChSt2 = _TmChSt2_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 6),
    _TmChSt2_Type()
)
tmChSt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmChSt2.setStatus("current")
_TmChSt3_Type = TruthValue
_TmChSt3_Object = MibScalar
tmChSt3 = _TmChSt3_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 8),
    _TmChSt3_Type()
)
tmChSt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmChSt3.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 4)
)


class _VConfEqpt_Type(UTF8String):
    """Custom type vConfEqpt based on UTF8String"""
    defaultValue = OctetString("Valeur par defaut")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VConfEqpt_Type.__name__ = "UTF8String"
_VConfEqpt_Object = MibScalar
vConfEqpt = _VConfEqpt_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 4, 1),
    _VConfEqpt_Type()
)
vConfEqpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vConfEqpt.setStatus("current")


class _VRedemarrage_Type(UTF8String):
    """Custom type vRedemarrage based on UTF8String"""
    defaultValue = OctetString("Valeur par defaut")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRedemarrage_Type.__name__ = "UTF8String"
_VRedemarrage_Object = MibScalar
vRedemarrage = _VRedemarrage_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 4, 2),
    _VRedemarrage_Type()
)
vRedemarrage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRedemarrage.setStatus("current")
_OnlineModifie_Type = TruthValue
_OnlineModifie_Object = MibScalar
onlineModifie = _OnlineModifie_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 4, 3),
    _OnlineModifie_Type()
)
onlineModifie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onlineModifie.setStatus("current")
_Application_ObjectIdentity = ObjectIdentity
application = _Application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5)
)
_Procede_ObjectIdentity = ObjectIdentity
procede = _Procede_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100)
)


class _ModeEquip_Type(Integer32):
    """Custom type modeEquip based on Integer32"""
    defaultValue = 0

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
        *(("modeLocal", 0),
          ("modeDistant", 1),
          ("modeTest", 2),
          ("modeConsigne", 3))
    )


_ModeEquip_Type.__name__ = "Integer32"
_ModeEquip_Object = MibScalar
modeEquip = _ModeEquip_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 3),
    _ModeEquip_Type()
)
modeEquip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeEquip.setStatus("current")
_CounterTable_Object = MibTable
counterTable = _CounterTable_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 4)
)
if mibBuilder.loadTexts:
    counterTable.setStatus("current")
_CounterEntry_Object = MibTableRow
counterEntry = _CounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 4, 1)
)
counterEntry.setIndexNames(
    (0, "SCLESFE-MIB-ARKENSCC", "counterIndex"),
)
if mibBuilder.loadTexts:
    counterEntry.setStatus("current")


class _CounterIndex_Type(Integer32):
    """Custom type counterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CounterIndex_Type.__name__ = "Integer32"
_CounterIndex_Object = MibTableColumn
counterIndex = _CounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 4, 1, 1),
    _CounterIndex_Type()
)
counterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    counterIndex.setStatus("current")


class _CounterName_Type(UTF8String):
    """Custom type counterName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CounterName_Type.__name__ = "UTF8String"
_CounterName_Object = MibTableColumn
counterName = _CounterName_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 4, 1, 2),
    _CounterName_Type()
)
counterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    counterName.setStatus("current")


class _CounterDesc_Type(UTF8String):
    """Custom type counterDesc based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CounterDesc_Type.__name__ = "UTF8String"
_CounterDesc_Object = MibTableColumn
counterDesc = _CounterDesc_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 4, 1, 3),
    _CounterDesc_Type()
)
counterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    counterDesc.setStatus("current")


class _CounterValue_Type(Unsigned32):
    """Custom type counterValue based on Unsigned32"""
    defaultValue = 0


_CounterValue_Type.__name__ = "Unsigned32"
_CounterValue_Object = MibTableColumn
counterValue = _CounterValue_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 4, 1, 4),
    _CounterValue_Type()
)
counterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterValue.setStatus("current")
_CounterLastChange_Type = DateAndTime
_CounterLastChange_Object = MibTableColumn
counterLastChange = _CounterLastChange_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 4, 1, 5),
    _CounterLastChange_Type()
)
counterLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    counterLastChange.setStatus("current")


class _FichierSAA_Type(UTF8String):
    """Custom type fichierSAA based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FichierSAA_Type.__name__ = "UTF8String"
_FichierSAA_Object = MibScalar
fichierSAA = _FichierSAA_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 105),
    _FichierSAA_Type()
)
fichierSAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fichierSAA.setStatus("current")
_Mvs_ObjectIdentity = ObjectIdentity
mvs = _Mvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 200)
)


class _DelaiRedem_Type(Integer32):
    """Custom type delaiRedem based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DelaiRedem_Type.__name__ = "Integer32"
_DelaiRedem_Object = MibScalar
delaiRedem = _DelaiRedem_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 200, 1),
    _DelaiRedem_Type()
)
delaiRedem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delaiRedem.setStatus("current")
if mibBuilder.loadTexts:
    delaiRedem.setUnits("s")


class _AutRedem_Type(TruthValue):
    """Custom type autRedem based on TruthValue"""
    defaultValue = 2


_AutRedem_Type.__name__ = "TruthValue"
_AutRedem_Object = MibScalar
autRedem = _AutRedem_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 200, 2),
    _AutRedem_Type()
)
autRedem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autRedem.setStatus("current")


class _TxtRedem_Type(UTF8String):
    """Custom type txtRedem based on UTF8String"""
    defaultValue = OctetString("")

    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TxtRedem_Type.__name__ = "UTF8String"
_TxtRedem_Object = MibScalar
txtRedem = _TxtRedem_Object(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 200, 3),
    _TxtRedem_Type()
)
txtRedem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txtRedem.setStatus("current")

# Managed Objects groups


# Notification objects

notifVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 2, 1)
)
notifVersion.setObjects(
    ("SCLESFE-MIB-ARKENSCC", "elementVersion")
)
if mibBuilder.loadTexts:
    notifVersion.setStatus(
        "current"
    )

notifState = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 1)
)
notifState.setObjects(
    ("SCLESFE-MIB-ARKENSCC", "state")
)
if mibBuilder.loadTexts:
    notifState.setStatus(
        "current"
    )

notifCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 1, 1)
)
notifCritical.setObjects(
    ("SCLESFE-MIB-ARKENSCC", "nbCritical")
)
if mibBuilder.loadTexts:
    notifCritical.setStatus(
        "current"
    )

notifWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 11, 2, 1)
)
notifWarning.setObjects(
    ("SCLESFE-MIB-ARKENSCC", "nbWarning")
)
if mibBuilder.loadTexts:
    notifWarning.setStatus(
        "current"
    )

notifSynchro = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 3, 150, 7)
)
notifSynchro.setObjects(
      *(("SCLESFE-MIB-ARKENSCC", "tmSyn"),
        ("SCLESFE-MIB-ARKENSCC", "tmAcc"))
)
if mibBuilder.loadTexts:
    notifSynchro.setStatus(
        "current"
    )

notifModifOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 4, 4)
)
notifModifOnline.setObjects(
      *(("SCLESFE-MIB-ARKENSCC", "vConfEqpt"),
        ("SCLESFE-MIB-ARKENSCC", "onlineModifie"))
)
if mibBuilder.loadTexts:
    notifModifOnline.setStatus(
        "current"
    )

notifModeEquip = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 2)
)
notifModeEquip.setObjects(
    ("SCLESFE-MIB-ARKENSCC", "modeEquip")
)
if mibBuilder.loadTexts:
    notifModeEquip.setStatus(
        "current"
    )

notifSAA = NotificationType(
    (1, 3, 6, 1, 4, 1, 51435, 3, 5, 100, 104)
)
notifSAA.setObjects(
    ("SCLESFE-MIB-ARKENSCC", "fichierSAA")
)
if mibBuilder.loadTexts:
    notifSAA.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCLESFE-MIB-ARKENSCC",
    **{"EventDate": EventDate,
       "UTF8String": UTF8String,
       "Unsigned64": Unsigned64,
       "arkenscc": arkenscc,
       "system": system,
       "type": type,
       "manufacturer": manufacturer,
       "name": name,
       "eqOGISPrefix": eqOGISPrefix,
       "macAddress": macAddress,
       "ipRF": ipRF,
       "ipRS": ipRS,
       "versionLog": versionLog,
       "versionProd": versionProd,
       "versionSousProd": versionSousProd,
       "devices": devices,
       "notifVersion": notifVersion,
       "elementTable": elementTable,
       "elementEntry": elementEntry,
       "elementIndex": elementIndex,
       "elementOGISSuffix": elementOGISSuffix,
       "elementVersion": elementVersion,
       "elementDetail": elementDetail,
       "elementStatus": elementStatus,
       "elementName": elementName,
       "elementUpdVersion": elementUpdVersion,
       "elementUpdDetail": elementUpdDetail,
       "elementUpdWaiting": elementUpdWaiting,
       "nicTable": nicTable,
       "nicEntry": nicEntry,
       "nicIndex": nicIndex,
       "nicName": nicName,
       "nicDetail": nicDetail,
       "nicMAC": nicMAC,
       "nicStatus": nicStatus,
       "nicIPoper": nicIPoper,
       "nicIPmaint": nicIPmaint,
       "status": status,
       "notifState": notifState,
       "state": state,
       "temperatures": temperatures,
       "cpuTemp": cpuTemp,
       "cardTemp": cardTemp,
       "usageLevels": usageLevels,
       "cpuLevel": cpuLevel,
       "memLevel": memLevel,
       "cpu2level": cpu2level,
       "storage": storage,
       "storageFree": storageFree,
       "storageFTPFree": storageFTPFree,
       "storageFreePct": storageFreePct,
       "storageFTPFreePct": storageFTPFreePct,
       "dates": dates,
       "currentDate": currentDate,
       "dateMajFW": dateMajFW,
       "dateMajConf": dateMajConf,
       "dateRedem": dateRedem,
       "errors": errors,
       "critical": critical,
       "notifCritical": notifCritical,
       "nbCritical": nbCritical,
       "criticalTable": criticalTable,
       "criticalEntry": criticalEntry,
       "criticalIndex": criticalIndex,
       "criticalDetail": criticalDetail,
       "criticalOGISSuffix": criticalOGISSuffix,
       "criticalTime": criticalTime,
       "warning": warning,
       "notifWarning": notifWarning,
       "nbWarning": nbWarning,
       "warningTable": warningTable,
       "warningEntry": warningEntry,
       "warningIndex": warningIndex,
       "warningDetail": warningDetail,
       "warningOGISSuffix": warningOGISSuffix,
       "warningTime": warningTime,
       "amsPresence": amsPresence,
       "ntp": ntp,
       "tmSrc": tmSrc,
       "tmSrcTyp": tmSrcTyp,
       "tmSyn": tmSyn,
       "tmAcc": tmAcc,
       "tmChSt1": tmChSt1,
       "tmChSt2": tmChSt2,
       "notifSynchro": notifSynchro,
       "tmChSt3": tmChSt3,
       "config": config,
       "vConfEqpt": vConfEqpt,
       "vRedemarrage": vRedemarrage,
       "onlineModifie": onlineModifie,
       "notifModifOnline": notifModifOnline,
       "application": application,
       "procede": procede,
       "notifModeEquip": notifModeEquip,
       "modeEquip": modeEquip,
       "counterTable": counterTable,
       "counterEntry": counterEntry,
       "counterIndex": counterIndex,
       "counterName": counterName,
       "counterDesc": counterDesc,
       "counterValue": counterValue,
       "counterLastChange": counterLastChange,
       "notifSAA": notifSAA,
       "fichierSAA": fichierSAA,
       "mvs": mvs,
       "delaiRedem": delaiRedem,
       "autRedem": autRedem,
       "txtRedem": txtRedem}
)
