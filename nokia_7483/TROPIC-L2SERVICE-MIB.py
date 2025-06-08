# SNMP MIB module (TROPIC-L2SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-L2SERVICE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnL2ServiceMIB,
 tnServiceModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnL2ServiceMIB",
    "tnServiceModules")

(TnPerHopBehaviourType,
 TnStatsProfileId) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnPerHopBehaviourType",
    "TnStatsProfileId")


# MODULE-IDENTITY

tnL2ServiceMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TnSepIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TnServiceId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_TnL2ServiceConf_ObjectIdentity = ObjectIdentity
tnL2ServiceConf = _TnL2ServiceConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1)
)
_TnL2ServiceGroups_ObjectIdentity = ObjectIdentity
tnL2ServiceGroups = _TnL2ServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1)
)
_TnL2ServiceCompliances_ObjectIdentity = ObjectIdentity
tnL2ServiceCompliances = _TnL2ServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 2)
)
_TnL2ServiceObjs_ObjectIdentity = ObjectIdentity
tnL2ServiceObjs = _TnL2ServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2)
)
_TnEthernetServiceObjs_ObjectIdentity = ObjectIdentity
tnEthernetServiceObjs = _TnEthernetServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1)
)
_TnEthernetService_ObjectIdentity = ObjectIdentity
tnEthernetService = _TnEthernetService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 1)
)
_TnEthernetServiceTable_Object = MibTable
tnEthernetServiceTable = _TnEthernetServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthernetServiceTable.setStatus("current")
_TnEthernetServiceEntry_Object = MibTableRow
tnEthernetServiceEntry = _TnEthernetServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 1, 1, 1)
)
tnEthernetServiceEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
)
if mibBuilder.loadTexts:
    tnEthernetServiceEntry.setStatus("current")


class _TnServiceId_Type(TnServiceId):
    """Custom type tnServiceId based on TnServiceId"""
    subtypeSpec = TnServiceId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnServiceId_Type.__name__ = "TnServiceId"
_TnServiceId_Object = MibTableColumn
tnServiceId = _TnServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 1, 1, 1, 1),
    _TnServiceId_Type()
)
tnServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnServiceId.setStatus("current")
_TnEthernetServiceRowStatus_Type = RowStatus
_TnEthernetServiceRowStatus_Object = MibTableColumn
tnEthernetServiceRowStatus = _TnEthernetServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 1, 1, 1, 2),
    _TnEthernetServiceRowStatus_Type()
)
tnEthernetServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetServiceRowStatus.setStatus("current")


class _TnEthernetServiceDescr_Type(SnmpAdminString):
    """Custom type tnEthernetServiceDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnEthernetServiceDescr_Type.__name__ = "SnmpAdminString"
_TnEthernetServiceDescr_Object = MibTableColumn
tnEthernetServiceDescr = _TnEthernetServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 1, 1, 1, 3),
    _TnEthernetServiceDescr_Type()
)
tnEthernetServiceDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetServiceDescr.setStatus("current")


class _TnEthernetServicePBNServiceId_Type(TnServiceId):
    """Custom type tnEthernetServicePBNServiceId based on TnServiceId"""
    defaultValue = 0


_TnEthernetServicePBNServiceId_Type.__name__ = "TnServiceId"
_TnEthernetServicePBNServiceId_Object = MibTableColumn
tnEthernetServicePBNServiceId = _TnEthernetServicePBNServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 1, 1, 1, 4),
    _TnEthernetServicePBNServiceId_Type()
)
tnEthernetServicePBNServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetServicePBNServiceId.setStatus("current")
_TnEthernetSep_ObjectIdentity = ObjectIdentity
tnEthernetSep = _TnEthernetSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2)
)
_TnEthernetSepTable_Object = MibTable
tnEthernetSepTable = _TnEthernetSepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnEthernetSepTable.setStatus("current")
_TnEthernetSepEntry_Object = MibTableRow
tnEthernetSepEntry = _TnEthernetSepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1)
)
tnEthernetSepEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
    (0, "TROPIC-L2SERVICE-MIB", "tnSepIndex"),
)
if mibBuilder.loadTexts:
    tnEthernetSepEntry.setStatus("current")
_TnSepIndex_Type = TnSepIndex
_TnSepIndex_Object = MibTableColumn
tnSepIndex = _TnSepIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 1),
    _TnSepIndex_Type()
)
tnSepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSepIndex.setStatus("current")
_TnEthernetSepRowStatus_Type = RowStatus
_TnEthernetSepRowStatus_Object = MibTableColumn
tnEthernetSepRowStatus = _TnEthernetSepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 2),
    _TnEthernetSepRowStatus_Type()
)
tnEthernetSepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepRowStatus.setStatus("current")


class _TnEthernetSepDescr_Type(SnmpAdminString):
    """Custom type tnEthernetSepDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnEthernetSepDescr_Type.__name__ = "SnmpAdminString"
_TnEthernetSepDescr_Object = MibTableColumn
tnEthernetSepDescr = _TnEthernetSepDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 3),
    _TnEthernetSepDescr_Type()
)
tnEthernetSepDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepDescr.setStatus("current")
_TnEthernetSepIfIndex_Type = InterfaceIndex
_TnEthernetSepIfIndex_Object = MibTableColumn
tnEthernetSepIfIndex = _TnEthernetSepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 4),
    _TnEthernetSepIfIndex_Type()
)
tnEthernetSepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepIfIndex.setStatus("current")


class _TnEthernetSepDeliverOnFailure_Type(TruthValue):
    """Custom type tnEthernetSepDeliverOnFailure based on TruthValue"""
    defaultValue = 2


_TnEthernetSepDeliverOnFailure_Type.__name__ = "TruthValue"
_TnEthernetSepDeliverOnFailure_Object = MibTableColumn
tnEthernetSepDeliverOnFailure = _TnEthernetSepDeliverOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 5),
    _TnEthernetSepDeliverOnFailure_Type()
)
tnEthernetSepDeliverOnFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepDeliverOnFailure.setStatus("current")


class _TnEthernetSepAggregatorVLANTag_Type(Unsigned32):
    """Custom type tnEthernetSepAggregatorVLANTag based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnEthernetSepAggregatorVLANTag_Type.__name__ = "Unsigned32"
_TnEthernetSepAggregatorVLANTag_Object = MibTableColumn
tnEthernetSepAggregatorVLANTag = _TnEthernetSepAggregatorVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 6),
    _TnEthernetSepAggregatorVLANTag_Type()
)
tnEthernetSepAggregatorVLANTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepAggregatorVLANTag.setStatus("current")


class _TnEthernetSepUseAggregatorVLANTag_Type(TruthValue):
    """Custom type tnEthernetSepUseAggregatorVLANTag based on TruthValue"""
    defaultValue = 2


_TnEthernetSepUseAggregatorVLANTag_Type.__name__ = "TruthValue"
_TnEthernetSepUseAggregatorVLANTag_Object = MibTableColumn
tnEthernetSepUseAggregatorVLANTag = _TnEthernetSepUseAggregatorVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 7),
    _TnEthernetSepUseAggregatorVLANTag_Type()
)
tnEthernetSepUseAggregatorVLANTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepUseAggregatorVLANTag.setStatus("current")


class _TnEthernetSepDefaultVLANTag_Type(Unsigned32):
    """Custom type tnEthernetSepDefaultVLANTag based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnEthernetSepDefaultVLANTag_Type.__name__ = "Unsigned32"
_TnEthernetSepDefaultVLANTag_Object = MibTableColumn
tnEthernetSepDefaultVLANTag = _TnEthernetSepDefaultVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 8),
    _TnEthernetSepDefaultVLANTag_Type()
)
tnEthernetSepDefaultVLANTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepDefaultVLANTag.setStatus("current")


class _TnEthernetSepVLANMode_Type(Integer32):
    """Custom type tnEthernetSepVLANMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2),
          ("priorityTag", 3))
    )


_TnEthernetSepVLANMode_Type.__name__ = "Integer32"
_TnEthernetSepVLANMode_Object = MibTableColumn
tnEthernetSepVLANMode = _TnEthernetSepVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 9),
    _TnEthernetSepVLANMode_Type()
)
tnEthernetSepVLANMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepVLANMode.setStatus("current")


class _TnEthernetSepStatsTCAProfileId_Type(TnStatsProfileId):
    """Custom type tnEthernetSepStatsTCAProfileId based on TnStatsProfileId"""
    defaultValue = 0


_TnEthernetSepStatsTCAProfileId_Type.__name__ = "TnStatsProfileId"
_TnEthernetSepStatsTCAProfileId_Object = MibTableColumn
tnEthernetSepStatsTCAProfileId = _TnEthernetSepStatsTCAProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 1, 2, 1, 1, 10),
    _TnEthernetSepStatsTCAProfileId_Type()
)
tnEthernetSepStatsTCAProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthernetSepStatsTCAProfileId.setStatus("current")
_TnPosInterconnectServiceObjs_ObjectIdentity = ObjectIdentity
tnPosInterconnectServiceObjs = _TnPosInterconnectServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2)
)
_TnPosInterconnectService_ObjectIdentity = ObjectIdentity
tnPosInterconnectService = _TnPosInterconnectService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 1)
)
_TnPosInterconnectServiceTable_Object = MibTable
tnPosInterconnectServiceTable = _TnPosInterconnectServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnPosInterconnectServiceTable.setStatus("current")
_TnPosInterconnectServiceEntry_Object = MibTableRow
tnPosInterconnectServiceEntry = _TnPosInterconnectServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 1, 1, 1)
)
tnPosInterconnectServiceEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
)
if mibBuilder.loadTexts:
    tnPosInterconnectServiceEntry.setStatus("current")
_TnPosInterconnectServiceRowStatus_Type = RowStatus
_TnPosInterconnectServiceRowStatus_Object = MibTableColumn
tnPosInterconnectServiceRowStatus = _TnPosInterconnectServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 1, 1, 1, 1),
    _TnPosInterconnectServiceRowStatus_Type()
)
tnPosInterconnectServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPosInterconnectServiceRowStatus.setStatus("current")


class _TnPosInterconnectServiceDescr_Type(SnmpAdminString):
    """Custom type tnPosInterconnectServiceDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnPosInterconnectServiceDescr_Type.__name__ = "SnmpAdminString"
