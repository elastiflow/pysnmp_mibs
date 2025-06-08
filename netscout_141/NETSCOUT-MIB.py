# SNMP MIB module (NETSCOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/netscout_141/NETSCOUT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:37:35 2025
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

(EntryStatus,
 OwnerString,
 alarmFallingThreshold,
 alarmIndex,
 alarmRisingThreshold,
 alarmSampleType,
 alarmValue,
 alarmVariable,
 eventDescription) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString",
    "alarmFallingThreshold",
    "alarmIndex",
    "alarmRisingThreshold",
    "alarmSampleType",
    "alarmValue",
    "alarmVariable",
    "eventDescription")

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

netscoutMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 141)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Frontier_ObjectIdentity = ObjectIdentity
frontier = _Frontier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141)
)
_Mibdoc_ObjectIdentity = ObjectIdentity
mibdoc = _Mibdoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1)
)
_Netscout_ObjectIdentity = ObjectIdentity
netscout = _Netscout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1)
)
_Administrative_ObjectIdentity = ObjectIdentity
administrative = _Administrative_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1)
)
_AdminNotificationTable_Object = MibTable
adminNotificationTable = _AdminNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adminNotificationTable.setStatus("current")
_AdminNotificationEntry_Object = MibTableRow
adminNotificationEntry = _AdminNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1)
)
adminNotificationEntry.setIndexNames(
    (0, "NETSCOUT-MIB", "adminNotificationIndex"),
)
if mibBuilder.loadTexts:
    adminNotificationEntry.setStatus("current")


class _AdminNotificationIndex_Type(Integer32):
    """Custom type adminNotificationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdminNotificationIndex_Type.__name__ = "Integer32"
_AdminNotificationIndex_Object = MibTableColumn
adminNotificationIndex = _AdminNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1, 1),
    _AdminNotificationIndex_Type()
)
adminNotificationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNotificationIndex.setStatus("current")


class _AdminNotificationIfIndex_Type(Integer32):
    """Custom type adminNotificationIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdminNotificationIfIndex_Type.__name__ = "Integer32"
_AdminNotificationIfIndex_Object = MibTableColumn
adminNotificationIfIndex = _AdminNotificationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1, 2),
    _AdminNotificationIfIndex_Type()
)
adminNotificationIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationIfIndex.setStatus("current")
_AdminNotificationIpAddr_Type = IpAddress
_AdminNotificationIpAddr_Object = MibTableColumn
adminNotificationIpAddr = _AdminNotificationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1, 3),
    _AdminNotificationIpAddr_Type()
)
adminNotificationIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationIpAddr.setStatus("current")


class _AdminNotificationCommunity_Type(OctetString):
    """Custom type adminNotificationCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AdminNotificationCommunity_Type.__name__ = "OctetString"
_AdminNotificationCommunity_Object = MibTableColumn
adminNotificationCommunity = _AdminNotificationCommunity_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1, 4),
    _AdminNotificationCommunity_Type()
)
adminNotificationCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationCommunity.setStatus("current")


class _AdminNotificationTrapMask_Type(Integer32):
    """Custom type adminNotificationTrapMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdminNotificationTrapMask_Type.__name__ = "Integer32"
_AdminNotificationTrapMask_Object = MibTableColumn
adminNotificationTrapMask = _AdminNotificationTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1, 5),
    _AdminNotificationTrapMask_Type()
)
adminNotificationTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationTrapMask.setStatus("current")
_AdminNotificationOwner_Type = OwnerString
_AdminNotificationOwner_Object = MibTableColumn
adminNotificationOwner = _AdminNotificationOwner_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1, 6),
    _AdminNotificationOwner_Type()
)
adminNotificationOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationOwner.setStatus("current")
_AdminNotificationStatus_Type = EntryStatus
_AdminNotificationStatus_Object = MibTableColumn
adminNotificationStatus = _AdminNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 1, 1, 1, 7),
    _AdminNotificationStatus_Type()
)
adminNotificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationStatus.setStatus("current")
_Transaction_ObjectIdentity = ObjectIdentity
transaction = _Transaction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 2)
)
_NsTraps_ObjectIdentity = ObjectIdentity
nsTraps = _NsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 3)
)
_Capabilities_ObjectIdentity = ObjectIdentity
capabilities = _Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 4)
)


