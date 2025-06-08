# SNMP MIB module (WLSX-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aruba_14823/WLSX-STACK-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:48:55 2025
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaStackState,) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaStackState")

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
 TextualConvention,
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
    "TextualConvention",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

wlsxStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19)
)
if mibBuilder.loadTexts:
    wlsxStackMIB.setRevisions(
        ("2011-08-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxStackMIBObjects_ObjectIdentity = ObjectIdentity
wlsxStackMIBObjects = _WlsxStackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1)
)
if mibBuilder.loadTexts:
    wlsxStackMIBObjects.setStatus("current")
_WlsxStackMember_ObjectIdentity = ObjectIdentity
wlsxStackMember = _WlsxStackMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1)
)
_WlsxStackMemberTable_Object = MibTable
wlsxStackMemberTable = _WlsxStackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxStackMemberTable.setStatus("current")
_WlsxStackMemberEntry_Object = MibTableRow
wlsxStackMemberEntry = _WlsxStackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1)
)
wlsxStackMemberEntry.setIndexNames(
    (0, "WLSX-STACK-MIB", "wlsxStackMemberId"),
)
if mibBuilder.loadTexts:
    wlsxStackMemberEntry.setStatus("current")
_WlsxStackMemberId_Type = Integer32
_WlsxStackMemberId_Object = MibTableColumn
wlsxStackMemberId = _WlsxStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 1),
    _WlsxStackMemberId_Type()
)
wlsxStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberId.setStatus("current")
_WlsxStackMemberState_Type = ArubaStackState
_WlsxStackMemberState_Object = MibTableColumn
wlsxStackMemberState = _WlsxStackMemberState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 2),
    _WlsxStackMemberState_Type()
)
wlsxStackMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberState.setStatus("current")
_WlsxStackMemberMacAddr_Type = MacAddress
_WlsxStackMemberMacAddr_Object = MibTableColumn
wlsxStackMemberMacAddr = _WlsxStackMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 3),
    _WlsxStackMemberMacAddr_Type()
)
wlsxStackMemberMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberMacAddr.setStatus("current")
_WlsxStackMemberPriority_Type = Integer32
_WlsxStackMemberPriority_Object = MibTableColumn
wlsxStackMemberPriority = _WlsxStackMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 4),
    _WlsxStackMemberPriority_Type()
)
wlsxStackMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberPriority.setStatus("current")
_WlsxStackMemberHostName_Type = SnmpAdminString
_WlsxStackMemberHostName_Object = MibTableColumn
wlsxStackMemberHostName = _WlsxStackMemberHostName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 5),
    _WlsxStackMemberHostName_Type()
)
wlsxStackMemberHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberHostName.setStatus("current")
_WlsxStackMemberSysLocation_Type = SnmpAdminString
_WlsxStackMemberSysLocation_Object = MibTableColumn
wlsxStackMemberSysLocation = _WlsxStackMemberSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 6),
    _WlsxStackMemberSysLocation_Type()
)
wlsxStackMemberSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberSysLocation.setStatus("current")
_WlsxStackMemberChangeDetectSeqNum_Type = Integer32
_WlsxStackMemberChangeDetectSeqNum_Object = MibTableColumn
wlsxStackMemberChangeDetectSeqNum = _WlsxStackMemberChangeDetectSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 7),
    _WlsxStackMemberChangeDetectSeqNum_Type()
)
wlsxStackMemberChangeDetectSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberChangeDetectSeqNum.setStatus("current")
_WlsxStackMemberSysUpTime_Type = Integer32
_WlsxStackMemberSysUpTime_Object = MibTableColumn
wlsxStackMemberSysUpTime = _WlsxStackMemberSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 8),
    _WlsxStackMemberSysUpTime_Type()
)
wlsxStackMemberSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberSysUpTime.setStatus("current")
if mibBuilder.loadTexts:
    wlsxStackMemberSysUpTime.setUnits("seconds")
_WlsxStackMemberModelName_Type = SnmpAdminString
_WlsxStackMemberModelName_Object = MibTableColumn
wlsxStackMemberModelName = _WlsxStackMemberModelName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 9),
    _WlsxStackMemberModelName_Type()
)
wlsxStackMemberModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberModelName.setStatus("current")
_WlsxStackMemberSWVersion_Type = SnmpAdminString
_WlsxStackMemberSWVersion_Object = MibTableColumn
wlsxStackMemberSWVersion = _WlsxStackMemberSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 1, 1, 1, 10),
    _WlsxStackMemberSWVersion_Type()
)
wlsxStackMemberSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackMemberSWVersion.setStatus("current")
_WlsxStackProtoIf_ObjectIdentity = ObjectIdentity
wlsxStackProtoIf = _WlsxStackProtoIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2)
)
_WlsxStackProtoIfTable_Object = MibTable
wlsxStackProtoIfTable = _WlsxStackProtoIfTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wlsxStackProtoIfTable.setStatus("current")
_WlsxStackProtoIfEntry_Object = MibTableRow
wlsxStackProtoIfEntry = _WlsxStackProtoIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1)
)
wlsxStackProtoIfEntry.setIndexNames(
    (0, "WLSX-STACK-MIB", "wlsxStackMemberId"),
    (0, "WLSX-STACK-MIB", "wlsxStackProtoIfName"),
)
if mibBuilder.loadTexts:
    wlsxStackProtoIfEntry.setStatus("current")