_TnPosInterconnectServiceDescr_Object = MibTableColumn
tnPosInterconnectServiceDescr = _TnPosInterconnectServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 1, 1, 1, 2),
    _TnPosInterconnectServiceDescr_Type()
)
tnPosInterconnectServiceDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPosInterconnectServiceDescr.setStatus("current")


class _TnPosInterconnectServiceSwitchingMode_Type(Integer32):
    """Custom type tnPosInterconnectServiceSwitchingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packetSwitched", 1),
          ("portSwitched", 2))
    )


_TnPosInterconnectServiceSwitchingMode_Type.__name__ = "Integer32"
_TnPosInterconnectServiceSwitchingMode_Object = MibTableColumn
tnPosInterconnectServiceSwitchingMode = _TnPosInterconnectServiceSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 1, 1, 1, 3),
    _TnPosInterconnectServiceSwitchingMode_Type()
)
tnPosInterconnectServiceSwitchingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPosInterconnectServiceSwitchingMode.setStatus("current")


class _TnPosInterconnectServiceEncapsulation_Type(Integer32):
    """Custom type tnPosInterconnectServiceEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("draftMartini", 2))
    )


_TnPosInterconnectServiceEncapsulation_Type.__name__ = "Integer32"
_TnPosInterconnectServiceEncapsulation_Object = MibTableColumn
tnPosInterconnectServiceEncapsulation = _TnPosInterconnectServiceEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 1, 1, 1, 4),
    _TnPosInterconnectServiceEncapsulation_Type()
)
tnPosInterconnectServiceEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPosInterconnectServiceEncapsulation.setStatus("current")
_TnPosInterconnectSep_ObjectIdentity = ObjectIdentity
tnPosInterconnectSep = _TnPosInterconnectSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 2)
)
_TnPosInterconnectSepTable_Object = MibTable
tnPosInterconnectSepTable = _TnPosInterconnectSepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnPosInterconnectSepTable.setStatus("current")
_TnPosInterconnectSepEntry_Object = MibTableRow
tnPosInterconnectSepEntry = _TnPosInterconnectSepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 2, 1, 1)
)
tnPosInterconnectSepEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
    (0, "TROPIC-L2SERVICE-MIB", "tnSepIndex"),
)
if mibBuilder.loadTexts:
    tnPosInterconnectSepEntry.setStatus("current")
_TnPosSepRowStatus_Type = RowStatus
_TnPosSepRowStatus_Object = MibTableColumn
tnPosSepRowStatus = _TnPosSepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 2, 1, 1, 1),
    _TnPosSepRowStatus_Type()
)
tnPosSepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPosSepRowStatus.setStatus("current")


class _TnPosSepDescr_Type(SnmpAdminString):
    """Custom type tnPosSepDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnPosSepDescr_Type.__name__ = "SnmpAdminString"
_TnPosSepDescr_Object = MibTableColumn
tnPosSepDescr = _TnPosSepDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 2, 1, 1, 2),
    _TnPosSepDescr_Type()
)
tnPosSepDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPosSepDescr.setStatus("current")
_TnPosSepIfIndex_Type = InterfaceIndex
_TnPosSepIfIndex_Object = MibTableColumn
tnPosSepIfIndex = _TnPosSepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 2, 2, 1, 1, 3),
    _TnPosSepIfIndex_Type()
)
tnPosSepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPosSepIfIndex.setStatus("current")
_TnIpServiceObjs_ObjectIdentity = ObjectIdentity
tnIpServiceObjs = _TnIpServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3)
)
_TnIpService_ObjectIdentity = ObjectIdentity
tnIpService = _TnIpService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 1)
)
_TnIpServiceTable_Object = MibTable
tnIpServiceTable = _TnIpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tnIpServiceTable.setStatus("current")
_TnIpServiceEntry_Object = MibTableRow
tnIpServiceEntry = _TnIpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 1, 1, 1)
)
tnIpServiceEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
)
if mibBuilder.loadTexts:
    tnIpServiceEntry.setStatus("current")
_TnIpServiceRowStatus_Type = RowStatus
_TnIpServiceRowStatus_Object = MibTableColumn
tnIpServiceRowStatus = _TnIpServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 1, 1, 1, 1),
    _TnIpServiceRowStatus_Type()
)
tnIpServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpServiceRowStatus.setStatus("current")


class _TnIpServiceDescr_Type(SnmpAdminString):
    """Custom type tnIpServiceDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnIpServiceDescr_Type.__name__ = "SnmpAdminString"
_TnIpServiceDescr_Object = MibTableColumn
tnIpServiceDescr = _TnIpServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 1, 1, 1, 2),
    _TnIpServiceDescr_Type()
)
tnIpServiceDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpServiceDescr.setStatus("current")


class _TnIpServicePBNServiceId_Type(TnServiceId):
    """Custom type tnIpServicePBNServiceId based on TnServiceId"""
    subtypeSpec = TnServiceId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnIpServicePBNServiceId_Type.__name__ = "TnServiceId"
_TnIpServicePBNServiceId_Object = MibTableColumn
tnIpServicePBNServiceId = _TnIpServicePBNServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 1, 1, 1, 3),
    _TnIpServicePBNServiceId_Type()
)
tnIpServicePBNServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpServicePBNServiceId.setStatus("current")
_TnIpSep_ObjectIdentity = ObjectIdentity
tnIpSep = _TnIpSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 2)
)
_TnIpSepTable_Object = MibTable
tnIpSepTable = _TnIpSepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tnIpSepTable.setStatus("current")
_TnIpSepEntry_Object = MibTableRow
tnIpSepEntry = _TnIpSepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 2, 1, 1)
)
tnIpSepEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
    (0, "TROPIC-L2SERVICE-MIB", "tnSepIndex"),
)
if mibBuilder.loadTexts:
    tnIpSepEntry.setStatus("current")
_TnIpSepRowStatus_Type = RowStatus
_TnIpSepRowStatus_Object = MibTableColumn
tnIpSepRowStatus = _TnIpSepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 2, 1, 1, 1),
    _TnIpSepRowStatus_Type()
)
tnIpSepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpSepRowStatus.setStatus("current")


class _TnIpSepDescr_Type(SnmpAdminString):
    """Custom type tnIpSepDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnIpSepDescr_Type.__name__ = "SnmpAdminString"
_TnIpSepDescr_Object = MibTableColumn
tnIpSepDescr = _TnIpSepDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 2, 1, 1, 2),
    _TnIpSepDescr_Type()
)
tnIpSepDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpSepDescr.setStatus("current")
_TnIpSepIfIndex_Type = InterfaceIndex
_TnIpSepIfIndex_Object = MibTableColumn
tnIpSepIfIndex = _TnIpSepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 3, 2, 1, 1, 3),
    _TnIpSepIfIndex_Type()
)
tnIpSepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIpSepIfIndex.setStatus("current")
_TnServiceObjs_ObjectIdentity = ObjectIdentity
tnServiceObjs = _TnServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4)
)
_TnServicePath_ObjectIdentity = ObjectIdentity
tnServicePath = _TnServicePath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1)
)
_TnServicePathTable_Object = MibTable
tnServicePathTable = _TnServicePathTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tnServicePathTable.setStatus("current")
_TnServicePathEntry_Object = MibTableRow
tnServicePathEntry = _TnServicePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1, 1, 1)
)
tnServicePathEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
    (0, "TROPIC-L2SERVICE-MIB", "tnSepIndex"),
    (0, "TROPIC-L2SERVICE-MIB", "tnServicePathDestIpAddress"),
    (0, "TROPIC-L2SERVICE-MIB", "tnServicePathDestSepIndex"),
)
if mibBuilder.loadTexts:
    tnServicePathEntry.setStatus("current")
_TnServicePathDestIpAddress_Type = IpAddress
_TnServicePathDestIpAddress_Object = MibTableColumn
tnServicePathDestIpAddress = _TnServicePathDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1, 1, 1, 1),
    _TnServicePathDestIpAddress_Type()
)
tnServicePathDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnServicePathDestIpAddress.setStatus("current")
_TnServicePathDestSepIndex_Type = TnSepIndex
_TnServicePathDestSepIndex_Object = MibTableColumn
tnServicePathDestSepIndex = _TnServicePathDestSepIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1, 1, 1, 2),
    _TnServicePathDestSepIndex_Type()
)
tnServicePathDestSepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnServicePathDestSepIndex.setStatus("current")
_TnServicePathRowStatus_Type = RowStatus
_TnServicePathRowStatus_Object = MibTableColumn
tnServicePathRowStatus = _TnServicePathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1, 1, 1, 3),
    _TnServicePathRowStatus_Type()
)
tnServicePathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServicePathRowStatus.setStatus("current")


class _TnServicePathDescr_Type(SnmpAdminString):
    """Custom type tnServicePathDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnServicePathDescr_Type.__name__ = "SnmpAdminString"
