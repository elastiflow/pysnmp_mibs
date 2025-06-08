# SNMP MIB module (RUIJIE-SMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SMP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:10 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(Community,) = mibBuilder.importSymbols(
    "RUIJIE-SNMP-AGENT-MIB",
    "Community")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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


# MODULE-IDENTITY

ruijieSMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39)
)
if mibBuilder.loadTexts:
    ruijieSMPMIB.setRevisions(
        ("2004-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSMPMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSMPMIBObjects = _RuijieSMPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1)
)
_RuijieSMPServer_Type = IpAddress
_RuijieSMPServer_Object = MibScalar
ruijieSMPServer = _RuijieSMPServer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 1),
    _RuijieSMPServer_Type()
)
ruijieSMPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPServer.setStatus("current")
_RuijieSMPServerKey_Type = Community
_RuijieSMPServerKey_Object = MibScalar
ruijieSMPServerKey = _RuijieSMPServerKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 2),
    _RuijieSMPServerKey_Type()
)
ruijieSMPServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPServerKey.setStatus("current")
_RuijieSMPEventSendSlice_Type = Unsigned32
_RuijieSMPEventSendSlice_Object = MibScalar
ruijieSMPEventSendSlice = _RuijieSMPEventSendSlice_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 3),
    _RuijieSMPEventSendSlice_Type()
)
ruijieSMPEventSendSlice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPEventSendSlice.setStatus("current")
_RuijieSMPPolicyDelete_Type = Integer32
_RuijieSMPPolicyDelete_Object = MibScalar
ruijieSMPPolicyDelete = _RuijieSMPPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 4),
    _RuijieSMPPolicyDelete_Type()
)
ruijieSMPPolicyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyDelete.setStatus("current")


class _RuijieSMPPolicyChecksum_Type(OctetString):
    """Custom type ruijieSMPPolicyChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieSMPPolicyChecksum_Type.__name__ = "OctetString"
_RuijieSMPPolicyChecksum_Object = MibScalar
ruijieSMPPolicyChecksum = _RuijieSMPPolicyChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 5),
    _RuijieSMPPolicyChecksum_Type()
)
ruijieSMPPolicyChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSMPPolicyChecksum.setStatus("current")
_RuijieSMPPolicyTimeout_Type = Unsigned32
_RuijieSMPPolicyTimeout_Object = MibScalar
ruijieSMPPolicyTimeout = _RuijieSMPPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 6),
    _RuijieSMPPolicyTimeout_Type()
)
ruijieSMPPolicyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyTimeout.setStatus("current")
_RuijieSMPFrameRelayTable_Object = MibTable
ruijieSMPFrameRelayTable = _RuijieSMPFrameRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayTable.setStatus("current")
_RuijieSMPFrameRelayEntry_Object = MibTableRow
ruijieSMPFrameRelayEntry = _RuijieSMPFrameRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 7, 1)
)
ruijieSMPFrameRelayEntry.setIndexNames(
    (0, "RUIJIE-SMP-MIB", "ruijieSMPFrameRelayIndex"),
)
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayEntry.setStatus("current")
_RuijieSMPFrameRelayIndex_Type = Unsigned32
_RuijieSMPFrameRelayIndex_Object = MibTableColumn
ruijieSMPFrameRelayIndex = _RuijieSMPFrameRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 7, 1, 1),
    _RuijieSMPFrameRelayIndex_Type()
)
ruijieSMPFrameRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayIndex.setStatus("current")


class _RuijieSMPFrameRelayContent_Type(OctetString):
    """Custom type ruijieSMPFrameRelayContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RuijieSMPFrameRelayContent_Type.__name__ = "OctetString"
