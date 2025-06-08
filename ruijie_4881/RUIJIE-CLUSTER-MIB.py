# SNMP MIB module (RUIJIE-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CLUSTER-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:45 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ruijieClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31)
)
if mibBuilder.loadTexts:
    ruijieClusterMIB.setRevisions(
        ("2012-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieClusterMIBObjects_ObjectIdentity = ObjectIdentity
ruijieClusterMIBObjects = _RuijieClusterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1)
)


class _RuijieClusterName_Type(DisplayString):
    """Custom type ruijieClusterName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RuijieClusterName_Type.__name__ = "DisplayString"
_RuijieClusterName_Object = MibScalar
ruijieClusterName = _RuijieClusterName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 1),
    _RuijieClusterName_Type()
)
ruijieClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterName.setStatus("current")


class _RuijieClusterStatus_Type(EnabledStatus):
    """Custom type ruijieClusterStatus based on EnabledStatus"""
    defaultValue = 1


_RuijieClusterStatus_Type.__name__ = "EnabledStatus"
_RuijieClusterStatus_Object = MibScalar
ruijieClusterStatus = _RuijieClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 2),
    _RuijieClusterStatus_Type()
)
ruijieClusterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterStatus.setStatus("current")
_RuijieClusterCmdMacAddress_Type = MacAddress
_RuijieClusterCmdMacAddress_Object = MibScalar
ruijieClusterCmdMacAddress = _RuijieClusterCmdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 3),
    _RuijieClusterCmdMacAddress_Type()
)
ruijieClusterCmdMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCmdMacAddress.setStatus("current")
_RuijieClusterCmdName_Type = DisplayString
_RuijieClusterCmdName_Object = MibScalar
ruijieClusterCmdName = _RuijieClusterCmdName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 4),
    _RuijieClusterCmdName_Type()
)
ruijieClusterCmdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCmdName.setStatus("current")


class _RuijieClusterVlan_Type(Integer32):
    """Custom type ruijieClusterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RuijieClusterVlan_Type.__name__ = "Integer32"
_RuijieClusterVlan_Object = MibScalar
ruijieClusterVlan = _RuijieClusterVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 5),
    _RuijieClusterVlan_Type()
)
ruijieClusterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterVlan.setStatus("current")


class _RuijieClusterHopsLimit_Type(Integer32):
    """Custom type ruijieClusterHopsLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RuijieClusterHopsLimit_Type.__name__ = "Integer32"
_RuijieClusterHopsLimit_Object = MibScalar
ruijieClusterHopsLimit = _RuijieClusterHopsLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 6),
    _RuijieClusterHopsLimit_Type()
)
ruijieClusterHopsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterHopsLimit.setStatus("current")


class _RuijieClusterTimerTopo_Type(Integer32):
    """Custom type ruijieClusterTimerTopo based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_RuijieClusterTimerTopo_Type.__name__ = "Integer32"
_RuijieClusterTimerTopo_Object = MibScalar
ruijieClusterTimerTopo = _RuijieClusterTimerTopo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 7),
    _RuijieClusterTimerTopo_Type()
)
ruijieClusterTimerTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterTimerTopo.setStatus("current")


class _RuijieClusterTimerHello_Type(Integer32):
    """Custom type ruijieClusterTimerHello based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_RuijieClusterTimerHello_Type.__name__ = "Integer32"
_RuijieClusterTimerHello_Object = MibScalar
ruijieClusterTimerHello = _RuijieClusterTimerHello_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 8),
    _RuijieClusterTimerHello_Type()
)
ruijieClusterTimerHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterTimerHello.setStatus("current")


class _RuijieClusterTimerHold_Type(Integer32):
    """Custom type ruijieClusterTimerHold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_RuijieClusterTimerHold_Type.__name__ = "Integer32"
_RuijieClusterTimerHold_Object = MibScalar
ruijieClusterTimerHold = _RuijieClusterTimerHold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 9),
    _RuijieClusterTimerHold_Type()
)
ruijieClusterTimerHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterTimerHold.setStatus("current")
_RuijieClusterTftpServer_Type = IpAddress
_RuijieClusterTftpServer_Object = MibScalar
ruijieClusterTftpServer = _RuijieClusterTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 10),
    _RuijieClusterTftpServer_Type()
)
ruijieClusterTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterTftpServer.setStatus("current")


class _RuijieClusterNumberOfMembers_Type(Integer32):
    """Custom type ruijieClusterNumberOfMembers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_RuijieClusterNumberOfMembers_Type.__name__ = "Integer32"
_RuijieClusterNumberOfMembers_Object = MibScalar
ruijieClusterNumberOfMembers = _RuijieClusterNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 11),
    _RuijieClusterNumberOfMembers_Type()
)
ruijieClusterNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterNumberOfMembers.setStatus("current")


class _RuijieClusterMaxNumberOfMembers_Type(Integer32):
    """Custom type ruijieClusterMaxNumberOfMembers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_RuijieClusterMaxNumberOfMembers_Type.__name__ = "Integer32"
_RuijieClusterMaxNumberOfMembers_Object = MibScalar
ruijieClusterMaxNumberOfMembers = _RuijieClusterMaxNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 12),
    _RuijieClusterMaxNumberOfMembers_Type()
)
ruijieClusterMaxNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMaxNumberOfMembers.setStatus("current")


