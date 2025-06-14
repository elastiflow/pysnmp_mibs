# SNMP MIB module (CISCOSB-rndMng) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-rndMng.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:13:48 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rndMng = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1)
)
if mibBuilder.loadTexts:
    rndMng.setRevisions(
        ("2012-12-04 00:00",
         "2012-04-04 00:00",
         "2009-02-24 00:00",
         "2007-10-24 00:00",
         "2006-06-20 00:00",
         "2004-06-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RndSysId_Type = Integer32
_RndSysId_Object = MibScalar
rndSysId = _RndSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 1),
    _RndSysId_Type()
)
rndSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndSysId.setStatus("current")


class _RndAction_Type(Integer32):
    """Custom type rndAction based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("sendNetworkTab", 2),
          ("deleteNetworkTab", 3),
          ("sendRoutingTab", 4),
          ("deleteRoutingTab", 5),
          ("sendLanTab", 6),
          ("deleteLanTab", 7),
          ("deleteArpTab", 8),
          ("sendArpTab", 9),
          ("deleteRouteTab", 10),
          ("sendRouteTab", 11),
          ("backupSPFRoutingTab", 12),
          ("backupIPRoutingTab", 13),
          ("backupNetworkTab", 14),
          ("backupLanTab", 15),
          ("backupArpTab", 16),
          ("backupIPXRipTab", 17),
          ("backupIPXSAPTab", 18),
          ("resetStartupCDB", 19),
          ("eraseStartupCDB", 20),
          ("deleteZeroHopRoutingAllocTab", 21),
          ("slipDisconnect", 22),
          ("deleteDynamicLanTab", 23),
          ("eraseRunningCDB", 24),
          ("copyStartupToRunning", 25),
          ("none", 26),
          ("resetToFactoryDefaults", 27))
    )


_RndAction_Type.__name__ = "Integer32"
_RndAction_Object = MibScalar
rndAction = _RndAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 2),
    _RndAction_Type()
)
rndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAction.setStatus("current")
_RndFileName_Type = OctetString
_RndFileName_Object = MibScalar
rndFileName = _RndFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 3),
    _RndFileName_Type()
)
rndFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFileName.setStatus("current")


class _RlSnmpVersionSupported_Type(OctetString):
    """Custom type rlSnmpVersionSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_RlSnmpVersionSupported_Type.__name__ = "OctetString"
_RlSnmpVersionSupported_Object = MibScalar
rlSnmpVersionSupported = _RlSnmpVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 4),
    _RlSnmpVersionSupported_Type()
)
rlSnmpVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpVersionSupported.setStatus("current")
_RlSnmpMibVersion_Type = Integer32
_RlSnmpMibVersion_Object = MibScalar
rlSnmpMibVersion = _RlSnmpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 5),
    _RlSnmpMibVersion_Type()
)
rlSnmpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpMibVersion.setStatus("current")


class _RlCpuUtilEnable_Type(TruthValue):
    """Custom type rlCpuUtilEnable based on TruthValue"""
    defaultValue = 1


_RlCpuUtilEnable_Type.__name__ = "TruthValue"
_RlCpuUtilEnable_Object = MibScalar
rlCpuUtilEnable = _RlCpuUtilEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 6),
    _RlCpuUtilEnable_Type()
)
rlCpuUtilEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCpuUtilEnable.setStatus("current")


class _RlCpuUtilDuringLastSecond_Type(Integer32):
    """Custom type rlCpuUtilDuringLastSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_RlCpuUtilDuringLastSecond_Type.__name__ = "Integer32"
_RlCpuUtilDuringLastSecond_Object = MibScalar
rlCpuUtilDuringLastSecond = _RlCpuUtilDuringLastSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 7),
    _RlCpuUtilDuringLastSecond_Type()
)
rlCpuUtilDuringLastSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuUtilDuringLastSecond.setStatus("current")


class _RlCpuUtilDuringLastMinute_Type(Integer32):
    """Custom type rlCpuUtilDuringLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_RlCpuUtilDuringLastMinute_Type.__name__ = "Integer32"
_RlCpuUtilDuringLastMinute_Object = MibScalar
rlCpuUtilDuringLastMinute = _RlCpuUtilDuringLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 8),
    _RlCpuUtilDuringLastMinute_Type()
)
rlCpuUtilDuringLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuUtilDuringLastMinute.setStatus("current")