class _NetscoutProbeCapabilities_Type(Bits):
    """Custom type netscoutProbeCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("admin", 0),
          ("console", 1),
          ("pvar", 2),
          ("art", 3),
          ("vlanIf", 4),
          ("dlciIf", 5),
          ("elanIf", 6),
          ("vcIf", 7),
          ("routeIf", 8),
          ("flashSize", 9),
          ("qos", 10),
          ("dsmon", 11),
          ("httpcrt", 12),
          ("bigflashSize", 13),
          ("voip", 14),
          ("urt", 15),
          ("site", 16))
    )

_NetscoutProbeCapabilities_Type.__name__ = "Bits"
_NetscoutProbeCapabilities_Object = MibScalar
netscoutProbeCapabilities = _NetscoutProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 4, 1),
    _NetscoutProbeCapabilities_Type()
)
netscoutProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netscoutProbeCapabilities.setStatus("current")
_Probe5100_ObjectIdentity = ObjectIdentity
probe5100 = _Probe5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 5100)
)
_Probe6010_ObjectIdentity = ObjectIdentity
probe6010 = _Probe6010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 6010)
)
_Probe6020_ObjectIdentity = ObjectIdentity
probe6020 = _Probe6020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 6020)
)
_Probe6030_ObjectIdentity = ObjectIdentity
probe6030 = _Probe6030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 6030)
)
_Probe6040_ObjectIdentity = ObjectIdentity
probe6040 = _Probe6040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 6040)
)
_Probe6050_ObjectIdentity = ObjectIdentity
probe6050 = _Probe6050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 6050)
)
_Probe6060_ObjectIdentity = ObjectIdentity
probe6060 = _Probe6060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 6060)
)
_Probe6070_ObjectIdentity = ObjectIdentity
probe6070 = _Probe6070_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 6070)
)
_Probe7100_ObjectIdentity = ObjectIdentity
probe7100 = _Probe7100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 7100)
)
_Probe7200_ObjectIdentity = ObjectIdentity
probe7200 = _Probe7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 7200)
)
_Probe7300_ObjectIdentity = ObjectIdentity
probe7300 = _Probe7300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 7300)
)
_Probe7400_ObjectIdentity = ObjectIdentity
probe7400 = _Probe7400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 7400)
)
_Probe7500_ObjectIdentity = ObjectIdentity
probe7500 = _Probe7500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 7500)
)
_Probe7510_ObjectIdentity = ObjectIdentity
probe7510 = _Probe7510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 7510)
)
_Probe8100_ObjectIdentity = ObjectIdentity
probe8100 = _Probe8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 8100)
)
_Mibdoc2_ObjectIdentity = ObjectIdentity
mibdoc2 = _Mibdoc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2)
)
_Netscout2_ObjectIdentity = ObjectIdentity
netscout2 = _Netscout2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1)
)
_Hostprot_ObjectIdentity = ObjectIdentity
hostprot = _Hostprot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 1)
)
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2)
)
_ConsoleControlTable_Object = MibTable
consoleControlTable = _ConsoleControlTable_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    consoleControlTable.setStatus("current")
_ConsoleControlEntry_Object = MibTableRow
consoleControlEntry = _ConsoleControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1)
)
consoleControlEntry.setIndexNames(
    (0, "NETSCOUT-MIB", "consoleControlIndex"),
)
if mibBuilder.loadTexts:
    consoleControlEntry.setStatus("current")


class _ConsoleControlIndex_Type(Integer32):
    """Custom type consoleControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConsoleControlIndex_Type.__name__ = "Integer32"
_ConsoleControlIndex_Object = MibTableColumn
consoleControlIndex = _ConsoleControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 1),
    _ConsoleControlIndex_Type()
)
consoleControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleControlIndex.setStatus("current")