class _RuijieClusterDevMaxCapicity_Type(Unsigned32):
    """Custom type ruijieClusterDevMaxCapicity based on Unsigned32"""
    defaultValue = 0


_RuijieClusterDevMaxCapicity_Type.__name__ = "Unsigned32"
_RuijieClusterDevMaxCapicity_Object = MibScalar
ruijieClusterDevMaxCapicity = _RuijieClusterDevMaxCapicity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 13),
    _RuijieClusterDevMaxCapicity_Type()
)
ruijieClusterDevMaxCapicity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterDevMaxCapicity.setStatus("current")


class _RuijieClusterAutoAdd_Type(Integer32):
    """Custom type ruijieClusterAutoAdd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable-with-def", 0),
          ("enable", 1),
          ("disabled-with-static", 2),
          ("disabled-with-del", 3))
    )


_RuijieClusterAutoAdd_Type.__name__ = "Integer32"
_RuijieClusterAutoAdd_Object = MibScalar
ruijieClusterAutoAdd = _RuijieClusterAutoAdd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 14),
    _RuijieClusterAutoAdd_Type()
)
ruijieClusterAutoAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterAutoAdd.setStatus("current")


class _RuijieClusterExplore_Type(EnabledStatus):
    """Custom type ruijieClusterExplore based on EnabledStatus"""
    defaultValue = 2


_RuijieClusterExplore_Type.__name__ = "EnabledStatus"
_RuijieClusterExplore_Object = MibScalar
ruijieClusterExplore = _RuijieClusterExplore_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 15),
    _RuijieClusterExplore_Type()
)
ruijieClusterExplore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterExplore.setStatus("current")
_RuijieClusterSpecifyAdmin_ObjectIdentity = ObjectIdentity
ruijieClusterSpecifyAdmin = _RuijieClusterSpecifyAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 16)
)
_RuijieClusterSpecifyAdminAddress_Type = MacAddress
_RuijieClusterSpecifyAdminAddress_Object = MibScalar
ruijieClusterSpecifyAdminAddress = _RuijieClusterSpecifyAdminAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 16, 1),
    _RuijieClusterSpecifyAdminAddress_Type()
)
ruijieClusterSpecifyAdminAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterSpecifyAdminAddress.setStatus("current")


class _RuijieClusterSpecifyAdminName_Type(DisplayString):
    """Custom type ruijieClusterSpecifyAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RuijieClusterSpecifyAdminName_Type.__name__ = "DisplayString"
_RuijieClusterSpecifyAdminName_Object = MibScalar
ruijieClusterSpecifyAdminName = _RuijieClusterSpecifyAdminName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 16, 2),
    _RuijieClusterSpecifyAdminName_Type()
)
ruijieClusterSpecifyAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterSpecifyAdminName.setStatus("current")
_RuijieClusterDeviceInfo_ObjectIdentity = ObjectIdentity
ruijieClusterDeviceInfo = _RuijieClusterDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 17)
)


class _RuijieClusterDeviceEnable_Type(EnabledStatus):
    """Custom type ruijieClusterDeviceEnable based on EnabledStatus"""
    defaultValue = 1


_RuijieClusterDeviceEnable_Type.__name__ = "EnabledStatus"
_RuijieClusterDeviceEnable_Object = MibScalar
ruijieClusterDeviceEnable = _RuijieClusterDeviceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 17, 1),
    _RuijieClusterDeviceEnable_Type()
)
ruijieClusterDeviceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterDeviceEnable.setStatus("current")


class _RuijieClusterDeviceRole_Type(Integer32):
    """Custom type ruijieClusterDeviceRole based on Integer32"""
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
        *(("candidateDevice", 1),
          ("managerDevice", 2),
          ("memberDevice", 3))
    )


_RuijieClusterDeviceRole_Type.__name__ = "Integer32"
_RuijieClusterDeviceRole_Object = MibScalar
ruijieClusterDeviceRole = _RuijieClusterDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 17, 2),
    _RuijieClusterDeviceRole_Type()
)
ruijieClusterDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterDeviceRole.setStatus("current")
_RuijieClusterDeviceIP_Type = IpAddress
_RuijieClusterDeviceIP_Object = MibScalar
ruijieClusterDeviceIP = _RuijieClusterDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 17, 3),
    _RuijieClusterDeviceIP_Type()
)
ruijieClusterDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterDeviceIP.setStatus("current")


