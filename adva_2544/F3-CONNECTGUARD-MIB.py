# SNMP MIB module (F3-CONNECTGUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-CONNECTGUARD-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 AfpTagControl,
 CmPmBinAction,
 CmPmIntervalType,
 EthernetMediaType,
 EthernetPortSpeed,
 F3DisplayString,
 OperationalState,
 PerfCounter64,
 PriorityMapMode,
 SecondaryState,
 SfpConnectorValue,
 SfpMediaType,
 TrafficDirection,
 VlanEthertype,
 VlanId,
 VlanPriority,
 VlanTagType) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "AfpTagControl",
    "CmPmBinAction",
    "CmPmIntervalType",
    "EthernetMediaType",
    "EthernetPortSpeed",
    "F3DisplayString",
    "OperationalState",
    "PerfCounter64",
    "PriorityMapMode",
    "SecondaryState",
    "SfpConnectorValue",
    "SfpMediaType",
    "TrafficDirection",
    "VlanEthertype",
    "VlanId",
    "VlanPriority",
    "VlanTagType")

(f3UsbHostIndex,
 neIndex,
 networkElementEntry,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "f3UsbHostIndex",
    "neIndex",
    "networkElementEntry",
    "shelfIndex",
    "slotIndex")

(cmFlowEntry,) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmFlowEntry")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(f3AccFlowPointEntry,
 f3NetFlowPointEntry) = mibBuilder.importSymbols(
    "F3-FPM-MIB",
    "f3AccFlowPointEntry",
    "f3NetFlowPointEntry")

(SecySCI,) = mibBuilder.importSymbols(
    "IEEE8021-SECY-MIB",
    "SecySCI")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3ConnectGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36)
)
if mibBuilder.loadTexts:
    f3ConnectGuardMIB.setRevisions(
        ("2016-07-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FlowSecureState(TextualConvention, Integer32):
    status = "current"
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
        *(("secureNormal", 1),
          ("secureBlocked", 2),
          ("unsecureNormal", 3),
          ("unsecureBlocked", 4))
    )



class CipherSuiteType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gcmAes256", 1),
          ("gcmAes128", 2))
    )



class KeyExchangeFrameTagControl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoSelect", 1),
          ("manual", 2))
    )



class ScSaState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )



class ConnectGuardKeyExMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authPasswordBasedDiffieHellman", 1),
          ("caBasedDiffieHellman", 2),
          ("ieee8021x", 3))
    )



class DiffieHellmanKeyPairLength(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("length2048", 1),
          ("length4096", 2))
    )



class ConnectGuardFlowActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("restartKeyXchg", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3ConnectGuardConfigObjects_ObjectIdentity = ObjectIdentity
f3ConnectGuardConfigObjects = _F3ConnectGuardConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1)
)
_F3ConnectGuardFlowTable_Object = MibTable
f3ConnectGuardFlowTable = _F3ConnectGuardFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1)
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowTable.setStatus("current")
_F3ConnectGuardFlowEntry_Object = MibTableRow
f3ConnectGuardFlowEntry = _F3ConnectGuardFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1)
)
f3ConnectGuardFlowEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowEntry.setStatus("current")
_F3ConnectGuardFlowIndex_Type = Integer32
_F3ConnectGuardFlowIndex_Object = MibTableColumn
f3ConnectGuardFlowIndex = _F3ConnectGuardFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 1),
    _F3ConnectGuardFlowIndex_Type()
)
f3ConnectGuardFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowIndex.setStatus("current")
_F3ConnectGuardFlowCipherSuite_Type = CipherSuiteType
_F3ConnectGuardFlowCipherSuite_Object = MibTableColumn
f3ConnectGuardFlowCipherSuite = _F3ConnectGuardFlowCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 2),
    _F3ConnectGuardFlowCipherSuite_Type()
)
f3ConnectGuardFlowCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowCipherSuite.setStatus("current")
_F3ConnectGuardFlowAdminState_Type = AdminState
_F3ConnectGuardFlowAdminState_Object = MibTableColumn
f3ConnectGuardFlowAdminState = _F3ConnectGuardFlowAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 3),
    _F3ConnectGuardFlowAdminState_Type()
)
f3ConnectGuardFlowAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowAdminState.setStatus("current")
_F3ConnectGuardFlowSecondaryState_Type = SecondaryState
_F3ConnectGuardFlowSecondaryState_Object = MibTableColumn
f3ConnectGuardFlowSecondaryState = _F3ConnectGuardFlowSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 4),
    _F3ConnectGuardFlowSecondaryState_Type()
)
f3ConnectGuardFlowSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowSecondaryState.setStatus("current")
_F3ConnectGuardFlowOperationalState_Type = OperationalState
_F3ConnectGuardFlowOperationalState_Object = MibTableColumn
f3ConnectGuardFlowOperationalState = _F3ConnectGuardFlowOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 5),
    _F3ConnectGuardFlowOperationalState_Type()
)
f3ConnectGuardFlowOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowOperationalState.setStatus("current")
_F3ConnectGuardFlowEgressInterface_Type = VariablePointer
_F3ConnectGuardFlowEgressInterface_Object = MibTableColumn
f3ConnectGuardFlowEgressInterface = _F3ConnectGuardFlowEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 6),
    _F3ConnectGuardFlowEgressInterface_Type()
)
f3ConnectGuardFlowEgressInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowEgressInterface.setStatus("current")
_F3ConnectGuardFlowKeyExchangeProfile_Type = VariablePointer
_F3ConnectGuardFlowKeyExchangeProfile_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeProfile = _F3ConnectGuardFlowKeyExchangeProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 7),
    _F3ConnectGuardFlowKeyExchangeProfile_Type()
)
f3ConnectGuardFlowKeyExchangeProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeProfile.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameTagControl_Type = KeyExchangeFrameTagControl
_F3ConnectGuardFlowKeyExchangeFrameTagControl_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameTagControl = _F3ConnectGuardFlowKeyExchangeFrameTagControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 8),
    _F3ConnectGuardFlowKeyExchangeFrameTagControl_Type()
)
f3ConnectGuardFlowKeyExchangeFrameTagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameTagControl.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled_Type = TruthValue
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled = _F3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 9),
    _F3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled_Type()
)
f3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanId_Type = VlanId
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanId_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameOuterVlanId = _F3ConnectGuardFlowKeyExchangeFrameOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 10),
    _F3ConnectGuardFlowKeyExchangeFrameOuterVlanId_Type()
)
f3ConnectGuardFlowKeyExchangeFrameOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameOuterVlanId.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority_Type = VlanPriority
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority = _F3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 11),
    _F3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority_Type()
)
f3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled_Type = TruthValue
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled = _F3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 12),
    _F3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanId_Type = VlanId
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanId_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner1VlanId = _F3ConnectGuardFlowKeyExchangeFrameInner1VlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 13),
    _F3ConnectGuardFlowKeyExchangeFrameInner1VlanId_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner1VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner1VlanId.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority_Type = VlanPriority
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority = _F3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 14),
    _F3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled_Type = TruthValue
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled = _F3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 15),
    _F3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanId_Type = VlanId
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanId_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner2VlanId = _F3ConnectGuardFlowKeyExchangeFrameInner2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 16),
    _F3ConnectGuardFlowKeyExchangeFrameInner2VlanId_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner2VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner2VlanId.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority_Type = VlanPriority
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority = _F3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 17),
    _F3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority.setStatus("current")
_F3ConnectGuardFlowKeyExchangeInterval_Type = Integer32
_F3ConnectGuardFlowKeyExchangeInterval_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeInterval = _F3ConnectGuardFlowKeyExchangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 18),
    _F3ConnectGuardFlowKeyExchangeInterval_Type()
)
f3ConnectGuardFlowKeyExchangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeInterval.setStatus("current")
_F3ConnectGuardFlowTagsClear_Type = Integer32
_F3ConnectGuardFlowTagsClear_Object = MibTableColumn
f3ConnectGuardFlowTagsClear = _F3ConnectGuardFlowTagsClear_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 19),
    _F3ConnectGuardFlowTagsClear_Type()
)
f3ConnectGuardFlowTagsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowTagsClear.setStatus("current")
_F3ConnectGuardFlowStorageType_Type = StorageType
_F3ConnectGuardFlowStorageType_Object = MibTableColumn
f3ConnectGuardFlowStorageType = _F3ConnectGuardFlowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 20),
    _F3ConnectGuardFlowStorageType_Type()
)
f3ConnectGuardFlowStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStorageType.setStatus("current")
_F3ConnectGuardFlowRowStatus_Type = RowStatus
_F3ConnectGuardFlowRowStatus_Object = MibTableColumn
f3ConnectGuardFlowRowStatus = _F3ConnectGuardFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 21),
    _F3ConnectGuardFlowRowStatus_Type()
)
f3ConnectGuardFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowRowStatus.setStatus("current")
_F3ConnectGuardFlowKeyXchgFailsCounts_Type = Unsigned32
_F3ConnectGuardFlowKeyXchgFailsCounts_Object = MibTableColumn
f3ConnectGuardFlowKeyXchgFailsCounts = _F3ConnectGuardFlowKeyXchgFailsCounts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 22),
    _F3ConnectGuardFlowKeyXchgFailsCounts_Type()
)
f3ConnectGuardFlowKeyXchgFailsCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyXchgFailsCounts.setStatus("current")
_F3ConnectGuardFlowAction_Type = ConnectGuardFlowActionType
_F3ConnectGuardFlowAction_Object = MibTableColumn
f3ConnectGuardFlowAction = _F3ConnectGuardFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 23),
    _F3ConnectGuardFlowAction_Type()
)
f3ConnectGuardFlowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowAction.setStatus("current")
_F3ConnectGuardFlowReplayProtectionEnabled_Type = TruthValue
_F3ConnectGuardFlowReplayProtectionEnabled_Object = MibTableColumn
f3ConnectGuardFlowReplayProtectionEnabled = _F3ConnectGuardFlowReplayProtectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 24),
    _F3ConnectGuardFlowReplayProtectionEnabled_Type()
)
f3ConnectGuardFlowReplayProtectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowReplayProtectionEnabled.setStatus("current")
_F3ConnectGuardFlowReplayProtectionWindow_Type = Unsigned32
_F3ConnectGuardFlowReplayProtectionWindow_Object = MibTableColumn
f3ConnectGuardFlowReplayProtectionWindow = _F3ConnectGuardFlowReplayProtectionWindow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 25),
    _F3ConnectGuardFlowReplayProtectionWindow_Type()
)
f3ConnectGuardFlowReplayProtectionWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowReplayProtectionWindow.setStatus("current")
_F3ConnectGuardFlowRemoteMacAddrEnabled_Type = TruthValue
_F3ConnectGuardFlowRemoteMacAddrEnabled_Object = MibTableColumn
f3ConnectGuardFlowRemoteMacAddrEnabled = _F3ConnectGuardFlowRemoteMacAddrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 26),
    _F3ConnectGuardFlowRemoteMacAddrEnabled_Type()
)
f3ConnectGuardFlowRemoteMacAddrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowRemoteMacAddrEnabled.setStatus("current")
_F3ConnectGuardFlowRemoteMacAddr_Type = MacAddress
_F3ConnectGuardFlowRemoteMacAddr_Object = MibTableColumn
f3ConnectGuardFlowRemoteMacAddr = _F3ConnectGuardFlowRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 27),
    _F3ConnectGuardFlowRemoteMacAddr_Type()
)
f3ConnectGuardFlowRemoteMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowRemoteMacAddr.setStatus("current")
_F3ConnectGuardFlowAssociatedMep_Type = VariablePointer
_F3ConnectGuardFlowAssociatedMep_Object = MibTableColumn
f3ConnectGuardFlowAssociatedMep = _F3ConnectGuardFlowAssociatedMep_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 28),
    _F3ConnectGuardFlowAssociatedMep_Type()
)
f3ConnectGuardFlowAssociatedMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowAssociatedMep.setStatus("current")


