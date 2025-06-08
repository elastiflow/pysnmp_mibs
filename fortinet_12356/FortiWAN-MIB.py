# SNMP MIB module (FortiWAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fortinet_12356/FortiWAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:36:32 2025
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

(fortinet,) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "fortinet")

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

fortiwan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 118)
)
if mibBuilder.loadTexts:
    fortiwan.setRevisions(
        ("2015-11-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FnFortiWANMib_ObjectIdentity = ObjectIdentity
fnFortiWANMib = _FnFortiWANMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118)
)
_FwnSystem_ObjectIdentity = ObjectIdentity
fwnSystem = _FwnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1)
)


class _FwnSysHAMode_Type(Integer32):
    """Custom type fwnSysHAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 0),
          ("supported", 1))
    )


_FwnSysHAMode_Type.__name__ = "Integer32"
_FwnSysHAMode_Object = MibScalar
fwnSysHAMode = _FwnSysHAMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 1),
    _FwnSysHAMode_Type()
)
fwnSysHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysHAMode.setStatus("current")
_FwnSysSlaveVersion_Type = DisplayString
_FwnSysSlaveVersion_Object = MibScalar
fwnSysSlaveVersion = _FwnSysSlaveVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 2),
    _FwnSysSlaveVersion_Type()
)
fwnSysSlaveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysSlaveVersion.setStatus("current")
_FwnSysSlaveSerialNumber_Type = DisplayString
_FwnSysSlaveSerialNumber_Object = MibScalar
fwnSysSlaveSerialNumber = _FwnSysSlaveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 3),
    _FwnSysSlaveSerialNumber_Type()
)
fwnSysSlaveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysSlaveSerialNumber.setStatus("current")
_FwnSysSlaveUptime_Type = TimeTicks
_FwnSysSlaveUptime_Object = MibScalar
fwnSysSlaveUptime = _FwnSysSlaveUptime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 4),
    _FwnSysSlaveUptime_Type()
)
fwnSysSlaveUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysSlaveUptime.setStatus("current")
_FwnSysSlaveState_Type = DisplayString
_FwnSysSlaveState_Object = MibScalar
fwnSysSlaveState = _FwnSysSlaveState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 5),
    _FwnSysSlaveState_Type()
)
fwnSysSlaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysSlaveState.setStatus("current")
_FwnSysConnections_Type = Integer32
_FwnSysConnections_Object = MibScalar
fwnSysConnections = _FwnSysConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 6),
    _FwnSysConnections_Type()
)
fwnSysConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysConnections.setStatus("current")
_FwnSysCpuLoad_Type = Integer32
_FwnSysCpuLoad_Object = MibScalar
fwnSysCpuLoad = _FwnSysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 7),
    _FwnSysCpuLoad_Type()
)
fwnSysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysCpuLoad.setStatus("current")
_FwnSysUsers_Type = Integer32
_FwnSysUsers_Object = MibScalar
fwnSysUsers = _FwnSysUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8),
    _FwnSysUsers_Type()
)
fwnSysUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysUsers.setStatus("current")
_FwnSysPktPerSec_Type = Counter32
_FwnSysPktPerSec_Object = MibScalar
fwnSysPktPerSec = _FwnSysPktPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 9),
    _FwnSysPktPerSec_Type()
)
fwnSysPktPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysPktPerSec.setStatus("current")
_FwnSysConnectionRates_Type = Counter32
_FwnSysConnectionRates_Object = MibScalar
fwnSysConnectionRates = _FwnSysConnectionRates_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 10),
    _FwnSysConnectionRates_Type()
)
fwnSysConnectionRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysConnectionRates.setStatus("current")
_FwnNetwork_ObjectIdentity = ObjectIdentity
fwnNetwork = _FwnNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2)
)
_FwnWanLink_ObjectIdentity = ObjectIdentity
fwnWanLink = _FwnWanLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1)
)
_FwnWanNumber_Type = Integer32
_FwnWanNumber_Object = MibScalar
fwnWanNumber = _FwnWanNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 1),
    _FwnWanNumber_Type()
)
fwnWanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanNumber.setStatus("current")
_FwnWanTable_Object = MibTable
fwnWanTable = _FwnWanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fwnWanTable.setStatus("current")
_FwnWanEntry_Object = MibTableRow
fwnWanEntry = _FwnWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1)
)
fwnWanEntry.setIndexNames(
    (0, "FortiWAN-MIB", "fwnWanIndex"),
)
if mibBuilder.loadTexts:
    fwnWanEntry.setStatus("current")


class _FwnWanIndex_Type(Integer32):
    """Custom type fwnWanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwnWanIndex_Type.__name__ = "Integer32"