class _RuijieClusterDeviceSn_Type(Integer32):
    """Custom type ruijieClusterDeviceSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_RuijieClusterDeviceSn_Type.__name__ = "Integer32"
_RuijieClusterDeviceSn_Object = MibScalar
ruijieClusterDeviceSn = _RuijieClusterDeviceSn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 17, 4),
    _RuijieClusterDeviceSn_Type()
)
ruijieClusterDeviceSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterDeviceSn.setStatus("current")
_RuijieClusterIpPoolTable_Object = MibTable
ruijieClusterIpPoolTable = _RuijieClusterIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 18)
)
if mibBuilder.loadTexts:
    ruijieClusterIpPoolTable.setStatus("current")
_RuijieClusterIpPoolEntry_Object = MibTableRow
ruijieClusterIpPoolEntry = _RuijieClusterIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 18, 1)
)
ruijieClusterIpPoolEntry.setIndexNames(
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterIpPool"),
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterIpMask"),
)
if mibBuilder.loadTexts:
    ruijieClusterIpPoolEntry.setStatus("current")
_RuijieClusterIpPool_Type = IpAddress
_RuijieClusterIpPool_Object = MibTableColumn
ruijieClusterIpPool = _RuijieClusterIpPool_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 18, 1, 1),
    _RuijieClusterIpPool_Type()
)
ruijieClusterIpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterIpPool.setStatus("current")
_RuijieClusterIpMask_Type = IpAddress
_RuijieClusterIpMask_Object = MibTableColumn
ruijieClusterIpMask = _RuijieClusterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 18, 1, 2),
    _RuijieClusterIpMask_Type()
)
ruijieClusterIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterIpMask.setStatus("current")
_RuijieClusterIpPoolRowStatus_Type = RowStatus
_RuijieClusterIpPoolRowStatus_Object = MibTableColumn
ruijieClusterIpPoolRowStatus = _RuijieClusterIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 18, 1, 3),
    _RuijieClusterIpPoolRowStatus_Type()
)
ruijieClusterIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterIpPoolRowStatus.setStatus("current")
_RuijieClusterMemberAddTable_Object = MibTable
ruijieClusterMemberAddTable = _RuijieClusterMemberAddTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 19)
)
if mibBuilder.loadTexts:
    ruijieClusterMemberAddTable.setStatus("current")
_RuijieClusterMemberAddEntry_Object = MibTableRow
ruijieClusterMemberAddEntry = _RuijieClusterMemberAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 19, 1)
)
ruijieClusterMemberAddEntry.setIndexNames(
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterMemberAddSn"),
)
if mibBuilder.loadTexts:
    ruijieClusterMemberAddEntry.setStatus("current")


class _RuijieClusterMemberAddSn_Type(Integer32):
    """Custom type ruijieClusterMemberAddSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_RuijieClusterMemberAddSn_Type.__name__ = "Integer32"
_RuijieClusterMemberAddSn_Object = MibTableColumn
ruijieClusterMemberAddSn = _RuijieClusterMemberAddSn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 19, 1, 1),
    _RuijieClusterMemberAddSn_Type()
)
ruijieClusterMemberAddSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberAddSn.setStatus("current")
_RuijieClusterMemberAddMacAddress_Type = MacAddress
_RuijieClusterMemberAddMacAddress_Object = MibTableColumn
ruijieClusterMemberAddMacAddress = _RuijieClusterMemberAddMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 19, 1, 2),
    _RuijieClusterMemberAddMacAddress_Type()
)
ruijieClusterMemberAddMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterMemberAddMacAddress.setStatus("current")
_RuijieClusterMemberAddRowStatus_Type = RowStatus
_RuijieClusterMemberAddRowStatus_Object = MibTableColumn
ruijieClusterMemberAddRowStatus = _RuijieClusterMemberAddRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 19, 1, 3),
    _RuijieClusterMemberAddRowStatus_Type()
)
ruijieClusterMemberAddRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterMemberAddRowStatus.setStatus("current")
_RuijieClusterMemberTable_Object = MibTable
ruijieClusterMemberTable = _RuijieClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20)
)
if mibBuilder.loadTexts:
    ruijieClusterMemberTable.setStatus("current")
_RuijieClusterMemberEntry_Object = MibTableRow
ruijieClusterMemberEntry = _RuijieClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1)
)
ruijieClusterMemberEntry.setIndexNames(
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterMemberSn"),
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterMemberUpMAC"),
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterMemberLcIfx"),
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterMemberUpIfx"),
)
if mibBuilder.loadTexts:
    ruijieClusterMemberEntry.setStatus("current")