class _RlCpuUtilDuringLast5Minutes_Type(Integer32):
    """Custom type rlCpuUtilDuringLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_RlCpuUtilDuringLast5Minutes_Type.__name__ = "Integer32"
_RlCpuUtilDuringLast5Minutes_Object = MibScalar
rlCpuUtilDuringLast5Minutes = _RlCpuUtilDuringLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 9),
    _RlCpuUtilDuringLast5Minutes_Type()
)
rlCpuUtilDuringLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuUtilDuringLast5Minutes.setStatus("current")
_RlRebootDelay_Type = TimeTicks
_RlRebootDelay_Object = MibScalar
rlRebootDelay = _RlRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 10),
    _RlRebootDelay_Type()
)
rlRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRebootDelay.setStatus("current")
_RlGroupManagement_ObjectIdentity = ObjectIdentity
rlGroupManagement = _RlGroupManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11)
)


class _RlGroupMngQuery_Type(Integer32):
    """Custom type rlGroupMngQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("query", 1),
          ("idle", 2))
    )


_RlGroupMngQuery_Type.__name__ = "Integer32"
_RlGroupMngQuery_Object = MibScalar
rlGroupMngQuery = _RlGroupMngQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 1),
    _RlGroupMngQuery_Type()
)
rlGroupMngQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGroupMngQuery.setStatus("current")


class _RlGroupMngQueryPeriod_Type(Integer32):
    """Custom type rlGroupMngQueryPeriod based on Integer32"""
    defaultValue = 0


_RlGroupMngQueryPeriod_Type.__name__ = "Integer32"
_RlGroupMngQueryPeriod_Object = MibScalar
rlGroupMngQueryPeriod = _RlGroupMngQueryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 2),
    _RlGroupMngQueryPeriod_Type()
)
rlGroupMngQueryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGroupMngQueryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    rlGroupMngQueryPeriod.setUnits("seconds")
_RlGroupMngLastUpdate_Type = TimeTicks
_RlGroupMngLastUpdate_Object = MibScalar
rlGroupMngLastUpdate = _RlGroupMngLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 3),
    _RlGroupMngLastUpdate_Type()
)
rlGroupMngLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngLastUpdate.setStatus("current")
_RlGroupMngDevicesTable_Object = MibTable
rlGroupMngDevicesTable = _RlGroupMngDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4)
)
if mibBuilder.loadTexts:
    rlGroupMngDevicesTable.setStatus("current")
_RlGroupMngDeviceEntry_Object = MibTableRow
rlGroupMngDeviceEntry = _RlGroupMngDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1)
)
rlGroupMngDeviceEntry.setIndexNames(
    (0, "CISCOSB-rndMng", "rlGroupMngDeviceIdType"),
    (0, "CISCOSB-rndMng", "rlGroupMngDeviceId"),
    (0, "CISCOSB-rndMng", "rlGroupMngSubdevice"),
)
if mibBuilder.loadTexts:
    rlGroupMngDeviceEntry.setStatus("current")
_RlGroupMngDeviceIdType_Type = InetAddressType
_RlGroupMngDeviceIdType_Object = MibTableColumn
rlGroupMngDeviceIdType = _RlGroupMngDeviceIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 1),
    _RlGroupMngDeviceIdType_Type()
)
rlGroupMngDeviceIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlGroupMngDeviceIdType.setStatus("current")
_RlGroupMngDeviceId_Type = InetAddress
_RlGroupMngDeviceId_Object = MibTableColumn
rlGroupMngDeviceId = _RlGroupMngDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 2),
    _RlGroupMngDeviceId_Type()
)
rlGroupMngDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlGroupMngDeviceId.setStatus("current")
_RlGroupMngSubdevice_Type = Integer32
_RlGroupMngSubdevice_Object = MibTableColumn
rlGroupMngSubdevice = _RlGroupMngSubdevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 3),
    _RlGroupMngSubdevice_Type()
)
rlGroupMngSubdevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlGroupMngSubdevice.setStatus("current")
_RlGroupMngDeviceDescription_Type = DisplayString
_RlGroupMngDeviceDescription_Object = MibTableColumn
rlGroupMngDeviceDescription = _RlGroupMngDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 4),
    _RlGroupMngDeviceDescription_Type()
)
rlGroupMngDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceDescription.setStatus("current")
_RlGroupMngGroupMngEnabled_Type = TruthValue
_RlGroupMngGroupMngEnabled_Object = MibTableColumn
rlGroupMngGroupMngEnabled = _RlGroupMngGroupMngEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 5),
    _RlGroupMngGroupMngEnabled_Type()
)
rlGroupMngGroupMngEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngGroupMngEnabled.setStatus("current")
_RlGroupMngGroupLLDPDeviceId_Type = DisplayString
_RlGroupMngGroupLLDPDeviceId_Object = MibTableColumn
rlGroupMngGroupLLDPDeviceId = _RlGroupMngGroupLLDPDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 6),
    _RlGroupMngGroupLLDPDeviceId_Type()
)
rlGroupMngGroupLLDPDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngGroupLLDPDeviceId.setStatus("current")
_RlGroupMngDeviceVendor_Type = DisplayString
_RlGroupMngDeviceVendor_Object = MibTableColumn
rlGroupMngDeviceVendor = _RlGroupMngDeviceVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 7),
    _RlGroupMngDeviceVendor_Type()
)
rlGroupMngDeviceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceVendor.setStatus("current")
_RlGroupMngDeviceAdvertisedCachingTime_Type = Integer32
_RlGroupMngDeviceAdvertisedCachingTime_Object = MibTableColumn
rlGroupMngDeviceAdvertisedCachingTime = _RlGroupMngDeviceAdvertisedCachingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 8),
    _RlGroupMngDeviceAdvertisedCachingTime_Type()
)
rlGroupMngDeviceAdvertisedCachingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceAdvertisedCachingTime.setStatus("current")
if mibBuilder.loadTexts:
    rlGroupMngDeviceAdvertisedCachingTime.setUnits("seconds")
