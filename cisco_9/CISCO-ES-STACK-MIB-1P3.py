# SNMP MIB module (CISCO-ES-STACK-MIB-1P3) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ES-STACK-MIB-1P3.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:14:07 2025
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

(sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName")

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
 enterprises,
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
    "enterprises",
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



class MacAddr(OctetString):
    """Custom type MacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco_ObjectIdentity = ObjectIdentity
cisco = _Cisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
_Workgroup_ObjectIdentity = ObjectIdentity
workgroup = _Workgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5)
)
_EsStack_ObjectIdentity = ObjectIdentity
esStack = _EsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14)
)
_CiscoEsDmns_ObjectIdentity = ObjectIdentity
ciscoEsDmns = _CiscoEsDmns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5)
)
_CiscoEsDmnPortTable_Object = MibTable
ciscoEsDmnPortTable = _CiscoEsDmnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoEsDmnPortTable.setStatus("mandatory")
_CiscoEsDmnPortEntry_Object = MibTableRow
ciscoEsDmnPortEntry = _CiscoEsDmnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 1, 1)
)
ciscoEsDmnPortEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnPortDmnNumber"),
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnPortSwitchNumber"),
)
if mibBuilder.loadTexts:
    ciscoEsDmnPortEntry.setStatus("mandatory")


class _CiscoEsDmnPortDmnNumber_Type(Integer32):
    """Custom type ciscoEsDmnPortDmnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsDmnPortDmnNumber_Type.__name__ = "Integer32"
_CiscoEsDmnPortDmnNumber_Object = MibTableColumn
ciscoEsDmnPortDmnNumber = _CiscoEsDmnPortDmnNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 1, 1, 1),
    _CiscoEsDmnPortDmnNumber_Type()
)
ciscoEsDmnPortDmnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnPortDmnNumber.setStatus("mandatory")


class _CiscoEsDmnPortSwitchNumber_Type(Integer32):
    """Custom type ciscoEsDmnPortSwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsDmnPortSwitchNumber_Type.__name__ = "Integer32"
_CiscoEsDmnPortSwitchNumber_Object = MibTableColumn
ciscoEsDmnPortSwitchNumber = _CiscoEsDmnPortSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 1, 1, 2),
    _CiscoEsDmnPortSwitchNumber_Type()
)
ciscoEsDmnPortSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnPortSwitchNumber.setStatus("mandatory")


class _CiscoEsDmnPortPorts_Type(OctetString):
    """Custom type ciscoEsDmnPortPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_CiscoEsDmnPortPorts_Type.__name__ = "OctetString"
_CiscoEsDmnPortPorts_Object = MibTableColumn
ciscoEsDmnPortPorts = _CiscoEsDmnPortPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 1, 1, 3),
    _CiscoEsDmnPortPorts_Type()
)
ciscoEsDmnPortPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnPortPorts.setStatus("mandatory")
_CiscoEsDmnInfoTable_Object = MibTable
ciscoEsDmnInfoTable = _CiscoEsDmnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2)
)
if mibBuilder.loadTexts:
    ciscoEsDmnInfoTable.setStatus("mandatory")
_CiscoEsDmnInfoEntry_Object = MibTableRow
ciscoEsDmnInfoEntry = _CiscoEsDmnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1)
)
ciscoEsDmnInfoEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnInfoDmnNumber"),
)
if mibBuilder.loadTexts:
    ciscoEsDmnInfoEntry.setStatus("mandatory")


class _CiscoEsDmnInfoDmnNumber_Type(Integer32):
    """Custom type ciscoEsDmnInfoDmnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsDmnInfoDmnNumber_Type.__name__ = "Integer32"
_CiscoEsDmnInfoDmnNumber_Object = MibTableColumn
ciscoEsDmnInfoDmnNumber = _CiscoEsDmnInfoDmnNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 1),
    _CiscoEsDmnInfoDmnNumber_Type()
)
ciscoEsDmnInfoDmnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoDmnNumber.setStatus("mandatory")


class _CiscoEsDmnInfoState_Type(Integer32):
    """Custom type ciscoEsDmnInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CiscoEsDmnInfoState_Type.__name__ = "Integer32"