_RuijieClusterMemberSn_Type = Unsigned32
_RuijieClusterMemberSn_Object = MibTableColumn
ruijieClusterMemberSn = _RuijieClusterMemberSn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 1),
    _RuijieClusterMemberSn_Type()
)
ruijieClusterMemberSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberSn.setStatus("current")
_RuijieClusterMemberUpMAC_Type = MacAddress
_RuijieClusterMemberUpMAC_Object = MibTableColumn
ruijieClusterMemberUpMAC = _RuijieClusterMemberUpMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 2),
    _RuijieClusterMemberUpMAC_Type()
)
ruijieClusterMemberUpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberUpMAC.setStatus("current")
_RuijieClusterMemberLcIfx_Type = Unsigned32
_RuijieClusterMemberLcIfx_Object = MibTableColumn
ruijieClusterMemberLcIfx = _RuijieClusterMemberLcIfx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 3),
    _RuijieClusterMemberLcIfx_Type()
)
ruijieClusterMemberLcIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberLcIfx.setStatus("current")
_RuijieClusterMemberUpIfx_Type = Unsigned32
_RuijieClusterMemberUpIfx_Object = MibTableColumn
ruijieClusterMemberUpIfx = _RuijieClusterMemberUpIfx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 4),
    _RuijieClusterMemberUpIfx_Type()
)
ruijieClusterMemberUpIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberUpIfx.setStatus("current")
_RuijieClusterMemberLcPort_Type = DisplayString
_RuijieClusterMemberLcPort_Object = MibTableColumn
ruijieClusterMemberLcPort = _RuijieClusterMemberLcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 5),
    _RuijieClusterMemberLcPort_Type()
)
ruijieClusterMemberLcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberLcPort.setStatus("current")
_RuijieClusterMemberUpPort_Type = DisplayString
_RuijieClusterMemberUpPort_Object = MibTableColumn
ruijieClusterMemberUpPort = _RuijieClusterMemberUpPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 6),
    _RuijieClusterMemberUpPort_Type()
)
ruijieClusterMemberUpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberUpPort.setStatus("current")
_RuijieClusterMemberMacAddress_Type = MacAddress
_RuijieClusterMemberMacAddress_Object = MibTableColumn
ruijieClusterMemberMacAddress = _RuijieClusterMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 7),
    _RuijieClusterMemberMacAddress_Type()
)
ruijieClusterMemberMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberMacAddress.setStatus("current")
_RuijieClusterMemberName_Type = DisplayString
_RuijieClusterMemberName_Object = MibTableColumn
ruijieClusterMemberName = _RuijieClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 8),
    _RuijieClusterMemberName_Type()
)
ruijieClusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberName.setStatus("current")
_RuijieClusterMemberIp_Type = IpAddress
_RuijieClusterMemberIp_Object = MibTableColumn
ruijieClusterMemberIp = _RuijieClusterMemberIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 9),
    _RuijieClusterMemberIp_Type()
)
ruijieClusterMemberIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberIp.setStatus("current")
_RuijieClusterMemberHops_Type = Unsigned32
_RuijieClusterMemberHops_Object = MibTableColumn
ruijieClusterMemberHops = _RuijieClusterMemberHops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 10),
    _RuijieClusterMemberHops_Type()
)
ruijieClusterMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberHops.setStatus("current")
_RuijieClusterMemberState_Type = DisplayString
_RuijieClusterMemberState_Object = MibTableColumn
ruijieClusterMemberState = _RuijieClusterMemberState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 11),
    _RuijieClusterMemberState_Type()
)
ruijieClusterMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberState.setStatus("current")
_RuijieClusterMemberUpSn_Type = Unsigned32
_RuijieClusterMemberUpSn_Object = MibTableColumn
ruijieClusterMemberUpSn = _RuijieClusterMemberUpSn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 12),
    _RuijieClusterMemberUpSn_Type()
)
ruijieClusterMemberUpSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberUpSn.setStatus("current")
_RuijieClusterMemberLastTopoUpdateTime_Type = Unsigned32
_RuijieClusterMemberLastTopoUpdateTime_Object = MibTableColumn
ruijieClusterMemberLastTopoUpdateTime = _RuijieClusterMemberLastTopoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 13),
    _RuijieClusterMemberLastTopoUpdateTime_Type()
)
ruijieClusterMemberLastTopoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberLastTopoUpdateTime.setStatus("current")
_RuijieClusterMemberLastUdpUpdateTime_Type = Unsigned32
_RuijieClusterMemberLastUdpUpdateTime_Object = MibTableColumn
ruijieClusterMemberLastUdpUpdateTime = _RuijieClusterMemberLastUdpUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 14),
    _RuijieClusterMemberLastUdpUpdateTime_Type()
)
ruijieClusterMemberLastUdpUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberLastUdpUpdateTime.setStatus("current")
_RuijieClusterMemberNoRecvTopoRspCount_Type = Unsigned32
_RuijieClusterMemberNoRecvTopoRspCount_Object = MibTableColumn
ruijieClusterMemberNoRecvTopoRspCount = _RuijieClusterMemberNoRecvTopoRspCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 15),
    _RuijieClusterMemberNoRecvTopoRspCount_Type()
)
ruijieClusterMemberNoRecvTopoRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberNoRecvTopoRspCount.setStatus("current")
_RuijieClusterMemberNoRecvUdpRspCount_Type = Unsigned32
_RuijieClusterMemberNoRecvUdpRspCount_Object = MibTableColumn
ruijieClusterMemberNoRecvUdpRspCount = _RuijieClusterMemberNoRecvUdpRspCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 16),
    _RuijieClusterMemberNoRecvUdpRspCount_Type()
)
ruijieClusterMemberNoRecvUdpRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterMemberNoRecvUdpRspCount.setStatus("current")
_RuijieClusterMemberReload_Type = EnabledStatus
_RuijieClusterMemberReload_Object = MibTableColumn
ruijieClusterMemberReload = _RuijieClusterMemberReload_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 20, 1, 17),
    _RuijieClusterMemberReload_Type()
)
ruijieClusterMemberReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClusterMemberReload.setStatus("current")
_RuijieClusterCandidateTable_Object = MibTable
ruijieClusterCandidateTable = _RuijieClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21)
)
if mibBuilder.loadTexts:
    ruijieClusterCandidateTable.setStatus("current")
_RuijieClusterCandidateEntry_Object = MibTableRow
ruijieClusterCandidateEntry = _RuijieClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1)
)
ruijieClusterCandidateEntry.setIndexNames(
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateMacAddress"),
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateUpMAC"),
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateLcIfx"),
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateUpIfx"),
)
if mibBuilder.loadTexts:
    ruijieClusterCandidateEntry.setStatus("current")
