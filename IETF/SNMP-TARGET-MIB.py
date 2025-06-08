# SNMP MIB module (SNMP-TARGET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMP-TARGET-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:28:46 2025
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

(SnmpAdminString,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

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
 iso,
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
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval")


# MODULE-IDENTITY

snmpTargetMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 12)
)
if mibBuilder.loadTexts:
    snmpTargetMIB.setRevisions(
        ("2002-10-14 00:00",
         "1998-08-04 00:00",
         "1997-07-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpTagValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SnmpTagList(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SnmpTargetObjects_ObjectIdentity = ObjectIdentity
snmpTargetObjects = _SnmpTargetObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 12, 1)
)
_SnmpTargetSpinLock_Type = TestAndIncr
_SnmpTargetSpinLock_Object = MibScalar
snmpTargetSpinLock = _SnmpTargetSpinLock_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 1),
    _SnmpTargetSpinLock_Type()
)
snmpTargetSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTargetSpinLock.setStatus("current")
_SnmpTargetAddrTable_Object = MibTable
snmpTargetAddrTable = _SnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2)
)
if mibBuilder.loadTexts:
    snmpTargetAddrTable.setStatus("current")
_SnmpTargetAddrEntry_Object = MibTableRow
snmpTargetAddrEntry = _SnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1)
)
snmpTargetAddrEntry.setIndexNames(
    (1, "SNMP-TARGET-MIB", "snmpTargetAddrName"),
)
if mibBuilder.loadTexts:
    snmpTargetAddrEntry.setStatus("current")


class _SnmpTargetAddrName_Type(SnmpAdminString):
    """Custom type snmpTargetAddrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpTargetAddrName_Type.__name__ = "SnmpAdminString"
_SnmpTargetAddrName_Object = MibTableColumn
snmpTargetAddrName = _SnmpTargetAddrName_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 1),
    _SnmpTargetAddrName_Type()
)
snmpTargetAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTargetAddrName.setStatus("current")
_SnmpTargetAddrTDomain_Type = TDomain
_SnmpTargetAddrTDomain_Object = MibTableColumn
snmpTargetAddrTDomain = _SnmpTargetAddrTDomain_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 2),
    _SnmpTargetAddrTDomain_Type()
)
snmpTargetAddrTDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrTDomain.setStatus("current")
_SnmpTargetAddrTAddress_Type = TAddress
_SnmpTargetAddrTAddress_Object = MibTableColumn
snmpTargetAddrTAddress = _SnmpTargetAddrTAddress_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 3),
    _SnmpTargetAddrTAddress_Type()
)
snmpTargetAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrTAddress.setStatus("current")


class _SnmpTargetAddrTimeout_Type(TimeInterval):
    """Custom type snmpTargetAddrTimeout based on TimeInterval"""
    defaultValue = 1500


_SnmpTargetAddrTimeout_Type.__name__ = "TimeInterval"
_SnmpTargetAddrTimeout_Object = MibTableColumn
snmpTargetAddrTimeout = _SnmpTargetAddrTimeout_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 4),
    _SnmpTargetAddrTimeout_Type()
)
snmpTargetAddrTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrTimeout.setStatus("current")


class _SnmpTargetAddrRetryCount_Type(Integer32):
    """Custom type snmpTargetAddrRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpTargetAddrRetryCount_Type.__name__ = "Integer32"
_SnmpTargetAddrRetryCount_Object = MibTableColumn
snmpTargetAddrRetryCount = _SnmpTargetAddrRetryCount_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 5),
    _SnmpTargetAddrRetryCount_Type()
)
snmpTargetAddrRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrRetryCount.setStatus("current")


class _SnmpTargetAddrTagList_Type(SnmpTagList):
    """Custom type snmpTargetAddrTagList based on SnmpTagList"""
    defaultValue = OctetString("")


_SnmpTargetAddrTagList_Type.__name__ = "SnmpTagList"
_SnmpTargetAddrTagList_Object = MibTableColumn
snmpTargetAddrTagList = _SnmpTargetAddrTagList_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 6),
    _SnmpTargetAddrTagList_Type()
)
snmpTargetAddrTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrTagList.setStatus("current")


