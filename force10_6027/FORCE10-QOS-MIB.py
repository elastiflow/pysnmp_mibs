# SNMP MIB module (FORCE10-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/FORCE10-QOS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:05 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(F10QueueID,
 F10SlotState) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "F10QueueID",
    "F10SlotState")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

f10QosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrafficDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )



class QosClassMapMatchType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAll", 1),
          ("matchAny", 2))
    )



class PolicyMapHonoringType(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("dscp", 2),
          ("mplsExp", 3),
          ("dot1p", 4))
    )



class MatchObjectType(TextualConvention, Integer32):
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("embededClassMap", 2),
          ("ipAcl", 3),
          ("macAcl", 4),
          ("ipPrecedence", 5),
          ("ipDscp", 6),
          ("ipProtocol", 7),
          ("macProtocol", 8),
          ("vlan", 9),
          ("mplsExp", 10),
          ("dot1p", 11))
    )



class QosPolicyState(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_F10QosGroup_ObjectIdentity = ObjectIdentity
f10QosGroup = _F10QosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 1)
)


class _F10QosMibVersion_Type(Integer32):
    """Custom type f10QosMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_F10QosMibVersion_Type.__name__ = "Integer32"
_F10QosMibVersion_Object = MibScalar
f10QosMibVersion = _F10QosMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 1, 1),
    _F10QosMibVersion_Type()
)
f10QosMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10QosMibVersion.setStatus("current")
_F10QosMaxWredProfile_Type = Integer32
_F10QosMaxWredProfile_Object = MibScalar
f10QosMaxWredProfile = _F10QosMaxWredProfile_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 1, 2),
    _F10QosMaxWredProfile_Type()
)
f10QosMaxWredProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10QosMaxWredProfile.setStatus("current")
_F10QosInterface_ObjectIdentity = ObjectIdentity
f10QosInterface = _F10QosInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 2)
)
_F10QosIfPolicyMapTable_Object = MibTable
f10QosIfPolicyMapTable = _F10QosIfPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    f10QosIfPolicyMapTable.setStatus("current")
_F10QosIfPolicyMapEntry_Object = MibTableRow
f10QosIfPolicyMapEntry = _F10QosIfPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 2, 1, 1)
)
f10QosIfPolicyMapEntry.setIndexNames(
    (0, "FORCE10-QOS-MIB", "f10QosIfPolicyMapIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    f10QosIfPolicyMapEntry.setStatus("current")
_F10QosIfPolicyMapIndex_Type = Integer32
_F10QosIfPolicyMapIndex_Object = MibTableColumn
f10QosIfPolicyMapIndex = _F10QosIfPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 2, 1, 1, 1),
    _F10QosIfPolicyMapIndex_Type()
)
f10QosIfPolicyMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosIfPolicyMapIndex.setStatus("current")
_F10QosIfPolicyMapRowStatus_Type = RowStatus
_F10QosIfPolicyMapRowStatus_Object = MibTableColumn
f10QosIfPolicyMapRowStatus = _F10QosIfPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 2, 1, 1, 2),
    _F10QosIfPolicyMapRowStatus_Type()
)
f10QosIfPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosIfPolicyMapRowStatus.setStatus("current")
_F10QosPolicyMap_ObjectIdentity = ObjectIdentity
f10QosPolicyMap = _F10QosPolicyMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3)
)
_F10QosPolicyMapTable_Object = MibTable
f10QosPolicyMapTable = _F10QosPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    f10QosPolicyMapTable.setStatus("current")
_F10QosPolicyMapEntry_Object = MibTableRow
f10QosPolicyMapEntry = _F10QosPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1, 1)
)
f10QosPolicyMapEntry.setIndexNames(
    (0, "FORCE10-QOS-MIB", "f10QosPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    f10QosPolicyMapEntry.setStatus("current")
_F10QosPolicyMapIndex_Type = Integer32
_F10QosPolicyMapIndex_Object = MibTableColumn
f10QosPolicyMapIndex = _F10QosPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1, 1, 1),
    _F10QosPolicyMapIndex_Type()
)
f10QosPolicyMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapIndex.setStatus("current")
_F10QosPolicyMapName_Type = DisplayString
_F10QosPolicyMapName_Object = MibTableColumn
f10QosPolicyMapName = _F10QosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1, 1, 2),
    _F10QosPolicyMapName_Type()
)
f10QosPolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapName.setStatus("current")
_F10QosPolicyMapDirection_Type = TrafficDirection
_F10QosPolicyMapDirection_Object = MibTableColumn
f10QosPolicyMapDirection = _F10QosPolicyMapDirection_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1, 1, 3),
    _F10QosPolicyMapDirection_Type()
)
f10QosPolicyMapDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapDirection.setStatus("current")


class _F10QosPolicyMapHonoring_Type(PolicyMapHonoringType):
    """Custom type f10QosPolicyMapHonoring based on PolicyMapHonoringType"""
    defaultValue = 1


_F10QosPolicyMapHonoring_Type.__name__ = "PolicyMapHonoringType"
_F10QosPolicyMapHonoring_Object = MibTableColumn
f10QosPolicyMapHonoring = _F10QosPolicyMapHonoring_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1, 1, 4),
    _F10QosPolicyMapHonoring_Type()
)
f10QosPolicyMapHonoring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapHonoring.setStatus("current")


class _F10QosPolicyMapAggPolicyIndex_Type(Integer32):
    """Custom type f10QosPolicyMapAggPolicyIndex based on Integer32"""
    defaultValue = -1


_F10QosPolicyMapAggPolicyIndex_Type.__name__ = "Integer32"
_F10QosPolicyMapAggPolicyIndex_Object = MibTableColumn
f10QosPolicyMapAggPolicyIndex = _F10QosPolicyMapAggPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1, 1, 5),
    _F10QosPolicyMapAggPolicyIndex_Type()
)
f10QosPolicyMapAggPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapAggPolicyIndex.setStatus("current")
_F10QosPolicyMapRowStatus_Type = RowStatus
_F10QosPolicyMapRowStatus_Object = MibTableColumn
f10QosPolicyMapRowStatus = _F10QosPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 1, 1, 6),
    _F10QosPolicyMapRowStatus_Type()
)
f10QosPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapRowStatus.setStatus("current")
_F10QosPolicyMapQueueTable_Object = MibTable
f10QosPolicyMapQueueTable = _F10QosPolicyMapQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    f10QosPolicyMapQueueTable.setStatus("current")
_F10QosPolicyMapQueueEntry_Object = MibTableRow
f10QosPolicyMapQueueEntry = _F10QosPolicyMapQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 2, 1)
)
f10QosPolicyMapQueueEntry.setIndexNames(
    (0, "FORCE10-QOS-MIB", "f10QosPolicyMapIndex"),
    (0, "FORCE10-QOS-MIB", "f10QosPolicyMapQueueId"),
)
if mibBuilder.loadTexts:
    f10QosPolicyMapQueueEntry.setStatus("current")
_F10QosPolicyMapQueueId_Type = F10QueueID
_F10QosPolicyMapQueueId_Object = MibTableColumn
f10QosPolicyMapQueueId = _F10QosPolicyMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 2, 1, 1),
    _F10QosPolicyMapQueueId_Type()
)
f10QosPolicyMapQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapQueueId.setStatus("current")
_F10QosPolicyMapQueueClassMapIndex_Type = Integer32
_F10QosPolicyMapQueueClassMapIndex_Object = MibTableColumn
f10QosPolicyMapQueueClassMapIndex = _F10QosPolicyMapQueueClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 2, 1, 2),
    _F10QosPolicyMapQueueClassMapIndex_Type()
)
f10QosPolicyMapQueueClassMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapQueueClassMapIndex.setStatus("current")
_F10QosPolicyMapQueuePolicyIndex_Type = Integer32
_F10QosPolicyMapQueuePolicyIndex_Object = MibTableColumn
f10QosPolicyMapQueuePolicyIndex = _F10QosPolicyMapQueuePolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 2, 1, 3),
    _F10QosPolicyMapQueuePolicyIndex_Type()
)
f10QosPolicyMapQueuePolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapQueuePolicyIndex.setStatus("current")
_F10QosPolicyMapQueueRowStatus_Type = RowStatus
_F10QosPolicyMapQueueRowStatus_Object = MibTableColumn
f10QosPolicyMapQueueRowStatus = _F10QosPolicyMapQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 3, 2, 1, 4),
    _F10QosPolicyMapQueueRowStatus_Type()
)
f10QosPolicyMapQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyMapQueueRowStatus.setStatus("current")
_F10QosClassMap_ObjectIdentity = ObjectIdentity
f10QosClassMap = _F10QosClassMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 4)
)
_F10QosClassMapTable_Object = MibTable
f10QosClassMapTable = _F10QosClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    f10QosClassMapTable.setStatus("current")
_F10QosClassMapEntry_Object = MibTableRow
f10QosClassMapEntry = _F10QosClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 4, 1, 1)
)
f10QosClassMapEntry.setIndexNames(
    (0, "FORCE10-QOS-MIB", "f10QosClassMapIndex"),
)
if mibBuilder.loadTexts:
    f10QosClassMapEntry.setStatus("current")
_F10QosClassMapIndex_Type = Integer32
_F10QosClassMapIndex_Object = MibTableColumn
f10QosClassMapIndex = _F10QosClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 4, 1, 1, 1),
    _F10QosClassMapIndex_Type()
)
f10QosClassMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosClassMapIndex.setStatus("current")
_F10QosClassMapName_Type = DisplayString
_F10QosClassMapName_Object = MibTableColumn
f10QosClassMapName = _F10QosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 4, 1, 1, 2),
    _F10QosClassMapName_Type()
)
f10QosClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosClassMapName.setStatus("current")
_F10QosClassMapMatch_Type = QosClassMapMatchType
_F10QosClassMapMatch_Object = MibTableColumn
f10QosClassMapMatch = _F10QosClassMapMatch_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 4, 1, 1, 3),
    _F10QosClassMapMatch_Type()
)
f10QosClassMapMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosClassMapMatch.setStatus("current")
_F10QosClassMapRowStatus_Type = RowStatus
_F10QosClassMapRowStatus_Object = MibTableColumn
f10QosClassMapRowStatus = _F10QosClassMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 4, 1, 1, 4),
    _F10QosClassMapRowStatus_Type()
)
f10QosClassMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosClassMapRowStatus.setStatus("current")
_F10QosMatchObject_ObjectIdentity = ObjectIdentity
f10QosMatchObject = _F10QosMatchObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 5)
)
_F10QosMatchObjectTable_Object = MibTable
f10QosMatchObjectTable = _F10QosMatchObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    f10QosMatchObjectTable.setStatus("current")
_F10QosMatchObjectEntry_Object = MibTableRow
f10QosMatchObjectEntry = _F10QosMatchObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 5, 1, 1)
)
f10QosMatchObjectEntry.setIndexNames(
    (0, "FORCE10-QOS-MIB", "f10QosClassMapIndex"),
    (0, "FORCE10-QOS-MIB", "f10QosMatchObjectSequence"),
)
if mibBuilder.loadTexts:
    f10QosMatchObjectEntry.setStatus("current")
_F10QosMatchObjectSequence_Type = Integer32
_F10QosMatchObjectSequence_Object = MibTableColumn
f10QosMatchObjectSequence = _F10QosMatchObjectSequence_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 5, 1, 1, 1),
    _F10QosMatchObjectSequence_Type()
)
f10QosMatchObjectSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10QosMatchObjectSequence.setStatus("current")
_F10QosMatchObjectType_Type = MatchObjectType
_F10QosMatchObjectType_Object = MibTableColumn
f10QosMatchObjectType = _F10QosMatchObjectType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 5, 1, 1, 2),
    _F10QosMatchObjectType_Type()
)
f10QosMatchObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10QosMatchObjectType.setStatus("current")
_F10QosMatchObjectString_Type = DisplayString
_F10QosMatchObjectString_Object = MibTableColumn
f10QosMatchObjectString = _F10QosMatchObjectString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 5, 1, 1, 3),
    _F10QosMatchObjectString_Type()
)
f10QosMatchObjectString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10QosMatchObjectString.setStatus("current")
_F10QosPolicy_ObjectIdentity = ObjectIdentity
f10QosPolicy = _F10QosPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6)
)
_F10QosPolicyTable_Object = MibTable
f10QosPolicyTable = _F10QosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    f10QosPolicyTable.setStatus("current")
_F10QosPolicyEntry_Object = MibTableRow
f10QosPolicyEntry = _F10QosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1)
)
f10QosPolicyEntry.setIndexNames(
    (0, "FORCE10-QOS-MIB", "f10QosPolicyIndex"),
)
if mibBuilder.loadTexts:
    f10QosPolicyEntry.setStatus("current")
_F10QosPolicyIndex_Type = Integer32
_F10QosPolicyIndex_Object = MibTableColumn
f10QosPolicyIndex = _F10QosPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 1),
    _F10QosPolicyIndex_Type()
)
f10QosPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyIndex.setStatus("current")
_F10QosPolicyName_Type = DisplayString
_F10QosPolicyName_Object = MibTableColumn
f10QosPolicyName = _F10QosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 2),
    _F10QosPolicyName_Type()
)
f10QosPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyName.setStatus("current")
_F10QosPolicyDirection_Type = TrafficDirection
_F10QosPolicyDirection_Object = MibTableColumn
f10QosPolicyDirection = _F10QosPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 3),
    _F10QosPolicyDirection_Type()
)
f10QosPolicyDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyDirection.setStatus("current")
_F10QosPolicyInRatePoliceState_Type = QosPolicyState
_F10QosPolicyInRatePoliceState_Object = MibTableColumn
f10QosPolicyInRatePoliceState = _F10QosPolicyInRatePoliceState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 4),
    _F10QosPolicyInRatePoliceState_Type()
)
f10QosPolicyInRatePoliceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInRatePoliceState.setStatus("current")
_F10QosPolicyInRatePoliceCmtRate_Type = Integer32
_F10QosPolicyInRatePoliceCmtRate_Object = MibTableColumn
f10QosPolicyInRatePoliceCmtRate = _F10QosPolicyInRatePoliceCmtRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 5),
    _F10QosPolicyInRatePoliceCmtRate_Type()
)
f10QosPolicyInRatePoliceCmtRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInRatePoliceCmtRate.setStatus("current")
_F10QosPolicyInRatePoliceCmtBurst_Type = Integer32
_F10QosPolicyInRatePoliceCmtBurst_Object = MibTableColumn
f10QosPolicyInRatePoliceCmtBurst = _F10QosPolicyInRatePoliceCmtBurst_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 6),
    _F10QosPolicyInRatePoliceCmtBurst_Type()
)
f10QosPolicyInRatePoliceCmtBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInRatePoliceCmtBurst.setStatus("current")
_F10QosPolicyInRatePolicePeakRate_Type = Integer32
_F10QosPolicyInRatePolicePeakRate_Object = MibTableColumn
f10QosPolicyInRatePolicePeakRate = _F10QosPolicyInRatePolicePeakRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 7),
    _F10QosPolicyInRatePolicePeakRate_Type()
)
f10QosPolicyInRatePolicePeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInRatePolicePeakRate.setStatus("current")
_F10QosPolicyInRatePolicePeakBurst_Type = Integer32
_F10QosPolicyInRatePolicePeakBurst_Object = MibTableColumn
f10QosPolicyInRatePolicePeakBurst = _F10QosPolicyInRatePolicePeakBurst_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 8),
    _F10QosPolicyInRatePolicePeakBurst_Type()
)
f10QosPolicyInRatePolicePeakBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInRatePolicePeakBurst.setStatus("current")
_F10QosPolicyInMarkIpDscp_Type = Integer32
_F10QosPolicyInMarkIpDscp_Object = MibTableColumn
f10QosPolicyInMarkIpDscp = _F10QosPolicyInMarkIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 9),
    _F10QosPolicyInMarkIpDscp_Type()
)
f10QosPolicyInMarkIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInMarkIpDscp.setStatus("current")
_F10QosPolicyInMarkDot1p_Type = Integer32
_F10QosPolicyInMarkDot1p_Object = MibTableColumn
f10QosPolicyInMarkDot1p = _F10QosPolicyInMarkDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 10),
    _F10QosPolicyInMarkDot1p_Type()
)
f10QosPolicyInMarkDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInMarkDot1p.setStatus("current")
_F10QosPolicyInMarkMplsExp_Type = Integer32
_F10QosPolicyInMarkMplsExp_Object = MibTableColumn
f10QosPolicyInMarkMplsExp = _F10QosPolicyInMarkMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 11),
    _F10QosPolicyInMarkMplsExp_Type()
)
f10QosPolicyInMarkMplsExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyInMarkMplsExp.setStatus("current")
_F10QosPolicyOutRateLimitState_Type = QosPolicyState
_F10QosPolicyOutRateLimitState_Object = MibTableColumn
f10QosPolicyOutRateLimitState = _F10QosPolicyOutRateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 12),
    _F10QosPolicyOutRateLimitState_Type()
)
f10QosPolicyOutRateLimitState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateLimitState.setStatus("current")
_F10QosPolicyOutRateLimitCmtRate_Type = Integer32
_F10QosPolicyOutRateLimitCmtRate_Object = MibTableColumn
f10QosPolicyOutRateLimitCmtRate = _F10QosPolicyOutRateLimitCmtRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 13),
    _F10QosPolicyOutRateLimitCmtRate_Type()
)
f10QosPolicyOutRateLimitCmtRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateLimitCmtRate.setStatus("current")
_F10QosPolicyOutRateLimitCmtBurst_Type = Integer32
_F10QosPolicyOutRateLimitCmtBurst_Object = MibTableColumn
f10QosPolicyOutRateLimitCmtBurst = _F10QosPolicyOutRateLimitCmtBurst_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 14),
    _F10QosPolicyOutRateLimitCmtBurst_Type()
)
f10QosPolicyOutRateLimitCmtBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateLimitCmtBurst.setStatus("current")
_F10QosPolicyOutRateLimitPeakRate_Type = Integer32
_F10QosPolicyOutRateLimitPeakRate_Object = MibTableColumn
f10QosPolicyOutRateLimitPeakRate = _F10QosPolicyOutRateLimitPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 15),
    _F10QosPolicyOutRateLimitPeakRate_Type()
)
f10QosPolicyOutRateLimitPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateLimitPeakRate.setStatus("current")
_F10QosPolicyOutRateLimitPeakBurst_Type = Integer32
_F10QosPolicyOutRateLimitPeakBurst_Object = MibTableColumn
f10QosPolicyOutRateLimitPeakBurst = _F10QosPolicyOutRateLimitPeakBurst_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 16),
    _F10QosPolicyOutRateLimitPeakBurst_Type()
)
f10QosPolicyOutRateLimitPeakBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateLimitPeakBurst.setStatus("current")
_F10QosPolicyOutRateShapeState_Type = QosPolicyState
_F10QosPolicyOutRateShapeState_Object = MibTableColumn
f10QosPolicyOutRateShapeState = _F10QosPolicyOutRateShapeState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 17),
    _F10QosPolicyOutRateShapeState_Type()
)
f10QosPolicyOutRateShapeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateShapeState.setStatus("current")
_F10QosPolicyOutRateShapeCmtRate_Type = Integer32
_F10QosPolicyOutRateShapeCmtRate_Object = MibTableColumn
f10QosPolicyOutRateShapeCmtRate = _F10QosPolicyOutRateShapeCmtRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 18),
    _F10QosPolicyOutRateShapeCmtRate_Type()
)
f10QosPolicyOutRateShapeCmtRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateShapeCmtRate.setStatus("current")
_F10QosPolicyOutRateShapeCmtBurst_Type = Integer32
_F10QosPolicyOutRateShapeCmtBurst_Object = MibTableColumn
f10QosPolicyOutRateShapeCmtBurst = _F10QosPolicyOutRateShapeCmtBurst_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 19),
    _F10QosPolicyOutRateShapeCmtBurst_Type()
)
f10QosPolicyOutRateShapeCmtBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutRateShapeCmtBurst.setStatus("current")


class _F10QosPolicyOutBandwidth_Type(Integer32):
    """Custom type f10QosPolicyOutBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_F10QosPolicyOutBandwidth_Type.__name__ = "Integer32"
