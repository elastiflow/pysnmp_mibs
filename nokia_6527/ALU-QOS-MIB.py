# SNMP MIB module (ALU-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-QOS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:25 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARObjs")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(tNetworkQueueEntry,
 tSapEgressEntry,
 tSapEgressQueueEntry,
 tSapIngressQueueEntry) = mibBuilder.importSymbols(
    "TIMETRA-QOS-MIB",
    "tNetworkQueueEntry",
    "tSapEgressEntry",
    "tSapEgressQueueEntry",
    "tSapIngressQueueEntry")

(TItemDescription,
 TNamedItem,
 TPolicyID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TPolicyID")


# MODULE-IDENTITY

aluQOSMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    aluQOSMIBModule.setRevisions(
        ("1908-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluFabricProfilePolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



class AluFabricProfileMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 1),
          ("destination", 2))
    )



class AluFabricProfileDestMdaRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )



class AluSystemAggregateRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500000),
    )



# MIB Managed Objects in the order of their OIDs

_AluQOSConformance_ObjectIdentity = ObjectIdentity
aluQOSConformance = _AluQOSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5)
)
_AluQOSCompliances_ObjectIdentity = ObjectIdentity
aluQOSCompliances = _AluQOSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1)
)
_AluQOSComp7705_ObjectIdentity = ObjectIdentity
aluQOSComp7705 = _AluQOSComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1)
)
_AluQOSGroups_ObjectIdentity = ObjectIdentity
aluQOSGroups = _AluQOSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2)
)
_AluQOSObjs_ObjectIdentity = ObjectIdentity
aluQOSObjs = _AluQOSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5)
)
_AluSapIngressQueueExtensionTable_Object = MibTable
aluSapIngressQueueExtensionTable = _AluSapIngressQueueExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    aluSapIngressQueueExtensionTable.setStatus("current")
_AluSapIngressQueueExtensionEntry_Object = MibTableRow
aluSapIngressQueueExtensionEntry = _AluSapIngressQueueExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    aluSapIngressQueueExtensionEntry.setStatus("current")


class _AluSapIngressQueueSlopePolicy_Type(TNamedItem):
    """Custom type aluSapIngressQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_AluSapIngressQueueSlopePolicy_Type.__name__ = "TNamedItem"
_AluSapIngressQueueSlopePolicy_Object = MibTableColumn
aluSapIngressQueueSlopePolicy = _AluSapIngressQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 1, 1, 1),
    _AluSapIngressQueueSlopePolicy_Type()
)
aluSapIngressQueueSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressQueueSlopePolicy.setStatus("current")
_AluSapEgressQueueExtensionTable_Object = MibTable
aluSapEgressQueueExtensionTable = _AluSapEgressQueueExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    aluSapEgressQueueExtensionTable.setStatus("current")
_AluSapEgressQueueExtensionEntry_Object = MibTableRow
aluSapEgressQueueExtensionEntry = _AluSapEgressQueueExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    aluSapEgressQueueExtensionEntry.setStatus("current")


class _AluSapEgressQueueSlopePolicy_Type(TNamedItem):
    """Custom type aluSapEgressQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_AluSapEgressQueueSlopePolicy_Type.__name__ = "TNamedItem"
_AluSapEgressQueueSlopePolicy_Object = MibTableColumn
aluSapEgressQueueSlopePolicy = _AluSapEgressQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 2, 1, 1),
    _AluSapEgressQueueSlopePolicy_Type()
)
aluSapEgressQueueSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressQueueSlopePolicy.setStatus("current")
_AluNetworkQueueExtensionTable_Object = MibTable
aluNetworkQueueExtensionTable = _AluNetworkQueueExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    aluNetworkQueueExtensionTable.setStatus("current")
_AluNetworkQueueExtensionEntry_Object = MibTableRow
aluNetworkQueueExtensionEntry = _AluNetworkQueueExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    aluNetworkQueueExtensionEntry.setStatus("current")