_CiscoEsDmnInfoState_Object = MibTableColumn
ciscoEsDmnInfoState = _CiscoEsDmnInfoState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 2),
    _CiscoEsDmnInfoState_Type()
)
ciscoEsDmnInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoState.setStatus("mandatory")


class _CiscoEsDmnInfoName_Type(DisplayString):
    """Custom type ciscoEsDmnInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiscoEsDmnInfoName_Type.__name__ = "DisplayString"
_CiscoEsDmnInfoName_Object = MibTableColumn
ciscoEsDmnInfoName = _CiscoEsDmnInfoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 3),
    _CiscoEsDmnInfoName_Type()
)
ciscoEsDmnInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoName.setStatus("mandatory")
_CiscoEsDmnInfoBaseAddr_Type = MacAddr
_CiscoEsDmnInfoBaseAddr_Object = MibTableColumn
ciscoEsDmnInfoBaseAddr = _CiscoEsDmnInfoBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 4),
    _CiscoEsDmnInfoBaseAddr_Type()
)
ciscoEsDmnInfoBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoBaseAddr.setStatus("mandatory")
_CiscoEsDmnInfoIfIndex_Type = Integer32
_CiscoEsDmnInfoIfIndex_Object = MibTableColumn
ciscoEsDmnInfoIfIndex = _CiscoEsDmnInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 5),
    _CiscoEsDmnInfoIfIndex_Type()
)
ciscoEsDmnInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoIfIndex.setStatus("mandatory")


class _CiscoEsDmnInfoIpState_Type(Integer32):
    """Custom type ciscoEsDmnInfoIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("auto-bootp", 2),
          ("always-bootp", 3))
    )


_CiscoEsDmnInfoIpState_Type.__name__ = "Integer32"
_CiscoEsDmnInfoIpState_Object = MibTableColumn
ciscoEsDmnInfoIpState = _CiscoEsDmnInfoIpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 6),
    _CiscoEsDmnInfoIpState_Type()
)
ciscoEsDmnInfoIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoIpState.setStatus("mandatory")
_CiscoEsDmnInfoIpAddress_Type = IpAddress
_CiscoEsDmnInfoIpAddress_Object = MibTableColumn
ciscoEsDmnInfoIpAddress = _CiscoEsDmnInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 7),
    _CiscoEsDmnInfoIpAddress_Type()
)
ciscoEsDmnInfoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoIpAddress.setStatus("mandatory")
_CiscoEsDmnInfoIpSubnetMask_Type = IpAddress
_CiscoEsDmnInfoIpSubnetMask_Object = MibTableColumn
ciscoEsDmnInfoIpSubnetMask = _CiscoEsDmnInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 8),
    _CiscoEsDmnInfoIpSubnetMask_Type()
)
ciscoEsDmnInfoIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoIpSubnetMask.setStatus("mandatory")
_CiscoEsDmnInfoIpDefaultGateway_Type = IpAddress
_CiscoEsDmnInfoIpDefaultGateway_Object = MibTableColumn
ciscoEsDmnInfoIpDefaultGateway = _CiscoEsDmnInfoIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 9),
    _CiscoEsDmnInfoIpDefaultGateway_Type()
)
ciscoEsDmnInfoIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoIpDefaultGateway.setStatus("mandatory")


class _CiscoEsDmnInfoStp_Type(Integer32):
    """Custom type ciscoEsDmnInfoStp based on Integer32"""
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