_TnServicePathDescr_Object = MibTableColumn
tnServicePathDescr = _TnServicePathDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1, 1, 1, 4),
    _TnServicePathDescr_Type()
)
tnServicePathDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServicePathDescr.setStatus("current")
_TnServicePathIfIndex_Type = InterfaceIndex
_TnServicePathIfIndex_Object = MibTableColumn
tnServicePathIfIndex = _TnServicePathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 4, 1, 1, 1, 5),
    _TnServicePathIfIndex_Type()
)
tnServicePathIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnServicePathIfIndex.setStatus("current")
_TnPBNObjs_ObjectIdentity = ObjectIdentity
tnPBNObjs = _TnPBNObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5)
)
_TnPBNService_ObjectIdentity = ObjectIdentity
tnPBNService = _TnPBNService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 1)
)
_TnPBNServiceTable_Object = MibTable
tnPBNServiceTable = _TnPBNServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tnPBNServiceTable.setStatus("current")
_TnPBNServiceEntry_Object = MibTableRow
tnPBNServiceEntry = _TnPBNServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 1, 1, 1)
)
tnPBNServiceEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
)
if mibBuilder.loadTexts:
    tnPBNServiceEntry.setStatus("current")
_TnPBNServiceRowStatus_Type = RowStatus
_TnPBNServiceRowStatus_Object = MibTableColumn
tnPBNServiceRowStatus = _TnPBNServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 1, 1, 1, 1),
    _TnPBNServiceRowStatus_Type()
)
tnPBNServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPBNServiceRowStatus.setStatus("current")


class _TnPBNServiceDescr_Type(SnmpAdminString):
    """Custom type tnPBNServiceDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnPBNServiceDescr_Type.__name__ = "SnmpAdminString"
_TnPBNServiceDescr_Object = MibTableColumn
tnPBNServiceDescr = _TnPBNServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 1, 1, 1, 2),
    _TnPBNServiceDescr_Type()
)
tnPBNServiceDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPBNServiceDescr.setStatus("current")
_TnPBL_ObjectIdentity = ObjectIdentity
tnPBL = _TnPBL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2)
)
_TnPBLTable_Object = MibTable
tnPBLTable = _TnPBLTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    tnPBLTable.setStatus("current")
_TnPBLEntry_Object = MibTableRow
tnPBLEntry = _TnPBLEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2, 1, 1)
)
tnPBLEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
    (0, "TROPIC-L2SERVICE-MIB", "tnPBLDestIpAddress"),
    (0, "TROPIC-L2SERVICE-MIB", "tnPBLId"),
)
if mibBuilder.loadTexts:
    tnPBLEntry.setStatus("current")
_TnPBLDestIpAddress_Type = IpAddress
_TnPBLDestIpAddress_Object = MibTableColumn
tnPBLDestIpAddress = _TnPBLDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2, 1, 1, 1),
    _TnPBLDestIpAddress_Type()
)
tnPBLDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPBLDestIpAddress.setStatus("current")


class _TnPBLId_Type(Integer32):
    """Custom type tnPBLId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnPBLId_Type.__name__ = "Integer32"
_TnPBLId_Object = MibTableColumn
tnPBLId = _TnPBLId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2, 1, 1, 2),
    _TnPBLId_Type()
)
tnPBLId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPBLId.setStatus("current")
_TnPBLRowStatus_Type = RowStatus
_TnPBLRowStatus_Object = MibTableColumn
tnPBLRowStatus = _TnPBLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2, 1, 1, 3),
    _TnPBLRowStatus_Type()
)
tnPBLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPBLRowStatus.setStatus("current")


class _TnPBLDescr_Type(SnmpAdminString):
    """Custom type tnPBLDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnPBLDescr_Type.__name__ = "SnmpAdminString"
_TnPBLDescr_Object = MibTableColumn
tnPBLDescr = _TnPBLDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2, 1, 1, 4),
    _TnPBLDescr_Type()
)
tnPBLDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPBLDescr.setStatus("current")
_TnPBLIfIndex_Type = InterfaceIndex
_TnPBLIfIndex_Object = MibTableColumn
tnPBLIfIndex = _TnPBLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 5, 2, 1, 1, 5),
    _TnPBLIfIndex_Type()
)
tnPBLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPBLIfIndex.setStatus("current")
_TnLinkAggregationObjs_ObjectIdentity = ObjectIdentity
tnLinkAggregationObjs = _TnLinkAggregationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6)
)
_TnAggregationLSP_ObjectIdentity = ObjectIdentity
tnAggregationLSP = _TnAggregationLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6, 1)
)
_TnAggregationLSPTable_Object = MibTable
tnAggregationLSPTable = _TnAggregationLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tnAggregationLSPTable.setStatus("current")
_TnAggregationLSPEntry_Object = MibTableRow
tnAggregationLSPEntry = _TnAggregationLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6, 1, 1, 1)
)
tnAggregationLSPEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnAggregationLSPDestIpAddress"),
)
if mibBuilder.loadTexts:
    tnAggregationLSPEntry.setStatus("current")
_TnAggregationLSPDestIpAddress_Type = IpAddress
_TnAggregationLSPDestIpAddress_Object = MibTableColumn
tnAggregationLSPDestIpAddress = _TnAggregationLSPDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6, 1, 1, 1, 1),
    _TnAggregationLSPDestIpAddress_Type()
)
tnAggregationLSPDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAggregationLSPDestIpAddress.setStatus("current")
_TnAggregationLSPRowStatus_Type = RowStatus
_TnAggregationLSPRowStatus_Object = MibTableColumn
tnAggregationLSPRowStatus = _TnAggregationLSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6, 1, 1, 1, 2),
    _TnAggregationLSPRowStatus_Type()
)
tnAggregationLSPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAggregationLSPRowStatus.setStatus("current")


class _TnAggregationLSPDescr_Type(SnmpAdminString):
    """Custom type tnAggregationLSPDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnAggregationLSPDescr_Type.__name__ = "SnmpAdminString"
_TnAggregationLSPDescr_Object = MibTableColumn
tnAggregationLSPDescr = _TnAggregationLSPDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6, 1, 1, 1, 3),
    _TnAggregationLSPDescr_Type()
)
tnAggregationLSPDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAggregationLSPDescr.setStatus("current")
_TnAggregationLSPIfIndex_Type = InterfaceIndex
_TnAggregationLSPIfIndex_Object = MibTableColumn
tnAggregationLSPIfIndex = _TnAggregationLSPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 6, 1, 1, 1, 4),
    _TnAggregationLSPIfIndex_Type()
)
tnAggregationLSPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAggregationLSPIfIndex.setStatus("current")
_TnServiceSelectionObjs_ObjectIdentity = ObjectIdentity
tnServiceSelectionObjs = _TnServiceSelectionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7)
)
_TnServiceSelection_ObjectIdentity = ObjectIdentity
tnServiceSelection = _TnServiceSelection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1)
)
_TnServiceSelectionTable_Object = MibTable
tnServiceSelectionTable = _TnServiceSelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tnServiceSelectionTable.setStatus("current")
_TnServiceSelectionEntry_Object = MibTableRow
tnServiceSelectionEntry = _TnServiceSelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1)
)
tnServiceSelectionEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
    (0, "TROPIC-L2SERVICE-MIB", "tnSepIndex"),
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceSelectionIndex"),
)
if mibBuilder.loadTexts:
    tnServiceSelectionEntry.setStatus("current")