_RuijieClusterCandidateMacAddress_Type = MacAddress
_RuijieClusterCandidateMacAddress_Object = MibTableColumn
ruijieClusterCandidateMacAddress = _RuijieClusterCandidateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 1),
    _RuijieClusterCandidateMacAddress_Type()
)
ruijieClusterCandidateMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateMacAddress.setStatus("current")
_RuijieClusterCandidateUpMAC_Type = MacAddress
_RuijieClusterCandidateUpMAC_Object = MibTableColumn
ruijieClusterCandidateUpMAC = _RuijieClusterCandidateUpMAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 2),
    _RuijieClusterCandidateUpMAC_Type()
)
ruijieClusterCandidateUpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateUpMAC.setStatus("current")
_RuijieClusterCandidateLcIfx_Type = Unsigned32
_RuijieClusterCandidateLcIfx_Object = MibTableColumn
ruijieClusterCandidateLcIfx = _RuijieClusterCandidateLcIfx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 3),
    _RuijieClusterCandidateLcIfx_Type()
)
ruijieClusterCandidateLcIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateLcIfx.setStatus("current")
_RuijieClusterCandidateUpIfx_Type = Unsigned32
_RuijieClusterCandidateUpIfx_Object = MibTableColumn
ruijieClusterCandidateUpIfx = _RuijieClusterCandidateUpIfx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 4),
    _RuijieClusterCandidateUpIfx_Type()
)
ruijieClusterCandidateUpIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateUpIfx.setStatus("current")
_RuijieClusterCandidateLcPort_Type = DisplayString
_RuijieClusterCandidateLcPort_Object = MibTableColumn
ruijieClusterCandidateLcPort = _RuijieClusterCandidateLcPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 5),
    _RuijieClusterCandidateLcPort_Type()
)
ruijieClusterCandidateLcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateLcPort.setStatus("current")
_RuijieClusterCandidateUpPort_Type = DisplayString
_RuijieClusterCandidateUpPort_Object = MibTableColumn
ruijieClusterCandidateUpPort = _RuijieClusterCandidateUpPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 6),
    _RuijieClusterCandidateUpPort_Type()
)
ruijieClusterCandidateUpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateUpPort.setStatus("current")
_RuijieClusterCandidateUpSn_Type = Unsigned32
_RuijieClusterCandidateUpSn_Object = MibTableColumn
ruijieClusterCandidateUpSn = _RuijieClusterCandidateUpSn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 7),
    _RuijieClusterCandidateUpSn_Type()
)
ruijieClusterCandidateUpSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateUpSn.setStatus("current")
_RuijieClusterCandidateHops_Type = Unsigned32
_RuijieClusterCandidateHops_Object = MibTableColumn
ruijieClusterCandidateHops = _RuijieClusterCandidateHops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 8),
    _RuijieClusterCandidateHops_Type()
)
ruijieClusterCandidateHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateHops.setStatus("current")
_RuijieClusterCandidateState_Type = DisplayString
_RuijieClusterCandidateState_Object = MibTableColumn
ruijieClusterCandidateState = _RuijieClusterCandidateState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 21, 1, 9),
    _RuijieClusterCandidateState_Type()
)
ruijieClusterCandidateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterCandidateState.setStatus("current")
_RuijieClusterBlacklistTable_Object = MibTable
ruijieClusterBlacklistTable = _RuijieClusterBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 22)
)
if mibBuilder.loadTexts:
    ruijieClusterBlacklistTable.setStatus("current")
_RuijieClusterBlacklistEntry_Object = MibTableRow
ruijieClusterBlacklistEntry = _RuijieClusterBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 22, 1)
)
ruijieClusterBlacklistEntry.setIndexNames(
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterBlacklistMacAddress"),
)
if mibBuilder.loadTexts:
    ruijieClusterBlacklistEntry.setStatus("current")
_RuijieClusterBlacklistMacAddress_Type = MacAddress
_RuijieClusterBlacklistMacAddress_Object = MibTableColumn
ruijieClusterBlacklistMacAddress = _RuijieClusterBlacklistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 22, 1, 1),
    _RuijieClusterBlacklistMacAddress_Type()
)
ruijieClusterBlacklistMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterBlacklistMacAddress.setStatus("current")
_RuijieClusterBlackListRowStatus_Type = RowStatus
_RuijieClusterBlackListRowStatus_Object = MibTableColumn
ruijieClusterBlackListRowStatus = _RuijieClusterBlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 22, 1, 2),
    _RuijieClusterBlackListRowStatus_Type()
)
ruijieClusterBlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterBlackListRowStatus.setStatus("current")
_RuijieClusterPasswordAuth_ObjectIdentity = ObjectIdentity
ruijieClusterPasswordAuth = _RuijieClusterPasswordAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23)
)
_RuijieClusterPasswordAuthPoolTable_Object = MibTable
ruijieClusterPasswordAuthPoolTable = _RuijieClusterPasswordAuthPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 1)
)
if mibBuilder.loadTexts:
    ruijieClusterPasswordAuthPoolTable.setStatus("current")
_RuijieClusterPasswordAuthPoolEntry_Object = MibTableRow
ruijieClusterPasswordAuthPoolEntry = _RuijieClusterPasswordAuthPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 1, 1)
)
ruijieClusterPasswordAuthPoolEntry.setIndexNames(
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterPasswordSn"),
)
if mibBuilder.loadTexts:
    ruijieClusterPasswordAuthPoolEntry.setStatus("current")


class _RuijieClusterPasswordSn_Type(Integer32):
    """Custom type ruijieClusterPasswordSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RuijieClusterPasswordSn_Type.__name__ = "Integer32"
_RuijieClusterPasswordSn_Object = MibTableColumn
ruijieClusterPasswordSn = _RuijieClusterPasswordSn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 1, 1, 1),
    _RuijieClusterPasswordSn_Type()
)
ruijieClusterPasswordSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterPasswordSn.setStatus("current")


class _RuijieClusterPassword_Type(DisplayString):
    """Custom type ruijieClusterPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_RuijieClusterPassword_Type.__name__ = "DisplayString"