class _AluNetworkQueueSlopePolicy_Type(TNamedItem):
    """Custom type aluNetworkQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_AluNetworkQueueSlopePolicy_Type.__name__ = "TNamedItem"
_AluNetworkQueueSlopePolicy_Object = MibTableColumn
aluNetworkQueueSlopePolicy = _AluNetworkQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 3, 1, 1),
    _AluNetworkQueueSlopePolicy_Type()
)
aluNetworkQueueSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluNetworkQueueSlopePolicy.setStatus("current")
_AluFabricProfileTable_Object = MibTable
aluFabricProfileTable = _AluFabricProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    aluFabricProfileTable.setStatus("current")
_AluFabricProfileEntry_Object = MibTableRow
aluFabricProfileEntry = _AluFabricProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1)
)
aluFabricProfileEntry.setIndexNames(
    (0, "ALU-QOS-MIB", "aluFabricProfileIndex"),
)
if mibBuilder.loadTexts:
    aluFabricProfileEntry.setStatus("current")


class _AluFabricProfileIndex_Type(AluFabricProfilePolicyID):
    """Custom type aluFabricProfileIndex based on AluFabricProfilePolicyID"""
    subtypeSpec = AluFabricProfilePolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AluFabricProfileIndex_Type.__name__ = "AluFabricProfilePolicyID"
_AluFabricProfileIndex_Object = MibTableColumn
aluFabricProfileIndex = _AluFabricProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 1),
    _AluFabricProfileIndex_Type()
)
aluFabricProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluFabricProfileIndex.setStatus("current")
_AluFabricProfileRowStatus_Type = RowStatus
_AluFabricProfileRowStatus_Object = MibTableColumn
aluFabricProfileRowStatus = _AluFabricProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 2),
    _AluFabricProfileRowStatus_Type()
)
aluFabricProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRowStatus.setStatus("current")
_AluFabricProfileDescription_Type = TItemDescription
_AluFabricProfileDescription_Object = MibTableColumn
aluFabricProfileDescription = _AluFabricProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 3),
    _AluFabricProfileDescription_Type()
)
aluFabricProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileDescription.setStatus("current")


class _AluFabricProfileRateToMdaIndex1_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex1 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex1_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex1_Object = MibTableColumn
aluFabricProfileRateToMdaIndex1 = _AluFabricProfileRateToMdaIndex1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 4),
    _AluFabricProfileRateToMdaIndex1_Type()
)
aluFabricProfileRateToMdaIndex1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex1.setStatus("current")


class _AluFabricProfileRateToMdaIndex2_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex2 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex2_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex2_Object = MibTableColumn
aluFabricProfileRateToMdaIndex2 = _AluFabricProfileRateToMdaIndex2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 5),
    _AluFabricProfileRateToMdaIndex2_Type()
)
aluFabricProfileRateToMdaIndex2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex2.setStatus("current")


class _AluFabricProfileRateToMdaIndex3_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex3 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex3_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex3_Object = MibTableColumn
aluFabricProfileRateToMdaIndex3 = _AluFabricProfileRateToMdaIndex3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 6),
    _AluFabricProfileRateToMdaIndex3_Type()
)
aluFabricProfileRateToMdaIndex3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex3.setStatus("current")


class _AluFabricProfileRateToMdaIndex4_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex4 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex4_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex4_Object = MibTableColumn
aluFabricProfileRateToMdaIndex4 = _AluFabricProfileRateToMdaIndex4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 7),
    _AluFabricProfileRateToMdaIndex4_Type()
)
aluFabricProfileRateToMdaIndex4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex4.setStatus("current")


class _AluFabricProfileRateToMdaIndex5_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex5 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex5_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex5_Object = MibTableColumn
aluFabricProfileRateToMdaIndex5 = _AluFabricProfileRateToMdaIndex5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 8),
    _AluFabricProfileRateToMdaIndex5_Type()
)
aluFabricProfileRateToMdaIndex5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex5.setStatus("current")


class _AluFabricProfileRateToMdaIndex6_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex6 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex6_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex6_Object = MibTableColumn
aluFabricProfileRateToMdaIndex6 = _AluFabricProfileRateToMdaIndex6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 9),
    _AluFabricProfileRateToMdaIndex6_Type()
)
aluFabricProfileRateToMdaIndex6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex6.setStatus("current")


class _AluFabricProfileRateToMdaIndex7_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex7 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex7_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex7_Object = MibTableColumn
aluFabricProfileRateToMdaIndex7 = _AluFabricProfileRateToMdaIndex7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 10),
    _AluFabricProfileRateToMdaIndex7_Type()
)
aluFabricProfileRateToMdaIndex7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex7.setStatus("current")


class _AluFabricProfileRateToMdaIndex8_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex8 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex8_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex8_Object = MibTableColumn
aluFabricProfileRateToMdaIndex8 = _AluFabricProfileRateToMdaIndex8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 11),
    _AluFabricProfileRateToMdaIndex8_Type()
)
aluFabricProfileRateToMdaIndex8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex8.setStatus("current")


class _AluFabricProfileRateToMdaIndex9_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex9 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex9_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex9_Object = MibTableColumn
aluFabricProfileRateToMdaIndex9 = _AluFabricProfileRateToMdaIndex9_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 12),
    _AluFabricProfileRateToMdaIndex9_Type()
)
aluFabricProfileRateToMdaIndex9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex9.setStatus("current")


class _AluFabricProfileRateToMdaIndex10_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex10 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex10_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex10_Object = MibTableColumn
aluFabricProfileRateToMdaIndex10 = _AluFabricProfileRateToMdaIndex10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 13),
    _AluFabricProfileRateToMdaIndex10_Type()
)
aluFabricProfileRateToMdaIndex10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex10.setStatus("current")


class _AluFabricProfileRateToMdaIndex11_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex11 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex11_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex11_Object = MibTableColumn
aluFabricProfileRateToMdaIndex11 = _AluFabricProfileRateToMdaIndex11_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 14),
    _AluFabricProfileRateToMdaIndex11_Type()
)
aluFabricProfileRateToMdaIndex11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex11.setStatus("current")


class _AluFabricProfileRateToMdaIndex12_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex12 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex12_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex12_Object = MibTableColumn
aluFabricProfileRateToMdaIndex12 = _AluFabricProfileRateToMdaIndex12_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 15),
    _AluFabricProfileRateToMdaIndex12_Type()
)
aluFabricProfileRateToMdaIndex12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex12.setStatus("current")


class _AluFabricProfileRateToMdaIndex13_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex13 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex13_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex13_Object = MibTableColumn
aluFabricProfileRateToMdaIndex13 = _AluFabricProfileRateToMdaIndex13_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 16),
    _AluFabricProfileRateToMdaIndex13_Type()
)
aluFabricProfileRateToMdaIndex13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex13.setStatus("current")


class _AluFabricProfileRateToMdaIndex14_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex14 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex14_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex14_Object = MibTableColumn
aluFabricProfileRateToMdaIndex14 = _AluFabricProfileRateToMdaIndex14_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 17),
    _AluFabricProfileRateToMdaIndex14_Type()
)
aluFabricProfileRateToMdaIndex14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex14.setStatus("current")


class _AluFabricProfileRateToMdaIndex15_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex15 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex15_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex15_Object = MibTableColumn
aluFabricProfileRateToMdaIndex15 = _AluFabricProfileRateToMdaIndex15_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 18),
    _AluFabricProfileRateToMdaIndex15_Type()
)
aluFabricProfileRateToMdaIndex15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex15.setStatus("current")


class _AluFabricProfileRateToMdaIndex16_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex16 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex16_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex16_Object = MibTableColumn
aluFabricProfileRateToMdaIndex16 = _AluFabricProfileRateToMdaIndex16_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 19),
    _AluFabricProfileRateToMdaIndex16_Type()
)
aluFabricProfileRateToMdaIndex16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex16.setStatus("current")


class _AluFabricProfileRateToMdaIndex17_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex17 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex17_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex17_Object = MibTableColumn
aluFabricProfileRateToMdaIndex17 = _AluFabricProfileRateToMdaIndex17_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 20),
    _AluFabricProfileRateToMdaIndex17_Type()
)
aluFabricProfileRateToMdaIndex17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex17.setStatus("current")


class _AluFabricProfileRateToMdaIndex18_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex18 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex18_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex18_Object = MibTableColumn
aluFabricProfileRateToMdaIndex18 = _AluFabricProfileRateToMdaIndex18_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 21),
    _AluFabricProfileRateToMdaIndex18_Type()
)
aluFabricProfileRateToMdaIndex18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex18.setStatus("current")


class _AluFabricProfileRateToMdaIndex19_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex19 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex19_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex19_Object = MibTableColumn
aluFabricProfileRateToMdaIndex19 = _AluFabricProfileRateToMdaIndex19_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 22),
    _AluFabricProfileRateToMdaIndex19_Type()
)
aluFabricProfileRateToMdaIndex19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex19.setStatus("current")


class _AluFabricProfileRateToMdaIndex20_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex20 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex20_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex20_Object = MibTableColumn
aluFabricProfileRateToMdaIndex20 = _AluFabricProfileRateToMdaIndex20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 23),
    _AluFabricProfileRateToMdaIndex20_Type()
)
aluFabricProfileRateToMdaIndex20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex20.setStatus("current")


class _AluFabricProfileRateToMdaIndex21_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex21 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex21_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex21_Object = MibTableColumn
aluFabricProfileRateToMdaIndex21 = _AluFabricProfileRateToMdaIndex21_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 24),
    _AluFabricProfileRateToMdaIndex21_Type()
)
aluFabricProfileRateToMdaIndex21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex21.setStatus("current")


class _AluFabricProfileRateToMdaIndex22_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex22 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex22_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex22_Object = MibTableColumn
aluFabricProfileRateToMdaIndex22 = _AluFabricProfileRateToMdaIndex22_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 25),
    _AluFabricProfileRateToMdaIndex22_Type()
)
aluFabricProfileRateToMdaIndex22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex22.setStatus("current")


class _AluFabricProfileRateToMdaIndex23_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex23 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex23_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex23_Object = MibTableColumn
aluFabricProfileRateToMdaIndex23 = _AluFabricProfileRateToMdaIndex23_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 26),
    _AluFabricProfileRateToMdaIndex23_Type()
)
aluFabricProfileRateToMdaIndex23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex23.setStatus("current")


class _AluFabricProfileRateToMdaIndex24_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex24 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex24_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex24_Object = MibTableColumn
aluFabricProfileRateToMdaIndex24 = _AluFabricProfileRateToMdaIndex24_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 27),
    _AluFabricProfileRateToMdaIndex24_Type()
)
aluFabricProfileRateToMdaIndex24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex24.setStatus("current")


class _AluFabricProfileRateToMdaIndex25_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex25 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex25_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex25_Object = MibTableColumn
aluFabricProfileRateToMdaIndex25 = _AluFabricProfileRateToMdaIndex25_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 28),
    _AluFabricProfileRateToMdaIndex25_Type()
)
aluFabricProfileRateToMdaIndex25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex25.setStatus("current")


class _AluFabricProfileRateToMdaIndex26_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex26 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex26_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex26_Object = MibTableColumn
aluFabricProfileRateToMdaIndex26 = _AluFabricProfileRateToMdaIndex26_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 29),
    _AluFabricProfileRateToMdaIndex26_Type()
)
aluFabricProfileRateToMdaIndex26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex26.setStatus("current")


class _AluFabricProfileRateToMdaIndex27_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex27 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex27_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex27_Object = MibTableColumn
aluFabricProfileRateToMdaIndex27 = _AluFabricProfileRateToMdaIndex27_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 30),
    _AluFabricProfileRateToMdaIndex27_Type()
)
aluFabricProfileRateToMdaIndex27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex27.setStatus("current")


class _AluFabricProfileRateToMdaIndex28_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex28 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex28_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex28_Object = MibTableColumn
aluFabricProfileRateToMdaIndex28 = _AluFabricProfileRateToMdaIndex28_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 31),
    _AluFabricProfileRateToMdaIndex28_Type()
)
aluFabricProfileRateToMdaIndex28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex28.setStatus("current")


class _AluFabricProfileRateToMdaIndex29_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex29 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex29_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex29_Object = MibTableColumn
aluFabricProfileRateToMdaIndex29 = _AluFabricProfileRateToMdaIndex29_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 32),
    _AluFabricProfileRateToMdaIndex29_Type()
)
aluFabricProfileRateToMdaIndex29.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex29.setStatus("current")


class _AluFabricProfileRateToMdaIndex30_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex30 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex30_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex30_Object = MibTableColumn
aluFabricProfileRateToMdaIndex30 = _AluFabricProfileRateToMdaIndex30_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 33),
    _AluFabricProfileRateToMdaIndex30_Type()
)
aluFabricProfileRateToMdaIndex30.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex30.setStatus("current")


class _AluFabricProfileRateToMdaIndex31_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex31 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex31_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex31_Object = MibTableColumn
aluFabricProfileRateToMdaIndex31 = _AluFabricProfileRateToMdaIndex31_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 34),
    _AluFabricProfileRateToMdaIndex31_Type()
)
aluFabricProfileRateToMdaIndex31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex31.setStatus("current")


class _AluFabricProfileRateToMdaIndex32_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileRateToMdaIndex32 based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileRateToMdaIndex32_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileRateToMdaIndex32_Object = MibTableColumn
aluFabricProfileRateToMdaIndex32 = _AluFabricProfileRateToMdaIndex32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 35),
    _AluFabricProfileRateToMdaIndex32_Type()
)
aluFabricProfileRateToMdaIndex32.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileRateToMdaIndex32.setStatus("current")
_AluFabricProfileLastChanged_Type = TimeStamp
_AluFabricProfileLastChanged_Object = MibTableColumn
aluFabricProfileLastChanged = _AluFabricProfileLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 36),
    _AluFabricProfileLastChanged_Type()
)
aluFabricProfileLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricProfileLastChanged.setStatus("current")


class _AluFabricProfileMode_Type(AluFabricProfileMode):
    """Custom type aluFabricProfileMode based on AluFabricProfileMode"""
    defaultValue = 1


_AluFabricProfileMode_Type.__name__ = "AluFabricProfileMode"
_AluFabricProfileMode_Object = MibTableColumn
aluFabricProfileMode = _AluFabricProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 37),
    _AluFabricProfileMode_Type()
)
aluFabricProfileMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileMode.setStatus("current")


class _AluFabricProfileAggregateRate_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileAggregateRate based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileAggregateRate_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileAggregateRate_Object = MibTableColumn
aluFabricProfileAggregateRate = _AluFabricProfileAggregateRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 38),
    _AluFabricProfileAggregateRate_Type()
)
aluFabricProfileAggregateRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileAggregateRate.setStatus("current")


class _AluFabricProfileMultipointRate_Type(AluFabricProfileDestMdaRate):
    """Custom type aluFabricProfileMultipointRate based on AluFabricProfileDestMdaRate"""
    defaultValue = 200000


_AluFabricProfileMultipointRate_Type.__name__ = "AluFabricProfileDestMdaRate"
_AluFabricProfileMultipointRate_Object = MibTableColumn
aluFabricProfileMultipointRate = _AluFabricProfileMultipointRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 4, 1, 39),
    _AluFabricProfileMultipointRate_Type()
)
aluFabricProfileMultipointRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluFabricProfileMultipointRate.setStatus("current")
_AluExtTSapEgressTable_Object = MibTable
aluExtTSapEgressTable = _AluExtTSapEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 5)
)
if mibBuilder.loadTexts:
    aluExtTSapEgressTable.setStatus("current")
_AluExtTSapEgressEntry_Object = MibTableRow
aluExtTSapEgressEntry = _AluExtTSapEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    aluExtTSapEgressEntry.setStatus("current")


class _AluSapEgressPolicyType_Type(Integer32):
    """Custom type aluSapEgressPolicyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("standard", 2),
          ("mc-mlppp", 3))
    )


