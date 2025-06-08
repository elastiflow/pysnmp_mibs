# SNMP MIB module (IEEE8021-TEIPS-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8021-TEIPS-V2-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:13:47 2025
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

(ieee8021BridgeBaseComponentId,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId")

(IEEE8021BridgePortNumber,
 IEEE8021PbbTeTSidId,
 IEEE8021TeipsIpgConfigActiveRequests,
 IEEE8021TeipsIpgConfigAdmin,
 IEEE8021TeipsIpgid,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbTeTSidId",
    "IEEE8021TeipsIpgConfigActiveRequests",
    "IEEE8021TeipsIpgConfigAdmin",
    "IEEE8021TeipsIpgid",
    "ieee802dot1mibs")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021TeipsV2Mib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 27)
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2Mib.setRevisions(
        ("2022-11-08 00:00",
         "2018-07-01 00:00",
         "2014-12-15 00:00",
         "2011-08-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021TeipsV2Notifications_ObjectIdentity = ObjectIdentity
ieee8021TeipsV2Notifications = _Ieee8021TeipsV2Notifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 27, 0)
)
_Ieee8021TeipsV2Objects_ObjectIdentity = ObjectIdentity
ieee8021TeipsV2Objects = _Ieee8021TeipsV2Objects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 27, 1)
)
_Ieee8021TeipsV2IpgTable_Object = MibTable
ieee8021TeipsV2IpgTable = _Ieee8021TeipsV2IpgTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgTable.setStatus("current")
_Ieee8021TeipsV2IpgEntry_Object = MibTableRow
ieee8021TeipsV2IpgEntry = _Ieee8021TeipsV2IpgEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1)
)
ieee8021TeipsV2IpgEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2Ipgid"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgEntry.setStatus("current")
_Ieee8021TeipsV2Ipgid_Type = IEEE8021TeipsIpgid
_Ieee8021TeipsV2Ipgid_Object = MibTableColumn
ieee8021TeipsV2Ipgid = _Ieee8021TeipsV2Ipgid_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1, 1),
    _Ieee8021TeipsV2Ipgid_Type()
)
ieee8021TeipsV2Ipgid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TeipsV2Ipgid.setStatus("current")
_Ieee8021TeipsV2IpgWorkingMA_Type = Unsigned32
_Ieee8021TeipsV2IpgWorkingMA_Object = MibTableColumn
ieee8021TeipsV2IpgWorkingMA = _Ieee8021TeipsV2IpgWorkingMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1, 2),
    _Ieee8021TeipsV2IpgWorkingMA_Type()
)
ieee8021TeipsV2IpgWorkingMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgWorkingMA.setStatus("current")
_Ieee8021TeipsV2IpgProtectionMA_Type = Unsigned32
_Ieee8021TeipsV2IpgProtectionMA_Object = MibTableColumn
ieee8021TeipsV2IpgProtectionMA = _Ieee8021TeipsV2IpgProtectionMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1, 3),
    _Ieee8021TeipsV2IpgProtectionMA_Type()
)
ieee8021TeipsV2IpgProtectionMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgProtectionMA.setStatus("current")
_Ieee8021TeipsV2IpgWorkingPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021TeipsV2IpgWorkingPortNumber_Object = MibTableColumn
ieee8021TeipsV2IpgWorkingPortNumber = _Ieee8021TeipsV2IpgWorkingPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1, 4),
    _Ieee8021TeipsV2IpgWorkingPortNumber_Type()
)
ieee8021TeipsV2IpgWorkingPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgWorkingPortNumber.setStatus("current")
_Ieee8021TeipsV2IpgProtectionPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021TeipsV2IpgProtectionPortNumber_Object = MibTableColumn
ieee8021TeipsV2IpgProtectionPortNumber = _Ieee8021TeipsV2IpgProtectionPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1, 5),
    _Ieee8021TeipsV2IpgProtectionPortNumber_Type()
)
ieee8021TeipsV2IpgProtectionPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgProtectionPortNumber.setStatus("current")