_RuijieSMPFrameRelayContent_Object = MibTableColumn
ruijieSMPFrameRelayContent = _RuijieSMPFrameRelayContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 7, 1, 2),
    _RuijieSMPFrameRelayContent_Type()
)
ruijieSMPFrameRelayContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayContent.setStatus("current")
_RuijieSMPFrameRelayLength_Type = Unsigned32
_RuijieSMPFrameRelayLength_Object = MibTableColumn
ruijieSMPFrameRelayLength = _RuijieSMPFrameRelayLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 7, 1, 3),
    _RuijieSMPFrameRelayLength_Type()
)
ruijieSMPFrameRelayLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayLength.setStatus("current")
_RuijieSMPFrameRelayDestPort_Type = IfIndex
_RuijieSMPFrameRelayDestPort_Object = MibTableColumn
ruijieSMPFrameRelayDestPort = _RuijieSMPFrameRelayDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 7, 1, 4),
    _RuijieSMPFrameRelayDestPort_Type()
)
ruijieSMPFrameRelayDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayDestPort.setStatus("current")
_RuijieSMPFrameRelayDestVlan_Type = VlanId
_RuijieSMPFrameRelayDestVlan_Object = MibTableColumn
ruijieSMPFrameRelayDestVlan = _RuijieSMPFrameRelayDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 7, 1, 5),
    _RuijieSMPFrameRelayDestVlan_Type()
)
ruijieSMPFrameRelayDestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayDestVlan.setStatus("current")
_RuijieSMPPolicyTable_Object = MibTable
ruijieSMPPolicyTable = _RuijieSMPPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieSMPPolicyTable.setStatus("current")
_RuijieSMPPolicyEntry_Object = MibTableRow
ruijieSMPPolicyEntry = _RuijieSMPPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1)
)
ruijieSMPPolicyEntry.setIndexNames(
    (0, "RUIJIE-SMP-MIB", "ruijieSMPGroupIndex"),
    (0, "RUIJIE-SMP-MIB", "ruijieSMPPolicyIndex"),
)
if mibBuilder.loadTexts:
    ruijieSMPPolicyEntry.setStatus("current")
_RuijieSMPGroupIndex_Type = Unsigned32
_RuijieSMPGroupIndex_Object = MibTableColumn
ruijieSMPGroupIndex = _RuijieSMPGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 1),
    _RuijieSMPGroupIndex_Type()
)
ruijieSMPGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSMPGroupIndex.setStatus("current")
_RuijieSMPPolicyIndex_Type = Unsigned32
_RuijieSMPPolicyIndex_Object = MibTableColumn
ruijieSMPPolicyIndex = _RuijieSMPPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 2),
    _RuijieSMPPolicyIndex_Type()
)
ruijieSMPPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSMPPolicyIndex.setStatus("current")
_RuijieSMPPolicyStatus_Type = ConfigStatus
_RuijieSMPPolicyStatus_Object = MibTableColumn
ruijieSMPPolicyStatus = _RuijieSMPPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 3),
    _RuijieSMPPolicyStatus_Type()
)
ruijieSMPPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyStatus.setStatus("current")
_RuijieSMPPolicyNumber_Type = Unsigned32
_RuijieSMPPolicyNumber_Object = MibTableColumn
ruijieSMPPolicyNumber = _RuijieSMPPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 4),
    _RuijieSMPPolicyNumber_Type()
)
ruijieSMPPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyNumber.setStatus("current")
_RuijieSMPPolicyInstallPort_Type = IfIndex
_RuijieSMPPolicyInstallPort_Object = MibTableColumn
ruijieSMPPolicyInstallPort = _RuijieSMPPolicyInstallPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 5),
    _RuijieSMPPolicyInstallPort_Type()
)
ruijieSMPPolicyInstallPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyInstallPort.setStatus("current")


class _RuijieSMPPolicyType_Type(Integer32):
    """Custom type ruijieSMPPolicyType based on Integer32"""
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
        *(("hi-isolate", 1),
          ("isolate", 2),
          ("blocked", 3),
          ("addrBind", 4))
    )


_RuijieSMPPolicyType_Type.__name__ = "Integer32"
_RuijieSMPPolicyType_Object = MibTableColumn
ruijieSMPPolicyType = _RuijieSMPPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 6),
    _RuijieSMPPolicyType_Type()
)
ruijieSMPPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyType.setStatus("current")