_FwnWanIndex_Object = MibTableColumn
fwnWanIndex = _FwnWanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 1),
    _FwnWanIndex_Type()
)
fwnWanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwnWanIndex.setStatus("current")
_FwnWanDescr_Type = DisplayString
_FwnWanDescr_Object = MibTableColumn
fwnWanDescr = _FwnWanDescr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 2),
    _FwnWanDescr_Type()
)
fwnWanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanDescr.setStatus("current")


class _FwnWanStatus_Type(Integer32):
    """Custom type fwnWanStatus based on Integer32"""
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
        *(("ok", 1),
          ("failed", 2),
          ("disabled", 3),
          ("backup", 4),
          ("unkown", 5))
    )


_FwnWanStatus_Type.__name__ = "Integer32"
_FwnWanStatus_Object = MibTableColumn
fwnWanStatus = _FwnWanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 3),
    _FwnWanStatus_Type()
)
fwnWanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanStatus.setStatus("current")
_FwnWanIP_Type = IpAddress
_FwnWanIP_Object = MibTableColumn
fwnWanIP = _FwnWanIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 4),
    _FwnWanIP_Type()
)
fwnWanIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanIP.setStatus("current")
_FwnWanInOctets_Type = Counter32
_FwnWanInOctets_Object = MibTableColumn
fwnWanInOctets = _FwnWanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 5),
    _FwnWanInOctets_Type()
)
fwnWanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanInOctets.setStatus("current")
_FwnWanOutOctets_Type = Counter32
_FwnWanOutOctets_Object = MibTableColumn
fwnWanOutOctets = _FwnWanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 6),
    _FwnWanOutOctets_Type()
)
fwnWanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanOutOctets.setStatus("current")
_FwnWanHealthReq_Type = Integer32
_FwnWanHealthReq_Object = MibTableColumn
fwnWanHealthReq = _FwnWanHealthReq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 7),
    _FwnWanHealthReq_Type()
)
fwnWanHealthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanHealthReq.setStatus("current")
_FwnWanHealthRep_Type = Integer32
_FwnWanHealthRep_Object = MibTableColumn
fwnWanHealthRep = _FwnWanHealthRep_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 8),
    _FwnWanHealthRep_Type()
)
fwnWanHealthRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanHealthRep.setStatus("current")
_FwnWanUpLimit_Type = Integer32
_FwnWanUpLimit_Object = MibTableColumn
fwnWanUpLimit = _FwnWanUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 9),
    _FwnWanUpLimit_Type()
)
fwnWanUpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanUpLimit.setStatus("current")
_FwnWanDownLimit_Type = Integer32
_FwnWanDownLimit_Object = MibTableColumn
fwnWanDownLimit = _FwnWanDownLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 10),
    _FwnWanDownLimit_Type()
)
fwnWanDownLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanDownLimit.setStatus("current")
_FwnWanTotalOctets_Type = Counter32
_FwnWanTotalOctets_Object = MibTableColumn
fwnWanTotalOctets = _FwnWanTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 11),
    _FwnWanTotalOctets_Type()
)
fwnWanTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanTotalOctets.setStatus("current")
_FwnWanConnTime_Type = TimeTicks
_FwnWanConnTime_Object = MibTableColumn
fwnWanConnTime = _FwnWanConnTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 12),
    _FwnWanConnTime_Type()
)
fwnWanConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanConnTime.setStatus("current")
_FwnWanInOctets64_Type = Counter64
_FwnWanInOctets64_Object = MibTableColumn
fwnWanInOctets64 = _FwnWanInOctets64_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 13),
    _FwnWanInOctets64_Type()
)
fwnWanInOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanInOctets64.setStatus("current")
_FwnWanOutOctets64_Type = Counter64
_FwnWanOutOctets64_Object = MibTableColumn
fwnWanOutOctets64 = _FwnWanOutOctets64_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 14),
    _FwnWanOutOctets64_Type()
)
fwnWanOutOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanOutOctets64.setStatus("current")
_FwnWanTotalOctets64_Type = Counter64
_FwnWanTotalOctets64_Object = MibTableColumn
fwnWanTotalOctets64 = _FwnWanTotalOctets64_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1, 2, 1, 15),
    _FwnWanTotalOctets64_Type()
)
fwnWanTotalOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnWanTotalOctets64.setStatus("current")
_FwnVlanLink_ObjectIdentity = ObjectIdentity
fwnVlanLink = _FwnVlanLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2)
)