_RuijieClusterPassword_Object = MibTableColumn
ruijieClusterPassword = _RuijieClusterPassword_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 1, 1, 2),
    _RuijieClusterPassword_Type()
)
ruijieClusterPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterPassword.setStatus("current")
_RuijieClusterPasswordAuthRowStatus_Type = RowStatus
_RuijieClusterPasswordAuthRowStatus_Object = MibTableColumn
ruijieClusterPasswordAuthRowStatus = _RuijieClusterPasswordAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 1, 1, 3),
    _RuijieClusterPasswordAuthRowStatus_Type()
)
ruijieClusterPasswordAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterPasswordAuthRowStatus.setStatus("current")
_RuijieClusterDeviceAuthPasswordTable_Object = MibTable
ruijieClusterDeviceAuthPasswordTable = _RuijieClusterDeviceAuthPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 2)
)
if mibBuilder.loadTexts:
    ruijieClusterDeviceAuthPasswordTable.setStatus("current")
_RuijieClusterDeviceAuthPasswordEntry_Object = MibTableRow
ruijieClusterDeviceAuthPasswordEntry = _RuijieClusterDeviceAuthPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 2, 1)
)
ruijieClusterDeviceAuthPasswordEntry.setIndexNames(
    (0, "RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceMacAddress"),
)
if mibBuilder.loadTexts:
    ruijieClusterDeviceAuthPasswordEntry.setStatus("current")
_RuijieClusterDeviceMacAddress_Type = MacAddress
_RuijieClusterDeviceMacAddress_Object = MibTableColumn
ruijieClusterDeviceMacAddress = _RuijieClusterDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 2, 1, 1),
    _RuijieClusterDeviceMacAddress_Type()
)
ruijieClusterDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClusterDeviceMacAddress.setStatus("current")


