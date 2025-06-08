# SNMP MIB module (FOUNDRY-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FOUNDRY-LAG-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:48 2025
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

(snSwitch,
 snTraps) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snSwitch",
    "snTraps")

(PhysAddress,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "PhysAddress")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fdryLinkAggregationGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33)
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupMIB.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdryLinkAggregationGroupNotifyObjects_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupNotifyObjects = _FdryLinkAggregationGroupNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 0)
)


class _FdryLAGName_Type(DisplayString):
    """Custom type fdryLAGName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FdryLAGName_Type.__name__ = "DisplayString"
_FdryLAGName_Object = MibScalar
fdryLAGName = _FdryLAGName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 0, 1),
    _FdryLAGName_Type()
)
fdryLAGName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fdryLAGName.setStatus("current")
_FdryLinkAggregationGroupTableObjects_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupTableObjects = _FdryLinkAggregationGroupTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1)
)
_FdryLinkAggregationGroupTable_Object = MibTable
fdryLinkAggregationGroupTable = _FdryLinkAggregationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1)
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupTable.setStatus("current")
_FdryLinkAggregationGroupEntry_Object = MibTableRow
fdryLinkAggregationGroupEntry = _FdryLinkAggregationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1)
)
fdryLinkAggregationGroupEntry.setIndexNames(
    (0, "FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupName"),
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupEntry.setStatus("current")


class _FdryLinkAggregationGroupName_Type(DisplayString):
    """Custom type fdryLinkAggregationGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FdryLinkAggregationGroupName_Type.__name__ = "DisplayString"
_FdryLinkAggregationGroupName_Object = MibTableColumn
fdryLinkAggregationGroupName = _FdryLinkAggregationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 1),
    _FdryLinkAggregationGroupName_Type()
)
fdryLinkAggregationGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupName.setStatus("current")


class _FdryLinkAggregationGroupType_Type(Integer32):
    """Custom type fdryLinkAggregationGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("keepalive", 3))
    )


_FdryLinkAggregationGroupType_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupType_Object = MibTableColumn
fdryLinkAggregationGroupType = _FdryLinkAggregationGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 2),
    _FdryLinkAggregationGroupType_Type()
)
fdryLinkAggregationGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupType.setStatus("current")


class _FdryLinkAggregationGroupAdminStatus_Type(Integer32):
    """Custom type fdryLinkAggregationGroupAdminStatus based on Integer32"""
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
        *(("deploy", 1),
          ("deployPassive", 2),
          ("undeploy", 3),
          ("undeployForced", 4))
    )


_FdryLinkAggregationGroupAdminStatus_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupAdminStatus_Object = MibTableColumn
fdryLinkAggregationGroupAdminStatus = _FdryLinkAggregationGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 3),
    _FdryLinkAggregationGroupAdminStatus_Type()
)
fdryLinkAggregationGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupAdminStatus.setStatus("current")
_FdryLinkAggregationGroupIfList_Type = OctetString
_FdryLinkAggregationGroupIfList_Object = MibTableColumn
fdryLinkAggregationGroupIfList = _FdryLinkAggregationGroupIfList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 4),
    _FdryLinkAggregationGroupIfList_Type()
)
fdryLinkAggregationGroupIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupIfList.setStatus("current")
_FdryLinkAggregationGroupPrimaryPort_Type = InterfaceIndexOrZero
_FdryLinkAggregationGroupPrimaryPort_Object = MibTableColumn
fdryLinkAggregationGroupPrimaryPort = _FdryLinkAggregationGroupPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 5),
    _FdryLinkAggregationGroupPrimaryPort_Type()
)
fdryLinkAggregationGroupPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPrimaryPort.setStatus("current")


class _FdryLinkAggregationGroupTrunkType_Type(Integer32):
    """Custom type fdryLinkAggregationGroupTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hashBased", 1),
          ("perPacket", 2))
    )