_F10QosPolicyOutBandwidth_Object = MibTableColumn
f10QosPolicyOutBandwidth = _F10QosPolicyOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 20),
    _F10QosPolicyOutBandwidth_Type()
)
f10QosPolicyOutBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutBandwidth.setStatus("current")
_F10QosPolicyOutWredIndex_Type = Integer32
_F10QosPolicyOutWredIndex_Object = MibTableColumn
f10QosPolicyOutWredIndex = _F10QosPolicyOutWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 21),
    _F10QosPolicyOutWredIndex_Type()
)
f10QosPolicyOutWredIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyOutWredIndex.setStatus("current")
_F10QosPolicyRowStatus_Type = RowStatus
_F10QosPolicyRowStatus_Object = MibTableColumn
f10QosPolicyRowStatus = _F10QosPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 1, 1, 22),
    _F10QosPolicyRowStatus_Type()
)
f10QosPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosPolicyRowStatus.setStatus("current")
_F10QosWredProfileTable_Object = MibTable
f10QosWredProfileTable = _F10QosWredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    f10QosWredProfileTable.setStatus("current")
_F10QosWredProfileEntry_Object = MibTableRow
f10QosWredProfileEntry = _F10QosWredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2, 1)
)
f10QosWredProfileEntry.setIndexNames(
    (0, "FORCE10-QOS-MIB", "f10QosWredIndex"),
)
if mibBuilder.loadTexts:
    f10QosWredProfileEntry.setStatus("current")