class _SnmpTargetAddrParams_Type(SnmpAdminString):
    """Custom type snmpTargetAddrParams based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpTargetAddrParams_Type.__name__ = "SnmpAdminString"
_SnmpTargetAddrParams_Object = MibTableColumn
snmpTargetAddrParams = _SnmpTargetAddrParams_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 7),
    _SnmpTargetAddrParams_Type()
)
snmpTargetAddrParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrParams.setStatus("current")


class _SnmpTargetAddrStorageType_Type(StorageType):
    """Custom type snmpTargetAddrStorageType based on StorageType"""
    defaultValue = 3


_SnmpTargetAddrStorageType_Type.__name__ = "StorageType"
_SnmpTargetAddrStorageType_Object = MibTableColumn
snmpTargetAddrStorageType = _SnmpTargetAddrStorageType_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 8),
    _SnmpTargetAddrStorageType_Type()
)
snmpTargetAddrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrStorageType.setStatus("current")
_SnmpTargetAddrRowStatus_Type = RowStatus
_SnmpTargetAddrRowStatus_Object = MibTableColumn
snmpTargetAddrRowStatus = _SnmpTargetAddrRowStatus_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 2, 1, 9),
    _SnmpTargetAddrRowStatus_Type()
)
snmpTargetAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrRowStatus.setStatus("current")
_SnmpTargetParamsTable_Object = MibTable
snmpTargetParamsTable = _SnmpTargetParamsTable_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3)
)
if mibBuilder.loadTexts:
    snmpTargetParamsTable.setStatus("current")
_SnmpTargetParamsEntry_Object = MibTableRow
snmpTargetParamsEntry = _SnmpTargetParamsEntry_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1)
)
snmpTargetParamsEntry.setIndexNames(
    (1, "SNMP-TARGET-MIB", "snmpTargetParamsName"),
)
if mibBuilder.loadTexts:
    snmpTargetParamsEntry.setStatus("current")


class _SnmpTargetParamsName_Type(SnmpAdminString):
    """Custom type snmpTargetParamsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpTargetParamsName_Type.__name__ = "SnmpAdminString"
_SnmpTargetParamsName_Object = MibTableColumn
snmpTargetParamsName = _SnmpTargetParamsName_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 1),
    _SnmpTargetParamsName_Type()
)
snmpTargetParamsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTargetParamsName.setStatus("current")
_SnmpTargetParamsMPModel_Type = SnmpMessageProcessingModel
_SnmpTargetParamsMPModel_Object = MibTableColumn
snmpTargetParamsMPModel = _SnmpTargetParamsMPModel_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 2),
    _SnmpTargetParamsMPModel_Type()
)
snmpTargetParamsMPModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetParamsMPModel.setStatus("current")


class _SnmpTargetParamsSecurityModel_Type(SnmpSecurityModel):
    """Custom type snmpTargetParamsSecurityModel based on SnmpSecurityModel"""
    subtypeSpec = SnmpSecurityModel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnmpTargetParamsSecurityModel_Type.__name__ = "SnmpSecurityModel"
_SnmpTargetParamsSecurityModel_Object = MibTableColumn
snmpTargetParamsSecurityModel = _SnmpTargetParamsSecurityModel_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 3),
    _SnmpTargetParamsSecurityModel_Type()
)
snmpTargetParamsSecurityModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetParamsSecurityModel.setStatus("current")
_SnmpTargetParamsSecurityName_Type = SnmpAdminString
_SnmpTargetParamsSecurityName_Object = MibTableColumn
snmpTargetParamsSecurityName = _SnmpTargetParamsSecurityName_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 4),
    _SnmpTargetParamsSecurityName_Type()
)
snmpTargetParamsSecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetParamsSecurityName.setStatus("current")
_SnmpTargetParamsSecurityLevel_Type = SnmpSecurityLevel
_SnmpTargetParamsSecurityLevel_Object = MibTableColumn
snmpTargetParamsSecurityLevel = _SnmpTargetParamsSecurityLevel_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 5),
    _SnmpTargetParamsSecurityLevel_Type()
)
snmpTargetParamsSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetParamsSecurityLevel.setStatus("current")


class _SnmpTargetParamsStorageType_Type(StorageType):
    """Custom type snmpTargetParamsStorageType based on StorageType"""
    defaultValue = 3


_SnmpTargetParamsStorageType_Type.__name__ = "StorageType"
_SnmpTargetParamsStorageType_Object = MibTableColumn
snmpTargetParamsStorageType = _SnmpTargetParamsStorageType_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 6),
    _SnmpTargetParamsStorageType_Type()
)
snmpTargetParamsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetParamsStorageType.setStatus("current")
_SnmpTargetParamsRowStatus_Type = RowStatus
_SnmpTargetParamsRowStatus_Object = MibTableColumn
snmpTargetParamsRowStatus = _SnmpTargetParamsRowStatus_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 3, 1, 7),
    _SnmpTargetParamsRowStatus_Type()
)
snmpTargetParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetParamsRowStatus.setStatus("current")
_SnmpUnavailableContexts_Type = Counter32
_SnmpUnavailableContexts_Object = MibScalar
snmpUnavailableContexts = _SnmpUnavailableContexts_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 4),
    _SnmpUnavailableContexts_Type()
)
snmpUnavailableContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnavailableContexts.setStatus("current")
_SnmpUnknownContexts_Type = Counter32
_SnmpUnknownContexts_Object = MibScalar
snmpUnknownContexts = _SnmpUnknownContexts_Object(
    (1, 3, 6, 1, 6, 3, 12, 1, 5),
    _SnmpUnknownContexts_Type()
)
snmpUnknownContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnknownContexts.setStatus("current")
_SnmpTargetConformance_ObjectIdentity = ObjectIdentity
snmpTargetConformance = _SnmpTargetConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 12, 3)
)
_SnmpTargetCompliances_ObjectIdentity = ObjectIdentity
snmpTargetCompliances = _SnmpTargetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 12, 3, 1)
)
_SnmpTargetGroups_ObjectIdentity = ObjectIdentity
snmpTargetGroups = _SnmpTargetGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 12, 3, 2)
)