class _TnServiceSelectionIndex_Type(Unsigned32):
    """Custom type tnServiceSelectionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnServiceSelectionIndex_Type.__name__ = "Unsigned32"
_TnServiceSelectionIndex_Object = MibTableColumn
tnServiceSelectionIndex = _TnServiceSelectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 1),
    _TnServiceSelectionIndex_Type()
)
tnServiceSelectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnServiceSelectionIndex.setStatus("current")
_TnServiceSelectionRowStatus_Type = RowStatus
_TnServiceSelectionRowStatus_Object = MibTableColumn
tnServiceSelectionRowStatus = _TnServiceSelectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 2),
    _TnServiceSelectionRowStatus_Type()
)
tnServiceSelectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionRowStatus.setStatus("current")


class _TnServiceSelectionPerHopBehaviour_Type(TnPerHopBehaviourType):
    """Custom type tnServiceSelectionPerHopBehaviour based on TnPerHopBehaviourType"""
    defaultValue = 4


_TnServiceSelectionPerHopBehaviour_Type.__name__ = "TnPerHopBehaviourType"
_TnServiceSelectionPerHopBehaviour_Object = MibTableColumn
tnServiceSelectionPerHopBehaviour = _TnServiceSelectionPerHopBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 3),
    _TnServiceSelectionPerHopBehaviour_Type()
)
tnServiceSelectionPerHopBehaviour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionPerHopBehaviour.setStatus("current")


class _TnServiceSelectionMask_Type(Bits):
    """Custom type tnServiceSelectionMask based on Bits"""
    namedValues = NamedValues(
        *(("tnServiceSelectionPort", 0),
          ("tnServiceSelectionEthPriority", 1),
          ("tnServiceSelectionEthVlanId", 2),
          ("tnServiceSelectionEthProtocolType", 3),
          ("tnServiceSelectionSrcIpSubnet", 4),
          ("tnServiceSelectionDestIpSubnet", 5),
          ("tnServiceSelectionIpProtocolNum", 6),
          ("tnServiceSelectionDSCP", 7),
          ("tnServiceSelectionSrcMinPort", 8),
          ("tnServiceSelectionSrcMaxPort", 9),
          ("tnServiceSelectionDestMinPort", 10),
          ("tnServiceSelectionDestMaxPort", 11),
          ("tnServiceSelectionMplsLabel", 12),
          ("tnServiceSelectionMplsEXP", 13))
    )

_TnServiceSelectionMask_Type.__name__ = "Bits"
_TnServiceSelectionMask_Object = MibTableColumn
tnServiceSelectionMask = _TnServiceSelectionMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 4),
    _TnServiceSelectionMask_Type()
)
tnServiceSelectionMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionMask.setStatus("current")
_TnServiceSelectionPort_Type = InterfaceIndex
_TnServiceSelectionPort_Object = MibTableColumn
tnServiceSelectionPort = _TnServiceSelectionPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 5),
    _TnServiceSelectionPort_Type()
)
tnServiceSelectionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionPort.setStatus("current")


class _TnServiceSelectionEthPriority_Type(Unsigned32):
    """Custom type tnServiceSelectionEthPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnServiceSelectionEthPriority_Type.__name__ = "Unsigned32"
_TnServiceSelectionEthPriority_Object = MibTableColumn
tnServiceSelectionEthPriority = _TnServiceSelectionEthPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 6),
    _TnServiceSelectionEthPriority_Type()
)
tnServiceSelectionEthPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionEthPriority.setStatus("current")


class _TnServiceSelectionEthVlanId_Type(Integer32):
    """Custom type tnServiceSelectionEthVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_TnServiceSelectionEthVlanId_Type.__name__ = "Integer32"
_TnServiceSelectionEthVlanId_Object = MibTableColumn
tnServiceSelectionEthVlanId = _TnServiceSelectionEthVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 7),
    _TnServiceSelectionEthVlanId_Type()
)
tnServiceSelectionEthVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionEthVlanId.setStatus("current")


class _TnServiceSelectionEthProtocolType_Type(Unsigned32):
    """Custom type tnServiceSelectionEthProtocolType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnServiceSelectionEthProtocolType_Type.__name__ = "Unsigned32"
_TnServiceSelectionEthProtocolType_Object = MibTableColumn
tnServiceSelectionEthProtocolType = _TnServiceSelectionEthProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 8),
    _TnServiceSelectionEthProtocolType_Type()
)
tnServiceSelectionEthProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionEthProtocolType.setStatus("current")
_TnServiceSelectionSrcIpSubnet_Type = IpAddress
_TnServiceSelectionSrcIpSubnet_Object = MibTableColumn
tnServiceSelectionSrcIpSubnet = _TnServiceSelectionSrcIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 9),
    _TnServiceSelectionSrcIpSubnet_Type()
)
tnServiceSelectionSrcIpSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionSrcIpSubnet.setStatus("current")
_TnServiceSelectionSrcIpSubnetMask_Type = IpAddress
_TnServiceSelectionSrcIpSubnetMask_Object = MibTableColumn
tnServiceSelectionSrcIpSubnetMask = _TnServiceSelectionSrcIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 10),
    _TnServiceSelectionSrcIpSubnetMask_Type()
)
tnServiceSelectionSrcIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionSrcIpSubnetMask.setStatus("current")
_TnServiceSelectionDestIpSubnet_Type = IpAddress
_TnServiceSelectionDestIpSubnet_Object = MibTableColumn
tnServiceSelectionDestIpSubnet = _TnServiceSelectionDestIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 11),
    _TnServiceSelectionDestIpSubnet_Type()
)
tnServiceSelectionDestIpSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionDestIpSubnet.setStatus("current")
_TnServiceSelectionDestIpSubnetMask_Type = IpAddress
_TnServiceSelectionDestIpSubnetMask_Object = MibTableColumn
tnServiceSelectionDestIpSubnetMask = _TnServiceSelectionDestIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 12),
    _TnServiceSelectionDestIpSubnetMask_Type()
)
tnServiceSelectionDestIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionDestIpSubnetMask.setStatus("current")


class _TnServiceSelectionIpProtocolNum_Type(Unsigned32):
    """Custom type tnServiceSelectionIpProtocolNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnServiceSelectionIpProtocolNum_Type.__name__ = "Unsigned32"
_TnServiceSelectionIpProtocolNum_Object = MibTableColumn
tnServiceSelectionIpProtocolNum = _TnServiceSelectionIpProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 13),
    _TnServiceSelectionIpProtocolNum_Type()
)
tnServiceSelectionIpProtocolNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionIpProtocolNum.setStatus("current")


class _TnServiceSelectionDSCP_Type(Integer32):
    """Custom type tnServiceSelectionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_TnServiceSelectionDSCP_Type.__name__ = "Integer32"
_TnServiceSelectionDSCP_Object = MibTableColumn
tnServiceSelectionDSCP = _TnServiceSelectionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 14),
    _TnServiceSelectionDSCP_Type()
)
tnServiceSelectionDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionDSCP.setStatus("current")


class _TnServiceSelectionSrcMinPort_Type(Unsigned32):
    """Custom type tnServiceSelectionSrcMinPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnServiceSelectionSrcMinPort_Type.__name__ = "Unsigned32"
_TnServiceSelectionSrcMinPort_Object = MibTableColumn
tnServiceSelectionSrcMinPort = _TnServiceSelectionSrcMinPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 15),
    _TnServiceSelectionSrcMinPort_Type()
)
tnServiceSelectionSrcMinPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionSrcMinPort.setStatus("current")


class _TnServiceSelectionSrcMaxPort_Type(Unsigned32):
    """Custom type tnServiceSelectionSrcMaxPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnServiceSelectionSrcMaxPort_Type.__name__ = "Unsigned32"
_TnServiceSelectionSrcMaxPort_Object = MibTableColumn
tnServiceSelectionSrcMaxPort = _TnServiceSelectionSrcMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 16),
    _TnServiceSelectionSrcMaxPort_Type()
)
tnServiceSelectionSrcMaxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionSrcMaxPort.setStatus("current")


class _TnServiceSelectionDestMinPort_Type(Unsigned32):
    """Custom type tnServiceSelectionDestMinPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnServiceSelectionDestMinPort_Type.__name__ = "Unsigned32"
_TnServiceSelectionDestMinPort_Object = MibTableColumn
tnServiceSelectionDestMinPort = _TnServiceSelectionDestMinPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 17),
    _TnServiceSelectionDestMinPort_Type()
)
tnServiceSelectionDestMinPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionDestMinPort.setStatus("current")


class _TnServiceSelectionDestMaxPort_Type(Unsigned32):
    """Custom type tnServiceSelectionDestMaxPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnServiceSelectionDestMaxPort_Type.__name__ = "Unsigned32"
_TnServiceSelectionDestMaxPort_Object = MibTableColumn
tnServiceSelectionDestMaxPort = _TnServiceSelectionDestMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 18),
    _TnServiceSelectionDestMaxPort_Type()
)
tnServiceSelectionDestMaxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionDestMaxPort.setStatus("current")


class _TnServiceSelectionMplsLabel_Type(Unsigned32):
    """Custom type tnServiceSelectionMplsLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_TnServiceSelectionMplsLabel_Type.__name__ = "Unsigned32"
_TnServiceSelectionMplsLabel_Object = MibTableColumn
tnServiceSelectionMplsLabel = _TnServiceSelectionMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 19),
    _TnServiceSelectionMplsLabel_Type()
)
tnServiceSelectionMplsLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionMplsLabel.setStatus("current")


class _TnServiceSelectionMplsEXP_Type(Unsigned32):
    """Custom type tnServiceSelectionMplsEXP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TnServiceSelectionMplsEXP_Type.__name__ = "Unsigned32"
