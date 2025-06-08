# SNMP MIB module (TIMETRA-SAS-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-PTP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:16 2025
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
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxChassisNotifyChassisId,
 tmnxChassisNotifyHwIndex,
 tmnxCpmCardEntry,
 tmnxCpmCardOscillatorType) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisNotifyChassisId",
    "tmnxChassisNotifyHwIndex",
    "tmnxCpmCardEntry",
    "tmnxCpmCardOscillatorType")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxPtpLogInterval,) = mibBuilder.importSymbols(
    "TIMETRA-PTP-MIB",
    "TmnxPtpLogInterval")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(TItemDescription,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TmnxAdminState",
    "TmnxOperState")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraSASPtpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 74)
)
if mibBuilder.loadTexts:
    timetraSASPtpMIBModule.setRevisions(
        ("2011-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASPtpGroups_ObjectIdentity = ObjectIdentity
tmnxSASPtpGroups = _TmnxSASPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 74)
)
_TmnxSASPtp1588Objs_ObjectIdentity = ObjectIdentity
tmnxSASPtp1588Objs = _TmnxSASPtp1588Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 74)
)
_TmnxSASPtpClockConfig_ObjectIdentity = ObjectIdentity
tmnxSASPtpClockConfig = _TmnxSASPtpClockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 74, 1)
)


class _TmnxPtpLogSyncInterval_Type(TmnxPtpLogInterval):
    """Custom type tmnxPtpLogSyncInterval based on TmnxPtpLogInterval"""
    defaultValue = -6

    subtypeSpec = TmnxPtpLogInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, -3),
    )


_TmnxPtpLogSyncInterval_Type.__name__ = "TmnxPtpLogInterval"
_TmnxPtpLogSyncInterval_Object = MibScalar
tmnxPtpLogSyncInterval = _TmnxPtpLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 74, 1, 1),
    _TmnxPtpLogSyncInterval_Type()
)
tmnxPtpLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPtpLogSyncInterval.setStatus("current")

# Managed Objects groups

tmnxSASPtpV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 74, 1)
)
tmnxSASPtpV5v0Group.setObjects(
    ("TIMETRA-SAS-PTP-MIB", "tmnxPtpLogSyncInterval")
)
if mibBuilder.loadTexts:
    tmnxSASPtpV5v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-PTP-MIB",
    **{"timetraSASPtpMIBModule": timetraSASPtpMIBModule,
       "tmnxSASPtpGroups": tmnxSASPtpGroups,
       "tmnxSASPtpV5v0Group": tmnxSASPtpV5v0Group,
       "tmnxSASPtp1588Objs": tmnxSASPtp1588Objs,
       "tmnxSASPtpClockConfig": tmnxSASPtpClockConfig,
       "tmnxPtpLogSyncInterval": tmnxPtpLogSyncInterval}
)
