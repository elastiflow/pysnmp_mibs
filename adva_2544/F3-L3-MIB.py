# SNMP MIB module (F3-L3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-L3-MIB.mib
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
 CmPmBinAction,
 CmPmIntervalType,
 F3DisplayString,
 IpVersion,
 OperationalState,
 PerfCounter64,
 SecondaryState,
 TrafficDirection,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "F3DisplayString",
    "IpVersion",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState",
    "TrafficDirection",
    "VlanId",
    "VlanPriority")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(PolicerAlgorithmType,
 PolicerColorMode) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "PolicerAlgorithmType",
    "PolicerColorMode")

(CmDhcpRole,
 DHCPCIDType,
 DHCPHostNameType,
 IpEntryType) = mibBuilder.importSymbols(
    "CM-IP-MIB",
    "CmDhcpRole",
    "DHCPCIDType",
    "DHCPHostNameType",
    "IpEntryType")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3L3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37)
)
if mibBuilder.loadTexts:
    f3L3MIB.setRevisions(
        ("2014-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VrfAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ping", 1),
          ("fluchARPCache", 2),
          ("traceRoute", 3),
          ("retrieveEffectiveRoutes", 4))
    )



class IfIpAddressSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )



class DhcpRelayInterfaceSide(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )



class L3AclRuleOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("accept", 1),
          ("deny", 2))
    )



class AclRuleL2Side(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("network", 2))
    )



class TrafficIpRouteStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("active", 1),
          ("nexthopUnresovled", 2),
          ("interfaceOutage", 3),
          ("noResources", 4),
          ("standby", 5))
    )



class RouteFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dDynamic", 0),
          ("gUseGW", 1),
          ("hFullMask", 2),
          ("mModifiedByIcmp", 3),
          ("oOutage", 4),
          ("uNormal", 5))
    )


class AffectiveArpActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("retrieveAffectiveArp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_F3L3Objects_ObjectIdentity = ObjectIdentity
f3L3Objects = _F3L3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1)
)
_F3DhcpRelayAgentTable_Object = MibTable
f3DhcpRelayAgentTable = _F3DhcpRelayAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1)
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTable.setStatus("current")
_F3DhcpRelayAgentEntry_Object = MibTableRow
f3DhcpRelayAgentEntry = _F3DhcpRelayAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1)
)
f3DhcpRelayAgentEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3DhcpRelayAgentIndex"),
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentEntry.setStatus("current")
_F3DhcpRelayAgentIndex_Type = Integer32
_F3DhcpRelayAgentIndex_Object = MibTableColumn
f3DhcpRelayAgentIndex = _F3DhcpRelayAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 1),
    _F3DhcpRelayAgentIndex_Type()
)
f3DhcpRelayAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentIndex.setStatus("current")


class _F3DhcpRelayAgentAlias_Type(F3DisplayString):
    """Custom type f3DhcpRelayAgentAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3DhcpRelayAgentAlias_Type.__name__ = "F3DisplayString"
_F3DhcpRelayAgentAlias_Object = MibTableColumn
f3DhcpRelayAgentAlias = _F3DhcpRelayAgentAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 2),
    _F3DhcpRelayAgentAlias_Type()
)
f3DhcpRelayAgentAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentAlias.setStatus("current")
_F3DhcpRelayAgentAdminState_Type = AdminState
_F3DhcpRelayAgentAdminState_Object = MibTableColumn
f3DhcpRelayAgentAdminState = _F3DhcpRelayAgentAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 3),
    _F3DhcpRelayAgentAdminState_Type()
)
f3DhcpRelayAgentAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentAdminState.setStatus("current")
_F3DhcpRelayAgentSecondaryState_Type = SecondaryState
_F3DhcpRelayAgentSecondaryState_Object = MibTableColumn
f3DhcpRelayAgentSecondaryState = _F3DhcpRelayAgentSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 4),
    _F3DhcpRelayAgentSecondaryState_Type()
)
f3DhcpRelayAgentSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentSecondaryState.setStatus("current")
_F3DhcpRelayAgentOperationalState_Type = OperationalState
_F3DhcpRelayAgentOperationalState_Object = MibTableColumn
f3DhcpRelayAgentOperationalState = _F3DhcpRelayAgentOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 5),
    _F3DhcpRelayAgentOperationalState_Type()
)
f3DhcpRelayAgentOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentOperationalState.setStatus("current")
_F3DhcpRelayAgentIpVersion_Type = IpVersion
_F3DhcpRelayAgentIpVersion_Object = MibTableColumn
f3DhcpRelayAgentIpVersion = _F3DhcpRelayAgentIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 6),
    _F3DhcpRelayAgentIpVersion_Type()
)
f3DhcpRelayAgentIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentIpVersion.setStatus("current")
_F3DhcpRelayAgentServerIpAddress_Type = IpAddress
_F3DhcpRelayAgentServerIpAddress_Object = MibTableColumn
f3DhcpRelayAgentServerIpAddress = _F3DhcpRelayAgentServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 7),
    _F3DhcpRelayAgentServerIpAddress_Type()
)
f3DhcpRelayAgentServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentServerIpAddress.setStatus("current")
_F3DhcpRelayAgentOp82SubOp9ControlEnabled_Type = TruthValue
_F3DhcpRelayAgentOp82SubOp9ControlEnabled_Object = MibTableColumn
f3DhcpRelayAgentOp82SubOp9ControlEnabled = _F3DhcpRelayAgentOp82SubOp9ControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 8),
    _F3DhcpRelayAgentOp82SubOp9ControlEnabled_Type()
)
f3DhcpRelayAgentOp82SubOp9ControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentOp82SubOp9ControlEnabled.setStatus("current")


class _F3DhcpRelayAgentOp82SubOp9Value_Type(DisplayString):
    """Custom type f3DhcpRelayAgentOp82SubOp9Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3DhcpRelayAgentOp82SubOp9Value_Type.__name__ = "DisplayString"
_F3DhcpRelayAgentOp82SubOp9Value_Object = MibTableColumn
f3DhcpRelayAgentOp82SubOp9Value = _F3DhcpRelayAgentOp82SubOp9Value_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 9),
    _F3DhcpRelayAgentOp82SubOp9Value_Type()
)
f3DhcpRelayAgentOp82SubOp9Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentOp82SubOp9Value.setStatus("current")
_F3DhcpRelayAgentStorageType_Type = StorageType
_F3DhcpRelayAgentStorageType_Object = MibTableColumn
f3DhcpRelayAgentStorageType = _F3DhcpRelayAgentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 10),
    _F3DhcpRelayAgentStorageType_Type()
)
f3DhcpRelayAgentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentStorageType.setStatus("current")
_F3DhcpRelayAgentRowStatus_Type = RowStatus
_F3DhcpRelayAgentRowStatus_Object = MibTableColumn
f3DhcpRelayAgentRowStatus = _F3DhcpRelayAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 11),
    _F3DhcpRelayAgentRowStatus_Type()
)
f3DhcpRelayAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentRowStatus.setStatus("current")
_F3VrfTable_Object = MibTable
f3VrfTable = _F3VrfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2)
)
if mibBuilder.loadTexts:
    f3VrfTable.setStatus("current")
_F3VrfEntry_Object = MibTableRow
f3VrfEntry = _F3VrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1)
)
f3VrfEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
)
if mibBuilder.loadTexts:
    f3VrfEntry.setStatus("current")
_F3VrfIndex_Type = Integer32
_F3VrfIndex_Object = MibTableColumn
f3VrfIndex = _F3VrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 1),
    _F3VrfIndex_Type()
)
f3VrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3VrfIndex.setStatus("current")


class _F3VrfAlias_Type(F3DisplayString):
    """Custom type f3VrfAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3VrfAlias_Type.__name__ = "F3DisplayString"
_F3VrfAlias_Object = MibTableColumn
f3VrfAlias = _F3VrfAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 2),
    _F3VrfAlias_Type()
)
f3VrfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAlias.setStatus("current")
_F3VrfAdminState_Type = AdminState
_F3VrfAdminState_Object = MibTableColumn
f3VrfAdminState = _F3VrfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 3),
    _F3VrfAdminState_Type()
)
f3VrfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAdminState.setStatus("current")
_F3VrfSecondaryState_Type = SecondaryState
_F3VrfSecondaryState_Object = MibTableColumn
f3VrfSecondaryState = _F3VrfSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 4),
    _F3VrfSecondaryState_Type()
)
f3VrfSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfSecondaryState.setStatus("current")
_F3VrfOperationalState_Type = OperationalState
_F3VrfOperationalState_Object = MibTableColumn
f3VrfOperationalState = _F3VrfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 5),
    _F3VrfOperationalState_Type()
)
f3VrfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfOperationalState.setStatus("current")
_F3VrfAccIsolationControlEnabled_Type = OperationalState
_F3VrfAccIsolationControlEnabled_Object = MibTableColumn
f3VrfAccIsolationControlEnabled = _F3VrfAccIsolationControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 6),
    _F3VrfAccIsolationControlEnabled_Type()
)
f3VrfAccIsolationControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAccIsolationControlEnabled.setStatus("current")
_F3VrfPingIpv4Destination_Type = IpAddress
_F3VrfPingIpv4Destination_Object = MibTableColumn
f3VrfPingIpv4Destination = _F3VrfPingIpv4Destination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 7),
    _F3VrfPingIpv4Destination_Type()
)
f3VrfPingIpv4Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfPingIpv4Destination.setStatus("current")
_F3VrfTraceRouteIpv4Destination_Type = IpAddress
_F3VrfTraceRouteIpv4Destination_Object = MibTableColumn
f3VrfTraceRouteIpv4Destination = _F3VrfTraceRouteIpv4Destination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 8),
    _F3VrfTraceRouteIpv4Destination_Type()
)
f3VrfTraceRouteIpv4Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfTraceRouteIpv4Destination.setStatus("current")
_F3VrfAction_Type = VrfAction
_F3VrfAction_Object = MibTableColumn
f3VrfAction = _F3VrfAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 9),
    _F3VrfAction_Type()
)
f3VrfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAction.setStatus("current")
_F3VrfPingResult_Type = F3DisplayString
_F3VrfPingResult_Object = MibTableColumn
f3VrfPingResult = _F3VrfPingResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 10),
    _F3VrfPingResult_Type()
)
f3VrfPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfPingResult.setStatus("current")
_F3VrfTraceRouteResult_Type = F3DisplayString
_F3VrfTraceRouteResult_Object = MibTableColumn
f3VrfTraceRouteResult = _F3VrfTraceRouteResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 11),
    _F3VrfTraceRouteResult_Type()
)
f3VrfTraceRouteResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfTraceRouteResult.setStatus("current")
_F3VrfStorageType_Type = StorageType
_F3VrfStorageType_Object = MibTableColumn
f3VrfStorageType = _F3VrfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 12),
    _F3VrfStorageType_Type()
)
f3VrfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfStorageType.setStatus("current")
_F3VrfRowStatus_Type = RowStatus
_F3VrfRowStatus_Object = MibTableColumn
f3VrfRowStatus = _F3VrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 13),
    _F3VrfRowStatus_Type()
)
f3VrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfRowStatus.setStatus("current")
_F3VrfDhcpRoutesControl_Type = TruthValue
_F3VrfDhcpRoutesControl_Object = MibTableColumn
f3VrfDhcpRoutesControl = _F3VrfDhcpRoutesControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 14),
    _F3VrfDhcpRoutesControl_Type()
)
f3VrfDhcpRoutesControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfDhcpRoutesControl.setStatus("current")
_F3L3FlowPointTable_Object = MibTable
f3L3FlowPointTable = _F3L3FlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3)
)
if mibBuilder.loadTexts:
    f3L3FlowPointTable.setStatus("current")
_F3L3FlowPointEntry_Object = MibTableRow
f3L3FlowPointEntry = _F3L3FlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1)
)
f3L3FlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointEntry.setStatus("current")
_F3L3FlowPointPortTypeIndex_Type = Integer32
_F3L3FlowPointPortTypeIndex_Object = MibTableColumn
f3L3FlowPointPortTypeIndex = _F3L3FlowPointPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 1),
    _F3L3FlowPointPortTypeIndex_Type()
)
f3L3FlowPointPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3FlowPointPortTypeIndex.setStatus("current")
_F3L3FlowPointPortIndex_Type = Integer32
_F3L3FlowPointPortIndex_Object = MibTableColumn
f3L3FlowPointPortIndex = _F3L3FlowPointPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 2),
    _F3L3FlowPointPortIndex_Type()
)
f3L3FlowPointPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3FlowPointPortIndex.setStatus("current")
_F3L3FlowPointIndex_Type = Integer32
_F3L3FlowPointIndex_Object = MibTableColumn
f3L3FlowPointIndex = _F3L3FlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 3),
    _F3L3FlowPointIndex_Type()
)
f3L3FlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3FlowPointIndex.setStatus("current")


class _F3L3FlowPointAlias_Type(F3DisplayString):
    """Custom type f3L3FlowPointAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L3FlowPointAlias_Type.__name__ = "F3DisplayString"
_F3L3FlowPointAlias_Object = MibTableColumn
f3L3FlowPointAlias = _F3L3FlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 4),
    _F3L3FlowPointAlias_Type()
)
f3L3FlowPointAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointAlias.setStatus("current")
_F3L3FlowPointAdminState_Type = AdminState
_F3L3FlowPointAdminState_Object = MibTableColumn
f3L3FlowPointAdminState = _F3L3FlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 5),
    _F3L3FlowPointAdminState_Type()
)
f3L3FlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointAdminState.setStatus("current")
_F3L3FlowPointSecondaryState_Type = SecondaryState
_F3L3FlowPointSecondaryState_Object = MibTableColumn
f3L3FlowPointSecondaryState = _F3L3FlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 6),
    _F3L3FlowPointSecondaryState_Type()
)
f3L3FlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointSecondaryState.setStatus("current")
_F3L3FlowPointOperationalState_Type = OperationalState
_F3L3FlowPointOperationalState_Object = MibTableColumn
f3L3FlowPointOperationalState = _F3L3FlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 7),
    _F3L3FlowPointOperationalState_Type()
)
f3L3FlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointOperationalState.setStatus("current")
_F3L3FlowPointMultiCOSEnabled_Type = TruthValue
_F3L3FlowPointMultiCOSEnabled_Object = MibTableColumn
f3L3FlowPointMultiCOSEnabled = _F3L3FlowPointMultiCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 8),
    _F3L3FlowPointMultiCOSEnabled_Type()
)
f3L3FlowPointMultiCOSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointMultiCOSEnabled.setStatus("current")
_F3L3FlowPointCOS_Type = Integer32
_F3L3FlowPointCOS_Object = MibTableColumn
f3L3FlowPointCOS = _F3L3FlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 9),
    _F3L3FlowPointCOS_Type()
)
f3L3FlowPointCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointCOS.setStatus("current")
_F3L3FlowPointUntaggedMemberShipEnabled_Type = TruthValue
_F3L3FlowPointUntaggedMemberShipEnabled_Object = MibTableColumn
f3L3FlowPointUntaggedMemberShipEnabled = _F3L3FlowPointUntaggedMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 10),
    _F3L3FlowPointUntaggedMemberShipEnabled_Type()
)
f3L3FlowPointUntaggedMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointUntaggedMemberShipEnabled.setStatus("current")
_F3L3FlowPointOuterTagMemberShipEnabled_Type = TruthValue
_F3L3FlowPointOuterTagMemberShipEnabled_Object = MibTableColumn
f3L3FlowPointOuterTagMemberShipEnabled = _F3L3FlowPointOuterTagMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 11),
    _F3L3FlowPointOuterTagMemberShipEnabled_Type()
)
f3L3FlowPointOuterTagMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointOuterTagMemberShipEnabled.setStatus("current")
_F3L3FlowPointOuterTagMemberShipVlanId_Type = VlanId
_F3L3FlowPointOuterTagMemberShipVlanId_Object = MibTableColumn
f3L3FlowPointOuterTagMemberShipVlanId = _F3L3FlowPointOuterTagMemberShipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 12),
    _F3L3FlowPointOuterTagMemberShipVlanId_Type()
)
f3L3FlowPointOuterTagMemberShipVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointOuterTagMemberShipVlanId.setStatus("current")
_F3L3FlowPointInnerTagMemberShipEnabled_Type = TruthValue
_F3L3FlowPointInnerTagMemberShipEnabled_Object = MibTableColumn
f3L3FlowPointInnerTagMemberShipEnabled = _F3L3FlowPointInnerTagMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 13),
    _F3L3FlowPointInnerTagMemberShipEnabled_Type()
)
f3L3FlowPointInnerTagMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointInnerTagMemberShipEnabled.setStatus("current")
_F3L3FlowPointInnerTagMemberShipVlanId_Type = VlanId
_F3L3FlowPointInnerTagMemberShipVlanId_Object = MibTableColumn
f3L3FlowPointInnerTagMemberShipVlanId = _F3L3FlowPointInnerTagMemberShipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 14),
    _F3L3FlowPointInnerTagMemberShipVlanId_Type()
)
f3L3FlowPointInnerTagMemberShipVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointInnerTagMemberShipVlanId.setStatus("current")
_F3L3FlowPointFragmentedPktsFwdEnabled_Type = TruthValue
_F3L3FlowPointFragmentedPktsFwdEnabled_Object = MibTableColumn
f3L3FlowPointFragmentedPktsFwdEnabled = _F3L3FlowPointFragmentedPktsFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 15),
    _F3L3FlowPointFragmentedPktsFwdEnabled_Type()
)
f3L3FlowPointFragmentedPktsFwdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointFragmentedPktsFwdEnabled.setStatus("current")
_F3L3FlowPointHCosMgmtEnabled_Type = TruthValue
_F3L3FlowPointHCosMgmtEnabled_Object = MibTableColumn
f3L3FlowPointHCosMgmtEnabled = _F3L3FlowPointHCosMgmtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 16),
    _F3L3FlowPointHCosMgmtEnabled_Type()
)
f3L3FlowPointHCosMgmtEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosMgmtEnabled.setStatus("current")
_F3L3FlowPointHCosGuaranteedBwHi_Type = Unsigned32
_F3L3FlowPointHCosGuaranteedBwHi_Object = MibTableColumn
f3L3FlowPointHCosGuaranteedBwHi = _F3L3FlowPointHCosGuaranteedBwHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 17),
    _F3L3FlowPointHCosGuaranteedBwHi_Type()
)
f3L3FlowPointHCosGuaranteedBwHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosGuaranteedBwHi.setStatus("current")
_F3L3FlowPointHCosGuaranteedBwLo_Type = Unsigned32
_F3L3FlowPointHCosGuaranteedBwLo_Object = MibTableColumn
f3L3FlowPointHCosGuaranteedBwLo = _F3L3FlowPointHCosGuaranteedBwLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 18),
    _F3L3FlowPointHCosGuaranteedBwLo_Type()
)
f3L3FlowPointHCosGuaranteedBwLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosGuaranteedBwLo.setStatus("current")
_F3L3FlowPointHCosMaximumBwHi_Type = Unsigned32
_F3L3FlowPointHCosMaximumBwHi_Object = MibTableColumn
f3L3FlowPointHCosMaximumBwHi = _F3L3FlowPointHCosMaximumBwHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 19),
    _F3L3FlowPointHCosMaximumBwHi_Type()
)
f3L3FlowPointHCosMaximumBwHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosMaximumBwHi.setStatus("current")
_F3L3FlowPointHCosMaximumBwLo_Type = Unsigned32
_F3L3FlowPointHCosMaximumBwLo_Object = MibTableColumn
f3L3FlowPointHCosMaximumBwLo = _F3L3FlowPointHCosMaximumBwLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 20),
    _F3L3FlowPointHCosMaximumBwLo_Type()
)
f3L3FlowPointHCosMaximumBwLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosMaximumBwLo.setStatus("current")
_F3L3FlowPointPolicingEnabled_Type = TruthValue
_F3L3FlowPointPolicingEnabled_Object = MibTableColumn
f3L3FlowPointPolicingEnabled = _F3L3FlowPointPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 21),
    _F3L3FlowPointPolicingEnabled_Type()
)
f3L3FlowPointPolicingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointPolicingEnabled.setStatus("current")
_F3L3FlowPointStorageType_Type = StorageType
_F3L3FlowPointStorageType_Object = MibTableColumn
f3L3FlowPointStorageType = _F3L3FlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 22),
    _F3L3FlowPointStorageType_Type()
)
f3L3FlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3FlowPointStorageType.setStatus("current")
_F3L3FlowPointRowStatus_Type = RowStatus
_F3L3FlowPointRowStatus_Object = MibTableColumn
f3L3FlowPointRowStatus = _F3L3FlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 23),
    _F3L3FlowPointRowStatus_Type()
)
f3L3FlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3FlowPointRowStatus.setStatus("current")
_F3L3AclRuleTable_Object = MibTable
f3L3AclRuleTable = _F3L3AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4)
)
if mibBuilder.loadTexts:
    f3L3AclRuleTable.setStatus("current")
_F3L3AclRuleEntry_Object = MibTableRow
f3L3AclRuleEntry = _F3L3AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1)
)
f3L3AclRuleEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleEntry.setStatus("current")
_F3L3AclRuleParentIndex_Type = Integer32
_F3L3AclRuleParentIndex_Object = MibTableColumn
f3L3AclRuleParentIndex = _F3L3AclRuleParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 1),
    _F3L3AclRuleParentIndex_Type()
)
f3L3AclRuleParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3AclRuleParentIndex.setStatus("current")
_F3L3AclRuleIndex_Type = Integer32
_F3L3AclRuleIndex_Object = MibTableColumn
f3L3AclRuleIndex = _F3L3AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 2),
    _F3L3AclRuleIndex_Type()
)
f3L3AclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3AclRuleIndex.setStatus("current")


class _F3L3AclRuleAlias_Type(F3DisplayString):
    """Custom type f3L3AclRuleAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L3AclRuleAlias_Type.__name__ = "F3DisplayString"
_F3L3AclRuleAlias_Object = MibTableColumn
f3L3AclRuleAlias = _F3L3AclRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 3),
    _F3L3AclRuleAlias_Type()
)
f3L3AclRuleAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleAlias.setStatus("current")
_F3L3AclRuleSrcIpv4AddressControl_Type = TruthValue
_F3L3AclRuleSrcIpv4AddressControl_Object = MibTableColumn
f3L3AclRuleSrcIpv4AddressControl = _F3L3AclRuleSrcIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 4),
    _F3L3AclRuleSrcIpv4AddressControl_Type()
)
f3L3AclRuleSrcIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpv4AddressControl.setStatus("current")
_F3L3AclRuleDynamicSrcIpControl_Type = TruthValue
_F3L3AclRuleDynamicSrcIpControl_Object = MibTableColumn
f3L3AclRuleDynamicSrcIpControl = _F3L3AclRuleDynamicSrcIpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 5),
    _F3L3AclRuleDynamicSrcIpControl_Type()
)
f3L3AclRuleDynamicSrcIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDynamicSrcIpControl.setStatus("current")
_F3L3AclRuleSrcIpv4AddressLowLimit_Type = IpAddress
_F3L3AclRuleSrcIpv4AddressLowLimit_Object = MibTableColumn
f3L3AclRuleSrcIpv4AddressLowLimit = _F3L3AclRuleSrcIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 6),
    _F3L3AclRuleSrcIpv4AddressLowLimit_Type()
)
f3L3AclRuleSrcIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpv4AddressLowLimit.setStatus("current")
_F3L3AclRuleDstIpv4AddressControl_Type = TruthValue
_F3L3AclRuleDstIpv4AddressControl_Object = MibTableColumn
f3L3AclRuleDstIpv4AddressControl = _F3L3AclRuleDstIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 7),
    _F3L3AclRuleDstIpv4AddressControl_Type()
)
f3L3AclRuleDstIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpv4AddressControl.setStatus("current")
_F3L3AclRuleDstIpv4AddressLowLimit_Type = IpAddress
_F3L3AclRuleDstIpv4AddressLowLimit_Object = MibTableColumn
f3L3AclRuleDstIpv4AddressLowLimit = _F3L3AclRuleDstIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 8),
    _F3L3AclRuleDstIpv4AddressLowLimit_Type()
)
f3L3AclRuleDstIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpv4AddressLowLimit.setStatus("current")
_F3L3AclRuleIpv4PriorityControl_Type = TruthValue
_F3L3AclRuleIpv4PriorityControl_Object = MibTableColumn
f3L3AclRuleIpv4PriorityControl = _F3L3AclRuleIpv4PriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 9),
    _F3L3AclRuleIpv4PriorityControl_Type()
)
f3L3AclRuleIpv4PriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpv4PriorityControl.setStatus("current")
_F3L3AclRuleIpv4PriorityLowLimit_Type = Integer32
_F3L3AclRuleIpv4PriorityLowLimit_Object = MibTableColumn
f3L3AclRuleIpv4PriorityLowLimit = _F3L3AclRuleIpv4PriorityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 10),
    _F3L3AclRuleIpv4PriorityLowLimit_Type()
)
f3L3AclRuleIpv4PriorityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpv4PriorityLowLimit.setStatus("current")
_F3L3AclRuleProtocolControl_Type = TruthValue
_F3L3AclRuleProtocolControl_Object = MibTableColumn
f3L3AclRuleProtocolControl = _F3L3AclRuleProtocolControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 11),
    _F3L3AclRuleProtocolControl_Type()
)
f3L3AclRuleProtocolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleProtocolControl.setStatus("current")
_F3L3AclRuleProtocolNumber_Type = Integer32
_F3L3AclRuleProtocolNumber_Object = MibTableColumn
f3L3AclRuleProtocolNumber = _F3L3AclRuleProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 12),
    _F3L3AclRuleProtocolNumber_Type()
)
f3L3AclRuleProtocolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleProtocolNumber.setStatus("current")
_F3L3AclRuleSrcPortControl_Type = TruthValue
_F3L3AclRuleSrcPortControl_Object = MibTableColumn
f3L3AclRuleSrcPortControl = _F3L3AclRuleSrcPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 13),
    _F3L3AclRuleSrcPortControl_Type()
)
f3L3AclRuleSrcPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcPortControl.setStatus("current")
_F3L3AclRuleSrcPortLowLimit_Type = Integer32
_F3L3AclRuleSrcPortLowLimit_Object = MibTableColumn
f3L3AclRuleSrcPortLowLimit = _F3L3AclRuleSrcPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 14),
    _F3L3AclRuleSrcPortLowLimit_Type()
)
f3L3AclRuleSrcPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcPortLowLimit.setStatus("current")
_F3L3AclRuleSrcPortHighLimit_Type = Integer32
_F3L3AclRuleSrcPortHighLimit_Object = MibTableColumn
f3L3AclRuleSrcPortHighLimit = _F3L3AclRuleSrcPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 15),
    _F3L3AclRuleSrcPortHighLimit_Type()
)
f3L3AclRuleSrcPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcPortHighLimit.setStatus("current")
_F3L3AclRuleDstPortControl_Type = TruthValue
_F3L3AclRuleDstPortControl_Object = MibTableColumn
f3L3AclRuleDstPortControl = _F3L3AclRuleDstPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 16),
    _F3L3AclRuleDstPortControl_Type()
)
f3L3AclRuleDstPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstPortControl.setStatus("current")
_F3L3AclRuleDstPortLowLimit_Type = Integer32
_F3L3AclRuleDstPortLowLimit_Object = MibTableColumn
f3L3AclRuleDstPortLowLimit = _F3L3AclRuleDstPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 17),
    _F3L3AclRuleDstPortLowLimit_Type()
)
f3L3AclRuleDstPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstPortLowLimit.setStatus("current")
_F3L3AclRuleDstPortHighLimit_Type = Integer32
_F3L3AclRuleDstPortHighLimit_Object = MibTableColumn
f3L3AclRuleDstPortHighLimit = _F3L3AclRuleDstPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 18),
    _F3L3AclRuleDstPortHighLimit_Type()
)
f3L3AclRuleDstPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstPortHighLimit.setStatus("current")
_F3L3AclRulePriority_Type = Integer32
_F3L3AclRulePriority_Object = MibTableColumn
f3L3AclRulePriority = _F3L3AclRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 19),
    _F3L3AclRulePriority_Type()
)
f3L3AclRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRulePriority.setStatus("current")
_F3L3AclRuleCOS_Type = Integer32
_F3L3AclRuleCOS_Object = MibTableColumn
f3L3AclRuleCOS = _F3L3AclRuleCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 20),
    _F3L3AclRuleCOS_Type()
)
f3L3AclRuleCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleCOS.setStatus("current")
_F3L3AclRuleOperation_Type = L3AclRuleOperation
_F3L3AclRuleOperation_Object = MibTableColumn
f3L3AclRuleOperation = _F3L3AclRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 21),
    _F3L3AclRuleOperation_Type()
)
f3L3AclRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOperation.setStatus("current")
_F3L3AclRuleSummary_Type = F3DisplayString
_F3L3AclRuleSummary_Object = MibTableColumn
f3L3AclRuleSummary = _F3L3AclRuleSummary_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 22),
    _F3L3AclRuleSummary_Type()
)
f3L3AclRuleSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleSummary.setStatus("current")
_F3L3AclRuleCosOverrideControl_Type = TruthValue
_F3L3AclRuleCosOverrideControl_Object = MibTableColumn
f3L3AclRuleCosOverrideControl = _F3L3AclRuleCosOverrideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 23),
    _F3L3AclRuleCosOverrideControl_Type()
)
f3L3AclRuleCosOverrideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleCosOverrideControl.setStatus("current")
_F3L3AclRuleSrcMacAddressControl_Type = TruthValue
_F3L3AclRuleSrcMacAddressControl_Object = MibTableColumn
f3L3AclRuleSrcMacAddressControl = _F3L3AclRuleSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 24),
    _F3L3AclRuleSrcMacAddressControl_Type()
)
f3L3AclRuleSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcMacAddressControl.setStatus("current")
_F3L3AclRuleDynamicSrcMacAddressControl_Type = TruthValue
_F3L3AclRuleDynamicSrcMacAddressControl_Object = MibTableColumn
f3L3AclRuleDynamicSrcMacAddressControl = _F3L3AclRuleDynamicSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 25),
    _F3L3AclRuleDynamicSrcMacAddressControl_Type()
)
f3L3AclRuleDynamicSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDynamicSrcMacAddressControl.setStatus("current")
_F3L3AclRuleSrcMacAddress_Type = MacAddress
_F3L3AclRuleSrcMacAddress_Object = MibTableColumn
f3L3AclRuleSrcMacAddress = _F3L3AclRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 26),
    _F3L3AclRuleSrcMacAddress_Type()
)
f3L3AclRuleSrcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcMacAddress.setStatus("current")
_F3L3AclRuleSrcMacAddressMask_Type = MacAddress
_F3L3AclRuleSrcMacAddressMask_Object = MibTableColumn
f3L3AclRuleSrcMacAddressMask = _F3L3AclRuleSrcMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 27),
    _F3L3AclRuleSrcMacAddressMask_Type()
)
f3L3AclRuleSrcMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcMacAddressMask.setStatus("current")
_F3L3AclRuleDstMacAddressControl_Type = TruthValue
_F3L3AclRuleDstMacAddressControl_Object = MibTableColumn
f3L3AclRuleDstMacAddressControl = _F3L3AclRuleDstMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 28),
    _F3L3AclRuleDstMacAddressControl_Type()
)
f3L3AclRuleDstMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstMacAddressControl.setStatus("current")
_F3L3AclRuleDstMacAddress_Type = MacAddress
_F3L3AclRuleDstMacAddress_Object = MibTableColumn
f3L3AclRuleDstMacAddress = _F3L3AclRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 29),
    _F3L3AclRuleDstMacAddress_Type()
)
f3L3AclRuleDstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstMacAddress.setStatus("current")
_F3L3AclRuleDstMacAddressMask_Type = MacAddress
_F3L3AclRuleDstMacAddressMask_Object = MibTableColumn
f3L3AclRuleDstMacAddressMask = _F3L3AclRuleDstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 30),
    _F3L3AclRuleDstMacAddressMask_Type()
)
f3L3AclRuleDstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstMacAddressMask.setStatus("current")
_F3L3AclRuleOuterVlanVIDControl_Type = TruthValue
_F3L3AclRuleOuterVlanVIDControl_Object = MibTableColumn
f3L3AclRuleOuterVlanVIDControl = _F3L3AclRuleOuterVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 31),
    _F3L3AclRuleOuterVlanVIDControl_Type()
)
f3L3AclRuleOuterVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanVIDControl.setStatus("current")
_F3L3AclRuleOuterVlanVIDLowLimit_Type = VlanId
_F3L3AclRuleOuterVlanVIDLowLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanVIDLowLimit = _F3L3AclRuleOuterVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 32),
    _F3L3AclRuleOuterVlanVIDLowLimit_Type()
)
f3L3AclRuleOuterVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanVIDLowLimit.setStatus("current")
_F3L3AclRuleOuterVlanVIDHighLimit_Type = VlanId
_F3L3AclRuleOuterVlanVIDHighLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanVIDHighLimit = _F3L3AclRuleOuterVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 33),
    _F3L3AclRuleOuterVlanVIDHighLimit_Type()
)
f3L3AclRuleOuterVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanVIDHighLimit.setStatus("current")
_F3L3AclRuleInnerVlanVIDControl_Type = TruthValue
_F3L3AclRuleInnerVlanVIDControl_Object = MibTableColumn
f3L3AclRuleInnerVlanVIDControl = _F3L3AclRuleInnerVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 34),
    _F3L3AclRuleInnerVlanVIDControl_Type()
)
f3L3AclRuleInnerVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanVIDControl.setStatus("current")
_F3L3AclRuleInnerVlanVIDLowLimit_Type = VlanId
_F3L3AclRuleInnerVlanVIDLowLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanVIDLowLimit = _F3L3AclRuleInnerVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 35),
    _F3L3AclRuleInnerVlanVIDLowLimit_Type()
)
f3L3AclRuleInnerVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanVIDLowLimit.setStatus("current")
_F3L3AclRuleInnerVlanVIDHighLimit_Type = VlanId
_F3L3AclRuleInnerVlanVIDHighLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanVIDHighLimit = _F3L3AclRuleInnerVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 36),
    _F3L3AclRuleInnerVlanVIDHighLimit_Type()
)
f3L3AclRuleInnerVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanVIDHighLimit.setStatus("current")
_F3L3AclRuleOuterVlanPcpControl_Type = TruthValue
_F3L3AclRuleOuterVlanPcpControl_Object = MibTableColumn
f3L3AclRuleOuterVlanPcpControl = _F3L3AclRuleOuterVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 37),
    _F3L3AclRuleOuterVlanPcpControl_Type()
)
f3L3AclRuleOuterVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanPcpControl.setStatus("current")
_F3L3AclRuleOuterVlanPcpLowLimit_Type = VlanPriority
_F3L3AclRuleOuterVlanPcpLowLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanPcpLowLimit = _F3L3AclRuleOuterVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 38),
    _F3L3AclRuleOuterVlanPcpLowLimit_Type()
)
f3L3AclRuleOuterVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanPcpLowLimit.setStatus("current")
_F3L3AclRuleOuterVlanPcpHighLimit_Type = VlanPriority
_F3L3AclRuleOuterVlanPcpHighLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanPcpHighLimit = _F3L3AclRuleOuterVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 39),
    _F3L3AclRuleOuterVlanPcpHighLimit_Type()
)
f3L3AclRuleOuterVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanPcpHighLimit.setStatus("current")
_F3L3AclRuleInnerVlanPcpControl_Type = TruthValue
_F3L3AclRuleInnerVlanPcpControl_Object = MibTableColumn
f3L3AclRuleInnerVlanPcpControl = _F3L3AclRuleInnerVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 40),
    _F3L3AclRuleInnerVlanPcpControl_Type()
)
f3L3AclRuleInnerVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanPcpControl.setStatus("current")
_F3L3AclRuleInnerVlanPcpLowLimit_Type = VlanPriority
_F3L3AclRuleInnerVlanPcpLowLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanPcpLowLimit = _F3L3AclRuleInnerVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 41),
    _F3L3AclRuleInnerVlanPcpLowLimit_Type()
)
f3L3AclRuleInnerVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanPcpLowLimit.setStatus("current")
_F3L3AclRuleInnerVlanPcpHighLimit_Type = VlanPriority
_F3L3AclRuleInnerVlanPcpHighLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanPcpHighLimit = _F3L3AclRuleInnerVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 42),
    _F3L3AclRuleInnerVlanPcpHighLimit_Type()
)
f3L3AclRuleInnerVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanPcpHighLimit.setStatus("current")
_F3L3AclRuleOuterVlanDeiControl_Type = TruthValue
_F3L3AclRuleOuterVlanDeiControl_Object = MibTableColumn
f3L3AclRuleOuterVlanDeiControl = _F3L3AclRuleOuterVlanDeiControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 43),
    _F3L3AclRuleOuterVlanDeiControl_Type()
)
f3L3AclRuleOuterVlanDeiControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanDeiControl.setStatus("current")


class _F3L3AclRuleOuterVlanDei_Type(Unsigned32):
    """Custom type f3L3AclRuleOuterVlanDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3L3AclRuleOuterVlanDei_Type.__name__ = "Unsigned32"