class _RuijieSMPPolicyContent_Type(OctetString):
    """Custom type ruijieSMPPolicyContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_RuijieSMPPolicyContent_Type.__name__ = "OctetString"
_RuijieSMPPolicyContent_Object = MibTableColumn
ruijieSMPPolicyContent = _RuijieSMPPolicyContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 7),
    _RuijieSMPPolicyContent_Type()
)
ruijieSMPPolicyContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyContent.setStatus("current")


class _RuijieSMPPolicyMask_Type(OctetString):
    """Custom type ruijieSMPPolicyMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_RuijieSMPPolicyMask_Type.__name__ = "OctetString"
_RuijieSMPPolicyMask_Object = MibTableColumn
ruijieSMPPolicyMask = _RuijieSMPPolicyMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 8),
    _RuijieSMPPolicyMask_Type()
)
ruijieSMPPolicyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyMask.setStatus("current")


class _RuijieSMPPolicyName_Type(DisplayString):
    """Custom type ruijieSMPPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSMPPolicyName_Type.__name__ = "DisplayString"
_RuijieSMPPolicyName_Object = MibTableColumn
ruijieSMPPolicyName = _RuijieSMPPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 8, 1, 9),
    _RuijieSMPPolicyName_Type()
)
ruijieSMPPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPPolicyName.setStatus("current")
_RuijieSMPPolicyGroupTable_Object = MibTable
ruijieSMPPolicyGroupTable = _RuijieSMPPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieSMPPolicyGroupTable.setStatus("current")
_RuijieSMPPolicyGroupEntry_Object = MibTableRow
ruijieSMPPolicyGroupEntry = _RuijieSMPPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 9, 1)
)
ruijieSMPPolicyGroupEntry.setIndexNames(
    (0, "RUIJIE-SMP-MIB", "ruijieSMPPolicyGroupIndex"),
)
if mibBuilder.loadTexts:
    ruijieSMPPolicyGroupEntry.setStatus("current")
_RuijieSMPPolicyGroupIndex_Type = Unsigned32
_RuijieSMPPolicyGroupIndex_Object = MibTableColumn
ruijieSMPPolicyGroupIndex = _RuijieSMPPolicyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 9, 1, 1),
    _RuijieSMPPolicyGroupIndex_Type()
)
ruijieSMPPolicyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSMPPolicyGroupIndex.setStatus("current")
_RuijieSMPPolicyGroupCount_Type = Unsigned32
_RuijieSMPPolicyGroupCount_Object = MibTableColumn
ruijieSMPPolicyGroupCount = _RuijieSMPPolicyGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 9, 1, 2),
    _RuijieSMPPolicyGroupCount_Type()
)
ruijieSMPPolicyGroupCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSMPPolicyGroupCount.setStatus("current")


class _RuijieSMPPolicyGroupChecksum_Type(OctetString):
    """Custom type ruijieSMPPolicyGroupChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieSMPPolicyGroupChecksum_Type.__name__ = "OctetString"
_RuijieSMPPolicyGroupChecksum_Object = MibTableColumn
ruijieSMPPolicyGroupChecksum = _RuijieSMPPolicyGroupChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 9, 1, 3),
    _RuijieSMPPolicyGroupChecksum_Type()
)
ruijieSMPPolicyGroupChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSMPPolicyGroupChecksum.setStatus("current")
_RuijieSMPPolicyGroupStatus_Type = RowStatus
_RuijieSMPPolicyGroupStatus_Object = MibTableColumn
ruijieSMPPolicyGroupStatus = _RuijieSMPPolicyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 1, 9, 1, 4),
    _RuijieSMPPolicyGroupStatus_Type()
)
ruijieSMPPolicyGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSMPPolicyGroupStatus.setStatus("current")
_RuijieEGMIBObjects_ObjectIdentity = ObjectIdentity
ruijieEGMIBObjects = _RuijieEGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2)
)
_RuijieEGUserTable_Object = MibTable
ruijieEGUserTable = _RuijieEGUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieEGUserTable.setStatus("current")
_RuijieEGUserEntry_Object = MibTableRow
ruijieEGUserEntry = _RuijieEGUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1)
)
ruijieEGUserEntry.setIndexNames(
    (0, "RUIJIE-SMP-MIB", "ruijieEGUserIpAddrType"),
    (0, "RUIJIE-SMP-MIB", "ruijieEGUserIpAddr"),
)
if mibBuilder.loadTexts:
    ruijieEGUserEntry.setStatus("current")