_AluSapEgressPolicyType_Type.__name__ = "Integer32"
_AluSapEgressPolicyType_Object = MibTableColumn
aluSapEgressPolicyType = _AluSapEgressPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 5, 1, 1),
    _AluSapEgressPolicyType_Type()
)
aluSapEgressPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressPolicyType.setStatus("current")
_AluSystemQosConfig_ObjectIdentity = ObjectIdentity
aluSystemQosConfig = _AluSystemQosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6)
)


class _AluSystemAccessIngAggRate_Type(AluSystemAggregateRate):
    """Custom type aluSystemAccessIngAggRate based on AluSystemAggregateRate"""
    defaultValue = 0


_AluSystemAccessIngAggRate_Type.__name__ = "AluSystemAggregateRate"
_AluSystemAccessIngAggRate_Object = MibScalar
aluSystemAccessIngAggRate = _AluSystemAccessIngAggRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6, 1),
    _AluSystemAccessIngAggRate_Type()
)
aluSystemAccessIngAggRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSystemAccessIngAggRate.setStatus("current")


class _AluSystemNetworkIngAggRate_Type(AluSystemAggregateRate):
    """Custom type aluSystemNetworkIngAggRate based on AluSystemAggregateRate"""
    defaultValue = 0


_AluSystemNetworkIngAggRate_Type.__name__ = "AluSystemAggregateRate"
_AluSystemNetworkIngAggRate_Object = MibScalar
aluSystemNetworkIngAggRate = _AluSystemNetworkIngAggRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6, 2),
    _AluSystemNetworkIngAggRate_Type()
)
aluSystemNetworkIngAggRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSystemNetworkIngAggRate.setStatus("current")
_AluSystemQosLastChanged_Type = TimeStamp
_AluSystemQosLastChanged_Object = MibScalar
aluSystemQosLastChanged = _AluSystemQosLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 5, 6, 3),
    _AluSystemQosLastChanged_Type()
)
aluSystemQosLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSystemQosLastChanged.setStatus("current")
tSapIngressQueueEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluSapIngressQueueExtensionEntry")
)
aluSapIngressQueueExtensionEntry.setIndexNames(*tSapIngressQueueEntry.getIndexNames())
tSapEgressQueueEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluSapEgressQueueExtensionEntry")
)
aluSapEgressQueueExtensionEntry.setIndexNames(*tSapEgressQueueEntry.getIndexNames())
tNetworkQueueEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluNetworkQueueExtensionEntry")
)
aluNetworkQueueExtensionEntry.setIndexNames(*tNetworkQueueEntry.getIndexNames())
tSapEgressEntry.registerAugmentions(
    ("ALU-QOS-MIB",
     "aluExtTSapEgressEntry")
)
aluExtTSapEgressEntry.setIndexNames(*tSapEgressEntry.getIndexNames())