_TnServiceSelectionMplsEXP_Object = MibTableColumn
tnServiceSelectionMplsEXP = _TnServiceSelectionMplsEXP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 1, 1, 1, 20),
    _TnServiceSelectionMplsEXP_Type()
)
tnServiceSelectionMplsEXP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnServiceSelectionMplsEXP.setStatus("current")
_TnBandwidthClassification_ObjectIdentity = ObjectIdentity
tnBandwidthClassification = _TnBandwidthClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2)
)
_TnBandwidthClassificationTable_Object = MibTable
tnBandwidthClassificationTable = _TnBandwidthClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    tnBandwidthClassificationTable.setStatus("current")
_TnBandwidthClassificationEntry_Object = MibTableRow
tnBandwidthClassificationEntry = _TnBandwidthClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1)
)
tnBandwidthClassificationEntry.setIndexNames(
    (0, "TROPIC-L2SERVICE-MIB", "tnServiceId"),
    (0, "TROPIC-L2SERVICE-MIB", "tnSepIndex"),
    (0, "TROPIC-L2SERVICE-MIB", "tnBandwidthClassPerHopBehaviour"),
)
if mibBuilder.loadTexts:
    tnBandwidthClassificationEntry.setStatus("current")
_TnBandwidthClassPerHopBehaviour_Type = TnPerHopBehaviourType
_TnBandwidthClassPerHopBehaviour_Object = MibTableColumn
tnBandwidthClassPerHopBehaviour = _TnBandwidthClassPerHopBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 1),
    _TnBandwidthClassPerHopBehaviour_Type()
)
tnBandwidthClassPerHopBehaviour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnBandwidthClassPerHopBehaviour.setStatus("current")
_TnBandwidthClassRowStatus_Type = RowStatus
_TnBandwidthClassRowStatus_Object = MibTableColumn
tnBandwidthClassRowStatus = _TnBandwidthClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 2),
    _TnBandwidthClassRowStatus_Type()
)
tnBandwidthClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassRowStatus.setStatus("current")
_TnBandwidthClassCIR_Type = Unsigned32
_TnBandwidthClassCIR_Object = MibTableColumn
tnBandwidthClassCIR = _TnBandwidthClassCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 3),
    _TnBandwidthClassCIR_Type()
)
tnBandwidthClassCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassCIR.setStatus("current")
if mibBuilder.loadTexts:
    tnBandwidthClassCIR.setUnits("Mb/s")
_TnBandwidthClassCBS_Type = Unsigned32
_TnBandwidthClassCBS_Object = MibTableColumn
tnBandwidthClassCBS = _TnBandwidthClassCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 4),
    _TnBandwidthClassCBS_Type()
)
tnBandwidthClassCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassCBS.setStatus("current")
if mibBuilder.loadTexts:
    tnBandwidthClassCBS.setUnits("bytes")
_TnBandwidthClassPIR_Type = Unsigned32
_TnBandwidthClassPIR_Object = MibTableColumn
tnBandwidthClassPIR = _TnBandwidthClassPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 5),
    _TnBandwidthClassPIR_Type()
)
tnBandwidthClassPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassPIR.setStatus("current")
if mibBuilder.loadTexts:
    tnBandwidthClassPIR.setUnits("Mb/s")
_TnBandwidthClassPBS_Type = Unsigned32
_TnBandwidthClassPBS_Object = MibTableColumn
tnBandwidthClassPBS = _TnBandwidthClassPBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 6),
    _TnBandwidthClassPBS_Type()
)
tnBandwidthClassPBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassPBS.setStatus("current")
if mibBuilder.loadTexts:
    tnBandwidthClassPBS.setUnits("bytes")
_TnBandwidthClassMinimumPolicedUnit_Type = Unsigned32
_TnBandwidthClassMinimumPolicedUnit_Object = MibTableColumn
tnBandwidthClassMinimumPolicedUnit = _TnBandwidthClassMinimumPolicedUnit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 7),
    _TnBandwidthClassMinimumPolicedUnit_Type()
)
tnBandwidthClassMinimumPolicedUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassMinimumPolicedUnit.setStatus("current")
if mibBuilder.loadTexts:
    tnBandwidthClassMinimumPolicedUnit.setUnits("bytes")
_TnBandwidthClassMaximumPacketSize_Type = Unsigned32
_TnBandwidthClassMaximumPacketSize_Object = MibTableColumn
tnBandwidthClassMaximumPacketSize = _TnBandwidthClassMaximumPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 8),
    _TnBandwidthClassMaximumPacketSize_Type()
)
tnBandwidthClassMaximumPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassMaximumPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    tnBandwidthClassMaximumPacketSize.setUnits("bytes")
_TnBandwidthClassDelay_Type = Unsigned32
_TnBandwidthClassDelay_Object = MibTableColumn
tnBandwidthClassDelay = _TnBandwidthClassDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 7, 2, 1, 1, 9),
    _TnBandwidthClassDelay_Type()
)
tnBandwidthClassDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnBandwidthClassDelay.setStatus("current")
if mibBuilder.loadTexts:
    tnBandwidthClassDelay.setUnits("microseconds")
_TnPathObjs_ObjectIdentity = ObjectIdentity
tnPathObjs = _TnPathObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8)
)
_TnPathDescriptor_ObjectIdentity = ObjectIdentity
tnPathDescriptor = _TnPathDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1)
)
_TnPathDescrTable_Object = MibTable
tnPathDescrTable = _TnPathDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tnPathDescrTable.setStatus("current")
_TnPathDescrEntry_Object = MibTableRow
tnPathDescrEntry = _TnPathDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1)
)
tnPathDescrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPathDescrEntry.setStatus("current")


class _TnPathDescrAdminStatus_Type(Integer32):
    """Custom type tnPathDescrAdminStatus based on Integer32"""
    defaultValue = 1

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


_TnPathDescrAdminStatus_Type.__name__ = "Integer32"
_TnPathDescrAdminStatus_Object = MibTableColumn
tnPathDescrAdminStatus = _TnPathDescrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 1),
    _TnPathDescrAdminStatus_Type()
)
tnPathDescrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrAdminStatus.setStatus("current")


class _TnPathDescrOperStatus_Type(Integer32):
    """Custom type tnPathDescrOperStatus based on Integer32"""
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
        *(("none", 1),
          ("setupInProgress", 2),
          ("restorationInProgress", 3),
          ("connected", 4),
          ("disconnected", 5))
    )


_TnPathDescrOperStatus_Type.__name__ = "Integer32"
_TnPathDescrOperStatus_Object = MibTableColumn
tnPathDescrOperStatus = _TnPathDescrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 2),
    _TnPathDescrOperStatus_Type()
)
tnPathDescrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPathDescrOperStatus.setStatus("current")


class _TnPathDescrPathId_Type(Counter64):
    """Custom type tnPathDescrPathId based on Counter64"""
    defaultValue = 0


_TnPathDescrPathId_Type.__name__ = "Counter64"
_TnPathDescrPathId_Object = MibTableColumn
tnPathDescrPathId = _TnPathDescrPathId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 3),
    _TnPathDescrPathId_Type()
)
tnPathDescrPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPathDescrPathId.setStatus("current")


class _TnPathDescrRestorationLevel_Type(Integer32):
    """Custom type tnPathDescrRestorationLevel based on Integer32"""
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
        *(("protectionWithDedicatedBandwidth", 1),
          ("highPriority", 2),
          ("lowPriority", 3))
    )


_TnPathDescrRestorationLevel_Type.__name__ = "Integer32"
_TnPathDescrRestorationLevel_Object = MibTableColumn
tnPathDescrRestorationLevel = _TnPathDescrRestorationLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 4),
    _TnPathDescrRestorationLevel_Type()
)
tnPathDescrRestorationLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrRestorationLevel.setStatus("current")


class _TnPathDescrUserDefinedExplicitRoute_Type(TruthValue):
    """Custom type tnPathDescrUserDefinedExplicitRoute based on TruthValue"""
    defaultValue = 2


_TnPathDescrUserDefinedExplicitRoute_Type.__name__ = "TruthValue"
_TnPathDescrUserDefinedExplicitRoute_Object = MibTableColumn
tnPathDescrUserDefinedExplicitRoute = _TnPathDescrUserDefinedExplicitRoute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 5),
    _TnPathDescrUserDefinedExplicitRoute_Type()
)
tnPathDescrUserDefinedExplicitRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrUserDefinedExplicitRoute.setStatus("current")


class _TnPathDescrProtectionSwitch_Type(TruthValue):
    """Custom type tnPathDescrProtectionSwitch based on TruthValue"""
    defaultValue = 2


_TnPathDescrProtectionSwitch_Type.__name__ = "TruthValue"
_TnPathDescrProtectionSwitch_Object = MibTableColumn
tnPathDescrProtectionSwitch = _TnPathDescrProtectionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 6),
    _TnPathDescrProtectionSwitch_Type()
)
tnPathDescrProtectionSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrProtectionSwitch.setStatus("current")


class _TnPathDescrOptimize_Type(Integer32):
    """Custom type tnPathDescrOptimize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("working", 2),
          ("protected", 3))
    )


_TnPathDescrOptimize_Type.__name__ = "Integer32"
_TnPathDescrOptimize_Object = MibTableColumn
tnPathDescrOptimize = _TnPathDescrOptimize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 7),
    _TnPathDescrOptimize_Type()
)
tnPathDescrOptimize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrOptimize.setStatus("current")


class _TnPathDescrSetupPriority_Type(Unsigned32):
    """Custom type tnPathDescrSetupPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TnPathDescrSetupPriority_Type.__name__ = "Unsigned32"