_F3L3AclRuleOuterVlanDei_Object = MibTableColumn
f3L3AclRuleOuterVlanDei = _F3L3AclRuleOuterVlanDei_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 44),
    _F3L3AclRuleOuterVlanDei_Type()
)
f3L3AclRuleOuterVlanDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanDei.setStatus("current")
_F3L3AclRuleEtherTypeControl_Type = TruthValue
_F3L3AclRuleEtherTypeControl_Object = MibTableColumn
f3L3AclRuleEtherTypeControl = _F3L3AclRuleEtherTypeControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 45),
    _F3L3AclRuleEtherTypeControl_Type()
)
f3L3AclRuleEtherTypeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleEtherTypeControl.setStatus("current")
_F3L3AclRuleEtherType_Type = Integer32
_F3L3AclRuleEtherType_Object = MibTableColumn
f3L3AclRuleEtherType = _F3L3AclRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 46),
    _F3L3AclRuleEtherType_Type()
)
f3L3AclRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleEtherType.setStatus("current")
_F3L3AclRuleTcpFlagsControl_Type = TruthValue
_F3L3AclRuleTcpFlagsControl_Object = MibTableColumn
f3L3AclRuleTcpFlagsControl = _F3L3AclRuleTcpFlagsControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 47),
    _F3L3AclRuleTcpFlagsControl_Type()
)
f3L3AclRuleTcpFlagsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleTcpFlagsControl.setStatus("current")
_F3L3AclRuleTcpFlags_Type = Integer32
_F3L3AclRuleTcpFlags_Object = MibTableColumn
f3L3AclRuleTcpFlags = _F3L3AclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 48),
    _F3L3AclRuleTcpFlags_Type()
)
f3L3AclRuleTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleTcpFlags.setStatus("current")
_F3L3AclRuleSrcIpv4AddressHighLimit_Type = IpAddress
_F3L3AclRuleSrcIpv4AddressHighLimit_Object = MibTableColumn
f3L3AclRuleSrcIpv4AddressHighLimit = _F3L3AclRuleSrcIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 49),
    _F3L3AclRuleSrcIpv4AddressHighLimit_Type()
)
f3L3AclRuleSrcIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpv4AddressHighLimit.setStatus("current")
_F3L3AclRuleDstIpv4AddressHighLimit_Type = IpAddress
_F3L3AclRuleDstIpv4AddressHighLimit_Object = MibTableColumn
f3L3AclRuleDstIpv4AddressHighLimit = _F3L3AclRuleDstIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 50),
    _F3L3AclRuleDstIpv4AddressHighLimit_Type()
)
f3L3AclRuleDstIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpv4AddressHighLimit.setStatus("current")
_F3L3AclRuleIpv4PriorityHighLimit_Type = Integer32
_F3L3AclRuleIpv4PriorityHighLimit_Object = MibTableColumn
f3L3AclRuleIpv4PriorityHighLimit = _F3L3AclRuleIpv4PriorityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 51),
    _F3L3AclRuleIpv4PriorityHighLimit_Type()
)
f3L3AclRuleIpv4PriorityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpv4PriorityHighLimit.setStatus("current")
_F3L3AclRuleStorageType_Type = StorageType
_F3L3AclRuleStorageType_Object = MibTableColumn
f3L3AclRuleStorageType = _F3L3AclRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 52),
    _F3L3AclRuleStorageType_Type()
)
f3L3AclRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3AclRuleStorageType.setStatus("current")
_F3L3AclRuleRowStatus_Type = RowStatus
_F3L3AclRuleRowStatus_Object = MibTableColumn
f3L3AclRuleRowStatus = _F3L3AclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 53),
    _F3L3AclRuleRowStatus_Type()
)
f3L3AclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3AclRuleRowStatus.setStatus("current")
_F3L3AclRuleAdminState_Type = AdminState
_F3L3AclRuleAdminState_Object = MibTableColumn
f3L3AclRuleAdminState = _F3L3AclRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 54),
    _F3L3AclRuleAdminState_Type()
)
f3L3AclRuleAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleAdminState.setStatus("current")
_F3L2A2NAclRuleTable_Object = MibTable
f3L2A2NAclRuleTable = _F3L2A2NAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleTable.setStatus("current")
_F3L2A2NAclRuleEntry_Object = MibTableRow
f3L2A2NAclRuleEntry = _F3L2A2NAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1)
)
f3L2A2NAclRuleEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleEntry.setStatus("current")
_F3L2A2NAclRuleParentIndex_Type = Integer32
_F3L2A2NAclRuleParentIndex_Object = MibTableColumn
f3L2A2NAclRuleParentIndex = _F3L2A2NAclRuleParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 1),
    _F3L2A2NAclRuleParentIndex_Type()
)
f3L2A2NAclRuleParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleParentIndex.setStatus("current")
_F3L2A2NAclRuleIndex_Type = Integer32
_F3L2A2NAclRuleIndex_Object = MibTableColumn
f3L2A2NAclRuleIndex = _F3L2A2NAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 2),
    _F3L2A2NAclRuleIndex_Type()
)
f3L2A2NAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIndex.setStatus("current")


class _F3L2A2NAclRuleAlias_Type(F3DisplayString):
    """Custom type f3L2A2NAclRuleAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L2A2NAclRuleAlias_Type.__name__ = "F3DisplayString"
_F3L2A2NAclRuleAlias_Object = MibTableColumn
f3L2A2NAclRuleAlias = _F3L2A2NAclRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 3),
    _F3L2A2NAclRuleAlias_Type()
)
f3L2A2NAclRuleAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleAlias.setStatus("current")
_F3L2A2NAclRuleSrcIpv4AddressControl_Type = TruthValue
_F3L2A2NAclRuleSrcIpv4AddressControl_Object = MibTableColumn
f3L2A2NAclRuleSrcIpv4AddressControl = _F3L2A2NAclRuleSrcIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 4),
    _F3L2A2NAclRuleSrcIpv4AddressControl_Type()
)
f3L2A2NAclRuleSrcIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpv4AddressControl.setStatus("current")
_F3L2A2NAclRuleDynamicSrcIpControl_Type = TruthValue
_F3L2A2NAclRuleDynamicSrcIpControl_Object = MibTableColumn
f3L2A2NAclRuleDynamicSrcIpControl = _F3L2A2NAclRuleDynamicSrcIpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 5),
    _F3L2A2NAclRuleDynamicSrcIpControl_Type()
)
f3L2A2NAclRuleDynamicSrcIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDynamicSrcIpControl.setStatus("current")
_F3L2A2NAclRuleSrcIpv4AddressLowLimit_Type = IpAddress
_F3L2A2NAclRuleSrcIpv4AddressLowLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcIpv4AddressLowLimit = _F3L2A2NAclRuleSrcIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 6),
    _F3L2A2NAclRuleSrcIpv4AddressLowLimit_Type()
)
f3L2A2NAclRuleSrcIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpv4AddressLowLimit.setStatus("current")
_F3L2A2NAclRuleDstIpv4AddressControl_Type = TruthValue
_F3L2A2NAclRuleDstIpv4AddressControl_Object = MibTableColumn
f3L2A2NAclRuleDstIpv4AddressControl = _F3L2A2NAclRuleDstIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 7),
    _F3L2A2NAclRuleDstIpv4AddressControl_Type()
)
f3L2A2NAclRuleDstIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpv4AddressControl.setStatus("current")
_F3L2A2NAclRuleDstIpv4AddressLowLimit_Type = IpAddress
_F3L2A2NAclRuleDstIpv4AddressLowLimit_Object = MibTableColumn
f3L2A2NAclRuleDstIpv4AddressLowLimit = _F3L2A2NAclRuleDstIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 8),
    _F3L2A2NAclRuleDstIpv4AddressLowLimit_Type()
)
f3L2A2NAclRuleDstIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpv4AddressLowLimit.setStatus("current")
_F3L2A2NAclRuleIpv4PriorityControl_Type = TruthValue
_F3L2A2NAclRuleIpv4PriorityControl_Object = MibTableColumn
f3L2A2NAclRuleIpv4PriorityControl = _F3L2A2NAclRuleIpv4PriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 9),
    _F3L2A2NAclRuleIpv4PriorityControl_Type()
)
f3L2A2NAclRuleIpv4PriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpv4PriorityControl.setStatus("current")
_F3L2A2NAclRuleIpv4PriorityLowLimit_Type = Integer32
_F3L2A2NAclRuleIpv4PriorityLowLimit_Object = MibTableColumn
f3L2A2NAclRuleIpv4PriorityLowLimit = _F3L2A2NAclRuleIpv4PriorityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 10),
    _F3L2A2NAclRuleIpv4PriorityLowLimit_Type()
)
f3L2A2NAclRuleIpv4PriorityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpv4PriorityLowLimit.setStatus("current")
_F3L2A2NAclRuleProtocolControl_Type = TruthValue
_F3L2A2NAclRuleProtocolControl_Object = MibTableColumn
f3L2A2NAclRuleProtocolControl = _F3L2A2NAclRuleProtocolControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 11),
    _F3L2A2NAclRuleProtocolControl_Type()
)
f3L2A2NAclRuleProtocolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleProtocolControl.setStatus("current")
_F3L2A2NAclRuleProtocolNumber_Type = Integer32
_F3L2A2NAclRuleProtocolNumber_Object = MibTableColumn
f3L2A2NAclRuleProtocolNumber = _F3L2A2NAclRuleProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 12),
    _F3L2A2NAclRuleProtocolNumber_Type()
)
f3L2A2NAclRuleProtocolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleProtocolNumber.setStatus("current")
_F3L2A2NAclRuleSrcPortControl_Type = TruthValue
_F3L2A2NAclRuleSrcPortControl_Object = MibTableColumn
f3L2A2NAclRuleSrcPortControl = _F3L2A2NAclRuleSrcPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 13),
    _F3L2A2NAclRuleSrcPortControl_Type()
)
f3L2A2NAclRuleSrcPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcPortControl.setStatus("current")
_F3L2A2NAclRuleSrcPortLowLimit_Type = Integer32
_F3L2A2NAclRuleSrcPortLowLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcPortLowLimit = _F3L2A2NAclRuleSrcPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 14),
    _F3L2A2NAclRuleSrcPortLowLimit_Type()
)
f3L2A2NAclRuleSrcPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcPortLowLimit.setStatus("current")
_F3L2A2NAclRuleSrcPortHighLimit_Type = Integer32
_F3L2A2NAclRuleSrcPortHighLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcPortHighLimit = _F3L2A2NAclRuleSrcPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 15),
    _F3L2A2NAclRuleSrcPortHighLimit_Type()
)
f3L2A2NAclRuleSrcPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcPortHighLimit.setStatus("current")
_F3L2A2NAclRuleDstPortControl_Type = TruthValue
_F3L2A2NAclRuleDstPortControl_Object = MibTableColumn
f3L2A2NAclRuleDstPortControl = _F3L2A2NAclRuleDstPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 16),
    _F3L2A2NAclRuleDstPortControl_Type()
)
f3L2A2NAclRuleDstPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstPortControl.setStatus("current")
_F3L2A2NAclRuleDstPortLowLimit_Type = Integer32
_F3L2A2NAclRuleDstPortLowLimit_Object = MibTableColumn
f3L2A2NAclRuleDstPortLowLimit = _F3L2A2NAclRuleDstPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 17),
    _F3L2A2NAclRuleDstPortLowLimit_Type()
)
f3L2A2NAclRuleDstPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstPortLowLimit.setStatus("current")
_F3L2A2NAclRuleDstPortHighLimit_Type = Integer32
_F3L2A2NAclRuleDstPortHighLimit_Object = MibTableColumn
f3L2A2NAclRuleDstPortHighLimit = _F3L2A2NAclRuleDstPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 18),
    _F3L2A2NAclRuleDstPortHighLimit_Type()
)
f3L2A2NAclRuleDstPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstPortHighLimit.setStatus("current")
_F3L2A2NAclRulePriority_Type = Integer32
_F3L2A2NAclRulePriority_Object = MibTableColumn
f3L2A2NAclRulePriority = _F3L2A2NAclRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 19),
    _F3L2A2NAclRulePriority_Type()
)
f3L2A2NAclRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRulePriority.setStatus("current")
_F3L2A2NAclRuleCOS_Type = Integer32
_F3L2A2NAclRuleCOS_Object = MibTableColumn
f3L2A2NAclRuleCOS = _F3L2A2NAclRuleCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 20),
    _F3L2A2NAclRuleCOS_Type()
)
f3L2A2NAclRuleCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleCOS.setStatus("current")
_F3L2A2NAclRuleOperation_Type = L3AclRuleOperation
_F3L2A2NAclRuleOperation_Object = MibTableColumn
f3L2A2NAclRuleOperation = _F3L2A2NAclRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 21),
    _F3L2A2NAclRuleOperation_Type()
)
f3L2A2NAclRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOperation.setStatus("current")
_F3L2A2NAclRuleSummary_Type = F3DisplayString
_F3L2A2NAclRuleSummary_Object = MibTableColumn
f3L2A2NAclRuleSummary = _F3L2A2NAclRuleSummary_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 22),
    _F3L2A2NAclRuleSummary_Type()
)
f3L2A2NAclRuleSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSummary.setStatus("current")
_F3L2A2NAclRuleCosOverrideControl_Type = TruthValue
_F3L2A2NAclRuleCosOverrideControl_Object = MibTableColumn
f3L2A2NAclRuleCosOverrideControl = _F3L2A2NAclRuleCosOverrideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 23),
    _F3L2A2NAclRuleCosOverrideControl_Type()
)
f3L2A2NAclRuleCosOverrideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleCosOverrideControl.setStatus("current")
_F3L2A2NAclRuleSrcMacAddressControl_Type = TruthValue
_F3L2A2NAclRuleSrcMacAddressControl_Object = MibTableColumn
f3L2A2NAclRuleSrcMacAddressControl = _F3L2A2NAclRuleSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 24),
    _F3L2A2NAclRuleSrcMacAddressControl_Type()
)
f3L2A2NAclRuleSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcMacAddressControl.setStatus("current")
_F3L2A2NAclRuleDynamicSrcMacAddressControl_Type = TruthValue
_F3L2A2NAclRuleDynamicSrcMacAddressControl_Object = MibTableColumn
f3L2A2NAclRuleDynamicSrcMacAddressControl = _F3L2A2NAclRuleDynamicSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 25),
    _F3L2A2NAclRuleDynamicSrcMacAddressControl_Type()
)
f3L2A2NAclRuleDynamicSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDynamicSrcMacAddressControl.setStatus("current")
_F3L2A2NAclRuleSrcMacAddress_Type = MacAddress
_F3L2A2NAclRuleSrcMacAddress_Object = MibTableColumn
f3L2A2NAclRuleSrcMacAddress = _F3L2A2NAclRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 26),
    _F3L2A2NAclRuleSrcMacAddress_Type()
)
f3L2A2NAclRuleSrcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcMacAddress.setStatus("current")
_F3L2A2NAclRuleSrcMacAddressMask_Type = MacAddress
_F3L2A2NAclRuleSrcMacAddressMask_Object = MibTableColumn
f3L2A2NAclRuleSrcMacAddressMask = _F3L2A2NAclRuleSrcMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 27),
    _F3L2A2NAclRuleSrcMacAddressMask_Type()
)
f3L2A2NAclRuleSrcMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcMacAddressMask.setStatus("current")
_F3L2A2NAclRuleDstMacAddressControl_Type = TruthValue
_F3L2A2NAclRuleDstMacAddressControl_Object = MibTableColumn
f3L2A2NAclRuleDstMacAddressControl = _F3L2A2NAclRuleDstMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 28),
    _F3L2A2NAclRuleDstMacAddressControl_Type()
)
f3L2A2NAclRuleDstMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstMacAddressControl.setStatus("current")
_F3L2A2NAclRuleDstMacAddress_Type = MacAddress
_F3L2A2NAclRuleDstMacAddress_Object = MibTableColumn
f3L2A2NAclRuleDstMacAddress = _F3L2A2NAclRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 29),
    _F3L2A2NAclRuleDstMacAddress_Type()
)
f3L2A2NAclRuleDstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstMacAddress.setStatus("current")
_F3L2A2NAclRuleDstMacAddressMask_Type = MacAddress
_F3L2A2NAclRuleDstMacAddressMask_Object = MibTableColumn
f3L2A2NAclRuleDstMacAddressMask = _F3L2A2NAclRuleDstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 30),
    _F3L2A2NAclRuleDstMacAddressMask_Type()
)
f3L2A2NAclRuleDstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstMacAddressMask.setStatus("current")
_F3L2A2NAclRuleOuterVlanVIDControl_Type = TruthValue
_F3L2A2NAclRuleOuterVlanVIDControl_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanVIDControl = _F3L2A2NAclRuleOuterVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 31),
    _F3L2A2NAclRuleOuterVlanVIDControl_Type()
)
f3L2A2NAclRuleOuterVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanVIDControl.setStatus("current")
_F3L2A2NAclRuleOuterVlanVIDLowLimit_Type = VlanId
_F3L2A2NAclRuleOuterVlanVIDLowLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanVIDLowLimit = _F3L2A2NAclRuleOuterVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 32),
    _F3L2A2NAclRuleOuterVlanVIDLowLimit_Type()
)
f3L2A2NAclRuleOuterVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanVIDLowLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanVIDHighLimit_Type = VlanId
_F3L2A2NAclRuleOuterVlanVIDHighLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanVIDHighLimit = _F3L2A2NAclRuleOuterVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 33),
    _F3L2A2NAclRuleOuterVlanVIDHighLimit_Type()
)
f3L2A2NAclRuleOuterVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanVIDHighLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanVIDControl_Type = TruthValue
_F3L2A2NAclRuleInnerVlanVIDControl_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanVIDControl = _F3L2A2NAclRuleInnerVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 34),
    _F3L2A2NAclRuleInnerVlanVIDControl_Type()
)
f3L2A2NAclRuleInnerVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanVIDControl.setStatus("current")
_F3L2A2NAclRuleInnerVlanVIDLowLimit_Type = VlanId
_F3L2A2NAclRuleInnerVlanVIDLowLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanVIDLowLimit = _F3L2A2NAclRuleInnerVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 35),
    _F3L2A2NAclRuleInnerVlanVIDLowLimit_Type()
)
f3L2A2NAclRuleInnerVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanVIDLowLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanVIDHighLimit_Type = VlanId
_F3L2A2NAclRuleInnerVlanVIDHighLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanVIDHighLimit = _F3L2A2NAclRuleInnerVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 36),
    _F3L2A2NAclRuleInnerVlanVIDHighLimit_Type()
)
f3L2A2NAclRuleInnerVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanVIDHighLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanPcpControl_Type = TruthValue
_F3L2A2NAclRuleOuterVlanPcpControl_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanPcpControl = _F3L2A2NAclRuleOuterVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 37),
    _F3L2A2NAclRuleOuterVlanPcpControl_Type()
)
f3L2A2NAclRuleOuterVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanPcpControl.setStatus("current")
_F3L2A2NAclRuleOuterVlanPcpLowLimit_Type = VlanPriority
_F3L2A2NAclRuleOuterVlanPcpLowLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanPcpLowLimit = _F3L2A2NAclRuleOuterVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 38),
    _F3L2A2NAclRuleOuterVlanPcpLowLimit_Type()
)
f3L2A2NAclRuleOuterVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanPcpLowLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanPcpHighLimit_Type = VlanPriority
_F3L2A2NAclRuleOuterVlanPcpHighLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanPcpHighLimit = _F3L2A2NAclRuleOuterVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 39),
    _F3L2A2NAclRuleOuterVlanPcpHighLimit_Type()
)
f3L2A2NAclRuleOuterVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanPcpHighLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanPcpControl_Type = TruthValue
_F3L2A2NAclRuleInnerVlanPcpControl_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanPcpControl = _F3L2A2NAclRuleInnerVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 40),
    _F3L2A2NAclRuleInnerVlanPcpControl_Type()
)
f3L2A2NAclRuleInnerVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanPcpControl.setStatus("current")
_F3L2A2NAclRuleInnerVlanPcpLowLimit_Type = VlanPriority
_F3L2A2NAclRuleInnerVlanPcpLowLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanPcpLowLimit = _F3L2A2NAclRuleInnerVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 41),
    _F3L2A2NAclRuleInnerVlanPcpLowLimit_Type()
)
f3L2A2NAclRuleInnerVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanPcpLowLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanPcpHighLimit_Type = VlanPriority
_F3L2A2NAclRuleInnerVlanPcpHighLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanPcpHighLimit = _F3L2A2NAclRuleInnerVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 42),
    _F3L2A2NAclRuleInnerVlanPcpHighLimit_Type()
)
f3L2A2NAclRuleInnerVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanPcpHighLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanDeiControl_Type = TruthValue
_F3L2A2NAclRuleOuterVlanDeiControl_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanDeiControl = _F3L2A2NAclRuleOuterVlanDeiControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 43),
    _F3L2A2NAclRuleOuterVlanDeiControl_Type()
)
f3L2A2NAclRuleOuterVlanDeiControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanDeiControl.setStatus("current")


class _F3L2A2NAclRuleOuterVlanDei_Type(Unsigned32):
    """Custom type f3L2A2NAclRuleOuterVlanDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3L2A2NAclRuleOuterVlanDei_Type.__name__ = "Unsigned32"
_F3L2A2NAclRuleOuterVlanDei_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanDei = _F3L2A2NAclRuleOuterVlanDei_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 44),
    _F3L2A2NAclRuleOuterVlanDei_Type()
)
f3L2A2NAclRuleOuterVlanDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanDei.setStatus("current")
_F3L2A2NAclRuleEtherTypeControl_Type = TruthValue
_F3L2A2NAclRuleEtherTypeControl_Object = MibTableColumn
f3L2A2NAclRuleEtherTypeControl = _F3L2A2NAclRuleEtherTypeControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 45),
    _F3L2A2NAclRuleEtherTypeControl_Type()
)
f3L2A2NAclRuleEtherTypeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleEtherTypeControl.setStatus("current")
_F3L2A2NAclRuleEtherType_Type = Integer32
_F3L2A2NAclRuleEtherType_Object = MibTableColumn
f3L2A2NAclRuleEtherType = _F3L2A2NAclRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 46),
    _F3L2A2NAclRuleEtherType_Type()
)
f3L2A2NAclRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleEtherType.setStatus("current")
_F3L2A2NAclRuleTcpFlagsControl_Type = TruthValue
_F3L2A2NAclRuleTcpFlagsControl_Object = MibTableColumn
f3L2A2NAclRuleTcpFlagsControl = _F3L2A2NAclRuleTcpFlagsControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 47),
    _F3L2A2NAclRuleTcpFlagsControl_Type()
)
f3L2A2NAclRuleTcpFlagsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleTcpFlagsControl.setStatus("current")
_F3L2A2NAclRuleTcpFlags_Type = Integer32
_F3L2A2NAclRuleTcpFlags_Object = MibTableColumn
f3L2A2NAclRuleTcpFlags = _F3L2A2NAclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 48),
    _F3L2A2NAclRuleTcpFlags_Type()
)
f3L2A2NAclRuleTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleTcpFlags.setStatus("current")
_F3L2A2NAclRuleSrcIpv4AddressHighLimit_Type = IpAddress
_F3L2A2NAclRuleSrcIpv4AddressHighLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcIpv4AddressHighLimit = _F3L2A2NAclRuleSrcIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 49),
    _F3L2A2NAclRuleSrcIpv4AddressHighLimit_Type()
)
f3L2A2NAclRuleSrcIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpv4AddressHighLimit.setStatus("current")
_F3L2A2NAclRuleDstIpv4AddressHighLimit_Type = IpAddress
_F3L2A2NAclRuleDstIpv4AddressHighLimit_Object = MibTableColumn
f3L2A2NAclRuleDstIpv4AddressHighLimit = _F3L2A2NAclRuleDstIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 50),
    _F3L2A2NAclRuleDstIpv4AddressHighLimit_Type()
)
f3L2A2NAclRuleDstIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpv4AddressHighLimit.setStatus("current")
_F3L2A2NAclRuleIpv4PriorityHighLimit_Type = Integer32
_F3L2A2NAclRuleIpv4PriorityHighLimit_Object = MibTableColumn
f3L2A2NAclRuleIpv4PriorityHighLimit = _F3L2A2NAclRuleIpv4PriorityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 51),
    _F3L2A2NAclRuleIpv4PriorityHighLimit_Type()
)
f3L2A2NAclRuleIpv4PriorityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpv4PriorityHighLimit.setStatus("current")
_F3L2A2NAclRuleStorageType_Type = StorageType
_F3L2A2NAclRuleStorageType_Object = MibTableColumn
f3L2A2NAclRuleStorageType = _F3L2A2NAclRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 52),
    _F3L2A2NAclRuleStorageType_Type()
)
f3L2A2NAclRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStorageType.setStatus("current")
_F3L2A2NAclRuleRowStatus_Type = RowStatus
_F3L2A2NAclRuleRowStatus_Object = MibTableColumn
f3L2A2NAclRuleRowStatus = _F3L2A2NAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 53),
    _F3L2A2NAclRuleRowStatus_Type()
)
f3L2A2NAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleRowStatus.setStatus("current")
_F3L2A2NAclRuleAdminState_Type = AdminState
_F3L2A2NAclRuleAdminState_Object = MibTableColumn
f3L2A2NAclRuleAdminState = _F3L2A2NAclRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 54),
    _F3L2A2NAclRuleAdminState_Type()
)
f3L2A2NAclRuleAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleAdminState.setStatus("current")
_F3L2N2AAclRuleTable_Object = MibTable
f3L2N2AAclRuleTable = _F3L2N2AAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleTable.setStatus("current")
_F3L2N2AAclRuleEntry_Object = MibTableRow
f3L2N2AAclRuleEntry = _F3L2N2AAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1)
)
f3L2N2AAclRuleEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleEntry.setStatus("current")
_F3L2N2AAclRuleParentIndex_Type = Integer32
_F3L2N2AAclRuleParentIndex_Object = MibTableColumn
f3L2N2AAclRuleParentIndex = _F3L2N2AAclRuleParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 1),
    _F3L2N2AAclRuleParentIndex_Type()
)
f3L2N2AAclRuleParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleParentIndex.setStatus("current")
_F3L2N2AAclRuleIndex_Type = Integer32
_F3L2N2AAclRuleIndex_Object = MibTableColumn
f3L2N2AAclRuleIndex = _F3L2N2AAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 2),
    _F3L2N2AAclRuleIndex_Type()
)
f3L2N2AAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIndex.setStatus("current")