class _F3ConnectGuardFlowAlias_Type(DisplayString):
    """Custom type f3ConnectGuardFlowAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3ConnectGuardFlowAlias_Type.__name__ = "DisplayString"
_F3ConnectGuardFlowAlias_Object = MibTableColumn
f3ConnectGuardFlowAlias = _F3ConnectGuardFlowAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 29),
    _F3ConnectGuardFlowAlias_Type()
)
f3ConnectGuardFlowAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowAlias.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType_Type = Unsigned32
_F3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType = _F3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 30),
    _F3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType_Type()
)
f3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType_Type = Unsigned32
_F3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType = _F3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 31),
    _F3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType.setStatus("current")
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType_Type = Unsigned32
_F3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType_Object = MibTableColumn
f3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType = _F3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 32),
    _F3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType_Type()
)
f3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType.setStatus("current")
_F3ConnectGuardFlowKeyInjectFlowPoint_Type = VariablePointer
_F3ConnectGuardFlowKeyInjectFlowPoint_Object = MibTableColumn
f3ConnectGuardFlowKeyInjectFlowPoint = _F3ConnectGuardFlowKeyInjectFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 1, 1, 33),
    _F3ConnectGuardFlowKeyInjectFlowPoint_Type()
)
f3ConnectGuardFlowKeyInjectFlowPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowKeyInjectFlowPoint.setStatus("current")
_F3ConnectGuardKeyExchangeProfileTable_Object = MibTable
f3ConnectGuardKeyExchangeProfileTable = _F3ConnectGuardKeyExchangeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2)
)
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileTable.setStatus("current")
_F3ConnectGuardKeyExchangeProfileEntry_Object = MibTableRow
f3ConnectGuardKeyExchangeProfileEntry = _F3ConnectGuardKeyExchangeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1)
)
f3ConnectGuardKeyExchangeProfileEntry.setIndexNames(
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileEntry.setStatus("current")
_F3ConnectGuardKeyExchangeProfileIndex_Type = Integer32
_F3ConnectGuardKeyExchangeProfileIndex_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileIndex = _F3ConnectGuardKeyExchangeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 1),
    _F3ConnectGuardKeyExchangeProfileIndex_Type()
)
f3ConnectGuardKeyExchangeProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileIndex.setStatus("current")
_F3ConnectGuardKeyExchangeProfileName_Type = DisplayString
_F3ConnectGuardKeyExchangeProfileName_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileName = _F3ConnectGuardKeyExchangeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 2),
    _F3ConnectGuardKeyExchangeProfileName_Type()
)
f3ConnectGuardKeyExchangeProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileName.setStatus("current")
_F3ConnectGuardKeyExchangeProfileUserId_Type = DisplayString
_F3ConnectGuardKeyExchangeProfileUserId_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileUserId = _F3ConnectGuardKeyExchangeProfileUserId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 3),
    _F3ConnectGuardKeyExchangeProfileUserId_Type()
)
f3ConnectGuardKeyExchangeProfileUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileUserId.setStatus("current")
_F3ConnectGuardKeyExchangeProfileMode_Type = ConnectGuardKeyExMode
_F3ConnectGuardKeyExchangeProfileMode_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileMode = _F3ConnectGuardKeyExchangeProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 4),
    _F3ConnectGuardKeyExchangeProfileMode_Type()
)
f3ConnectGuardKeyExchangeProfileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileMode.setStatus("current")
_F3ConnectGuardKeyExchangeProfileAuthPassword_Type = DisplayString
_F3ConnectGuardKeyExchangeProfileAuthPassword_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileAuthPassword = _F3ConnectGuardKeyExchangeProfileAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 5),
    _F3ConnectGuardKeyExchangeProfileAuthPassword_Type()
)
f3ConnectGuardKeyExchangeProfileAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileAuthPassword.setStatus("current")
_F3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen_Type = DiffieHellmanKeyPairLength
_F3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen = _F3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 6),
    _F3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen_Type()
)
f3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen.setStatus("current")
_F3ConnectGuardKeyExchangeProfileStorageType_Type = StorageType
_F3ConnectGuardKeyExchangeProfileStorageType_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileStorageType = _F3ConnectGuardKeyExchangeProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 7),
    _F3ConnectGuardKeyExchangeProfileStorageType_Type()
)
f3ConnectGuardKeyExchangeProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileStorageType.setStatus("current")
_F3ConnectGuardKeyExchangeProfileRowStatus_Type = RowStatus
_F3ConnectGuardKeyExchangeProfileRowStatus_Object = MibTableColumn
f3ConnectGuardKeyExchangeProfileRowStatus = _F3ConnectGuardKeyExchangeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 2, 1, 8),
    _F3ConnectGuardKeyExchangeProfileRowStatus_Type()
)
f3ConnectGuardKeyExchangeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ConnectGuardKeyExchangeProfileRowStatus.setStatus("current")
_F3ConnectGuardTxSCTable_Object = MibTable
f3ConnectGuardTxSCTable = _F3ConnectGuardTxSCTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3)
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCTable.setStatus("current")
_F3ConnectGuardTxSCEntry_Object = MibTableRow
f3ConnectGuardTxSCEntry = _F3ConnectGuardTxSCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1)
)
f3ConnectGuardTxSCEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCEntry.setStatus("current")
_F3ConnectGuardTxSCIndex_Type = Integer32
_F3ConnectGuardTxSCIndex_Object = MibTableColumn
f3ConnectGuardTxSCIndex = _F3ConnectGuardTxSCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 1),
    _F3ConnectGuardTxSCIndex_Type()
)
f3ConnectGuardTxSCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCIndex.setStatus("current")
_F3ConnectGuardTxSCI_Type = SecySCI
_F3ConnectGuardTxSCI_Object = MibTableColumn
f3ConnectGuardTxSCI = _F3ConnectGuardTxSCI_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 2),
    _F3ConnectGuardTxSCI_Type()
)
f3ConnectGuardTxSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCI.setStatus("current")
_F3ConnectGuardTxScState_Type = ScSaState
_F3ConnectGuardTxScState_Object = MibTableColumn
f3ConnectGuardTxScState = _F3ConnectGuardTxScState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 3),
    _F3ConnectGuardTxScState_Type()
)
f3ConnectGuardTxScState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxScState.setStatus("current")
_F3ConnectGuardCurrentTxSa_Type = Integer32
_F3ConnectGuardCurrentTxSa_Object = MibTableColumn
f3ConnectGuardCurrentTxSa = _F3ConnectGuardCurrentTxSa_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 4),
    _F3ConnectGuardCurrentTxSa_Type()
)
f3ConnectGuardCurrentTxSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardCurrentTxSa.setStatus("current")
_F3ConnectGuardPreviousTxSa_Type = Integer32
_F3ConnectGuardPreviousTxSa_Object = MibTableColumn
f3ConnectGuardPreviousTxSa = _F3ConnectGuardPreviousTxSa_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 5),
    _F3ConnectGuardPreviousTxSa_Type()
)
f3ConnectGuardPreviousTxSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardPreviousTxSa.setStatus("current")
_F3ConnectGuardTxScCreateTime_Type = DateAndTime
_F3ConnectGuardTxScCreateTime_Object = MibTableColumn
f3ConnectGuardTxScCreateTime = _F3ConnectGuardTxScCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 6),
    _F3ConnectGuardTxScCreateTime_Type()
)
f3ConnectGuardTxScCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxScCreateTime.setStatus("current")
_F3ConnectGuardTxScStartTime_Type = DateAndTime
_F3ConnectGuardTxScStartTime_Object = MibTableColumn
f3ConnectGuardTxScStartTime = _F3ConnectGuardTxScStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 7),
    _F3ConnectGuardTxScStartTime_Type()
)
f3ConnectGuardTxScStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxScStartTime.setStatus("current")
_F3ConnectGuardTxScStopTime_Type = DateAndTime
_F3ConnectGuardTxScStopTime_Object = MibTableColumn
f3ConnectGuardTxScStopTime = _F3ConnectGuardTxScStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 3, 1, 8),
    _F3ConnectGuardTxScStopTime_Type()
)
f3ConnectGuardTxScStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxScStopTime.setStatus("current")
_F3ConnectGuardRxSCTable_Object = MibTable
f3ConnectGuardRxSCTable = _F3ConnectGuardRxSCTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4)
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCTable.setStatus("current")
_F3ConnectGuardRxSCEntry_Object = MibTableRow
f3ConnectGuardRxSCEntry = _F3ConnectGuardRxSCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1)
)
f3ConnectGuardRxSCEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCEntry.setStatus("current")
_F3ConnectGuardRxSCIndex_Type = Integer32
_F3ConnectGuardRxSCIndex_Object = MibTableColumn
f3ConnectGuardRxSCIndex = _F3ConnectGuardRxSCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1, 1),
    _F3ConnectGuardRxSCIndex_Type()
)
f3ConnectGuardRxSCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCIndex.setStatus("current")
_F3ConnectGuardRxSCI_Type = SecySCI
_F3ConnectGuardRxSCI_Object = MibTableColumn
f3ConnectGuardRxSCI = _F3ConnectGuardRxSCI_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1, 2),
    _F3ConnectGuardRxSCI_Type()
)
f3ConnectGuardRxSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCI.setStatus("current")
_F3ConnectGuardRxScState_Type = ScSaState
_F3ConnectGuardRxScState_Object = MibTableColumn
f3ConnectGuardRxScState = _F3ConnectGuardRxScState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1, 3),
    _F3ConnectGuardRxScState_Type()
)
f3ConnectGuardRxScState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxScState.setStatus("current")
_F3ConnectGuardCurrentRxSa_Type = Integer32
_F3ConnectGuardCurrentRxSa_Object = MibTableColumn
f3ConnectGuardCurrentRxSa = _F3ConnectGuardCurrentRxSa_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1, 4),
    _F3ConnectGuardCurrentRxSa_Type()
)
f3ConnectGuardCurrentRxSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardCurrentRxSa.setStatus("current")
_F3ConnectGuardRxScCreateTime_Type = DateAndTime
_F3ConnectGuardRxScCreateTime_Object = MibTableColumn
f3ConnectGuardRxScCreateTime = _F3ConnectGuardRxScCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1, 5),
    _F3ConnectGuardRxScCreateTime_Type()
)
f3ConnectGuardRxScCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxScCreateTime.setStatus("current")
_F3ConnectGuardRxScStartTime_Type = DateAndTime
_F3ConnectGuardRxScStartTime_Object = MibTableColumn
f3ConnectGuardRxScStartTime = _F3ConnectGuardRxScStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1, 6),
    _F3ConnectGuardRxScStartTime_Type()
)
f3ConnectGuardRxScStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxScStartTime.setStatus("current")
_F3ConnectGuardRxScStopTime_Type = DateAndTime
_F3ConnectGuardRxScStopTime_Object = MibTableColumn
f3ConnectGuardRxScStopTime = _F3ConnectGuardRxScStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 4, 1, 7),
    _F3ConnectGuardRxScStopTime_Type()
)
f3ConnectGuardRxScStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxScStopTime.setStatus("current")
_F3ConnectGuardTxSATable_Object = MibTable
f3ConnectGuardTxSATable = _F3ConnectGuardTxSATable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5)
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSATable.setStatus("current")
_F3ConnectGuardTxSAEntry_Object = MibTableRow
f3ConnectGuardTxSAEntry = _F3ConnectGuardTxSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1)
)
f3ConnectGuardTxSAEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAEntry.setStatus("current")
_F3ConnectGuardTxSAIndex_Type = Unsigned32
_F3ConnectGuardTxSAIndex_Object = MibTableColumn
f3ConnectGuardTxSAIndex = _F3ConnectGuardTxSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1, 1),
    _F3ConnectGuardTxSAIndex_Type()
)
f3ConnectGuardTxSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAIndex.setStatus("current")
_F3ConnectGuardTxSAState_Type = ScSaState
_F3ConnectGuardTxSAState_Object = MibTableColumn
f3ConnectGuardTxSAState = _F3ConnectGuardTxSAState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1, 2),
    _F3ConnectGuardTxSAState_Type()
)
f3ConnectGuardTxSAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAState.setStatus("current")
_F3ConnectGuardTxSANextPN_Type = Unsigned32
_F3ConnectGuardTxSANextPN_Object = MibTableColumn
f3ConnectGuardTxSANextPN = _F3ConnectGuardTxSANextPN_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1, 3),
    _F3ConnectGuardTxSANextPN_Type()
)
f3ConnectGuardTxSANextPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSANextPN.setStatus("current")
_F3ConnectGuardTxSASAKUnchanged_Type = TruthValue
_F3ConnectGuardTxSASAKUnchanged_Object = MibTableColumn
f3ConnectGuardTxSASAKUnchanged = _F3ConnectGuardTxSASAKUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1, 4),
    _F3ConnectGuardTxSASAKUnchanged_Type()
)
f3ConnectGuardTxSASAKUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSASAKUnchanged.setStatus("current")
_F3ConnectGuardTxSACreatedTime_Type = DateAndTime
_F3ConnectGuardTxSACreatedTime_Object = MibTableColumn
f3ConnectGuardTxSACreatedTime = _F3ConnectGuardTxSACreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1, 5),
    _F3ConnectGuardTxSACreatedTime_Type()
)
f3ConnectGuardTxSACreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSACreatedTime.setStatus("current")
_F3ConnectGuardTxSAStartedTime_Type = DateAndTime
_F3ConnectGuardTxSAStartedTime_Object = MibTableColumn
f3ConnectGuardTxSAStartedTime = _F3ConnectGuardTxSAStartedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1, 6),
    _F3ConnectGuardTxSAStartedTime_Type()
)
f3ConnectGuardTxSAStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAStartedTime.setStatus("current")
_F3ConnectGuardTxSAStoppedTime_Type = DateAndTime
_F3ConnectGuardTxSAStoppedTime_Object = MibTableColumn
f3ConnectGuardTxSAStoppedTime = _F3ConnectGuardTxSAStoppedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 5, 1, 7),
    _F3ConnectGuardTxSAStoppedTime_Type()
)
f3ConnectGuardTxSAStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAStoppedTime.setStatus("current")
_F3ConnectGuardRxSATable_Object = MibTable
f3ConnectGuardRxSATable = _F3ConnectGuardRxSATable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6)
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSATable.setStatus("current")
_F3ConnectGuardRxSAEntry_Object = MibTableRow
f3ConnectGuardRxSAEntry = _F3ConnectGuardRxSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1)
)
f3ConnectGuardRxSAEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAEntry.setStatus("current")
_F3ConnectGuardRxSAIndex_Type = Unsigned32
_F3ConnectGuardRxSAIndex_Object = MibTableColumn
f3ConnectGuardRxSAIndex = _F3ConnectGuardRxSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1, 1),
    _F3ConnectGuardRxSAIndex_Type()
)
f3ConnectGuardRxSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAIndex.setStatus("current")
_F3ConnectGuardRxSAState_Type = ScSaState
_F3ConnectGuardRxSAState_Object = MibTableColumn
f3ConnectGuardRxSAState = _F3ConnectGuardRxSAState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1, 2),
    _F3ConnectGuardRxSAState_Type()
)
f3ConnectGuardRxSAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAState.setStatus("current")
_F3ConnectGuardRxSANextPN_Type = Unsigned32
_F3ConnectGuardRxSANextPN_Object = MibTableColumn
f3ConnectGuardRxSANextPN = _F3ConnectGuardRxSANextPN_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1, 3),
    _F3ConnectGuardRxSANextPN_Type()
)
f3ConnectGuardRxSANextPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSANextPN.setStatus("current")
_F3ConnectGuardRxSASAKUnchanged_Type = TruthValue
_F3ConnectGuardRxSASAKUnchanged_Object = MibTableColumn
f3ConnectGuardRxSASAKUnchanged = _F3ConnectGuardRxSASAKUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1, 4),
    _F3ConnectGuardRxSASAKUnchanged_Type()
)
f3ConnectGuardRxSASAKUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSASAKUnchanged.setStatus("current")
_F3ConnectGuardRxSACreatedTime_Type = DateAndTime
_F3ConnectGuardRxSACreatedTime_Object = MibTableColumn
f3ConnectGuardRxSACreatedTime = _F3ConnectGuardRxSACreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1, 5),
    _F3ConnectGuardRxSACreatedTime_Type()
)
f3ConnectGuardRxSACreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSACreatedTime.setStatus("current")
_F3ConnectGuardRxSAStartedTime_Type = DateAndTime
_F3ConnectGuardRxSAStartedTime_Object = MibTableColumn
f3ConnectGuardRxSAStartedTime = _F3ConnectGuardRxSAStartedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1, 6),
    _F3ConnectGuardRxSAStartedTime_Type()
)
f3ConnectGuardRxSAStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStartedTime.setStatus("current")
_F3ConnectGuardRxSAStoppedTime_Type = DateAndTime
_F3ConnectGuardRxSAStoppedTime_Object = MibTableColumn
f3ConnectGuardRxSAStoppedTime = _F3ConnectGuardRxSAStoppedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 6, 1, 7),
    _F3ConnectGuardRxSAStoppedTime_Type()
)
f3ConnectGuardRxSAStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStoppedTime.setStatus("current")
_F3FlowExtConnectGuardTable_Object = MibTable
f3FlowExtConnectGuardTable = _F3FlowExtConnectGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 7)
)
if mibBuilder.loadTexts:
    f3FlowExtConnectGuardTable.setStatus("deprecated")
_F3FlowExtConnectGuardEntry_Object = MibTableRow
f3FlowExtConnectGuardEntry = _F3FlowExtConnectGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 7, 1)
)
if mibBuilder.loadTexts:
    f3FlowExtConnectGuardEntry.setStatus("deprecated")
_F3FlowRefConnectGuardFlowObject_Type = VariablePointer
_F3FlowRefConnectGuardFlowObject_Object = MibTableColumn
f3FlowRefConnectGuardFlowObject = _F3FlowRefConnectGuardFlowObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 7, 1, 1),
    _F3FlowRefConnectGuardFlowObject_Type()
)
f3FlowRefConnectGuardFlowObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowRefConnectGuardFlowObject.setStatus("current")
_F3FlowSecureBlockingEnabled_Type = TruthValue
_F3FlowSecureBlockingEnabled_Object = MibTableColumn
f3FlowSecureBlockingEnabled = _F3FlowSecureBlockingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 7, 1, 2),
    _F3FlowSecureBlockingEnabled_Type()
)
f3FlowSecureBlockingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FlowSecureBlockingEnabled.setStatus("current")
_F3FlowSecureState_Type = FlowSecureState
_F3FlowSecureState_Object = MibTableColumn
f3FlowSecureState = _F3FlowSecureState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 7, 1, 3),
    _F3FlowSecureState_Type()
)
f3FlowSecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FlowSecureState.setStatus("current")
_F3ConnectGuardConfigScalars_ObjectIdentity = ObjectIdentity
f3ConnectGuardConfigScalars = _F3ConnectGuardConfigScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 8)
)
_F3ConnectGuardRestoreFactoryApproved_Type = TruthValue
_F3ConnectGuardRestoreFactoryApproved_Object = MibScalar
f3ConnectGuardRestoreFactoryApproved = _F3ConnectGuardRestoreFactoryApproved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 8, 1),
    _F3ConnectGuardRestoreFactoryApproved_Type()
)
f3ConnectGuardRestoreFactoryApproved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardRestoreFactoryApproved.setStatus("current")
_F3ConnectGuardSoftwareVersionApproved_Type = DisplayString
_F3ConnectGuardSoftwareVersionApproved_Object = MibScalar
f3ConnectGuardSoftwareVersionApproved = _F3ConnectGuardSoftwareVersionApproved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 8, 2),
    _F3ConnectGuardSoftwareVersionApproved_Type()
)
f3ConnectGuardSoftwareVersionApproved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardSoftwareVersionApproved.setStatus("current")
_F3ConnectGuardSoftwareInstallApproved_Type = TruthValue
_F3ConnectGuardSoftwareInstallApproved_Object = MibScalar
f3ConnectGuardSoftwareInstallApproved = _F3ConnectGuardSoftwareInstallApproved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 8, 3),
    _F3ConnectGuardSoftwareInstallApproved_Type()
)
f3ConnectGuardSoftwareInstallApproved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardSoftwareInstallApproved.setStatus("current")
_F3ConnectGuardRestoreDatabaseApproved_Type = TruthValue
_F3ConnectGuardRestoreDatabaseApproved_Object = MibScalar
f3ConnectGuardRestoreDatabaseApproved = _F3ConnectGuardRestoreDatabaseApproved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 8, 4),
    _F3ConnectGuardRestoreDatabaseApproved_Type()
)
f3ConnectGuardRestoreDatabaseApproved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardRestoreDatabaseApproved.setStatus("current")
_F3ConnectGuardConfigFileLoadApproved_Type = TruthValue
_F3ConnectGuardConfigFileLoadApproved_Object = MibScalar
f3ConnectGuardConfigFileLoadApproved = _F3ConnectGuardConfigFileLoadApproved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 8, 5),
    _F3ConnectGuardConfigFileLoadApproved_Type()
)
f3ConnectGuardConfigFileLoadApproved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardConfigFileLoadApproved.setStatus("current")
_F3ConnectGuardCryptoPasswordControl_Type = TruthValue
_F3ConnectGuardCryptoPasswordControl_Object = MibScalar
f3ConnectGuardCryptoPasswordControl = _F3ConnectGuardCryptoPasswordControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 8, 6),
    _F3ConnectGuardCryptoPasswordControl_Type()
)
f3ConnectGuardCryptoPasswordControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardCryptoPasswordControl.setStatus("current")
_F3ConnectGuardPasswordScalars_ObjectIdentity = ObjectIdentity
f3ConnectGuardPasswordScalars = _F3ConnectGuardPasswordScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 9)
)
_F3ConnectGuardCryptoPassword_Type = DisplayString
_F3ConnectGuardCryptoPassword_Object = MibScalar
f3ConnectGuardCryptoPassword = _F3ConnectGuardCryptoPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 1, 9, 1),
    _F3ConnectGuardCryptoPassword_Type()
)
f3ConnectGuardCryptoPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardCryptoPassword.setStatus("current")
_F3ConnectGuardPerformanceObjects_ObjectIdentity = ObjectIdentity
f3ConnectGuardPerformanceObjects = _F3ConnectGuardPerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2)
)
_F3ConnectGuardFlowStatsTable_Object = MibTable
f3ConnectGuardFlowStatsTable = _F3ConnectGuardFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1)
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsTable.setStatus("current")
_F3ConnectGuardFlowStatsEntry_Object = MibTableRow
f3ConnectGuardFlowStatsEntry = _F3ConnectGuardFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1)
)
f3ConnectGuardFlowStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsEntry.setStatus("current")


class _F3ConnectGuardFlowStatsIndex_Type(Integer32):
    """Custom type f3ConnectGuardFlowStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3ConnectGuardFlowStatsIndex_Type.__name__ = "Integer32"