# Managed Objects groups

snmpTargetBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 12, 3, 2, 1)
)
snmpTargetBasicGroup.setObjects(
      *(("SNMP-TARGET-MIB", "snmpTargetSpinLock"),
        ("SNMP-TARGET-MIB", "snmpTargetAddrTDomain"),
        ("SNMP-TARGET-MIB", "snmpTargetAddrTAddress"),
        ("SNMP-TARGET-MIB", "snmpTargetAddrTagList"),
        ("SNMP-TARGET-MIB", "snmpTargetAddrParams"),
        ("SNMP-TARGET-MIB", "snmpTargetAddrStorageType"),
        ("SNMP-TARGET-MIB", "snmpTargetAddrRowStatus"),
        ("SNMP-TARGET-MIB", "snmpTargetParamsMPModel"),
        ("SNMP-TARGET-MIB", "snmpTargetParamsSecurityModel"),
        ("SNMP-TARGET-MIB", "snmpTargetParamsSecurityName"),
        ("SNMP-TARGET-MIB", "snmpTargetParamsSecurityLevel"),
        ("SNMP-TARGET-MIB", "snmpTargetParamsStorageType"),
        ("SNMP-TARGET-MIB", "snmpTargetParamsRowStatus"))
)
if mibBuilder.loadTexts:
    snmpTargetBasicGroup.setStatus("current")

snmpTargetResponseGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 12, 3, 2, 2)
)
snmpTargetResponseGroup.setObjects(
      *(("SNMP-TARGET-MIB", "snmpTargetAddrTimeout"),
        ("SNMP-TARGET-MIB", "snmpTargetAddrRetryCount"))
)
if mibBuilder.loadTexts:
    snmpTargetResponseGroup.setStatus("current")

snmpTargetCommandResponderGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 12, 3, 2, 3)
)
snmpTargetCommandResponderGroup.setObjects(
      *(("SNMP-TARGET-MIB", "snmpUnavailableContexts"),
        ("SNMP-TARGET-MIB", "snmpUnknownContexts"))
)
if mibBuilder.loadTexts:
    snmpTargetCommandResponderGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpTargetCommandResponderCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 12, 3, 1, 1)
)
snmpTargetCommandResponderCompliance.setObjects(
    ("SNMP-TARGET-MIB", "snmpTargetCommandResponderGroup")
)
if mibBuilder.loadTexts:
    snmpTargetCommandResponderCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-TARGET-MIB",
    **{"SnmpTagValue": SnmpTagValue,
       "SnmpTagList": SnmpTagList,
       "snmpTargetMIB": snmpTargetMIB,
       "snmpTargetObjects": snmpTargetObjects,
       "snmpTargetSpinLock": snmpTargetSpinLock,
       "snmpTargetAddrTable": snmpTargetAddrTable,
       "snmpTargetAddrEntry": snmpTargetAddrEntry,
       "snmpTargetAddrName": snmpTargetAddrName,
       "snmpTargetAddrTDomain": snmpTargetAddrTDomain,
       "snmpTargetAddrTAddress": snmpTargetAddrTAddress,
       "snmpTargetAddrTimeout": snmpTargetAddrTimeout,
       "snmpTargetAddrRetryCount": snmpTargetAddrRetryCount,
       "snmpTargetAddrTagList": snmpTargetAddrTagList,
       "snmpTargetAddrParams": snmpTargetAddrParams,
       "snmpTargetAddrStorageType": snmpTargetAddrStorageType,
       "snmpTargetAddrRowStatus": snmpTargetAddrRowStatus,
       "snmpTargetParamsTable": snmpTargetParamsTable,
       "snmpTargetParamsEntry": snmpTargetParamsEntry,
       "snmpTargetParamsName": snmpTargetParamsName,
       "snmpTargetParamsMPModel": snmpTargetParamsMPModel,
       "snmpTargetParamsSecurityModel": snmpTargetParamsSecurityModel,
       "snmpTargetParamsSecurityName": snmpTargetParamsSecurityName,
       "snmpTargetParamsSecurityLevel": snmpTargetParamsSecurityLevel,
       "snmpTargetParamsStorageType": snmpTargetParamsStorageType,
       "snmpTargetParamsRowStatus": snmpTargetParamsRowStatus,
       "snmpUnavailableContexts": snmpUnavailableContexts,
       "snmpUnknownContexts": snmpUnknownContexts,
       "snmpTargetConformance": snmpTargetConformance,
       "snmpTargetCompliances": snmpTargetCompliances,
       "snmpTargetCommandResponderCompliance": snmpTargetCommandResponderCompliance,
       "snmpTargetGroups": snmpTargetGroups,
       "snmpTargetBasicGroup": snmpTargetBasicGroup,
       "snmpTargetResponseGroup": snmpTargetResponseGroup,
       "snmpTargetCommandResponderGroup": snmpTargetCommandResponderGroup}
)