class _F3L2N2AAclRuleAlias_Type(F3DisplayString):
    """Custom type f3L2N2AAclRuleAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L2N2AAclRuleAlias_Type.__name__ = "F3DisplayString"
_F3L2N2AAclRuleAlias_Object = MibTableColumn
f3L2N2AAclRuleAlias = _F3L2N2AAclRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 3),
    _F3L2N2AAclRuleAlias_Type()
)
f3L2N2AAclRuleAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleAlias.setStatus("current")
_F3L2N2AAclRuleSrcIpv4AddressControl_Type = TruthValue
_F3L2N2AAclRuleSrcIpv4AddressControl_Object = MibTableColumn
f3L2N2AAclRuleSrcIpv4AddressControl = _F3L2N2AAclRuleSrcIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 4),
    _F3L2N2AAclRuleSrcIpv4AddressControl_Type()
)
f3L2N2AAclRuleSrcIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpv4AddressControl.setStatus("current")
_F3L2N2AAclRuleDynamicSrcIpControl_Type = TruthValue
_F3L2N2AAclRuleDynamicSrcIpControl_Object = MibTableColumn
f3L2N2AAclRuleDynamicSrcIpControl = _F3L2N2AAclRuleDynamicSrcIpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 5),
    _F3L2N2AAclRuleDynamicSrcIpControl_Type()
)
f3L2N2AAclRuleDynamicSrcIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDynamicSrcIpControl.setStatus("current")
_F3L2N2AAclRuleSrcIpv4AddressLowLimit_Type = IpAddress
_F3L2N2AAclRuleSrcIpv4AddressLowLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcIpv4AddressLowLimit = _F3L2N2AAclRuleSrcIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 6),
    _F3L2N2AAclRuleSrcIpv4AddressLowLimit_Type()
)
f3L2N2AAclRuleSrcIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpv4AddressLowLimit.setStatus("current")
_F3L2N2AAclRuleDstIpv4AddressControl_Type = TruthValue
_F3L2N2AAclRuleDstIpv4AddressControl_Object = MibTableColumn
f3L2N2AAclRuleDstIpv4AddressControl = _F3L2N2AAclRuleDstIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 7),
    _F3L2N2AAclRuleDstIpv4AddressControl_Type()
)
f3L2N2AAclRuleDstIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpv4AddressControl.setStatus("current")
_F3L2N2AAclRuleDstIpv4AddressLowLimit_Type = IpAddress
_F3L2N2AAclRuleDstIpv4AddressLowLimit_Object = MibTableColumn
f3L2N2AAclRuleDstIpv4AddressLowLimit = _F3L2N2AAclRuleDstIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 8),
    _F3L2N2AAclRuleDstIpv4AddressLowLimit_Type()
)
f3L2N2AAclRuleDstIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpv4AddressLowLimit.setStatus("current")
_F3L2N2AAclRuleIpv4PriorityControl_Type = TruthValue
_F3L2N2AAclRuleIpv4PriorityControl_Object = MibTableColumn
f3L2N2AAclRuleIpv4PriorityControl = _F3L2N2AAclRuleIpv4PriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 9),
    _F3L2N2AAclRuleIpv4PriorityControl_Type()
)
f3L2N2AAclRuleIpv4PriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpv4PriorityControl.setStatus("current")
_F3L2N2AAclRuleIpv4PriorityLowLimit_Type = Integer32
_F3L2N2AAclRuleIpv4PriorityLowLimit_Object = MibTableColumn
f3L2N2AAclRuleIpv4PriorityLowLimit = _F3L2N2AAclRuleIpv4PriorityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 10),
    _F3L2N2AAclRuleIpv4PriorityLowLimit_Type()
)
f3L2N2AAclRuleIpv4PriorityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpv4PriorityLowLimit.setStatus("current")
_F3L2N2AAclRuleProtocolControl_Type = TruthValue
_F3L2N2AAclRuleProtocolControl_Object = MibTableColumn
f3L2N2AAclRuleProtocolControl = _F3L2N2AAclRuleProtocolControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 11),
    _F3L2N2AAclRuleProtocolControl_Type()
)
f3L2N2AAclRuleProtocolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleProtocolControl.setStatus("current")
_F3L2N2AAclRuleProtocolNumber_Type = Integer32
_F3L2N2AAclRuleProtocolNumber_Object = MibTableColumn
f3L2N2AAclRuleProtocolNumber = _F3L2N2AAclRuleProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 12),
    _F3L2N2AAclRuleProtocolNumber_Type()
)
f3L2N2AAclRuleProtocolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleProtocolNumber.setStatus("current")
_F3L2N2AAclRuleSrcPortControl_Type = TruthValue
_F3L2N2AAclRuleSrcPortControl_Object = MibTableColumn
f3L2N2AAclRuleSrcPortControl = _F3L2N2AAclRuleSrcPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 13),
    _F3L2N2AAclRuleSrcPortControl_Type()
)
f3L2N2AAclRuleSrcPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcPortControl.setStatus("current")
_F3L2N2AAclRuleSrcPortLowLimit_Type = Integer32
_F3L2N2AAclRuleSrcPortLowLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcPortLowLimit = _F3L2N2AAclRuleSrcPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 14),
    _F3L2N2AAclRuleSrcPortLowLimit_Type()
)
f3L2N2AAclRuleSrcPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcPortLowLimit.setStatus("current")
_F3L2N2AAclRuleSrcPortHighLimit_Type = Integer32
_F3L2N2AAclRuleSrcPortHighLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcPortHighLimit = _F3L2N2AAclRuleSrcPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 15),
    _F3L2N2AAclRuleSrcPortHighLimit_Type()
)
f3L2N2AAclRuleSrcPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcPortHighLimit.setStatus("current")
_F3L2N2AAclRuleDstPortControl_Type = TruthValue
_F3L2N2AAclRuleDstPortControl_Object = MibTableColumn
f3L2N2AAclRuleDstPortControl = _F3L2N2AAclRuleDstPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 16),
    _F3L2N2AAclRuleDstPortControl_Type()
)
f3L2N2AAclRuleDstPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstPortControl.setStatus("current")
_F3L2N2AAclRuleDstPortLowLimit_Type = Integer32
_F3L2N2AAclRuleDstPortLowLimit_Object = MibTableColumn
f3L2N2AAclRuleDstPortLowLimit = _F3L2N2AAclRuleDstPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 17),
    _F3L2N2AAclRuleDstPortLowLimit_Type()
)
f3L2N2AAclRuleDstPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstPortLowLimit.setStatus("current")
_F3L2N2AAclRuleDstPortHighLimit_Type = Integer32
_F3L2N2AAclRuleDstPortHighLimit_Object = MibTableColumn
f3L2N2AAclRuleDstPortHighLimit = _F3L2N2AAclRuleDstPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 18),
    _F3L2N2AAclRuleDstPortHighLimit_Type()
)
f3L2N2AAclRuleDstPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstPortHighLimit.setStatus("current")
_F3L2N2AAclRulePriority_Type = Integer32
_F3L2N2AAclRulePriority_Object = MibTableColumn
f3L2N2AAclRulePriority = _F3L2N2AAclRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 19),
    _F3L2N2AAclRulePriority_Type()
)
f3L2N2AAclRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRulePriority.setStatus("current")
_F3L2N2AAclRuleCOS_Type = Integer32
_F3L2N2AAclRuleCOS_Object = MibTableColumn
f3L2N2AAclRuleCOS = _F3L2N2AAclRuleCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 20),
    _F3L2N2AAclRuleCOS_Type()
)
f3L2N2AAclRuleCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleCOS.setStatus("current")
_F3L2N2AAclRuleOperation_Type = L3AclRuleOperation
_F3L2N2AAclRuleOperation_Object = MibTableColumn
f3L2N2AAclRuleOperation = _F3L2N2AAclRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 21),
    _F3L2N2AAclRuleOperation_Type()
)
f3L2N2AAclRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOperation.setStatus("current")
_F3L2N2AAclRuleSummary_Type = F3DisplayString
_F3L2N2AAclRuleSummary_Object = MibTableColumn
f3L2N2AAclRuleSummary = _F3L2N2AAclRuleSummary_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 22),
    _F3L2N2AAclRuleSummary_Type()
)
f3L2N2AAclRuleSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSummary.setStatus("current")
_F3L2N2AAclRuleCosOverrideControl_Type = TruthValue
_F3L2N2AAclRuleCosOverrideControl_Object = MibTableColumn
f3L2N2AAclRuleCosOverrideControl = _F3L2N2AAclRuleCosOverrideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 23),
    _F3L2N2AAclRuleCosOverrideControl_Type()
)
f3L2N2AAclRuleCosOverrideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleCosOverrideControl.setStatus("current")
_F3L2N2AAclRuleSrcMacAddressControl_Type = TruthValue
_F3L2N2AAclRuleSrcMacAddressControl_Object = MibTableColumn
f3L2N2AAclRuleSrcMacAddressControl = _F3L2N2AAclRuleSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 24),
    _F3L2N2AAclRuleSrcMacAddressControl_Type()
)
f3L2N2AAclRuleSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcMacAddressControl.setStatus("current")
_F3L2N2AAclRuleDynamicSrcMacAddressControl_Type = TruthValue
_F3L2N2AAclRuleDynamicSrcMacAddressControl_Object = MibTableColumn
f3L2N2AAclRuleDynamicSrcMacAddressControl = _F3L2N2AAclRuleDynamicSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 25),
    _F3L2N2AAclRuleDynamicSrcMacAddressControl_Type()
)
f3L2N2AAclRuleDynamicSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDynamicSrcMacAddressControl.setStatus("current")
_F3L2N2AAclRuleSrcMacAddress_Type = MacAddress
_F3L2N2AAclRuleSrcMacAddress_Object = MibTableColumn
f3L2N2AAclRuleSrcMacAddress = _F3L2N2AAclRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 26),
    _F3L2N2AAclRuleSrcMacAddress_Type()
)
f3L2N2AAclRuleSrcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcMacAddress.setStatus("current")
_F3L2N2AAclRuleSrcMacAddressMask_Type = MacAddress
_F3L2N2AAclRuleSrcMacAddressMask_Object = MibTableColumn
f3L2N2AAclRuleSrcMacAddressMask = _F3L2N2AAclRuleSrcMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 27),
    _F3L2N2AAclRuleSrcMacAddressMask_Type()
)
f3L2N2AAclRuleSrcMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcMacAddressMask.setStatus("current")
_F3L2N2AAclRuleDstMacAddressControl_Type = TruthValue
_F3L2N2AAclRuleDstMacAddressControl_Object = MibTableColumn
f3L2N2AAclRuleDstMacAddressControl = _F3L2N2AAclRuleDstMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 28),
    _F3L2N2AAclRuleDstMacAddressControl_Type()
)
f3L2N2AAclRuleDstMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstMacAddressControl.setStatus("current")
_F3L2N2AAclRuleDstMacAddress_Type = MacAddress
_F3L2N2AAclRuleDstMacAddress_Object = MibTableColumn
f3L2N2AAclRuleDstMacAddress = _F3L2N2AAclRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 29),
    _F3L2N2AAclRuleDstMacAddress_Type()
)
f3L2N2AAclRuleDstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstMacAddress.setStatus("current")
_F3L2N2AAclRuleDstMacAddressMask_Type = MacAddress
_F3L2N2AAclRuleDstMacAddressMask_Object = MibTableColumn
f3L2N2AAclRuleDstMacAddressMask = _F3L2N2AAclRuleDstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 30),
    _F3L2N2AAclRuleDstMacAddressMask_Type()
)
f3L2N2AAclRuleDstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstMacAddressMask.setStatus("current")
_F3L2N2AAclRuleOuterVlanVIDControl_Type = TruthValue
_F3L2N2AAclRuleOuterVlanVIDControl_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanVIDControl = _F3L2N2AAclRuleOuterVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 31),
    _F3L2N2AAclRuleOuterVlanVIDControl_Type()
)
f3L2N2AAclRuleOuterVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanVIDControl.setStatus("current")
_F3L2N2AAclRuleOuterVlanVIDLowLimit_Type = VlanId
_F3L2N2AAclRuleOuterVlanVIDLowLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanVIDLowLimit = _F3L2N2AAclRuleOuterVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 32),
    _F3L2N2AAclRuleOuterVlanVIDLowLimit_Type()
)
f3L2N2AAclRuleOuterVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanVIDLowLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanVIDHighLimit_Type = VlanId
_F3L2N2AAclRuleOuterVlanVIDHighLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanVIDHighLimit = _F3L2N2AAclRuleOuterVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 33),
    _F3L2N2AAclRuleOuterVlanVIDHighLimit_Type()
)
f3L2N2AAclRuleOuterVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanVIDHighLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanVIDControl_Type = TruthValue
_F3L2N2AAclRuleInnerVlanVIDControl_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanVIDControl = _F3L2N2AAclRuleInnerVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 34),
    _F3L2N2AAclRuleInnerVlanVIDControl_Type()
)
f3L2N2AAclRuleInnerVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanVIDControl.setStatus("current")
_F3L2N2AAclRuleInnerVlanVIDLowLimit_Type = VlanId
_F3L2N2AAclRuleInnerVlanVIDLowLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanVIDLowLimit = _F3L2N2AAclRuleInnerVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 35),
    _F3L2N2AAclRuleInnerVlanVIDLowLimit_Type()
)
f3L2N2AAclRuleInnerVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanVIDLowLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanVIDHighLimit_Type = VlanId
_F3L2N2AAclRuleInnerVlanVIDHighLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanVIDHighLimit = _F3L2N2AAclRuleInnerVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 36),
    _F3L2N2AAclRuleInnerVlanVIDHighLimit_Type()
)
f3L2N2AAclRuleInnerVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanVIDHighLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanPcpControl_Type = TruthValue
_F3L2N2AAclRuleOuterVlanPcpControl_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanPcpControl = _F3L2N2AAclRuleOuterVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 37),
    _F3L2N2AAclRuleOuterVlanPcpControl_Type()
)
f3L2N2AAclRuleOuterVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanPcpControl.setStatus("current")
_F3L2N2AAclRuleOuterVlanPcpLowLimit_Type = VlanPriority
_F3L2N2AAclRuleOuterVlanPcpLowLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanPcpLowLimit = _F3L2N2AAclRuleOuterVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 38),
    _F3L2N2AAclRuleOuterVlanPcpLowLimit_Type()
)
f3L2N2AAclRuleOuterVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanPcpLowLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanPcpHighLimit_Type = VlanPriority
_F3L2N2AAclRuleOuterVlanPcpHighLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanPcpHighLimit = _F3L2N2AAclRuleOuterVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 39),
    _F3L2N2AAclRuleOuterVlanPcpHighLimit_Type()
)
f3L2N2AAclRuleOuterVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanPcpHighLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanPcpControl_Type = TruthValue
_F3L2N2AAclRuleInnerVlanPcpControl_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanPcpControl = _F3L2N2AAclRuleInnerVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 40),
    _F3L2N2AAclRuleInnerVlanPcpControl_Type()
)
f3L2N2AAclRuleInnerVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanPcpControl.setStatus("current")
_F3L2N2AAclRuleInnerVlanPcpLowLimit_Type = VlanPriority
_F3L2N2AAclRuleInnerVlanPcpLowLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanPcpLowLimit = _F3L2N2AAclRuleInnerVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 41),
    _F3L2N2AAclRuleInnerVlanPcpLowLimit_Type()
)
f3L2N2AAclRuleInnerVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanPcpLowLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanPcpHighLimit_Type = VlanPriority
_F3L2N2AAclRuleInnerVlanPcpHighLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanPcpHighLimit = _F3L2N2AAclRuleInnerVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 42),
    _F3L2N2AAclRuleInnerVlanPcpHighLimit_Type()
)
f3L2N2AAclRuleInnerVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanPcpHighLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanDeiControl_Type = TruthValue
_F3L2N2AAclRuleOuterVlanDeiControl_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanDeiControl = _F3L2N2AAclRuleOuterVlanDeiControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 43),
    _F3L2N2AAclRuleOuterVlanDeiControl_Type()
)
f3L2N2AAclRuleOuterVlanDeiControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanDeiControl.setStatus("current")


class _F3L2N2AAclRuleOuterVlanDei_Type(Unsigned32):
    """Custom type f3L2N2AAclRuleOuterVlanDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3L2N2AAclRuleOuterVlanDei_Type.__name__ = "Unsigned32"
_F3L2N2AAclRuleOuterVlanDei_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanDei = _F3L2N2AAclRuleOuterVlanDei_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 44),
    _F3L2N2AAclRuleOuterVlanDei_Type()
)
f3L2N2AAclRuleOuterVlanDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanDei.setStatus("current")
_F3L2N2AAclRuleEtherTypeControl_Type = TruthValue
_F3L2N2AAclRuleEtherTypeControl_Object = MibTableColumn
f3L2N2AAclRuleEtherTypeControl = _F3L2N2AAclRuleEtherTypeControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 45),
    _F3L2N2AAclRuleEtherTypeControl_Type()
)
f3L2N2AAclRuleEtherTypeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleEtherTypeControl.setStatus("current")
_F3L2N2AAclRuleEtherType_Type = Integer32
_F3L2N2AAclRuleEtherType_Object = MibTableColumn
f3L2N2AAclRuleEtherType = _F3L2N2AAclRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 46),
    _F3L2N2AAclRuleEtherType_Type()
)
f3L2N2AAclRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleEtherType.setStatus("current")
_F3L2N2AAclRuleTcpFlagsControl_Type = TruthValue
_F3L2N2AAclRuleTcpFlagsControl_Object = MibTableColumn
f3L2N2AAclRuleTcpFlagsControl = _F3L2N2AAclRuleTcpFlagsControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 47),
    _F3L2N2AAclRuleTcpFlagsControl_Type()
)
f3L2N2AAclRuleTcpFlagsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleTcpFlagsControl.setStatus("current")
_F3L2N2AAclRuleTcpFlags_Type = Integer32
_F3L2N2AAclRuleTcpFlags_Object = MibTableColumn
f3L2N2AAclRuleTcpFlags = _F3L2N2AAclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 48),
    _F3L2N2AAclRuleTcpFlags_Type()
)
f3L2N2AAclRuleTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleTcpFlags.setStatus("current")
_F3L2N2AAclRuleSrcIpv4AddressHighLimit_Type = IpAddress
_F3L2N2AAclRuleSrcIpv4AddressHighLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcIpv4AddressHighLimit = _F3L2N2AAclRuleSrcIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 49),
    _F3L2N2AAclRuleSrcIpv4AddressHighLimit_Type()
)
f3L2N2AAclRuleSrcIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpv4AddressHighLimit.setStatus("current")
_F3L2N2AAclRuleDstIpv4AddressHighLimit_Type = IpAddress
_F3L2N2AAclRuleDstIpv4AddressHighLimit_Object = MibTableColumn
f3L2N2AAclRuleDstIpv4AddressHighLimit = _F3L2N2AAclRuleDstIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 50),
    _F3L2N2AAclRuleDstIpv4AddressHighLimit_Type()
)
f3L2N2AAclRuleDstIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpv4AddressHighLimit.setStatus("current")
_F3L2N2AAclRuleIpv4PriorityHighLimit_Type = Integer32
_F3L2N2AAclRuleIpv4PriorityHighLimit_Object = MibTableColumn
f3L2N2AAclRuleIpv4PriorityHighLimit = _F3L2N2AAclRuleIpv4PriorityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 51),
    _F3L2N2AAclRuleIpv4PriorityHighLimit_Type()
)
f3L2N2AAclRuleIpv4PriorityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpv4PriorityHighLimit.setStatus("current")
_F3L2N2AAclRuleStorageType_Type = StorageType
_F3L2N2AAclRuleStorageType_Object = MibTableColumn
f3L2N2AAclRuleStorageType = _F3L2N2AAclRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 52),
    _F3L2N2AAclRuleStorageType_Type()
)
f3L2N2AAclRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStorageType.setStatus("current")
_F3L2N2AAclRuleRowStatus_Type = RowStatus
_F3L2N2AAclRuleRowStatus_Object = MibTableColumn
f3L2N2AAclRuleRowStatus = _F3L2N2AAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 53),
    _F3L2N2AAclRuleRowStatus_Type()
)
f3L2N2AAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleRowStatus.setStatus("current")
_F3L2N2AAclRuleAdminState_Type = AdminState
_F3L2N2AAclRuleAdminState_Object = MibTableColumn
f3L2N2AAclRuleAdminState = _F3L2N2AAclRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 54),
    _F3L2N2AAclRuleAdminState_Type()
)
f3L2N2AAclRuleAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleAdminState.setStatus("current")
_F3L3QosPolicerTable_Object = MibTable
f3L3QosPolicerTable = _F3L3QosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerTable.setStatus("current")
_F3L3QosPolicerEntry_Object = MibTableRow
f3L3QosPolicerEntry = _F3L3QosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1)
)
f3L3QosPolicerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerEntry.setStatus("current")


class _F3L3QosPolicerIndex_Type(Integer32):
    """Custom type f3L3QosPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_F3L3QosPolicerIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerIndex_Object = MibTableColumn
f3L3QosPolicerIndex = _F3L3QosPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 1),
    _F3L3QosPolicerIndex_Type()
)
f3L3QosPolicerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerIndex.setStatus("current")
_F3L3QosPolicerAdminState_Type = AdminState
_F3L3QosPolicerAdminState_Object = MibTableColumn
f3L3QosPolicerAdminState = _F3L3QosPolicerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 2),
    _F3L3QosPolicerAdminState_Type()
)
f3L3QosPolicerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerAdminState.setStatus("current")
_F3L3QosPolicerOperationalState_Type = OperationalState
_F3L3QosPolicerOperationalState_Object = MibTableColumn
f3L3QosPolicerOperationalState = _F3L3QosPolicerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 3),
    _F3L3QosPolicerOperationalState_Type()
)
f3L3QosPolicerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerOperationalState.setStatus("current")
_F3L3QosPolicerSecondaryState_Type = SecondaryState
_F3L3QosPolicerSecondaryState_Object = MibTableColumn
f3L3QosPolicerSecondaryState = _F3L3QosPolicerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 4),
    _F3L3QosPolicerSecondaryState_Type()
)
f3L3QosPolicerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerSecondaryState.setStatus("current")
_F3L3QosPolicerCIRLo_Type = Unsigned32
_F3L3QosPolicerCIRLo_Object = MibTableColumn
f3L3QosPolicerCIRLo = _F3L3QosPolicerCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 5),
    _F3L3QosPolicerCIRLo_Type()
)
f3L3QosPolicerCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCIRLo.setStatus("current")
_F3L3QosPolicerCIRHi_Type = Unsigned32
_F3L3QosPolicerCIRHi_Object = MibTableColumn
f3L3QosPolicerCIRHi = _F3L3QosPolicerCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 6),
    _F3L3QosPolicerCIRHi_Type()
)
f3L3QosPolicerCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCIRHi.setStatus("current")
_F3L3QosPolicerEIRLo_Type = Unsigned32
_F3L3QosPolicerEIRLo_Object = MibTableColumn
f3L3QosPolicerEIRLo = _F3L3QosPolicerEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 7),
    _F3L3QosPolicerEIRLo_Type()
)
f3L3QosPolicerEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerEIRLo.setStatus("current")
_F3L3QosPolicerEIRHi_Type = Unsigned32
_F3L3QosPolicerEIRHi_Object = MibTableColumn
f3L3QosPolicerEIRHi = _F3L3QosPolicerEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 8),
    _F3L3QosPolicerEIRHi_Type()
)
f3L3QosPolicerEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerEIRHi.setStatus("current")
_F3L3QosPolicerCBS_Type = Integer32
_F3L3QosPolicerCBS_Object = MibTableColumn
f3L3QosPolicerCBS = _F3L3QosPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 9),
    _F3L3QosPolicerCBS_Type()
)
f3L3QosPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCBS.setStatus("current")
_F3L3QosPolicerEBS_Type = Integer32
_F3L3QosPolicerEBS_Object = MibTableColumn
f3L3QosPolicerEBS = _F3L3QosPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 10),
    _F3L3QosPolicerEBS_Type()
)
f3L3QosPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerEBS.setStatus("current")
_F3L3QosPolicerAlgorithm_Type = PolicerAlgorithmType
_F3L3QosPolicerAlgorithm_Object = MibTableColumn
f3L3QosPolicerAlgorithm = _F3L3QosPolicerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 11),
    _F3L3QosPolicerAlgorithm_Type()
)
f3L3QosPolicerAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerAlgorithm.setStatus("current")
_F3L3QosPolicerColorMode_Type = PolicerColorMode
_F3L3QosPolicerColorMode_Object = MibTableColumn
f3L3QosPolicerColorMode = _F3L3QosPolicerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 12),
    _F3L3QosPolicerColorMode_Type()
)
f3L3QosPolicerColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerColorMode.setStatus("current")
_F3L3QosPolicerCouplingFlag_Type = TruthValue
_F3L3QosPolicerCouplingFlag_Object = MibTableColumn
f3L3QosPolicerCouplingFlag = _F3L3QosPolicerCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 13),
    _F3L3QosPolicerCouplingFlag_Type()
)
f3L3QosPolicerCouplingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCouplingFlag.setStatus("current")
_F3L3QosPolicerStorageType_Type = StorageType
_F3L3QosPolicerStorageType_Object = MibTableColumn
f3L3QosPolicerStorageType = _F3L3QosPolicerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 14),
    _F3L3QosPolicerStorageType_Type()
)
f3L3QosPolicerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerStorageType.setStatus("current")
_F3L3QosPolicerRowStatus_Type = RowStatus
_F3L3QosPolicerRowStatus_Object = MibTableColumn
f3L3QosPolicerRowStatus = _F3L3QosPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 15),
    _F3L3QosPolicerRowStatus_Type()
)
f3L3QosPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerRowStatus.setStatus("current")
_F3L3QosShaperTable_Object = MibTable
f3L3QosShaperTable = _F3L3QosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8)
)
if mibBuilder.loadTexts:
    f3L3QosShaperTable.setStatus("current")
_F3L3QosShaperEntry_Object = MibTableRow
f3L3QosShaperEntry = _F3L3QosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1)
)
f3L3QosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperEntry.setStatus("current")


class _F3L3QosShaperIndex_Type(Integer32):
    """Custom type f3L3QosShaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_F3L3QosShaperIndex_Type.__name__ = "Integer32"
_F3L3QosShaperIndex_Object = MibTableColumn
f3L3QosShaperIndex = _F3L3QosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 1),
    _F3L3QosShaperIndex_Type()
)
f3L3QosShaperIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperIndex.setStatus("current")
_F3L3QosShaperAdminState_Type = AdminState
_F3L3QosShaperAdminState_Object = MibTableColumn
f3L3QosShaperAdminState = _F3L3QosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 2),
    _F3L3QosShaperAdminState_Type()
)
f3L3QosShaperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperAdminState.setStatus("current")
_F3L3QosShaperOperationalState_Type = OperationalState
_F3L3QosShaperOperationalState_Object = MibTableColumn
f3L3QosShaperOperationalState = _F3L3QosShaperOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 3),
    _F3L3QosShaperOperationalState_Type()
)
f3L3QosShaperOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperOperationalState.setStatus("current")
_F3L3QosShaperSecondaryState_Type = SecondaryState
_F3L3QosShaperSecondaryState_Object = MibTableColumn
f3L3QosShaperSecondaryState = _F3L3QosShaperSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 4),
    _F3L3QosShaperSecondaryState_Type()
)
f3L3QosShaperSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperSecondaryState.setStatus("current")
_F3L3QosShaperCIRLo_Type = Unsigned32
_F3L3QosShaperCIRLo_Object = MibTableColumn
f3L3QosShaperCIRLo = _F3L3QosShaperCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 5),
    _F3L3QosShaperCIRLo_Type()
)
f3L3QosShaperCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperCIRLo.setStatus("current")
_F3L3QosShaperCIRHi_Type = Unsigned32
_F3L3QosShaperCIRHi_Object = MibTableColumn
f3L3QosShaperCIRHi = _F3L3QosShaperCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 6),
    _F3L3QosShaperCIRHi_Type()
)
f3L3QosShaperCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperCIRHi.setStatus("current")
_F3L3QosShaperEIRLo_Type = Unsigned32
_F3L3QosShaperEIRLo_Object = MibTableColumn
f3L3QosShaperEIRLo = _F3L3QosShaperEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 7),
    _F3L3QosShaperEIRLo_Type()
)
f3L3QosShaperEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperEIRLo.setStatus("current")
_F3L3QosShaperEIRHi_Type = Unsigned32
_F3L3QosShaperEIRHi_Object = MibTableColumn
f3L3QosShaperEIRHi = _F3L3QosShaperEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 8),
    _F3L3QosShaperEIRHi_Type()
)
f3L3QosShaperEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperEIRHi.setStatus("current")
_F3L3QosShaperBufferSize_Type = Unsigned32
_F3L3QosShaperBufferSize_Object = MibTableColumn
f3L3QosShaperBufferSize = _F3L3QosShaperBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 9),
    _F3L3QosShaperBufferSize_Type()
)
f3L3QosShaperBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperBufferSize.setStatus("current")


class _F3L3QosShaperCOS_Type(Integer32):
    """Custom type f3L3QosShaperCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3L3QosShaperCOS_Type.__name__ = "Integer32"
_F3L3QosShaperCOS_Object = MibTableColumn
f3L3QosShaperCOS = _F3L3QosShaperCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 10),
    _F3L3QosShaperCOS_Type()
)
f3L3QosShaperCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperCOS.setStatus("current")
_F3L3QosShaperWredGreenMinQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredGreenMinQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredGreenMinQueueThreshold = _F3L3QosShaperWredGreenMinQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 11),
    _F3L3QosShaperWredGreenMinQueueThreshold_Type()
)
f3L3QosShaperWredGreenMinQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredGreenMinQueueThreshold.setStatus("current")
_F3L3QosShaperWredGreenMaxQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredGreenMaxQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredGreenMaxQueueThreshold = _F3L3QosShaperWredGreenMaxQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 12),
    _F3L3QosShaperWredGreenMaxQueueThreshold_Type()
)
f3L3QosShaperWredGreenMaxQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredGreenMaxQueueThreshold.setStatus("current")
_F3L3QosShaperWredGreenDropProbability_Type = Unsigned32
_F3L3QosShaperWredGreenDropProbability_Object = MibTableColumn
f3L3QosShaperWredGreenDropProbability = _F3L3QosShaperWredGreenDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 13),
    _F3L3QosShaperWredGreenDropProbability_Type()
)
f3L3QosShaperWredGreenDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredGreenDropProbability.setStatus("current")
_F3L3QosShaperWredYellowMinQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredYellowMinQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredYellowMinQueueThreshold = _F3L3QosShaperWredYellowMinQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 14),
    _F3L3QosShaperWredYellowMinQueueThreshold_Type()
)
f3L3QosShaperWredYellowMinQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredYellowMinQueueThreshold.setStatus("current")
_F3L3QosShaperWredYellowMaxQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredYellowMaxQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredYellowMaxQueueThreshold = _F3L3QosShaperWredYellowMaxQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 15),
    _F3L3QosShaperWredYellowMaxQueueThreshold_Type()
)
f3L3QosShaperWredYellowMaxQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredYellowMaxQueueThreshold.setStatus("current")
_F3L3QosShaperWredYellowDropProbability_Type = Unsigned32
_F3L3QosShaperWredYellowDropProbability_Object = MibTableColumn
f3L3QosShaperWredYellowDropProbability = _F3L3QosShaperWredYellowDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 16),
    _F3L3QosShaperWredYellowDropProbability_Type()
)
f3L3QosShaperWredYellowDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredYellowDropProbability.setStatus("current")
_F3L3QosShaperStorageType_Type = StorageType
_F3L3QosShaperStorageType_Object = MibTableColumn
f3L3QosShaperStorageType = _F3L3QosShaperStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 17),
    _F3L3QosShaperStorageType_Type()
)
f3L3QosShaperStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperStorageType.setStatus("current")
_F3L3QosShaperRowStatus_Type = RowStatus
_F3L3QosShaperRowStatus_Object = MibTableColumn
f3L3QosShaperRowStatus = _F3L3QosShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 18),
    _F3L3QosShaperRowStatus_Type()
)
f3L3QosShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperRowStatus.setStatus("current")
_F3L3TrafficIPInterfaceTable_Object = MibTable
f3L3TrafficIPInterfaceTable = _F3L3TrafficIPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceTable.setStatus("current")
_F3L3TrafficIPInterfaceEntry_Object = MibTableRow
f3L3TrafficIPInterfaceEntry = _F3L3TrafficIPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1)
)
f3L3TrafficIPInterfaceEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceEntry.setStatus("current")
_F3L3TrafficIPIfIndex_Type = Integer32
_F3L3TrafficIPIfIndex_Object = MibTableColumn
f3L3TrafficIPIfIndex = _F3L3TrafficIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 1),
    _F3L3TrafficIPIfIndex_Type()
)
f3L3TrafficIPIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIndex.setStatus("current")


class _F3L3TrafficIPIfName_Type(DisplayString):
    """Custom type f3L3TrafficIPIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIPIfName_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfName_Object = MibTableColumn