class _FwnVlanNumber_Type(Integer32):
    """Custom type fwnVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FwnVlanNumber_Type.__name__ = "Integer32"
_FwnVlanNumber_Object = MibScalar
fwnVlanNumber = _FwnVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 1),
    _FwnVlanNumber_Type()
)
fwnVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanNumber.setStatus("current")
_FwnVlanTable_Object = MibTable
fwnVlanTable = _FwnVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fwnVlanTable.setStatus("current")
_FwnVlanEntry_Object = MibTableRow
fwnVlanEntry = _FwnVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1)
)
fwnVlanEntry.setIndexNames(
    (0, "FortiWAN-MIB", "fwnVlanIndex"),
)
if mibBuilder.loadTexts:
    fwnVlanEntry.setStatus("current")
_FwnVlanDescr_Type = DisplayString
_FwnVlanDescr_Object = MibTableColumn
fwnVlanDescr = _FwnVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 1),
    _FwnVlanDescr_Type()
)
fwnVlanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanDescr.setStatus("current")
_FwnVlanInOctets_Type = Counter32
_FwnVlanInOctets_Object = MibTableColumn
fwnVlanInOctets = _FwnVlanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 2),
    _FwnVlanInOctets_Type()
)
fwnVlanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanInOctets.setStatus("current")
_FwnVlanOutOctets_Type = Counter32
_FwnVlanOutOctets_Object = MibTableColumn
fwnVlanOutOctets = _FwnVlanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 3),
    _FwnVlanOutOctets_Type()
)
fwnVlanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanOutOctets.setStatus("current")
_FwnVlanTotalOctets_Type = Counter32
_FwnVlanTotalOctets_Object = MibTableColumn
fwnVlanTotalOctets = _FwnVlanTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 4),
    _FwnVlanTotalOctets_Type()
)
fwnVlanTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanTotalOctets.setStatus("current")
_FwnVlanInOctets64_Type = Counter64
_FwnVlanInOctets64_Object = MibTableColumn
fwnVlanInOctets64 = _FwnVlanInOctets64_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 5),
    _FwnVlanInOctets64_Type()
)
fwnVlanInOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanInOctets64.setStatus("current")
_FwnVlanOutOctets64_Type = Counter64
_FwnVlanOutOctets64_Object = MibTableColumn
fwnVlanOutOctets64 = _FwnVlanOutOctets64_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 6),
    _FwnVlanOutOctets64_Type()
)
fwnVlanOutOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanOutOctets64.setStatus("current")
_FwnVlanTotalOctets64_Type = Counter64
_FwnVlanTotalOctets64_Object = MibTableColumn
fwnVlanTotalOctets64 = _FwnVlanTotalOctets64_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 7),
    _FwnVlanTotalOctets64_Type()
)
fwnVlanTotalOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVlanTotalOctets64.setStatus("current")


class _FwnVlanIndex_Type(Integer32):
    """Custom type fwnVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwnVlanIndex_Type.__name__ = "Integer32"