_F3ConnectGuardFlowStatsIndex_Object = MibTableColumn
f3ConnectGuardFlowStatsIndex = _F3ConnectGuardFlowStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 1),
    _F3ConnectGuardFlowStatsIndex_Type()
)
f3ConnectGuardFlowStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsIndex.setStatus("current")
_F3ConnectGuardFlowStatsIntervalType_Type = CmPmIntervalType
_F3ConnectGuardFlowStatsIntervalType_Object = MibTableColumn
f3ConnectGuardFlowStatsIntervalType = _F3ConnectGuardFlowStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 2),
    _F3ConnectGuardFlowStatsIntervalType_Type()
)
f3ConnectGuardFlowStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsIntervalType.setStatus("current")
_F3ConnectGuardFlowStatsValid_Type = TruthValue
_F3ConnectGuardFlowStatsValid_Object = MibTableColumn
f3ConnectGuardFlowStatsValid = _F3ConnectGuardFlowStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 3),
    _F3ConnectGuardFlowStatsValid_Type()
)
f3ConnectGuardFlowStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsValid.setStatus("current")
_F3ConnectGuardFlowStatsAction_Type = CmPmBinAction
_F3ConnectGuardFlowStatsAction_Object = MibTableColumn
f3ConnectGuardFlowStatsAction = _F3ConnectGuardFlowStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 4),
    _F3ConnectGuardFlowStatsAction_Type()
)
f3ConnectGuardFlowStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsAction.setStatus("current")
_F3ConnectGuardFlowStatsTxUntaggedPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsTxUntaggedPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsTxUntaggedPkts = _F3ConnectGuardFlowStatsTxUntaggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 5),
    _F3ConnectGuardFlowStatsTxUntaggedPkts_Type()
)
f3ConnectGuardFlowStatsTxUntaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsTxUntaggedPkts.setStatus("current")
_F3ConnectGuardFlowStatsTxTooLongPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsTxTooLongPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsTxTooLongPkts = _F3ConnectGuardFlowStatsTxTooLongPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 6),
    _F3ConnectGuardFlowStatsTxTooLongPkts_Type()
)
f3ConnectGuardFlowStatsTxTooLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsTxTooLongPkts.setStatus("current")
_F3ConnectGuardFlowStatsRxUntaggedPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsRxUntaggedPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsRxUntaggedPkts = _F3ConnectGuardFlowStatsRxUntaggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 7),
    _F3ConnectGuardFlowStatsRxUntaggedPkts_Type()
)
f3ConnectGuardFlowStatsRxUntaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsRxUntaggedPkts.setStatus("current")
_F3ConnectGuardFlowStatsRxNotagPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsRxNotagPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsRxNotagPkts = _F3ConnectGuardFlowStatsRxNotagPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 8),
    _F3ConnectGuardFlowStatsRxNotagPkts_Type()
)
f3ConnectGuardFlowStatsRxNotagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsRxNotagPkts.setStatus("current")
_F3ConnectGuardFlowStatsRxBadtagPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsRxBadtagPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsRxBadtagPkts = _F3ConnectGuardFlowStatsRxBadtagPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 9),
    _F3ConnectGuardFlowStatsRxBadtagPkts_Type()
)
f3ConnectGuardFlowStatsRxBadtagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsRxBadtagPkts.setStatus("current")
_F3ConnectGuardFlowStatsRxUnknownSCIPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsRxUnknownSCIPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsRxUnknownSCIPkts = _F3ConnectGuardFlowStatsRxUnknownSCIPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 10),
    _F3ConnectGuardFlowStatsRxUnknownSCIPkts_Type()
)
f3ConnectGuardFlowStatsRxUnknownSCIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsRxUnknownSCIPkts.setStatus("current")
_F3ConnectGuardFlowStatsRxNoSCIPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsRxNoSCIPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsRxNoSCIPkts = _F3ConnectGuardFlowStatsRxNoSCIPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 11),
    _F3ConnectGuardFlowStatsRxNoSCIPkts_Type()
)
f3ConnectGuardFlowStatsRxNoSCIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsRxNoSCIPkts.setStatus("current")
_F3ConnectGuardFlowStatsRxOverrunPkts_Type = PerfCounter64
_F3ConnectGuardFlowStatsRxOverrunPkts_Object = MibTableColumn
f3ConnectGuardFlowStatsRxOverrunPkts = _F3ConnectGuardFlowStatsRxOverrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 1, 1, 12),
    _F3ConnectGuardFlowStatsRxOverrunPkts_Type()
)
f3ConnectGuardFlowStatsRxOverrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowStatsRxOverrunPkts.setStatus("current")
_F3ConnectGuardFlowHistoryTable_Object = MibTable
f3ConnectGuardFlowHistoryTable = _F3ConnectGuardFlowHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2)
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryTable.setStatus("current")
_F3ConnectGuardFlowHistoryEntry_Object = MibTableRow
f3ConnectGuardFlowHistoryEntry = _F3ConnectGuardFlowHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1)
)
f3ConnectGuardFlowHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryEntry.setStatus("current")
_F3ConnectGuardFlowHistoryIndex_Type = Integer32
_F3ConnectGuardFlowHistoryIndex_Object = MibTableColumn
f3ConnectGuardFlowHistoryIndex = _F3ConnectGuardFlowHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 1),
    _F3ConnectGuardFlowHistoryIndex_Type()
)
f3ConnectGuardFlowHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryIndex.setStatus("current")
_F3ConnectGuardFlowHistoryTime_Type = DateAndTime
_F3ConnectGuardFlowHistoryTime_Object = MibTableColumn
f3ConnectGuardFlowHistoryTime = _F3ConnectGuardFlowHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 2),
    _F3ConnectGuardFlowHistoryTime_Type()
)
f3ConnectGuardFlowHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryTime.setStatus("current")
_F3ConnectGuardFlowHistoryValid_Type = TruthValue
_F3ConnectGuardFlowHistoryValid_Object = MibTableColumn
f3ConnectGuardFlowHistoryValid = _F3ConnectGuardFlowHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 3),
    _F3ConnectGuardFlowHistoryValid_Type()
)
f3ConnectGuardFlowHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryValid.setStatus("current")
_F3ConnectGuardFlowHistoryAction_Type = CmPmBinAction
_F3ConnectGuardFlowHistoryAction_Object = MibTableColumn
f3ConnectGuardFlowHistoryAction = _F3ConnectGuardFlowHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 4),
    _F3ConnectGuardFlowHistoryAction_Type()
)
f3ConnectGuardFlowHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryAction.setStatus("current")
_F3ConnectGuardFlowHistoryTxUntaggedPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryTxUntaggedPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryTxUntaggedPkts = _F3ConnectGuardFlowHistoryTxUntaggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 5),
    _F3ConnectGuardFlowHistoryTxUntaggedPkts_Type()
)
f3ConnectGuardFlowHistoryTxUntaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryTxUntaggedPkts.setStatus("current")
_F3ConnectGuardFlowHistoryTxTooLongPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryTxTooLongPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryTxTooLongPkts = _F3ConnectGuardFlowHistoryTxTooLongPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 6),
    _F3ConnectGuardFlowHistoryTxTooLongPkts_Type()
)
f3ConnectGuardFlowHistoryTxTooLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryTxTooLongPkts.setStatus("current")
_F3ConnectGuardFlowHistoryRxUntaggedPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryRxUntaggedPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryRxUntaggedPkts = _F3ConnectGuardFlowHistoryRxUntaggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 7),
    _F3ConnectGuardFlowHistoryRxUntaggedPkts_Type()
)
f3ConnectGuardFlowHistoryRxUntaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryRxUntaggedPkts.setStatus("current")
_F3ConnectGuardFlowHistoryRxNotagPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryRxNotagPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryRxNotagPkts = _F3ConnectGuardFlowHistoryRxNotagPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 8),
    _F3ConnectGuardFlowHistoryRxNotagPkts_Type()
)
f3ConnectGuardFlowHistoryRxNotagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryRxNotagPkts.setStatus("current")
_F3ConnectGuardFlowHistoryRxBadtagPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryRxBadtagPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryRxBadtagPkts = _F3ConnectGuardFlowHistoryRxBadtagPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 9),
    _F3ConnectGuardFlowHistoryRxBadtagPkts_Type()
)
f3ConnectGuardFlowHistoryRxBadtagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryRxBadtagPkts.setStatus("current")
_F3ConnectGuardFlowHistoryRxUnknownSCIPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryRxUnknownSCIPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryRxUnknownSCIPkts = _F3ConnectGuardFlowHistoryRxUnknownSCIPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 10),
    _F3ConnectGuardFlowHistoryRxUnknownSCIPkts_Type()
)
f3ConnectGuardFlowHistoryRxUnknownSCIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryRxUnknownSCIPkts.setStatus("current")
_F3ConnectGuardFlowHistoryRxNoSCIPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryRxNoSCIPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryRxNoSCIPkts = _F3ConnectGuardFlowHistoryRxNoSCIPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 11),
    _F3ConnectGuardFlowHistoryRxNoSCIPkts_Type()
)
f3ConnectGuardFlowHistoryRxNoSCIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryRxNoSCIPkts.setStatus("current")
_F3ConnectGuardFlowHistoryRxOverrunPkts_Type = PerfCounter64
_F3ConnectGuardFlowHistoryRxOverrunPkts_Object = MibTableColumn
f3ConnectGuardFlowHistoryRxOverrunPkts = _F3ConnectGuardFlowHistoryRxOverrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 2, 1, 12),
    _F3ConnectGuardFlowHistoryRxOverrunPkts_Type()
)
f3ConnectGuardFlowHistoryRxOverrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowHistoryRxOverrunPkts.setStatus("current")
_F3ConnectGuardFlowThresholdTable_Object = MibTable
f3ConnectGuardFlowThresholdTable = _F3ConnectGuardFlowThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3)
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdTable.setStatus("current")
_F3ConnectGuardFlowThresholdEntry_Object = MibTableRow
f3ConnectGuardFlowThresholdEntry = _F3ConnectGuardFlowThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3, 1)
)
f3ConnectGuardFlowThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdEntry.setStatus("current")