_RuijieEGUserIpAddrType_Type = InetAddressType
_RuijieEGUserIpAddrType_Object = MibTableColumn
ruijieEGUserIpAddrType = _RuijieEGUserIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 1),
    _RuijieEGUserIpAddrType_Type()
)
ruijieEGUserIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEGUserIpAddrType.setStatus("current")
_RuijieEGUserIpAddr_Type = InetAddress
_RuijieEGUserIpAddr_Object = MibTableColumn
ruijieEGUserIpAddr = _RuijieEGUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 2),
    _RuijieEGUserIpAddr_Type()
)
ruijieEGUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEGUserIpAddr.setStatus("current")


class _RuijieEGUserId_Type(OctetString):
    """Custom type ruijieEGUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieEGUserId_Type.__name__ = "OctetString"
_RuijieEGUserId_Object = MibTableColumn
ruijieEGUserId = _RuijieEGUserId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 3),
    _RuijieEGUserId_Type()
)
ruijieEGUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGUserId.setStatus("current")


class _RuijieEGUserName_Type(OctetString):
    """Custom type ruijieEGUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieEGUserName_Type.__name__ = "OctetString"
_RuijieEGUserName_Object = MibTableColumn
ruijieEGUserName = _RuijieEGUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 4),
    _RuijieEGUserName_Type()
)
ruijieEGUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGUserName.setStatus("current")