# Managed Objects groups

aluQosQueuePolicySlopePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 31)
)
aluQosQueuePolicySlopePolicyGroup.setObjects(
      *(("ALU-QOS-MIB", "aluSapIngressQueueSlopePolicy"),
        ("ALU-QOS-MIB", "aluSapEgressQueueSlopePolicy"),
        ("ALU-QOS-MIB", "aluNetworkQueueSlopePolicy"))
)
if mibBuilder.loadTexts:
    aluQosQueuePolicySlopePolicyGroup.setStatus("current")

aluQosFabricProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 32)
)
aluQosFabricProfileGroup.setObjects(
      *(("ALU-QOS-MIB", "aluFabricProfileRowStatus"),
        ("ALU-QOS-MIB", "aluFabricProfileDescription"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex1"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex2"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex3"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex4"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex5"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex6"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex7"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex8"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex9"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex10"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex11"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex12"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex13"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex14"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex15"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex16"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex17"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex18"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex19"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex20"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex21"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex22"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex23"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex24"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex25"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex26"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex27"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex28"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex29"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex30"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex31"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex32"),
        ("ALU-QOS-MIB", "aluFabricProfileLastChanged"),
        ("ALU-QOS-MIB", "aluFabricProfileMode"),
        ("ALU-QOS-MIB", "aluFabricProfileAggregateRate"))
)
if mibBuilder.loadTexts:
    aluQosFabricProfileGroup.setStatus("obsolete")

aluQosSapEgressPolicyTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 33)
)
aluQosSapEgressPolicyTypeGroup.setObjects(
    ("ALU-QOS-MIB", "aluSapEgressPolicyType")
)
if mibBuilder.loadTexts:
    aluQosSapEgressPolicyTypeGroup.setStatus("current")

aluQosFabricProfileGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 34)
)
aluQosFabricProfileGroupV4v0.setObjects(
      *(("ALU-QOS-MIB", "aluFabricProfileRowStatus"),
        ("ALU-QOS-MIB", "aluFabricProfileDescription"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex1"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex2"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex3"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex4"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex5"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex6"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex7"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex8"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex9"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex10"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex11"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex12"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex13"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex14"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex15"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex16"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex17"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex18"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex19"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex20"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex21"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex22"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex23"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex24"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex25"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex26"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex27"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex28"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex29"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex30"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex31"),
        ("ALU-QOS-MIB", "aluFabricProfileRateToMdaIndex32"),
        ("ALU-QOS-MIB", "aluFabricProfileLastChanged"),
        ("ALU-QOS-MIB", "aluFabricProfileMode"),
        ("ALU-QOS-MIB", "aluFabricProfileAggregateRate"),
        ("ALU-QOS-MIB", "aluFabricProfileMultipointRate"))
)
if mibBuilder.loadTexts:
    aluQosFabricProfileGroupV4v0.setStatus("current")

aluSystemQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 2, 35)
)
aluSystemQosGroup.setObjects(
      *(("ALU-QOS-MIB", "aluSystemAccessIngAggRate"),
        ("ALU-QOS-MIB", "aluSystemNetworkIngAggRate"),
        ("ALU-QOS-MIB", "aluSystemQosLastChanged"))
)
if mibBuilder.loadTexts:
    aluSystemQosGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluQOSComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1, 1)
)
aluQOSComp7705V1v0.setObjects(
      *(("ALU-QOS-MIB", "aluQosQueuePolicySlopePolicyGroup"),
        ("ALU-QOS-MIB", "aluQosFabricProfileGroup"),
        ("ALU-QOS-MIB", "aluQosSapEgressPolicyTypeGroup"))
)
if mibBuilder.loadTexts:
    aluQOSComp7705V1v0.setStatus(
        "obsolete"
    )