_WlsxStackProtoIfName_Type = SnmpAdminString
_WlsxStackProtoIfName_Object = MibTableColumn
wlsxStackProtoIfName = _WlsxStackProtoIfName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 1),
    _WlsxStackProtoIfName_Type()
)
wlsxStackProtoIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxStackProtoIfName.setStatus("current")


class _WlsxStackProtoIfNeighborState_Type(Integer32):
    """Custom type wlsxStackProtoIfNeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_WlsxStackProtoIfNeighborState_Type.__name__ = "Integer32"
_WlsxStackProtoIfNeighborState_Object = MibTableColumn
wlsxStackProtoIfNeighborState = _WlsxStackProtoIfNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 2),
    _WlsxStackProtoIfNeighborState_Type()
)
wlsxStackProtoIfNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfNeighborState.setStatus("current")
_WlsxStackProtoIfStatTxPkt_Type = Counter64
_WlsxStackProtoIfStatTxPkt_Object = MibTableColumn
wlsxStackProtoIfStatTxPkt = _WlsxStackProtoIfStatTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 3),
    _WlsxStackProtoIfStatTxPkt_Type()
)
wlsxStackProtoIfStatTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatTxPkt.setStatus("current")
_WlsxStackProtoIfStatRxPkt_Type = Counter64
_WlsxStackProtoIfStatRxPkt_Object = MibTableColumn
wlsxStackProtoIfStatRxPkt = _WlsxStackProtoIfStatRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 4),
    _WlsxStackProtoIfStatRxPkt_Type()
)
wlsxStackProtoIfStatRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatRxPkt.setStatus("current")
_WlsxStackProtoIfStatTxErr_Type = Counter64
_WlsxStackProtoIfStatTxErr_Object = MibTableColumn
wlsxStackProtoIfStatTxErr = _WlsxStackProtoIfStatTxErr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 5),
    _WlsxStackProtoIfStatTxErr_Type()
)
wlsxStackProtoIfStatTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatTxErr.setStatus("current")
_WlsxStackProtoIfStatNeighborTransDown_Type = Counter64
_WlsxStackProtoIfStatNeighborTransDown_Object = MibTableColumn
wlsxStackProtoIfStatNeighborTransDown = _WlsxStackProtoIfStatNeighborTransDown_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 6),
    _WlsxStackProtoIfStatNeighborTransDown_Type()
)
wlsxStackProtoIfStatNeighborTransDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatNeighborTransDown.setStatus("current")
_WlsxStackProtoIfStatNeighborTransUp_Type = Counter64
_WlsxStackProtoIfStatNeighborTransUp_Object = MibTableColumn
wlsxStackProtoIfStatNeighborTransUp = _WlsxStackProtoIfStatNeighborTransUp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 7),
    _WlsxStackProtoIfStatNeighborTransUp_Type()
)
wlsxStackProtoIfStatNeighborTransUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatNeighborTransUp.setStatus("current")
_WlsxStackProtoIfStatKeepAliveTx_Type = Counter64
_WlsxStackProtoIfStatKeepAliveTx_Object = MibTableColumn
wlsxStackProtoIfStatKeepAliveTx = _WlsxStackProtoIfStatKeepAliveTx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 8),
    _WlsxStackProtoIfStatKeepAliveTx_Type()
)
wlsxStackProtoIfStatKeepAliveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatKeepAliveTx.setStatus("current")
_WlsxStackProtoIfStatKeepAliveRx_Type = Counter64
_WlsxStackProtoIfStatKeepAliveRx_Object = MibTableColumn
wlsxStackProtoIfStatKeepAliveRx = _WlsxStackProtoIfStatKeepAliveRx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 9),
    _WlsxStackProtoIfStatKeepAliveRx_Type()
)
wlsxStackProtoIfStatKeepAliveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatKeepAliveRx.setStatus("current")
_WlsxStackProtoIfStatRouteUpdateTx_Type = Counter64
_WlsxStackProtoIfStatRouteUpdateTx_Object = MibTableColumn
wlsxStackProtoIfStatRouteUpdateTx = _WlsxStackProtoIfStatRouteUpdateTx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 10),
    _WlsxStackProtoIfStatRouteUpdateTx_Type()
)
wlsxStackProtoIfStatRouteUpdateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatRouteUpdateTx.setStatus("current")
_WlsxStackProtoIfStatRouteUpdateRx_Type = Counter64
_WlsxStackProtoIfStatRouteUpdateRx_Object = MibTableColumn
wlsxStackProtoIfStatRouteUpdateRx = _WlsxStackProtoIfStatRouteUpdateRx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 2, 1, 1, 11),
    _WlsxStackProtoIfStatRouteUpdateRx_Type()
)
wlsxStackProtoIfStatRouteUpdateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackProtoIfStatRouteUpdateRx.setStatus("current")
_WlsxStackTopo_ObjectIdentity = ObjectIdentity
wlsxStackTopo = _WlsxStackTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 3)
)
_WlsxStackTopoTable_Object = MibTable
wlsxStackTopoTable = _WlsxStackTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wlsxStackTopoTable.setStatus("current")
_WlsxStackTopoEntry_Object = MibTableRow
wlsxStackTopoEntry = _WlsxStackTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 3, 1, 1)
)
wlsxStackTopoEntry.setIndexNames(
    (0, "WLSX-STACK-MIB", "wlsxStackMemberId"),
    (0, "WLSX-STACK-MIB", "wlsxStackProtoIfName"),
)
if mibBuilder.loadTexts:
    wlsxStackTopoEntry.setStatus("current")
_WlsxStackTopoNeighborSlot_Type = Integer32
_WlsxStackTopoNeighborSlot_Object = MibTableColumn
wlsxStackTopoNeighborSlot = _WlsxStackTopoNeighborSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 3, 1, 1, 1),
    _WlsxStackTopoNeighborSlot_Type()
)
wlsxStackTopoNeighborSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackTopoNeighborSlot.setStatus("current")
_WlsxStackTopoNeighborIfName_Type = SnmpAdminString
_WlsxStackTopoNeighborIfName_Object = MibTableColumn
wlsxStackTopoNeighborIfName = _WlsxStackTopoNeighborIfName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 3, 1, 1, 2),
    _WlsxStackTopoNeighborIfName_Type()
)
wlsxStackTopoNeighborIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackTopoNeighborIfName.setStatus("current")


class _WlsxStackNeighborState_Type(Integer32):
    """Custom type wlsxStackNeighborState based on Integer32"""
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
        *(("unknown", 1),
          ("initializing", 2),
          ("up", 3),
          ("failed", 4),
          ("down", 5))
    )


_WlsxStackNeighborState_Type.__name__ = "Integer32"
_WlsxStackNeighborState_Object = MibTableColumn
wlsxStackNeighborState = _WlsxStackNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 1, 3, 1, 1, 3),
    _WlsxStackNeighborState_Type()
)
wlsxStackNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxStackNeighborState.setStatus("current")
_WlsxStackMIBConformance_ObjectIdentity = ObjectIdentity
wlsxStackMIBConformance = _WlsxStackMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 2)
)
if mibBuilder.loadTexts:
    wlsxStackMIBConformance.setStatus("current")
_WlsxStackMIBGroups_ObjectIdentity = ObjectIdentity
wlsxStackMIBGroups = _WlsxStackMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    wlsxStackMIBGroups.setStatus("current")
_WlsxStackMIBCompliances_ObjectIdentity = ObjectIdentity
wlsxStackMIBCompliances = _WlsxStackMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 2, 2)
)
if mibBuilder.loadTexts:
    wlsxStackMIBCompliances.setStatus("current")

# Managed Objects groups

wlsxStackChasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 2, 1, 1)
)
wlsxStackChasGroup.setObjects(
      *(("WLSX-STACK-MIB", "wlsxStackMemberState"),
        ("WLSX-STACK-MIB", "wlsxStackMemberMacAddr"),
        ("WLSX-STACK-MIB", "wlsxStackMemberPriority"),
        ("WLSX-STACK-MIB", "wlsxStackMemberHostName"),
        ("WLSX-STACK-MIB", "wlsxStackMemberSysLocation"),
        ("WLSX-STACK-MIB", "wlsxStackMemberChangeDetectSeqNum"),
        ("WLSX-STACK-MIB", "wlsxStackMemberSysUpTime"),
        ("WLSX-STACK-MIB", "wlsxStackMemberModelName"),
        ("WLSX-STACK-MIB", "wlsxStackMemberSWVersion"))
)
if mibBuilder.loadTexts:
    wlsxStackChasGroup.setStatus("current")

wlsxStackTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 2, 1, 2)
)
wlsxStackTopologyGroup.setObjects(
      *(("WLSX-STACK-MIB", "wlsxStackTopoNeighborSlot"),
        ("WLSX-STACK-MIB", "wlsxStackTopoNeighborIfName"))
)
if mibBuilder.loadTexts:
    wlsxStackTopologyGroup.setStatus("current")

wlsxStackProtoIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 2, 1, 3)
)
wlsxStackProtoIfGroup.setObjects(
      *(("WLSX-STACK-MIB", "wlsxStackProtoIfName"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfNeighborState"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatTxPkt"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatRxPkt"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatTxErr"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatNeighborTransDown"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatNeighborTransUp"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatKeepAliveTx"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatKeepAliveRx"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatRouteUpdateTx"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfStatRouteUpdateRx"))
)
if mibBuilder.loadTexts:
    wlsxStackProtoIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wlsxStackMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 19, 2, 2, 1)
)
wlsxStackMIBCompliance.setObjects(
      *(("WLSX-STACK-MIB", "wlsxStackChasGroup"),
        ("WLSX-STACK-MIB", "wlsxStackTopologyGroup"),
        ("WLSX-STACK-MIB", "wlsxStackProtoIfGroup"))
)
if mibBuilder.loadTexts:
    wlsxStackMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-STACK-MIB",
    **{"wlsxStackMIB": wlsxStackMIB,
       "wlsxStackMIBObjects": wlsxStackMIBObjects,
       "wlsxStackMember": wlsxStackMember,
       "wlsxStackMemberTable": wlsxStackMemberTable,
       "wlsxStackMemberEntry": wlsxStackMemberEntry,
       "wlsxStackMemberId": wlsxStackMemberId,
       "wlsxStackMemberState": wlsxStackMemberState,
       "wlsxStackMemberMacAddr": wlsxStackMemberMacAddr,
       "wlsxStackMemberPriority": wlsxStackMemberPriority,
       "wlsxStackMemberHostName": wlsxStackMemberHostName,
       "wlsxStackMemberSysLocation": wlsxStackMemberSysLocation,
       "wlsxStackMemberChangeDetectSeqNum": wlsxStackMemberChangeDetectSeqNum,
       "wlsxStackMemberSysUpTime": wlsxStackMemberSysUpTime,
       "wlsxStackMemberModelName": wlsxStackMemberModelName,
       "wlsxStackMemberSWVersion": wlsxStackMemberSWVersion,
       "wlsxStackProtoIf": wlsxStackProtoIf,
       "wlsxStackProtoIfTable": wlsxStackProtoIfTable,
       "wlsxStackProtoIfEntry": wlsxStackProtoIfEntry,
       "wlsxStackProtoIfName": wlsxStackProtoIfName,
       "wlsxStackProtoIfNeighborState": wlsxStackProtoIfNeighborState,
       "wlsxStackProtoIfStatTxPkt": wlsxStackProtoIfStatTxPkt,
       "wlsxStackProtoIfStatRxPkt": wlsxStackProtoIfStatRxPkt,
       "wlsxStackProtoIfStatTxErr": wlsxStackProtoIfStatTxErr,
       "wlsxStackProtoIfStatNeighborTransDown": wlsxStackProtoIfStatNeighborTransDown,
       "wlsxStackProtoIfStatNeighborTransUp": wlsxStackProtoIfStatNeighborTransUp,
       "wlsxStackProtoIfStatKeepAliveTx": wlsxStackProtoIfStatKeepAliveTx,
       "wlsxStackProtoIfStatKeepAliveRx": wlsxStackProtoIfStatKeepAliveRx,
       "wlsxStackProtoIfStatRouteUpdateTx": wlsxStackProtoIfStatRouteUpdateTx,
       "wlsxStackProtoIfStatRouteUpdateRx": wlsxStackProtoIfStatRouteUpdateRx,
       "wlsxStackTopo": wlsxStackTopo,
       "wlsxStackTopoTable": wlsxStackTopoTable,
       "wlsxStackTopoEntry": wlsxStackTopoEntry,
       "wlsxStackTopoNeighborSlot": wlsxStackTopoNeighborSlot,
       "wlsxStackTopoNeighborIfName": wlsxStackTopoNeighborIfName,
       "wlsxStackNeighborState": wlsxStackNeighborState,
       "wlsxStackMIBConformance": wlsxStackMIBConformance,
       "wlsxStackMIBGroups": wlsxStackMIBGroups,
       "wlsxStackChasGroup": wlsxStackChasGroup,
       "wlsxStackTopologyGroup": wlsxStackTopologyGroup,
       "wlsxStackProtoIfGroup": wlsxStackProtoIfGroup,
       "wlsxStackMIBCompliances": wlsxStackMIBCompliances,
       "wlsxStackMIBCompliance": wlsxStackMIBCompliance}
)