class _RuijieEGUserGroupName_Type(OctetString):
    """Custom type ruijieEGUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieEGUserGroupName_Type.__name__ = "OctetString"
_RuijieEGUserGroupName_Object = MibTableColumn
ruijieEGUserGroupName = _RuijieEGUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 5),
    _RuijieEGUserGroupName_Type()
)
ruijieEGUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGUserGroupName.setStatus("current")
_RuijieEGUserMac_Type = MacAddress
_RuijieEGUserMac_Object = MibTableColumn
ruijieEGUserMac = _RuijieEGUserMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 6),
    _RuijieEGUserMac_Type()
)
ruijieEGUserMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGUserMac.setStatus("current")
_RuijieEGNasIp_Type = InetAddress
_RuijieEGNasIp_Object = MibTableColumn
ruijieEGNasIp = _RuijieEGNasIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 7),
    _RuijieEGNasIp_Type()
)
ruijieEGNasIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGNasIp.setStatus("current")
_RuijieEGNasPort_Type = Gauge32
_RuijieEGNasPort_Object = MibTableColumn
ruijieEGNasPort = _RuijieEGNasPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 8),
    _RuijieEGNasPort_Type()
)
ruijieEGNasPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGNasPort.setStatus("current")
_RuijieEGGatewayIp_Type = InetAddress
_RuijieEGGatewayIp_Object = MibTableColumn
ruijieEGGatewayIp = _RuijieEGGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 9),
    _RuijieEGGatewayIp_Type()
)
ruijieEGGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGGatewayIp.setStatus("current")
_RuijieEGVlanId_Type = Gauge32
_RuijieEGVlanId_Object = MibTableColumn
ruijieEGVlanId = _RuijieEGVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 10),
    _RuijieEGVlanId_Type()
)
ruijieEGVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGVlanId.setStatus("current")
_RuijieEGLoginTime_Type = OctetString
_RuijieEGLoginTime_Object = MibTableColumn
ruijieEGLoginTime = _RuijieEGLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 11),
    _RuijieEGLoginTime_Type()
)
ruijieEGLoginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGLoginTime.setStatus("current")
_RuijieEGLogoutTime_Type = OctetString
_RuijieEGLogoutTime_Object = MibTableColumn
ruijieEGLogoutTime = _RuijieEGLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 12),
    _RuijieEGLogoutTime_Type()
)
ruijieEGLogoutTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGLogoutTime.setStatus("current")
_RuijieEGMessageType_Type = Gauge32
_RuijieEGMessageType_Object = MibTableColumn
ruijieEGMessageType = _RuijieEGMessageType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 13),
    _RuijieEGMessageType_Type()
)
ruijieEGMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGMessageType.setStatus("current")
_RuijieEGUserStatus_Type = RowStatus
_RuijieEGUserStatus_Object = MibTableColumn
ruijieEGUserStatus = _RuijieEGUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 1, 1, 14),
    _RuijieEGUserStatus_Type()
)
ruijieEGUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieEGUserStatus.setStatus("current")
_RuijieEGUserDelete_Type = Integer32
_RuijieEGUserDelete_Object = MibScalar
ruijieEGUserDelete = _RuijieEGUserDelete_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 2, 2),
    _RuijieEGUserDelete_Type()
)
ruijieEGUserDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieEGUserDelete.setStatus("current")
_RuijieSMPMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSMPMIBConformance = _RuijieSMPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3)
)
_RuijieSMPMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSMPMIBCompliances = _RuijieSMPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3, 1)
)
_RuijieSMPMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSMPMIBGroups = _RuijieSMPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3, 2)
)
_RuijieSMPTraps_ObjectIdentity = ObjectIdentity
ruijieSMPTraps = _RuijieSMPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535)
)
_RuijieSMPSwitchIP_Type = IpAddress
_RuijieSMPSwitchIP_Object = MibScalar
ruijieSMPSwitchIP = _RuijieSMPSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 1),
    _RuijieSMPSwitchIP_Type()
)
ruijieSMPSwitchIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPSwitchIP.setStatus("current")
_RuijieSMPSwitchInterfaceID_Type = IfIndex
_RuijieSMPSwitchInterfaceID_Object = MibScalar
ruijieSMPSwitchInterfaceID = _RuijieSMPSwitchInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 2),
    _RuijieSMPSwitchInterfaceID_Type()
)
ruijieSMPSwitchInterfaceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPSwitchInterfaceID.setStatus("current")
_RuijieSMPSwitchInterfaceVLANID_Type = VlanId
_RuijieSMPSwitchInterfaceVLANID_Object = MibScalar
ruijieSMPSwitchInterfaceVLANID = _RuijieSMPSwitchInterfaceVLANID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 3),
    _RuijieSMPSwitchInterfaceVLANID_Type()
)
ruijieSMPSwitchInterfaceVLANID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPSwitchInterfaceVLANID.setStatus("current")
_RuijieSMPFrameContentLength_Type = Unsigned32
_RuijieSMPFrameContentLength_Object = MibScalar
ruijieSMPFrameContentLength = _RuijieSMPFrameContentLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 4),
    _RuijieSMPFrameContentLength_Type()
)
ruijieSMPFrameContentLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPFrameContentLength.setStatus("current")


class _RuijieSMPFrameContent_Type(OctetString):
    """Custom type ruijieSMPFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RuijieSMPFrameContent_Type.__name__ = "OctetString"
_RuijieSMPFrameContent_Object = MibScalar
ruijieSMPFrameContent = _RuijieSMPFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 5),
    _RuijieSMPFrameContent_Type()
)
ruijieSMPFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPFrameContent.setStatus("current")