class _ConsolePassword_Type(DisplayString):
    """Custom type consolePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ConsolePassword_Type.__name__ = "DisplayString"
_ConsolePassword_Object = MibTableColumn
consolePassword = _ConsolePassword_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 2),
    _ConsolePassword_Type()
)
consolePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePassword.setStatus("current")


class _ConsoleCommand_Type(DisplayString):
    """Custom type consoleCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ConsoleCommand_Type.__name__ = "DisplayString"
_ConsoleCommand_Object = MibTableColumn
consoleCommand = _ConsoleCommand_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 3),
    _ConsoleCommand_Type()
)
consoleCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleCommand.setStatus("current")


class _ConsoleTimeout_Type(Integer32):
    """Custom type consoleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConsoleTimeout_Type.__name__ = "Integer32"
_ConsoleTimeout_Object = MibTableColumn
consoleTimeout = _ConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 4),
    _ConsoleTimeout_Type()
)
consoleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleTimeout.setStatus("current")


class _ConsoleMode_Type(Integer32):
    """Custom type consoleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cmdline", 1),
          ("menu", 2))
    )


_ConsoleMode_Type.__name__ = "Integer32"
_ConsoleMode_Object = MibTableColumn
consoleMode = _ConsoleMode_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 5),
    _ConsoleMode_Type()
)
consoleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleMode.setStatus("current")


class _ConsoleState_Type(Integer32):
    """Custom type consoleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("busy", 2))
    )


_ConsoleState_Type.__name__ = "Integer32"
_ConsoleState_Object = MibTableColumn
consoleState = _ConsoleState_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 6),
    _ConsoleState_Type()
)
consoleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleState.setStatus("current")
_ConsoleControlOwner_Type = OwnerString
_ConsoleControlOwner_Object = MibTableColumn
consoleControlOwner = _ConsoleControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 7),
    _ConsoleControlOwner_Type()
)
consoleControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleControlOwner.setStatus("current")
_ConsoleControlStatus_Type = EntryStatus
_ConsoleControlStatus_Object = MibTableColumn
consoleControlStatus = _ConsoleControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 1, 1, 8),
    _ConsoleControlStatus_Type()
)
consoleControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleControlStatus.setStatus("current")
_ConsoleTable_Object = MibTable
consoleTable = _ConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    consoleTable.setStatus("current")
_ConsoleEntry_Object = MibTableRow
consoleEntry = _ConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 2, 1)
)
consoleEntry.setIndexNames(
    (0, "NETSCOUT-MIB", "consoleIndex"),
    (0, "NETSCOUT-MIB", "consoleReplyLineID"),
)
if mibBuilder.loadTexts:
    consoleEntry.setStatus("current")


class _ConsoleIndex_Type(Integer32):
    """Custom type consoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConsoleIndex_Type.__name__ = "Integer32"
_ConsoleIndex_Object = MibTableColumn
consoleIndex = _ConsoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 2, 1, 1),
    _ConsoleIndex_Type()
)
consoleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleIndex.setStatus("current")


class _ConsoleReplyLineID_Type(Integer32):
    """Custom type consoleReplyLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConsoleReplyLineID_Type.__name__ = "Integer32"
_ConsoleReplyLineID_Object = MibTableColumn
consoleReplyLineID = _ConsoleReplyLineID_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 2, 1, 2),
    _ConsoleReplyLineID_Type()
)
consoleReplyLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleReplyLineID.setStatus("current")


class _ConsoleReplyLineData_Type(DisplayString):
    """Custom type consoleReplyLineData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ConsoleReplyLineData_Type.__name__ = "DisplayString"
_ConsoleReplyLineData_Object = MibTableColumn
consoleReplyLineData = _ConsoleReplyLineData_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 2, 2, 1, 3),
    _ConsoleReplyLineData_Type()
)
consoleReplyLineData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleReplyLineData.setStatus("current")
_Pvar_ObjectIdentity = ObjectIdentity
pvar = _Pvar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3)
)
_PvarTable_Object = MibTable
pvarTable = _PvarTable_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pvarTable.setStatus("current")
_PvarEntry_Object = MibTableRow
pvarEntry = _PvarEntry_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1)
)
pvarEntry.setIndexNames(
    (0, "NETSCOUT-MIB", "pvarControlIndex"),
)
if mibBuilder.loadTexts:
    pvarEntry.setStatus("current")