_TnPathDescrSetupPriority_Object = MibTableColumn
tnPathDescrSetupPriority = _TnPathDescrSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 8),
    _TnPathDescrSetupPriority_Type()
)
tnPathDescrSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrSetupPriority.setStatus("current")
_TnPathDescrProbePktsEnabled_Type = TruthValue
_TnPathDescrProbePktsEnabled_Object = MibTableColumn
tnPathDescrProbePktsEnabled = _TnPathDescrProbePktsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 9),
    _TnPathDescrProbePktsEnabled_Type()
)
tnPathDescrProbePktsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrProbePktsEnabled.setStatus("current")
_TnPathDescrStatsTCAProfileId_Type = TnStatsProfileId
_TnPathDescrStatsTCAProfileId_Object = MibTableColumn
tnPathDescrStatsTCAProfileId = _TnPathDescrStatsTCAProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 10),
    _TnPathDescrStatsTCAProfileId_Type()
)
tnPathDescrStatsTCAProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrStatsTCAProfileId.setStatus("current")
_TnPathDescrProbePktsStatsTCAProfileId_Type = TnStatsProfileId
_TnPathDescrProbePktsStatsTCAProfileId_Object = MibTableColumn
tnPathDescrProbePktsStatsTCAProfileId = _TnPathDescrProbePktsStatsTCAProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 11),
    _TnPathDescrProbePktsStatsTCAProfileId_Type()
)
tnPathDescrProbePktsStatsTCAProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathDescrProbePktsStatsTCAProfileId.setStatus("current")


class _TnPathDescrErrorStatus_Type(Integer32):
    """Custom type tnPathDescrErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cacFailure", 2))
    )


_TnPathDescrErrorStatus_Type.__name__ = "Integer32"
_TnPathDescrErrorStatus_Object = MibTableColumn
tnPathDescrErrorStatus = _TnPathDescrErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 1, 1, 1, 12),
    _TnPathDescrErrorStatus_Type()
)
tnPathDescrErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPathDescrErrorStatus.setStatus("current")
_TnPathTrafficParam_ObjectIdentity = ObjectIdentity
tnPathTrafficParam = _TnPathTrafficParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2)
)
_TnPathTrafficParamTable_Object = MibTable
tnPathTrafficParamTable = _TnPathTrafficParamTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    tnPathTrafficParamTable.setStatus("current")
_TnPathTrafficParamEntry_Object = MibTableRow
tnPathTrafficParamEntry = _TnPathTrafficParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1)
)
tnPathTrafficParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-L2SERVICE-MIB", "tnPathTrafficParamPerHopBehaviour"),
)
if mibBuilder.loadTexts:
    tnPathTrafficParamEntry.setStatus("current")
_TnPathTrafficParamPerHopBehaviour_Type = TnPerHopBehaviourType
_TnPathTrafficParamPerHopBehaviour_Object = MibTableColumn
tnPathTrafficParamPerHopBehaviour = _TnPathTrafficParamPerHopBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 1),
    _TnPathTrafficParamPerHopBehaviour_Type()
)
tnPathTrafficParamPerHopBehaviour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPathTrafficParamPerHopBehaviour.setStatus("current")
_TnPathTrafficParamCIR_Type = Unsigned32
_TnPathTrafficParamCIR_Object = MibTableColumn
tnPathTrafficParamCIR = _TnPathTrafficParamCIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 2),
    _TnPathTrafficParamCIR_Type()
)
tnPathTrafficParamCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathTrafficParamCIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPathTrafficParamCIR.setUnits("Mb/s")
_TnPathTrafficParamCBS_Type = Unsigned32
_TnPathTrafficParamCBS_Object = MibTableColumn
tnPathTrafficParamCBS = _TnPathTrafficParamCBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 3),
    _TnPathTrafficParamCBS_Type()
)
tnPathTrafficParamCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathTrafficParamCBS.setStatus("current")
if mibBuilder.loadTexts:
    tnPathTrafficParamCBS.setUnits("bytes")
_TnPathTrafficParamPIR_Type = Unsigned32
_TnPathTrafficParamPIR_Object = MibTableColumn
tnPathTrafficParamPIR = _TnPathTrafficParamPIR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 4),
    _TnPathTrafficParamPIR_Type()
)
tnPathTrafficParamPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathTrafficParamPIR.setStatus("current")
if mibBuilder.loadTexts:
    tnPathTrafficParamPIR.setUnits("Mb/s")
_TnPathTrafficParamPBS_Type = Unsigned32
_TnPathTrafficParamPBS_Object = MibTableColumn
tnPathTrafficParamPBS = _TnPathTrafficParamPBS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 5),
    _TnPathTrafficParamPBS_Type()
)
tnPathTrafficParamPBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathTrafficParamPBS.setStatus("current")
if mibBuilder.loadTexts:
    tnPathTrafficParamPBS.setUnits("bytes")
_TnPathTrafficParamMinimumPolicedUnit_Type = Unsigned32
_TnPathTrafficParamMinimumPolicedUnit_Object = MibTableColumn
tnPathTrafficParamMinimumPolicedUnit = _TnPathTrafficParamMinimumPolicedUnit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 6),
    _TnPathTrafficParamMinimumPolicedUnit_Type()
)
tnPathTrafficParamMinimumPolicedUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathTrafficParamMinimumPolicedUnit.setStatus("current")
if mibBuilder.loadTexts:
    tnPathTrafficParamMinimumPolicedUnit.setUnits("bytes")
_TnPathTrafficParamMaximumPacketSize_Type = Unsigned32
_TnPathTrafficParamMaximumPacketSize_Object = MibTableColumn
tnPathTrafficParamMaximumPacketSize = _TnPathTrafficParamMaximumPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 7),
    _TnPathTrafficParamMaximumPacketSize_Type()
)
tnPathTrafficParamMaximumPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathTrafficParamMaximumPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPathTrafficParamMaximumPacketSize.setUnits("bytes")
_TnPathTrafficParamDelay_Type = Unsigned32
_TnPathTrafficParamDelay_Object = MibTableColumn
tnPathTrafficParamDelay = _TnPathTrafficParamDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 2, 1, 1, 8),
    _TnPathTrafficParamDelay_Type()
)
tnPathTrafficParamDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPathTrafficParamDelay.setStatus("current")
if mibBuilder.loadTexts:
    tnPathTrafficParamDelay.setUnits("microseconds")
_TnLSPHop_ObjectIdentity = ObjectIdentity
tnLSPHop = _TnLSPHop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3)
)
_TnLSPHopTable_Object = MibTable
tnLSPHopTable = _TnLSPHopTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    tnLSPHopTable.setStatus("current")
_TnLSPHopEntry_Object = MibTableRow
tnLSPHopEntry = _TnLSPHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3, 1, 1)
)
tnLSPHopEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-L2SERVICE-MIB", "tnLSPProtectionType"),
    (0, "TROPIC-L2SERVICE-MIB", "tnLSPHopCount"),
)
if mibBuilder.loadTexts:
    tnLSPHopEntry.setStatus("current")


class _TnLSPProtectionType_Type(Integer32):
    """Custom type tnLSPProtectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protected", 2))
    )


_TnLSPProtectionType_Type.__name__ = "Integer32"
_TnLSPProtectionType_Object = MibTableColumn
tnLSPProtectionType = _TnLSPProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3, 1, 1, 1),
    _TnLSPProtectionType_Type()
)
tnLSPProtectionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLSPProtectionType.setStatus("current")