class _RuijieSMPArpAttackSubnetIP_Type(OctetString):
    """Custom type ruijieSMPArpAttackSubnetIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RuijieSMPArpAttackSubnetIP_Type.__name__ = "OctetString"
_RuijieSMPArpAttackSubnetIP_Object = MibScalar
ruijieSMPArpAttackSubnetIP = _RuijieSMPArpAttackSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 7),
    _RuijieSMPArpAttackSubnetIP_Type()
)
ruijieSMPArpAttackSubnetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackSubnetIP.setStatus("current")
_RuijieSMPArpAttackSubnetIPNum_Type = Integer32
_RuijieSMPArpAttackSubnetIPNum_Object = MibScalar
ruijieSMPArpAttackSubnetIPNum = _RuijieSMPArpAttackSubnetIPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 8),
    _RuijieSMPArpAttackSubnetIPNum_Type()
)
ruijieSMPArpAttackSubnetIPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackSubnetIPNum.setStatus("current")
_RuijieSMPArpAttackInterfaceSlot_Type = Integer32
_RuijieSMPArpAttackInterfaceSlot_Object = MibScalar
ruijieSMPArpAttackInterfaceSlot = _RuijieSMPArpAttackInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 9),
    _RuijieSMPArpAttackInterfaceSlot_Type()
)
ruijieSMPArpAttackInterfaceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackInterfaceSlot.setStatus("current")
_RuijieSMPArpAttackInterfacePort_Type = Integer32
_RuijieSMPArpAttackInterfacePort_Object = MibScalar
ruijieSMPArpAttackInterfacePort = _RuijieSMPArpAttackInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 10),
    _RuijieSMPArpAttackInterfacePort_Type()
)
ruijieSMPArpAttackInterfacePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackInterfacePort.setStatus("current")
_RuijieSMPArpAttackInterfaceVlanID_Type = VlanId
_RuijieSMPArpAttackInterfaceVlanID_Object = MibScalar
ruijieSMPArpAttackInterfaceVlanID = _RuijieSMPArpAttackInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 11),
    _RuijieSMPArpAttackInterfaceVlanID_Type()
)
ruijieSMPArpAttackInterfaceVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackInterfaceVlanID.setStatus("current")


class _RuijieSMPArpAttackFrameContent_Type(OctetString):
    """Custom type ruijieSMPArpAttackFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieSMPArpAttackFrameContent_Type.__name__ = "OctetString"
_RuijieSMPArpAttackFrameContent_Object = MibScalar
ruijieSMPArpAttackFrameContent = _RuijieSMPArpAttackFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 12),
    _RuijieSMPArpAttackFrameContent_Type()
)
ruijieSMPArpAttackFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackFrameContent.setStatus("current")
_RuijieSMPArpAttackStatus_Type = TruthValue
_RuijieSMPArpAttackStatus_Object = MibScalar
ruijieSMPArpAttackStatus = _RuijieSMPArpAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 13),
    _RuijieSMPArpAttackStatus_Type()
)
ruijieSMPArpAttackStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackStatus.setStatus("current")