class _Ieee8021TeipsV2IpgStorageType_Type(StorageType):
    """Custom type ieee8021TeipsV2IpgStorageType based on StorageType"""
    defaultValue = 3


_Ieee8021TeipsV2IpgStorageType_Type.__name__ = "StorageType"
_Ieee8021TeipsV2IpgStorageType_Object = MibTableColumn
ieee8021TeipsV2IpgStorageType = _Ieee8021TeipsV2IpgStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1, 6),
    _Ieee8021TeipsV2IpgStorageType_Type()
)
ieee8021TeipsV2IpgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgStorageType.setStatus("current")
_Ieee8021TeipsV2IpgRowStatus_Type = RowStatus
_Ieee8021TeipsV2IpgRowStatus_Object = MibTableColumn
ieee8021TeipsV2IpgRowStatus = _Ieee8021TeipsV2IpgRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 1, 1, 7),
    _Ieee8021TeipsV2IpgRowStatus_Type()
)
ieee8021TeipsV2IpgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgRowStatus.setStatus("current")
_Ieee8021TeipsV2TesiTable_Object = MibTable
ieee8021TeipsV2TesiTable = _Ieee8021TeipsV2TesiTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2TesiTable.setStatus("current")
_Ieee8021TeipsV2TesiEntry_Object = MibTableRow
ieee8021TeipsV2TesiEntry = _Ieee8021TeipsV2TesiEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 2, 1)
)
ieee8021TeipsV2TesiEntry.setIndexNames(
    (0, "IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2Ipgid"),
    (0, "IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2TesiIndex"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2TesiEntry.setStatus("current")


class _Ieee8021TeipsV2TesiIndex_Type(Unsigned32):
    """Custom type ieee8021TeipsV2TesiIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ieee8021TeipsV2TesiIndex_Type.__name__ = "Unsigned32"
_Ieee8021TeipsV2TesiIndex_Object = MibTableColumn
ieee8021TeipsV2TesiIndex = _Ieee8021TeipsV2TesiIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 2, 1, 1),
    _Ieee8021TeipsV2TesiIndex_Type()
)
ieee8021TeipsV2TesiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TeipsV2TesiIndex.setStatus("current")
_Ieee8021TeipsV2TesiId_Type = IEEE8021PbbTeTSidId
_Ieee8021TeipsV2TesiId_Object = MibTableColumn
ieee8021TeipsV2TesiId = _Ieee8021TeipsV2TesiId_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 2, 1, 2),
    _Ieee8021TeipsV2TesiId_Type()
)
ieee8021TeipsV2TesiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2TesiId.setStatus("current")


class _Ieee8021TeipsV2TesiStorageType_Type(StorageType):
    """Custom type ieee8021TeipsV2TesiStorageType based on StorageType"""
    defaultValue = 3


_Ieee8021TeipsV2TesiStorageType_Type.__name__ = "StorageType"
_Ieee8021TeipsV2TesiStorageType_Object = MibTableColumn
ieee8021TeipsV2TesiStorageType = _Ieee8021TeipsV2TesiStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 2, 1, 3),
    _Ieee8021TeipsV2TesiStorageType_Type()
)
ieee8021TeipsV2TesiStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2TesiStorageType.setStatus("current")
_Ieee8021TeipsV2TesiRowStatus_Type = RowStatus
_Ieee8021TeipsV2TesiRowStatus_Object = MibTableColumn
ieee8021TeipsV2TesiRowStatus = _Ieee8021TeipsV2TesiRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 2, 1, 4),
    _Ieee8021TeipsV2TesiRowStatus_Type()
)
ieee8021TeipsV2TesiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2TesiRowStatus.setStatus("current")
_Ieee8021TeipsV2CandidatePsTable_Object = MibTable
ieee8021TeipsV2CandidatePsTable = _Ieee8021TeipsV2CandidatePsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsTable.setStatus("current")
_Ieee8021TeipsV2CandidatePsEntry_Object = MibTableRow
ieee8021TeipsV2CandidatePsEntry = _Ieee8021TeipsV2CandidatePsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3, 1)
)
ieee8021TeipsV2CandidatePsEntry.setIndexNames(
    (0, "IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2Ipgid"),
    (0, "IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2CandidatePsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsEntry.setStatus("current")


class _Ieee8021TeipsV2CandidatePsIndex_Type(Unsigned32):
    """Custom type ieee8021TeipsV2CandidatePsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ieee8021TeipsV2CandidatePsIndex_Type.__name__ = "Unsigned32"
_Ieee8021TeipsV2CandidatePsIndex_Object = MibTableColumn
ieee8021TeipsV2CandidatePsIndex = _Ieee8021TeipsV2CandidatePsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3, 1, 1),
    _Ieee8021TeipsV2CandidatePsIndex_Type()
)
ieee8021TeipsV2CandidatePsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsIndex.setStatus("current")
_Ieee8021TeipsV2CandidatePsMA_Type = Unsigned32
_Ieee8021TeipsV2CandidatePsMA_Object = MibTableColumn
ieee8021TeipsV2CandidatePsMA = _Ieee8021TeipsV2CandidatePsMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3, 1, 2),
    _Ieee8021TeipsV2CandidatePsMA_Type()
)
ieee8021TeipsV2CandidatePsMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsMA.setStatus("current")
_Ieee8021TeipsV2CandidatePsPort_Type = IEEE8021BridgePortNumber
_Ieee8021TeipsV2CandidatePsPort_Object = MibTableColumn
ieee8021TeipsV2CandidatePsPort = _Ieee8021TeipsV2CandidatePsPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3, 1, 3),
    _Ieee8021TeipsV2CandidatePsPort_Type()
)
ieee8021TeipsV2CandidatePsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsPort.setStatus("current")
_Ieee8021TeipsV2CandidatePsOper_Type = TruthValue
_Ieee8021TeipsV2CandidatePsOper_Object = MibTableColumn
ieee8021TeipsV2CandidatePsOper = _Ieee8021TeipsV2CandidatePsOper_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3, 1, 4),
    _Ieee8021TeipsV2CandidatePsOper_Type()
)
ieee8021TeipsV2CandidatePsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsOper.setStatus("current")