_RlGroupMngDeviceLocationURL_Type = DisplayString
_RlGroupMngDeviceLocationURL_Object = MibTableColumn
rlGroupMngDeviceLocationURL = _RlGroupMngDeviceLocationURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 9),
    _RlGroupMngDeviceLocationURL_Type()
)
rlGroupMngDeviceLocationURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceLocationURL.setStatus("current")
if mibBuilder.loadTexts:
    rlGroupMngDeviceLocationURL.setUnits("seconds")
_RlGroupMngDeviceLastSeen_Type = TimeTicks
_RlGroupMngDeviceLastSeen_Object = MibTableColumn
rlGroupMngDeviceLastSeen = _RlGroupMngDeviceLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 11, 4, 1, 10),
    _RlGroupMngDeviceLastSeen_Type()
)
rlGroupMngDeviceLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceLastSeen.setStatus("current")
_RlRunningCDBequalToStartupCDB_Type = TruthValue
_RlRunningCDBequalToStartupCDB_Object = MibScalar
rlRunningCDBequalToStartupCDB = _RlRunningCDBequalToStartupCDB_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 13),
    _RlRunningCDBequalToStartupCDB_Type()
)
rlRunningCDBequalToStartupCDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRunningCDBequalToStartupCDB.setStatus("current")
_RlClearMib_Type = DisplayString
_RlClearMib_Object = MibScalar
rlClearMib = _RlClearMib_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 14),
    _RlClearMib_Type()
)
rlClearMib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlClearMib.setStatus("current")


class _RlScheduledReload_Type(DisplayString):
    """Custom type rlScheduledReload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RlScheduledReload_Type.__name__ = "DisplayString"
_RlScheduledReload_Object = MibScalar
rlScheduledReload = _RlScheduledReload_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 15),
    _RlScheduledReload_Type()
)
rlScheduledReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlScheduledReload.setStatus("current")


class _RlScheduledReloadPendingDate_Type(DisplayString):
    """Custom type rlScheduledReloadPendingDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_RlScheduledReloadPendingDate_Type.__name__ = "DisplayString"
_RlScheduledReloadPendingDate_Object = MibScalar
rlScheduledReloadPendingDate = _RlScheduledReloadPendingDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 16),
    _RlScheduledReloadPendingDate_Type()
)
rlScheduledReloadPendingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlScheduledReloadPendingDate.setStatus("current")


class _RlScheduledReloadApprovedDate_Type(DisplayString):
    """Custom type rlScheduledReloadApprovedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_RlScheduledReloadApprovedDate_Type.__name__ = "DisplayString"
_RlScheduledReloadApprovedDate_Object = MibScalar
rlScheduledReloadApprovedDate = _RlScheduledReloadApprovedDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 17),
    _RlScheduledReloadApprovedDate_Type()
)
rlScheduledReloadApprovedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlScheduledReloadApprovedDate.setStatus("current")
_RlScheduledReloadCommit_Type = TruthValue
_RlScheduledReloadCommit_Object = MibScalar
rlScheduledReloadCommit = _RlScheduledReloadCommit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 18),
    _RlScheduledReloadCommit_Type()
)
rlScheduledReloadCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlScheduledReloadCommit.setStatus("current")
_RlSysNameTable_Object = MibTable
rlSysNameTable = _RlSysNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 19)
)
if mibBuilder.loadTexts:
    rlSysNameTable.setStatus("current")
_RlSysNameEntry_Object = MibTableRow
rlSysNameEntry = _RlSysNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 19, 1)
)
rlSysNameEntry.setIndexNames(
    (0, "CISCOSB-rndMng", "rlSysNameSource"),
    (0, "CISCOSB-rndMng", "rlSysNameIfIndex"),
)
if mibBuilder.loadTexts:
    rlSysNameEntry.setStatus("current")


class _RlSysNameSource_Type(Integer32):
    """Custom type rlSysNameSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 1),
          ("dhcpv4", 2),
          ("static", 3))
    )