_CiscoEsDmnInfoStp_Type.__name__ = "Integer32"
_CiscoEsDmnInfoStp_Object = MibTableColumn
ciscoEsDmnInfoStp = _CiscoEsDmnInfoStp_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 10),
    _CiscoEsDmnInfoStp_Type()
)
ciscoEsDmnInfoStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoStp.setStatus("mandatory")
_CiscoEsDmnInfoNumStations_Type = Gauge32
_CiscoEsDmnInfoNumStations_Object = MibTableColumn
ciscoEsDmnInfoNumStations = _CiscoEsDmnInfoNumStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 11),
    _CiscoEsDmnInfoNumStations_Type()
)
ciscoEsDmnInfoNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoNumStations.setStatus("mandatory")
_CiscoEsDmnInfoMaxStations_Type = Integer32
_CiscoEsDmnInfoMaxStations_Object = MibTableColumn
ciscoEsDmnInfoMaxStations = _CiscoEsDmnInfoMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 2, 1, 12),
    _CiscoEsDmnInfoMaxStations_Type()
)
ciscoEsDmnInfoMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnInfoMaxStations.setStatus("mandatory")
_CiscoEsDmnStpTable_Object = MibTable
ciscoEsDmnStpTable = _CiscoEsDmnStpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3)
)
if mibBuilder.loadTexts:
    ciscoEsDmnStpTable.setStatus("mandatory")
_CiscoEsDmnStpEntry_Object = MibTableRow
ciscoEsDmnStpEntry = _CiscoEsDmnStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1)
)
ciscoEsDmnStpEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnStpDmnIndex"),
)
if mibBuilder.loadTexts:
    ciscoEsDmnStpEntry.setStatus("mandatory")


class _CiscoEsDmnStpDmnIndex_Type(Integer32):
    """Custom type ciscoEsDmnStpDmnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsDmnStpDmnIndex_Type.__name__ = "Integer32"
_CiscoEsDmnStpDmnIndex_Object = MibTableColumn
ciscoEsDmnStpDmnIndex = _CiscoEsDmnStpDmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 1),
    _CiscoEsDmnStpDmnIndex_Type()
)
ciscoEsDmnStpDmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpDmnIndex.setStatus("mandatory")


class _CiscoEsDmnStpPriority_Type(Integer32):
    """Custom type ciscoEsDmnStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoEsDmnStpPriority_Type.__name__ = "Integer32"
_CiscoEsDmnStpPriority_Object = MibTableColumn
ciscoEsDmnStpPriority = _CiscoEsDmnStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 2),
    _CiscoEsDmnStpPriority_Type()
)
ciscoEsDmnStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnStpPriority.setStatus("mandatory")
_CiscoEsDmnStpTimeSinceTopologyChange_Type = TimeTicks
_CiscoEsDmnStpTimeSinceTopologyChange_Object = MibTableColumn
ciscoEsDmnStpTimeSinceTopologyChange = _CiscoEsDmnStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 3),
    _CiscoEsDmnStpTimeSinceTopologyChange_Type()
)
ciscoEsDmnStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpTimeSinceTopologyChange.setStatus("mandatory")
_CiscoEsDmnStpTopChanges_Type = Counter32
_CiscoEsDmnStpTopChanges_Object = MibTableColumn
ciscoEsDmnStpTopChanges = _CiscoEsDmnStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 4),
    _CiscoEsDmnStpTopChanges_Type()
)
ciscoEsDmnStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpTopChanges.setStatus("mandatory")
_CiscoEsDmnStpDesignatedRoot_Type = BridgeId
_CiscoEsDmnStpDesignatedRoot_Object = MibTableColumn
ciscoEsDmnStpDesignatedRoot = _CiscoEsDmnStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 5),
    _CiscoEsDmnStpDesignatedRoot_Type()
)
ciscoEsDmnStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpDesignatedRoot.setStatus("mandatory")
_CiscoEsDmnStpRootCost_Type = Integer32
_CiscoEsDmnStpRootCost_Object = MibTableColumn
ciscoEsDmnStpRootCost = _CiscoEsDmnStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 6),
    _CiscoEsDmnStpRootCost_Type()
)
ciscoEsDmnStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpRootCost.setStatus("mandatory")
_CiscoEsDmnStpRootPort_Type = Integer32
_CiscoEsDmnStpRootPort_Object = MibTableColumn
ciscoEsDmnStpRootPort = _CiscoEsDmnStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 7),
    _CiscoEsDmnStpRootPort_Type()
)
ciscoEsDmnStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpRootPort.setStatus("mandatory")
_CiscoEsDmnStpMaxAge_Type = Integer32
_CiscoEsDmnStpMaxAge_Object = MibTableColumn
ciscoEsDmnStpMaxAge = _CiscoEsDmnStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 8),
    _CiscoEsDmnStpMaxAge_Type()
)
ciscoEsDmnStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpMaxAge.setStatus("mandatory")
_CiscoEsDmnStpHelloTime_Type = Integer32
_CiscoEsDmnStpHelloTime_Object = MibTableColumn
ciscoEsDmnStpHelloTime = _CiscoEsDmnStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 9),
    _CiscoEsDmnStpHelloTime_Type()
)
ciscoEsDmnStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpHelloTime.setStatus("mandatory")
_CiscoEsDmnStpHoldTime_Type = Integer32
_CiscoEsDmnStpHoldTime_Object = MibTableColumn
ciscoEsDmnStpHoldTime = _CiscoEsDmnStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 10),
    _CiscoEsDmnStpHoldTime_Type()
)
ciscoEsDmnStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpHoldTime.setStatus("mandatory")
_CiscoEsDmnStpForwardDelay_Type = Integer32
_CiscoEsDmnStpForwardDelay_Object = MibTableColumn
ciscoEsDmnStpForwardDelay = _CiscoEsDmnStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 11),
    _CiscoEsDmnStpForwardDelay_Type()
)
ciscoEsDmnStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStpForwardDelay.setStatus("mandatory")