class _Ieee8021TeipsV2CandidatePsStorageType_Type(StorageType):
    """Custom type ieee8021TeipsV2CandidatePsStorageType based on StorageType"""
    defaultValue = 3


_Ieee8021TeipsV2CandidatePsStorageType_Type.__name__ = "StorageType"
_Ieee8021TeipsV2CandidatePsStorageType_Object = MibTableColumn
ieee8021TeipsV2CandidatePsStorageType = _Ieee8021TeipsV2CandidatePsStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3, 1, 5),
    _Ieee8021TeipsV2CandidatePsStorageType_Type()
)
ieee8021TeipsV2CandidatePsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsStorageType.setStatus("current")
_Ieee8021TeipsV2CandidatePsRowStatus_Type = RowStatus
_Ieee8021TeipsV2CandidatePsRowStatus_Object = MibTableColumn
ieee8021TeipsV2CandidatePsRowStatus = _Ieee8021TeipsV2CandidatePsRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 3, 1, 6),
    _Ieee8021TeipsV2CandidatePsRowStatus_Type()
)
ieee8021TeipsV2CandidatePsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsRowStatus.setStatus("current")
_Ieee8021TeipsV2IpgConfigTable_Object = MibTable
ieee8021TeipsV2IpgConfigTable = _Ieee8021TeipsV2IpgConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigTable.setStatus("current")
_Ieee8021TeipsV2IpgConfigEntry_Object = MibTableRow
ieee8021TeipsV2IpgConfigEntry = _Ieee8021TeipsV2IpgConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1)
)
ieee8021TeipsV2IpgConfigEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2Ipgid"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigEntry.setStatus("current")