_FwnVlanIndex_Object = MibTableColumn
fwnVlanIndex = _FwnVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2, 2, 1, 8),
    _FwnVlanIndex_Type()
)
fwnVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwnVlanIndex.setStatus("current")
_FwnEvent_ObjectIdentity = ObjectIdentity
fwnEvent = _FwnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3)
)
_FwnEventSystem_ObjectIdentity = ObjectIdentity
fwnEventSystem = _FwnEventSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1)
)
_FwnEventAdministrator_ObjectIdentity = ObjectIdentity
fwnEventAdministrator = _FwnEventAdministrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1)
)
_FwnEventAdminAccountPwChanged_Type = DisplayString
_FwnEventAdminAccountPwChanged_Object = MibScalar
fwnEventAdminAccountPwChanged = _FwnEventAdminAccountPwChanged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1, 1),
    _FwnEventAdminAccountPwChanged_Type()
)
fwnEventAdminAccountPwChanged.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventAdminAccountPwChanged.setStatus("current")
_FwnEventAdminAccountAdded_Type = DisplayString
_FwnEventAdminAccountAdded_Object = MibScalar
fwnEventAdminAccountAdded = _FwnEventAdminAccountAdded_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1, 2),
    _FwnEventAdminAccountAdded_Type()
)
fwnEventAdminAccountAdded.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventAdminAccountAdded.setStatus("current")
_FwnEventAdminAccountRemoved_Type = DisplayString
_FwnEventAdminAccountRemoved_Object = MibScalar
fwnEventAdminAccountRemoved = _FwnEventAdminAccountRemoved_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1, 3),
    _FwnEventAdminAccountRemoved_Type()
)
fwnEventAdminAccountRemoved.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventAdminAccountRemoved.setStatus("current")
_FwnEventMonitorAccountPwChanged_Type = DisplayString
_FwnEventMonitorAccountPwChanged_Object = MibScalar
fwnEventMonitorAccountPwChanged = _FwnEventMonitorAccountPwChanged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1, 4),
    _FwnEventMonitorAccountPwChanged_Type()
)
fwnEventMonitorAccountPwChanged.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventMonitorAccountPwChanged.setStatus("current")
_FwnEventMonitorAccountAdded_Type = DisplayString
_FwnEventMonitorAccountAdded_Object = MibScalar
fwnEventMonitorAccountAdded = _FwnEventMonitorAccountAdded_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1, 5),
    _FwnEventMonitorAccountAdded_Type()
)
fwnEventMonitorAccountAdded.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventMonitorAccountAdded.setStatus("current")
_FwnEventMonitorAccountRemoved_Type = DisplayString
_FwnEventMonitorAccountRemoved_Object = MibScalar
fwnEventMonitorAccountRemoved = _FwnEventMonitorAccountRemoved_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 1, 6),
    _FwnEventMonitorAccountRemoved_Type()
)
fwnEventMonitorAccountRemoved.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventMonitorAccountRemoved.setStatus("current")
_FwnEventConnection_ObjectIdentity = ObjectIdentity
fwnEventConnection = _FwnEventConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 2)
)
_FwnEventConnectionNum_Type = Counter32
_FwnEventConnectionNum_Object = MibScalar
fwnEventConnectionNum = _FwnEventConnectionNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 2, 1),
    _FwnEventConnectionNum_Type()
)
fwnEventConnectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventConnectionNum.setStatus("current")
_FwnEventConnectionRate_Type = Counter32
_FwnEventConnectionRate_Object = MibScalar
fwnEventConnectionRate = _FwnEventConnectionRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 2, 2),
    _FwnEventConnectionRate_Type()
)
fwnEventConnectionRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventConnectionRate.setStatus("current")
_FwnEventHA_ObjectIdentity = ObjectIdentity
fwnEventHA = _FwnEventHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 3)
)