class _CiscoEsDmnStpBridgeMaxAge_Type(Integer32):
    """Custom type ciscoEsDmnStpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_CiscoEsDmnStpBridgeMaxAge_Type.__name__ = "Integer32"
_CiscoEsDmnStpBridgeMaxAge_Object = MibTableColumn
ciscoEsDmnStpBridgeMaxAge = _CiscoEsDmnStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 12),
    _CiscoEsDmnStpBridgeMaxAge_Type()
)
ciscoEsDmnStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnStpBridgeMaxAge.setStatus("mandatory")


class _CiscoEsDmnStpBridgeHelloTime_Type(Integer32):
    """Custom type ciscoEsDmnStpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CiscoEsDmnStpBridgeHelloTime_Type.__name__ = "Integer32"
_CiscoEsDmnStpBridgeHelloTime_Object = MibTableColumn
ciscoEsDmnStpBridgeHelloTime = _CiscoEsDmnStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 13),
    _CiscoEsDmnStpBridgeHelloTime_Type()
)
ciscoEsDmnStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnStpBridgeHelloTime.setStatus("mandatory")


class _CiscoEsDmnStpBridgeForwardDelay_Type(Integer32):
    """Custom type ciscoEsDmnStpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_CiscoEsDmnStpBridgeForwardDelay_Type.__name__ = "Integer32"
_CiscoEsDmnStpBridgeForwardDelay_Object = MibTableColumn
ciscoEsDmnStpBridgeForwardDelay = _CiscoEsDmnStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 3, 1, 14),
    _CiscoEsDmnStpBridgeForwardDelay_Type()
)
ciscoEsDmnStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoEsDmnStpBridgeForwardDelay.setStatus("mandatory")
_CiscoEsDmnStationTable_Object = MibTable
ciscoEsDmnStationTable = _CiscoEsDmnStationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 4)
)
if mibBuilder.loadTexts:
    ciscoEsDmnStationTable.setStatus("mandatory")
_CiscoEsDmnStationEntry_Object = MibTableRow
ciscoEsDmnStationEntry = _CiscoEsDmnStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 4, 1)
)
ciscoEsDmnStationEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnStationDmnIndex"),
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnStationBoxNum"),
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnStationAddress"),
)
if mibBuilder.loadTexts:
    ciscoEsDmnStationEntry.setStatus("mandatory")


class _CiscoEsDmnStationDmnIndex_Type(Integer32):
    """Custom type ciscoEsDmnStationDmnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CiscoEsDmnStationDmnIndex_Type.__name__ = "Integer32"
_CiscoEsDmnStationDmnIndex_Object = MibTableColumn
ciscoEsDmnStationDmnIndex = _CiscoEsDmnStationDmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 4, 1, 1),
    _CiscoEsDmnStationDmnIndex_Type()
)
ciscoEsDmnStationDmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStationDmnIndex.setStatus("mandatory")