_F10QosWredIndex_Type = Integer32
_F10QosWredIndex_Object = MibTableColumn
f10QosWredIndex = _F10QosWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2, 1, 1),
    _F10QosWredIndex_Type()
)
f10QosWredIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosWredIndex.setStatus("current")
_F10QosWredName_Type = DisplayString
_F10QosWredName_Object = MibTableColumn
f10QosWredName = _F10QosWredName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2, 1, 2),
    _F10QosWredName_Type()
)
f10QosWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosWredName.setStatus("current")


class _F10QosWredType_Type(Integer32):
    """Custom type f10QosWredType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linear", 1),
          ("exponential", 2))
    )


_F10QosWredType_Type.__name__ = "Integer32"
_F10QosWredType_Object = MibTableColumn
f10QosWredType = _F10QosWredType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2, 1, 3),
    _F10QosWredType_Type()
)
f10QosWredType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosWredType.setStatus("current")
_F10QosWredThresholdLow_Type = Integer32
_F10QosWredThresholdLow_Object = MibTableColumn
f10QosWredThresholdLow = _F10QosWredThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2, 1, 4),
    _F10QosWredThresholdLow_Type()
)
f10QosWredThresholdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10QosWredThresholdLow.setStatus("current")
_F10QosWredThresholdHigh_Type = Integer32
_F10QosWredThresholdHigh_Object = MibTableColumn
f10QosWredThresholdHigh = _F10QosWredThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2, 1, 5),
    _F10QosWredThresholdHigh_Type()
)
f10QosWredThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10QosWredThresholdHigh.setStatus("current")
_F10QosWredRowStatus_Type = RowStatus
_F10QosWredRowStatus_Object = MibTableColumn
f10QosWredRowStatus = _F10QosWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 6, 2, 1, 6),
    _F10QosWredRowStatus_Type()
)
f10QosWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10QosWredRowStatus.setStatus("current")
_F10QosNotification_ObjectIdentity = ObjectIdentity
f10QosNotification = _F10QosNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 7)
)
_F10QosAlarm_ObjectIdentity = ObjectIdentity
f10QosAlarm = _F10QosAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 7, 0)
)
_F10QosAlarmData_ObjectIdentity = ObjectIdentity
f10QosAlarmData = _F10QosAlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 7, 1)
)
_F10QosAlarmDescription_Type = DisplayString
_F10QosAlarmDescription_Object = MibScalar
f10QosAlarmDescription = _F10QosAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 7, 1, 1),
    _F10QosAlarmDescription_Type()
)
f10QosAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    f10QosAlarmDescription.setStatus("current")

# Managed Objects groups


# Notification objects

f10QosAlarmGeneric = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 4, 7, 0, 1)
)
f10QosAlarmGeneric.setObjects(
    ("FORCE10-QOS-MIB", "f10QosAlarmDescription")
)
if mibBuilder.loadTexts:
    f10QosAlarmGeneric.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-QOS-MIB",
    **{"TrafficDirection": TrafficDirection,
       "QosClassMapMatchType": QosClassMapMatchType,
       "PolicyMapHonoringType": PolicyMapHonoringType,
       "MatchObjectType": MatchObjectType,
       "QosPolicyState": QosPolicyState,
       "f10QosMib": f10QosMib,
       "f10QosGroup": f10QosGroup,
       "f10QosMibVersion": f10QosMibVersion,
       "f10QosMaxWredProfile": f10QosMaxWredProfile,
       "f10QosInterface": f10QosInterface,
       "f10QosIfPolicyMapTable": f10QosIfPolicyMapTable,
       "f10QosIfPolicyMapEntry": f10QosIfPolicyMapEntry,
       "f10QosIfPolicyMapIndex": f10QosIfPolicyMapIndex,
       "f10QosIfPolicyMapRowStatus": f10QosIfPolicyMapRowStatus,
       "f10QosPolicyMap": f10QosPolicyMap,
       "f10QosPolicyMapTable": f10QosPolicyMapTable,
       "f10QosPolicyMapEntry": f10QosPolicyMapEntry,
       "f10QosPolicyMapIndex": f10QosPolicyMapIndex,
       "f10QosPolicyMapName": f10QosPolicyMapName,
       "f10QosPolicyMapDirection": f10QosPolicyMapDirection,
       "f10QosPolicyMapHonoring": f10QosPolicyMapHonoring,
       "f10QosPolicyMapAggPolicyIndex": f10QosPolicyMapAggPolicyIndex,
       "f10QosPolicyMapRowStatus": f10QosPolicyMapRowStatus,
       "f10QosPolicyMapQueueTable": f10QosPolicyMapQueueTable,
       "f10QosPolicyMapQueueEntry": f10QosPolicyMapQueueEntry,
       "f10QosPolicyMapQueueId": f10QosPolicyMapQueueId,
       "f10QosPolicyMapQueueClassMapIndex": f10QosPolicyMapQueueClassMapIndex,
       "f10QosPolicyMapQueuePolicyIndex": f10QosPolicyMapQueuePolicyIndex,
       "f10QosPolicyMapQueueRowStatus": f10QosPolicyMapQueueRowStatus,
       "f10QosClassMap": f10QosClassMap,
       "f10QosClassMapTable": f10QosClassMapTable,
       "f10QosClassMapEntry": f10QosClassMapEntry,
       "f10QosClassMapIndex": f10QosClassMapIndex,
       "f10QosClassMapName": f10QosClassMapName,
       "f10QosClassMapMatch": f10QosClassMapMatch,
       "f10QosClassMapRowStatus": f10QosClassMapRowStatus,
       "f10QosMatchObject": f10QosMatchObject,
       "f10QosMatchObjectTable": f10QosMatchObjectTable,
       "f10QosMatchObjectEntry": f10QosMatchObjectEntry,
       "f10QosMatchObjectSequence": f10QosMatchObjectSequence,
       "f10QosMatchObjectType": f10QosMatchObjectType,
       "f10QosMatchObjectString": f10QosMatchObjectString,
       "f10QosPolicy": f10QosPolicy,
       "f10QosPolicyTable": f10QosPolicyTable,
       "f10QosPolicyEntry": f10QosPolicyEntry,
       "f10QosPolicyIndex": f10QosPolicyIndex,
       "f10QosPolicyName": f10QosPolicyName,
       "f10QosPolicyDirection": f10QosPolicyDirection,
       "f10QosPolicyInRatePoliceState": f10QosPolicyInRatePoliceState,
       "f10QosPolicyInRatePoliceCmtRate": f10QosPolicyInRatePoliceCmtRate,
       "f10QosPolicyInRatePoliceCmtBurst": f10QosPolicyInRatePoliceCmtBurst,
       "f10QosPolicyInRatePolicePeakRate": f10QosPolicyInRatePolicePeakRate,
       "f10QosPolicyInRatePolicePeakBurst": f10QosPolicyInRatePolicePeakBurst,
       "f10QosPolicyInMarkIpDscp": f10QosPolicyInMarkIpDscp,
       "f10QosPolicyInMarkDot1p": f10QosPolicyInMarkDot1p,
       "f10QosPolicyInMarkMplsExp": f10QosPolicyInMarkMplsExp,
       "f10QosPolicyOutRateLimitState": f10QosPolicyOutRateLimitState,
       "f10QosPolicyOutRateLimitCmtRate": f10QosPolicyOutRateLimitCmtRate,
       "f10QosPolicyOutRateLimitCmtBurst": f10QosPolicyOutRateLimitCmtBurst,
       "f10QosPolicyOutRateLimitPeakRate": f10QosPolicyOutRateLimitPeakRate,
       "f10QosPolicyOutRateLimitPeakBurst": f10QosPolicyOutRateLimitPeakBurst,
       "f10QosPolicyOutRateShapeState": f10QosPolicyOutRateShapeState,
       "f10QosPolicyOutRateShapeCmtRate": f10QosPolicyOutRateShapeCmtRate,
       "f10QosPolicyOutRateShapeCmtBurst": f10QosPolicyOutRateShapeCmtBurst,
       "f10QosPolicyOutBandwidth": f10QosPolicyOutBandwidth,
       "f10QosPolicyOutWredIndex": f10QosPolicyOutWredIndex,
       "f10QosPolicyRowStatus": f10QosPolicyRowStatus,
       "f10QosWredProfileTable": f10QosWredProfileTable,
       "f10QosWredProfileEntry": f10QosWredProfileEntry,
       "f10QosWredIndex": f10QosWredIndex,
       "f10QosWredName": f10QosWredName,
       "f10QosWredType": f10QosWredType,
       "f10QosWredThresholdLow": f10QosWredThresholdLow,
       "f10QosWredThresholdHigh": f10QosWredThresholdHigh,
       "f10QosWredRowStatus": f10QosWredRowStatus,
       "f10QosNotification": f10QosNotification,
       "f10QosAlarm": f10QosAlarm,
       "f10QosAlarmGeneric": f10QosAlarmGeneric,
       "f10QosAlarmData": f10QosAlarmData,
       "f10QosAlarmDescription": f10QosAlarmDescription}
)