class _TnLSPHopCount_Type(Unsigned32):
    """Custom type tnLSPHopCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnLSPHopCount_Type.__name__ = "Unsigned32"
_TnLSPHopCount_Object = MibTableColumn
tnLSPHopCount = _TnLSPHopCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3, 1, 1, 2),
    _TnLSPHopCount_Type()
)
tnLSPHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLSPHopCount.setStatus("current")
_TnLSPHopRowStatus_Type = RowStatus
_TnLSPHopRowStatus_Object = MibTableColumn
tnLSPHopRowStatus = _TnLSPHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3, 1, 1, 3),
    _TnLSPHopRowStatus_Type()
)
tnLSPHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLSPHopRowStatus.setStatus("current")
_TnLSPHopOutgoingIp_Type = IpAddress
_TnLSPHopOutgoingIp_Object = MibTableColumn
tnLSPHopOutgoingIp = _TnLSPHopOutgoingIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3, 1, 1, 4),
    _TnLSPHopOutgoingIp_Type()
)
tnLSPHopOutgoingIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLSPHopOutgoingIp.setStatus("current")
_TnLSPHopOutgoingIfIndex_Type = InterfaceIndex
_TnLSPHopOutgoingIfIndex_Object = MibTableColumn
tnLSPHopOutgoingIfIndex = _TnLSPHopOutgoingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 2, 8, 3, 1, 1, 5),
    _TnLSPHopOutgoingIfIndex_Type()
)
tnLSPHopOutgoingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLSPHopOutgoingIfIndex.setStatus("current")

# Managed Objects groups

tnEthernetServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 1)
)
tnEthernetServiceGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnEthernetServiceRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetServiceDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetServicePBNServiceId"))
)
if mibBuilder.loadTexts:
    tnEthernetServiceGroup.setStatus("current")

tnEthernetSepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 2)
)
tnEthernetSepGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnEthernetSepRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepIfIndex"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepDeliverOnFailure"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepAggregatorVLANTag"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepUseAggregatorVLANTag"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepDefaultVLANTag"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepVLANMode"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepStatsTCAProfileId"))
)
if mibBuilder.loadTexts:
    tnEthernetSepGroup.setStatus("current")

tnPosInterconnectServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 3)
)
tnPosInterconnectServiceGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnPosInterconnectServiceRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnPosInterconnectServiceDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnPosInterconnectServiceSwitchingMode"),
        ("TROPIC-L2SERVICE-MIB", "tnPosInterconnectServiceEncapsulation"))
)
if mibBuilder.loadTexts:
    tnPosInterconnectServiceGroup.setStatus("current")

tnPosSepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 4)
)
tnPosSepGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnPosSepRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnPosSepDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnPosSepIfIndex"))
)
if mibBuilder.loadTexts:
    tnPosSepGroup.setStatus("current")

tnIpServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 5)
)
tnIpServiceGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnIpServiceRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnIpServiceDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnIpServicePBNServiceId"))
)
if mibBuilder.loadTexts:
    tnIpServiceGroup.setStatus("current")

tnIpSepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 6)
)
tnIpSepGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnIpSepRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnIpSepDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnIpSepIfIndex"))
)
if mibBuilder.loadTexts:
    tnIpSepGroup.setStatus("current")

tnServicePathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 7)
)
tnServicePathGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnServicePathRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnServicePathDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnServicePathIfIndex"))
)
if mibBuilder.loadTexts:
    tnServicePathGroup.setStatus("current")

tnPBNServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 8)
)
tnPBNServiceGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnPBNServiceRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnPBNServiceDescr"))
)
if mibBuilder.loadTexts:
    tnPBNServiceGroup.setStatus("current")

tnPBLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 9)
)
tnPBLGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnPBLRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnPBLDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnPBLIfIndex"))
)
if mibBuilder.loadTexts:
    tnPBLGroup.setStatus("current")

tnAggregationLSPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 10)
)
tnAggregationLSPGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnAggregationLSPRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnAggregationLSPDescr"),
        ("TROPIC-L2SERVICE-MIB", "tnAggregationLSPIfIndex"))
)
if mibBuilder.loadTexts:
    tnAggregationLSPGroup.setStatus("current")

tnServiceSelectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 11)
)
tnServiceSelectionGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnServiceSelectionRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionPerHopBehaviour"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionMask"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionPort"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionEthPriority"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionEthVlanId"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionEthProtocolType"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionSrcIpSubnet"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionSrcIpSubnetMask"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionDestIpSubnet"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionDestIpSubnetMask"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionIpProtocolNum"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionDSCP"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionSrcMinPort"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionSrcMaxPort"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionDestMinPort"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionDestMaxPort"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionMplsLabel"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionMplsEXP"))
)
if mibBuilder.loadTexts:
    tnServiceSelectionGroup.setStatus("current")

tnBandwidthClassificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 12)
)
tnBandwidthClassificationGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnBandwidthClassRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassCIR"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassCBS"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassPIR"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassPBS"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassMinimumPolicedUnit"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassMaximumPacketSize"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassDelay"))
)
if mibBuilder.loadTexts:
    tnBandwidthClassificationGroup.setStatus("current")

tnPathDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 13)
)
tnPathDescrGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnPathDescrAdminStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrOperStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrPathId"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrRestorationLevel"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrUserDefinedExplicitRoute"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrProtectionSwitch"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrOptimize"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrSetupPriority"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrProbePktsEnabled"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrStatsTCAProfileId"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrProbePktsStatsTCAProfileId"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrErrorStatus"))
)
if mibBuilder.loadTexts:
    tnPathDescrGroup.setStatus("current")

tnPathTrafficParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 14)
)
tnPathTrafficParamGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamCIR"),
        ("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamCBS"),
        ("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamPIR"),
        ("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamPBS"),
        ("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamMinimumPolicedUnit"),
        ("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamMaximumPacketSize"),
        ("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamDelay"))
)
if mibBuilder.loadTexts:
    tnPathTrafficParamGroup.setStatus("current")

tnLSPHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 1, 15)
)
tnLSPHopGroup.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnLSPHopRowStatus"),
        ("TROPIC-L2SERVICE-MIB", "tnLSPHopOutgoingIp"),
        ("TROPIC-L2SERVICE-MIB", "tnLSPHopOutgoingIfIndex"))
)
if mibBuilder.loadTexts:
    tnLSPHopGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnL2ServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2, 1, 2, 1)
)
tnL2ServiceCompliance.setObjects(
      *(("TROPIC-L2SERVICE-MIB", "tnEthernetServiceGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnEthernetSepGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnPosInterconnectServiceGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnPosSepGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnIpServiceGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnIpSepGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnServicePathGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnPBNServiceGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnPBLGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnAggregationLSPGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnServiceSelectionGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnBandwidthClassificationGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnPathDescrGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnPathTrafficParamGroup"),
        ("TROPIC-L2SERVICE-MIB", "tnLSPHopGroup"))
)
if mibBuilder.loadTexts:
    tnL2ServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-L2SERVICE-MIB",
    **{"TnSepIndex": TnSepIndex,
       "TnServiceId": TnServiceId,
       "tnL2ServiceMibModule": tnL2ServiceMibModule,
       "tnL2ServiceConf": tnL2ServiceConf,
       "tnL2ServiceGroups": tnL2ServiceGroups,
       "tnEthernetServiceGroup": tnEthernetServiceGroup,
       "tnEthernetSepGroup": tnEthernetSepGroup,
       "tnPosInterconnectServiceGroup": tnPosInterconnectServiceGroup,
       "tnPosSepGroup": tnPosSepGroup,
       "tnIpServiceGroup": tnIpServiceGroup,
       "tnIpSepGroup": tnIpSepGroup,
       "tnServicePathGroup": tnServicePathGroup,
       "tnPBNServiceGroup": tnPBNServiceGroup,
       "tnPBLGroup": tnPBLGroup,
       "tnAggregationLSPGroup": tnAggregationLSPGroup,
       "tnServiceSelectionGroup": tnServiceSelectionGroup,
       "tnBandwidthClassificationGroup": tnBandwidthClassificationGroup,
       "tnPathDescrGroup": tnPathDescrGroup,
       "tnPathTrafficParamGroup": tnPathTrafficParamGroup,
       "tnLSPHopGroup": tnLSPHopGroup,
       "tnL2ServiceCompliances": tnL2ServiceCompliances,
       "tnL2ServiceCompliance": tnL2ServiceCompliance,
       "tnL2ServiceObjs": tnL2ServiceObjs,
       "tnEthernetServiceObjs": tnEthernetServiceObjs,
       "tnEthernetService": tnEthernetService,
       "tnEthernetServiceTable": tnEthernetServiceTable,
       "tnEthernetServiceEntry": tnEthernetServiceEntry,
       "tnServiceId": tnServiceId,
       "tnEthernetServiceRowStatus": tnEthernetServiceRowStatus,
       "tnEthernetServiceDescr": tnEthernetServiceDescr,
       "tnEthernetServicePBNServiceId": tnEthernetServicePBNServiceId,
       "tnEthernetSep": tnEthernetSep,
       "tnEthernetSepTable": tnEthernetSepTable,
       "tnEthernetSepEntry": tnEthernetSepEntry,
       "tnSepIndex": tnSepIndex,
       "tnEthernetSepRowStatus": tnEthernetSepRowStatus,
       "tnEthernetSepDescr": tnEthernetSepDescr,
       "tnEthernetSepIfIndex": tnEthernetSepIfIndex,
       "tnEthernetSepDeliverOnFailure": tnEthernetSepDeliverOnFailure,
       "tnEthernetSepAggregatorVLANTag": tnEthernetSepAggregatorVLANTag,
       "tnEthernetSepUseAggregatorVLANTag": tnEthernetSepUseAggregatorVLANTag,
       "tnEthernetSepDefaultVLANTag": tnEthernetSepDefaultVLANTag,
       "tnEthernetSepVLANMode": tnEthernetSepVLANMode,
       "tnEthernetSepStatsTCAProfileId": tnEthernetSepStatsTCAProfileId,
       "tnPosInterconnectServiceObjs": tnPosInterconnectServiceObjs,
       "tnPosInterconnectService": tnPosInterconnectService,
       "tnPosInterconnectServiceTable": tnPosInterconnectServiceTable,
       "tnPosInterconnectServiceEntry": tnPosInterconnectServiceEntry,
       "tnPosInterconnectServiceRowStatus": tnPosInterconnectServiceRowStatus,
       "tnPosInterconnectServiceDescr": tnPosInterconnectServiceDescr,
       "tnPosInterconnectServiceSwitchingMode": tnPosInterconnectServiceSwitchingMode,
       "tnPosInterconnectServiceEncapsulation": tnPosInterconnectServiceEncapsulation,
       "tnPosInterconnectSep": tnPosInterconnectSep,
       "tnPosInterconnectSepTable": tnPosInterconnectSepTable,
       "tnPosInterconnectSepEntry": tnPosInterconnectSepEntry,
       "tnPosSepRowStatus": tnPosSepRowStatus,
       "tnPosSepDescr": tnPosSepDescr,
       "tnPosSepIfIndex": tnPosSepIfIndex,
       "tnIpServiceObjs": tnIpServiceObjs,
       "tnIpService": tnIpService,
       "tnIpServiceTable": tnIpServiceTable,
       "tnIpServiceEntry": tnIpServiceEntry,
       "tnIpServiceRowStatus": tnIpServiceRowStatus,
       "tnIpServiceDescr": tnIpServiceDescr,
       "tnIpServicePBNServiceId": tnIpServicePBNServiceId,
       "tnIpSep": tnIpSep,
       "tnIpSepTable": tnIpSepTable,
       "tnIpSepEntry": tnIpSepEntry,
       "tnIpSepRowStatus": tnIpSepRowStatus,
       "tnIpSepDescr": tnIpSepDescr,
       "tnIpSepIfIndex": tnIpSepIfIndex,
       "tnServiceObjs": tnServiceObjs,
       "tnServicePath": tnServicePath,
       "tnServicePathTable": tnServicePathTable,
       "tnServicePathEntry": tnServicePathEntry,
       "tnServicePathDestIpAddress": tnServicePathDestIpAddress,
       "tnServicePathDestSepIndex": tnServicePathDestSepIndex,
       "tnServicePathRowStatus": tnServicePathRowStatus,
       "tnServicePathDescr": tnServicePathDescr,
       "tnServicePathIfIndex": tnServicePathIfIndex,
       "tnPBNObjs": tnPBNObjs,
       "tnPBNService": tnPBNService,
       "tnPBNServiceTable": tnPBNServiceTable,
       "tnPBNServiceEntry": tnPBNServiceEntry,
       "tnPBNServiceRowStatus": tnPBNServiceRowStatus,
       "tnPBNServiceDescr": tnPBNServiceDescr,
       "tnPBL": tnPBL,
       "tnPBLTable": tnPBLTable,
       "tnPBLEntry": tnPBLEntry,
       "tnPBLDestIpAddress": tnPBLDestIpAddress,
       "tnPBLId": tnPBLId,
       "tnPBLRowStatus": tnPBLRowStatus,
       "tnPBLDescr": tnPBLDescr,
       "tnPBLIfIndex": tnPBLIfIndex,
       "tnLinkAggregationObjs": tnLinkAggregationObjs,
       "tnAggregationLSP": tnAggregationLSP,
       "tnAggregationLSPTable": tnAggregationLSPTable,
       "tnAggregationLSPEntry": tnAggregationLSPEntry,
       "tnAggregationLSPDestIpAddress": tnAggregationLSPDestIpAddress,
       "tnAggregationLSPRowStatus": tnAggregationLSPRowStatus,
       "tnAggregationLSPDescr": tnAggregationLSPDescr,
       "tnAggregationLSPIfIndex": tnAggregationLSPIfIndex,
       "tnServiceSelectionObjs": tnServiceSelectionObjs,
       "tnServiceSelection": tnServiceSelection,
       "tnServiceSelectionTable": tnServiceSelectionTable,
       "tnServiceSelectionEntry": tnServiceSelectionEntry,
       "tnServiceSelectionIndex": tnServiceSelectionIndex,
       "tnServiceSelectionRowStatus": tnServiceSelectionRowStatus,
       "tnServiceSelectionPerHopBehaviour": tnServiceSelectionPerHopBehaviour,
       "tnServiceSelectionMask": tnServiceSelectionMask,
       "tnServiceSelectionPort": tnServiceSelectionPort,
       "tnServiceSelectionEthPriority": tnServiceSelectionEthPriority,
       "tnServiceSelectionEthVlanId": tnServiceSelectionEthVlanId,
       "tnServiceSelectionEthProtocolType": tnServiceSelectionEthProtocolType,
       "tnServiceSelectionSrcIpSubnet": tnServiceSelectionSrcIpSubnet,
       "tnServiceSelectionSrcIpSubnetMask": tnServiceSelectionSrcIpSubnetMask,
       "tnServiceSelectionDestIpSubnet": tnServiceSelectionDestIpSubnet,
       "tnServiceSelectionDestIpSubnetMask": tnServiceSelectionDestIpSubnetMask,
       "tnServiceSelectionIpProtocolNum": tnServiceSelectionIpProtocolNum,
       "tnServiceSelectionDSCP": tnServiceSelectionDSCP,
       "tnServiceSelectionSrcMinPort": tnServiceSelectionSrcMinPort,
       "tnServiceSelectionSrcMaxPort": tnServiceSelectionSrcMaxPort,
       "tnServiceSelectionDestMinPort": tnServiceSelectionDestMinPort,
       "tnServiceSelectionDestMaxPort": tnServiceSelectionDestMaxPort,
       "tnServiceSelectionMplsLabel": tnServiceSelectionMplsLabel,
       "tnServiceSelectionMplsEXP": tnServiceSelectionMplsEXP,
       "tnBandwidthClassification": tnBandwidthClassification,
       "tnBandwidthClassificationTable": tnBandwidthClassificationTable,
       "tnBandwidthClassificationEntry": tnBandwidthClassificationEntry,
       "tnBandwidthClassPerHopBehaviour": tnBandwidthClassPerHopBehaviour,
       "tnBandwidthClassRowStatus": tnBandwidthClassRowStatus,
       "tnBandwidthClassCIR": tnBandwidthClassCIR,
       "tnBandwidthClassCBS": tnBandwidthClassCBS,
       "tnBandwidthClassPIR": tnBandwidthClassPIR,
       "tnBandwidthClassPBS": tnBandwidthClassPBS,
       "tnBandwidthClassMinimumPolicedUnit": tnBandwidthClassMinimumPolicedUnit,
       "tnBandwidthClassMaximumPacketSize": tnBandwidthClassMaximumPacketSize,
       "tnBandwidthClassDelay": tnBandwidthClassDelay,
       "tnPathObjs": tnPathObjs,
       "tnPathDescriptor": tnPathDescriptor,
       "tnPathDescrTable": tnPathDescrTable,
       "tnPathDescrEntry": tnPathDescrEntry,
       "tnPathDescrAdminStatus": tnPathDescrAdminStatus,
       "tnPathDescrOperStatus": tnPathDescrOperStatus,
       "tnPathDescrPathId": tnPathDescrPathId,
       "tnPathDescrRestorationLevel": tnPathDescrRestorationLevel,
       "tnPathDescrUserDefinedExplicitRoute": tnPathDescrUserDefinedExplicitRoute,
       "tnPathDescrProtectionSwitch": tnPathDescrProtectionSwitch,
       "tnPathDescrOptimize": tnPathDescrOptimize,
       "tnPathDescrSetupPriority": tnPathDescrSetupPriority,
       "tnPathDescrProbePktsEnabled": tnPathDescrProbePktsEnabled,
       "tnPathDescrStatsTCAProfileId": tnPathDescrStatsTCAProfileId,
       "tnPathDescrProbePktsStatsTCAProfileId": tnPathDescrProbePktsStatsTCAProfileId,
       "tnPathDescrErrorStatus": tnPathDescrErrorStatus,
       "tnPathTrafficParam": tnPathTrafficParam,
       "tnPathTrafficParamTable": tnPathTrafficParamTable,
       "tnPathTrafficParamEntry": tnPathTrafficParamEntry,
       "tnPathTrafficParamPerHopBehaviour": tnPathTrafficParamPerHopBehaviour,
       "tnPathTrafficParamCIR": tnPathTrafficParamCIR,
       "tnPathTrafficParamCBS": tnPathTrafficParamCBS,
       "tnPathTrafficParamPIR": tnPathTrafficParamPIR,
       "tnPathTrafficParamPBS": tnPathTrafficParamPBS,
       "tnPathTrafficParamMinimumPolicedUnit": tnPathTrafficParamMinimumPolicedUnit,
       "tnPathTrafficParamMaximumPacketSize": tnPathTrafficParamMaximumPacketSize,
       "tnPathTrafficParamDelay": tnPathTrafficParamDelay,
       "tnLSPHop": tnLSPHop,
       "tnLSPHopTable": tnLSPHopTable,
       "tnLSPHopEntry": tnLSPHopEntry,
       "tnLSPProtectionType": tnLSPProtectionType,
       "tnLSPHopCount": tnLSPHopCount,
       "tnLSPHopRowStatus": tnLSPHopRowStatus,
       "tnLSPHopOutgoingIp": tnLSPHopOutgoingIp,
       "tnLSPHopOutgoingIfIndex": tnLSPHopOutgoingIfIndex}
)