f3L3TrafficIPIfName = _F3L3TrafficIPIfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 2),
    _F3L3TrafficIPIfName_Type()
)
f3L3TrafficIPIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfName.setStatus("current")
_F3L3TrafficIPIfAdminState_Type = AdminState
_F3L3TrafficIPIfAdminState_Object = MibTableColumn
f3L3TrafficIPIfAdminState = _F3L3TrafficIPIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 3),
    _F3L3TrafficIPIfAdminState_Type()
)
f3L3TrafficIPIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfAdminState.setStatus("current")
_F3L3TrafficIPIfSecondaryState_Type = SecondaryState
_F3L3TrafficIPIfSecondaryState_Object = MibTableColumn
f3L3TrafficIPIfSecondaryState = _F3L3TrafficIPIfSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 4),
    _F3L3TrafficIPIfSecondaryState_Type()
)
f3L3TrafficIPIfSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfSecondaryState.setStatus("current")
_F3L3TrafficIPIfOperationalState_Type = OperationalState
_F3L3TrafficIPIfOperationalState_Object = MibTableColumn
f3L3TrafficIPIfOperationalState = _F3L3TrafficIPIfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 5),
    _F3L3TrafficIPIfOperationalState_Type()
)
f3L3TrafficIPIfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOperationalState.setStatus("current")
_F3L3TrafficIPIfProxyArpEnabled_Type = TruthValue
_F3L3TrafficIPIfProxyArpEnabled_Object = MibTableColumn
f3L3TrafficIPIfProxyArpEnabled = _F3L3TrafficIPIfProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 6),
    _F3L3TrafficIPIfProxyArpEnabled_Type()
)
f3L3TrafficIPIfProxyArpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfProxyArpEnabled.setStatus("current")
_F3L3TrafficIPIfIpAddressSourceType_Type = IfIpAddressSourceType
_F3L3TrafficIPIfIpAddressSourceType_Object = MibTableColumn
f3L3TrafficIPIfIpAddressSourceType = _F3L3TrafficIPIfIpAddressSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 7),
    _F3L3TrafficIPIfIpAddressSourceType_Type()
)
f3L3TrafficIPIfIpAddressSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpAddressSourceType.setStatus("current")
_F3L3TrafficIPIfMgmtUseEnable_Type = TruthValue
_F3L3TrafficIPIfMgmtUseEnable_Object = MibTableColumn
f3L3TrafficIPIfMgmtUseEnable = _F3L3TrafficIPIfMgmtUseEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 8),
    _F3L3TrafficIPIfMgmtUseEnable_Type()
)
f3L3TrafficIPIfMgmtUseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfMgmtUseEnable.setStatus("current")
_F3L3TrafficIPIfIpAddress_Type = IpAddress
_F3L3TrafficIPIfIpAddress_Object = MibTableColumn
f3L3TrafficIPIfIpAddress = _F3L3TrafficIPIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 9),
    _F3L3TrafficIPIfIpAddress_Type()
)
f3L3TrafficIPIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpAddress.setStatus("current")
_F3L3TrafficIPIfMask_Type = IpAddress
_F3L3TrafficIPIfMask_Object = MibTableColumn
f3L3TrafficIPIfMask = _F3L3TrafficIPIfMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 10),
    _F3L3TrafficIPIfMask_Type()
)
f3L3TrafficIPIfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfMask.setStatus("current")
_F3L3TrafficIPIfDhcpRelayInterfaceSide_Type = DhcpRelayInterfaceSide
_F3L3TrafficIPIfDhcpRelayInterfaceSide_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInterfaceSide = _F3L3TrafficIPIfDhcpRelayInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 11),
    _F3L3TrafficIPIfDhcpRelayInterfaceSide_Type()
)
f3L3TrafficIPIfDhcpRelayInterfaceSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInterfaceSide.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60 = _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 12),
    _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Type()
)
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60.setStatus("current")
_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control = _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 13),
    _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Type()
)
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayUserClassOpt77_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayUserClassOpt77 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayUserClassOpt77_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayUserClassOpt77_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayUserClassOpt77 = _F3L3TrafficIPIfDhcpRelayUserClassOpt77_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 14),
    _F3L3TrafficIPIfDhcpRelayUserClassOpt77_Type()
)
f3L3TrafficIPIfDhcpRelayUserClassOpt77.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayUserClassOpt77.setStatus("current")
_F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayUserClassOpt77Control = _F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 15),
    _F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Type()
)
f3L3TrafficIPIfDhcpRelayUserClassOpt77Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayUserClassOpt77Control.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1 = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 16),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1.setStatus("current")
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 17),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2 = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 18),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2.setStatus("current")
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 19),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled.setStatus("current")
_F3L3TrafficIPIfDhcpEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpEnabled = _F3L3TrafficIPIfDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 20),
    _F3L3TrafficIPIfDhcpEnabled_Type()
)
f3L3TrafficIPIfDhcpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpRole_Type = CmDhcpRole
_F3L3TrafficIPIfDhcpRole_Object = MibTableColumn
f3L3TrafficIPIfDhcpRole = _F3L3TrafficIPIfDhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 21),
    _F3L3TrafficIPIfDhcpRole_Type()
)
f3L3TrafficIPIfDhcpRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRole.setStatus("current")
_F3L3TrafficIPIfDhcpClientIdEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpClientIdEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpClientIdEnabled = _F3L3TrafficIPIfDhcpClientIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 22),
    _F3L3TrafficIPIfDhcpClientIdEnabled_Type()
)
f3L3TrafficIPIfDhcpClientIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClientIdEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpClientId_Type = DisplayString
_F3L3TrafficIPIfDhcpClientId_Object = MibTableColumn
f3L3TrafficIPIfDhcpClientId = _F3L3TrafficIPIfDhcpClientId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 23),
    _F3L3TrafficIPIfDhcpClientId_Type()
)
f3L3TrafficIPIfDhcpClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClientId.setStatus("current")
_F3L3TrafficIPIfDhcpClassIdEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpClassIdEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpClassIdEnabled = _F3L3TrafficIPIfDhcpClassIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 24),
    _F3L3TrafficIPIfDhcpClassIdEnabled_Type()
)
f3L3TrafficIPIfDhcpClassIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClassIdEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpHostNameEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpHostNameEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpHostNameEnabled = _F3L3TrafficIPIfDhcpHostNameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 25),
    _F3L3TrafficIPIfDhcpHostNameEnabled_Type()
)
f3L3TrafficIPIfDhcpHostNameEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpHostNameEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpHostName_Type = DisplayString
_F3L3TrafficIPIfDhcpHostName_Object = MibTableColumn
f3L3TrafficIPIfDhcpHostName = _F3L3TrafficIPIfDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 26),
    _F3L3TrafficIPIfDhcpHostName_Type()
)
f3L3TrafficIPIfDhcpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpHostName.setStatus("current")
_F3L3TrafficIPIfDhcpClientIdType_Type = DHCPCIDType
_F3L3TrafficIPIfDhcpClientIdType_Object = MibTableColumn
f3L3TrafficIPIfDhcpClientIdType = _F3L3TrafficIPIfDhcpClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 27),
    _F3L3TrafficIPIfDhcpClientIdType_Type()
)
f3L3TrafficIPIfDhcpClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClientIdType.setStatus("current")
_F3L3TrafficIPIfDhcpHostNameType_Type = DHCPHostNameType
_F3L3TrafficIPIfDhcpHostNameType_Object = MibTableColumn
f3L3TrafficIPIfDhcpHostNameType = _F3L3TrafficIPIfDhcpHostNameType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 28),
    _F3L3TrafficIPIfDhcpHostNameType_Type()
)
f3L3TrafficIPIfDhcpHostNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpHostNameType.setStatus("current")
_F3L3TrafficIPIfStorageType_Type = StorageType
_F3L3TrafficIPIfStorageType_Object = MibTableColumn
f3L3TrafficIPIfStorageType = _F3L3TrafficIPIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 29),
    _F3L3TrafficIPIfStorageType_Type()
)
f3L3TrafficIPIfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfStorageType.setStatus("current")
_F3L3TrafficIPIfRowStatus_Type = RowStatus
_F3L3TrafficIPIfRowStatus_Object = MibTableColumn
f3L3TrafficIPIfRowStatus = _F3L3TrafficIPIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 30),
    _F3L3TrafficIPIfRowStatus_Type()
)
f3L3TrafficIPIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRowStatus.setStatus("current")
_F3L3TrafficIPIfAction_Type = AffectiveArpActionType
_F3L3TrafficIPIfAction_Object = MibTableColumn
f3L3TrafficIPIfAction = _F3L3TrafficIPIfAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 31),
    _F3L3TrafficIPIfAction_Type()
)
f3L3TrafficIPIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfAction.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberTable_Object = MibTable
f3DhcpRelayAgentTrafficIpIfMemberTable = _F3DhcpRelayAgentTrafficIpIfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10)
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberTable.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberEntry_Object = MibTableRow
f3DhcpRelayAgentTrafficIpIfMemberEntry = _F3DhcpRelayAgentTrafficIpIfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1)
)
f3DhcpRelayAgentTrafficIpIfMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3DhcpRelayAgentIndex"),
    (0, "F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberObject"),
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberEntry.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberObject_Type = VariablePointer
_F3DhcpRelayAgentTrafficIpIfMemberObject_Object = MibTableColumn
f3DhcpRelayAgentTrafficIpIfMemberObject = _F3DhcpRelayAgentTrafficIpIfMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1, 1),
    _F3DhcpRelayAgentTrafficIpIfMemberObject_Type()
)
f3DhcpRelayAgentTrafficIpIfMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberObject.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberStorageType_Type = StorageType
_F3DhcpRelayAgentTrafficIpIfMemberStorageType_Object = MibTableColumn
f3DhcpRelayAgentTrafficIpIfMemberStorageType = _F3DhcpRelayAgentTrafficIpIfMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1, 2),
    _F3DhcpRelayAgentTrafficIpIfMemberStorageType_Type()
)
f3DhcpRelayAgentTrafficIpIfMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberStorageType.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Type = RowStatus
_F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Object = MibTableColumn
f3DhcpRelayAgentTrafficIpIfMemberRowStatus = _F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1, 3),
    _F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Type()
)
f3DhcpRelayAgentTrafficIpIfMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberRowStatus.setStatus("current")
_F3VrfTrafficIpIfMemberTable_Object = MibTable
f3VrfTrafficIpIfMemberTable = _F3VrfTrafficIpIfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11)
)
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberTable.setStatus("current")
_F3VrfTrafficIpIfMemberEntry_Object = MibTableRow
f3VrfTrafficIpIfMemberEntry = _F3VrfTrafficIpIfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1)
)
f3VrfTrafficIpIfMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfTrafficIpIfMemberObject"),
)
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberEntry.setStatus("current")
_F3VrfTrafficIpIfMemberObject_Type = VariablePointer
_F3VrfTrafficIpIfMemberObject_Object = MibTableColumn
f3VrfTrafficIpIfMemberObject = _F3VrfTrafficIpIfMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1, 1),
    _F3VrfTrafficIpIfMemberObject_Type()
)
f3VrfTrafficIpIfMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberObject.setStatus("current")
_F3VrfTrafficIpIfMemberStorageType_Type = StorageType
_F3VrfTrafficIpIfMemberStorageType_Object = MibTableColumn
f3VrfTrafficIpIfMemberStorageType = _F3VrfTrafficIpIfMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1, 2),
    _F3VrfTrafficIpIfMemberStorageType_Type()
)
f3VrfTrafficIpIfMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberStorageType.setStatus("current")
_F3VrfTrafficIpIfMemberRowStatus_Type = RowStatus
_F3VrfTrafficIpIfMemberRowStatus_Object = MibTableColumn
f3VrfTrafficIpIfMemberRowStatus = _F3VrfTrafficIpIfMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1, 3),
    _F3VrfTrafficIpIfMemberRowStatus_Type()
)
f3VrfTrafficIpIfMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberRowStatus.setStatus("current")
_F3L3TrafficIpv4RouteTable_Object = MibTable
f3L3TrafficIpv4RouteTable = _F3L3TrafficIpv4RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteTable.setStatus("current")
_F3L3TrafficIpv4RouteEntry_Object = MibTableRow
f3L3TrafficIpv4RouteEntry = _F3L3TrafficIpv4RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1)
)
f3L3TrafficIpv4RouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteDest"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteMask"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteNextHop"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteInterface"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteEntry.setStatus("current")
_F3L3TrafficIpv4RouteDest_Type = IpAddress
_F3L3TrafficIpv4RouteDest_Object = MibTableColumn
f3L3TrafficIpv4RouteDest = _F3L3TrafficIpv4RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 1),
    _F3L3TrafficIpv4RouteDest_Type()
)
f3L3TrafficIpv4RouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteDest.setStatus("current")
_F3L3TrafficIpv4RouteMask_Type = IpAddress
_F3L3TrafficIpv4RouteMask_Object = MibTableColumn
f3L3TrafficIpv4RouteMask = _F3L3TrafficIpv4RouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 2),
    _F3L3TrafficIpv4RouteMask_Type()
)
f3L3TrafficIpv4RouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteMask.setStatus("current")
_F3L3TrafficIpv4RouteNextHop_Type = IpAddress
_F3L3TrafficIpv4RouteNextHop_Object = MibTableColumn
f3L3TrafficIpv4RouteNextHop = _F3L3TrafficIpv4RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 3),
    _F3L3TrafficIpv4RouteNextHop_Type()
)
f3L3TrafficIpv4RouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteNextHop.setStatus("current")
_F3L3TrafficIpv4RouteMetric_Type = Integer32
_F3L3TrafficIpv4RouteMetric_Object = MibTableColumn
f3L3TrafficIpv4RouteMetric = _F3L3TrafficIpv4RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 4),
    _F3L3TrafficIpv4RouteMetric_Type()
)
f3L3TrafficIpv4RouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteMetric.setStatus("current")
_F3L3TrafficIpv4RouteInterface_Type = DisplayString
_F3L3TrafficIpv4RouteInterface_Object = MibTableColumn
f3L3TrafficIpv4RouteInterface = _F3L3TrafficIpv4RouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 5),
    _F3L3TrafficIpv4RouteInterface_Type()
)
f3L3TrafficIpv4RouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteInterface.setStatus("current")
_F3L3TrafficIpv4RouteAdvertise_Type = TruthValue
_F3L3TrafficIpv4RouteAdvertise_Object = MibTableColumn
f3L3TrafficIpv4RouteAdvertise = _F3L3TrafficIpv4RouteAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 6),
    _F3L3TrafficIpv4RouteAdvertise_Type()
)
f3L3TrafficIpv4RouteAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteAdvertise.setStatus("current")
_F3L3TrafficIpv4RouteStatus_Type = TrafficIpRouteStatus
_F3L3TrafficIpv4RouteStatus_Object = MibTableColumn
f3L3TrafficIpv4RouteStatus = _F3L3TrafficIpv4RouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 7),
    _F3L3TrafficIpv4RouteStatus_Type()
)
f3L3TrafficIpv4RouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteStatus.setStatus("current")
_F3L3TrafficIpv4RouteSourceForwardingEnable_Type = TruthValue
_F3L3TrafficIpv4RouteSourceForwardingEnable_Object = MibTableColumn
f3L3TrafficIpv4RouteSourceForwardingEnable = _F3L3TrafficIpv4RouteSourceForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 8),
    _F3L3TrafficIpv4RouteSourceForwardingEnable_Type()
)
f3L3TrafficIpv4RouteSourceForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteSourceForwardingEnable.setStatus("current")
_F3L3TrafficIpv4RouteFlags_Type = RouteFlags
_F3L3TrafficIpv4RouteFlags_Object = MibTableColumn
f3L3TrafficIpv4RouteFlags = _F3L3TrafficIpv4RouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 9),
    _F3L3TrafficIpv4RouteFlags_Type()
)
f3L3TrafficIpv4RouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteFlags.setStatus("current")
_F3L3TrafficIpv4RouteStorageType_Type = StorageType
_F3L3TrafficIpv4RouteStorageType_Object = MibTableColumn
f3L3TrafficIpv4RouteStorageType = _F3L3TrafficIpv4RouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 10),
    _F3L3TrafficIpv4RouteStorageType_Type()
)
f3L3TrafficIpv4RouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteStorageType.setStatus("current")
_F3L3TrafficIpv4RouteRowStatus_Type = RowStatus
_F3L3TrafficIpv4RouteRowStatus_Object = MibTableColumn
f3L3TrafficIpv4RouteRowStatus = _F3L3TrafficIpv4RouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 11),
    _F3L3TrafficIpv4RouteRowStatus_Type()
)
f3L3TrafficIpv4RouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteRowStatus.setStatus("current")
_F3L3TrafficIpv4RouteType_Type = IpEntryType
_F3L3TrafficIpv4RouteType_Object = MibTableColumn
f3L3TrafficIpv4RouteType = _F3L3TrafficIpv4RouteType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 12),
    _F3L3TrafficIpv4RouteType_Type()
)
f3L3TrafficIpv4RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteType.setStatus("current")
_F3L3TrafficArpTable_Object = MibTable
f3L3TrafficArpTable = _F3L3TrafficArpTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13)
)
if mibBuilder.loadTexts:
    f3L3TrafficArpTable.setStatus("current")
_F3L3TrafficArpEntry_Object = MibTableRow
f3L3TrafficArpEntry = _F3L3TrafficArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1)
)
f3L3TrafficArpEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficArpIPAddress"),
)
if mibBuilder.loadTexts:
    f3L3TrafficArpEntry.setStatus("current")
_F3L3TrafficArpIPAddress_Type = IpAddress
_F3L3TrafficArpIPAddress_Object = MibTableColumn
f3L3TrafficArpIPAddress = _F3L3TrafficArpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 1),
    _F3L3TrafficArpIPAddress_Type()
)
f3L3TrafficArpIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficArpIPAddress.setStatus("current")
_F3L3TrafficArpMacAddress_Type = MacAddress
_F3L3TrafficArpMacAddress_Object = MibTableColumn
f3L3TrafficArpMacAddress = _F3L3TrafficArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 2),
    _F3L3TrafficArpMacAddress_Type()
)
f3L3TrafficArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficArpMacAddress.setStatus("current")
_F3L3TrafficArpInterface_Type = DisplayString
_F3L3TrafficArpInterface_Object = MibTableColumn
f3L3TrafficArpInterface = _F3L3TrafficArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 3),
    _F3L3TrafficArpInterface_Type()
)
f3L3TrafficArpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficArpInterface.setStatus("current")
_F3L3TrafficArpEntryType_Type = IpEntryType
_F3L3TrafficArpEntryType_Object = MibTableColumn
f3L3TrafficArpEntryType = _F3L3TrafficArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 4),
    _F3L3TrafficArpEntryType_Type()
)
f3L3TrafficArpEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficArpEntryType.setStatus("current")
_F3L3TrafficArpStorageType_Type = StorageType
_F3L3TrafficArpStorageType_Object = MibTableColumn
f3L3TrafficArpStorageType = _F3L3TrafficArpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 5),
    _F3L3TrafficArpStorageType_Type()
)
f3L3TrafficArpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficArpStorageType.setStatus("current")
_F3L3TrafficArpRowStatus_Type = RowStatus
_F3L3TrafficArpRowStatus_Object = MibTableColumn
f3L3TrafficArpRowStatus = _F3L3TrafficArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 6),
    _F3L3TrafficArpRowStatus_Type()
)
f3L3TrafficArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficArpRowStatus.setStatus("current")
_F3L3Performance_ObjectIdentity = ObjectIdentity
f3L3Performance = _F3L3Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2)
)
_F3L3FlowPointStatsTable_Object = MibTable
f3L3FlowPointStatsTable = _F3L3FlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1)
)
if mibBuilder.loadTexts:
    f3L3FlowPointStatsTable.setStatus("current")
_F3L3FlowPointStatsEntry_Object = MibTableRow
f3L3FlowPointStatsEntry = _F3L3FlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1)
)
f3L3FlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointStatsEntry.setStatus("current")


class _F3L3FlowPointStatsIndex_Type(Integer32):
    """Custom type f3L3FlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3FlowPointStatsIndex_Type.__name__ = "Integer32"
_F3L3FlowPointStatsIndex_Object = MibTableColumn
f3L3FlowPointStatsIndex = _F3L3FlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 1),
    _F3L3FlowPointStatsIndex_Type()
)
f3L3FlowPointStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsIndex.setStatus("current")
_F3L3FlowPointStatsIntervalType_Type = CmPmIntervalType
_F3L3FlowPointStatsIntervalType_Object = MibTableColumn
f3L3FlowPointStatsIntervalType = _F3L3FlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 2),
    _F3L3FlowPointStatsIntervalType_Type()
)
f3L3FlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsIntervalType.setStatus("current")
_F3L3FlowPointStatsValid_Type = TruthValue
_F3L3FlowPointStatsValid_Object = MibTableColumn
f3L3FlowPointStatsValid = _F3L3FlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 3),
    _F3L3FlowPointStatsValid_Type()
)
f3L3FlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsValid.setStatus("current")
_F3L3FlowPointStatsAction_Type = CmPmBinAction
_F3L3FlowPointStatsAction_Object = MibTableColumn
f3L3FlowPointStatsAction = _F3L3FlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 4),
    _F3L3FlowPointStatsAction_Type()
)
f3L3FlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsAction.setStatus("current")
_F3L3FlowPointStatsFMG_Type = PerfCounter64
_F3L3FlowPointStatsFMG_Object = MibTableColumn
f3L3FlowPointStatsFMG = _F3L3FlowPointStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 5),
    _F3L3FlowPointStatsFMG_Type()
)
f3L3FlowPointStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFMG.setStatus("current")
_F3L3FlowPointStatsFMY_Type = PerfCounter64
_F3L3FlowPointStatsFMY_Object = MibTableColumn
f3L3FlowPointStatsFMY = _F3L3FlowPointStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 6),
    _F3L3FlowPointStatsFMY_Type()
)
f3L3FlowPointStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFMY.setStatus("current")
_F3L3FlowPointStatsFMRD_Type = PerfCounter64
_F3L3FlowPointStatsFMRD_Object = MibTableColumn
f3L3FlowPointStatsFMRD = _F3L3FlowPointStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 7),
    _F3L3FlowPointStatsFMRD_Type()
)
f3L3FlowPointStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFMRD.setStatus("current")
_F3L3FlowPointStatsFTD_Type = PerfCounter64
_F3L3FlowPointStatsFTD_Object = MibTableColumn
f3L3FlowPointStatsFTD = _F3L3FlowPointStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 8),
    _F3L3FlowPointStatsFTD_Type()
)
f3L3FlowPointStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFTD.setStatus("current")
_F3L3FlowPointStatsFragmentedDropAcl_Type = PerfCounter64
_F3L3FlowPointStatsFragmentedDropAcl_Object = MibTableColumn
f3L3FlowPointStatsFragmentedDropAcl = _F3L3FlowPointStatsFragmentedDropAcl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 9),
    _F3L3FlowPointStatsFragmentedDropAcl_Type()
)
f3L3FlowPointStatsFragmentedDropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFragmentedDropAcl.setStatus("current")
_F3L3FlowPointStatsAclRuleDrop_Type = PerfCounter64
_F3L3FlowPointStatsAclRuleDrop_Object = MibTableColumn
f3L3FlowPointStatsAclRuleDrop = _F3L3FlowPointStatsAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 10),
    _F3L3FlowPointStatsAclRuleDrop_Type()
)
f3L3FlowPointStatsAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsAclRuleDrop.setStatus("current")
_F3L3FlowPointStatsTtlEqual1Drop_Type = PerfCounter64
_F3L3FlowPointStatsTtlEqual1Drop_Object = MibTableColumn
f3L3FlowPointStatsTtlEqual1Drop = _F3L3FlowPointStatsTtlEqual1Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 11),
    _F3L3FlowPointStatsTtlEqual1Drop_Type()
)
f3L3FlowPointStatsTtlEqual1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsTtlEqual1Drop.setStatus("current")
_F3L3FlowPointStatsFrameTx_Type = PerfCounter64
_F3L3FlowPointStatsFrameTx_Object = MibTableColumn
f3L3FlowPointStatsFrameTx = _F3L3FlowPointStatsFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 12),
    _F3L3FlowPointStatsFrameTx_Type()
)
f3L3FlowPointStatsFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFrameTx.setStatus("current")
_F3L3FlowPointStatsFrameRx_Type = PerfCounter64
_F3L3FlowPointStatsFrameRx_Object = MibTableColumn
f3L3FlowPointStatsFrameRx = _F3L3FlowPointStatsFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 13),
    _F3L3FlowPointStatsFrameRx_Type()
)
f3L3FlowPointStatsFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFrameRx.setStatus("current")
_F3L3FlowPointStatsNoRouteDrop_Type = PerfCounter64
_F3L3FlowPointStatsNoRouteDrop_Object = MibTableColumn
f3L3FlowPointStatsNoRouteDrop = _F3L3FlowPointStatsNoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 14),
    _F3L3FlowPointStatsNoRouteDrop_Type()
)
f3L3FlowPointStatsNoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsNoRouteDrop.setStatus("current")
_F3L3FlowPointHistoryTable_Object = MibTable
f3L3FlowPointHistoryTable = _F3L3FlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2)
)
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryTable.setStatus("current")
_F3L3FlowPointHistoryEntry_Object = MibTableRow
f3L3FlowPointHistoryEntry = _F3L3FlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1)
)
f3L3FlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointStatsIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryEntry.setStatus("current")


class _F3L3FlowPointHistoryIndex_Type(Integer32):
    """Custom type f3L3FlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3FlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3L3FlowPointHistoryIndex_Object = MibTableColumn
f3L3FlowPointHistoryIndex = _F3L3FlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 1),
    _F3L3FlowPointHistoryIndex_Type()
)
f3L3FlowPointHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryIndex.setStatus("current")
_F3L3FlowPointHistoryTime_Type = DateAndTime
_F3L3FlowPointHistoryTime_Object = MibTableColumn
f3L3FlowPointHistoryTime = _F3L3FlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 2),
    _F3L3FlowPointHistoryTime_Type()
)
f3L3FlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryTime.setStatus("current")
_F3L3FlowPointHistoryValid_Type = TruthValue
_F3L3FlowPointHistoryValid_Object = MibTableColumn
f3L3FlowPointHistoryValid = _F3L3FlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 3),
    _F3L3FlowPointHistoryValid_Type()
)
f3L3FlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryValid.setStatus("current")
_F3L3FlowPointHistoryAction_Type = CmPmBinAction
_F3L3FlowPointHistoryAction_Object = MibTableColumn
f3L3FlowPointHistoryAction = _F3L3FlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 4),
    _F3L3FlowPointHistoryAction_Type()
)
f3L3FlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryAction.setStatus("current")
_F3L3FlowPointHistoryFMG_Type = PerfCounter64
_F3L3FlowPointHistoryFMG_Object = MibTableColumn
f3L3FlowPointHistoryFMG = _F3L3FlowPointHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 5),
    _F3L3FlowPointHistoryFMG_Type()
)
f3L3FlowPointHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFMG.setStatus("current")
_F3L3FlowPointHistoryFMY_Type = PerfCounter64
_F3L3FlowPointHistoryFMY_Object = MibTableColumn
f3L3FlowPointHistoryFMY = _F3L3FlowPointHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 6),
    _F3L3FlowPointHistoryFMY_Type()
)
f3L3FlowPointHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFMY.setStatus("current")
_F3L3FlowPointHistoryFMRD_Type = PerfCounter64
_F3L3FlowPointHistoryFMRD_Object = MibTableColumn
f3L3FlowPointHistoryFMRD = _F3L3FlowPointHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 7),
    _F3L3FlowPointHistoryFMRD_Type()
)
f3L3FlowPointHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFMRD.setStatus("current")
_F3L3FlowPointHistoryFTD_Type = PerfCounter64
_F3L3FlowPointHistoryFTD_Object = MibTableColumn
f3L3FlowPointHistoryFTD = _F3L3FlowPointHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 8),
    _F3L3FlowPointHistoryFTD_Type()
)
f3L3FlowPointHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFTD.setStatus("current")
_F3L3FlowPointHistoryFragmentedDropAcl_Type = PerfCounter64
_F3L3FlowPointHistoryFragmentedDropAcl_Object = MibTableColumn
f3L3FlowPointHistoryFragmentedDropAcl = _F3L3FlowPointHistoryFragmentedDropAcl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 9),
    _F3L3FlowPointHistoryFragmentedDropAcl_Type()
)
f3L3FlowPointHistoryFragmentedDropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFragmentedDropAcl.setStatus("current")
_F3L3FlowPointHistoryAclRuleDrop_Type = PerfCounter64
_F3L3FlowPointHistoryAclRuleDrop_Object = MibTableColumn
f3L3FlowPointHistoryAclRuleDrop = _F3L3FlowPointHistoryAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 10),
    _F3L3FlowPointHistoryAclRuleDrop_Type()
)
f3L3FlowPointHistoryAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryAclRuleDrop.setStatus("current")
_F3L3FlowPointHistoryTtlEqual1Drop_Type = PerfCounter64
_F3L3FlowPointHistoryTtlEqual1Drop_Object = MibTableColumn
f3L3FlowPointHistoryTtlEqual1Drop = _F3L3FlowPointHistoryTtlEqual1Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 11),
    _F3L3FlowPointHistoryTtlEqual1Drop_Type()
)
f3L3FlowPointHistoryTtlEqual1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryTtlEqual1Drop.setStatus("current")
_F3L3FlowPointHistoryFrameTx_Type = PerfCounter64
_F3L3FlowPointHistoryFrameTx_Object = MibTableColumn
f3L3FlowPointHistoryFrameTx = _F3L3FlowPointHistoryFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 12),
    _F3L3FlowPointHistoryFrameTx_Type()
)
f3L3FlowPointHistoryFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFrameTx.setStatus("current")
_F3L3FlowPointHistoryFrameRx_Type = PerfCounter64
_F3L3FlowPointHistoryFrameRx_Object = MibTableColumn
f3L3FlowPointHistoryFrameRx = _F3L3FlowPointHistoryFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 13),
    _F3L3FlowPointHistoryFrameRx_Type()
)
f3L3FlowPointHistoryFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFrameRx.setStatus("current")
_F3L3FlowPointHistoryNoRouteDrop_Type = PerfCounter64
_F3L3FlowPointHistoryNoRouteDrop_Object = MibTableColumn
f3L3FlowPointHistoryNoRouteDrop = _F3L3FlowPointHistoryNoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 14),
    _F3L3FlowPointHistoryNoRouteDrop_Type()
)
f3L3FlowPointHistoryNoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryNoRouteDrop.setStatus("current")
_F3L3FlowPointThresholdTable_Object = MibTable
f3L3FlowPointThresholdTable = _F3L3FlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3)
)
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdTable.setStatus("current")
_F3L3FlowPointThresholdEntry_Object = MibTableRow
f3L3FlowPointThresholdEntry = _F3L3FlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1)
)
f3L3FlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointStatsIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdEntry.setStatus("current")


class _F3L3FlowPointThresholdIndex_Type(Integer32):
    """Custom type f3L3FlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3FlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3L3FlowPointThresholdIndex_Object = MibTableColumn
f3L3FlowPointThresholdIndex = _F3L3FlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 1),
    _F3L3FlowPointThresholdIndex_Type()
)
f3L3FlowPointThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdIndex.setStatus("current")
_F3L3FlowPointThresholdInterval_Type = CmPmIntervalType
_F3L3FlowPointThresholdInterval_Object = MibTableColumn
f3L3FlowPointThresholdInterval = _F3L3FlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 2),
    _F3L3FlowPointThresholdInterval_Type()
)
f3L3FlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdInterval.setStatus("current")
_F3L3FlowPointThresholdVariable_Type = VariablePointer
_F3L3FlowPointThresholdVariable_Object = MibTableColumn
f3L3FlowPointThresholdVariable = _F3L3FlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 3),
    _F3L3FlowPointThresholdVariable_Type()
)
f3L3FlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdVariable.setStatus("current")
_F3L3FlowPointThresholdValueLo_Type = Unsigned32
_F3L3FlowPointThresholdValueLo_Object = MibTableColumn
f3L3FlowPointThresholdValueLo = _F3L3FlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 4),
    _F3L3FlowPointThresholdValueLo_Type()
)
f3L3FlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdValueLo.setStatus("current")
_F3L3FlowPointThresholdValueHi_Type = Unsigned32
_F3L3FlowPointThresholdValueHi_Object = MibTableColumn
f3L3FlowPointThresholdValueHi = _F3L3FlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 5),
    _F3L3FlowPointThresholdValueHi_Type()
)
f3L3FlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdValueHi.setStatus("current")
_F3L3FlowPointThresholdMonValue_Type = Counter64
_F3L3FlowPointThresholdMonValue_Object = MibTableColumn
f3L3FlowPointThresholdMonValue = _F3L3FlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 6),
    _F3L3FlowPointThresholdMonValue_Type()
)
f3L3FlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdMonValue.setStatus("current")
_F3L3TrafficIpInterfaceStatsTable_Object = MibTable
f3L3TrafficIpInterfaceStatsTable = _F3L3TrafficIpInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsTable.setStatus("current")
_F3L3TrafficIpInterfaceStatsEntry_Object = MibTableRow
f3L3TrafficIpInterfaceStatsEntry = _F3L3TrafficIpInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1)
)
f3L3TrafficIpInterfaceStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsEntry.setStatus("current")


class _F3L3TrafficIpInterfaceStatsIndex_Type(Integer32):
    """Custom type f3L3TrafficIpInterfaceStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3TrafficIpInterfaceStatsIndex_Type.__name__ = "Integer32"