class _RuijieSMPArpAttackCriticalStatus_Type(Integer32):
    """Custom type ruijieSMPArpAttackCriticalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("emergencies", 2))
    )


_RuijieSMPArpAttackCriticalStatus_Type.__name__ = "Integer32"
_RuijieSMPArpAttackCriticalStatus_Object = MibScalar
ruijieSMPArpAttackCriticalStatus = _RuijieSMPArpAttackCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 14),
    _RuijieSMPArpAttackCriticalStatus_Type()
)
ruijieSMPArpAttackCriticalStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackCriticalStatus.setStatus("current")
_RuijieSMPArpAttackMac_Type = MacAddress
_RuijieSMPArpAttackMac_Object = MibScalar
ruijieSMPArpAttackMac = _RuijieSMPArpAttackMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 15),
    _RuijieSMPArpAttackMac_Type()
)
ruijieSMPArpAttackMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackMac.setStatus("current")
_RuijieSMPArpAttackInterfaceIndex_Type = Integer32
_RuijieSMPArpAttackInterfaceIndex_Object = MibScalar
ruijieSMPArpAttackInterfaceIndex = _RuijieSMPArpAttackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 16),
    _RuijieSMPArpAttackInterfaceIndex_Type()
)
ruijieSMPArpAttackInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSMPArpAttackInterfaceIndex.setStatus("current")

# Managed Objects groups

ruijieSMPServerMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3, 2, 1)
)
ruijieSMPServerMibGroup.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPServer"),
        ("RUIJIE-SMP-MIB", "ruijieSMPServerKey"))
)
if mibBuilder.loadTexts:
    ruijieSMPServerMibGroup.setStatus("current")

ruijieSMPClientMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3, 2, 2)
)
ruijieSMPClientMibGroup.setObjects(
    ("RUIJIE-SMP-MIB", "ruijieSMPEventSendSlice")
)
if mibBuilder.loadTexts:
    ruijieSMPClientMibGroup.setStatus("current")

ruijieSMPPolicyMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3, 2, 3)
)
ruijieSMPPolicyMibGroup.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPPolicyDelete"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyChecksum"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyIndex"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyStatus"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyInstallPort"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyType"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyContent"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyMask"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyName"))
)
if mibBuilder.loadTexts:
    ruijieSMPPolicyMibGroup.setStatus("current")

ruijieSMPFrameRelayMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3, 2, 4)
)
ruijieSMPFrameRelayMibGroup.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPFrameRelayIndex"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameRelayContent"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameRelayLength"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameRelayDestPort"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameRelayDestVlan"))
)
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayMibGroup.setStatus("current")


# Notification objects

ruijieSMPFrameRelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 6)
)
ruijieSMPFrameRelayTrap.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPSwitchIP"),
        ("RUIJIE-SMP-MIB", "ruijieSMPSwitchInterfaceID"),
        ("RUIJIE-SMP-MIB", "ruijieSMPSwitchInterfaceVLANID"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameContentLength"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameContent"))
)
if mibBuilder.loadTexts:
    ruijieSMPFrameRelayTrap.setStatus(
        "current"
    )

ruijieSMPArpAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 65535, 17)
)
ruijieSMPArpAttackTrap.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPArpAttackSubnetIP"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackSubnetIPNum"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfaceSlot"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfacePort"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfaceVlanID"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackFrameContent"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackStatus"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackCriticalStatus"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackMac"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfaceIndex"))
)
if mibBuilder.loadTexts:
    ruijieSMPArpAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 39, 3, 1, 1)
)
ruijieDeviceMIBCompliance.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPServerMibGroup"),
        ("RUIJIE-SMP-MIB", "ruijieSMPClientMibGroup"),
        ("RUIJIE-SMP-MIB", "ruijieSMPPolicyMibGroup"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameRelayMibGroup"))
)
if mibBuilder.loadTexts:
    ruijieDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SMP-MIB",
    **{"ruijieSMPMIB": ruijieSMPMIB,
       "ruijieSMPMIBObjects": ruijieSMPMIBObjects,
       "ruijieSMPServer": ruijieSMPServer,
       "ruijieSMPServerKey": ruijieSMPServerKey,
       "ruijieSMPEventSendSlice": ruijieSMPEventSendSlice,
       "ruijieSMPPolicyDelete": ruijieSMPPolicyDelete,
       "ruijieSMPPolicyChecksum": ruijieSMPPolicyChecksum,
       "ruijieSMPPolicyTimeout": ruijieSMPPolicyTimeout,
       "ruijieSMPFrameRelayTable": ruijieSMPFrameRelayTable,
       "ruijieSMPFrameRelayEntry": ruijieSMPFrameRelayEntry,
       "ruijieSMPFrameRelayIndex": ruijieSMPFrameRelayIndex,
       "ruijieSMPFrameRelayContent": ruijieSMPFrameRelayContent,
       "ruijieSMPFrameRelayLength": ruijieSMPFrameRelayLength,
       "ruijieSMPFrameRelayDestPort": ruijieSMPFrameRelayDestPort,
       "ruijieSMPFrameRelayDestVlan": ruijieSMPFrameRelayDestVlan,
       "ruijieSMPPolicyTable": ruijieSMPPolicyTable,
       "ruijieSMPPolicyEntry": ruijieSMPPolicyEntry,
       "ruijieSMPGroupIndex": ruijieSMPGroupIndex,
       "ruijieSMPPolicyIndex": ruijieSMPPolicyIndex,
       "ruijieSMPPolicyStatus": ruijieSMPPolicyStatus,
       "ruijieSMPPolicyNumber": ruijieSMPPolicyNumber,
       "ruijieSMPPolicyInstallPort": ruijieSMPPolicyInstallPort,
       "ruijieSMPPolicyType": ruijieSMPPolicyType,
       "ruijieSMPPolicyContent": ruijieSMPPolicyContent,
       "ruijieSMPPolicyMask": ruijieSMPPolicyMask,
       "ruijieSMPPolicyName": ruijieSMPPolicyName,
       "ruijieSMPPolicyGroupTable": ruijieSMPPolicyGroupTable,
       "ruijieSMPPolicyGroupEntry": ruijieSMPPolicyGroupEntry,
       "ruijieSMPPolicyGroupIndex": ruijieSMPPolicyGroupIndex,
       "ruijieSMPPolicyGroupCount": ruijieSMPPolicyGroupCount,
       "ruijieSMPPolicyGroupChecksum": ruijieSMPPolicyGroupChecksum,
       "ruijieSMPPolicyGroupStatus": ruijieSMPPolicyGroupStatus,
       "ruijieEGMIBObjects": ruijieEGMIBObjects,
       "ruijieEGUserTable": ruijieEGUserTable,
       "ruijieEGUserEntry": ruijieEGUserEntry,
       "ruijieEGUserIpAddrType": ruijieEGUserIpAddrType,
       "ruijieEGUserIpAddr": ruijieEGUserIpAddr,
       "ruijieEGUserId": ruijieEGUserId,
       "ruijieEGUserName": ruijieEGUserName,
       "ruijieEGUserGroupName": ruijieEGUserGroupName,
       "ruijieEGUserMac": ruijieEGUserMac,
       "ruijieEGNasIp": ruijieEGNasIp,
       "ruijieEGNasPort": ruijieEGNasPort,
       "ruijieEGGatewayIp": ruijieEGGatewayIp,
       "ruijieEGVlanId": ruijieEGVlanId,
       "ruijieEGLoginTime": ruijieEGLoginTime,
       "ruijieEGLogoutTime": ruijieEGLogoutTime,
       "ruijieEGMessageType": ruijieEGMessageType,
       "ruijieEGUserStatus": ruijieEGUserStatus,
       "ruijieEGUserDelete": ruijieEGUserDelete,
       "ruijieSMPMIBConformance": ruijieSMPMIBConformance,
       "ruijieSMPMIBCompliances": ruijieSMPMIBCompliances,
       "ruijieDeviceMIBCompliance": ruijieDeviceMIBCompliance,
       "ruijieSMPMIBGroups": ruijieSMPMIBGroups,
       "ruijieSMPServerMibGroup": ruijieSMPServerMibGroup,
       "ruijieSMPClientMibGroup": ruijieSMPClientMibGroup,
       "ruijieSMPPolicyMibGroup": ruijieSMPPolicyMibGroup,
       "ruijieSMPFrameRelayMibGroup": ruijieSMPFrameRelayMibGroup,
       "ruijieSMPTraps": ruijieSMPTraps,
       "ruijieSMPSwitchIP": ruijieSMPSwitchIP,
       "ruijieSMPSwitchInterfaceID": ruijieSMPSwitchInterfaceID,
       "ruijieSMPSwitchInterfaceVLANID": ruijieSMPSwitchInterfaceVLANID,
       "ruijieSMPFrameContentLength": ruijieSMPFrameContentLength,
       "ruijieSMPFrameContent": ruijieSMPFrameContent,
       "ruijieSMPFrameRelayTrap": ruijieSMPFrameRelayTrap,
       "ruijieSMPArpAttackSubnetIP": ruijieSMPArpAttackSubnetIP,
       "ruijieSMPArpAttackSubnetIPNum": ruijieSMPArpAttackSubnetIPNum,
       "ruijieSMPArpAttackInterfaceSlot": ruijieSMPArpAttackInterfaceSlot,
       "ruijieSMPArpAttackInterfacePort": ruijieSMPArpAttackInterfacePort,
       "ruijieSMPArpAttackInterfaceVlanID": ruijieSMPArpAttackInterfaceVlanID,
       "ruijieSMPArpAttackFrameContent": ruijieSMPArpAttackFrameContent,
       "ruijieSMPArpAttackStatus": ruijieSMPArpAttackStatus,
       "ruijieSMPArpAttackCriticalStatus": ruijieSMPArpAttackCriticalStatus,
       "ruijieSMPArpAttackMac": ruijieSMPArpAttackMac,
       "ruijieSMPArpAttackInterfaceIndex": ruijieSMPArpAttackInterfaceIndex,
       "ruijieSMPArpAttackTrap": ruijieSMPArpAttackTrap}
)