_FdryLinkAggregationGroupTrunkType_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupTrunkType_Object = MibTableColumn
fdryLinkAggregationGroupTrunkType = _FdryLinkAggregationGroupTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 6),
    _FdryLinkAggregationGroupTrunkType_Type()
)
fdryLinkAggregationGroupTrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupTrunkType.setStatus("current")
_FdryLinkAggregationGroupTrunkThreshold_Type = Unsigned32
_FdryLinkAggregationGroupTrunkThreshold_Object = MibTableColumn
fdryLinkAggregationGroupTrunkThreshold = _FdryLinkAggregationGroupTrunkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 7),
    _FdryLinkAggregationGroupTrunkThreshold_Type()
)
fdryLinkAggregationGroupTrunkThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupTrunkThreshold.setStatus("current")


class _FdryLinkAggregationGroupLacpTimeout_Type(Integer32):
    """Custom type fdryLinkAggregationGroupLacpTimeout based on Integer32"""
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
          ("long", 2),
          ("short", 3))
    )


_FdryLinkAggregationGroupLacpTimeout_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupLacpTimeout_Object = MibTableColumn
fdryLinkAggregationGroupLacpTimeout = _FdryLinkAggregationGroupLacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 8),
    _FdryLinkAggregationGroupLacpTimeout_Type()
)
fdryLinkAggregationGroupLacpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpTimeout.setStatus("current")
_FdryLinkAggregationGroupIfIndex_Type = InterfaceIndexOrZero
_FdryLinkAggregationGroupIfIndex_Object = MibTableColumn
fdryLinkAggregationGroupIfIndex = _FdryLinkAggregationGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 9),
    _FdryLinkAggregationGroupIfIndex_Type()
)
fdryLinkAggregationGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupIfIndex.setStatus("current")
_FdryLinkAggregationGroupPortCount_Type = Unsigned32
_FdryLinkAggregationGroupPortCount_Object = MibTableColumn
fdryLinkAggregationGroupPortCount = _FdryLinkAggregationGroupPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 10),
    _FdryLinkAggregationGroupPortCount_Type()
)
fdryLinkAggregationGroupPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortCount.setStatus("current")
_FdryLinkAggregationGroupRowStatus_Type = RowStatus
_FdryLinkAggregationGroupRowStatus_Object = MibTableColumn
fdryLinkAggregationGroupRowStatus = _FdryLinkAggregationGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 11),
    _FdryLinkAggregationGroupRowStatus_Type()
)
fdryLinkAggregationGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupRowStatus.setStatus("current")
_FdryLinkAggregationGroupId_Type = Unsigned32
_FdryLinkAggregationGroupId_Object = MibTableColumn
fdryLinkAggregationGroupId = _FdryLinkAggregationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 12),
    _FdryLinkAggregationGroupId_Type()
)
fdryLinkAggregationGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupId.setStatus("current")
_FdryLinkAggregationGroupPortTableObjects_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupPortTableObjects = _FdryLinkAggregationGroupPortTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2)
)
_FdryLinkAggregationGroupPortTable_Object = MibTable
fdryLinkAggregationGroupPortTable = _FdryLinkAggregationGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1)
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortTable.setStatus("current")
_FdryLinkAggregationGroupPortEntry_Object = MibTableRow
fdryLinkAggregationGroupPortEntry = _FdryLinkAggregationGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1, 1)
)
fdryLinkAggregationGroupPortEntry.setIndexNames(
    (0, "FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortEntry.setStatus("current")


class _FdryLinkAggregationGroupPortLacpPriority_Type(Integer32):
    """Custom type fdryLinkAggregationGroupPortLacpPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryLinkAggregationGroupPortLacpPriority_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupPortLacpPriority_Object = MibTableColumn
fdryLinkAggregationGroupPortLacpPriority = _FdryLinkAggregationGroupPortLacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1, 1, 1),
    _FdryLinkAggregationGroupPortLacpPriority_Type()
)
fdryLinkAggregationGroupPortLacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortLacpPriority.setStatus("current")
_FdryLinkAggregationGroupLacpPortTableObjects_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupLacpPortTableObjects = _FdryLinkAggregationGroupLacpPortTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3)
)
_FdryLinkAggregationGroupLacpPortTable_Object = MibTable
fdryLinkAggregationGroupLacpPortTable = _FdryLinkAggregationGroupLacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1)
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortTable.setStatus("current")
_FdryLinkAggregationGroupLacpPortEntry_Object = MibTableRow
fdryLinkAggregationGroupLacpPortEntry = _FdryLinkAggregationGroupLacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1)
)
fdryLinkAggregationGroupLacpPortEntry.setIndexNames(
    (0, "FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortEntry.setStatus("current")


class _FdryLinkAggregationGroupLacpPortAdminStatus_Type(Integer32):
    """Custom type fdryLinkAggregationGroupLacpPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_FdryLinkAggregationGroupLacpPortAdminStatus_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupLacpPortAdminStatus_Object = MibTableColumn
fdryLinkAggregationGroupLacpPortAdminStatus = _FdryLinkAggregationGroupLacpPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1, 1),
    _FdryLinkAggregationGroupLacpPortAdminStatus_Type()
)
fdryLinkAggregationGroupLacpPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortAdminStatus.setStatus("current")