class _Ieee8021TeipsV2IpgConfigState_Type(Integer32):
    """Custom type ieee8021TeipsV2IpgConfigState based on Integer32"""
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
        *(("workingSegment", 1),
          ("protectionSegment", 2),
          ("waitToRestore", 3),
          ("protAdmin", 4))
    )


_Ieee8021TeipsV2IpgConfigState_Type.__name__ = "Integer32"
_Ieee8021TeipsV2IpgConfigState_Object = MibTableColumn
ieee8021TeipsV2IpgConfigState = _Ieee8021TeipsV2IpgConfigState_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 1),
    _Ieee8021TeipsV2IpgConfigState_Type()
)
ieee8021TeipsV2IpgConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigState.setStatus("current")
_Ieee8021TeipsV2IpgConfigCommandStatus_Type = IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsV2IpgConfigCommandStatus_Object = MibTableColumn
ieee8021TeipsV2IpgConfigCommandStatus = _Ieee8021TeipsV2IpgConfigCommandStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 2),
    _Ieee8021TeipsV2IpgConfigCommandStatus_Type()
)
ieee8021TeipsV2IpgConfigCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigCommandStatus.setStatus("current")
_Ieee8021TeipsV2IpgConfigCommandLast_Type = IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsV2IpgConfigCommandLast_Object = MibTableColumn
ieee8021TeipsV2IpgConfigCommandLast = _Ieee8021TeipsV2IpgConfigCommandLast_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 3),
    _Ieee8021TeipsV2IpgConfigCommandLast_Type()
)
ieee8021TeipsV2IpgConfigCommandLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigCommandLast.setStatus("current")


class _Ieee8021TeipsV2IpgConfigCommandAdmin_Type(IEEE8021TeipsIpgConfigAdmin):
    """Custom type ieee8021TeipsV2IpgConfigCommandAdmin based on IEEE8021TeipsIpgConfigAdmin"""
    defaultValue = 1


_Ieee8021TeipsV2IpgConfigCommandAdmin_Type.__name__ = "IEEE8021TeipsIpgConfigAdmin"
_Ieee8021TeipsV2IpgConfigCommandAdmin_Object = MibTableColumn
ieee8021TeipsV2IpgConfigCommandAdmin = _Ieee8021TeipsV2IpgConfigCommandAdmin_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 4),
    _Ieee8021TeipsV2IpgConfigCommandAdmin_Type()
)
ieee8021TeipsV2IpgConfigCommandAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigCommandAdmin.setStatus("current")
_Ieee8021TeipsV2IpgConfigActiveRequests_Type = IEEE8021TeipsIpgConfigActiveRequests
_Ieee8021TeipsV2IpgConfigActiveRequests_Object = MibTableColumn
ieee8021TeipsV2IpgConfigActiveRequests = _Ieee8021TeipsV2IpgConfigActiveRequests_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 5),
    _Ieee8021TeipsV2IpgConfigActiveRequests_Type()
)
ieee8021TeipsV2IpgConfigActiveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigActiveRequests.setStatus("current")


class _Ieee8021TeipsV2IpgConfigWTR_Type(Unsigned32):
    """Custom type ieee8021TeipsV2IpgConfigWTR based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 12),
    )


_Ieee8021TeipsV2IpgConfigWTR_Type.__name__ = "Unsigned32"
_Ieee8021TeipsV2IpgConfigWTR_Object = MibTableColumn
ieee8021TeipsV2IpgConfigWTR = _Ieee8021TeipsV2IpgConfigWTR_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 6),
    _Ieee8021TeipsV2IpgConfigWTR_Type()
)
ieee8021TeipsV2IpgConfigWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigWTR.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigWTR.setUnits("minutes")


class _Ieee8021TeipsV2IpgConfigHoldOff_Type(Unsigned32):
    """Custom type ieee8021TeipsV2IpgConfigHoldOff based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ieee8021TeipsV2IpgConfigHoldOff_Type.__name__ = "Unsigned32"