_F3L3TrafficIpInterfaceStatsIndex_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIndex = _F3L3TrafficIpInterfaceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 1),
    _F3L3TrafficIpInterfaceStatsIndex_Type()
)
f3L3TrafficIpInterfaceStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIndex.setStatus("current")
_F3L3TrafficIpInterfaceStatsIntervalType_Type = CmPmIntervalType
_F3L3TrafficIpInterfaceStatsIntervalType_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIntervalType = _F3L3TrafficIpInterfaceStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 2),
    _F3L3TrafficIpInterfaceStatsIntervalType_Type()
)
f3L3TrafficIpInterfaceStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIntervalType.setStatus("current")
_F3L3TrafficIpInterfaceStatsValid_Type = TruthValue
_F3L3TrafficIpInterfaceStatsValid_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsValid = _F3L3TrafficIpInterfaceStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 3),
    _F3L3TrafficIpInterfaceStatsValid_Type()
)
f3L3TrafficIpInterfaceStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsValid.setStatus("current")
_F3L3TrafficIpInterfaceStatsAction_Type = CmPmBinAction
_F3L3TrafficIpInterfaceStatsAction_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsAction = _F3L3TrafficIpInterfaceStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 4),
    _F3L3TrafficIpInterfaceStatsAction_Type()
)
f3L3TrafficIpInterfaceStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsAction.setStatus("current")
_F3L3TrafficIpInterfaceStatsDhcpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsDhcpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsDhcpTx = _F3L3TrafficIpInterfaceStatsDhcpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 5),
    _F3L3TrafficIpInterfaceStatsDhcpTx_Type()
)
f3L3TrafficIpInterfaceStatsDhcpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsDhcpTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsDhcpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsDhcpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsDhcpRx = _F3L3TrafficIpInterfaceStatsDhcpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 6),
    _F3L3TrafficIpInterfaceStatsDhcpRx_Type()
)
f3L3TrafficIpInterfaceStatsDhcpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsDhcpRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsIcmpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsIcmpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIcmpTx = _F3L3TrafficIpInterfaceStatsIcmpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 7),
    _F3L3TrafficIpInterfaceStatsIcmpTx_Type()
)
f3L3TrafficIpInterfaceStatsIcmpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIcmpTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsIcmpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsIcmpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIcmpRx = _F3L3TrafficIpInterfaceStatsIcmpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 8),
    _F3L3TrafficIpInterfaceStatsIcmpRx_Type()
)
f3L3TrafficIpInterfaceStatsIcmpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIcmpRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReqTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReqTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReqTx = _F3L3TrafficIpInterfaceStatsArpReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 9),
    _F3L3TrafficIpInterfaceStatsArpReqTx_Type()
)
f3L3TrafficIpInterfaceStatsArpReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReqTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReqRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReqRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReqRx = _F3L3TrafficIpInterfaceStatsArpReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 10),
    _F3L3TrafficIpInterfaceStatsArpReqRx_Type()
)
f3L3TrafficIpInterfaceStatsArpReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReqRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReplyTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReplyTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReplyTx = _F3L3TrafficIpInterfaceStatsArpReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 11),
    _F3L3TrafficIpInterfaceStatsArpReplyTx_Type()
)
f3L3TrafficIpInterfaceStatsArpReplyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReplyTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReplyRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReplyRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReplyRx = _F3L3TrafficIpInterfaceStatsArpReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 12),
    _F3L3TrafficIpInterfaceStatsArpReplyRx_Type()
)
f3L3TrafficIpInterfaceStatsArpReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReplyRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryTable_Object = MibTable
f3L3TrafficIpInterfaceHistoryTable = _F3L3TrafficIpInterfaceHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryTable.setStatus("current")
_F3L3TrafficIpInterfaceHistoryEntry_Object = MibTableRow
f3L3TrafficIpInterfaceHistoryEntry = _F3L3TrafficIpInterfaceHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1)
)
f3L3TrafficIpInterfaceHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryEntry.setStatus("current")


class _F3L3TrafficIpInterfaceHistoryIndex_Type(Integer32):
    """Custom type f3L3TrafficIpInterfaceHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3TrafficIpInterfaceHistoryIndex_Type.__name__ = "Integer32"
_F3L3TrafficIpInterfaceHistoryIndex_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIndex = _F3L3TrafficIpInterfaceHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 1),
    _F3L3TrafficIpInterfaceHistoryIndex_Type()
)
f3L3TrafficIpInterfaceHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIndex.setStatus("current")
_F3L3TrafficIpInterfaceHistoryTime_Type = DateAndTime
_F3L3TrafficIpInterfaceHistoryTime_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryTime = _F3L3TrafficIpInterfaceHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 2),
    _F3L3TrafficIpInterfaceHistoryTime_Type()
)
f3L3TrafficIpInterfaceHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryTime.setStatus("current")
_F3L3TrafficIpInterfaceHistoryValid_Type = TruthValue
_F3L3TrafficIpInterfaceHistoryValid_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryValid = _F3L3TrafficIpInterfaceHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 3),
    _F3L3TrafficIpInterfaceHistoryValid_Type()
)
f3L3TrafficIpInterfaceHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryValid.setStatus("current")
_F3L3TrafficIpInterfaceHistoryAction_Type = CmPmBinAction
_F3L3TrafficIpInterfaceHistoryAction_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryAction = _F3L3TrafficIpInterfaceHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 4),
    _F3L3TrafficIpInterfaceHistoryAction_Type()
)
f3L3TrafficIpInterfaceHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryAction.setStatus("current")
_F3L3TrafficIpInterfaceHistoryDhcpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryDhcpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryDhcpTx = _F3L3TrafficIpInterfaceHistoryDhcpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 5),
    _F3L3TrafficIpInterfaceHistoryDhcpTx_Type()
)
f3L3TrafficIpInterfaceHistoryDhcpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryDhcpTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryDhcpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryDhcpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryDhcpRx = _F3L3TrafficIpInterfaceHistoryDhcpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 6),
    _F3L3TrafficIpInterfaceHistoryDhcpRx_Type()
)
f3L3TrafficIpInterfaceHistoryDhcpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryDhcpRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryIcmpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryIcmpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIcmpTx = _F3L3TrafficIpInterfaceHistoryIcmpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 7),
    _F3L3TrafficIpInterfaceHistoryIcmpTx_Type()
)
f3L3TrafficIpInterfaceHistoryIcmpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIcmpTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryIcmpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryIcmpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIcmpRx = _F3L3TrafficIpInterfaceHistoryIcmpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 8),
    _F3L3TrafficIpInterfaceHistoryIcmpRx_Type()
)
f3L3TrafficIpInterfaceHistoryIcmpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIcmpRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReqTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReqTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReqTx = _F3L3TrafficIpInterfaceHistoryArpReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 9),
    _F3L3TrafficIpInterfaceHistoryArpReqTx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReqTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReqRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReqRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReqRx = _F3L3TrafficIpInterfaceHistoryArpReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 10),
    _F3L3TrafficIpInterfaceHistoryArpReqRx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReqRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReplyTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReplyTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReplyTx = _F3L3TrafficIpInterfaceHistoryArpReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 11),
    _F3L3TrafficIpInterfaceHistoryArpReplyTx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReplyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReplyTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReplyRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReplyRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReplyRx = _F3L3TrafficIpInterfaceHistoryArpReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 12),
    _F3L3TrafficIpInterfaceHistoryArpReplyRx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReplyRx.setStatus("current")
_F3L3TrafficIpInterfaceThresholdTable_Object = MibTable
f3L3TrafficIpInterfaceThresholdTable = _F3L3TrafficIpInterfaceThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdTable.setStatus("current")
_F3L3TrafficIpInterfaceThresholdEntry_Object = MibTableRow
f3L3TrafficIpInterfaceThresholdEntry = _F3L3TrafficIpInterfaceThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1)
)
f3L3TrafficIpInterfaceThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdEntry.setStatus("current")


class _F3L3TrafficIpInterfaceThresholdIndex_Type(Integer32):
    """Custom type f3L3TrafficIpInterfaceThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3TrafficIpInterfaceThresholdIndex_Type.__name__ = "Integer32"
_F3L3TrafficIpInterfaceThresholdIndex_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdIndex = _F3L3TrafficIpInterfaceThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 1),
    _F3L3TrafficIpInterfaceThresholdIndex_Type()
)
f3L3TrafficIpInterfaceThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdIndex.setStatus("current")
_F3L3TrafficIpInterfaceThresholdInterval_Type = CmPmIntervalType
_F3L3TrafficIpInterfaceThresholdInterval_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdInterval = _F3L3TrafficIpInterfaceThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 2),
    _F3L3TrafficIpInterfaceThresholdInterval_Type()
)
f3L3TrafficIpInterfaceThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdInterval.setStatus("current")
_F3L3TrafficIpInterfaceThresholdVariable_Type = VariablePointer
_F3L3TrafficIpInterfaceThresholdVariable_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdVariable = _F3L3TrafficIpInterfaceThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 3),
    _F3L3TrafficIpInterfaceThresholdVariable_Type()
)
f3L3TrafficIpInterfaceThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdVariable.setStatus("current")
_F3L3TrafficIpInterfaceThresholdValueLo_Type = Unsigned32
_F3L3TrafficIpInterfaceThresholdValueLo_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdValueLo = _F3L3TrafficIpInterfaceThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 4),
    _F3L3TrafficIpInterfaceThresholdValueLo_Type()
)
f3L3TrafficIpInterfaceThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdValueLo.setStatus("current")
_F3L3TrafficIpInterfaceThresholdValueHi_Type = Unsigned32
_F3L3TrafficIpInterfaceThresholdValueHi_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdValueHi = _F3L3TrafficIpInterfaceThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 5),
    _F3L3TrafficIpInterfaceThresholdValueHi_Type()
)
f3L3TrafficIpInterfaceThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdValueHi.setStatus("current")
_F3L3TrafficIpInterfaceThresholdMonValue_Type = Counter64
_F3L3TrafficIpInterfaceThresholdMonValue_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdMonValue = _F3L3TrafficIpInterfaceThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 6),
    _F3L3TrafficIpInterfaceThresholdMonValue_Type()
)
f3L3TrafficIpInterfaceThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdMonValue.setStatus("current")
_F3L3AclRuleStatsTable_Object = MibTable
f3L3AclRuleStatsTable = _F3L3AclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7)
)
if mibBuilder.loadTexts:
    f3L3AclRuleStatsTable.setStatus("current")
_F3L3AclRuleStatsEntry_Object = MibTableRow
f3L3AclRuleStatsEntry = _F3L3AclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1)
)
f3L3AclRuleStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleStatsEntry.setStatus("current")


class _F3L3AclRuleStatsIndex_Type(Integer32):
    """Custom type f3L3AclRuleStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3AclRuleStatsIndex_Type.__name__ = "Integer32"
_F3L3AclRuleStatsIndex_Object = MibTableColumn
f3L3AclRuleStatsIndex = _F3L3AclRuleStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 1),
    _F3L3AclRuleStatsIndex_Type()
)
f3L3AclRuleStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsIndex.setStatus("current")
_F3L3AclRuleStatsIntervalType_Type = CmPmIntervalType
_F3L3AclRuleStatsIntervalType_Object = MibTableColumn
f3L3AclRuleStatsIntervalType = _F3L3AclRuleStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 2),
    _F3L3AclRuleStatsIntervalType_Type()
)
f3L3AclRuleStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsIntervalType.setStatus("current")
_F3L3AclRuleStatsValid_Type = TruthValue
_F3L3AclRuleStatsValid_Object = MibTableColumn
f3L3AclRuleStatsValid = _F3L3AclRuleStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 3),
    _F3L3AclRuleStatsValid_Type()
)
f3L3AclRuleStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsValid.setStatus("current")
_F3L3AclRuleStatsAction_Type = CmPmBinAction
_F3L3AclRuleStatsAction_Object = MibTableColumn
f3L3AclRuleStatsAction = _F3L3AclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 4),
    _F3L3AclRuleStatsAction_Type()
)
f3L3AclRuleStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsAction.setStatus("current")
_F3L3AclRuleStatsRuleMatch_Type = PerfCounter64
_F3L3AclRuleStatsRuleMatch_Object = MibTableColumn
f3L3AclRuleStatsRuleMatch = _F3L3AclRuleStatsRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 5),
    _F3L3AclRuleStatsRuleMatch_Type()
)
f3L3AclRuleStatsRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsRuleMatch.setStatus("current")
_F3L3AclRuleHistoryTable_Object = MibTable
f3L3AclRuleHistoryTable = _F3L3AclRuleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8)
)
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryTable.setStatus("current")
_F3L3AclRuleHistoryEntry_Object = MibTableRow
f3L3AclRuleHistoryEntry = _F3L3AclRuleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1)
)
f3L3AclRuleHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryEntry.setStatus("current")


class _F3L3AclRuleHistoryIndex_Type(Integer32):
    """Custom type f3L3AclRuleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3AclRuleHistoryIndex_Type.__name__ = "Integer32"
_F3L3AclRuleHistoryIndex_Object = MibTableColumn
f3L3AclRuleHistoryIndex = _F3L3AclRuleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 1),
    _F3L3AclRuleHistoryIndex_Type()
)
f3L3AclRuleHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryIndex.setStatus("current")
_F3L3AclRuleHistoryTime_Type = DateAndTime
_F3L3AclRuleHistoryTime_Object = MibTableColumn
f3L3AclRuleHistoryTime = _F3L3AclRuleHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 2),
    _F3L3AclRuleHistoryTime_Type()
)
f3L3AclRuleHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryTime.setStatus("current")
_F3L3AclRuleHistoryValid_Type = TruthValue
_F3L3AclRuleHistoryValid_Object = MibTableColumn
f3L3AclRuleHistoryValid = _F3L3AclRuleHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 3),
    _F3L3AclRuleHistoryValid_Type()
)
f3L3AclRuleHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryValid.setStatus("current")
_F3L3AclRuleHistoryAction_Type = CmPmBinAction
_F3L3AclRuleHistoryAction_Object = MibTableColumn
f3L3AclRuleHistoryAction = _F3L3AclRuleHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 4),
    _F3L3AclRuleHistoryAction_Type()
)
f3L3AclRuleHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryAction.setStatus("current")
_F3L3AclRuleHistoryRuleMatch_Type = PerfCounter64
_F3L3AclRuleHistoryRuleMatch_Object = MibTableColumn
f3L3AclRuleHistoryRuleMatch = _F3L3AclRuleHistoryRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 5),
    _F3L3AclRuleHistoryRuleMatch_Type()
)
f3L3AclRuleHistoryRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryRuleMatch.setStatus("current")
_F3L3AclRuleThresholdTable_Object = MibTable
f3L3AclRuleThresholdTable = _F3L3AclRuleThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9)
)
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdTable.setStatus("current")
_F3L3AclRuleThresholdEntry_Object = MibTableRow
f3L3AclRuleThresholdEntry = _F3L3AclRuleThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1)
)
f3L3AclRuleThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdEntry.setStatus("current")


class _F3L3AclRuleThresholdIndex_Type(Integer32):
    """Custom type f3L3AclRuleThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3AclRuleThresholdIndex_Type.__name__ = "Integer32"
_F3L3AclRuleThresholdIndex_Object = MibTableColumn
f3L3AclRuleThresholdIndex = _F3L3AclRuleThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 1),
    _F3L3AclRuleThresholdIndex_Type()
)
f3L3AclRuleThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdIndex.setStatus("current")
_F3L3AclRuleThresholdInterval_Type = CmPmIntervalType
_F3L3AclRuleThresholdInterval_Object = MibTableColumn
f3L3AclRuleThresholdInterval = _F3L3AclRuleThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 2),
    _F3L3AclRuleThresholdInterval_Type()
)
f3L3AclRuleThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdInterval.setStatus("current")
_F3L3AclRuleThresholdVariable_Type = VariablePointer
_F3L3AclRuleThresholdVariable_Object = MibTableColumn
f3L3AclRuleThresholdVariable = _F3L3AclRuleThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 3),
    _F3L3AclRuleThresholdVariable_Type()
)
f3L3AclRuleThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdVariable.setStatus("current")
_F3L3AclRuleThresholdValueLo_Type = Unsigned32
_F3L3AclRuleThresholdValueLo_Object = MibTableColumn
f3L3AclRuleThresholdValueLo = _F3L3AclRuleThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 4),
    _F3L3AclRuleThresholdValueLo_Type()
)
f3L3AclRuleThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdValueLo.setStatus("current")
_F3L3AclRuleThresholdValueHi_Type = Unsigned32
_F3L3AclRuleThresholdValueHi_Object = MibTableColumn
f3L3AclRuleThresholdValueHi = _F3L3AclRuleThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 5),
    _F3L3AclRuleThresholdValueHi_Type()
)
f3L3AclRuleThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdValueHi.setStatus("current")
_F3L3AclRuleThresholdMonValue_Type = Counter64
_F3L3AclRuleThresholdMonValue_Object = MibTableColumn
f3L3AclRuleThresholdMonValue = _F3L3AclRuleThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 6),
    _F3L3AclRuleThresholdMonValue_Type()
)
f3L3AclRuleThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdMonValue.setStatus("current")
_F3L3QosPolicerStatsTable_Object = MibTable
f3L3QosPolicerStatsTable = _F3L3QosPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsTable.setStatus("current")
_F3L3QosPolicerStatsEntry_Object = MibTableRow
f3L3QosPolicerStatsEntry = _F3L3QosPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1)
)
f3L3QosPolicerStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsEntry.setStatus("current")


class _F3L3QosPolicerStatsIndex_Type(Integer32):
    """Custom type f3L3QosPolicerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosPolicerStatsIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerStatsIndex_Object = MibTableColumn
f3L3QosPolicerStatsIndex = _F3L3QosPolicerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 1),
    _F3L3QosPolicerStatsIndex_Type()
)
f3L3QosPolicerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsIndex.setStatus("current")
_F3L3QosPolicerStatsIntervalType_Type = CmPmIntervalType
_F3L3QosPolicerStatsIntervalType_Object = MibTableColumn
f3L3QosPolicerStatsIntervalType = _F3L3QosPolicerStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 2),
    _F3L3QosPolicerStatsIntervalType_Type()
)
f3L3QosPolicerStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsIntervalType.setStatus("current")
_F3L3QosPolicerStatsValid_Type = TruthValue
_F3L3QosPolicerStatsValid_Object = MibTableColumn
f3L3QosPolicerStatsValid = _F3L3QosPolicerStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 3),
    _F3L3QosPolicerStatsValid_Type()
)
f3L3QosPolicerStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsValid.setStatus("current")
_F3L3QosPolicerStatsAction_Type = CmPmBinAction
_F3L3QosPolicerStatsAction_Object = MibTableColumn
f3L3QosPolicerStatsAction = _F3L3QosPolicerStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 4),
    _F3L3QosPolicerStatsAction_Type()
)
f3L3QosPolicerStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsAction.setStatus("current")
_F3L3QosPolicerStatsFMG_Type = PerfCounter64
_F3L3QosPolicerStatsFMG_Object = MibTableColumn
f3L3QosPolicerStatsFMG = _F3L3QosPolicerStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 5),
    _F3L3QosPolicerStatsFMG_Type()
)
f3L3QosPolicerStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMG.setStatus("current")
_F3L3QosPolicerStatsFMY_Type = PerfCounter64
_F3L3QosPolicerStatsFMY_Object = MibTableColumn
f3L3QosPolicerStatsFMY = _F3L3QosPolicerStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 6),
    _F3L3QosPolicerStatsFMY_Type()
)
f3L3QosPolicerStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMY.setStatus("current")
_F3L3QosPolicerStatsFMYD_Type = PerfCounter64
_F3L3QosPolicerStatsFMYD_Object = MibTableColumn
f3L3QosPolicerStatsFMYD = _F3L3QosPolicerStatsFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 7),
    _F3L3QosPolicerStatsFMYD_Type()
)
f3L3QosPolicerStatsFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMYD.setStatus("deprecated")
_F3L3QosPolicerStatsFMRD_Type = PerfCounter64
_F3L3QosPolicerStatsFMRD_Object = MibTableColumn
f3L3QosPolicerStatsFMRD = _F3L3QosPolicerStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 8),
    _F3L3QosPolicerStatsFMRD_Type()
)
f3L3QosPolicerStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMRD.setStatus("current")
_F3L3QosPolicerStatsBytesIn_Type = PerfCounter64
_F3L3QosPolicerStatsBytesIn_Object = MibTableColumn
f3L3QosPolicerStatsBytesIn = _F3L3QosPolicerStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 9),
    _F3L3QosPolicerStatsBytesIn_Type()
)
f3L3QosPolicerStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsBytesIn.setStatus("current")
_F3L3QosPolicerStatsBytesOut_Type = PerfCounter64
_F3L3QosPolicerStatsBytesOut_Object = MibTableColumn
f3L3QosPolicerStatsBytesOut = _F3L3QosPolicerStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 10),
    _F3L3QosPolicerStatsBytesOut_Type()
)
f3L3QosPolicerStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsBytesOut.setStatus("current")
_F3L3QosPolicerStatsABR_Type = PerfCounter64
_F3L3QosPolicerStatsABR_Object = MibTableColumn
f3L3QosPolicerStatsABR = _F3L3QosPolicerStatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 11),
    _F3L3QosPolicerStatsABR_Type()
)
f3L3QosPolicerStatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsABR.setStatus("current")
_F3L3QosPolicerHistoryTable_Object = MibTable
f3L3QosPolicerHistoryTable = _F3L3QosPolicerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryTable.setStatus("current")
_F3L3QosPolicerHistoryEntry_Object = MibTableRow
f3L3QosPolicerHistoryEntry = _F3L3QosPolicerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1)
)
f3L3QosPolicerHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryEntry.setStatus("current")


class _F3L3QosPolicerHistoryIndex_Type(Integer32):
    """Custom type f3L3QosPolicerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosPolicerHistoryIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerHistoryIndex_Object = MibTableColumn
f3L3QosPolicerHistoryIndex = _F3L3QosPolicerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 1),
    _F3L3QosPolicerHistoryIndex_Type()
)
f3L3QosPolicerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryIndex.setStatus("current")
_F3L3QosPolicerHistoryTime_Type = DateAndTime
_F3L3QosPolicerHistoryTime_Object = MibTableColumn
f3L3QosPolicerHistoryTime = _F3L3QosPolicerHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 2),
    _F3L3QosPolicerHistoryTime_Type()
)
f3L3QosPolicerHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryTime.setStatus("current")
_F3L3QosPolicerHistoryValid_Type = TruthValue
_F3L3QosPolicerHistoryValid_Object = MibTableColumn
f3L3QosPolicerHistoryValid = _F3L3QosPolicerHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 3),
    _F3L3QosPolicerHistoryValid_Type()
)
f3L3QosPolicerHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryValid.setStatus("current")
_F3L3QosPolicerHistoryAction_Type = CmPmBinAction
_F3L3QosPolicerHistoryAction_Object = MibTableColumn
f3L3QosPolicerHistoryAction = _F3L3QosPolicerHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 4),
    _F3L3QosPolicerHistoryAction_Type()
)
f3L3QosPolicerHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryAction.setStatus("current")
_F3L3QosPolicerHistoryFMG_Type = PerfCounter64
_F3L3QosPolicerHistoryFMG_Object = MibTableColumn
f3L3QosPolicerHistoryFMG = _F3L3QosPolicerHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 5),
    _F3L3QosPolicerHistoryFMG_Type()
)
f3L3QosPolicerHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMG.setStatus("current")
_F3L3QosPolicerHistoryFMY_Type = PerfCounter64
_F3L3QosPolicerHistoryFMY_Object = MibTableColumn
f3L3QosPolicerHistoryFMY = _F3L3QosPolicerHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 6),
    _F3L3QosPolicerHistoryFMY_Type()
)
f3L3QosPolicerHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMY.setStatus("current")
_F3L3QosPolicerHistoryFMYD_Type = PerfCounter64
_F3L3QosPolicerHistoryFMYD_Object = MibTableColumn
f3L3QosPolicerHistoryFMYD = _F3L3QosPolicerHistoryFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 7),
    _F3L3QosPolicerHistoryFMYD_Type()
)
f3L3QosPolicerHistoryFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMYD.setStatus("deprecated")
_F3L3QosPolicerHistoryFMRD_Type = PerfCounter64
_F3L3QosPolicerHistoryFMRD_Object = MibTableColumn
f3L3QosPolicerHistoryFMRD = _F3L3QosPolicerHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 8),
    _F3L3QosPolicerHistoryFMRD_Type()
)
f3L3QosPolicerHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMRD.setStatus("current")
_F3L3QosPolicerHistoryBytesIn_Type = PerfCounter64
_F3L3QosPolicerHistoryBytesIn_Object = MibTableColumn
f3L3QosPolicerHistoryBytesIn = _F3L3QosPolicerHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 9),
    _F3L3QosPolicerHistoryBytesIn_Type()
)
f3L3QosPolicerHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryBytesIn.setStatus("current")
_F3L3QosPolicerHistoryBytesOut_Type = PerfCounter64
_F3L3QosPolicerHistoryBytesOut_Object = MibTableColumn
f3L3QosPolicerHistoryBytesOut = _F3L3QosPolicerHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 10),
    _F3L3QosPolicerHistoryBytesOut_Type()
)
f3L3QosPolicerHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryBytesOut.setStatus("current")
_F3L3QosPolicerHistoryABR_Type = PerfCounter64
_F3L3QosPolicerHistoryABR_Object = MibTableColumn
f3L3QosPolicerHistoryABR = _F3L3QosPolicerHistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 11),
    _F3L3QosPolicerHistoryABR_Type()
)
f3L3QosPolicerHistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryABR.setStatus("current")
_F3L3QosPolicerThresholdTable_Object = MibTable
f3L3QosPolicerThresholdTable = _F3L3QosPolicerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdTable.setStatus("current")
_F3L3QosPolicerThresholdEntry_Object = MibTableRow
f3L3QosPolicerThresholdEntry = _F3L3QosPolicerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1)
)
f3L3QosPolicerThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdEntry.setStatus("current")


class _F3L3QosPolicerThresholdIndex_Type(Integer32):
    """Custom type f3L3QosPolicerThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosPolicerThresholdIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerThresholdIndex_Object = MibTableColumn
f3L3QosPolicerThresholdIndex = _F3L3QosPolicerThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 1),
    _F3L3QosPolicerThresholdIndex_Type()
)
f3L3QosPolicerThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdIndex.setStatus("current")
_F3L3QosPolicerThresholdInterval_Type = CmPmIntervalType
_F3L3QosPolicerThresholdInterval_Object = MibTableColumn
f3L3QosPolicerThresholdInterval = _F3L3QosPolicerThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 2),
    _F3L3QosPolicerThresholdInterval_Type()
)
f3L3QosPolicerThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdInterval.setStatus("current")
_F3L3QosPolicerThresholdVariable_Type = VariablePointer
_F3L3QosPolicerThresholdVariable_Object = MibTableColumn
f3L3QosPolicerThresholdVariable = _F3L3QosPolicerThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 3),
    _F3L3QosPolicerThresholdVariable_Type()
)
f3L3QosPolicerThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdVariable.setStatus("current")
_F3L3QosPolicerThresholdValueLo_Type = Unsigned32
_F3L3QosPolicerThresholdValueLo_Object = MibTableColumn
f3L3QosPolicerThresholdValueLo = _F3L3QosPolicerThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 4),
    _F3L3QosPolicerThresholdValueLo_Type()
)
f3L3QosPolicerThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdValueLo.setStatus("current")
_F3L3QosPolicerThresholdValueHi_Type = Unsigned32
_F3L3QosPolicerThresholdValueHi_Object = MibTableColumn
f3L3QosPolicerThresholdValueHi = _F3L3QosPolicerThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 5),
    _F3L3QosPolicerThresholdValueHi_Type()
)
f3L3QosPolicerThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdValueHi.setStatus("current")
_F3L3QosPolicerThresholdMonValue_Type = Counter64
_F3L3QosPolicerThresholdMonValue_Object = MibTableColumn
f3L3QosPolicerThresholdMonValue = _F3L3QosPolicerThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 6),
    _F3L3QosPolicerThresholdMonValue_Type()
)
f3L3QosPolicerThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdMonValue.setStatus("current")
_F3L3QosShaperStatsTable_Object = MibTable
f3L3QosShaperStatsTable = _F3L3QosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13)
)
if mibBuilder.loadTexts:
    f3L3QosShaperStatsTable.setStatus("current")
_F3L3QosShaperStatsEntry_Object = MibTableRow
f3L3QosShaperStatsEntry = _F3L3QosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1)
)
f3L3QosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperStatsEntry.setStatus("current")