class _FwnEventHASlaveState_Type(Integer32):
    """Custom type fwnEventHASlaveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("recovery", 1),
          ("failure", 2))
    )


_FwnEventHASlaveState_Type.__name__ = "Integer32"
_FwnEventHASlaveState_Object = MibScalar
fwnEventHASlaveState = _FwnEventHASlaveState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 3, 1),
    _FwnEventHASlaveState_Type()
)
fwnEventHASlaveState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventHASlaveState.setStatus("current")


class _FwnEventHATakeover_Type(Integer32):
    """Custom type fwnEventHATakeover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_FwnEventHATakeover_Type.__name__ = "Integer32"
_FwnEventHATakeover_Object = MibScalar
fwnEventHATakeover = _FwnEventHATakeover_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 3, 2),
    _FwnEventHATakeover_Type()
)
fwnEventHATakeover.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventHATakeover.setStatus("current")
_FwnEventVRRP_ObjectIdentity = ObjectIdentity
fwnEventVRRP = _FwnEventVRRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 4)
)


class _FwnEventVRRPTakeover_Type(Integer32):
    """Custom type fwnEventVRRPTakeover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_FwnEventVRRPTakeover_Type.__name__ = "Integer32"
_FwnEventVRRPTakeover_Object = MibScalar
fwnEventVRRPTakeover = _FwnEventVRRPTakeover_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1, 4, 1),
    _FwnEventVRRPTakeover_Type()
)
fwnEventVRRPTakeover.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventVRRPTakeover.setStatus("current")
_FwnEventNetwork_ObjectIdentity = ObjectIdentity
fwnEventNetwork = _FwnEventNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2)
)
_FwnEventWanlink_ObjectIdentity = ObjectIdentity
fwnEventWanlink = _FwnEventWanlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1)
)
_FwnEventWanLinkRecovery_Type = Integer32
_FwnEventWanLinkRecovery_Object = MibScalar
fwnEventWanLinkRecovery = _FwnEventWanLinkRecovery_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 1),
    _FwnEventWanLinkRecovery_Type()
)
fwnEventWanLinkRecovery.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventWanLinkRecovery.setStatus("current")
_FwnEventWanLinkFailure_Type = Integer32
_FwnEventWanLinkFailure_Object = MibScalar
fwnEventWanLinkFailure = _FwnEventWanLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 2),
    _FwnEventWanLinkFailure_Type()
)
fwnEventWanLinkFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventWanLinkFailure.setStatus("current")
_FwnEventTraffic_ObjectIdentity = ObjectIdentity
fwnEventTraffic = _FwnEventTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 3)
)
_FwnEventTotalWanTraffic_Type = Counter32
_FwnEventTotalWanTraffic_Object = MibScalar
fwnEventTotalWanTraffic = _FwnEventTotalWanTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 3, 1),
    _FwnEventTotalWanTraffic_Type()
)
fwnEventTotalWanTraffic.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwnEventTotalWanTraffic.setStatus("current")
_FnHAConformance_ObjectIdentity = ObjectIdentity
fnHAConformance = _FnHAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4)
)
_FnSysConformance_ObjectIdentity = ObjectIdentity
fnSysConformance = _FnSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5)
)
_FnWANConformance_ObjectIdentity = ObjectIdentity
fnWANConformance = _FnWANConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6)
)

# Managed Objects groups

fwnSystemHAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1)
)
fwnSystemHAGroup.setObjects(
      *(("FortiWAN-MIB", "fwnSysHAMode"),
        ("FortiWAN-MIB", "fwnSysSlaveVersion"),
        ("FortiWAN-MIB", "fwnSysSlaveSerialNumber"),
        ("FortiWAN-MIB", "fwnSysSlaveUptime"),
        ("FortiWAN-MIB", "fwnSysSlaveState"),
        ("FortiWAN-MIB", "fwnEventHASlaveState"),
        ("FortiWAN-MIB", "fwnEventHATakeover"))
)
if mibBuilder.loadTexts:
    fwnSystemHAGroup.setStatus("current")

fwnSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1)
)
fwnSystemGroup.setObjects(
      *(("FortiWAN-MIB", "fwnSysConnections"),
        ("FortiWAN-MIB", "fwnSysCpuLoad"),
        ("FortiWAN-MIB", "fwnSysUsers"),
        ("FortiWAN-MIB", "fwnSysPktPerSec"),
        ("FortiWAN-MIB", "fwnSysConnectionRates"),
        ("FortiWAN-MIB", "fwnEventAdminAccountPwChanged"),
        ("FortiWAN-MIB", "fwnEventAdminAccountAdded"),
        ("FortiWAN-MIB", "fwnEventAdminAccountRemoved"),
        ("FortiWAN-MIB", "fwnEventMonitorAccountPwChanged"),
        ("FortiWAN-MIB", "fwnEventMonitorAccountAdded"),
        ("FortiWAN-MIB", "fwnEventMonitorAccountRemoved"),
        ("FortiWAN-MIB", "fwnEventConnectionNum"),
        ("FortiWAN-MIB", "fwnEventConnectionRate"),
        ("FortiWAN-MIB", "fwnEventVRRPTakeover"))
)
if mibBuilder.loadTexts:
    fwnSystemGroup.setStatus("current")

fwnNetworkWANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1)
)
fwnNetworkWANGroup.setObjects(
      *(("FortiWAN-MIB", "fwnWanNumber"),
        ("FortiWAN-MIB", "fwnWanDescr"),
        ("FortiWAN-MIB", "fwnWanStatus"),
        ("FortiWAN-MIB", "fwnWanIP"),
        ("FortiWAN-MIB", "fwnWanInOctets"),
        ("FortiWAN-MIB", "fwnWanOutOctets"),
        ("FortiWAN-MIB", "fwnWanHealthReq"),
        ("FortiWAN-MIB", "fwnWanHealthRep"),
        ("FortiWAN-MIB", "fwnWanUpLimit"),
        ("FortiWAN-MIB", "fwnWanDownLimit"),
        ("FortiWAN-MIB", "fwnWanTotalOctets"),
        ("FortiWAN-MIB", "fwnWanConnTime"),
        ("FortiWAN-MIB", "fwnWanInOctets64"),
        ("FortiWAN-MIB", "fwnWanOutOctets64"),
        ("FortiWAN-MIB", "fwnWanTotalOctets64"),
        ("FortiWAN-MIB", "fwnVlanNumber"),
        ("FortiWAN-MIB", "fwnVlanDescr"),
        ("FortiWAN-MIB", "fwnVlanInOctets"),
        ("FortiWAN-MIB", "fwnVlanOutOctets"),
        ("FortiWAN-MIB", "fwnVlanTotalOctets"),
        ("FortiWAN-MIB", "fwnVlanInOctets64"),
        ("FortiWAN-MIB", "fwnVlanOutOctets64"),
        ("FortiWAN-MIB", "fwnVlanTotalOctets64"),
        ("FortiWAN-MIB", "fwnEventWanLinkRecovery"),
        ("FortiWAN-MIB", "fwnEventWanLinkFailure"),
        ("FortiWAN-MIB", "fwnEventTotalWanTraffic"))
)
if mibBuilder.loadTexts:
    fwnNetworkWANGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fwnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 118, 7)
)
fwnCompliance.setObjects(
      *(("FortiWAN-MIB", "fwnSystemHAGroup"),
        ("FortiWAN-MIB", "fwnSystemGroup"),
        ("FortiWAN-MIB", "fwnNetworkWANGroup"))
)
if mibBuilder.loadTexts:
    fwnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FortiWAN-MIB",
    **{"fortiwan": fortiwan,
       "fnFortiWANMib": fnFortiWANMib,
       "fwnSystem": fwnSystem,
       "fwnSysHAMode": fwnSysHAMode,
       "fwnSysSlaveVersion": fwnSysSlaveVersion,
       "fwnSysSlaveSerialNumber": fwnSysSlaveSerialNumber,
       "fwnSysSlaveUptime": fwnSysSlaveUptime,
       "fwnSysSlaveState": fwnSysSlaveState,
       "fwnSysConnections": fwnSysConnections,
       "fwnSysCpuLoad": fwnSysCpuLoad,
       "fwnSysUsers": fwnSysUsers,
       "fwnSysPktPerSec": fwnSysPktPerSec,
       "fwnSysConnectionRates": fwnSysConnectionRates,
       "fwnNetwork": fwnNetwork,
       "fwnWanLink": fwnWanLink,
       "fwnWanNumber": fwnWanNumber,
       "fwnWanTable": fwnWanTable,
       "fwnWanEntry": fwnWanEntry,
       "fwnWanIndex": fwnWanIndex,
       "fwnWanDescr": fwnWanDescr,
       "fwnWanStatus": fwnWanStatus,
       "fwnWanIP": fwnWanIP,
       "fwnWanInOctets": fwnWanInOctets,
       "fwnWanOutOctets": fwnWanOutOctets,
       "fwnWanHealthReq": fwnWanHealthReq,
       "fwnWanHealthRep": fwnWanHealthRep,
       "fwnWanUpLimit": fwnWanUpLimit,
       "fwnWanDownLimit": fwnWanDownLimit,
       "fwnWanTotalOctets": fwnWanTotalOctets,
       "fwnWanConnTime": fwnWanConnTime,
       "fwnWanInOctets64": fwnWanInOctets64,
       "fwnWanOutOctets64": fwnWanOutOctets64,
       "fwnWanTotalOctets64": fwnWanTotalOctets64,
       "fwnVlanLink": fwnVlanLink,
       "fwnVlanNumber": fwnVlanNumber,
       "fwnVlanTable": fwnVlanTable,
       "fwnVlanEntry": fwnVlanEntry,
       "fwnVlanDescr": fwnVlanDescr,
       "fwnVlanInOctets": fwnVlanInOctets,
       "fwnVlanOutOctets": fwnVlanOutOctets,
       "fwnVlanTotalOctets": fwnVlanTotalOctets,
       "fwnVlanInOctets64": fwnVlanInOctets64,
       "fwnVlanOutOctets64": fwnVlanOutOctets64,
       "fwnVlanTotalOctets64": fwnVlanTotalOctets64,
       "fwnVlanIndex": fwnVlanIndex,
       "fwnEvent": fwnEvent,
       "fwnEventSystem": fwnEventSystem,
       "fwnEventAdministrator": fwnEventAdministrator,
       "fwnEventAdminAccountPwChanged": fwnEventAdminAccountPwChanged,
       "fwnEventAdminAccountAdded": fwnEventAdminAccountAdded,
       "fwnEventAdminAccountRemoved": fwnEventAdminAccountRemoved,
       "fwnEventMonitorAccountPwChanged": fwnEventMonitorAccountPwChanged,
       "fwnEventMonitorAccountAdded": fwnEventMonitorAccountAdded,
       "fwnEventMonitorAccountRemoved": fwnEventMonitorAccountRemoved,
       "fwnEventConnection": fwnEventConnection,
       "fwnEventConnectionNum": fwnEventConnectionNum,
       "fwnEventConnectionRate": fwnEventConnectionRate,
       "fwnEventHA": fwnEventHA,
       "fwnEventHASlaveState": fwnEventHASlaveState,
       "fwnEventHATakeover": fwnEventHATakeover,
       "fwnEventVRRP": fwnEventVRRP,
       "fwnEventVRRPTakeover": fwnEventVRRPTakeover,
       "fwnEventNetwork": fwnEventNetwork,
       "fwnEventWanlink": fwnEventWanlink,
       "fwnEventWanLinkRecovery": fwnEventWanLinkRecovery,
       "fwnEventWanLinkFailure": fwnEventWanLinkFailure,
       "fwnEventTraffic": fwnEventTraffic,
       "fwnEventTotalWanTraffic": fwnEventTotalWanTraffic,
       "fnHAConformance": fnHAConformance,
       "fwnSystemHAGroup": fwnSystemHAGroup,
       "fnSysConformance": fnSysConformance,
       "fwnSystemGroup": fwnSystemGroup,
       "fnWANConformance": fnWANConformance,
       "fwnNetworkWANGroup": fwnNetworkWANGroup,
       "fwnCompliance": fwnCompliance}
)