_RlSysNameSource_Type.__name__ = "Integer32"
_RlSysNameSource_Object = MibTableColumn
rlSysNameSource = _RlSysNameSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 19, 1, 1),
    _RlSysNameSource_Type()
)
rlSysNameSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysNameSource.setStatus("current")


class _RlSysNameIfIndex_Type(InterfaceIndex):
    """Custom type rlSysNameIfIndex based on InterfaceIndex"""
    defaultValue = 1


_RlSysNameIfIndex_Type.__name__ = "InterfaceIndex"
_RlSysNameIfIndex_Object = MibTableColumn
rlSysNameIfIndex = _RlSysNameIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 19, 1, 2),
    _RlSysNameIfIndex_Type()
)
rlSysNameIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysNameIfIndex.setStatus("current")


class _RlSysNameName_Type(DisplayString):
    """Custom type rlSysNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RlSysNameName_Type.__name__ = "DisplayString"
_RlSysNameName_Object = MibTableColumn
rlSysNameName = _RlSysNameName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 19, 1, 3),
    _RlSysNameName_Type()
)
rlSysNameName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSysNameName.setStatus("current")
_RlSysNameRowStatus_Type = RowStatus
_RlSysNameRowStatus_Object = MibTableColumn
rlSysNameRowStatus = _RlSysNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 19, 1, 4),
    _RlSysNameRowStatus_Type()
)
rlSysNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSysNameRowStatus.setStatus("current")
_RlErrdisableLinkFlappingCause_Type = TruthValue
_RlErrdisableLinkFlappingCause_Object = MibScalar
rlErrdisableLinkFlappingCause = _RlErrdisableLinkFlappingCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1, 20),
    _RlErrdisableLinkFlappingCause_Type()
)
rlErrdisableLinkFlappingCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlErrdisableLinkFlappingCause.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-rndMng",
    **{"rndMng": rndMng,
       "rndSysId": rndSysId,
       "rndAction": rndAction,
       "rndFileName": rndFileName,
       "rlSnmpVersionSupported": rlSnmpVersionSupported,
       "rlSnmpMibVersion": rlSnmpMibVersion,
       "rlCpuUtilEnable": rlCpuUtilEnable,
       "rlCpuUtilDuringLastSecond": rlCpuUtilDuringLastSecond,
       "rlCpuUtilDuringLastMinute": rlCpuUtilDuringLastMinute,
       "rlCpuUtilDuringLast5Minutes": rlCpuUtilDuringLast5Minutes,
       "rlRebootDelay": rlRebootDelay,
       "rlGroupManagement": rlGroupManagement,
       "rlGroupMngQuery": rlGroupMngQuery,
       "rlGroupMngQueryPeriod": rlGroupMngQueryPeriod,
       "rlGroupMngLastUpdate": rlGroupMngLastUpdate,
       "rlGroupMngDevicesTable": rlGroupMngDevicesTable,
       "rlGroupMngDeviceEntry": rlGroupMngDeviceEntry,
       "rlGroupMngDeviceIdType": rlGroupMngDeviceIdType,
       "rlGroupMngDeviceId": rlGroupMngDeviceId,
       "rlGroupMngSubdevice": rlGroupMngSubdevice,
       "rlGroupMngDeviceDescription": rlGroupMngDeviceDescription,
       "rlGroupMngGroupMngEnabled": rlGroupMngGroupMngEnabled,
       "rlGroupMngGroupLLDPDeviceId": rlGroupMngGroupLLDPDeviceId,
       "rlGroupMngDeviceVendor": rlGroupMngDeviceVendor,
       "rlGroupMngDeviceAdvertisedCachingTime": rlGroupMngDeviceAdvertisedCachingTime,
       "rlGroupMngDeviceLocationURL": rlGroupMngDeviceLocationURL,
       "rlGroupMngDeviceLastSeen": rlGroupMngDeviceLastSeen,
       "rlRunningCDBequalToStartupCDB": rlRunningCDBequalToStartupCDB,
       "rlClearMib": rlClearMib,
       "rlScheduledReload": rlScheduledReload,
       "rlScheduledReloadPendingDate": rlScheduledReloadPendingDate,
       "rlScheduledReloadApprovedDate": rlScheduledReloadApprovedDate,
       "rlScheduledReloadCommit": rlScheduledReloadCommit,
       "rlSysNameTable": rlSysNameTable,
       "rlSysNameEntry": rlSysNameEntry,
       "rlSysNameSource": rlSysNameSource,
       "rlSysNameIfIndex": rlSysNameIfIndex,
       "rlSysNameName": rlSysNameName,
       "rlSysNameRowStatus": rlSysNameRowStatus,
       "rlErrdisableLinkFlappingCause": rlErrdisableLinkFlappingCause}
)