class _F3L3QosShaperStatsIndex_Type(Integer32):
    """Custom type f3L3QosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosShaperStatsIndex_Type.__name__ = "Integer32"
_F3L3QosShaperStatsIndex_Object = MibTableColumn
f3L3QosShaperStatsIndex = _F3L3QosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 1),
    _F3L3QosShaperStatsIndex_Type()
)
f3L3QosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsIndex.setStatus("current")
_F3L3QosShaperStatsIntervalType_Type = CmPmIntervalType
_F3L3QosShaperStatsIntervalType_Object = MibTableColumn
f3L3QosShaperStatsIntervalType = _F3L3QosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 2),
    _F3L3QosShaperStatsIntervalType_Type()
)
f3L3QosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsIntervalType.setStatus("current")
_F3L3QosShaperStatsValid_Type = TruthValue
_F3L3QosShaperStatsValid_Object = MibTableColumn
f3L3QosShaperStatsValid = _F3L3QosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 3),
    _F3L3QosShaperStatsValid_Type()
)
f3L3QosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsValid.setStatus("current")
_F3L3QosShaperStatsAction_Type = CmPmBinAction
_F3L3QosShaperStatsAction_Object = MibTableColumn
f3L3QosShaperStatsAction = _F3L3QosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 4),
    _F3L3QosShaperStatsAction_Type()
)
f3L3QosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsAction.setStatus("current")
_F3L3QosShaperStatsBT_Type = PerfCounter64
_F3L3QosShaperStatsBT_Object = MibTableColumn
f3L3QosShaperStatsBT = _F3L3QosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 5),
    _F3L3QosShaperStatsBT_Type()
)
f3L3QosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBT.setStatus("current")
_F3L3QosShaperStatsBTD_Type = PerfCounter64
_F3L3QosShaperStatsBTD_Object = MibTableColumn
f3L3QosShaperStatsBTD = _F3L3QosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 6),
    _F3L3QosShaperStatsBTD_Type()
)
f3L3QosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBTD.setStatus("current")
_F3L3QosShaperStatsFD_Type = PerfCounter64
_F3L3QosShaperStatsFD_Object = MibTableColumn
f3L3QosShaperStatsFD = _F3L3QosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 7),
    _F3L3QosShaperStatsFD_Type()
)
f3L3QosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFD.setStatus("current")
_F3L3QosShaperStatsFTD_Type = PerfCounter64
_F3L3QosShaperStatsFTD_Object = MibTableColumn
f3L3QosShaperStatsFTD = _F3L3QosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 8),
    _F3L3QosShaperStatsFTD_Type()
)
f3L3QosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFTD.setStatus("current")
_F3L3QosShaperStatsBR_Type = PerfCounter64
_F3L3QosShaperStatsBR_Object = MibTableColumn
f3L3QosShaperStatsBR = _F3L3QosShaperStatsBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 9),
    _F3L3QosShaperStatsBR_Type()
)
f3L3QosShaperStatsBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBR.setStatus("current")
_F3L3QosShaperStatsFR_Type = PerfCounter64
_F3L3QosShaperStatsFR_Object = MibTableColumn
f3L3QosShaperStatsFR = _F3L3QosShaperStatsFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 10),
    _F3L3QosShaperStatsFR_Type()
)
f3L3QosShaperStatsFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFR.setStatus("current")
_F3L3QosShaperStatsABRRL_Type = PerfCounter64
_F3L3QosShaperStatsABRRL_Object = MibTableColumn
f3L3QosShaperStatsABRRL = _F3L3QosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 11),
    _F3L3QosShaperStatsABRRL_Type()
)
f3L3QosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsABRRL.setStatus("current")
_F3L3QosShaperStatsABRRLR_Type = PerfCounter64
_F3L3QosShaperStatsABRRLR_Object = MibTableColumn
f3L3QosShaperStatsABRRLR = _F3L3QosShaperStatsABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 12),
    _F3L3QosShaperStatsABRRLR_Type()
)
f3L3QosShaperStatsABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsABRRLR.setStatus("current")
_F3L3QosShaperStatsBREDD_Type = PerfCounter64
_F3L3QosShaperStatsBREDD_Object = MibTableColumn
f3L3QosShaperStatsBREDD = _F3L3QosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 13),
    _F3L3QosShaperStatsBREDD_Type()
)
f3L3QosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBREDD.setStatus("current")
_F3L3QosShaperStatsFREDD_Type = PerfCounter64
_F3L3QosShaperStatsFREDD_Object = MibTableColumn
f3L3QosShaperStatsFREDD = _F3L3QosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 14),
    _F3L3QosShaperStatsFREDD_Type()
)
f3L3QosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFREDD.setStatus("current")
_F3L3QosShaperHistoryTable_Object = MibTable
f3L3QosShaperHistoryTable = _F3L3QosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14)
)
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryTable.setStatus("current")
_F3L3QosShaperHistoryEntry_Object = MibTableRow
f3L3QosShaperHistoryEntry = _F3L3QosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1)
)
f3L3QosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryEntry.setStatus("current")


class _F3L3QosShaperHistoryIndex_Type(Integer32):
    """Custom type f3L3QosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosShaperHistoryIndex_Type.__name__ = "Integer32"
_F3L3QosShaperHistoryIndex_Object = MibTableColumn
f3L3QosShaperHistoryIndex = _F3L3QosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 1),
    _F3L3QosShaperHistoryIndex_Type()
)
f3L3QosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryIndex.setStatus("current")
_F3L3QosShaperHistoryTime_Type = DateAndTime
_F3L3QosShaperHistoryTime_Object = MibTableColumn
f3L3QosShaperHistoryTime = _F3L3QosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 2),
    _F3L3QosShaperHistoryTime_Type()
)
f3L3QosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryTime.setStatus("current")
_F3L3QosShaperHistoryValid_Type = TruthValue
_F3L3QosShaperHistoryValid_Object = MibTableColumn
f3L3QosShaperHistoryValid = _F3L3QosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 3),
    _F3L3QosShaperHistoryValid_Type()
)
f3L3QosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryValid.setStatus("current")
_F3L3QosShaperHistoryAction_Type = CmPmBinAction
_F3L3QosShaperHistoryAction_Object = MibTableColumn
f3L3QosShaperHistoryAction = _F3L3QosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 4),
    _F3L3QosShaperHistoryAction_Type()
)
f3L3QosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryAction.setStatus("current")
_F3L3QosShaperHistoryBT_Type = PerfCounter64
_F3L3QosShaperHistoryBT_Object = MibTableColumn
f3L3QosShaperHistoryBT = _F3L3QosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 5),
    _F3L3QosShaperHistoryBT_Type()
)
f3L3QosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBT.setStatus("current")
_F3L3QosShaperHistoryBTD_Type = PerfCounter64
_F3L3QosShaperHistoryBTD_Object = MibTableColumn
f3L3QosShaperHistoryBTD = _F3L3QosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 6),
    _F3L3QosShaperHistoryBTD_Type()
)
f3L3QosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBTD.setStatus("current")
_F3L3QosShaperHistoryFD_Type = PerfCounter64
_F3L3QosShaperHistoryFD_Object = MibTableColumn
f3L3QosShaperHistoryFD = _F3L3QosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 7),
    _F3L3QosShaperHistoryFD_Type()
)
f3L3QosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFD.setStatus("current")
_F3L3QosShaperHistoryFTD_Type = PerfCounter64
_F3L3QosShaperHistoryFTD_Object = MibTableColumn
f3L3QosShaperHistoryFTD = _F3L3QosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 8),
    _F3L3QosShaperHistoryFTD_Type()
)
f3L3QosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFTD.setStatus("current")
_F3L3QosShaperHistoryBR_Type = PerfCounter64
_F3L3QosShaperHistoryBR_Object = MibTableColumn
f3L3QosShaperHistoryBR = _F3L3QosShaperHistoryBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 9),
    _F3L3QosShaperHistoryBR_Type()
)
f3L3QosShaperHistoryBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBR.setStatus("current")
_F3L3QosShaperHistoryFR_Type = PerfCounter64
_F3L3QosShaperHistoryFR_Object = MibTableColumn
f3L3QosShaperHistoryFR = _F3L3QosShaperHistoryFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 10),
    _F3L3QosShaperHistoryFR_Type()
)
f3L3QosShaperHistoryFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFR.setStatus("current")
_F3L3QosShaperHistoryABRRL_Type = PerfCounter64
_F3L3QosShaperHistoryABRRL_Object = MibTableColumn
f3L3QosShaperHistoryABRRL = _F3L3QosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 11),
    _F3L3QosShaperHistoryABRRL_Type()
)
f3L3QosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryABRRL.setStatus("current")
_F3L3QosShaperHistoryABRRLR_Type = PerfCounter64
_F3L3QosShaperHistoryABRRLR_Object = MibTableColumn
f3L3QosShaperHistoryABRRLR = _F3L3QosShaperHistoryABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 12),
    _F3L3QosShaperHistoryABRRLR_Type()
)
f3L3QosShaperHistoryABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryABRRLR.setStatus("current")
_F3L3QosShaperHistoryBREDD_Type = PerfCounter64
_F3L3QosShaperHistoryBREDD_Object = MibTableColumn
f3L3QosShaperHistoryBREDD = _F3L3QosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 13),
    _F3L3QosShaperHistoryBREDD_Type()
)
f3L3QosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBREDD.setStatus("current")
_F3L3QosShaperHistoryFREDD_Type = PerfCounter64
_F3L3QosShaperHistoryFREDD_Object = MibTableColumn
f3L3QosShaperHistoryFREDD = _F3L3QosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 14),
    _F3L3QosShaperHistoryFREDD_Type()
)
f3L3QosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFREDD.setStatus("current")
_F3L3QosShaperThresholdTable_Object = MibTable
f3L3QosShaperThresholdTable = _F3L3QosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15)
)
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdTable.setStatus("current")
_F3L3QosShaperThresholdEntry_Object = MibTableRow
f3L3QosShaperThresholdEntry = _F3L3QosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1)
)
f3L3QosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdEntry.setStatus("current")


class _F3L3QosShaperThresholdIndex_Type(Integer32):
    """Custom type f3L3QosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosShaperThresholdIndex_Type.__name__ = "Integer32"
_F3L3QosShaperThresholdIndex_Object = MibTableColumn
f3L3QosShaperThresholdIndex = _F3L3QosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 1),
    _F3L3QosShaperThresholdIndex_Type()
)
f3L3QosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdIndex.setStatus("current")
_F3L3QosShaperThresholdInterval_Type = CmPmIntervalType
_F3L3QosShaperThresholdInterval_Object = MibTableColumn
f3L3QosShaperThresholdInterval = _F3L3QosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 2),
    _F3L3QosShaperThresholdInterval_Type()
)
f3L3QosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdInterval.setStatus("current")
_F3L3QosShaperThresholdVariable_Type = VariablePointer
_F3L3QosShaperThresholdVariable_Object = MibTableColumn
f3L3QosShaperThresholdVariable = _F3L3QosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 3),
    _F3L3QosShaperThresholdVariable_Type()
)
f3L3QosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdVariable.setStatus("current")
_F3L3QosShaperThresholdValueLo_Type = Unsigned32
_F3L3QosShaperThresholdValueLo_Object = MibTableColumn
f3L3QosShaperThresholdValueLo = _F3L3QosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 4),
    _F3L3QosShaperThresholdValueLo_Type()
)
f3L3QosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdValueLo.setStatus("current")
_F3L3QosShaperThresholdValueHi_Type = Unsigned32
_F3L3QosShaperThresholdValueHi_Object = MibTableColumn
f3L3QosShaperThresholdValueHi = _F3L3QosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 5),
    _F3L3QosShaperThresholdValueHi_Type()
)
f3L3QosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdValueHi.setStatus("current")
_F3L3QosShaperThresholdMonValue_Type = Counter64
_F3L3QosShaperThresholdMonValue_Object = MibTableColumn
f3L3QosShaperThresholdMonValue = _F3L3QosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 6),
    _F3L3QosShaperThresholdMonValue_Type()
)
f3L3QosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdMonValue.setStatus("current")
_F3L2A2NAclRuleStatsTable_Object = MibTable
f3L2A2NAclRuleStatsTable = _F3L2A2NAclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsTable.setStatus("current")
_F3L2A2NAclRuleStatsEntry_Object = MibTableRow
f3L2A2NAclRuleStatsEntry = _F3L2A2NAclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1)
)
f3L2A2NAclRuleStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsEntry.setStatus("current")


class _F3L2A2NAclRuleStatsIndex_Type(Integer32):
    """Custom type f3L2A2NAclRuleStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L2A2NAclRuleStatsIndex_Type.__name__ = "Integer32"
_F3L2A2NAclRuleStatsIndex_Object = MibTableColumn
f3L2A2NAclRuleStatsIndex = _F3L2A2NAclRuleStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 1),
    _F3L2A2NAclRuleStatsIndex_Type()
)
f3L2A2NAclRuleStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsIndex.setStatus("current")
_F3L2A2NAclRuleStatsIntervalType_Type = CmPmIntervalType
_F3L2A2NAclRuleStatsIntervalType_Object = MibTableColumn
f3L2A2NAclRuleStatsIntervalType = _F3L2A2NAclRuleStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 2),
    _F3L2A2NAclRuleStatsIntervalType_Type()
)
f3L2A2NAclRuleStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsIntervalType.setStatus("current")
_F3L2A2NAclRuleStatsValid_Type = TruthValue
_F3L2A2NAclRuleStatsValid_Object = MibTableColumn
f3L2A2NAclRuleStatsValid = _F3L2A2NAclRuleStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 3),
    _F3L2A2NAclRuleStatsValid_Type()
)
f3L2A2NAclRuleStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsValid.setStatus("current")
_F3L2A2NAclRuleStatsAction_Type = CmPmBinAction
_F3L2A2NAclRuleStatsAction_Object = MibTableColumn
f3L2A2NAclRuleStatsAction = _F3L2A2NAclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 4),
    _F3L2A2NAclRuleStatsAction_Type()
)
f3L2A2NAclRuleStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsAction.setStatus("current")
_F3L2A2NAclRuleStatsRuleMatch_Type = PerfCounter64
_F3L2A2NAclRuleStatsRuleMatch_Object = MibTableColumn
f3L2A2NAclRuleStatsRuleMatch = _F3L2A2NAclRuleStatsRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 5),
    _F3L2A2NAclRuleStatsRuleMatch_Type()
)
f3L2A2NAclRuleStatsRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsRuleMatch.setStatus("current")
_F3L2A2NAclRuleHistoryTable_Object = MibTable
f3L2A2NAclRuleHistoryTable = _F3L2A2NAclRuleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryTable.setStatus("current")
_F3L2A2NAclRuleHistoryEntry_Object = MibTableRow
f3L2A2NAclRuleHistoryEntry = _F3L2A2NAclRuleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1)
)
f3L2A2NAclRuleHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryEntry.setStatus("current")


class _F3L2A2NAclRuleHistoryIndex_Type(Integer32):
    """Custom type f3L2A2NAclRuleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L2A2NAclRuleHistoryIndex_Type.__name__ = "Integer32"
_F3L2A2NAclRuleHistoryIndex_Object = MibTableColumn
f3L2A2NAclRuleHistoryIndex = _F3L2A2NAclRuleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 1),
    _F3L2A2NAclRuleHistoryIndex_Type()
)
f3L2A2NAclRuleHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryIndex.setStatus("current")
_F3L2A2NAclRuleHistoryTime_Type = DateAndTime
_F3L2A2NAclRuleHistoryTime_Object = MibTableColumn
f3L2A2NAclRuleHistoryTime = _F3L2A2NAclRuleHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 2),
    _F3L2A2NAclRuleHistoryTime_Type()
)
f3L2A2NAclRuleHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryTime.setStatus("current")
_F3L2A2NAclRuleHistoryValid_Type = TruthValue
_F3L2A2NAclRuleHistoryValid_Object = MibTableColumn
f3L2A2NAclRuleHistoryValid = _F3L2A2NAclRuleHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 3),
    _F3L2A2NAclRuleHistoryValid_Type()
)
f3L2A2NAclRuleHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryValid.setStatus("current")
_F3L2A2NAclRuleHistoryAction_Type = CmPmBinAction
_F3L2A2NAclRuleHistoryAction_Object = MibTableColumn
f3L2A2NAclRuleHistoryAction = _F3L2A2NAclRuleHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 4),
    _F3L2A2NAclRuleHistoryAction_Type()
)
f3L2A2NAclRuleHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryAction.setStatus("current")
_F3L2A2NAclRuleHistoryRuleMatch_Type = PerfCounter64
_F3L2A2NAclRuleHistoryRuleMatch_Object = MibTableColumn
f3L2A2NAclRuleHistoryRuleMatch = _F3L2A2NAclRuleHistoryRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 5),
    _F3L2A2NAclRuleHistoryRuleMatch_Type()
)
f3L2A2NAclRuleHistoryRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryRuleMatch.setStatus("current")
_F3L2A2NAclRuleThresholdTable_Object = MibTable
f3L2A2NAclRuleThresholdTable = _F3L2A2NAclRuleThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdTable.setStatus("current")
_F3L2A2NAclRuleThresholdEntry_Object = MibTableRow
f3L2A2NAclRuleThresholdEntry = _F3L2A2NAclRuleThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1)
)
f3L2A2NAclRuleThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdEntry.setStatus("current")


class _F3L2A2NAclRuleThresholdIndex_Type(Integer32):
    """Custom type f3L2A2NAclRuleThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L2A2NAclRuleThresholdIndex_Type.__name__ = "Integer32"
_F3L2A2NAclRuleThresholdIndex_Object = MibTableColumn
f3L2A2NAclRuleThresholdIndex = _F3L2A2NAclRuleThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 1),
    _F3L2A2NAclRuleThresholdIndex_Type()
)
f3L2A2NAclRuleThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdIndex.setStatus("current")
_F3L2A2NAclRuleThresholdInterval_Type = CmPmIntervalType
_F3L2A2NAclRuleThresholdInterval_Object = MibTableColumn
f3L2A2NAclRuleThresholdInterval = _F3L2A2NAclRuleThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 2),
    _F3L2A2NAclRuleThresholdInterval_Type()
)
f3L2A2NAclRuleThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdInterval.setStatus("current")
_F3L2A2NAclRuleThresholdVariable_Type = VariablePointer
_F3L2A2NAclRuleThresholdVariable_Object = MibTableColumn
f3L2A2NAclRuleThresholdVariable = _F3L2A2NAclRuleThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 3),
    _F3L2A2NAclRuleThresholdVariable_Type()
)
f3L2A2NAclRuleThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdVariable.setStatus("current")
_F3L2A2NAclRuleThresholdValueLo_Type = Unsigned32
_F3L2A2NAclRuleThresholdValueLo_Object = MibTableColumn
f3L2A2NAclRuleThresholdValueLo = _F3L2A2NAclRuleThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 4),
    _F3L2A2NAclRuleThresholdValueLo_Type()
)
f3L2A2NAclRuleThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdValueLo.setStatus("current")
_F3L2A2NAclRuleThresholdValueHi_Type = Unsigned32
_F3L2A2NAclRuleThresholdValueHi_Object = MibTableColumn
f3L2A2NAclRuleThresholdValueHi = _F3L2A2NAclRuleThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 5),
    _F3L2A2NAclRuleThresholdValueHi_Type()
)
f3L2A2NAclRuleThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdValueHi.setStatus("current")
_F3L2A2NAclRuleThresholdMonValue_Type = Counter64
_F3L2A2NAclRuleThresholdMonValue_Object = MibTableColumn
f3L2A2NAclRuleThresholdMonValue = _F3L2A2NAclRuleThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 6),
    _F3L2A2NAclRuleThresholdMonValue_Type()
)
f3L2A2NAclRuleThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdMonValue.setStatus("current")
_F3L2N2AAclRuleStatsTable_Object = MibTable
f3L2N2AAclRuleStatsTable = _F3L2N2AAclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsTable.setStatus("current")
_F3L2N2AAclRuleStatsEntry_Object = MibTableRow
f3L2N2AAclRuleStatsEntry = _F3L2N2AAclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1)
)
f3L2N2AAclRuleStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsEntry.setStatus("current")


class _F3L2N2AAclRuleStatsIndex_Type(Integer32):
    """Custom type f3L2N2AAclRuleStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L2N2AAclRuleStatsIndex_Type.__name__ = "Integer32"
_F3L2N2AAclRuleStatsIndex_Object = MibTableColumn
f3L2N2AAclRuleStatsIndex = _F3L2N2AAclRuleStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 1),
    _F3L2N2AAclRuleStatsIndex_Type()
)
f3L2N2AAclRuleStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsIndex.setStatus("current")
_F3L2N2AAclRuleStatsIntervalType_Type = CmPmIntervalType
_F3L2N2AAclRuleStatsIntervalType_Object = MibTableColumn
f3L2N2AAclRuleStatsIntervalType = _F3L2N2AAclRuleStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 2),
    _F3L2N2AAclRuleStatsIntervalType_Type()
)
f3L2N2AAclRuleStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsIntervalType.setStatus("current")
_F3L2N2AAclRuleStatsValid_Type = TruthValue
_F3L2N2AAclRuleStatsValid_Object = MibTableColumn
f3L2N2AAclRuleStatsValid = _F3L2N2AAclRuleStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 3),
    _F3L2N2AAclRuleStatsValid_Type()
)
f3L2N2AAclRuleStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsValid.setStatus("current")
_F3L2N2AAclRuleStatsAction_Type = CmPmBinAction
_F3L2N2AAclRuleStatsAction_Object = MibTableColumn
f3L2N2AAclRuleStatsAction = _F3L2N2AAclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 4),
    _F3L2N2AAclRuleStatsAction_Type()
)
f3L2N2AAclRuleStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsAction.setStatus("current")
_F3L2N2AAclRuleStatsRuleMatch_Type = PerfCounter64
_F3L2N2AAclRuleStatsRuleMatch_Object = MibTableColumn
f3L2N2AAclRuleStatsRuleMatch = _F3L2N2AAclRuleStatsRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 5),
    _F3L2N2AAclRuleStatsRuleMatch_Type()
)
f3L2N2AAclRuleStatsRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsRuleMatch.setStatus("current")
_F3L2N2AAclRuleHistoryTable_Object = MibTable
f3L2N2AAclRuleHistoryTable = _F3L2N2AAclRuleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryTable.setStatus("current")
_F3L2N2AAclRuleHistoryEntry_Object = MibTableRow
f3L2N2AAclRuleHistoryEntry = _F3L2N2AAclRuleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1)
)
f3L2N2AAclRuleHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryEntry.setStatus("current")


class _F3L2N2AAclRuleHistoryIndex_Type(Integer32):
    """Custom type f3L2N2AAclRuleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L2N2AAclRuleHistoryIndex_Type.__name__ = "Integer32"
_F3L2N2AAclRuleHistoryIndex_Object = MibTableColumn
f3L2N2AAclRuleHistoryIndex = _F3L2N2AAclRuleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 1),
    _F3L2N2AAclRuleHistoryIndex_Type()
)
f3L2N2AAclRuleHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryIndex.setStatus("current")
_F3L2N2AAclRuleHistoryTime_Type = DateAndTime
_F3L2N2AAclRuleHistoryTime_Object = MibTableColumn
f3L2N2AAclRuleHistoryTime = _F3L2N2AAclRuleHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 2),
    _F3L2N2AAclRuleHistoryTime_Type()
)
f3L2N2AAclRuleHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryTime.setStatus("current")
_F3L2N2AAclRuleHistoryValid_Type = TruthValue
_F3L2N2AAclRuleHistoryValid_Object = MibTableColumn
f3L2N2AAclRuleHistoryValid = _F3L2N2AAclRuleHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 3),
    _F3L2N2AAclRuleHistoryValid_Type()
)
f3L2N2AAclRuleHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryValid.setStatus("current")
_F3L2N2AAclRuleHistoryAction_Type = CmPmBinAction
_F3L2N2AAclRuleHistoryAction_Object = MibTableColumn
f3L2N2AAclRuleHistoryAction = _F3L2N2AAclRuleHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 4),
    _F3L2N2AAclRuleHistoryAction_Type()
)
f3L2N2AAclRuleHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryAction.setStatus("current")
_F3L2N2AAclRuleHistoryRuleMatch_Type = PerfCounter64
_F3L2N2AAclRuleHistoryRuleMatch_Object = MibTableColumn
f3L2N2AAclRuleHistoryRuleMatch = _F3L2N2AAclRuleHistoryRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 5),
    _F3L2N2AAclRuleHistoryRuleMatch_Type()
)
f3L2N2AAclRuleHistoryRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryRuleMatch.setStatus("current")
_F3L2N2AAclRuleThresholdTable_Object = MibTable
f3L2N2AAclRuleThresholdTable = _F3L2N2AAclRuleThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdTable.setStatus("current")
_F3L2N2AAclRuleThresholdEntry_Object = MibTableRow
f3L2N2AAclRuleThresholdEntry = _F3L2N2AAclRuleThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1)
)
f3L2N2AAclRuleThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdEntry.setStatus("current")