aluQOSComp7705V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1, 2)
)
aluQOSComp7705V4v0.setObjects(
    ("ALU-QOS-MIB", "aluQosFabricProfileGroupV4v0")
)
if mibBuilder.loadTexts:
    aluQOSComp7705V4v0.setStatus(
        "obsolete"
    )

aluQOSComp7705V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 5, 1, 1, 3)
)
aluQOSComp7705V5v0.setObjects(
      *(("ALU-QOS-MIB", "aluQosQueuePolicySlopePolicyGroup"),
        ("ALU-QOS-MIB", "aluQosFabricProfileGroup"),
        ("ALU-QOS-MIB", "aluQosSapEgressPolicyTypeGroup"),
        ("ALU-QOS-MIB", "aluQosFabricProfileGroupV4v0"),
        ("ALU-QOS-MIB", "aluSystemQosGroup"))
)
if mibBuilder.loadTexts:
    aluQOSComp7705V5v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-QOS-MIB",
    **{"AluFabricProfilePolicyID": AluFabricProfilePolicyID,
       "AluFabricProfileMode": AluFabricProfileMode,
       "AluFabricProfileDestMdaRate": AluFabricProfileDestMdaRate,
       "AluSystemAggregateRate": AluSystemAggregateRate,
       "aluQOSMIBModule": aluQOSMIBModule,
       "aluQOSConformance": aluQOSConformance,
       "aluQOSCompliances": aluQOSCompliances,
       "aluQOSComp7705": aluQOSComp7705,
       "aluQOSComp7705V1v0": aluQOSComp7705V1v0,
       "aluQOSComp7705V4v0": aluQOSComp7705V4v0,
       "aluQOSComp7705V5v0": aluQOSComp7705V5v0,
       "aluQOSGroups": aluQOSGroups,
       "aluQosQueuePolicySlopePolicyGroup": aluQosQueuePolicySlopePolicyGroup,
       "aluQosFabricProfileGroup": aluQosFabricProfileGroup,
       "aluQosSapEgressPolicyTypeGroup": aluQosSapEgressPolicyTypeGroup,
       "aluQosFabricProfileGroupV4v0": aluQosFabricProfileGroupV4v0,
       "aluSystemQosGroup": aluSystemQosGroup,
       "aluQOSObjs": aluQOSObjs,
       "aluSapIngressQueueExtensionTable": aluSapIngressQueueExtensionTable,
       "aluSapIngressQueueExtensionEntry": aluSapIngressQueueExtensionEntry,
       "aluSapIngressQueueSlopePolicy": aluSapIngressQueueSlopePolicy,
       "aluSapEgressQueueExtensionTable": aluSapEgressQueueExtensionTable,
       "aluSapEgressQueueExtensionEntry": aluSapEgressQueueExtensionEntry,
       "aluSapEgressQueueSlopePolicy": aluSapEgressQueueSlopePolicy,
       "aluNetworkQueueExtensionTable": aluNetworkQueueExtensionTable,
       "aluNetworkQueueExtensionEntry": aluNetworkQueueExtensionEntry,
       "aluNetworkQueueSlopePolicy": aluNetworkQueueSlopePolicy,
       "aluFabricProfileTable": aluFabricProfileTable,
       "aluFabricProfileEntry": aluFabricProfileEntry,
       "aluFabricProfileIndex": aluFabricProfileIndex,
       "aluFabricProfileRowStatus": aluFabricProfileRowStatus,
       "aluFabricProfileDescription": aluFabricProfileDescription,
       "aluFabricProfileRateToMdaIndex1": aluFabricProfileRateToMdaIndex1,
       "aluFabricProfileRateToMdaIndex2": aluFabricProfileRateToMdaIndex2,
       "aluFabricProfileRateToMdaIndex3": aluFabricProfileRateToMdaIndex3,
       "aluFabricProfileRateToMdaIndex4": aluFabricProfileRateToMdaIndex4,
       "aluFabricProfileRateToMdaIndex5": aluFabricProfileRateToMdaIndex5,
       "aluFabricProfileRateToMdaIndex6": aluFabricProfileRateToMdaIndex6,
       "aluFabricProfileRateToMdaIndex7": aluFabricProfileRateToMdaIndex7,
       "aluFabricProfileRateToMdaIndex8": aluFabricProfileRateToMdaIndex8,
       "aluFabricProfileRateToMdaIndex9": aluFabricProfileRateToMdaIndex9,
       "aluFabricProfileRateToMdaIndex10": aluFabricProfileRateToMdaIndex10,
       "aluFabricProfileRateToMdaIndex11": aluFabricProfileRateToMdaIndex11,
       "aluFabricProfileRateToMdaIndex12": aluFabricProfileRateToMdaIndex12,
       "aluFabricProfileRateToMdaIndex13": aluFabricProfileRateToMdaIndex13,
       "aluFabricProfileRateToMdaIndex14": aluFabricProfileRateToMdaIndex14,
       "aluFabricProfileRateToMdaIndex15": aluFabricProfileRateToMdaIndex15,
       "aluFabricProfileRateToMdaIndex16": aluFabricProfileRateToMdaIndex16,
       "aluFabricProfileRateToMdaIndex17": aluFabricProfileRateToMdaIndex17,
       "aluFabricProfileRateToMdaIndex18": aluFabricProfileRateToMdaIndex18,
       "aluFabricProfileRateToMdaIndex19": aluFabricProfileRateToMdaIndex19,
       "aluFabricProfileRateToMdaIndex20": aluFabricProfileRateToMdaIndex20,
       "aluFabricProfileRateToMdaIndex21": aluFabricProfileRateToMdaIndex21,
       "aluFabricProfileRateToMdaIndex22": aluFabricProfileRateToMdaIndex22,
       "aluFabricProfileRateToMdaIndex23": aluFabricProfileRateToMdaIndex23,
       "aluFabricProfileRateToMdaIndex24": aluFabricProfileRateToMdaIndex24,
       "aluFabricProfileRateToMdaIndex25": aluFabricProfileRateToMdaIndex25,
       "aluFabricProfileRateToMdaIndex26": aluFabricProfileRateToMdaIndex26,
       "aluFabricProfileRateToMdaIndex27": aluFabricProfileRateToMdaIndex27,
       "aluFabricProfileRateToMdaIndex28": aluFabricProfileRateToMdaIndex28,
       "aluFabricProfileRateToMdaIndex29": aluFabricProfileRateToMdaIndex29,
       "aluFabricProfileRateToMdaIndex30": aluFabricProfileRateToMdaIndex30,
       "aluFabricProfileRateToMdaIndex31": aluFabricProfileRateToMdaIndex31,
       "aluFabricProfileRateToMdaIndex32": aluFabricProfileRateToMdaIndex32,
       "aluFabricProfileLastChanged": aluFabricProfileLastChanged,
       "aluFabricProfileMode": aluFabricProfileMode,
       "aluFabricProfileAggregateRate": aluFabricProfileAggregateRate,
       "aluFabricProfileMultipointRate": aluFabricProfileMultipointRate,
       "aluExtTSapEgressTable": aluExtTSapEgressTable,
       "aluExtTSapEgressEntry": aluExtTSapEgressEntry,
       "aluSapEgressPolicyType": aluSapEgressPolicyType,
       "aluSystemQosConfig": aluSystemQosConfig,
       "aluSystemAccessIngAggRate": aluSystemAccessIngAggRate,
       "aluSystemNetworkIngAggRate": aluSystemNetworkIngAggRate,
       "aluSystemQosLastChanged": aluSystemQosLastChanged}
)