class _F3ConnectGuardFlowThresholdIndex_Type(Integer32):
    """Custom type f3ConnectGuardFlowThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3ConnectGuardFlowThresholdIndex_Type.__name__ = "Integer32"
_F3ConnectGuardFlowThresholdIndex_Object = MibTableColumn
f3ConnectGuardFlowThresholdIndex = _F3ConnectGuardFlowThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3, 1, 1),
    _F3ConnectGuardFlowThresholdIndex_Type()
)
f3ConnectGuardFlowThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdIndex.setStatus("current")
_F3ConnectGuardFlowThresholdInterval_Type = CmPmIntervalType
_F3ConnectGuardFlowThresholdInterval_Object = MibTableColumn
f3ConnectGuardFlowThresholdInterval = _F3ConnectGuardFlowThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3, 1, 2),
    _F3ConnectGuardFlowThresholdInterval_Type()
)
f3ConnectGuardFlowThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdInterval.setStatus("current")
_F3ConnectGuardFlowThresholdVariable_Type = VariablePointer
_F3ConnectGuardFlowThresholdVariable_Object = MibTableColumn
f3ConnectGuardFlowThresholdVariable = _F3ConnectGuardFlowThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3, 1, 3),
    _F3ConnectGuardFlowThresholdVariable_Type()
)
f3ConnectGuardFlowThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdVariable.setStatus("current")
_F3ConnectGuardFlowThresholdValueLo_Type = Unsigned32
_F3ConnectGuardFlowThresholdValueLo_Object = MibTableColumn
f3ConnectGuardFlowThresholdValueLo = _F3ConnectGuardFlowThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3, 1, 4),
    _F3ConnectGuardFlowThresholdValueLo_Type()
)
f3ConnectGuardFlowThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdValueLo.setStatus("current")
_F3ConnectGuardFlowThresholdValueHi_Type = Unsigned32
_F3ConnectGuardFlowThresholdValueHi_Object = MibTableColumn
f3ConnectGuardFlowThresholdValueHi = _F3ConnectGuardFlowThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3, 1, 5),
    _F3ConnectGuardFlowThresholdValueHi_Type()
)
f3ConnectGuardFlowThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdValueHi.setStatus("current")
_F3ConnectGuardFlowThresholdMonValue_Type = PerfCounter64
_F3ConnectGuardFlowThresholdMonValue_Object = MibTableColumn
f3ConnectGuardFlowThresholdMonValue = _F3ConnectGuardFlowThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 3, 1, 6),
    _F3ConnectGuardFlowThresholdMonValue_Type()
)
f3ConnectGuardFlowThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdMonValue.setStatus("current")
_F3ConnectGuardTxSCStatsTable_Object = MibTable
f3ConnectGuardTxSCStatsTable = _F3ConnectGuardTxSCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4)
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsTable.setStatus("current")
_F3ConnectGuardTxSCStatsEntry_Object = MibTableRow
f3ConnectGuardTxSCStatsEntry = _F3ConnectGuardTxSCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1)
)
f3ConnectGuardTxSCStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsEntry.setStatus("current")


class _F3ConnectGuardTxSCStatsIndex_Type(Integer32):
    """Custom type f3ConnectGuardTxSCStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3ConnectGuardTxSCStatsIndex_Type.__name__ = "Integer32"
_F3ConnectGuardTxSCStatsIndex_Object = MibTableColumn
f3ConnectGuardTxSCStatsIndex = _F3ConnectGuardTxSCStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 1),
    _F3ConnectGuardTxSCStatsIndex_Type()
)
f3ConnectGuardTxSCStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsIndex.setStatus("current")
_F3ConnectGuardTxSCStatsIntervalType_Type = CmPmIntervalType
_F3ConnectGuardTxSCStatsIntervalType_Object = MibTableColumn
f3ConnectGuardTxSCStatsIntervalType = _F3ConnectGuardTxSCStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 2),
    _F3ConnectGuardTxSCStatsIntervalType_Type()
)
f3ConnectGuardTxSCStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsIntervalType.setStatus("current")
_F3ConnectGuardTxSCStatsValid_Type = TruthValue
_F3ConnectGuardTxSCStatsValid_Object = MibTableColumn
f3ConnectGuardTxSCStatsValid = _F3ConnectGuardTxSCStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 3),
    _F3ConnectGuardTxSCStatsValid_Type()
)
f3ConnectGuardTxSCStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsValid.setStatus("current")
_F3ConnectGuardTxSCStatsAction_Type = CmPmBinAction
_F3ConnectGuardTxSCStatsAction_Object = MibTableColumn
f3ConnectGuardTxSCStatsAction = _F3ConnectGuardTxSCStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 4),
    _F3ConnectGuardTxSCStatsAction_Type()
)
f3ConnectGuardTxSCStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsAction.setStatus("current")
_F3ConnectGuardTxSCStatsTxProtectedPkts_Type = PerfCounter64
_F3ConnectGuardTxSCStatsTxProtectedPkts_Object = MibTableColumn
f3ConnectGuardTxSCStatsTxProtectedPkts = _F3ConnectGuardTxSCStatsTxProtectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 5),
    _F3ConnectGuardTxSCStatsTxProtectedPkts_Type()
)
f3ConnectGuardTxSCStatsTxProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsTxProtectedPkts.setStatus("current")
_F3ConnectGuardTxSCStatsTxEncryptedPkts_Type = PerfCounter64
_F3ConnectGuardTxSCStatsTxEncryptedPkts_Object = MibTableColumn
f3ConnectGuardTxSCStatsTxEncryptedPkts = _F3ConnectGuardTxSCStatsTxEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 6),
    _F3ConnectGuardTxSCStatsTxEncryptedPkts_Type()
)
f3ConnectGuardTxSCStatsTxEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsTxEncryptedPkts.setStatus("current")
_F3ConnectGuardTxSCStatsTxOctetsProtected_Type = PerfCounter64
_F3ConnectGuardTxSCStatsTxOctetsProtected_Object = MibTableColumn
f3ConnectGuardTxSCStatsTxOctetsProtected = _F3ConnectGuardTxSCStatsTxOctetsProtected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 7),
    _F3ConnectGuardTxSCStatsTxOctetsProtected_Type()
)
f3ConnectGuardTxSCStatsTxOctetsProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsTxOctetsProtected.setStatus("current")
_F3ConnectGuardTxSCStatsTxOctetsEncrypted_Type = PerfCounter64
_F3ConnectGuardTxSCStatsTxOctetsEncrypted_Object = MibTableColumn
f3ConnectGuardTxSCStatsTxOctetsEncrypted = _F3ConnectGuardTxSCStatsTxOctetsEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 4, 1, 8),
    _F3ConnectGuardTxSCStatsTxOctetsEncrypted_Type()
)
f3ConnectGuardTxSCStatsTxOctetsEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCStatsTxOctetsEncrypted.setStatus("current")
_F3ConnectGuardTxSCHistoryTable_Object = MibTable
f3ConnectGuardTxSCHistoryTable = _F3ConnectGuardTxSCHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5)
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryTable.setStatus("current")
_F3ConnectGuardTxSCHistoryEntry_Object = MibTableRow
f3ConnectGuardTxSCHistoryEntry = _F3ConnectGuardTxSCHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1)
)
f3ConnectGuardTxSCHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryEntry.setStatus("current")
_F3ConnectGuardTxSCHistoryIndex_Type = Integer32
_F3ConnectGuardTxSCHistoryIndex_Object = MibTableColumn
f3ConnectGuardTxSCHistoryIndex = _F3ConnectGuardTxSCHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 1),
    _F3ConnectGuardTxSCHistoryIndex_Type()
)
f3ConnectGuardTxSCHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryIndex.setStatus("current")
_F3ConnectGuardTxSCHistoryTime_Type = DateAndTime
_F3ConnectGuardTxSCHistoryTime_Object = MibTableColumn
f3ConnectGuardTxSCHistoryTime = _F3ConnectGuardTxSCHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 2),
    _F3ConnectGuardTxSCHistoryTime_Type()
)
f3ConnectGuardTxSCHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryTime.setStatus("current")
_F3ConnectGuardTxSCHistoryValid_Type = TruthValue
_F3ConnectGuardTxSCHistoryValid_Object = MibTableColumn
f3ConnectGuardTxSCHistoryValid = _F3ConnectGuardTxSCHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 3),
    _F3ConnectGuardTxSCHistoryValid_Type()
)
f3ConnectGuardTxSCHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryValid.setStatus("current")
_F3ConnectGuardTxSCHistoryAction_Type = CmPmBinAction
_F3ConnectGuardTxSCHistoryAction_Object = MibTableColumn
f3ConnectGuardTxSCHistoryAction = _F3ConnectGuardTxSCHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 4),
    _F3ConnectGuardTxSCHistoryAction_Type()
)
f3ConnectGuardTxSCHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryAction.setStatus("current")
_F3ConnectGuardTxSCHistoryTxProtectedPkts_Type = PerfCounter64
_F3ConnectGuardTxSCHistoryTxProtectedPkts_Object = MibTableColumn
f3ConnectGuardTxSCHistoryTxProtectedPkts = _F3ConnectGuardTxSCHistoryTxProtectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 5),
    _F3ConnectGuardTxSCHistoryTxProtectedPkts_Type()
)
f3ConnectGuardTxSCHistoryTxProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryTxProtectedPkts.setStatus("current")
_F3ConnectGuardTxSCHistoryTxEncryptedPkts_Type = PerfCounter64
_F3ConnectGuardTxSCHistoryTxEncryptedPkts_Object = MibTableColumn
f3ConnectGuardTxSCHistoryTxEncryptedPkts = _F3ConnectGuardTxSCHistoryTxEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 6),
    _F3ConnectGuardTxSCHistoryTxEncryptedPkts_Type()
)
f3ConnectGuardTxSCHistoryTxEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryTxEncryptedPkts.setStatus("current")
_F3ConnectGuardTxSCHistoryTxOctetsProtected_Type = PerfCounter64
_F3ConnectGuardTxSCHistoryTxOctetsProtected_Object = MibTableColumn
f3ConnectGuardTxSCHistoryTxOctetsProtected = _F3ConnectGuardTxSCHistoryTxOctetsProtected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 7),
    _F3ConnectGuardTxSCHistoryTxOctetsProtected_Type()
)
f3ConnectGuardTxSCHistoryTxOctetsProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryTxOctetsProtected.setStatus("current")
_F3ConnectGuardTxSCHistoryTxOctetsEncrypted_Type = PerfCounter64
_F3ConnectGuardTxSCHistoryTxOctetsEncrypted_Object = MibTableColumn
f3ConnectGuardTxSCHistoryTxOctetsEncrypted = _F3ConnectGuardTxSCHistoryTxOctetsEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 5, 1, 8),
    _F3ConnectGuardTxSCHistoryTxOctetsEncrypted_Type()
)
f3ConnectGuardTxSCHistoryTxOctetsEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCHistoryTxOctetsEncrypted.setStatus("current")
_F3ConnectGuardTxSCThresholdTable_Object = MibTable
f3ConnectGuardTxSCThresholdTable = _F3ConnectGuardTxSCThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6)
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdTable.setStatus("current")
_F3ConnectGuardTxSCThresholdEntry_Object = MibTableRow
f3ConnectGuardTxSCThresholdEntry = _F3ConnectGuardTxSCThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6, 1)
)
f3ConnectGuardTxSCThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdEntry.setStatus("current")