class _PvarControlIndex_Type(Integer32):
    """Custom type pvarControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvarControlIndex_Type.__name__ = "Integer32"
_PvarControlIndex_Object = MibTableColumn
pvarControlIndex = _PvarControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 1),
    _PvarControlIndex_Type()
)
pvarControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvarControlIndex.setStatus("current")
_PvarOid_Type = ObjectIdentifier
_PvarOid_Object = MibTableColumn
pvarOid = _PvarOid_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 2),
    _PvarOid_Type()
)
pvarOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarOid.setStatus("current")
_PvarHome_Type = OctetString
_PvarHome_Object = MibTableColumn
pvarHome = _PvarHome_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 3),
    _PvarHome_Type()
)
pvarHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarHome.setStatus("current")


class _PvarUpdateInterval_Type(Integer32):
    """Custom type pvarUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PvarUpdateInterval_Type.__name__ = "Integer32"
_PvarUpdateInterval_Object = MibTableColumn
pvarUpdateInterval = _PvarUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 4),
    _PvarUpdateInterval_Type()
)
pvarUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarUpdateInterval.setStatus("current")


class _PvarType_Type(Integer32):
    """Custom type pvarType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ping", 1),
          ("dupip", 2),
          ("mib", 3))
    )


_PvarType_Type.__name__ = "Integer32"
_PvarType_Object = MibTableColumn
pvarType = _PvarType_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 5),
    _PvarType_Type()
)
pvarType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarType.setStatus("current")


class _PvarValue_Type(Integer32):
    """Custom type pvarValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PvarValue_Type.__name__ = "Integer32"
_PvarValue_Object = MibTableColumn
pvarValue = _PvarValue_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 6),
    _PvarValue_Type()
)
pvarValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvarValue.setStatus("current")


class _PvarLastUpdateTime_Type(Integer32):
    """Custom type pvarLastUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PvarLastUpdateTime_Type.__name__ = "Integer32"
_PvarLastUpdateTime_Object = MibTableColumn
pvarLastUpdateTime = _PvarLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 7),
    _PvarLastUpdateTime_Type()
)
pvarLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvarLastUpdateTime.setStatus("current")


class _PvarUpdateFailures_Type(Integer32):
    """Custom type pvarUpdateFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PvarUpdateFailures_Type.__name__ = "Integer32"
_PvarUpdateFailures_Object = MibTableColumn
pvarUpdateFailures = _PvarUpdateFailures_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 8),
    _PvarUpdateFailures_Type()
)
pvarUpdateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvarUpdateFailures.setStatus("current")


class _PvarCommunity_Type(OctetString):
    """Custom type pvarCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvarCommunity_Type.__name__ = "OctetString"
_PvarCommunity_Object = MibTableColumn
pvarCommunity = _PvarCommunity_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 9),
    _PvarCommunity_Type()
)
pvarCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarCommunity.setStatus("current")


class _PvarDescription_Type(DisplayString):
    """Custom type pvarDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PvarDescription_Type.__name__ = "DisplayString"
_PvarDescription_Object = MibTableColumn
pvarDescription = _PvarDescription_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 10),
    _PvarDescription_Type()
)
pvarDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarDescription.setStatus("current")
_PvarOwner_Type = OwnerString
_PvarOwner_Object = MibTableColumn
pvarOwner = _PvarOwner_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 11),
    _PvarOwner_Type()
)
pvarOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarOwner.setStatus("current")
_PvarStatus_Type = EntryStatus
_PvarStatus_Object = MibTableColumn
pvarStatus = _PvarStatus_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 12),
    _PvarStatus_Type()
)
pvarStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarStatus.setStatus("current")


class _PvarTrapType_Type(Integer32):
    """Custom type pvarTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PvarTrapType_Type.__name__ = "Integer32"
_PvarTrapType_Object = MibTableColumn
pvarTrapType = _PvarTrapType_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 13),
    _PvarTrapType_Type()
)
pvarTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarTrapType.setStatus("current")


class _PvarRisingTrapNumber_Type(Integer32):
    """Custom type pvarRisingTrapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PvarRisingTrapNumber_Type.__name__ = "Integer32"