class _CiscoEsDmnStationBoxNum_Type(Integer32):
    """Custom type ciscoEsDmnStationBoxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiscoEsDmnStationBoxNum_Type.__name__ = "Integer32"
_CiscoEsDmnStationBoxNum_Object = MibTableColumn
ciscoEsDmnStationBoxNum = _CiscoEsDmnStationBoxNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 4, 1, 2),
    _CiscoEsDmnStationBoxNum_Type()
)
ciscoEsDmnStationBoxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStationBoxNum.setStatus("mandatory")


class _CiscoEsDmnStationAddress_Type(OctetString):
    """Custom type ciscoEsDmnStationAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_CiscoEsDmnStationAddress_Type.__name__ = "OctetString"
_CiscoEsDmnStationAddress_Object = MibTableColumn
ciscoEsDmnStationAddress = _CiscoEsDmnStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 4, 1, 3),
    _CiscoEsDmnStationAddress_Type()
)
ciscoEsDmnStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStationAddress.setStatus("mandatory")
_CiscoEsDmnStationPort_Type = Integer32
_CiscoEsDmnStationPort_Object = MibTableColumn
ciscoEsDmnStationPort = _CiscoEsDmnStationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 4, 1, 4),
    _CiscoEsDmnStationPort_Type()
)
ciscoEsDmnStationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStationPort.setStatus("mandatory")


class _CiscoEsDmnStationTraffic_Type(OctetString):
    """Custom type ciscoEsDmnStationTraffic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_CiscoEsDmnStationTraffic_Type.__name__ = "OctetString"
_CiscoEsDmnStationTraffic_Object = MibTableColumn
ciscoEsDmnStationTraffic = _CiscoEsDmnStationTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 4, 1, 5),
    _CiscoEsDmnStationTraffic_Type()
)
ciscoEsDmnStationTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsDmnStationTraffic.setStatus("mandatory")
_CiscoEsOptDmnStaTable_Object = MibTable
ciscoEsOptDmnStaTable = _CiscoEsOptDmnStaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 5)
)
if mibBuilder.loadTexts:
    ciscoEsOptDmnStaTable.setStatus("mandatory")
_CiscoEsOptDmnStaEntry_Object = MibTableRow
ciscoEsOptDmnStaEntry = _CiscoEsOptDmnStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 5, 1)
)
ciscoEsOptDmnStaEntry.setIndexNames(
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnStationDmnIndex"),
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsDmnStationBoxNum"),
    (0, "CISCO-ES-STACK-MIB-1P3", "ciscoEsOptDmnStaPos"),
)
if mibBuilder.loadTexts:
    ciscoEsOptDmnStaEntry.setStatus("mandatory")


class _CiscoEsOptDmnStaPos_Type(Integer32):
    """Custom type ciscoEsOptDmnStaPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoEsOptDmnStaPos_Type.__name__ = "Integer32"