class _F3L2N2AAclRuleThresholdIndex_Type(Integer32):
    """Custom type f3L2N2AAclRuleThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L2N2AAclRuleThresholdIndex_Type.__name__ = "Integer32"
_F3L2N2AAclRuleThresholdIndex_Object = MibTableColumn
f3L2N2AAclRuleThresholdIndex = _F3L2N2AAclRuleThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 1),
    _F3L2N2AAclRuleThresholdIndex_Type()
)
f3L2N2AAclRuleThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdIndex.setStatus("current")
_F3L2N2AAclRuleThresholdInterval_Type = CmPmIntervalType
_F3L2N2AAclRuleThresholdInterval_Object = MibTableColumn
f3L2N2AAclRuleThresholdInterval = _F3L2N2AAclRuleThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 2),
    _F3L2N2AAclRuleThresholdInterval_Type()
)
f3L2N2AAclRuleThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdInterval.setStatus("current")
_F3L2N2AAclRuleThresholdVariable_Type = VariablePointer
_F3L2N2AAclRuleThresholdVariable_Object = MibTableColumn
f3L2N2AAclRuleThresholdVariable = _F3L2N2AAclRuleThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 3),
    _F3L2N2AAclRuleThresholdVariable_Type()
)
f3L2N2AAclRuleThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdVariable.setStatus("current")
_F3L2N2AAclRuleThresholdValueLo_Type = Unsigned32
_F3L2N2AAclRuleThresholdValueLo_Object = MibTableColumn
f3L2N2AAclRuleThresholdValueLo = _F3L2N2AAclRuleThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 4),
    _F3L2N2AAclRuleThresholdValueLo_Type()
)
f3L2N2AAclRuleThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdValueLo.setStatus("current")
_F3L2N2AAclRuleThresholdValueHi_Type = Unsigned32
_F3L2N2AAclRuleThresholdValueHi_Object = MibTableColumn
f3L2N2AAclRuleThresholdValueHi = _F3L2N2AAclRuleThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 5),
    _F3L2N2AAclRuleThresholdValueHi_Type()
)
f3L2N2AAclRuleThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdValueHi.setStatus("current")
_F3L2N2AAclRuleThresholdMonValue_Type = Counter64
_F3L2N2AAclRuleThresholdMonValue_Object = MibTableColumn
f3L2N2AAclRuleThresholdMonValue = _F3L2N2AAclRuleThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 6),
    _F3L2N2AAclRuleThresholdMonValue_Type()
)
f3L2N2AAclRuleThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdMonValue.setStatus("current")
_F3L3Notifications_ObjectIdentity = ObjectIdentity
f3L3Notifications = _F3L3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3)
)
_F3L3Conformance_ObjectIdentity = ObjectIdentity
f3L3Conformance = _F3L3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4)
)
_F3L3Compliances_ObjectIdentity = ObjectIdentity
f3L3Compliances = _F3L3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 1)
)
_F3L3Groups_ObjectIdentity = ObjectIdentity
f3L3Groups = _F3L3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2)
)

# Managed Objects groups

f3L3ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2, 1)
)
f3L3ObjectsGroup.setObjects(
      *(("F3-L3-MIB", "f3DhcpRelayAgentIndex"),
        ("F3-L3-MIB", "f3DhcpRelayAgentAlias"),
        ("F3-L3-MIB", "f3DhcpRelayAgentAdminState"),
        ("F3-L3-MIB", "f3DhcpRelayAgentSecondaryState"),
        ("F3-L3-MIB", "f3DhcpRelayAgentOperationalState"),
        ("F3-L3-MIB", "f3DhcpRelayAgentIpVersion"),
        ("F3-L3-MIB", "f3DhcpRelayAgentServerIpAddress"),
        ("F3-L3-MIB", "f3DhcpRelayAgentOp82SubOp9ControlEnabled"),
        ("F3-L3-MIB", "f3DhcpRelayAgentOp82SubOp9Value"),
        ("F3-L3-MIB", "f3DhcpRelayAgentStorageType"),
        ("F3-L3-MIB", "f3DhcpRelayAgentRowStatus"),
        ("F3-L3-MIB", "f3VrfIndex"),
        ("F3-L3-MIB", "f3VrfAlias"),
        ("F3-L3-MIB", "f3VrfAdminState"),
        ("F3-L3-MIB", "f3VrfSecondaryState"),
        ("F3-L3-MIB", "f3VrfTraceRouteIpv4Destination"),
        ("F3-L3-MIB", "f3VrfOperationalState"),
        ("F3-L3-MIB", "f3VrfAccIsolationControlEnabled"),
        ("F3-L3-MIB", "f3VrfPingResult"),
        ("F3-L3-MIB", "f3VrfPingIpv4Destination"),
        ("F3-L3-MIB", "f3VrfTraceRouteResult"),
        ("F3-L3-MIB", "f3VrfAction"),
        ("F3-L3-MIB", "f3VrfStorageType"),
        ("F3-L3-MIB", "f3VrfRowStatus"),
        ("F3-L3-MIB", "f3VrfDhcpRoutesControl"),
        ("F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
        ("F3-L3-MIB", "f3L3FlowPointPortIndex"),
        ("F3-L3-MIB", "f3L3FlowPointIndex"),
        ("F3-L3-MIB", "f3L3FlowPointAlias"),
        ("F3-L3-MIB", "f3L3FlowPointAdminState"),
        ("F3-L3-MIB", "f3L3FlowPointSecondaryState"),
        ("F3-L3-MIB", "f3L3FlowPointOperationalState"),
        ("F3-L3-MIB", "f3L3FlowPointMultiCOSEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointCOS"),
        ("F3-L3-MIB", "f3L3FlowPointUntaggedMemberShipEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointOuterTagMemberShipEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointOuterTagMemberShipVlanId"),
        ("F3-L3-MIB", "f3L3FlowPointInnerTagMemberShipEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointInnerTagMemberShipVlanId"),
        ("F3-L3-MIB", "f3L3FlowPointFragmentedPktsFwdEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointHCosMgmtEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointHCosGuaranteedBwHi"),
        ("F3-L3-MIB", "f3L3FlowPointHCosGuaranteedBwLo"),
        ("F3-L3-MIB", "f3L3FlowPointHCosMaximumBwHi"),
        ("F3-L3-MIB", "f3L3FlowPointHCosMaximumBwLo"),
        ("F3-L3-MIB", "f3L3FlowPointPolicingEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointStorageType"),
        ("F3-L3-MIB", "f3L3FlowPointRowStatus"),
        ("F3-L3-MIB", "f3L3AclRuleParentIndex"),
        ("F3-L3-MIB", "f3L3AclRuleIndex"),
        ("F3-L3-MIB", "f3L3AclRuleAlias"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpv4AddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDynamicSrcIpControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpv4AddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleIpv4PriorityControl"),
        ("F3-L3-MIB", "f3L3AclRuleIpv4PriorityLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleProtocolControl"),
        ("F3-L3-MIB", "f3L3AclRuleProtocolNumber"),
        ("F3-L3-MIB", "f3L3AclRuleSrcPortControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcPortLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleSrcPortHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstPortControl"),
        ("F3-L3-MIB", "f3L3AclRuleDstPortLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstPortHighLimit"),
        ("F3-L3-MIB", "f3L3AclRulePriority"),
        ("F3-L3-MIB", "f3L3AclRuleCOS"),
        ("F3-L3-MIB", "f3L3AclRuleOperation"),
        ("F3-L3-MIB", "f3L3AclRuleSummary"),
        ("F3-L3-MIB", "f3L3AclRuleCosOverrideControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDynamicSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcMacAddress"),
        ("F3-L3-MIB", "f3L3AclRuleSrcMacAddressMask"),
        ("F3-L3-MIB", "f3L3AclRuleDstMacAddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDstMacAddress"),
        ("F3-L3-MIB", "f3L3AclRuleDstMacAddressMask"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanVIDControl"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanVIDControl"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanPcpControl"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanPcpControl"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanDeiControl"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanDei"),
        ("F3-L3-MIB", "f3L3AclRuleEtherTypeControl"),
        ("F3-L3-MIB", "f3L3AclRuleEtherType"),
        ("F3-L3-MIB", "f3L3AclRuleTcpFlagsControl"),
        ("F3-L3-MIB", "f3L3AclRuleTcpFlags"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleIpv4PriorityHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleStorageType"),
        ("F3-L3-MIB", "f3L3AclRuleRowStatus"),
        ("F3-L3-MIB", "f3L3AclRuleAdminState"),
        ("F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleAlias"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDynamicSrcIpControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpv4PriorityControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpv4PriorityLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleProtocolControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleProtocolNumber"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcPortControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcPortLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcPortHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstPortControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstPortLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstPortHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRulePriority"),
        ("F3-L3-MIB", "f3L2A2NAclRuleCOS"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOperation"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSummary"),
        ("F3-L3-MIB", "f3L2A2NAclRuleCosOverrideControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDynamicSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcMacAddress"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcMacAddressMask"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstMacAddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstMacAddress"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstMacAddressMask"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanVIDControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanVIDControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanPcpControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanPcpControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanDeiControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanDei"),
        ("F3-L3-MIB", "f3L2A2NAclRuleEtherTypeControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleEtherType"),
        ("F3-L3-MIB", "f3L2A2NAclRuleTcpFlagsControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleTcpFlags"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpv4PriorityHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStorageType"),
        ("F3-L3-MIB", "f3L2A2NAclRuleRowStatus"),
        ("F3-L3-MIB", "f3L2A2NAclRuleAdminState"),
        ("F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleAlias"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDynamicSrcIpControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIpv4PriorityControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIpv4PriorityLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleProtocolControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleProtocolNumber"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcPortControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcPortLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcPortHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstPortControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstPortLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstPortHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRulePriority"),
        ("F3-L3-MIB", "f3L2N2AAclRuleCOS"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOperation"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSummary"),
        ("F3-L3-MIB", "f3L2N2AAclRuleCosOverrideControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDynamicSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcMacAddress"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcMacAddressMask"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstMacAddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstMacAddress"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstMacAddressMask"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanVIDControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanVIDControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanPcpControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanPcpControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanDeiControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanDei"),
        ("F3-L3-MIB", "f3L2N2AAclRuleEtherTypeControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleEtherType"),
        ("F3-L3-MIB", "f3L2N2AAclRuleTcpFlagsControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleTcpFlags"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIpv4PriorityHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStorageType"),
        ("F3-L3-MIB", "f3L2N2AAclRuleRowStatus"),
        ("F3-L3-MIB", "f3L2N2AAclRuleAdminState"),
        ("F3-L3-MIB", "f3L3QosPolicerIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerAdminState"),
        ("F3-L3-MIB", "f3L3QosPolicerOperationalState"),
        ("F3-L3-MIB", "f3L3QosPolicerSecondaryState"),
        ("F3-L3-MIB", "f3L3QosPolicerCIRLo"),
        ("F3-L3-MIB", "f3L3QosPolicerCIRHi"),
        ("F3-L3-MIB", "f3L3QosPolicerEIRLo"),
        ("F3-L3-MIB", "f3L3QosPolicerEIRHi"),
        ("F3-L3-MIB", "f3L3QosPolicerCBS"),
        ("F3-L3-MIB", "f3L3QosPolicerEBS"),
        ("F3-L3-MIB", "f3L3QosPolicerAlgorithm"),
        ("F3-L3-MIB", "f3L3QosPolicerColorMode"),
        ("F3-L3-MIB", "f3L3QosPolicerCouplingFlag"),
        ("F3-L3-MIB", "f3L3QosPolicerStorageType"),
        ("F3-L3-MIB", "f3L3QosPolicerRowStatus"),
        ("F3-L3-MIB", "f3L3QosShaperIndex"),
        ("F3-L3-MIB", "f3L3QosShaperAdminState"),
        ("F3-L3-MIB", "f3L3QosShaperOperationalState"),
        ("F3-L3-MIB", "f3L3QosShaperSecondaryState"),
        ("F3-L3-MIB", "f3L3QosShaperCIRLo"),
        ("F3-L3-MIB", "f3L3QosShaperCIRHi"),
        ("F3-L3-MIB", "f3L3QosShaperEIRLo"),
        ("F3-L3-MIB", "f3L3QosShaperEIRHi"),
        ("F3-L3-MIB", "f3L3QosShaperBufferSize"),
        ("F3-L3-MIB", "f3L3QosShaperCOS"),
        ("F3-L3-MIB", "f3L3QosShaperWredGreenMinQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredGreenMaxQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredGreenDropProbability"),
        ("F3-L3-MIB", "f3L3QosShaperWredYellowMinQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredYellowMaxQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredYellowDropProbability"),
        ("F3-L3-MIB", "f3L3QosShaperStorageType"),
        ("F3-L3-MIB", "f3L3QosShaperRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPIfName"),
        ("F3-L3-MIB", "f3L3TrafficIPIfAdminState"),
        ("F3-L3-MIB", "f3L3TrafficIPIfSecondaryState"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOperationalState"),
        ("F3-L3-MIB", "f3L3TrafficIPIfProxyArpEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpAddressSourceType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfMgmtUseEnable"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpAddress"),
        ("F3-L3-MIB", "f3L3TrafficIPIfMask"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInterfaceSide"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayUserClassOpt77"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayUserClassOpt77Control"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRole"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClientIdEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClientId"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClassIdEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpHostNameEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpHostName"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClientIdType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpHostNameType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPIfAction"),
        ("F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberObject"),
        ("F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberStorageType"),
        ("F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberRowStatus"),
        ("F3-L3-MIB", "f3VrfTrafficIpIfMemberObject"),
        ("F3-L3-MIB", "f3VrfTrafficIpIfMemberStorageType"),
        ("F3-L3-MIB", "f3VrfTrafficIpIfMemberRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteDest"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteMask"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteInterface"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteAdvertise"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteSourceForwardingEnable"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteFlags"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteType"),
        ("F3-L3-MIB", "f3L3TrafficArpIPAddress"),
        ("F3-L3-MIB", "f3L3TrafficArpMacAddress"),
        ("F3-L3-MIB", "f3L3TrafficArpInterface"),
        ("F3-L3-MIB", "f3L3TrafficArpEntryType"),
        ("F3-L3-MIB", "f3L3TrafficArpStorageType"),
        ("F3-L3-MIB", "f3L3TrafficArpRowStatus"))
)
if mibBuilder.loadTexts:
    f3L3ObjectsGroup.setStatus("current")

f3L3PerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2, 2)
)
f3L3PerfGroup.setObjects(
      *(("F3-L3-MIB", "f3L3FlowPointStatsIndex"),
        ("F3-L3-MIB", "f3L3FlowPointStatsIntervalType"),
        ("F3-L3-MIB", "f3L3FlowPointStatsValid"),
        ("F3-L3-MIB", "f3L3FlowPointStatsAction"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFMG"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFMY"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFMRD"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFTD"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFragmentedDropAcl"),
        ("F3-L3-MIB", "f3L3FlowPointStatsAclRuleDrop"),
        ("F3-L3-MIB", "f3L3FlowPointStatsTtlEqual1Drop"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFrameTx"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFrameRx"),
        ("F3-L3-MIB", "f3L3FlowPointStatsNoRouteDrop"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryIndex"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryTime"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryValid"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryAction"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFMG"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFMY"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFMRD"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFTD"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFragmentedDropAcl"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryAclRuleDrop"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryTtlEqual1Drop"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFrameTx"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFrameRx"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryNoRouteDrop"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdIndex"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdInterval"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdVariable"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueLo"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueHi"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdMonValue"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIntervalType"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsValid"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsAction"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsDhcpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsDhcpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIcmpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIcmpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReqTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReqRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReplyTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReplyRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryTime"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryValid"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryAction"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryDhcpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryDhcpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIcmpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIcmpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReqTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReqRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReplyTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReplyRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdInterval"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdVariable"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueLo"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueHi"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdMonValue"),
        ("F3-L3-MIB", "f3L3AclRuleStatsIndex"),
        ("F3-L3-MIB", "f3L3AclRuleStatsIntervalType"),
        ("F3-L3-MIB", "f3L3AclRuleStatsValid"),
        ("F3-L3-MIB", "f3L3AclRuleStatsAction"),
        ("F3-L3-MIB", "f3L3AclRuleStatsRuleMatch"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryIndex"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryTime"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryValid"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryAction"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryRuleMatch"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdMonValue"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsIntervalType"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsValid"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsAction"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsRuleMatch"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryTime"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryValid"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryAction"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryRuleMatch"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdMonValue"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsIntervalType"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsValid"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsAction"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsRuleMatch"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryTime"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryValid"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryAction"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryRuleMatch"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdMonValue"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsIntervalType"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsValid"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsAction"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMG"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMY"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMYD"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMRD"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsBytesIn"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsBytesOut"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsABR"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryTime"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryValid"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryAction"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMG"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMY"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMYD"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMRD"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryBytesIn"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryBytesOut"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryABR"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdMonValue"),
        ("F3-L3-MIB", "f3L3QosShaperStatsIndex"),
        ("F3-L3-MIB", "f3L3QosShaperStatsIntervalType"),
        ("F3-L3-MIB", "f3L3QosShaperStatsValid"),
        ("F3-L3-MIB", "f3L3QosShaperStatsAction"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBT"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBTD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFTD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBR"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFR"),
        ("F3-L3-MIB", "f3L3QosShaperStatsABRRL"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBREDD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFREDD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryIndex"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryTime"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryValid"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryAction"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBT"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBTD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFTD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBR"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFR"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryABRRL"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBREDD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFREDD"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3PerfGroup.setStatus("current")


# Notification objects

f3L3FlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 1)
)
f3L3FlowPointThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3FlowPointThresholdIndex"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdInterval"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdVariable"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueLo"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueHi"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3QosPolicerThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 2)
)
f3L3QosPolicerThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3QosPolicerThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3QosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 3)
)
f3L3QosShaperThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3QosShaperThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3TrafficIpInterfaceThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 4)
)
f3L3TrafficIpInterfaceThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdInterval"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdVariable"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueLo"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueHi"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3AclRuleThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 5)
)
f3L3AclRuleThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3AclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdCrossingAlert.setStatus(
        "current"
    )

f3L2A2NAclRuleThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 6)
)
f3L2A2NAclRuleThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L2A2NAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdCrossingAlert.setStatus(
        "current"
    )

f3L2N2AAclRuleThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 7)
)
f3L2N2AAclRuleThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L2N2AAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

f3L3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 1, 1)
)
f3L3Compliance.setObjects(
      *(("F3-L3-MIB", "f3L3ObjectsGroup"),
        ("F3-L3-MIB", "f3L3PerfGroup"))
)
if mibBuilder.loadTexts:
    f3L3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-L3-MIB",
    **{"VrfAction": VrfAction,
       "IfIpAddressSourceType": IfIpAddressSourceType,
       "DhcpRelayInterfaceSide": DhcpRelayInterfaceSide,
       "L3AclRuleOperation": L3AclRuleOperation,
       "AclRuleL2Side": AclRuleL2Side,
       "TrafficIpRouteStatus": TrafficIpRouteStatus,
       "RouteFlags": RouteFlags,
       "AffectiveArpActionType": AffectiveArpActionType,
       "f3L3MIB": f3L3MIB,
       "f3L3Objects": f3L3Objects,
       "f3DhcpRelayAgentTable": f3DhcpRelayAgentTable,
       "f3DhcpRelayAgentEntry": f3DhcpRelayAgentEntry,
       "f3DhcpRelayAgentIndex": f3DhcpRelayAgentIndex,
       "f3DhcpRelayAgentAlias": f3DhcpRelayAgentAlias,
       "f3DhcpRelayAgentAdminState": f3DhcpRelayAgentAdminState,
       "f3DhcpRelayAgentSecondaryState": f3DhcpRelayAgentSecondaryState,
       "f3DhcpRelayAgentOperationalState": f3DhcpRelayAgentOperationalState,
       "f3DhcpRelayAgentIpVersion": f3DhcpRelayAgentIpVersion,
       "f3DhcpRelayAgentServerIpAddress": f3DhcpRelayAgentServerIpAddress,
       "f3DhcpRelayAgentOp82SubOp9ControlEnabled": f3DhcpRelayAgentOp82SubOp9ControlEnabled,
       "f3DhcpRelayAgentOp82SubOp9Value": f3DhcpRelayAgentOp82SubOp9Value,
       "f3DhcpRelayAgentStorageType": f3DhcpRelayAgentStorageType,
       "f3DhcpRelayAgentRowStatus": f3DhcpRelayAgentRowStatus,
       "f3VrfTable": f3VrfTable,
       "f3VrfEntry": f3VrfEntry,
       "f3VrfIndex": f3VrfIndex,
       "f3VrfAlias": f3VrfAlias,
       "f3VrfAdminState": f3VrfAdminState,
       "f3VrfSecondaryState": f3VrfSecondaryState,
       "f3VrfOperationalState": f3VrfOperationalState,
       "f3VrfAccIsolationControlEnabled": f3VrfAccIsolationControlEnabled,
       "f3VrfPingIpv4Destination": f3VrfPingIpv4Destination,
       "f3VrfTraceRouteIpv4Destination": f3VrfTraceRouteIpv4Destination,
       "f3VrfAction": f3VrfAction,
       "f3VrfPingResult": f3VrfPingResult,
       "f3VrfTraceRouteResult": f3VrfTraceRouteResult,
       "f3VrfStorageType": f3VrfStorageType,
       "f3VrfRowStatus": f3VrfRowStatus,
       "f3VrfDhcpRoutesControl": f3VrfDhcpRoutesControl,
       "f3L3FlowPointTable": f3L3FlowPointTable,
       "f3L3FlowPointEntry": f3L3FlowPointEntry,
       "f3L3FlowPointPortTypeIndex": f3L3FlowPointPortTypeIndex,
       "f3L3FlowPointPortIndex": f3L3FlowPointPortIndex,
       "f3L3FlowPointIndex": f3L3FlowPointIndex,
       "f3L3FlowPointAlias": f3L3FlowPointAlias,
       "f3L3FlowPointAdminState": f3L3FlowPointAdminState,
       "f3L3FlowPointSecondaryState": f3L3FlowPointSecondaryState,
       "f3L3FlowPointOperationalState": f3L3FlowPointOperationalState,
       "f3L3FlowPointMultiCOSEnabled": f3L3FlowPointMultiCOSEnabled,
       "f3L3FlowPointCOS": f3L3FlowPointCOS,
       "f3L3FlowPointUntaggedMemberShipEnabled": f3L3FlowPointUntaggedMemberShipEnabled,
       "f3L3FlowPointOuterTagMemberShipEnabled": f3L3FlowPointOuterTagMemberShipEnabled,
       "f3L3FlowPointOuterTagMemberShipVlanId": f3L3FlowPointOuterTagMemberShipVlanId,
       "f3L3FlowPointInnerTagMemberShipEnabled": f3L3FlowPointInnerTagMemberShipEnabled,
       "f3L3FlowPointInnerTagMemberShipVlanId": f3L3FlowPointInnerTagMemberShipVlanId,
       "f3L3FlowPointFragmentedPktsFwdEnabled": f3L3FlowPointFragmentedPktsFwdEnabled,
       "f3L3FlowPointHCosMgmtEnabled": f3L3FlowPointHCosMgmtEnabled,
       "f3L3FlowPointHCosGuaranteedBwHi": f3L3FlowPointHCosGuaranteedBwHi,
       "f3L3FlowPointHCosGuaranteedBwLo": f3L3FlowPointHCosGuaranteedBwLo,
       "f3L3FlowPointHCosMaximumBwHi": f3L3FlowPointHCosMaximumBwHi,
       "f3L3FlowPointHCosMaximumBwLo": f3L3FlowPointHCosMaximumBwLo,
       "f3L3FlowPointPolicingEnabled": f3L3FlowPointPolicingEnabled,
       "f3L3FlowPointStorageType": f3L3FlowPointStorageType,
       "f3L3FlowPointRowStatus": f3L3FlowPointRowStatus,
       "f3L3AclRuleTable": f3L3AclRuleTable,
       "f3L3AclRuleEntry": f3L3AclRuleEntry,
       "f3L3AclRuleParentIndex": f3L3AclRuleParentIndex,
       "f3L3AclRuleIndex": f3L3AclRuleIndex,
       "f3L3AclRuleAlias": f3L3AclRuleAlias,
       "f3L3AclRuleSrcIpv4AddressControl": f3L3AclRuleSrcIpv4AddressControl,
       "f3L3AclRuleDynamicSrcIpControl": f3L3AclRuleDynamicSrcIpControl,
       "f3L3AclRuleSrcIpv4AddressLowLimit": f3L3AclRuleSrcIpv4AddressLowLimit,
       "f3L3AclRuleDstIpv4AddressControl": f3L3AclRuleDstIpv4AddressControl,
       "f3L3AclRuleDstIpv4AddressLowLimit": f3L3AclRuleDstIpv4AddressLowLimit,
       "f3L3AclRuleIpv4PriorityControl": f3L3AclRuleIpv4PriorityControl,
       "f3L3AclRuleIpv4PriorityLowLimit": f3L3AclRuleIpv4PriorityLowLimit,
       "f3L3AclRuleProtocolControl": f3L3AclRuleProtocolControl,
       "f3L3AclRuleProtocolNumber": f3L3AclRuleProtocolNumber,
       "f3L3AclRuleSrcPortControl": f3L3AclRuleSrcPortControl,
       "f3L3AclRuleSrcPortLowLimit": f3L3AclRuleSrcPortLowLimit,
       "f3L3AclRuleSrcPortHighLimit": f3L3AclRuleSrcPortHighLimit,
       "f3L3AclRuleDstPortControl": f3L3AclRuleDstPortControl,
       "f3L3AclRuleDstPortLowLimit": f3L3AclRuleDstPortLowLimit,
       "f3L3AclRuleDstPortHighLimit": f3L3AclRuleDstPortHighLimit,
       "f3L3AclRulePriority": f3L3AclRulePriority,
       "f3L3AclRuleCOS": f3L3AclRuleCOS,
       "f3L3AclRuleOperation": f3L3AclRuleOperation,
       "f3L3AclRuleSummary": f3L3AclRuleSummary,
       "f3L3AclRuleCosOverrideControl": f3L3AclRuleCosOverrideControl,
       "f3L3AclRuleSrcMacAddressControl": f3L3AclRuleSrcMacAddressControl,
       "f3L3AclRuleDynamicSrcMacAddressControl": f3L3AclRuleDynamicSrcMacAddressControl,
       "f3L3AclRuleSrcMacAddress": f3L3AclRuleSrcMacAddress,
       "f3L3AclRuleSrcMacAddressMask": f3L3AclRuleSrcMacAddressMask,
       "f3L3AclRuleDstMacAddressControl": f3L3AclRuleDstMacAddressControl,
       "f3L3AclRuleDstMacAddress": f3L3AclRuleDstMacAddress,
       "f3L3AclRuleDstMacAddressMask": f3L3AclRuleDstMacAddressMask,
       "f3L3AclRuleOuterVlanVIDControl": f3L3AclRuleOuterVlanVIDControl,
       "f3L3AclRuleOuterVlanVIDLowLimit": f3L3AclRuleOuterVlanVIDLowLimit,
       "f3L3AclRuleOuterVlanVIDHighLimit": f3L3AclRuleOuterVlanVIDHighLimit,
       "f3L3AclRuleInnerVlanVIDControl": f3L3AclRuleInnerVlanVIDControl,
       "f3L3AclRuleInnerVlanVIDLowLimit": f3L3AclRuleInnerVlanVIDLowLimit,
       "f3L3AclRuleInnerVlanVIDHighLimit": f3L3AclRuleInnerVlanVIDHighLimit,
       "f3L3AclRuleOuterVlanPcpControl": f3L3AclRuleOuterVlanPcpControl,
       "f3L3AclRuleOuterVlanPcpLowLimit": f3L3AclRuleOuterVlanPcpLowLimit,
       "f3L3AclRuleOuterVlanPcpHighLimit": f3L3AclRuleOuterVlanPcpHighLimit,
       "f3L3AclRuleInnerVlanPcpControl": f3L3AclRuleInnerVlanPcpControl,
       "f3L3AclRuleInnerVlanPcpLowLimit": f3L3AclRuleInnerVlanPcpLowLimit,
       "f3L3AclRuleInnerVlanPcpHighLimit": f3L3AclRuleInnerVlanPcpHighLimit,
       "f3L3AclRuleOuterVlanDeiControl": f3L3AclRuleOuterVlanDeiControl,
       "f3L3AclRuleOuterVlanDei": f3L3AclRuleOuterVlanDei,
       "f3L3AclRuleEtherTypeControl": f3L3AclRuleEtherTypeControl,
       "f3L3AclRuleEtherType": f3L3AclRuleEtherType,
       "f3L3AclRuleTcpFlagsControl": f3L3AclRuleTcpFlagsControl,
       "f3L3AclRuleTcpFlags": f3L3AclRuleTcpFlags,
       "f3L3AclRuleSrcIpv4AddressHighLimit": f3L3AclRuleSrcIpv4AddressHighLimit,
       "f3L3AclRuleDstIpv4AddressHighLimit": f3L3AclRuleDstIpv4AddressHighLimit,
       "f3L3AclRuleIpv4PriorityHighLimit": f3L3AclRuleIpv4PriorityHighLimit,
       "f3L3AclRuleStorageType": f3L3AclRuleStorageType,
       "f3L3AclRuleRowStatus": f3L3AclRuleRowStatus,
       "f3L3AclRuleAdminState": f3L3AclRuleAdminState,
       "f3L2A2NAclRuleTable": f3L2A2NAclRuleTable,
       "f3L2A2NAclRuleEntry": f3L2A2NAclRuleEntry,
       "f3L2A2NAclRuleParentIndex": f3L2A2NAclRuleParentIndex,
       "f3L2A2NAclRuleIndex": f3L2A2NAclRuleIndex,
       "f3L2A2NAclRuleAlias": f3L2A2NAclRuleAlias,
       "f3L2A2NAclRuleSrcIpv4AddressControl": f3L2A2NAclRuleSrcIpv4AddressControl,
       "f3L2A2NAclRuleDynamicSrcIpControl": f3L2A2NAclRuleDynamicSrcIpControl,
       "f3L2A2NAclRuleSrcIpv4AddressLowLimit": f3L2A2NAclRuleSrcIpv4AddressLowLimit,
       "f3L2A2NAclRuleDstIpv4AddressControl": f3L2A2NAclRuleDstIpv4AddressControl,
       "f3L2A2NAclRuleDstIpv4AddressLowLimit": f3L2A2NAclRuleDstIpv4AddressLowLimit,
       "f3L2A2NAclRuleIpv4PriorityControl": f3L2A2NAclRuleIpv4PriorityControl,
       "f3L2A2NAclRuleIpv4PriorityLowLimit": f3L2A2NAclRuleIpv4PriorityLowLimit,
       "f3L2A2NAclRuleProtocolControl": f3L2A2NAclRuleProtocolControl,
       "f3L2A2NAclRuleProtocolNumber": f3L2A2NAclRuleProtocolNumber,
       "f3L2A2NAclRuleSrcPortControl": f3L2A2NAclRuleSrcPortControl,
       "f3L2A2NAclRuleSrcPortLowLimit": f3L2A2NAclRuleSrcPortLowLimit,
       "f3L2A2NAclRuleSrcPortHighLimit": f3L2A2NAclRuleSrcPortHighLimit,
       "f3L2A2NAclRuleDstPortControl": f3L2A2NAclRuleDstPortControl,
       "f3L2A2NAclRuleDstPortLowLimit": f3L2A2NAclRuleDstPortLowLimit,
       "f3L2A2NAclRuleDstPortHighLimit": f3L2A2NAclRuleDstPortHighLimit,
       "f3L2A2NAclRulePriority": f3L2A2NAclRulePriority,
       "f3L2A2NAclRuleCOS": f3L2A2NAclRuleCOS,
       "f3L2A2NAclRuleOperation": f3L2A2NAclRuleOperation,
       "f3L2A2NAclRuleSummary": f3L2A2NAclRuleSummary,
       "f3L2A2NAclRuleCosOverrideControl": f3L2A2NAclRuleCosOverrideControl,
       "f3L2A2NAclRuleSrcMacAddressControl": f3L2A2NAclRuleSrcMacAddressControl,
       "f3L2A2NAclRuleDynamicSrcMacAddressControl": f3L2A2NAclRuleDynamicSrcMacAddressControl,
       "f3L2A2NAclRuleSrcMacAddress": f3L2A2NAclRuleSrcMacAddress,
       "f3L2A2NAclRuleSrcMacAddressMask": f3L2A2NAclRuleSrcMacAddressMask,
       "f3L2A2NAclRuleDstMacAddressControl": f3L2A2NAclRuleDstMacAddressControl,
       "f3L2A2NAclRuleDstMacAddress": f3L2A2NAclRuleDstMacAddress,
       "f3L2A2NAclRuleDstMacAddressMask": f3L2A2NAclRuleDstMacAddressMask,
       "f3L2A2NAclRuleOuterVlanVIDControl": f3L2A2NAclRuleOuterVlanVIDControl,
       "f3L2A2NAclRuleOuterVlanVIDLowLimit": f3L2A2NAclRuleOuterVlanVIDLowLimit,
       "f3L2A2NAclRuleOuterVlanVIDHighLimit": f3L2A2NAclRuleOuterVlanVIDHighLimit,
       "f3L2A2NAclRuleInnerVlanVIDControl": f3L2A2NAclRuleInnerVlanVIDControl,
       "f3L2A2NAclRuleInnerVlanVIDLowLimit": f3L2A2NAclRuleInnerVlanVIDLowLimit,
       "f3L2A2NAclRuleInnerVlanVIDHighLimit": f3L2A2NAclRuleInnerVlanVIDHighLimit,
       "f3L2A2NAclRuleOuterVlanPcpControl": f3L2A2NAclRuleOuterVlanPcpControl,
       "f3L2A2NAclRuleOuterVlanPcpLowLimit": f3L2A2NAclRuleOuterVlanPcpLowLimit,
       "f3L2A2NAclRuleOuterVlanPcpHighLimit": f3L2A2NAclRuleOuterVlanPcpHighLimit,
       "f3L2A2NAclRuleInnerVlanPcpControl": f3L2A2NAclRuleInnerVlanPcpControl,
       "f3L2A2NAclRuleInnerVlanPcpLowLimit": f3L2A2NAclRuleInnerVlanPcpLowLimit,
       "f3L2A2NAclRuleInnerVlanPcpHighLimit": f3L2A2NAclRuleInnerVlanPcpHighLimit,
       "f3L2A2NAclRuleOuterVlanDeiControl": f3L2A2NAclRuleOuterVlanDeiControl,
       "f3L2A2NAclRuleOuterVlanDei": f3L2A2NAclRuleOuterVlanDei,
       "f3L2A2NAclRuleEtherTypeControl": f3L2A2NAclRuleEtherTypeControl,
       "f3L2A2NAclRuleEtherType": f3L2A2NAclRuleEtherType,
       "f3L2A2NAclRuleTcpFlagsControl": f3L2A2NAclRuleTcpFlagsControl,
       "f3L2A2NAclRuleTcpFlags": f3L2A2NAclRuleTcpFlags,
       "f3L2A2NAclRuleSrcIpv4AddressHighLimit": f3L2A2NAclRuleSrcIpv4AddressHighLimit,
       "f3L2A2NAclRuleDstIpv4AddressHighLimit": f3L2A2NAclRuleDstIpv4AddressHighLimit,
       "f3L2A2NAclRuleIpv4PriorityHighLimit": f3L2A2NAclRuleIpv4PriorityHighLimit,
       "f3L2A2NAclRuleStorageType": f3L2A2NAclRuleStorageType,
       "f3L2A2NAclRuleRowStatus": f3L2A2NAclRuleRowStatus,
       "f3L2A2NAclRuleAdminState": f3L2A2NAclRuleAdminState,
       "f3L2N2AAclRuleTable": f3L2N2AAclRuleTable,
       "f3L2N2AAclRuleEntry": f3L2N2AAclRuleEntry,
       "f3L2N2AAclRuleParentIndex": f3L2N2AAclRuleParentIndex,
       "f3L2N2AAclRuleIndex": f3L2N2AAclRuleIndex,
       "f3L2N2AAclRuleAlias": f3L2N2AAclRuleAlias,
       "f3L2N2AAclRuleSrcIpv4AddressControl": f3L2N2AAclRuleSrcIpv4AddressControl,
       "f3L2N2AAclRuleDynamicSrcIpControl": f3L2N2AAclRuleDynamicSrcIpControl,
       "f3L2N2AAclRuleSrcIpv4AddressLowLimit": f3L2N2AAclRuleSrcIpv4AddressLowLimit,
       "f3L2N2AAclRuleDstIpv4AddressControl": f3L2N2AAclRuleDstIpv4AddressControl,
       "f3L2N2AAclRuleDstIpv4AddressLowLimit": f3L2N2AAclRuleDstIpv4AddressLowLimit,
       "f3L2N2AAclRuleIpv4PriorityControl": f3L2N2AAclRuleIpv4PriorityControl,
       "f3L2N2AAclRuleIpv4PriorityLowLimit": f3L2N2AAclRuleIpv4PriorityLowLimit,
       "f3L2N2AAclRuleProtocolControl": f3L2N2AAclRuleProtocolControl,
       "f3L2N2AAclRuleProtocolNumber": f3L2N2AAclRuleProtocolNumber,
       "f3L2N2AAclRuleSrcPortControl": f3L2N2AAclRuleSrcPortControl,
       "f3L2N2AAclRuleSrcPortLowLimit": f3L2N2AAclRuleSrcPortLowLimit,
       "f3L2N2AAclRuleSrcPortHighLimit": f3L2N2AAclRuleSrcPortHighLimit,
       "f3L2N2AAclRuleDstPortControl": f3L2N2AAclRuleDstPortControl,
       "f3L2N2AAclRuleDstPortLowLimit": f3L2N2AAclRuleDstPortLowLimit,
       "f3L2N2AAclRuleDstPortHighLimit": f3L2N2AAclRuleDstPortHighLimit,
       "f3L2N2AAclRulePriority": f3L2N2AAclRulePriority,
       "f3L2N2AAclRuleCOS": f3L2N2AAclRuleCOS,
       "f3L2N2AAclRuleOperation": f3L2N2AAclRuleOperation,
       "f3L2N2AAclRuleSummary": f3L2N2AAclRuleSummary,
       "f3L2N2AAclRuleCosOverrideControl": f3L2N2AAclRuleCosOverrideControl,
       "f3L2N2AAclRuleSrcMacAddressControl": f3L2N2AAclRuleSrcMacAddressControl,
       "f3L2N2AAclRuleDynamicSrcMacAddressControl": f3L2N2AAclRuleDynamicSrcMacAddressControl,
       "f3L2N2AAclRuleSrcMacAddress": f3L2N2AAclRuleSrcMacAddress,
       "f3L2N2AAclRuleSrcMacAddressMask": f3L2N2AAclRuleSrcMacAddressMask,
       "f3L2N2AAclRuleDstMacAddressControl": f3L2N2AAclRuleDstMacAddressControl,
       "f3L2N2AAclRuleDstMacAddress": f3L2N2AAclRuleDstMacAddress,
       "f3L2N2AAclRuleDstMacAddressMask": f3L2N2AAclRuleDstMacAddressMask,
       "f3L2N2AAclRuleOuterVlanVIDControl": f3L2N2AAclRuleOuterVlanVIDControl,
       "f3L2N2AAclRuleOuterVlanVIDLowLimit": f3L2N2AAclRuleOuterVlanVIDLowLimit,
       "f3L2N2AAclRuleOuterVlanVIDHighLimit": f3L2N2AAclRuleOuterVlanVIDHighLimit,
       "f3L2N2AAclRuleInnerVlanVIDControl": f3L2N2AAclRuleInnerVlanVIDControl,
       "f3L2N2AAclRuleInnerVlanVIDLowLimit": f3L2N2AAclRuleInnerVlanVIDLowLimit,
       "f3L2N2AAclRuleInnerVlanVIDHighLimit": f3L2N2AAclRuleInnerVlanVIDHighLimit,
       "f3L2N2AAclRuleOuterVlanPcpControl": f3L2N2AAclRuleOuterVlanPcpControl,
       "f3L2N2AAclRuleOuterVlanPcpLowLimit": f3L2N2AAclRuleOuterVlanPcpLowLimit,
       "f3L2N2AAclRuleOuterVlanPcpHighLimit": f3L2N2AAclRuleOuterVlanPcpHighLimit,
       "f3L2N2AAclRuleInnerVlanPcpControl": f3L2N2AAclRuleInnerVlanPcpControl,
       "f3L2N2AAclRuleInnerVlanPcpLowLimit": f3L2N2AAclRuleInnerVlanPcpLowLimit,
       "f3L2N2AAclRuleInnerVlanPcpHighLimit": f3L2N2AAclRuleInnerVlanPcpHighLimit,
       "f3L2N2AAclRuleOuterVlanDeiControl": f3L2N2AAclRuleOuterVlanDeiControl,
       "f3L2N2AAclRuleOuterVlanDei": f3L2N2AAclRuleOuterVlanDei,
       "f3L2N2AAclRuleEtherTypeControl": f3L2N2AAclRuleEtherTypeControl,
       "f3L2N2AAclRuleEtherType": f3L2N2AAclRuleEtherType,
       "f3L2N2AAclRuleTcpFlagsControl": f3L2N2AAclRuleTcpFlagsControl,
       "f3L2N2AAclRuleTcpFlags": f3L2N2AAclRuleTcpFlags,
       "f3L2N2AAclRuleSrcIpv4AddressHighLimit": f3L2N2AAclRuleSrcIpv4AddressHighLimit,
       "f3L2N2AAclRuleDstIpv4AddressHighLimit": f3L2N2AAclRuleDstIpv4AddressHighLimit,
       "f3L2N2AAclRuleIpv4PriorityHighLimit": f3L2N2AAclRuleIpv4PriorityHighLimit,
       "f3L2N2AAclRuleStorageType": f3L2N2AAclRuleStorageType,
       "f3L2N2AAclRuleRowStatus": f3L2N2AAclRuleRowStatus,
       "f3L2N2AAclRuleAdminState": f3L2N2AAclRuleAdminState,
       "f3L3QosPolicerTable": f3L3QosPolicerTable,
       "f3L3QosPolicerEntry": f3L3QosPolicerEntry,
       "f3L3QosPolicerIndex": f3L3QosPolicerIndex,
       "f3L3QosPolicerAdminState": f3L3QosPolicerAdminState,
       "f3L3QosPolicerOperationalState": f3L3QosPolicerOperationalState,
       "f3L3QosPolicerSecondaryState": f3L3QosPolicerSecondaryState,
       "f3L3QosPolicerCIRLo": f3L3QosPolicerCIRLo,
       "f3L3QosPolicerCIRHi": f3L3QosPolicerCIRHi,
       "f3L3QosPolicerEIRLo": f3L3QosPolicerEIRLo,
       "f3L3QosPolicerEIRHi": f3L3QosPolicerEIRHi,
       "f3L3QosPolicerCBS": f3L3QosPolicerCBS,
       "f3L3QosPolicerEBS": f3L3QosPolicerEBS,
       "f3L3QosPolicerAlgorithm": f3L3QosPolicerAlgorithm,
       "f3L3QosPolicerColorMode": f3L3QosPolicerColorMode,
       "f3L3QosPolicerCouplingFlag": f3L3QosPolicerCouplingFlag,
       "f3L3QosPolicerStorageType": f3L3QosPolicerStorageType,
       "f3L3QosPolicerRowStatus": f3L3QosPolicerRowStatus,
       "f3L3QosShaperTable": f3L3QosShaperTable,
       "f3L3QosShaperEntry": f3L3QosShaperEntry,
       "f3L3QosShaperIndex": f3L3QosShaperIndex,
       "f3L3QosShaperAdminState": f3L3QosShaperAdminState,
       "f3L3QosShaperOperationalState": f3L3QosShaperOperationalState,
       "f3L3QosShaperSecondaryState": f3L3QosShaperSecondaryState,
       "f3L3QosShaperCIRLo": f3L3QosShaperCIRLo,
       "f3L3QosShaperCIRHi": f3L3QosShaperCIRHi,
       "f3L3QosShaperEIRLo": f3L3QosShaperEIRLo,
       "f3L3QosShaperEIRHi": f3L3QosShaperEIRHi,
       "f3L3QosShaperBufferSize": f3L3QosShaperBufferSize,
       "f3L3QosShaperCOS": f3L3QosShaperCOS,
       "f3L3QosShaperWredGreenMinQueueThreshold": f3L3QosShaperWredGreenMinQueueThreshold,
       "f3L3QosShaperWredGreenMaxQueueThreshold": f3L3QosShaperWredGreenMaxQueueThreshold,
       "f3L3QosShaperWredGreenDropProbability": f3L3QosShaperWredGreenDropProbability,
       "f3L3QosShaperWredYellowMinQueueThreshold": f3L3QosShaperWredYellowMinQueueThreshold,
       "f3L3QosShaperWredYellowMaxQueueThreshold": f3L3QosShaperWredYellowMaxQueueThreshold,
       "f3L3QosShaperWredYellowDropProbability": f3L3QosShaperWredYellowDropProbability,
       "f3L3QosShaperStorageType": f3L3QosShaperStorageType,
       "f3L3QosShaperRowStatus": f3L3QosShaperRowStatus,
       "f3L3TrafficIPInterfaceTable": f3L3TrafficIPInterfaceTable,
       "f3L3TrafficIPInterfaceEntry": f3L3TrafficIPInterfaceEntry,
       "f3L3TrafficIPIfIndex": f3L3TrafficIPIfIndex,
       "f3L3TrafficIPIfName": f3L3TrafficIPIfName,
       "f3L3TrafficIPIfAdminState": f3L3TrafficIPIfAdminState,
       "f3L3TrafficIPIfSecondaryState": f3L3TrafficIPIfSecondaryState,
       "f3L3TrafficIPIfOperationalState": f3L3TrafficIPIfOperationalState,
       "f3L3TrafficIPIfProxyArpEnabled": f3L3TrafficIPIfProxyArpEnabled,
       "f3L3TrafficIPIfIpAddressSourceType": f3L3TrafficIPIfIpAddressSourceType,
       "f3L3TrafficIPIfMgmtUseEnable": f3L3TrafficIPIfMgmtUseEnable,
       "f3L3TrafficIPIfIpAddress": f3L3TrafficIPIfIpAddress,
       "f3L3TrafficIPIfMask": f3L3TrafficIPIfMask,
       "f3L3TrafficIPIfDhcpRelayInterfaceSide": f3L3TrafficIPIfDhcpRelayInterfaceSide,
       "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60": f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60,
       "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control": f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control,
       "f3L3TrafficIPIfDhcpRelayUserClassOpt77": f3L3TrafficIPIfDhcpRelayUserClassOpt77,
       "f3L3TrafficIPIfDhcpRelayUserClassOpt77Control": f3L3TrafficIPIfDhcpRelayUserClassOpt77Control,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled,
       "f3L3TrafficIPIfDhcpEnabled": f3L3TrafficIPIfDhcpEnabled,
       "f3L3TrafficIPIfDhcpRole": f3L3TrafficIPIfDhcpRole,
       "f3L3TrafficIPIfDhcpClientIdEnabled": f3L3TrafficIPIfDhcpClientIdEnabled,
       "f3L3TrafficIPIfDhcpClientId": f3L3TrafficIPIfDhcpClientId,
       "f3L3TrafficIPIfDhcpClassIdEnabled": f3L3TrafficIPIfDhcpClassIdEnabled,
       "f3L3TrafficIPIfDhcpHostNameEnabled": f3L3TrafficIPIfDhcpHostNameEnabled,
       "f3L3TrafficIPIfDhcpHostName": f3L3TrafficIPIfDhcpHostName,
       "f3L3TrafficIPIfDhcpClientIdType": f3L3TrafficIPIfDhcpClientIdType,
       "f3L3TrafficIPIfDhcpHostNameType": f3L3TrafficIPIfDhcpHostNameType,
       "f3L3TrafficIPIfStorageType": f3L3TrafficIPIfStorageType,
       "f3L3TrafficIPIfRowStatus": f3L3TrafficIPIfRowStatus,
       "f3L3TrafficIPIfAction": f3L3TrafficIPIfAction,
       "f3DhcpRelayAgentTrafficIpIfMemberTable": f3DhcpRelayAgentTrafficIpIfMemberTable,
       "f3DhcpRelayAgentTrafficIpIfMemberEntry": f3DhcpRelayAgentTrafficIpIfMemberEntry,
       "f3DhcpRelayAgentTrafficIpIfMemberObject": f3DhcpRelayAgentTrafficIpIfMemberObject,
       "f3DhcpRelayAgentTrafficIpIfMemberStorageType": f3DhcpRelayAgentTrafficIpIfMemberStorageType,
       "f3DhcpRelayAgentTrafficIpIfMemberRowStatus": f3DhcpRelayAgentTrafficIpIfMemberRowStatus,
       "f3VrfTrafficIpIfMemberTable": f3VrfTrafficIpIfMemberTable,
       "f3VrfTrafficIpIfMemberEntry": f3VrfTrafficIpIfMemberEntry,
       "f3VrfTrafficIpIfMemberObject": f3VrfTrafficIpIfMemberObject,
       "f3VrfTrafficIpIfMemberStorageType": f3VrfTrafficIpIfMemberStorageType,
       "f3VrfTrafficIpIfMemberRowStatus": f3VrfTrafficIpIfMemberRowStatus,
       "f3L3TrafficIpv4RouteTable": f3L3TrafficIpv4RouteTable,
       "f3L3TrafficIpv4RouteEntry": f3L3TrafficIpv4RouteEntry,
       "f3L3TrafficIpv4RouteDest": f3L3TrafficIpv4RouteDest,
       "f3L3TrafficIpv4RouteMask": f3L3TrafficIpv4RouteMask,
       "f3L3TrafficIpv4RouteNextHop": f3L3TrafficIpv4RouteNextHop,
       "f3L3TrafficIpv4RouteMetric": f3L3TrafficIpv4RouteMetric,
       "f3L3TrafficIpv4RouteInterface": f3L3TrafficIpv4RouteInterface,
       "f3L3TrafficIpv4RouteAdvertise": f3L3TrafficIpv4RouteAdvertise,
       "f3L3TrafficIpv4RouteStatus": f3L3TrafficIpv4RouteStatus,
       "f3L3TrafficIpv4RouteSourceForwardingEnable": f3L3TrafficIpv4RouteSourceForwardingEnable,
       "f3L3TrafficIpv4RouteFlags": f3L3TrafficIpv4RouteFlags,
       "f3L3TrafficIpv4RouteStorageType": f3L3TrafficIpv4RouteStorageType,
       "f3L3TrafficIpv4RouteRowStatus": f3L3TrafficIpv4RouteRowStatus,
       "f3L3TrafficIpv4RouteType": f3L3TrafficIpv4RouteType,
       "f3L3TrafficArpTable": f3L3TrafficArpTable,
       "f3L3TrafficArpEntry": f3L3TrafficArpEntry,
       "f3L3TrafficArpIPAddress": f3L3TrafficArpIPAddress,
       "f3L3TrafficArpMacAddress": f3L3TrafficArpMacAddress,
       "f3L3TrafficArpInterface": f3L3TrafficArpInterface,
       "f3L3TrafficArpEntryType": f3L3TrafficArpEntryType,
       "f3L3TrafficArpStorageType": f3L3TrafficArpStorageType,
       "f3L3TrafficArpRowStatus": f3L3TrafficArpRowStatus,
       "f3L3Performance": f3L3Performance,
       "f3L3FlowPointStatsTable": f3L3FlowPointStatsTable,
       "f3L3FlowPointStatsEntry": f3L3FlowPointStatsEntry,
       "f3L3FlowPointStatsIndex": f3L3FlowPointStatsIndex,
       "f3L3FlowPointStatsIntervalType": f3L3FlowPointStatsIntervalType,
       "f3L3FlowPointStatsValid": f3L3FlowPointStatsValid,
       "f3L3FlowPointStatsAction": f3L3FlowPointStatsAction,
       "f3L3FlowPointStatsFMG": f3L3FlowPointStatsFMG,
       "f3L3FlowPointStatsFMY": f3L3FlowPointStatsFMY,
       "f3L3FlowPointStatsFMRD": f3L3FlowPointStatsFMRD,
       "f3L3FlowPointStatsFTD": f3L3FlowPointStatsFTD,
       "f3L3FlowPointStatsFragmentedDropAcl": f3L3FlowPointStatsFragmentedDropAcl,
       "f3L3FlowPointStatsAclRuleDrop": f3L3FlowPointStatsAclRuleDrop,
       "f3L3FlowPointStatsTtlEqual1Drop": f3L3FlowPointStatsTtlEqual1Drop,
       "f3L3FlowPointStatsFrameTx": f3L3FlowPointStatsFrameTx,
       "f3L3FlowPointStatsFrameRx": f3L3FlowPointStatsFrameRx,
       "f3L3FlowPointStatsNoRouteDrop": f3L3FlowPointStatsNoRouteDrop,
       "f3L3FlowPointHistoryTable": f3L3FlowPointHistoryTable,
       "f3L3FlowPointHistoryEntry": f3L3FlowPointHistoryEntry,
       "f3L3FlowPointHistoryIndex": f3L3FlowPointHistoryIndex,
       "f3L3FlowPointHistoryTime": f3L3FlowPointHistoryTime,
       "f3L3FlowPointHistoryValid": f3L3FlowPointHistoryValid,
       "f3L3FlowPointHistoryAction": f3L3FlowPointHistoryAction,
       "f3L3FlowPointHistoryFMG": f3L3FlowPointHistoryFMG,
       "f3L3FlowPointHistoryFMY": f3L3FlowPointHistoryFMY,
       "f3L3FlowPointHistoryFMRD": f3L3FlowPointHistoryFMRD,
       "f3L3FlowPointHistoryFTD": f3L3FlowPointHistoryFTD,
       "f3L3FlowPointHistoryFragmentedDropAcl": f3L3FlowPointHistoryFragmentedDropAcl,
       "f3L3FlowPointHistoryAclRuleDrop": f3L3FlowPointHistoryAclRuleDrop,
       "f3L3FlowPointHistoryTtlEqual1Drop": f3L3FlowPointHistoryTtlEqual1Drop,
       "f3L3FlowPointHistoryFrameTx": f3L3FlowPointHistoryFrameTx,
       "f3L3FlowPointHistoryFrameRx": f3L3FlowPointHistoryFrameRx,
       "f3L3FlowPointHistoryNoRouteDrop": f3L3FlowPointHistoryNoRouteDrop,
       "f3L3FlowPointThresholdTable": f3L3FlowPointThresholdTable,
       "f3L3FlowPointThresholdEntry": f3L3FlowPointThresholdEntry,
       "f3L3FlowPointThresholdIndex": f3L3FlowPointThresholdIndex,
       "f3L3FlowPointThresholdInterval": f3L3FlowPointThresholdInterval,
       "f3L3FlowPointThresholdVariable": f3L3FlowPointThresholdVariable,
       "f3L3FlowPointThresholdValueLo": f3L3FlowPointThresholdValueLo,
       "f3L3FlowPointThresholdValueHi": f3L3FlowPointThresholdValueHi,
       "f3L3FlowPointThresholdMonValue": f3L3FlowPointThresholdMonValue,
       "f3L3TrafficIpInterfaceStatsTable": f3L3TrafficIpInterfaceStatsTable,
       "f3L3TrafficIpInterfaceStatsEntry": f3L3TrafficIpInterfaceStatsEntry,
       "f3L3TrafficIpInterfaceStatsIndex": f3L3TrafficIpInterfaceStatsIndex,
       "f3L3TrafficIpInterfaceStatsIntervalType": f3L3TrafficIpInterfaceStatsIntervalType,
       "f3L3TrafficIpInterfaceStatsValid": f3L3TrafficIpInterfaceStatsValid,
       "f3L3TrafficIpInterfaceStatsAction": f3L3TrafficIpInterfaceStatsAction,
       "f3L3TrafficIpInterfaceStatsDhcpTx": f3L3TrafficIpInterfaceStatsDhcpTx,
       "f3L3TrafficIpInterfaceStatsDhcpRx": f3L3TrafficIpInterfaceStatsDhcpRx,
       "f3L3TrafficIpInterfaceStatsIcmpTx": f3L3TrafficIpInterfaceStatsIcmpTx,
       "f3L3TrafficIpInterfaceStatsIcmpRx": f3L3TrafficIpInterfaceStatsIcmpRx,
       "f3L3TrafficIpInterfaceStatsArpReqTx": f3L3TrafficIpInterfaceStatsArpReqTx,
       "f3L3TrafficIpInterfaceStatsArpReqRx": f3L3TrafficIpInterfaceStatsArpReqRx,
       "f3L3TrafficIpInterfaceStatsArpReplyTx": f3L3TrafficIpInterfaceStatsArpReplyTx,
       "f3L3TrafficIpInterfaceStatsArpReplyRx": f3L3TrafficIpInterfaceStatsArpReplyRx,
       "f3L3TrafficIpInterfaceHistoryTable": f3L3TrafficIpInterfaceHistoryTable,
       "f3L3TrafficIpInterfaceHistoryEntry": f3L3TrafficIpInterfaceHistoryEntry,
       "f3L3TrafficIpInterfaceHistoryIndex": f3L3TrafficIpInterfaceHistoryIndex,
       "f3L3TrafficIpInterfaceHistoryTime": f3L3TrafficIpInterfaceHistoryTime,
       "f3L3TrafficIpInterfaceHistoryValid": f3L3TrafficIpInterfaceHistoryValid,
       "f3L3TrafficIpInterfaceHistoryAction": f3L3TrafficIpInterfaceHistoryAction,
       "f3L3TrafficIpInterfaceHistoryDhcpTx": f3L3TrafficIpInterfaceHistoryDhcpTx,
       "f3L3TrafficIpInterfaceHistoryDhcpRx": f3L3TrafficIpInterfaceHistoryDhcpRx,
       "f3L3TrafficIpInterfaceHistoryIcmpTx": f3L3TrafficIpInterfaceHistoryIcmpTx,
       "f3L3TrafficIpInterfaceHistoryIcmpRx": f3L3TrafficIpInterfaceHistoryIcmpRx,
       "f3L3TrafficIpInterfaceHistoryArpReqTx": f3L3TrafficIpInterfaceHistoryArpReqTx,
       "f3L3TrafficIpInterfaceHistoryArpReqRx": f3L3TrafficIpInterfaceHistoryArpReqRx,
       "f3L3TrafficIpInterfaceHistoryArpReplyTx": f3L3TrafficIpInterfaceHistoryArpReplyTx,
       "f3L3TrafficIpInterfaceHistoryArpReplyRx": f3L3TrafficIpInterfaceHistoryArpReplyRx,
       "f3L3TrafficIpInterfaceThresholdTable": f3L3TrafficIpInterfaceThresholdTable,
       "f3L3TrafficIpInterfaceThresholdEntry": f3L3TrafficIpInterfaceThresholdEntry,
       "f3L3TrafficIpInterfaceThresholdIndex": f3L3TrafficIpInterfaceThresholdIndex,
       "f3L3TrafficIpInterfaceThresholdInterval": f3L3TrafficIpInterfaceThresholdInterval,
       "f3L3TrafficIpInterfaceThresholdVariable": f3L3TrafficIpInterfaceThresholdVariable,
       "f3L3TrafficIpInterfaceThresholdValueLo": f3L3TrafficIpInterfaceThresholdValueLo,
       "f3L3TrafficIpInterfaceThresholdValueHi": f3L3TrafficIpInterfaceThresholdValueHi,
       "f3L3TrafficIpInterfaceThresholdMonValue": f3L3TrafficIpInterfaceThresholdMonValue,
       "f3L3AclRuleStatsTable": f3L3AclRuleStatsTable,
       "f3L3AclRuleStatsEntry": f3L3AclRuleStatsEntry,
       "f3L3AclRuleStatsIndex": f3L3AclRuleStatsIndex,
       "f3L3AclRuleStatsIntervalType": f3L3AclRuleStatsIntervalType,
       "f3L3AclRuleStatsValid": f3L3AclRuleStatsValid,
       "f3L3AclRuleStatsAction": f3L3AclRuleStatsAction,
       "f3L3AclRuleStatsRuleMatch": f3L3AclRuleStatsRuleMatch,
       "f3L3AclRuleHistoryTable": f3L3AclRuleHistoryTable,
       "f3L3AclRuleHistoryEntry": f3L3AclRuleHistoryEntry,
       "f3L3AclRuleHistoryIndex": f3L3AclRuleHistoryIndex,
       "f3L3AclRuleHistoryTime": f3L3AclRuleHistoryTime,
       "f3L3AclRuleHistoryValid": f3L3AclRuleHistoryValid,
       "f3L3AclRuleHistoryAction": f3L3AclRuleHistoryAction,
       "f3L3AclRuleHistoryRuleMatch": f3L3AclRuleHistoryRuleMatch,
       "f3L3AclRuleThresholdTable": f3L3AclRuleThresholdTable,
       "f3L3AclRuleThresholdEntry": f3L3AclRuleThresholdEntry,
       "f3L3AclRuleThresholdIndex": f3L3AclRuleThresholdIndex,
       "f3L3AclRuleThresholdInterval": f3L3AclRuleThresholdInterval,
       "f3L3AclRuleThresholdVariable": f3L3AclRuleThresholdVariable,
       "f3L3AclRuleThresholdValueLo": f3L3AclRuleThresholdValueLo,
       "f3L3AclRuleThresholdValueHi": f3L3AclRuleThresholdValueHi,
       "f3L3AclRuleThresholdMonValue": f3L3AclRuleThresholdMonValue,
       "f3L3QosPolicerStatsTable": f3L3QosPolicerStatsTable,
       "f3L3QosPolicerStatsEntry": f3L3QosPolicerStatsEntry,
       "f3L3QosPolicerStatsIndex": f3L3QosPolicerStatsIndex,
       "f3L3QosPolicerStatsIntervalType": f3L3QosPolicerStatsIntervalType,
       "f3L3QosPolicerStatsValid": f3L3QosPolicerStatsValid,
       "f3L3QosPolicerStatsAction": f3L3QosPolicerStatsAction,
       "f3L3QosPolicerStatsFMG": f3L3QosPolicerStatsFMG,
       "f3L3QosPolicerStatsFMY": f3L3QosPolicerStatsFMY,
       "f3L3QosPolicerStatsFMYD": f3L3QosPolicerStatsFMYD,
       "f3L3QosPolicerStatsFMRD": f3L3QosPolicerStatsFMRD,
       "f3L3QosPolicerStatsBytesIn": f3L3QosPolicerStatsBytesIn,
       "f3L3QosPolicerStatsBytesOut": f3L3QosPolicerStatsBytesOut,
       "f3L3QosPolicerStatsABR": f3L3QosPolicerStatsABR,
       "f3L3QosPolicerHistoryTable": f3L3QosPolicerHistoryTable,
       "f3L3QosPolicerHistoryEntry": f3L3QosPolicerHistoryEntry,
       "f3L3QosPolicerHistoryIndex": f3L3QosPolicerHistoryIndex,
       "f3L3QosPolicerHistoryTime": f3L3QosPolicerHistoryTime,
       "f3L3QosPolicerHistoryValid": f3L3QosPolicerHistoryValid,
       "f3L3QosPolicerHistoryAction": f3L3QosPolicerHistoryAction,
       "f3L3QosPolicerHistoryFMG": f3L3QosPolicerHistoryFMG,
       "f3L3QosPolicerHistoryFMY": f3L3QosPolicerHistoryFMY,
       "f3L3QosPolicerHistoryFMYD": f3L3QosPolicerHistoryFMYD,
       "f3L3QosPolicerHistoryFMRD": f3L3QosPolicerHistoryFMRD,
       "f3L3QosPolicerHistoryBytesIn": f3L3QosPolicerHistoryBytesIn,
       "f3L3QosPolicerHistoryBytesOut": f3L3QosPolicerHistoryBytesOut,
       "f3L3QosPolicerHistoryABR": f3L3QosPolicerHistoryABR,
       "f3L3QosPolicerThresholdTable": f3L3QosPolicerThresholdTable,
       "f3L3QosPolicerThresholdEntry": f3L3QosPolicerThresholdEntry,
       "f3L3QosPolicerThresholdIndex": f3L3QosPolicerThresholdIndex,
       "f3L3QosPolicerThresholdInterval": f3L3QosPolicerThresholdInterval,
       "f3L3QosPolicerThresholdVariable": f3L3QosPolicerThresholdVariable,
       "f3L3QosPolicerThresholdValueLo": f3L3QosPolicerThresholdValueLo,
       "f3L3QosPolicerThresholdValueHi": f3L3QosPolicerThresholdValueHi,
       "f3L3QosPolicerThresholdMonValue": f3L3QosPolicerThresholdMonValue,
       "f3L3QosShaperStatsTable": f3L3QosShaperStatsTable,
       "f3L3QosShaperStatsEntry": f3L3QosShaperStatsEntry,
       "f3L3QosShaperStatsIndex": f3L3QosShaperStatsIndex,
       "f3L3QosShaperStatsIntervalType": f3L3QosShaperStatsIntervalType,
       "f3L3QosShaperStatsValid": f3L3QosShaperStatsValid,
       "f3L3QosShaperStatsAction": f3L3QosShaperStatsAction,
       "f3L3QosShaperStatsBT": f3L3QosShaperStatsBT,
       "f3L3QosShaperStatsBTD": f3L3QosShaperStatsBTD,
       "f3L3QosShaperStatsFD": f3L3QosShaperStatsFD,
       "f3L3QosShaperStatsFTD": f3L3QosShaperStatsFTD,
       "f3L3QosShaperStatsBR": f3L3QosShaperStatsBR,
       "f3L3QosShaperStatsFR": f3L3QosShaperStatsFR,
       "f3L3QosShaperStatsABRRL": f3L3QosShaperStatsABRRL,
       "f3L3QosShaperStatsABRRLR": f3L3QosShaperStatsABRRLR,
       "f3L3QosShaperStatsBREDD": f3L3QosShaperStatsBREDD,
       "f3L3QosShaperStatsFREDD": f3L3QosShaperStatsFREDD,
       "f3L3QosShaperHistoryTable": f3L3QosShaperHistoryTable,
       "f3L3QosShaperHistoryEntry": f3L3QosShaperHistoryEntry,
       "f3L3QosShaperHistoryIndex": f3L3QosShaperHistoryIndex,
       "f3L3QosShaperHistoryTime": f3L3QosShaperHistoryTime,
       "f3L3QosShaperHistoryValid": f3L3QosShaperHistoryValid,
       "f3L3QosShaperHistoryAction": f3L3QosShaperHistoryAction,
       "f3L3QosShaperHistoryBT": f3L3QosShaperHistoryBT,
       "f3L3QosShaperHistoryBTD": f3L3QosShaperHistoryBTD,
       "f3L3QosShaperHistoryFD": f3L3QosShaperHistoryFD,
       "f3L3QosShaperHistoryFTD": f3L3QosShaperHistoryFTD,
       "f3L3QosShaperHistoryBR": f3L3QosShaperHistoryBR,
       "f3L3QosShaperHistoryFR": f3L3QosShaperHistoryFR,
       "f3L3QosShaperHistoryABRRL": f3L3QosShaperHistoryABRRL,
       "f3L3QosShaperHistoryABRRLR": f3L3QosShaperHistoryABRRLR,
       "f3L3QosShaperHistoryBREDD": f3L3QosShaperHistoryBREDD,
       "f3L3QosShaperHistoryFREDD": f3L3QosShaperHistoryFREDD,
       "f3L3QosShaperThresholdTable": f3L3QosShaperThresholdTable,
       "f3L3QosShaperThresholdEntry": f3L3QosShaperThresholdEntry,
       "f3L3QosShaperThresholdIndex": f3L3QosShaperThresholdIndex,
       "f3L3QosShaperThresholdInterval": f3L3QosShaperThresholdInterval,
       "f3L3QosShaperThresholdVariable": f3L3QosShaperThresholdVariable,
       "f3L3QosShaperThresholdValueLo": f3L3QosShaperThresholdValueLo,
       "f3L3QosShaperThresholdValueHi": f3L3QosShaperThresholdValueHi,
       "f3L3QosShaperThresholdMonValue": f3L3QosShaperThresholdMonValue,
       "f3L2A2NAclRuleStatsTable": f3L2A2NAclRuleStatsTable,
       "f3L2A2NAclRuleStatsEntry": f3L2A2NAclRuleStatsEntry,
       "f3L2A2NAclRuleStatsIndex": f3L2A2NAclRuleStatsIndex,
       "f3L2A2NAclRuleStatsIntervalType": f3L2A2NAclRuleStatsIntervalType,
       "f3L2A2NAclRuleStatsValid": f3L2A2NAclRuleStatsValid,
       "f3L2A2NAclRuleStatsAction": f3L2A2NAclRuleStatsAction,
       "f3L2A2NAclRuleStatsRuleMatch": f3L2A2NAclRuleStatsRuleMatch,
       "f3L2A2NAclRuleHistoryTable": f3L2A2NAclRuleHistoryTable,
       "f3L2A2NAclRuleHistoryEntry": f3L2A2NAclRuleHistoryEntry,
       "f3L2A2NAclRuleHistoryIndex": f3L2A2NAclRuleHistoryIndex,
       "f3L2A2NAclRuleHistoryTime": f3L2A2NAclRuleHistoryTime,
       "f3L2A2NAclRuleHistoryValid": f3L2A2NAclRuleHistoryValid,
       "f3L2A2NAclRuleHistoryAction": f3L2A2NAclRuleHistoryAction,
       "f3L2A2NAclRuleHistoryRuleMatch": f3L2A2NAclRuleHistoryRuleMatch,
       "f3L2A2NAclRuleThresholdTable": f3L2A2NAclRuleThresholdTable,
       "f3L2A2NAclRuleThresholdEntry": f3L2A2NAclRuleThresholdEntry,
       "f3L2A2NAclRuleThresholdIndex": f3L2A2NAclRuleThresholdIndex,
       "f3L2A2NAclRuleThresholdInterval": f3L2A2NAclRuleThresholdInterval,
       "f3L2A2NAclRuleThresholdVariable": f3L2A2NAclRuleThresholdVariable,
       "f3L2A2NAclRuleThresholdValueLo": f3L2A2NAclRuleThresholdValueLo,
       "f3L2A2NAclRuleThresholdValueHi": f3L2A2NAclRuleThresholdValueHi,
       "f3L2A2NAclRuleThresholdMonValue": f3L2A2NAclRuleThresholdMonValue,
       "f3L2N2AAclRuleStatsTable": f3L2N2AAclRuleStatsTable,
       "f3L2N2AAclRuleStatsEntry": f3L2N2AAclRuleStatsEntry,
       "f3L2N2AAclRuleStatsIndex": f3L2N2AAclRuleStatsIndex,
       "f3L2N2AAclRuleStatsIntervalType": f3L2N2AAclRuleStatsIntervalType,
       "f3L2N2AAclRuleStatsValid": f3L2N2AAclRuleStatsValid,
       "f3L2N2AAclRuleStatsAction": f3L2N2AAclRuleStatsAction,
       "f3L2N2AAclRuleStatsRuleMatch": f3L2N2AAclRuleStatsRuleMatch,
       "f3L2N2AAclRuleHistoryTable": f3L2N2AAclRuleHistoryTable,
       "f3L2N2AAclRuleHistoryEntry": f3L2N2AAclRuleHistoryEntry,
       "f3L2N2AAclRuleHistoryIndex": f3L2N2AAclRuleHistoryIndex,
       "f3L2N2AAclRuleHistoryTime": f3L2N2AAclRuleHistoryTime,
       "f3L2N2AAclRuleHistoryValid": f3L2N2AAclRuleHistoryValid,
       "f3L2N2AAclRuleHistoryAction": f3L2N2AAclRuleHistoryAction,
       "f3L2N2AAclRuleHistoryRuleMatch": f3L2N2AAclRuleHistoryRuleMatch,
       "f3L2N2AAclRuleThresholdTable": f3L2N2AAclRuleThresholdTable,
       "f3L2N2AAclRuleThresholdEntry": f3L2N2AAclRuleThresholdEntry,
       "f3L2N2AAclRuleThresholdIndex": f3L2N2AAclRuleThresholdIndex,
       "f3L2N2AAclRuleThresholdInterval": f3L2N2AAclRuleThresholdInterval,
       "f3L2N2AAclRuleThresholdVariable": f3L2N2AAclRuleThresholdVariable,
       "f3L2N2AAclRuleThresholdValueLo": f3L2N2AAclRuleThresholdValueLo,
       "f3L2N2AAclRuleThresholdValueHi": f3L2N2AAclRuleThresholdValueHi,
       "f3L2N2AAclRuleThresholdMonValue": f3L2N2AAclRuleThresholdMonValue,
       "f3L3Notifications": f3L3Notifications,
       "f3L3FlowPointThresholdCrossingAlert": f3L3FlowPointThresholdCrossingAlert,
       "f3L3QosPolicerThresholdCrossingAlert": f3L3QosPolicerThresholdCrossingAlert,
       "f3L3QosShaperThresholdCrossingAlert": f3L3QosShaperThresholdCrossingAlert,
       "f3L3TrafficIpInterfaceThresholdCrossingAlert": f3L3TrafficIpInterfaceThresholdCrossingAlert,
       "f3L3AclRuleThresholdCrossingAlert": f3L3AclRuleThresholdCrossingAlert,
       "f3L2A2NAclRuleThresholdCrossingAlert": f3L2A2NAclRuleThresholdCrossingAlert,
       "f3L2N2AAclRuleThresholdCrossingAlert": f3L2N2AAclRuleThresholdCrossingAlert,
       "f3L3Conformance": f3L3Conformance,
       "f3L3Compliances": f3L3Compliances,
       "f3L3Compliance": f3L3Compliance,
       "f3L3Groups": f3L3Groups,
       "f3L3ObjectsGroup": f3L3ObjectsGroup,
       "f3L3PerfGroup": f3L3PerfGroup}
)