_Ieee8021TeipsV2IpgConfigHoldOff_Object = MibTableColumn
ieee8021TeipsV2IpgConfigHoldOff = _Ieee8021TeipsV2IpgConfigHoldOff_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 7),
    _Ieee8021TeipsV2IpgConfigHoldOff_Type()
)
ieee8021TeipsV2IpgConfigHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigHoldOff.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigHoldOff.setUnits("deciseconds")


class _Ieee8021TeipsV2IpgM1ConfigState_Type(Integer32):
    """Custom type ieee8021TeipsV2IpgM1ConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("psAssigned", 1),
          ("segmentOk", 2),
          ("segmentFailed", 3),
          ("assignNewPs", 4),
          ("revertToBetterPs", 5))
    )


_Ieee8021TeipsV2IpgM1ConfigState_Type.__name__ = "Integer32"
_Ieee8021TeipsV2IpgM1ConfigState_Object = MibTableColumn
ieee8021TeipsV2IpgM1ConfigState = _Ieee8021TeipsV2IpgM1ConfigState_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 8),
    _Ieee8021TeipsV2IpgM1ConfigState_Type()
)
ieee8021TeipsV2IpgM1ConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgM1ConfigState.setStatus("current")


class _Ieee8021TeipsV2IpgConfigMWTR_Type(Unsigned32):
    """Custom type ieee8021TeipsV2IpgConfigMWTR based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 12),
    )


_Ieee8021TeipsV2IpgConfigMWTR_Type.__name__ = "Unsigned32"
_Ieee8021TeipsV2IpgConfigMWTR_Object = MibTableColumn
ieee8021TeipsV2IpgConfigMWTR = _Ieee8021TeipsV2IpgConfigMWTR_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 9),
    _Ieee8021TeipsV2IpgConfigMWTR_Type()
)
ieee8021TeipsV2IpgConfigMWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigMWTR.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigMWTR.setUnits("minutes")


class _Ieee8021TeipsV2IpgConfigNotifyEnable_Type(TruthValue):
    """Custom type ieee8021TeipsV2IpgConfigNotifyEnable based on TruthValue"""
    defaultValue = 2


_Ieee8021TeipsV2IpgConfigNotifyEnable_Type.__name__ = "TruthValue"
_Ieee8021TeipsV2IpgConfigNotifyEnable_Object = MibTableColumn
ieee8021TeipsV2IpgConfigNotifyEnable = _Ieee8021TeipsV2IpgConfigNotifyEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 10),
    _Ieee8021TeipsV2IpgConfigNotifyEnable_Type()
)
ieee8021TeipsV2IpgConfigNotifyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigNotifyEnable.setStatus("current")


class _Ieee8021TeipsV2IpgConfigStorageType_Type(StorageType):
    """Custom type ieee8021TeipsV2IpgConfigStorageType based on StorageType"""
    defaultValue = 3


_Ieee8021TeipsV2IpgConfigStorageType_Type.__name__ = "StorageType"
_Ieee8021TeipsV2IpgConfigStorageType_Object = MibTableColumn
ieee8021TeipsV2IpgConfigStorageType = _Ieee8021TeipsV2IpgConfigStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 27, 1, 4, 1, 11),
    _Ieee8021TeipsV2IpgConfigStorageType_Type()
)
ieee8021TeipsV2IpgConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigStorageType.setStatus("current")
_Ieee8021TeipsV2Conformance_ObjectIdentity = ObjectIdentity
ieee8021TeipsV2Conformance = _Ieee8021TeipsV2Conformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 27, 2)
)
_Ieee8021TeipsV2Compliances_ObjectIdentity = ObjectIdentity
ieee8021TeipsV2Compliances = _Ieee8021TeipsV2Compliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 1)
)
_Ieee8021TeipsV2Groups_ObjectIdentity = ObjectIdentity
ieee8021TeipsV2Groups = _Ieee8021TeipsV2Groups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 2)
)