_CiscoEsOptDmnStaPos_Object = MibTableColumn
ciscoEsOptDmnStaPos = _CiscoEsOptDmnStaPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 5, 1, 1),
    _CiscoEsOptDmnStaPos_Type()
)
ciscoEsOptDmnStaPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsOptDmnStaPos.setStatus("mandatory")
_CiscoEsOptDmnStaVal_Type = OctetString
_CiscoEsOptDmnStaVal_Object = MibTableColumn
ciscoEsOptDmnStaVal = _CiscoEsOptDmnStaVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 14, 5, 5, 1, 2),
    _CiscoEsOptDmnStaVal_Type()
)
ciscoEsOptDmnStaVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoEsOptDmnStaVal.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ES-STACK-MIB-1P3",
    **{"MacAddr": MacAddr,
       "BridgeId": BridgeId,
       "cisco": cisco,
       "workgroup": workgroup,
       "esStack": esStack,
       "ciscoEsDmns": ciscoEsDmns,
       "ciscoEsDmnPortTable": ciscoEsDmnPortTable,
       "ciscoEsDmnPortEntry": ciscoEsDmnPortEntry,
       "ciscoEsDmnPortDmnNumber": ciscoEsDmnPortDmnNumber,
       "ciscoEsDmnPortSwitchNumber": ciscoEsDmnPortSwitchNumber,
       "ciscoEsDmnPortPorts": ciscoEsDmnPortPorts,
       "ciscoEsDmnInfoTable": ciscoEsDmnInfoTable,
       "ciscoEsDmnInfoEntry": ciscoEsDmnInfoEntry,
       "ciscoEsDmnInfoDmnNumber": ciscoEsDmnInfoDmnNumber,
       "ciscoEsDmnInfoState": ciscoEsDmnInfoState,
       "ciscoEsDmnInfoName": ciscoEsDmnInfoName,
       "ciscoEsDmnInfoBaseAddr": ciscoEsDmnInfoBaseAddr,
       "ciscoEsDmnInfoIfIndex": ciscoEsDmnInfoIfIndex,
       "ciscoEsDmnInfoIpState": ciscoEsDmnInfoIpState,
       "ciscoEsDmnInfoIpAddress": ciscoEsDmnInfoIpAddress,
       "ciscoEsDmnInfoIpSubnetMask": ciscoEsDmnInfoIpSubnetMask,
       "ciscoEsDmnInfoIpDefaultGateway": ciscoEsDmnInfoIpDefaultGateway,
       "ciscoEsDmnInfoStp": ciscoEsDmnInfoStp,
       "ciscoEsDmnInfoNumStations": ciscoEsDmnInfoNumStations,
       "ciscoEsDmnInfoMaxStations": ciscoEsDmnInfoMaxStations,
       "ciscoEsDmnStpTable": ciscoEsDmnStpTable,
       "ciscoEsDmnStpEntry": ciscoEsDmnStpEntry,
       "ciscoEsDmnStpDmnIndex": ciscoEsDmnStpDmnIndex,
       "ciscoEsDmnStpPriority": ciscoEsDmnStpPriority,
       "ciscoEsDmnStpTimeSinceTopologyChange": ciscoEsDmnStpTimeSinceTopologyChange,
       "ciscoEsDmnStpTopChanges": ciscoEsDmnStpTopChanges,
       "ciscoEsDmnStpDesignatedRoot": ciscoEsDmnStpDesignatedRoot,
       "ciscoEsDmnStpRootCost": ciscoEsDmnStpRootCost,
       "ciscoEsDmnStpRootPort": ciscoEsDmnStpRootPort,
       "ciscoEsDmnStpMaxAge": ciscoEsDmnStpMaxAge,
       "ciscoEsDmnStpHelloTime": ciscoEsDmnStpHelloTime,
       "ciscoEsDmnStpHoldTime": ciscoEsDmnStpHoldTime,
       "ciscoEsDmnStpForwardDelay": ciscoEsDmnStpForwardDelay,
       "ciscoEsDmnStpBridgeMaxAge": ciscoEsDmnStpBridgeMaxAge,
       "ciscoEsDmnStpBridgeHelloTime": ciscoEsDmnStpBridgeHelloTime,
       "ciscoEsDmnStpBridgeForwardDelay": ciscoEsDmnStpBridgeForwardDelay,
       "ciscoEsDmnStationTable": ciscoEsDmnStationTable,
       "ciscoEsDmnStationEntry": ciscoEsDmnStationEntry,
       "ciscoEsDmnStationDmnIndex": ciscoEsDmnStationDmnIndex,
       "ciscoEsDmnStationBoxNum": ciscoEsDmnStationBoxNum,
       "ciscoEsDmnStationAddress": ciscoEsDmnStationAddress,
       "ciscoEsDmnStationPort": ciscoEsDmnStationPort,
       "ciscoEsDmnStationTraffic": ciscoEsDmnStationTraffic,
       "ciscoEsOptDmnStaTable": ciscoEsOptDmnStaTable,
       "ciscoEsOptDmnStaEntry": ciscoEsOptDmnStaEntry,
       "ciscoEsOptDmnStaPos": ciscoEsOptDmnStaPos,
       "ciscoEsOptDmnStaVal": ciscoEsOptDmnStaVal}
)