class _RuijieClusterDevicePassword_Type(DisplayString):
    """Custom type ruijieClusterDevicePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_RuijieClusterDevicePassword_Type.__name__ = "DisplayString"
_RuijieClusterDevicePassword_Object = MibTableColumn
ruijieClusterDevicePassword = _RuijieClusterDevicePassword_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 2, 1, 2),
    _RuijieClusterDevicePassword_Type()
)
ruijieClusterDevicePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterDevicePassword.setStatus("current")
_RuijieClusterDevicePasswordRowStatus_Type = RowStatus
_RuijieClusterDevicePasswordRowStatus_Object = MibTableColumn
ruijieClusterDevicePasswordRowStatus = _RuijieClusterDevicePasswordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 1, 23, 2, 1, 3),
    _RuijieClusterDevicePasswordRowStatus_Type()
)
ruijieClusterDevicePasswordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieClusterDevicePasswordRowStatus.setStatus("current")
_RuijieClusterTraps_ObjectIdentity = ObjectIdentity
ruijieClusterTraps = _RuijieClusterTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 2)
)
_RuijieClusterMIBConformance_ObjectIdentity = ObjectIdentity
ruijieClusterMIBConformance = _RuijieClusterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3)
)
_RuijieClusterMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieClusterMIBCompliances = _RuijieClusterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 1)
)
_RuijieClusterMIBGroups_ObjectIdentity = ObjectIdentity
ruijieClusterMIBGroups = _RuijieClusterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2)
)

# Managed Objects groups

ruijieClusterStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 1)
)
ruijieClusterStatusGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterName"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCmdMacAddress"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterIpPool"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterIpMask"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterVlan"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterHopsLimit"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterHopsLimit"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterTimerTopo"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterTimerHello"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterTimerHold"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterTftpServer"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterNumberOfMembers"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMaxNumberOfMembers"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDevMaxCapicity"))
)
if mibBuilder.loadTexts:
    ruijieClusterStatusGroup.setStatus("current")

ruijieClusterMemberStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 2)
)
ruijieClusterMemberStatusGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterName"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceEnable"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceRole"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceIP"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceSn"))
)
if mibBuilder.loadTexts:
    ruijieClusterMemberStatusGroup.setStatus("current")

ruijieClusterCandidateStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 3)
)
ruijieClusterCandidateStatusGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterName"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceRole"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceEnable"))
)
if mibBuilder.loadTexts:
    ruijieClusterCandidateStatusGroup.setStatus("current")

ruijieClusterMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 4)
)
ruijieClusterMemberGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberSn"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberMacAddress"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberLcIfx"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberUpIfx"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberLcPort"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberUpPort"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberName"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberIp"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberHops"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberState"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberUpSn"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberUpMAC"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberLastTopoUpdateTime"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberLastUdpUpdateTime"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberNoRecvTopoRspCount"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberNoRecvUdpRspCount"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberReload"))
)
if mibBuilder.loadTexts:
    ruijieClusterMemberGroup.setStatus("current")

ruijieClusterCandidateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 5)
)
ruijieClusterCandidateGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateMacAddress"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateUpMAC"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateLcIfx"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateUpIfx"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateLcPort"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateUpPort"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateHops"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateUpSn"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateState"))
)
if mibBuilder.loadTexts:
    ruijieClusterCandidateGroup.setStatus("current")

ruijieClusterMemberAddGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 6)
)
ruijieClusterMemberAddGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberAddMacAddress"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberAddSn"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberAddRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieClusterMemberAddGroup.setStatus("current")

ruijieClusterBlackListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 7)
)
ruijieClusterBlackListGroup.setObjects(
    ("RUIJIE-CLUSTER-MIB", "ruijieClusterBlacklistMacAddress")
)
if mibBuilder.loadTexts:
    ruijieClusterBlackListGroup.setStatus("current")

ruijieClusterPasswordAuthPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 8)
)
ruijieClusterPasswordAuthPoolGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterPasswordSn"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterPassword"))
)
if mibBuilder.loadTexts:
    ruijieClusterPasswordAuthPoolGroup.setStatus("current")

ruijieClsuterDeviceAuthPasswordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 2, 9)
)
ruijieClsuterDeviceAuthPasswordGroup.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterDeviceMacAddress"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterDevicePassword"))
)
if mibBuilder.loadTexts:
    ruijieClsuterDeviceAuthPasswordGroup.setStatus("current")


# Notification objects

ruijieClusterMemberStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 2, 1)
)
ruijieClusterMemberStateChangeTrap.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberSn"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberState"))
)
if mibBuilder.loadTexts:
    ruijieClusterMemberStateChangeTrap.setStatus(
        "current"
    )

ruijieClusterMemberFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 2, 2)
)
ruijieClusterMemberFailureTrap.setObjects(
    ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateMacAddress")
)
if mibBuilder.loadTexts:
    ruijieClusterMemberFailureTrap.setStatus(
        "current"
    )

ruijieClusterDevMaximumAllowedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieClusterDevMaximumAllowedTrap.setStatus(
        "current"
    )

ruijieClusterMemberMaximumAllowedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieClusterMemberMaximumAllowedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieClusterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 31, 3, 1, 1)
)
ruijieClusterCompliance.setObjects(
      *(("RUIJIE-CLUSTER-MIB", "ruijieClusterStatusGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberStatusGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterMemberAddGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterBlackListGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterPasswordAuthPoolGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClsuterDeviceAuthPasswordGroup"),
        ("RUIJIE-CLUSTER-MIB", "ruijieClusterCandidateStatusGroup"))
)
if mibBuilder.loadTexts:
    ruijieClusterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CLUSTER-MIB",
    **{"ruijieClusterMIB": ruijieClusterMIB,
       "ruijieClusterMIBObjects": ruijieClusterMIBObjects,
       "ruijieClusterName": ruijieClusterName,
       "ruijieClusterStatus": ruijieClusterStatus,
       "ruijieClusterCmdMacAddress": ruijieClusterCmdMacAddress,
       "ruijieClusterCmdName": ruijieClusterCmdName,
       "ruijieClusterVlan": ruijieClusterVlan,
       "ruijieClusterHopsLimit": ruijieClusterHopsLimit,
       "ruijieClusterTimerTopo": ruijieClusterTimerTopo,
       "ruijieClusterTimerHello": ruijieClusterTimerHello,
       "ruijieClusterTimerHold": ruijieClusterTimerHold,
       "ruijieClusterTftpServer": ruijieClusterTftpServer,
       "ruijieClusterNumberOfMembers": ruijieClusterNumberOfMembers,
       "ruijieClusterMaxNumberOfMembers": ruijieClusterMaxNumberOfMembers,
       "ruijieClusterDevMaxCapicity": ruijieClusterDevMaxCapicity,
       "ruijieClusterAutoAdd": ruijieClusterAutoAdd,
       "ruijieClusterExplore": ruijieClusterExplore,
       "ruijieClusterSpecifyAdmin": ruijieClusterSpecifyAdmin,
       "ruijieClusterSpecifyAdminAddress": ruijieClusterSpecifyAdminAddress,
       "ruijieClusterSpecifyAdminName": ruijieClusterSpecifyAdminName,
       "ruijieClusterDeviceInfo": ruijieClusterDeviceInfo,
       "ruijieClusterDeviceEnable": ruijieClusterDeviceEnable,
       "ruijieClusterDeviceRole": ruijieClusterDeviceRole,
       "ruijieClusterDeviceIP": ruijieClusterDeviceIP,
       "ruijieClusterDeviceSn": ruijieClusterDeviceSn,
       "ruijieClusterIpPoolTable": ruijieClusterIpPoolTable,
       "ruijieClusterIpPoolEntry": ruijieClusterIpPoolEntry,
       "ruijieClusterIpPool": ruijieClusterIpPool,
       "ruijieClusterIpMask": ruijieClusterIpMask,
       "ruijieClusterIpPoolRowStatus": ruijieClusterIpPoolRowStatus,
       "ruijieClusterMemberAddTable": ruijieClusterMemberAddTable,
       "ruijieClusterMemberAddEntry": ruijieClusterMemberAddEntry,
       "ruijieClusterMemberAddSn": ruijieClusterMemberAddSn,
       "ruijieClusterMemberAddMacAddress": ruijieClusterMemberAddMacAddress,
       "ruijieClusterMemberAddRowStatus": ruijieClusterMemberAddRowStatus,
       "ruijieClusterMemberTable": ruijieClusterMemberTable,
       "ruijieClusterMemberEntry": ruijieClusterMemberEntry,
       "ruijieClusterMemberSn": ruijieClusterMemberSn,
       "ruijieClusterMemberUpMAC": ruijieClusterMemberUpMAC,
       "ruijieClusterMemberLcIfx": ruijieClusterMemberLcIfx,
       "ruijieClusterMemberUpIfx": ruijieClusterMemberUpIfx,
       "ruijieClusterMemberLcPort": ruijieClusterMemberLcPort,
       "ruijieClusterMemberUpPort": ruijieClusterMemberUpPort,
       "ruijieClusterMemberMacAddress": ruijieClusterMemberMacAddress,
       "ruijieClusterMemberName": ruijieClusterMemberName,
       "ruijieClusterMemberIp": ruijieClusterMemberIp,
       "ruijieClusterMemberHops": ruijieClusterMemberHops,
       "ruijieClusterMemberState": ruijieClusterMemberState,
       "ruijieClusterMemberUpSn": ruijieClusterMemberUpSn,
       "ruijieClusterMemberLastTopoUpdateTime": ruijieClusterMemberLastTopoUpdateTime,
       "ruijieClusterMemberLastUdpUpdateTime": ruijieClusterMemberLastUdpUpdateTime,
       "ruijieClusterMemberNoRecvTopoRspCount": ruijieClusterMemberNoRecvTopoRspCount,
       "ruijieClusterMemberNoRecvUdpRspCount": ruijieClusterMemberNoRecvUdpRspCount,
       "ruijieClusterMemberReload": ruijieClusterMemberReload,
       "ruijieClusterCandidateTable": ruijieClusterCandidateTable,
       "ruijieClusterCandidateEntry": ruijieClusterCandidateEntry,
       "ruijieClusterCandidateMacAddress": ruijieClusterCandidateMacAddress,
       "ruijieClusterCandidateUpMAC": ruijieClusterCandidateUpMAC,
       "ruijieClusterCandidateLcIfx": ruijieClusterCandidateLcIfx,
       "ruijieClusterCandidateUpIfx": ruijieClusterCandidateUpIfx,
       "ruijieClusterCandidateLcPort": ruijieClusterCandidateLcPort,
       "ruijieClusterCandidateUpPort": ruijieClusterCandidateUpPort,
       "ruijieClusterCandidateUpSn": ruijieClusterCandidateUpSn,
       "ruijieClusterCandidateHops": ruijieClusterCandidateHops,
       "ruijieClusterCandidateState": ruijieClusterCandidateState,
       "ruijieClusterBlacklistTable": ruijieClusterBlacklistTable,
       "ruijieClusterBlacklistEntry": ruijieClusterBlacklistEntry,
       "ruijieClusterBlacklistMacAddress": ruijieClusterBlacklistMacAddress,
       "ruijieClusterBlackListRowStatus": ruijieClusterBlackListRowStatus,
       "ruijieClusterPasswordAuth": ruijieClusterPasswordAuth,
       "ruijieClusterPasswordAuthPoolTable": ruijieClusterPasswordAuthPoolTable,
       "ruijieClusterPasswordAuthPoolEntry": ruijieClusterPasswordAuthPoolEntry,
       "ruijieClusterPasswordSn": ruijieClusterPasswordSn,
       "ruijieClusterPassword": ruijieClusterPassword,
       "ruijieClusterPasswordAuthRowStatus": ruijieClusterPasswordAuthRowStatus,
       "ruijieClusterDeviceAuthPasswordTable": ruijieClusterDeviceAuthPasswordTable,
       "ruijieClusterDeviceAuthPasswordEntry": ruijieClusterDeviceAuthPasswordEntry,
       "ruijieClusterDeviceMacAddress": ruijieClusterDeviceMacAddress,
       "ruijieClusterDevicePassword": ruijieClusterDevicePassword,
       "ruijieClusterDevicePasswordRowStatus": ruijieClusterDevicePasswordRowStatus,
       "ruijieClusterTraps": ruijieClusterTraps,
       "ruijieClusterMemberStateChangeTrap": ruijieClusterMemberStateChangeTrap,
       "ruijieClusterMemberFailureTrap": ruijieClusterMemberFailureTrap,
       "ruijieClusterDevMaximumAllowedTrap": ruijieClusterDevMaximumAllowedTrap,
       "ruijieClusterMemberMaximumAllowedTrap": ruijieClusterMemberMaximumAllowedTrap,
       "ruijieClusterMIBConformance": ruijieClusterMIBConformance,
       "ruijieClusterMIBCompliances": ruijieClusterMIBCompliances,
       "ruijieClusterCompliance": ruijieClusterCompliance,
       "ruijieClusterMIBGroups": ruijieClusterMIBGroups,
       "ruijieClusterStatusGroup": ruijieClusterStatusGroup,
       "ruijieClusterMemberStatusGroup": ruijieClusterMemberStatusGroup,
       "ruijieClusterCandidateStatusGroup": ruijieClusterCandidateStatusGroup,
       "ruijieClusterMemberGroup": ruijieClusterMemberGroup,
       "ruijieClusterCandidateGroup": ruijieClusterCandidateGroup,
       "ruijieClusterMemberAddGroup": ruijieClusterMemberAddGroup,
       "ruijieClusterBlackListGroup": ruijieClusterBlackListGroup,
       "ruijieClusterPasswordAuthPoolGroup": ruijieClusterPasswordAuthPoolGroup,
       "ruijieClsuterDeviceAuthPasswordGroup": ruijieClsuterDeviceAuthPasswordGroup}
)