# Managed Objects groups

ieee8021TeipsV2IpgGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 2, 1)
)
ieee8021TeipsV2IpgGroup.setObjects(
      *(("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgWorkingMA"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgProtectionMA"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgWorkingPortNumber"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgProtectionPortNumber"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgStorageType"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgGroup.setStatus("current")

ieee8021TeipsV2CandidatePsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 2, 2)
)
ieee8021TeipsV2CandidatePsGroup.setObjects(
      *(("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2CandidatePsMA"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2CandidatePsPort"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2CandidatePsOper"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2CandidatePsStorageType"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2CandidatePsRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2CandidatePsGroup.setStatus("current")

ieee8021TeipsV2IpgTesiGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 2, 3)
)
ieee8021TeipsV2IpgTesiGroup.setObjects(
      *(("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2TesiId"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2TesiStorageType"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2TesiRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgTesiGroup.setStatus("current")

ieee8021TeipsV2IpgConfigManGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 2, 4)
)
ieee8021TeipsV2IpgConfigManGroup.setObjects(
      *(("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigState"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigCommandStatus"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigCommandLast"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigCommandAdmin"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigActiveRequests"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigNotifyEnable"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigStorageType"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigManGroup.setStatus("current")

ieee8021TeipsV2IpgConfigOptGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 2, 5)
)
ieee8021TeipsV2IpgConfigOptGroup.setObjects(
      *(("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigWTR"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigMWTR"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgM1ConfigState"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigHoldOff"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgConfigOptGroup.setStatus("current")


# Notification objects

ieee8021TeipsV2IpgAdminFailure = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 27, 0, 1)
)
ieee8021TeipsV2IpgAdminFailure.setObjects(
      *(("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigState"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigCommandStatus"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigCommandLast"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2IpgAdminFailure.setStatus(
        "current"
    )


# Notifications groups

ieee8021TeipsV2NotificationsGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 2, 6)
)
ieee8021TeipsV2NotificationsGroup.setObjects(
    ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgAdminFailure")
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ieee8021TeipsV2Compliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 27, 2, 1, 1)
)
ieee8021TeipsV2Compliance.setObjects(
      *(("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgGroup"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgTesiGroup"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigManGroup"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2NotificationsGroup"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2IpgConfigOptGroup"),
        ("IEEE8021-TEIPS-V2-MIB", "ieee8021TeipsV2CandidatePsGroup"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsV2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-TEIPS-V2-MIB",
    **{"ieee8021TeipsV2Mib": ieee8021TeipsV2Mib,
       "ieee8021TeipsV2Notifications": ieee8021TeipsV2Notifications,
       "ieee8021TeipsV2IpgAdminFailure": ieee8021TeipsV2IpgAdminFailure,
       "ieee8021TeipsV2Objects": ieee8021TeipsV2Objects,
       "ieee8021TeipsV2IpgTable": ieee8021TeipsV2IpgTable,
       "ieee8021TeipsV2IpgEntry": ieee8021TeipsV2IpgEntry,
       "ieee8021TeipsV2Ipgid": ieee8021TeipsV2Ipgid,
       "ieee8021TeipsV2IpgWorkingMA": ieee8021TeipsV2IpgWorkingMA,
       "ieee8021TeipsV2IpgProtectionMA": ieee8021TeipsV2IpgProtectionMA,
       "ieee8021TeipsV2IpgWorkingPortNumber": ieee8021TeipsV2IpgWorkingPortNumber,
       "ieee8021TeipsV2IpgProtectionPortNumber": ieee8021TeipsV2IpgProtectionPortNumber,
       "ieee8021TeipsV2IpgStorageType": ieee8021TeipsV2IpgStorageType,
       "ieee8021TeipsV2IpgRowStatus": ieee8021TeipsV2IpgRowStatus,
       "ieee8021TeipsV2TesiTable": ieee8021TeipsV2TesiTable,
       "ieee8021TeipsV2TesiEntry": ieee8021TeipsV2TesiEntry,
       "ieee8021TeipsV2TesiIndex": ieee8021TeipsV2TesiIndex,
       "ieee8021TeipsV2TesiId": ieee8021TeipsV2TesiId,
       "ieee8021TeipsV2TesiStorageType": ieee8021TeipsV2TesiStorageType,
       "ieee8021TeipsV2TesiRowStatus": ieee8021TeipsV2TesiRowStatus,
       "ieee8021TeipsV2CandidatePsTable": ieee8021TeipsV2CandidatePsTable,
       "ieee8021TeipsV2CandidatePsEntry": ieee8021TeipsV2CandidatePsEntry,
       "ieee8021TeipsV2CandidatePsIndex": ieee8021TeipsV2CandidatePsIndex,
       "ieee8021TeipsV2CandidatePsMA": ieee8021TeipsV2CandidatePsMA,
       "ieee8021TeipsV2CandidatePsPort": ieee8021TeipsV2CandidatePsPort,
       "ieee8021TeipsV2CandidatePsOper": ieee8021TeipsV2CandidatePsOper,
       "ieee8021TeipsV2CandidatePsStorageType": ieee8021TeipsV2CandidatePsStorageType,
       "ieee8021TeipsV2CandidatePsRowStatus": ieee8021TeipsV2CandidatePsRowStatus,
       "ieee8021TeipsV2IpgConfigTable": ieee8021TeipsV2IpgConfigTable,
       "ieee8021TeipsV2IpgConfigEntry": ieee8021TeipsV2IpgConfigEntry,
       "ieee8021TeipsV2IpgConfigState": ieee8021TeipsV2IpgConfigState,
       "ieee8021TeipsV2IpgConfigCommandStatus": ieee8021TeipsV2IpgConfigCommandStatus,
       "ieee8021TeipsV2IpgConfigCommandLast": ieee8021TeipsV2IpgConfigCommandLast,
       "ieee8021TeipsV2IpgConfigCommandAdmin": ieee8021TeipsV2IpgConfigCommandAdmin,
       "ieee8021TeipsV2IpgConfigActiveRequests": ieee8021TeipsV2IpgConfigActiveRequests,
       "ieee8021TeipsV2IpgConfigWTR": ieee8021TeipsV2IpgConfigWTR,
       "ieee8021TeipsV2IpgConfigHoldOff": ieee8021TeipsV2IpgConfigHoldOff,
       "ieee8021TeipsV2IpgM1ConfigState": ieee8021TeipsV2IpgM1ConfigState,
       "ieee8021TeipsV2IpgConfigMWTR": ieee8021TeipsV2IpgConfigMWTR,
       "ieee8021TeipsV2IpgConfigNotifyEnable": ieee8021TeipsV2IpgConfigNotifyEnable,
       "ieee8021TeipsV2IpgConfigStorageType": ieee8021TeipsV2IpgConfigStorageType,
       "ieee8021TeipsV2Conformance": ieee8021TeipsV2Conformance,
       "ieee8021TeipsV2Compliances": ieee8021TeipsV2Compliances,
       "ieee8021TeipsV2Compliance": ieee8021TeipsV2Compliance,
       "ieee8021TeipsV2Groups": ieee8021TeipsV2Groups,
       "ieee8021TeipsV2IpgGroup": ieee8021TeipsV2IpgGroup,
       "ieee8021TeipsV2CandidatePsGroup": ieee8021TeipsV2CandidatePsGroup,
       "ieee8021TeipsV2IpgTesiGroup": ieee8021TeipsV2IpgTesiGroup,
       "ieee8021TeipsV2IpgConfigManGroup": ieee8021TeipsV2IpgConfigManGroup,
       "ieee8021TeipsV2IpgConfigOptGroup": ieee8021TeipsV2IpgConfigOptGroup,
       "ieee8021TeipsV2NotificationsGroup": ieee8021TeipsV2NotificationsGroup}
)