_PvarRisingTrapNumber_Object = MibTableColumn
pvarRisingTrapNumber = _PvarRisingTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 14),
    _PvarRisingTrapNumber_Type()
)
pvarRisingTrapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarRisingTrapNumber.setStatus("current")


class _PvarFallingTrapNumber_Type(Integer32):
    """Custom type pvarFallingTrapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PvarFallingTrapNumber_Type.__name__ = "Integer32"
_PvarFallingTrapNumber_Object = MibTableColumn
pvarFallingTrapNumber = _PvarFallingTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 15),
    _PvarFallingTrapNumber_Type()
)
pvarFallingTrapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarFallingTrapNumber.setStatus("current")
_PvarTrapSysOid_Type = ObjectIdentifier
_PvarTrapSysOid_Object = MibTableColumn
pvarTrapSysOid = _PvarTrapSysOid_Object(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 3, 1, 1, 16),
    _PvarTrapSysOid_Type()
)
pvarTrapSysOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvarTrapSysOid.setStatus("current")
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 4)
)
_Art_ObjectIdentity = ObjectIdentity
art = _Art_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 2, 1, 5)
)
_NetscoutConformance_ObjectIdentity = ObjectIdentity
netscoutConformance = _NetscoutConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 5)
)
_NetscoutMIBCompliances_ObjectIdentity = ObjectIdentity
netscoutMIBCompliances = _NetscoutMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 5, 1)
)
_NetscoutMIBGroups_ObjectIdentity = ObjectIdentity
netscoutMIBGroups = _NetscoutMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 5, 2)
)
_ProbeMgmt_ObjectIdentity = ObjectIdentity
probeMgmt = _ProbeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 6)
)


class _ProbeMgmtOwner_Type(OctetString):
    """Custom type probeMgmtOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_ProbeMgmtOwner_Type.__name__ = "OctetString"
_ProbeMgmtOwner_Object = MibScalar
probeMgmtOwner = _ProbeMgmtOwner_Object(
    (1, 3, 6, 1, 4, 1, 141, 6, 1),
    _ProbeMgmtOwner_Type()
)
probeMgmtOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeMgmtOwner.setStatus("current")
_ActiveAgentTest_ObjectIdentity = ObjectIdentity
activeAgentTest = _ActiveAgentTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 7)
)


class _ActiveAgentTestStart_Type(OctetString):
    """Custom type activeAgentTestStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ActiveAgentTestStart_Type.__name__ = "OctetString"
_ActiveAgentTestStart_Object = MibScalar
activeAgentTestStart = _ActiveAgentTestStart_Object(
    (1, 3, 6, 1, 4, 1, 141, 7, 1),
    _ActiveAgentTestStart_Type()
)
activeAgentTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAgentTestStart.setStatus("current")


class _ActiveAgentTestStop_Type(OctetString):
    """Custom type activeAgentTestStop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ActiveAgentTestStop_Type.__name__ = "OctetString"
_ActiveAgentTestStop_Object = MibScalar
activeAgentTestStop = _ActiveAgentTestStop_Object(
    (1, 3, 6, 1, 4, 1, 141, 7, 2),
    _ActiveAgentTestStop_Type()
)
activeAgentTestStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAgentTestStop.setStatus("current")
_NsServerGroup_ObjectIdentity = ObjectIdentity
nsServerGroup = _NsServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 141, 50)
)

# Managed Objects groups

netscoutProbeCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 141, 5, 2, 1)
)
netscoutProbeCapabilitiesGroup.setObjects(
    ("NETSCOUT-MIB", "netscoutProbeCapabilities")
)
if mibBuilder.loadTexts:
    netscoutProbeCapabilitiesGroup.setStatus("current")

adminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 141, 5, 2, 2)
)
adminGroup.setObjects(
      *(("NETSCOUT-MIB", "adminNotificationIndex"),
        ("NETSCOUT-MIB", "adminNotificationIfIndex"),
        ("NETSCOUT-MIB", "adminNotificationIpAddr"),
        ("NETSCOUT-MIB", "adminNotificationCommunity"),
        ("NETSCOUT-MIB", "adminNotificationTrapMask"),
        ("NETSCOUT-MIB", "adminNotificationOwner"),
        ("NETSCOUT-MIB", "adminNotificationStatus"))
)
if mibBuilder.loadTexts:
    adminGroup.setStatus("current")

consoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 141, 5, 2, 4)
)
consoleGroup.setObjects(
      *(("NETSCOUT-MIB", "consoleControlIndex"),
        ("NETSCOUT-MIB", "consolePassword"),
        ("NETSCOUT-MIB", "consoleCommand"),
        ("NETSCOUT-MIB", "consoleTimeout"),
        ("NETSCOUT-MIB", "consoleMode"),
        ("NETSCOUT-MIB", "consoleState"),
        ("NETSCOUT-MIB", "consoleControlOwner"),
        ("NETSCOUT-MIB", "consoleControlStatus"),
        ("NETSCOUT-MIB", "consoleIndex"),
        ("NETSCOUT-MIB", "consoleReplyLineID"),
        ("NETSCOUT-MIB", "consoleReplyLineData"))
)
if mibBuilder.loadTexts:
    consoleGroup.setStatus("current")

pvarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 141, 5, 2, 5)
)
pvarGroup.setObjects(
      *(("NETSCOUT-MIB", "pvarControlIndex"),
        ("NETSCOUT-MIB", "pvarOid"),
        ("NETSCOUT-MIB", "pvarHome"),
        ("NETSCOUT-MIB", "pvarUpdateInterval"),
        ("NETSCOUT-MIB", "pvarType"),
        ("NETSCOUT-MIB", "pvarValue"),
        ("NETSCOUT-MIB", "pvarLastUpdateTime"),
        ("NETSCOUT-MIB", "pvarUpdateFailures"),
        ("NETSCOUT-MIB", "pvarCommunity"),
        ("NETSCOUT-MIB", "pvarDescription"),
        ("NETSCOUT-MIB", "pvarOwner"),
        ("NETSCOUT-MIB", "pvarStatus"),
        ("NETSCOUT-MIB", "pvarTrapType"),
        ("NETSCOUT-MIB", "pvarRisingTrapNumber"),
        ("NETSCOUT-MIB", "pvarFallingTrapNumber"),
        ("NETSCOUT-MIB", "pvarTrapSysOid"))
)
if mibBuilder.loadTexts:
    pvarGroup.setStatus("current")


# Notification objects

RisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 3, 1)
)
RisingAlarm.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmSampleType"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmRisingThreshold"),
        ("RMON-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    RisingAlarm.setStatus(
        "mandatory"
    )

FallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 3, 2)
)
FallingAlarm.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmVariable"),
        ("RMON-MIB", "alarmSampleType"),
        ("RMON-MIB", "alarmValue"),
        ("RMON-MIB", "alarmFallingThreshold"),
        ("RMON-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    FallingAlarm.setStatus(
        "current"
    )

respAvailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 141, 1, 1, 3, 3)
)
respAvailAlarm.setObjects(
    ("NETSCOUT-MIB", "probeMgmtOwner")
)
if mibBuilder.loadTexts:
    respAvailAlarm.setStatus(
        "current"
    )


# Notifications groups

alarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 141, 5, 2, 3)
)
alarmGroup.setObjects(
      *(("NETSCOUT-MIB", "RisingAlarm"),
        ("NETSCOUT-MIB", "FallingAlarm"))
)
if mibBuilder.loadTexts:
    alarmGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

netscoutMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 141, 5, 1, 1)
)
netscoutMIBCompliance.setObjects(
      *(("NETSCOUT-MIB", "netscoutProbeCapabilitiesGroup"),
        ("NETSCOUT-MIB", "adminGroup"),
        ("NETSCOUT-MIB", "alarmGroup"),
        ("NETSCOUT-MIB", "consoleGroup"),
        ("NETSCOUT-MIB", "pvarGroup"))
)
if mibBuilder.loadTexts:
    netscoutMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCOUT-MIB",
    **{"netscoutMib": netscoutMib,
       "frontier": frontier,
       "mibdoc": mibdoc,
       "netscout": netscout,
       "administrative": administrative,
       "adminNotificationTable": adminNotificationTable,
       "adminNotificationEntry": adminNotificationEntry,
       "adminNotificationIndex": adminNotificationIndex,
       "adminNotificationIfIndex": adminNotificationIfIndex,
       "adminNotificationIpAddr": adminNotificationIpAddr,
       "adminNotificationCommunity": adminNotificationCommunity,
       "adminNotificationTrapMask": adminNotificationTrapMask,
       "adminNotificationOwner": adminNotificationOwner,
       "adminNotificationStatus": adminNotificationStatus,
       "transaction": transaction,
       "nsTraps": nsTraps,
       "RisingAlarm": RisingAlarm,
       "FallingAlarm": FallingAlarm,
       "respAvailAlarm": respAvailAlarm,
       "capabilities": capabilities,
       "netscoutProbeCapabilities": netscoutProbeCapabilities,
       "probe5100": probe5100,
       "probe6010": probe6010,
       "probe6020": probe6020,
       "probe6030": probe6030,
       "probe6040": probe6040,
       "probe6050": probe6050,
       "probe6060": probe6060,
       "probe6070": probe6070,
       "probe7100": probe7100,
       "probe7200": probe7200,
       "probe7300": probe7300,
       "probe7400": probe7400,
       "probe7500": probe7500,
       "probe7510": probe7510,
       "probe8100": probe8100,
       "mibdoc2": mibdoc2,
       "netscout2": netscout2,
       "hostprot": hostprot,
       "console": console,
       "consoleControlTable": consoleControlTable,
       "consoleControlEntry": consoleControlEntry,
       "consoleControlIndex": consoleControlIndex,
       "consolePassword": consolePassword,
       "consoleCommand": consoleCommand,
       "consoleTimeout": consoleTimeout,
       "consoleMode": consoleMode,
       "consoleState": consoleState,
       "consoleControlOwner": consoleControlOwner,
       "consoleControlStatus": consoleControlStatus,
       "consoleTable": consoleTable,
       "consoleEntry": consoleEntry,
       "consoleIndex": consoleIndex,
       "consoleReplyLineID": consoleReplyLineID,
       "consoleReplyLineData": consoleReplyLineData,
       "pvar": pvar,
       "pvarTable": pvarTable,
       "pvarEntry": pvarEntry,
       "pvarControlIndex": pvarControlIndex,
       "pvarOid": pvarOid,
       "pvarHome": pvarHome,
       "pvarUpdateInterval": pvarUpdateInterval,
       "pvarType": pvarType,
       "pvarValue": pvarValue,
       "pvarLastUpdateTime": pvarLastUpdateTime,
       "pvarUpdateFailures": pvarUpdateFailures,
       "pvarCommunity": pvarCommunity,
       "pvarDescription": pvarDescription,
       "pvarOwner": pvarOwner,
       "pvarStatus": pvarStatus,
       "pvarTrapType": pvarTrapType,
       "pvarRisingTrapNumber": pvarRisingTrapNumber,
       "pvarFallingTrapNumber": pvarFallingTrapNumber,
       "pvarTrapSysOid": pvarTrapSysOid,
       "server": server,
       "art": art,
       "netscoutConformance": netscoutConformance,
       "netscoutMIBCompliances": netscoutMIBCompliances,
       "netscoutMIBCompliance": netscoutMIBCompliance,
       "netscoutMIBGroups": netscoutMIBGroups,
       "netscoutProbeCapabilitiesGroup": netscoutProbeCapabilitiesGroup,
       "adminGroup": adminGroup,
       "alarmGroup": alarmGroup,
       "consoleGroup": consoleGroup,
       "pvarGroup": pvarGroup,
       "probeMgmt": probeMgmt,
       "probeMgmtOwner": probeMgmtOwner,
       "activeAgentTest": activeAgentTest,
       "activeAgentTestStart": activeAgentTestStart,
       "activeAgentTestStop": activeAgentTestStop,
       "nsServerGroup": nsServerGroup}
)