class _F3ConnectGuardTxSCThresholdIndex_Type(Integer32):
    """Custom type f3ConnectGuardTxSCThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3ConnectGuardTxSCThresholdIndex_Type.__name__ = "Integer32"
_F3ConnectGuardTxSCThresholdIndex_Object = MibTableColumn
f3ConnectGuardTxSCThresholdIndex = _F3ConnectGuardTxSCThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6, 1, 1),
    _F3ConnectGuardTxSCThresholdIndex_Type()
)
f3ConnectGuardTxSCThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdIndex.setStatus("current")
_F3ConnectGuardTxSCThresholdInterval_Type = CmPmIntervalType
_F3ConnectGuardTxSCThresholdInterval_Object = MibTableColumn
f3ConnectGuardTxSCThresholdInterval = _F3ConnectGuardTxSCThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6, 1, 2),
    _F3ConnectGuardTxSCThresholdInterval_Type()
)
f3ConnectGuardTxSCThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdInterval.setStatus("current")
_F3ConnectGuardTxSCThresholdVariable_Type = VariablePointer
_F3ConnectGuardTxSCThresholdVariable_Object = MibTableColumn
f3ConnectGuardTxSCThresholdVariable = _F3ConnectGuardTxSCThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6, 1, 3),
    _F3ConnectGuardTxSCThresholdVariable_Type()
)
f3ConnectGuardTxSCThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdVariable.setStatus("current")
_F3ConnectGuardTxSCThresholdValueLo_Type = Unsigned32
_F3ConnectGuardTxSCThresholdValueLo_Object = MibTableColumn
f3ConnectGuardTxSCThresholdValueLo = _F3ConnectGuardTxSCThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6, 1, 4),
    _F3ConnectGuardTxSCThresholdValueLo_Type()
)
f3ConnectGuardTxSCThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdValueLo.setStatus("current")
_F3ConnectGuardTxSCThresholdValueHi_Type = Unsigned32
_F3ConnectGuardTxSCThresholdValueHi_Object = MibTableColumn
f3ConnectGuardTxSCThresholdValueHi = _F3ConnectGuardTxSCThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6, 1, 5),
    _F3ConnectGuardTxSCThresholdValueHi_Type()
)
f3ConnectGuardTxSCThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdValueHi.setStatus("current")
_F3ConnectGuardTxSCThresholdMonValue_Type = PerfCounter64
_F3ConnectGuardTxSCThresholdMonValue_Object = MibTableColumn
f3ConnectGuardTxSCThresholdMonValue = _F3ConnectGuardTxSCThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 6, 1, 6),
    _F3ConnectGuardTxSCThresholdMonValue_Type()
)
f3ConnectGuardTxSCThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdMonValue.setStatus("current")
_F3ConnectGuardRxSCStatsTable_Object = MibTable
f3ConnectGuardRxSCStatsTable = _F3ConnectGuardRxSCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7)
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsTable.setStatus("current")
_F3ConnectGuardRxSCStatsEntry_Object = MibTableRow
f3ConnectGuardRxSCStatsEntry = _F3ConnectGuardRxSCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1)
)
f3ConnectGuardRxSCStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsEntry.setStatus("current")


class _F3ConnectGuardRxSCStatsIndex_Type(Integer32):
    """Custom type f3ConnectGuardRxSCStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3ConnectGuardRxSCStatsIndex_Type.__name__ = "Integer32"
_F3ConnectGuardRxSCStatsIndex_Object = MibTableColumn
f3ConnectGuardRxSCStatsIndex = _F3ConnectGuardRxSCStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 1),
    _F3ConnectGuardRxSCStatsIndex_Type()
)
f3ConnectGuardRxSCStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsIndex.setStatus("current")
_F3ConnectGuardRxSCStatsIntervalType_Type = CmPmIntervalType
_F3ConnectGuardRxSCStatsIntervalType_Object = MibTableColumn
f3ConnectGuardRxSCStatsIntervalType = _F3ConnectGuardRxSCStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 2),
    _F3ConnectGuardRxSCStatsIntervalType_Type()
)
f3ConnectGuardRxSCStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsIntervalType.setStatus("current")
_F3ConnectGuardRxSCStatsValid_Type = TruthValue
_F3ConnectGuardRxSCStatsValid_Object = MibTableColumn
f3ConnectGuardRxSCStatsValid = _F3ConnectGuardRxSCStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 3),
    _F3ConnectGuardRxSCStatsValid_Type()
)
f3ConnectGuardRxSCStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsValid.setStatus("current")
_F3ConnectGuardRxSCStatsAction_Type = CmPmBinAction
_F3ConnectGuardRxSCStatsAction_Object = MibTableColumn
f3ConnectGuardRxSCStatsAction = _F3ConnectGuardRxSCStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 4),
    _F3ConnectGuardRxSCStatsAction_Type()
)
f3ConnectGuardRxSCStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsAction.setStatus("current")
_F3ConnectGuardRxSCStatsRxUnusedSAPkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxUnusedSAPkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxUnusedSAPkts = _F3ConnectGuardRxSCStatsRxUnusedSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 5),
    _F3ConnectGuardRxSCStatsRxUnusedSAPkts_Type()
)
f3ConnectGuardRxSCStatsRxUnusedSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxUnusedSAPkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxNoUsingSAPkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxNoUsingSAPkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxNoUsingSAPkts = _F3ConnectGuardRxSCStatsRxNoUsingSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 6),
    _F3ConnectGuardRxSCStatsRxNoUsingSAPkts_Type()
)
f3ConnectGuardRxSCStatsRxNoUsingSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxNoUsingSAPkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxLatePkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxLatePkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxLatePkts = _F3ConnectGuardRxSCStatsRxLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 7),
    _F3ConnectGuardRxSCStatsRxLatePkts_Type()
)
f3ConnectGuardRxSCStatsRxLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxLatePkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxNotValidPkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxNotValidPkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxNotValidPkts = _F3ConnectGuardRxSCStatsRxNotValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 8),
    _F3ConnectGuardRxSCStatsRxNotValidPkts_Type()
)
f3ConnectGuardRxSCStatsRxNotValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxNotValidPkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxInvalidPkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxInvalidPkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxInvalidPkts = _F3ConnectGuardRxSCStatsRxInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 9),
    _F3ConnectGuardRxSCStatsRxInvalidPkts_Type()
)
f3ConnectGuardRxSCStatsRxInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxInvalidPkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxDelayedPkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxDelayedPkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxDelayedPkts = _F3ConnectGuardRxSCStatsRxDelayedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 10),
    _F3ConnectGuardRxSCStatsRxDelayedPkts_Type()
)
f3ConnectGuardRxSCStatsRxDelayedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxDelayedPkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxUncheckedPkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxUncheckedPkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxUncheckedPkts = _F3ConnectGuardRxSCStatsRxUncheckedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 11),
    _F3ConnectGuardRxSCStatsRxUncheckedPkts_Type()
)
f3ConnectGuardRxSCStatsRxUncheckedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxUncheckedPkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxOKPkts_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxOKPkts_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxOKPkts = _F3ConnectGuardRxSCStatsRxOKPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 12),
    _F3ConnectGuardRxSCStatsRxOKPkts_Type()
)
f3ConnectGuardRxSCStatsRxOKPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxOKPkts.setStatus("current")
_F3ConnectGuardRxSCStatsRxOctetsValidated_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxOctetsValidated_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxOctetsValidated = _F3ConnectGuardRxSCStatsRxOctetsValidated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 13),
    _F3ConnectGuardRxSCStatsRxOctetsValidated_Type()
)
f3ConnectGuardRxSCStatsRxOctetsValidated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxOctetsValidated.setStatus("current")
_F3ConnectGuardRxSCStatsRxOctetsDecrypted_Type = PerfCounter64
_F3ConnectGuardRxSCStatsRxOctetsDecrypted_Object = MibTableColumn
f3ConnectGuardRxSCStatsRxOctetsDecrypted = _F3ConnectGuardRxSCStatsRxOctetsDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 7, 1, 14),
    _F3ConnectGuardRxSCStatsRxOctetsDecrypted_Type()
)
f3ConnectGuardRxSCStatsRxOctetsDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCStatsRxOctetsDecrypted.setStatus("current")
_F3ConnectGuardRxSCHistoryTable_Object = MibTable
f3ConnectGuardRxSCHistoryTable = _F3ConnectGuardRxSCHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8)
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryTable.setStatus("current")
_F3ConnectGuardRxSCHistoryEntry_Object = MibTableRow
f3ConnectGuardRxSCHistoryEntry = _F3ConnectGuardRxSCHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1)
)
f3ConnectGuardRxSCHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryEntry.setStatus("current")
_F3ConnectGuardRxSCHistoryIndex_Type = Integer32
_F3ConnectGuardRxSCHistoryIndex_Object = MibTableColumn
f3ConnectGuardRxSCHistoryIndex = _F3ConnectGuardRxSCHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 1),
    _F3ConnectGuardRxSCHistoryIndex_Type()
)
f3ConnectGuardRxSCHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryIndex.setStatus("current")
_F3ConnectGuardRxSCHistoryTime_Type = DateAndTime
_F3ConnectGuardRxSCHistoryTime_Object = MibTableColumn
f3ConnectGuardRxSCHistoryTime = _F3ConnectGuardRxSCHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 2),
    _F3ConnectGuardRxSCHistoryTime_Type()
)
f3ConnectGuardRxSCHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryTime.setStatus("current")
_F3ConnectGuardRxSCHistoryValid_Type = TruthValue
_F3ConnectGuardRxSCHistoryValid_Object = MibTableColumn
f3ConnectGuardRxSCHistoryValid = _F3ConnectGuardRxSCHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 3),
    _F3ConnectGuardRxSCHistoryValid_Type()
)
f3ConnectGuardRxSCHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryValid.setStatus("current")
_F3ConnectGuardRxSCHistoryAction_Type = CmPmBinAction
_F3ConnectGuardRxSCHistoryAction_Object = MibTableColumn
f3ConnectGuardRxSCHistoryAction = _F3ConnectGuardRxSCHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 4),
    _F3ConnectGuardRxSCHistoryAction_Type()
)
f3ConnectGuardRxSCHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryAction.setStatus("current")
_F3ConnectGuardRxSCHistoryRxUnusedSAPkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxUnusedSAPkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxUnusedSAPkts = _F3ConnectGuardRxSCHistoryRxUnusedSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 5),
    _F3ConnectGuardRxSCHistoryRxUnusedSAPkts_Type()
)
f3ConnectGuardRxSCHistoryRxUnusedSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxUnusedSAPkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxNoUsingSAPkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxNoUsingSAPkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxNoUsingSAPkts = _F3ConnectGuardRxSCHistoryRxNoUsingSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 6),
    _F3ConnectGuardRxSCHistoryRxNoUsingSAPkts_Type()
)
f3ConnectGuardRxSCHistoryRxNoUsingSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxNoUsingSAPkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxLatePkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxLatePkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxLatePkts = _F3ConnectGuardRxSCHistoryRxLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 7),
    _F3ConnectGuardRxSCHistoryRxLatePkts_Type()
)
f3ConnectGuardRxSCHistoryRxLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxLatePkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxNotValidPkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxNotValidPkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxNotValidPkts = _F3ConnectGuardRxSCHistoryRxNotValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 8),
    _F3ConnectGuardRxSCHistoryRxNotValidPkts_Type()
)
f3ConnectGuardRxSCHistoryRxNotValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxNotValidPkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxInvalidPkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxInvalidPkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxInvalidPkts = _F3ConnectGuardRxSCHistoryRxInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 9),
    _F3ConnectGuardRxSCHistoryRxInvalidPkts_Type()
)
f3ConnectGuardRxSCHistoryRxInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxInvalidPkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxDelayedPkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxDelayedPkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxDelayedPkts = _F3ConnectGuardRxSCHistoryRxDelayedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 10),
    _F3ConnectGuardRxSCHistoryRxDelayedPkts_Type()
)
f3ConnectGuardRxSCHistoryRxDelayedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxDelayedPkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxUncheckedPkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxUncheckedPkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxUncheckedPkts = _F3ConnectGuardRxSCHistoryRxUncheckedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 11),
    _F3ConnectGuardRxSCHistoryRxUncheckedPkts_Type()
)
f3ConnectGuardRxSCHistoryRxUncheckedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxUncheckedPkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxOKPkts_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxOKPkts_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxOKPkts = _F3ConnectGuardRxSCHistoryRxOKPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 12),
    _F3ConnectGuardRxSCHistoryRxOKPkts_Type()
)
f3ConnectGuardRxSCHistoryRxOKPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxOKPkts.setStatus("current")
_F3ConnectGuardRxSCHistoryRxOctetsValidated_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxOctetsValidated_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxOctetsValidated = _F3ConnectGuardRxSCHistoryRxOctetsValidated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 13),
    _F3ConnectGuardRxSCHistoryRxOctetsValidated_Type()
)
f3ConnectGuardRxSCHistoryRxOctetsValidated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxOctetsValidated.setStatus("current")
_F3ConnectGuardRxSCHistoryRxOctetsDecrypted_Type = PerfCounter64
_F3ConnectGuardRxSCHistoryRxOctetsDecrypted_Object = MibTableColumn
f3ConnectGuardRxSCHistoryRxOctetsDecrypted = _F3ConnectGuardRxSCHistoryRxOctetsDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 8, 1, 14),
    _F3ConnectGuardRxSCHistoryRxOctetsDecrypted_Type()
)
f3ConnectGuardRxSCHistoryRxOctetsDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCHistoryRxOctetsDecrypted.setStatus("current")
_F3ConnectGuardRxSCThresholdTable_Object = MibTable
f3ConnectGuardRxSCThresholdTable = _F3ConnectGuardRxSCThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9)
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdTable.setStatus("current")
_F3ConnectGuardRxSCThresholdEntry_Object = MibTableRow
f3ConnectGuardRxSCThresholdEntry = _F3ConnectGuardRxSCThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9, 1)
)
f3ConnectGuardRxSCThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdEntry.setStatus("current")