class _FdryLinkAggregationGroupLacpPortLinkStatus_Type(Integer32):
    """Custom type fdryLinkAggregationGroupLacpPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_FdryLinkAggregationGroupLacpPortLinkStatus_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupLacpPortLinkStatus_Object = MibTableColumn
fdryLinkAggregationGroupLacpPortLinkStatus = _FdryLinkAggregationGroupLacpPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1, 2),
    _FdryLinkAggregationGroupLacpPortLinkStatus_Type()
)
fdryLinkAggregationGroupLacpPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortLinkStatus.setStatus("current")


class _FdryLinkAggregationGroupLacpPortLacpStatus_Type(Integer32):
    """Custom type fdryLinkAggregationGroupLacpPortLacpStatus based on Integer32"""
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
        *(("operation", 1),
          ("down", 2),
          ("blocked", 3),
          ("inactive", 4),
          ("pexforceup", 5))
    )


_FdryLinkAggregationGroupLacpPortLacpStatus_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupLacpPortLacpStatus_Object = MibTableColumn
fdryLinkAggregationGroupLacpPortLacpStatus = _FdryLinkAggregationGroupLacpPortLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1, 3),
    _FdryLinkAggregationGroupLacpPortLacpStatus_Type()
)
fdryLinkAggregationGroupLacpPortLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortLacpStatus.setStatus("current")
_FdryLinkAggregationGroupLacpPortLacpSysID_Type = PhysAddress
_FdryLinkAggregationGroupLacpPortLacpSysID_Object = MibTableColumn
fdryLinkAggregationGroupLacpPortLacpSysID = _FdryLinkAggregationGroupLacpPortLacpSysID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1, 4),
    _FdryLinkAggregationGroupLacpPortLacpSysID_Type()
)
fdryLinkAggregationGroupLacpPortLacpSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortLacpSysID.setStatus("current")
_FdryLinkAggregationGroupLacpPortLacpKey_Type = Integer32
_FdryLinkAggregationGroupLacpPortLacpKey_Object = MibTableColumn
fdryLinkAggregationGroupLacpPortLacpKey = _FdryLinkAggregationGroupLacpPortLacpKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1, 5),
    _FdryLinkAggregationGroupLacpPortLacpKey_Type()
)
fdryLinkAggregationGroupLacpPortLacpKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortLacpKey.setStatus("current")
_FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Type = PhysAddress
_FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Object = MibTableColumn
fdryLinkAggregationGroupLacpPortLacpRemoteSysID = _FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1, 6),
    _FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Type()
)
fdryLinkAggregationGroupLacpPortLacpRemoteSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortLacpRemoteSysID.setStatus("current")
_FdryLinkAggregationGroupLacpPortLacpRemoteKey_Type = Integer32
_FdryLinkAggregationGroupLacpPortLacpRemoteKey_Object = MibTableColumn
fdryLinkAggregationGroupLacpPortLacpRemoteKey = _FdryLinkAggregationGroupLacpPortLacpRemoteKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 3, 1, 1, 7),
    _FdryLinkAggregationGroupLacpPortLacpRemoteKey_Type()
)
fdryLinkAggregationGroupLacpPortLacpRemoteKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpPortLacpRemoteKey.setStatus("current")

# Managed Objects groups


# Notification objects

fdryTrapLagDeployed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1204)
)
fdryTrapLagDeployed.setObjects(
      *(("FOUNDRY-LAG-MIB", "fdryLAGName"),
        ("FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupIfIndex"))
)
if mibBuilder.loadTexts:
    fdryTrapLagDeployed.setStatus(
        "current"
    )

fdryTrapLagUndeployed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1205)
)
fdryTrapLagUndeployed.setObjects(
      *(("FOUNDRY-LAG-MIB", "fdryLAGName"),
        ("FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupIfIndex"))
)
if mibBuilder.loadTexts:
    fdryTrapLagUndeployed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-LAG-MIB",
    **{"fdryTrapLagDeployed": fdryTrapLagDeployed,
       "fdryTrapLagUndeployed": fdryTrapLagUndeployed,
       "fdryLinkAggregationGroupMIB": fdryLinkAggregationGroupMIB,
       "fdryLinkAggregationGroupNotifyObjects": fdryLinkAggregationGroupNotifyObjects,
       "fdryLAGName": fdryLAGName,
       "fdryLinkAggregationGroupTableObjects": fdryLinkAggregationGroupTableObjects,
       "fdryLinkAggregationGroupTable": fdryLinkAggregationGroupTable,
       "fdryLinkAggregationGroupEntry": fdryLinkAggregationGroupEntry,
       "fdryLinkAggregationGroupName": fdryLinkAggregationGroupName,
       "fdryLinkAggregationGroupType": fdryLinkAggregationGroupType,
       "fdryLinkAggregationGroupAdminStatus": fdryLinkAggregationGroupAdminStatus,
       "fdryLinkAggregationGroupIfList": fdryLinkAggregationGroupIfList,
       "fdryLinkAggregationGroupPrimaryPort": fdryLinkAggregationGroupPrimaryPort,
       "fdryLinkAggregationGroupTrunkType": fdryLinkAggregationGroupTrunkType,
       "fdryLinkAggregationGroupTrunkThreshold": fdryLinkAggregationGroupTrunkThreshold,
       "fdryLinkAggregationGroupLacpTimeout": fdryLinkAggregationGroupLacpTimeout,
       "fdryLinkAggregationGroupIfIndex": fdryLinkAggregationGroupIfIndex,
       "fdryLinkAggregationGroupPortCount": fdryLinkAggregationGroupPortCount,
       "fdryLinkAggregationGroupRowStatus": fdryLinkAggregationGroupRowStatus,
       "fdryLinkAggregationGroupId": fdryLinkAggregationGroupId,
       "fdryLinkAggregationGroupPortTableObjects": fdryLinkAggregationGroupPortTableObjects,
       "fdryLinkAggregationGroupPortTable": fdryLinkAggregationGroupPortTable,
       "fdryLinkAggregationGroupPortEntry": fdryLinkAggregationGroupPortEntry,
       "fdryLinkAggregationGroupPortLacpPriority": fdryLinkAggregationGroupPortLacpPriority,
       "fdryLinkAggregationGroupLacpPortTableObjects": fdryLinkAggregationGroupLacpPortTableObjects,
       "fdryLinkAggregationGroupLacpPortTable": fdryLinkAggregationGroupLacpPortTable,
       "fdryLinkAggregationGroupLacpPortEntry": fdryLinkAggregationGroupLacpPortEntry,
       "fdryLinkAggregationGroupLacpPortAdminStatus": fdryLinkAggregationGroupLacpPortAdminStatus,
       "fdryLinkAggregationGroupLacpPortLinkStatus": fdryLinkAggregationGroupLacpPortLinkStatus,
       "fdryLinkAggregationGroupLacpPortLacpStatus": fdryLinkAggregationGroupLacpPortLacpStatus,
       "fdryLinkAggregationGroupLacpPortLacpSysID": fdryLinkAggregationGroupLacpPortLacpSysID,
       "fdryLinkAggregationGroupLacpPortLacpKey": fdryLinkAggregationGroupLacpPortLacpKey,
       "fdryLinkAggregationGroupLacpPortLacpRemoteSysID": fdryLinkAggregationGroupLacpPortLacpRemoteSysID,
       "fdryLinkAggregationGroupLacpPortLacpRemoteKey": fdryLinkAggregationGroupLacpPortLacpRemoteKey}
)