class _F3ConnectGuardRxSCThresholdIndex_Type(Integer32):
    """Custom type f3ConnectGuardRxSCThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3ConnectGuardRxSCThresholdIndex_Type.__name__ = "Integer32"
_F3ConnectGuardRxSCThresholdIndex_Object = MibTableColumn
f3ConnectGuardRxSCThresholdIndex = _F3ConnectGuardRxSCThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9, 1, 1),
    _F3ConnectGuardRxSCThresholdIndex_Type()
)
f3ConnectGuardRxSCThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdIndex.setStatus("current")
_F3ConnectGuardRxSCThresholdInterval_Type = CmPmIntervalType
_F3ConnectGuardRxSCThresholdInterval_Object = MibTableColumn
f3ConnectGuardRxSCThresholdInterval = _F3ConnectGuardRxSCThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9, 1, 2),
    _F3ConnectGuardRxSCThresholdInterval_Type()
)
f3ConnectGuardRxSCThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdInterval.setStatus("current")
_F3ConnectGuardRxSCThresholdVariable_Type = VariablePointer
_F3ConnectGuardRxSCThresholdVariable_Object = MibTableColumn
f3ConnectGuardRxSCThresholdVariable = _F3ConnectGuardRxSCThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9, 1, 3),
    _F3ConnectGuardRxSCThresholdVariable_Type()
)
f3ConnectGuardRxSCThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdVariable.setStatus("current")
_F3ConnectGuardRxSCThresholdValueLo_Type = Unsigned32
_F3ConnectGuardRxSCThresholdValueLo_Object = MibTableColumn
f3ConnectGuardRxSCThresholdValueLo = _F3ConnectGuardRxSCThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9, 1, 4),
    _F3ConnectGuardRxSCThresholdValueLo_Type()
)
f3ConnectGuardRxSCThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdValueLo.setStatus("current")
_F3ConnectGuardRxSCThresholdValueHi_Type = Unsigned32
_F3ConnectGuardRxSCThresholdValueHi_Object = MibTableColumn
f3ConnectGuardRxSCThresholdValueHi = _F3ConnectGuardRxSCThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9, 1, 5),
    _F3ConnectGuardRxSCThresholdValueHi_Type()
)
f3ConnectGuardRxSCThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdValueHi.setStatus("current")
_F3ConnectGuardRxSCThresholdMonValue_Type = PerfCounter64
_F3ConnectGuardRxSCThresholdMonValue_Object = MibTableColumn
f3ConnectGuardRxSCThresholdMonValue = _F3ConnectGuardRxSCThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 9, 1, 6),
    _F3ConnectGuardRxSCThresholdMonValue_Type()
)
f3ConnectGuardRxSCThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdMonValue.setStatus("current")
_F3ConnectGuardTxSAStatsTable_Object = MibTable
f3ConnectGuardTxSAStatsTable = _F3ConnectGuardTxSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 10)
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAStatsTable.setStatus("current")
_F3ConnectGuardTxSAStatsEntry_Object = MibTableRow
f3ConnectGuardTxSAStatsEntry = _F3ConnectGuardTxSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 10, 1)
)
f3ConnectGuardTxSAStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAStatsEntry.setStatus("current")
_F3ConnectGuardTxSAStatsProtectedPkts_Type = PerfCounter64
_F3ConnectGuardTxSAStatsProtectedPkts_Object = MibTableColumn
f3ConnectGuardTxSAStatsProtectedPkts = _F3ConnectGuardTxSAStatsProtectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 10, 1, 1),
    _F3ConnectGuardTxSAStatsProtectedPkts_Type()
)
f3ConnectGuardTxSAStatsProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAStatsProtectedPkts.setStatus("current")
_F3ConnectGuardTxSAStatsEncryptedPkts_Type = PerfCounter64
_F3ConnectGuardTxSAStatsEncryptedPkts_Object = MibTableColumn
f3ConnectGuardTxSAStatsEncryptedPkts = _F3ConnectGuardTxSAStatsEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 10, 1, 2),
    _F3ConnectGuardTxSAStatsEncryptedPkts_Type()
)
f3ConnectGuardTxSAStatsEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardTxSAStatsEncryptedPkts.setStatus("current")
_F3ConnectGuardRxSAStatsTable_Object = MibTable
f3ConnectGuardRxSAStatsTable = _F3ConnectGuardRxSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 11)
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStatsTable.setStatus("current")
_F3ConnectGuardRxSAStatsEntry_Object = MibTableRow
f3ConnectGuardRxSAStatsEntry = _F3ConnectGuardRxSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 11, 1)
)
f3ConnectGuardRxSAStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCIndex"),
    (0, "F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAIndex"),
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStatsEntry.setStatus("current")
_F3ConnectGuardRxSAStatsUnusedSAPkts_Type = PerfCounter64
_F3ConnectGuardRxSAStatsUnusedSAPkts_Object = MibTableColumn
f3ConnectGuardRxSAStatsUnusedSAPkts = _F3ConnectGuardRxSAStatsUnusedSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 11, 1, 1),
    _F3ConnectGuardRxSAStatsUnusedSAPkts_Type()
)
f3ConnectGuardRxSAStatsUnusedSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStatsUnusedSAPkts.setStatus("current")
_F3ConnectGuardRxSAStatsNoUsingSAPkts_Type = PerfCounter64
_F3ConnectGuardRxSAStatsNoUsingSAPkts_Object = MibTableColumn
f3ConnectGuardRxSAStatsNoUsingSAPkts = _F3ConnectGuardRxSAStatsNoUsingSAPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 11, 1, 2),
    _F3ConnectGuardRxSAStatsNoUsingSAPkts_Type()
)
f3ConnectGuardRxSAStatsNoUsingSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStatsNoUsingSAPkts.setStatus("current")
_F3ConnectGuardRxSAStatsNotValidPkts_Type = PerfCounter64
_F3ConnectGuardRxSAStatsNotValidPkts_Object = MibTableColumn
f3ConnectGuardRxSAStatsNotValidPkts = _F3ConnectGuardRxSAStatsNotValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 11, 1, 3),
    _F3ConnectGuardRxSAStatsNotValidPkts_Type()
)
f3ConnectGuardRxSAStatsNotValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStatsNotValidPkts.setStatus("current")
_F3ConnectGuardRxSAStatsInvalidPkts_Type = PerfCounter64
_F3ConnectGuardRxSAStatsInvalidPkts_Object = MibTableColumn
f3ConnectGuardRxSAStatsInvalidPkts = _F3ConnectGuardRxSAStatsInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 11, 1, 4),
    _F3ConnectGuardRxSAStatsInvalidPkts_Type()
)
f3ConnectGuardRxSAStatsInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStatsInvalidPkts.setStatus("current")
_F3ConnectGuardRxSAStatsOKPkts_Type = PerfCounter64
_F3ConnectGuardRxSAStatsOKPkts_Object = MibTableColumn
f3ConnectGuardRxSAStatsOKPkts = _F3ConnectGuardRxSAStatsOKPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 2, 11, 1, 5),
    _F3ConnectGuardRxSAStatsOKPkts_Type()
)
f3ConnectGuardRxSAStatsOKPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ConnectGuardRxSAStatsOKPkts.setStatus("current")
_F3ConnectGuardNotifications_ObjectIdentity = ObjectIdentity
f3ConnectGuardNotifications = _F3ConnectGuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 3)
)
_F3ConnectGuardConformance_ObjectIdentity = ObjectIdentity
f3ConnectGuardConformance = _F3ConnectGuardConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 4)
)
_F3ConnectGuardCompliances_ObjectIdentity = ObjectIdentity
f3ConnectGuardCompliances = _F3ConnectGuardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 4, 1)
)
_F3ConnectGuardGroups_ObjectIdentity = ObjectIdentity
f3ConnectGuardGroups = _F3ConnectGuardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 4, 2)
)
cmFlowEntry.registerAugmentions(
    ("F3-CONNECTGUARD-MIB",
     "f3FlowExtConnectGuardEntry")
)
f3FlowExtConnectGuardEntry.setIndexNames(*cmFlowEntry.getIndexNames())

# Managed Objects groups

f3ConnectGuardObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 4, 2, 1)
)
f3ConnectGuardObjectsGroup.setObjects(
      *(("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowEgressInterface"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowAdminState"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowSecondaryState"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowOperationalState"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowCipherSuite"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeProfile"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameTagControl"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameOuterVlanId"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner1VlanId"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner2VlanId"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeInterval"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowTagsClear"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStorageType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowRowStatus"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyXchgFailsCounts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowAction"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowReplayProtectionEnabled"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowReplayProtectionWindow"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowRemoteMacAddrEnabled"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowRemoteMacAddr"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowAssociatedMep"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowAlias"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowKeyInjectFlowPoint"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileName"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileUserId"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileMode"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileAuthPassword"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileStorageType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardKeyExchangeProfileRowStatus"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCI"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxScState"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardCurrentTxSa"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardPreviousTxSa"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxScCreateTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxScStartTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxScStopTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCI"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxScState"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardCurrentRxSa"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxScCreateTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxScStartTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxScStopTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAState"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSANextPN"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSASAKUnchanged"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSACreatedTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAStartedTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAStoppedTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAState"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSANextPN"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSASAKUnchanged"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSACreatedTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAStartedTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAStoppedTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardCryptoPassword"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRestoreFactoryApproved"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardSoftwareVersionApproved"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardSoftwareInstallApproved"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRestoreDatabaseApproved"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardConfigFileLoadApproved"))
)
if mibBuilder.loadTexts:
    f3ConnectGuardObjectsGroup.setStatus("current")

f3ConnectGuardPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 4, 2, 2)
)
f3ConnectGuardPerfGroup.setObjects(
      *(("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsIntervalType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsValid"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsAction"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsTxUntaggedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsTxTooLongPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsRxUntaggedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsRxNotagPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsRxBadtagPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsRxUnknownSCIPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsRxNoSCIPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowStatsRxOverrunPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryValid"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryAction"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryTxUntaggedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryTxTooLongPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryRxUntaggedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryRxNotagPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryRxBadtagPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryRxUnknownSCIPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryRxNoSCIPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowHistoryRxOverrunPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdInterval"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdVariable"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdValueLo"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdValueHi"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdMonValue"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsIntervalType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsValid"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsAction"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsTxProtectedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsTxEncryptedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsTxOctetsProtected"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCStatsTxOctetsEncrypted"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryValid"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryAction"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryTxProtectedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryTxEncryptedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryTxOctetsProtected"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCHistoryTxOctetsEncrypted"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdInterval"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdVariable"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdValueLo"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdValueHi"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdMonValue"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsIntervalType"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsValid"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsAction"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxUnusedSAPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxNoUsingSAPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxLatePkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxNotValidPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxInvalidPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxDelayedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxUncheckedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxOKPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxOctetsValidated"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCStatsRxOctetsDecrypted"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryTime"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryValid"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryAction"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxUnusedSAPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxNoUsingSAPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxLatePkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxNotValidPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxInvalidPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxDelayedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxUncheckedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxOKPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxOctetsValidated"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCHistoryRxOctetsDecrypted"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdInterval"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdVariable"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdValueLo"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdValueHi"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdMonValue"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAStatsProtectedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSAStatsEncryptedPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAStatsUnusedSAPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAStatsNoUsingSAPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAStatsNotValidPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAStatsInvalidPkts"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSAStatsOKPkts"))
)
if mibBuilder.loadTexts:
    f3ConnectGuardPerfGroup.setStatus("current")


# Notification objects

f3ConnectGuardFlowThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 3, 1)
)
f3ConnectGuardFlowThresholdCrossingAlert.setObjects(
      *(("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdInterval"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdVariable"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdValueLo"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdValueHi"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardFlowThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3ConnectGuardFlowThresholdCrossingAlert.setStatus(
        "current"
    )

f3ConnectGuardTxSCThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 3, 2)
)
f3ConnectGuardTxSCThresholdCrossingAlert.setObjects(
      *(("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdInterval"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdVariable"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdValueLo"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdValueHi"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardTxSCThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3ConnectGuardTxSCThresholdCrossingAlert.setStatus(
        "current"
    )

f3ConnectGuardRxSCThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 3, 3)
)
f3ConnectGuardRxSCThresholdCrossingAlert.setObjects(
      *(("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdIndex"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdInterval"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdVariable"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdValueLo"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdValueHi"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardRxSCThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3ConnectGuardRxSCThresholdCrossingAlert.setStatus(
        "current"
    )

f3ConnectGuardStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 3, 4)
)
f3ConnectGuardStateChangeTrap.setObjects(
    ("F3-CONNECTGUARD-MIB", "f3FlowSecureState")
)
if mibBuilder.loadTexts:
    f3ConnectGuardStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

f3ConnectGuardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 36, 4, 1, 1)
)
f3ConnectGuardCompliance.setObjects(
      *(("F3-CONNECTGUARD-MIB", "f3ConnectGuardObjectsGroup"),
        ("F3-CONNECTGUARD-MIB", "f3ConnectGuardPerfGroup"))
)
if mibBuilder.loadTexts:
    f3ConnectGuardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-CONNECTGUARD-MIB",
    **{"FlowSecureState": FlowSecureState,
       "CipherSuiteType": CipherSuiteType,
       "KeyExchangeFrameTagControl": KeyExchangeFrameTagControl,
       "ScSaState": ScSaState,
       "ConnectGuardKeyExMode": ConnectGuardKeyExMode,
       "DiffieHellmanKeyPairLength": DiffieHellmanKeyPairLength,
       "ConnectGuardFlowActionType": ConnectGuardFlowActionType,
       "f3ConnectGuardMIB": f3ConnectGuardMIB,
       "f3ConnectGuardConfigObjects": f3ConnectGuardConfigObjects,
       "f3ConnectGuardFlowTable": f3ConnectGuardFlowTable,
       "f3ConnectGuardFlowEntry": f3ConnectGuardFlowEntry,
       "f3ConnectGuardFlowIndex": f3ConnectGuardFlowIndex,
       "f3ConnectGuardFlowCipherSuite": f3ConnectGuardFlowCipherSuite,
       "f3ConnectGuardFlowAdminState": f3ConnectGuardFlowAdminState,
       "f3ConnectGuardFlowSecondaryState": f3ConnectGuardFlowSecondaryState,
       "f3ConnectGuardFlowOperationalState": f3ConnectGuardFlowOperationalState,
       "f3ConnectGuardFlowEgressInterface": f3ConnectGuardFlowEgressInterface,
       "f3ConnectGuardFlowKeyExchangeProfile": f3ConnectGuardFlowKeyExchangeProfile,
       "f3ConnectGuardFlowKeyExchangeFrameTagControl": f3ConnectGuardFlowKeyExchangeFrameTagControl,
       "f3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled": f3ConnectGuardFlowKeyExchangeFrameOuterVlanEnabled,
       "f3ConnectGuardFlowKeyExchangeFrameOuterVlanId": f3ConnectGuardFlowKeyExchangeFrameOuterVlanId,
       "f3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority": f3ConnectGuardFlowKeyExchangeFrameOuterVlanPriority,
       "f3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled": f3ConnectGuardFlowKeyExchangeFrameInner1VlanEnabled,
       "f3ConnectGuardFlowKeyExchangeFrameInner1VlanId": f3ConnectGuardFlowKeyExchangeFrameInner1VlanId,
       "f3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority": f3ConnectGuardFlowKeyExchangeFrameInner1VlanPriority,
       "f3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled": f3ConnectGuardFlowKeyExchangeFrameInner2VlanEnabled,
       "f3ConnectGuardFlowKeyExchangeFrameInner2VlanId": f3ConnectGuardFlowKeyExchangeFrameInner2VlanId,
       "f3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority": f3ConnectGuardFlowKeyExchangeFrameInner2VlanPriority,
       "f3ConnectGuardFlowKeyExchangeInterval": f3ConnectGuardFlowKeyExchangeInterval,
       "f3ConnectGuardFlowTagsClear": f3ConnectGuardFlowTagsClear,
       "f3ConnectGuardFlowStorageType": f3ConnectGuardFlowStorageType,
       "f3ConnectGuardFlowRowStatus": f3ConnectGuardFlowRowStatus,
       "f3ConnectGuardFlowKeyXchgFailsCounts": f3ConnectGuardFlowKeyXchgFailsCounts,
       "f3ConnectGuardFlowAction": f3ConnectGuardFlowAction,
       "f3ConnectGuardFlowReplayProtectionEnabled": f3ConnectGuardFlowReplayProtectionEnabled,
       "f3ConnectGuardFlowReplayProtectionWindow": f3ConnectGuardFlowReplayProtectionWindow,
       "f3ConnectGuardFlowRemoteMacAddrEnabled": f3ConnectGuardFlowRemoteMacAddrEnabled,
       "f3ConnectGuardFlowRemoteMacAddr": f3ConnectGuardFlowRemoteMacAddr,
       "f3ConnectGuardFlowAssociatedMep": f3ConnectGuardFlowAssociatedMep,
       "f3ConnectGuardFlowAlias": f3ConnectGuardFlowAlias,
       "f3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType": f3ConnectGuardFlowKeyExchangeFrameOuterVlanEtherType,
       "f3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType": f3ConnectGuardFlowKeyExchangeFrameInner1VlanEtherType,
       "f3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType": f3ConnectGuardFlowKeyExchangeFrameInner2VlanEtherType,
       "f3ConnectGuardFlowKeyInjectFlowPoint": f3ConnectGuardFlowKeyInjectFlowPoint,
       "f3ConnectGuardKeyExchangeProfileTable": f3ConnectGuardKeyExchangeProfileTable,
       "f3ConnectGuardKeyExchangeProfileEntry": f3ConnectGuardKeyExchangeProfileEntry,
       "f3ConnectGuardKeyExchangeProfileIndex": f3ConnectGuardKeyExchangeProfileIndex,
       "f3ConnectGuardKeyExchangeProfileName": f3ConnectGuardKeyExchangeProfileName,
       "f3ConnectGuardKeyExchangeProfileUserId": f3ConnectGuardKeyExchangeProfileUserId,
       "f3ConnectGuardKeyExchangeProfileMode": f3ConnectGuardKeyExchangeProfileMode,
       "f3ConnectGuardKeyExchangeProfileAuthPassword": f3ConnectGuardKeyExchangeProfileAuthPassword,
       "f3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen": f3ConnectGuardKeyExchangeProfileDiffieHellmanKeyPairLen,
       "f3ConnectGuardKeyExchangeProfileStorageType": f3ConnectGuardKeyExchangeProfileStorageType,
       "f3ConnectGuardKeyExchangeProfileRowStatus": f3ConnectGuardKeyExchangeProfileRowStatus,
       "f3ConnectGuardTxSCTable": f3ConnectGuardTxSCTable,
       "f3ConnectGuardTxSCEntry": f3ConnectGuardTxSCEntry,
       "f3ConnectGuardTxSCIndex": f3ConnectGuardTxSCIndex,
       "f3ConnectGuardTxSCI": f3ConnectGuardTxSCI,
       "f3ConnectGuardTxScState": f3ConnectGuardTxScState,
       "f3ConnectGuardCurrentTxSa": f3ConnectGuardCurrentTxSa,
       "f3ConnectGuardPreviousTxSa": f3ConnectGuardPreviousTxSa,
       "f3ConnectGuardTxScCreateTime": f3ConnectGuardTxScCreateTime,
       "f3ConnectGuardTxScStartTime": f3ConnectGuardTxScStartTime,
       "f3ConnectGuardTxScStopTime": f3ConnectGuardTxScStopTime,
       "f3ConnectGuardRxSCTable": f3ConnectGuardRxSCTable,
       "f3ConnectGuardRxSCEntry": f3ConnectGuardRxSCEntry,
       "f3ConnectGuardRxSCIndex": f3ConnectGuardRxSCIndex,
       "f3ConnectGuardRxSCI": f3ConnectGuardRxSCI,
       "f3ConnectGuardRxScState": f3ConnectGuardRxScState,
       "f3ConnectGuardCurrentRxSa": f3ConnectGuardCurrentRxSa,
       "f3ConnectGuardRxScCreateTime": f3ConnectGuardRxScCreateTime,
       "f3ConnectGuardRxScStartTime": f3ConnectGuardRxScStartTime,
       "f3ConnectGuardRxScStopTime": f3ConnectGuardRxScStopTime,
       "f3ConnectGuardTxSATable": f3ConnectGuardTxSATable,
       "f3ConnectGuardTxSAEntry": f3ConnectGuardTxSAEntry,
       "f3ConnectGuardTxSAIndex": f3ConnectGuardTxSAIndex,
       "f3ConnectGuardTxSAState": f3ConnectGuardTxSAState,
       "f3ConnectGuardTxSANextPN": f3ConnectGuardTxSANextPN,
       "f3ConnectGuardTxSASAKUnchanged": f3ConnectGuardTxSASAKUnchanged,
       "f3ConnectGuardTxSACreatedTime": f3ConnectGuardTxSACreatedTime,
       "f3ConnectGuardTxSAStartedTime": f3ConnectGuardTxSAStartedTime,
       "f3ConnectGuardTxSAStoppedTime": f3ConnectGuardTxSAStoppedTime,
       "f3ConnectGuardRxSATable": f3ConnectGuardRxSATable,
       "f3ConnectGuardRxSAEntry": f3ConnectGuardRxSAEntry,
       "f3ConnectGuardRxSAIndex": f3ConnectGuardRxSAIndex,
       "f3ConnectGuardRxSAState": f3ConnectGuardRxSAState,
       "f3ConnectGuardRxSANextPN": f3ConnectGuardRxSANextPN,
       "f3ConnectGuardRxSASAKUnchanged": f3ConnectGuardRxSASAKUnchanged,
       "f3ConnectGuardRxSACreatedTime": f3ConnectGuardRxSACreatedTime,
       "f3ConnectGuardRxSAStartedTime": f3ConnectGuardRxSAStartedTime,
       "f3ConnectGuardRxSAStoppedTime": f3ConnectGuardRxSAStoppedTime,
       "f3FlowExtConnectGuardTable": f3FlowExtConnectGuardTable,
       "f3FlowExtConnectGuardEntry": f3FlowExtConnectGuardEntry,
       "f3FlowRefConnectGuardFlowObject": f3FlowRefConnectGuardFlowObject,
       "f3FlowSecureBlockingEnabled": f3FlowSecureBlockingEnabled,
       "f3FlowSecureState": f3FlowSecureState,
       "f3ConnectGuardConfigScalars": f3ConnectGuardConfigScalars,
       "f3ConnectGuardRestoreFactoryApproved": f3ConnectGuardRestoreFactoryApproved,
       "f3ConnectGuardSoftwareVersionApproved": f3ConnectGuardSoftwareVersionApproved,
       "f3ConnectGuardSoftwareInstallApproved": f3ConnectGuardSoftwareInstallApproved,
       "f3ConnectGuardRestoreDatabaseApproved": f3ConnectGuardRestoreDatabaseApproved,
       "f3ConnectGuardConfigFileLoadApproved": f3ConnectGuardConfigFileLoadApproved,
       "f3ConnectGuardCryptoPasswordControl": f3ConnectGuardCryptoPasswordControl,
       "f3ConnectGuardPasswordScalars": f3ConnectGuardPasswordScalars,
       "f3ConnectGuardCryptoPassword": f3ConnectGuardCryptoPassword,
       "f3ConnectGuardPerformanceObjects": f3ConnectGuardPerformanceObjects,
       "f3ConnectGuardFlowStatsTable": f3ConnectGuardFlowStatsTable,
       "f3ConnectGuardFlowStatsEntry": f3ConnectGuardFlowStatsEntry,
       "f3ConnectGuardFlowStatsIndex": f3ConnectGuardFlowStatsIndex,
       "f3ConnectGuardFlowStatsIntervalType": f3ConnectGuardFlowStatsIntervalType,
       "f3ConnectGuardFlowStatsValid": f3ConnectGuardFlowStatsValid,
       "f3ConnectGuardFlowStatsAction": f3ConnectGuardFlowStatsAction,
       "f3ConnectGuardFlowStatsTxUntaggedPkts": f3ConnectGuardFlowStatsTxUntaggedPkts,
       "f3ConnectGuardFlowStatsTxTooLongPkts": f3ConnectGuardFlowStatsTxTooLongPkts,
       "f3ConnectGuardFlowStatsRxUntaggedPkts": f3ConnectGuardFlowStatsRxUntaggedPkts,
       "f3ConnectGuardFlowStatsRxNotagPkts": f3ConnectGuardFlowStatsRxNotagPkts,
       "f3ConnectGuardFlowStatsRxBadtagPkts": f3ConnectGuardFlowStatsRxBadtagPkts,
       "f3ConnectGuardFlowStatsRxUnknownSCIPkts": f3ConnectGuardFlowStatsRxUnknownSCIPkts,
       "f3ConnectGuardFlowStatsRxNoSCIPkts": f3ConnectGuardFlowStatsRxNoSCIPkts,
       "f3ConnectGuardFlowStatsRxOverrunPkts": f3ConnectGuardFlowStatsRxOverrunPkts,
       "f3ConnectGuardFlowHistoryTable": f3ConnectGuardFlowHistoryTable,
       "f3ConnectGuardFlowHistoryEntry": f3ConnectGuardFlowHistoryEntry,
       "f3ConnectGuardFlowHistoryIndex": f3ConnectGuardFlowHistoryIndex,
       "f3ConnectGuardFlowHistoryTime": f3ConnectGuardFlowHistoryTime,
       "f3ConnectGuardFlowHistoryValid": f3ConnectGuardFlowHistoryValid,
       "f3ConnectGuardFlowHistoryAction": f3ConnectGuardFlowHistoryAction,
       "f3ConnectGuardFlowHistoryTxUntaggedPkts": f3ConnectGuardFlowHistoryTxUntaggedPkts,
       "f3ConnectGuardFlowHistoryTxTooLongPkts": f3ConnectGuardFlowHistoryTxTooLongPkts,
       "f3ConnectGuardFlowHistoryRxUntaggedPkts": f3ConnectGuardFlowHistoryRxUntaggedPkts,
       "f3ConnectGuardFlowHistoryRxNotagPkts": f3ConnectGuardFlowHistoryRxNotagPkts,
       "f3ConnectGuardFlowHistoryRxBadtagPkts": f3ConnectGuardFlowHistoryRxBadtagPkts,
       "f3ConnectGuardFlowHistoryRxUnknownSCIPkts": f3ConnectGuardFlowHistoryRxUnknownSCIPkts,
       "f3ConnectGuardFlowHistoryRxNoSCIPkts": f3ConnectGuardFlowHistoryRxNoSCIPkts,
       "f3ConnectGuardFlowHistoryRxOverrunPkts": f3ConnectGuardFlowHistoryRxOverrunPkts,
       "f3ConnectGuardFlowThresholdTable": f3ConnectGuardFlowThresholdTable,
       "f3ConnectGuardFlowThresholdEntry": f3ConnectGuardFlowThresholdEntry,
       "f3ConnectGuardFlowThresholdIndex": f3ConnectGuardFlowThresholdIndex,
       "f3ConnectGuardFlowThresholdInterval": f3ConnectGuardFlowThresholdInterval,
       "f3ConnectGuardFlowThresholdVariable": f3ConnectGuardFlowThresholdVariable,
       "f3ConnectGuardFlowThresholdValueLo": f3ConnectGuardFlowThresholdValueLo,
       "f3ConnectGuardFlowThresholdValueHi": f3ConnectGuardFlowThresholdValueHi,
       "f3ConnectGuardFlowThresholdMonValue": f3ConnectGuardFlowThresholdMonValue,
       "f3ConnectGuardTxSCStatsTable": f3ConnectGuardTxSCStatsTable,
       "f3ConnectGuardTxSCStatsEntry": f3ConnectGuardTxSCStatsEntry,
       "f3ConnectGuardTxSCStatsIndex": f3ConnectGuardTxSCStatsIndex,
       "f3ConnectGuardTxSCStatsIntervalType": f3ConnectGuardTxSCStatsIntervalType,
       "f3ConnectGuardTxSCStatsValid": f3ConnectGuardTxSCStatsValid,
       "f3ConnectGuardTxSCStatsAction": f3ConnectGuardTxSCStatsAction,
       "f3ConnectGuardTxSCStatsTxProtectedPkts": f3ConnectGuardTxSCStatsTxProtectedPkts,
       "f3ConnectGuardTxSCStatsTxEncryptedPkts": f3ConnectGuardTxSCStatsTxEncryptedPkts,
       "f3ConnectGuardTxSCStatsTxOctetsProtected": f3ConnectGuardTxSCStatsTxOctetsProtected,
       "f3ConnectGuardTxSCStatsTxOctetsEncrypted": f3ConnectGuardTxSCStatsTxOctetsEncrypted,
       "f3ConnectGuardTxSCHistoryTable": f3ConnectGuardTxSCHistoryTable,
       "f3ConnectGuardTxSCHistoryEntry": f3ConnectGuardTxSCHistoryEntry,
       "f3ConnectGuardTxSCHistoryIndex": f3ConnectGuardTxSCHistoryIndex,
       "f3ConnectGuardTxSCHistoryTime": f3ConnectGuardTxSCHistoryTime,
       "f3ConnectGuardTxSCHistoryValid": f3ConnectGuardTxSCHistoryValid,
       "f3ConnectGuardTxSCHistoryAction": f3ConnectGuardTxSCHistoryAction,
       "f3ConnectGuardTxSCHistoryTxProtectedPkts": f3ConnectGuardTxSCHistoryTxProtectedPkts,
       "f3ConnectGuardTxSCHistoryTxEncryptedPkts": f3ConnectGuardTxSCHistoryTxEncryptedPkts,
       "f3ConnectGuardTxSCHistoryTxOctetsProtected": f3ConnectGuardTxSCHistoryTxOctetsProtected,
       "f3ConnectGuardTxSCHistoryTxOctetsEncrypted": f3ConnectGuardTxSCHistoryTxOctetsEncrypted,
       "f3ConnectGuardTxSCThresholdTable": f3ConnectGuardTxSCThresholdTable,
       "f3ConnectGuardTxSCThresholdEntry": f3ConnectGuardTxSCThresholdEntry,
       "f3ConnectGuardTxSCThresholdIndex": f3ConnectGuardTxSCThresholdIndex,
       "f3ConnectGuardTxSCThresholdInterval": f3ConnectGuardTxSCThresholdInterval,
       "f3ConnectGuardTxSCThresholdVariable": f3ConnectGuardTxSCThresholdVariable,
       "f3ConnectGuardTxSCThresholdValueLo": f3ConnectGuardTxSCThresholdValueLo,
       "f3ConnectGuardTxSCThresholdValueHi": f3ConnectGuardTxSCThresholdValueHi,
       "f3ConnectGuardTxSCThresholdMonValue": f3ConnectGuardTxSCThresholdMonValue,
       "f3ConnectGuardRxSCStatsTable": f3ConnectGuardRxSCStatsTable,
       "f3ConnectGuardRxSCStatsEntry": f3ConnectGuardRxSCStatsEntry,
       "f3ConnectGuardRxSCStatsIndex": f3ConnectGuardRxSCStatsIndex,
       "f3ConnectGuardRxSCStatsIntervalType": f3ConnectGuardRxSCStatsIntervalType,
       "f3ConnectGuardRxSCStatsValid": f3ConnectGuardRxSCStatsValid,
       "f3ConnectGuardRxSCStatsAction": f3ConnectGuardRxSCStatsAction,
       "f3ConnectGuardRxSCStatsRxUnusedSAPkts": f3ConnectGuardRxSCStatsRxUnusedSAPkts,
       "f3ConnectGuardRxSCStatsRxNoUsingSAPkts": f3ConnectGuardRxSCStatsRxNoUsingSAPkts,
       "f3ConnectGuardRxSCStatsRxLatePkts": f3ConnectGuardRxSCStatsRxLatePkts,
       "f3ConnectGuardRxSCStatsRxNotValidPkts": f3ConnectGuardRxSCStatsRxNotValidPkts,
       "f3ConnectGuardRxSCStatsRxInvalidPkts": f3ConnectGuardRxSCStatsRxInvalidPkts,
       "f3ConnectGuardRxSCStatsRxDelayedPkts": f3ConnectGuardRxSCStatsRxDelayedPkts,
       "f3ConnectGuardRxSCStatsRxUncheckedPkts": f3ConnectGuardRxSCStatsRxUncheckedPkts,
       "f3ConnectGuardRxSCStatsRxOKPkts": f3ConnectGuardRxSCStatsRxOKPkts,
       "f3ConnectGuardRxSCStatsRxOctetsValidated": f3ConnectGuardRxSCStatsRxOctetsValidated,
       "f3ConnectGuardRxSCStatsRxOctetsDecrypted": f3ConnectGuardRxSCStatsRxOctetsDecrypted,
       "f3ConnectGuardRxSCHistoryTable": f3ConnectGuardRxSCHistoryTable,
       "f3ConnectGuardRxSCHistoryEntry": f3ConnectGuardRxSCHistoryEntry,
       "f3ConnectGuardRxSCHistoryIndex": f3ConnectGuardRxSCHistoryIndex,
       "f3ConnectGuardRxSCHistoryTime": f3ConnectGuardRxSCHistoryTime,
       "f3ConnectGuardRxSCHistoryValid": f3ConnectGuardRxSCHistoryValid,
       "f3ConnectGuardRxSCHistoryAction": f3ConnectGuardRxSCHistoryAction,
       "f3ConnectGuardRxSCHistoryRxUnusedSAPkts": f3ConnectGuardRxSCHistoryRxUnusedSAPkts,
       "f3ConnectGuardRxSCHistoryRxNoUsingSAPkts": f3ConnectGuardRxSCHistoryRxNoUsingSAPkts,
       "f3ConnectGuardRxSCHistoryRxLatePkts": f3ConnectGuardRxSCHistoryRxLatePkts,
       "f3ConnectGuardRxSCHistoryRxNotValidPkts": f3ConnectGuardRxSCHistoryRxNotValidPkts,
       "f3ConnectGuardRxSCHistoryRxInvalidPkts": f3ConnectGuardRxSCHistoryRxInvalidPkts,
       "f3ConnectGuardRxSCHistoryRxDelayedPkts": f3ConnectGuardRxSCHistoryRxDelayedPkts,
       "f3ConnectGuardRxSCHistoryRxUncheckedPkts": f3ConnectGuardRxSCHistoryRxUncheckedPkts,
       "f3ConnectGuardRxSCHistoryRxOKPkts": f3ConnectGuardRxSCHistoryRxOKPkts,
       "f3ConnectGuardRxSCHistoryRxOctetsValidated": f3ConnectGuardRxSCHistoryRxOctetsValidated,
       "f3ConnectGuardRxSCHistoryRxOctetsDecrypted": f3ConnectGuardRxSCHistoryRxOctetsDecrypted,
       "f3ConnectGuardRxSCThresholdTable": f3ConnectGuardRxSCThresholdTable,
       "f3ConnectGuardRxSCThresholdEntry": f3ConnectGuardRxSCThresholdEntry,
       "f3ConnectGuardRxSCThresholdIndex": f3ConnectGuardRxSCThresholdIndex,
       "f3ConnectGuardRxSCThresholdInterval": f3ConnectGuardRxSCThresholdInterval,
       "f3ConnectGuardRxSCThresholdVariable": f3ConnectGuardRxSCThresholdVariable,
       "f3ConnectGuardRxSCThresholdValueLo": f3ConnectGuardRxSCThresholdValueLo,
       "f3ConnectGuardRxSCThresholdValueHi": f3ConnectGuardRxSCThresholdValueHi,
       "f3ConnectGuardRxSCThresholdMonValue": f3ConnectGuardRxSCThresholdMonValue,
       "f3ConnectGuardTxSAStatsTable": f3ConnectGuardTxSAStatsTable,
       "f3ConnectGuardTxSAStatsEntry": f3ConnectGuardTxSAStatsEntry,
       "f3ConnectGuardTxSAStatsProtectedPkts": f3ConnectGuardTxSAStatsProtectedPkts,
       "f3ConnectGuardTxSAStatsEncryptedPkts": f3ConnectGuardTxSAStatsEncryptedPkts,
       "f3ConnectGuardRxSAStatsTable": f3ConnectGuardRxSAStatsTable,
       "f3ConnectGuardRxSAStatsEntry": f3ConnectGuardRxSAStatsEntry,
       "f3ConnectGuardRxSAStatsUnusedSAPkts": f3ConnectGuardRxSAStatsUnusedSAPkts,
       "f3ConnectGuardRxSAStatsNoUsingSAPkts": f3ConnectGuardRxSAStatsNoUsingSAPkts,
       "f3ConnectGuardRxSAStatsNotValidPkts": f3ConnectGuardRxSAStatsNotValidPkts,
       "f3ConnectGuardRxSAStatsInvalidPkts": f3ConnectGuardRxSAStatsInvalidPkts,
       "f3ConnectGuardRxSAStatsOKPkts": f3ConnectGuardRxSAStatsOKPkts,
       "f3ConnectGuardNotifications": f3ConnectGuardNotifications,
       "f3ConnectGuardFlowThresholdCrossingAlert": f3ConnectGuardFlowThresholdCrossingAlert,
       "f3ConnectGuardTxSCThresholdCrossingAlert": f3ConnectGuardTxSCThresholdCrossingAlert,
       "f3ConnectGuardRxSCThresholdCrossingAlert": f3ConnectGuardRxSCThresholdCrossingAlert,
       "f3ConnectGuardStateChangeTrap": f3ConnectGuardStateChangeTrap,
       "f3ConnectGuardConformance": f3ConnectGuardConformance,
       "f3ConnectGuardCompliances": f3ConnectGuardCompliances,
       "f3ConnectGuardCompliance": f3ConnectGuardCompliance,
       "f3ConnectGuardGroups": f3ConnectGuardGroups,
       "f3ConnectGuardObjectsGroup": f3ConnectGuardObjectsGroup,
       "f3ConnectGuardPerfGroup": f3ConnectGuardPerfGroup}
)
