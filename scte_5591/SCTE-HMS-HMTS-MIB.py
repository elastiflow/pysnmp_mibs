# SNMP MIB module (SCTE-HMS-HMTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HMTS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:32:18 2025
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

(entityGeneralGroup,
 entityNotificationsGroup,
 entityPhysical2Group,
 entityPhysicalGroup) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entityGeneralGroup",
    "entityNotificationsGroup",
    "entityPhysical2Group",
    "entityPhysicalGroup")

(heCommonLogGroup,
 heCommonNotificationsGroup) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-COMMON-MIB",
    "heCommonLogGroup",
    "heCommonNotificationsGroup")

(heHMTS,) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "heHMTS")

(analogAlarmsGroup,
 currentAlarmsGroup,
 discreteAlarmsGroup) = mibBuilder.importSymbols(
    "SCTE-HMS-PROPERTY-MIB",
    "analogAlarmsGroup",
    "currentAlarmsGroup",
    "discreteAlarmsGroup")

(snmpTargetBasicGroup,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetBasicGroup")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(systemGroup,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "systemGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

heHMTSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HmtsComStatCodes(TextualConvention, Integer32):
    status = "current"
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
              20,
              21,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("noRevPortId", 2),
          ("notActive", 3),
          ("notRegis", 4),
          ("pendRegis", 5),
          ("registering", 6),
          ("transDisabled", 7),
          ("rcvrDisabled", 8),
          ("rtrnLvl", 9),
          ("notResp", 10),
          ("invMac", 11),
          ("fwdFreqMismatch", 12),
          ("invIP", 20),
          ("dupIP", 21),
          ("invComm", 30),
          ("dupComm", 31),
          ("other", 32))
    )



# MIB Managed Objects in the order of their OIDs

_HeHMTSObjects_ObjectIdentity = ObjectIdentity
heHMTSObjects = _HeHMTSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1)
)
_HmtsNotifications_ObjectIdentity = ObjectIdentity
hmtsNotifications = _HmtsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 0)
)
_HmtsInfoGroup_ObjectIdentity = ObjectIdentity
hmtsInfoGroup = _HmtsInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1)
)


class _HmtsAdminState_Type(Integer32):
    """Custom type hmtsAdminState based on Integer32"""
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


_HmtsAdminState_Type.__name__ = "Integer32"
_HmtsAdminState_Object = MibScalar
hmtsAdminState = _HmtsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 1),
    _HmtsAdminState_Type()
)
hmtsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsAdminState.setStatus("current")


class _HmtsOperState_Type(Integer32):
    """Custom type hmtsOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("swFailure", 2),
          ("hwFailure", 3))
    )


_HmtsOperState_Type.__name__ = "Integer32"
_HmtsOperState_Object = MibScalar
hmtsOperState = _HmtsOperState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 2),
    _HmtsOperState_Type()
)
hmtsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsOperState.setStatus("current")


class _HmtsProxyType_Type(Integer32):
    """Custom type hmtsProxyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipBased", 1),
          ("communityBased", 2),
          ("both", 3))
    )


_HmtsProxyType_Type.__name__ = "Integer32"
_HmtsProxyType_Object = MibScalar
hmtsProxyType = _HmtsProxyType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 3),
    _HmtsProxyType_Type()
)
hmtsProxyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsProxyType.setStatus("current")


class _HmtsFreqSwitchMethod_Type(Integer32):
    """Custom type hmtsFreqSwitchMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_HmtsFreqSwitchMethod_Type.__name__ = "Integer32"
_HmtsFreqSwitchMethod_Object = MibScalar
hmtsFreqSwitchMethod = _HmtsFreqSwitchMethod_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 4),
    _HmtsFreqSwitchMethod_Type()
)
hmtsFreqSwitchMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsFreqSwitchMethod.setStatus("current")


class _HmtsModel_Type(DisplayString):
    """Custom type hmtsModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmtsModel_Type.__name__ = "DisplayString"
_HmtsModel_Object = MibScalar
hmtsModel = _HmtsModel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 5),
    _HmtsModel_Type()
)
hmtsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsModel.setStatus("current")


class _HmtsSerialNumber_Type(DisplayString):
    """Custom type hmtsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmtsSerialNumber_Type.__name__ = "DisplayString"
_HmtsSerialNumber_Object = MibScalar
hmtsSerialNumber = _HmtsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 6),
    _HmtsSerialNumber_Type()
)
hmtsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsSerialNumber.setStatus("current")


class _HmtsSoftwareVersion_Type(DisplayString):
    """Custom type hmtsSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmtsSoftwareVersion_Type.__name__ = "DisplayString"
_HmtsSoftwareVersion_Object = MibScalar
hmtsSoftwareVersion = _HmtsSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 7),
    _HmtsSoftwareVersion_Type()
)
hmtsSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsSoftwareVersion.setStatus("current")
_HmtsTimeServerAddress_Type = IpAddress
_HmtsTimeServerAddress_Object = MibScalar
hmtsTimeServerAddress = _HmtsTimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 8),
    _HmtsTimeServerAddress_Type()
)
hmtsTimeServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsTimeServerAddress.setStatus("current")


class _HmtsTimeServerSyncInterval_Type(Integer32):
    """Custom type hmtsTimeServerSyncInterval based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 8640000),
    )


_HmtsTimeServerSyncInterval_Type.__name__ = "Integer32"
_HmtsTimeServerSyncInterval_Object = MibScalar
hmtsTimeServerSyncInterval = _HmtsTimeServerSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 1, 9),
    _HmtsTimeServerSyncInterval_Type()
)
hmtsTimeServerSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsTimeServerSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    hmtsTimeServerSyncInterval.setUnits("1 s")
_HmtsManagementGroup_ObjectIdentity = ObjectIdentity
hmtsManagementGroup = _HmtsManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2)
)
_HmtsMacPduGroup_ObjectIdentity = ObjectIdentity
hmtsMacPduGroup = _HmtsMacPduGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1)
)


class _HmtsMacPduTimeout_Type(Integer32):
    """Custom type hmtsMacPduTimeout based on Integer32"""
    defaultValue = 15


_HmtsMacPduTimeout_Type.__name__ = "Integer32"
_HmtsMacPduTimeout_Object = MibScalar
hmtsMacPduTimeout = _HmtsMacPduTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1, 1),
    _HmtsMacPduTimeout_Type()
)
hmtsMacPduTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsMacPduTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hmtsMacPduTimeout.setUnits("1 ms")


class _HmtsTalkPduTimeout_Type(Integer32):
    """Custom type hmtsTalkPduTimeout based on Integer32"""
    defaultValue = 5000


_HmtsTalkPduTimeout_Type.__name__ = "Integer32"
_HmtsTalkPduTimeout_Object = MibScalar
hmtsTalkPduTimeout = _HmtsTalkPduTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1, 2),
    _HmtsTalkPduTimeout_Type()
)
hmtsTalkPduTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsTalkPduTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hmtsTalkPduTimeout.setUnits("1 ms")


class _HmtsMacBroadcastDelay_Type(Integer32):
    """Custom type hmtsMacBroadcastDelay based on Integer32"""
    defaultValue = 250


_HmtsMacBroadcastDelay_Type.__name__ = "Integer32"
_HmtsMacBroadcastDelay_Object = MibScalar
hmtsMacBroadcastDelay = _HmtsMacBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1, 3),
    _HmtsMacBroadcastDelay_Type()
)
hmtsMacBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsMacBroadcastDelay.setStatus("current")
if mibBuilder.loadTexts:
    hmtsMacBroadcastDelay.setUnits("1 ms")


class _HmtsAlarmDiscoveryMode_Type(Integer32):
    """Custom type hmtsAlarmDiscoveryMode based on Integer32"""
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
        *(("polling", 1),
          ("contention", 2),
          ("hybrid", 3),
          ("off", 4))
    )


_HmtsAlarmDiscoveryMode_Type.__name__ = "Integer32"
_HmtsAlarmDiscoveryMode_Object = MibScalar
hmtsAlarmDiscoveryMode = _HmtsAlarmDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1, 4),
    _HmtsAlarmDiscoveryMode_Type()
)
hmtsAlarmDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsAlarmDiscoveryMode.setStatus("current")


class _HmtsChnldescPduInt_Type(Integer32):
    """Custom type hmtsChnldescPduInt based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HmtsChnldescPduInt_Type.__name__ = "Integer32"
_HmtsChnldescPduInt_Object = MibScalar
hmtsChnldescPduInt = _HmtsChnldescPduInt_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1, 5),
    _HmtsChnldescPduInt_Type()
)
hmtsChnldescPduInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsChnldescPduInt.setStatus("current")
if mibBuilder.loadTexts:
    hmtsChnldescPduInt.setUnits("1 s")


class _HmtsTimePduInt_Type(Integer32):
    """Custom type hmtsTimePduInt based on Integer32"""
    defaultValue = 3600


_HmtsTimePduInt_Type.__name__ = "Integer32"
_HmtsTimePduInt_Object = MibScalar
hmtsTimePduInt = _HmtsTimePduInt_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1, 6),
    _HmtsTimePduInt_Type()
)
hmtsTimePduInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsTimePduInt.setStatus("current")
if mibBuilder.loadTexts:
    hmtsTimePduInt.setUnits("1 s")


class _HmtsDeviceAccessMode_Type(Integer32):
    """Custom type hmtsDeviceAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("queued", 2),
          ("interrupt", 3))
    )


_HmtsDeviceAccessMode_Type.__name__ = "Integer32"
_HmtsDeviceAccessMode_Object = MibScalar
hmtsDeviceAccessMode = _HmtsDeviceAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 1, 7),
    _HmtsDeviceAccessMode_Type()
)
hmtsDeviceAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsDeviceAccessMode.setStatus("current")
_HmtsRegistrationGroup_ObjectIdentity = ObjectIdentity
hmtsRegistrationGroup = _HmtsRegistrationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 2)
)


class _HmtsRegInterval_Type(Integer32):
    """Custom type hmtsRegInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_HmtsRegInterval_Type.__name__ = "Integer32"
_HmtsRegInterval_Object = MibScalar
hmtsRegInterval = _HmtsRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 2, 1),
    _HmtsRegInterval_Type()
)
hmtsRegInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRegInterval.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRegInterval.setUnits("1 s")


class _HmtsRegMinDuration_Type(Integer32):
    """Custom type hmtsRegMinDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmtsRegMinDuration_Type.__name__ = "Integer32"
_HmtsRegMinDuration_Object = MibScalar
hmtsRegMinDuration = _HmtsRegMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 2, 2),
    _HmtsRegMinDuration_Type()
)
hmtsRegMinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRegMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRegMinDuration.setUnits("1 s")


class _HmtsRegMaxDuration_Type(Integer32):
    """Custom type hmtsRegMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmtsRegMaxDuration_Type.__name__ = "Integer32"
_HmtsRegMaxDuration_Object = MibScalar
hmtsRegMaxDuration = _HmtsRegMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 2, 3),
    _HmtsRegMaxDuration_Type()
)
hmtsRegMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRegMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRegMaxDuration.setUnits("1 s")


class _HmtsRegContinuity_Type(Integer32):
    """Custom type hmtsRegContinuity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("queued", 2),
          ("continuous", 3))
    )


_HmtsRegContinuity_Type.__name__ = "Integer32"
_HmtsRegContinuity_Object = MibScalar
hmtsRegContinuity = _HmtsRegContinuity_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 2, 4),
    _HmtsRegContinuity_Type()
)
hmtsRegContinuity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRegContinuity.setStatus("current")
_HmtsSnmpTrapControlGroup_ObjectIdentity = ObjectIdentity
hmtsSnmpTrapControlGroup = _HmtsSnmpTrapControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3)
)
_HmtsTrapControlTable_Object = MibTable
hmtsTrapControlTable = _HmtsTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hmtsTrapControlTable.setStatus("current")
_HmtsTrapControlEntry_Object = MibTableRow
hmtsTrapControlEntry = _HmtsTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1)
)
hmtsTrapControlEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsTControlId"),
)
if mibBuilder.loadTexts:
    hmtsTrapControlEntry.setStatus("current")


class _HmtsTControlId_Type(Integer32):
    """Custom type hmtsTControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmtsTControlId_Type.__name__ = "Integer32"
_HmtsTControlId_Object = MibTableColumn
hmtsTControlId = _HmtsTControlId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 1),
    _HmtsTControlId_Type()
)
hmtsTControlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsTControlId.setStatus("current")


class _HmtsTControlInterval_Type(Integer32):
    """Custom type hmtsTControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HmtsTControlInterval_Type.__name__ = "Integer32"
_HmtsTControlInterval_Object = MibTableColumn
hmtsTControlInterval = _HmtsTControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 2),
    _HmtsTControlInterval_Type()
)
hmtsTControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsTControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    hmtsTControlInterval.setUnits("1 s")


class _HmtsTControlChainId_Type(Integer32):
    """Custom type hmtsTControlChainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HmtsTControlChainId_Type.__name__ = "Integer32"
_HmtsTControlChainId_Object = MibTableColumn
hmtsTControlChainId = _HmtsTControlChainId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 3),
    _HmtsTControlChainId_Type()
)
hmtsTControlChainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsTControlChainId.setStatus("current")


class _HmtsTControlMinDuration_Type(Integer32):
    """Custom type hmtsTControlMinDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_HmtsTControlMinDuration_Type.__name__ = "Integer32"
_HmtsTControlMinDuration_Object = MibTableColumn
hmtsTControlMinDuration = _HmtsTControlMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 4),
    _HmtsTControlMinDuration_Type()
)
hmtsTControlMinDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsTControlMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    hmtsTControlMinDuration.setUnits("1 s")


class _HmtsTControlMaxDuration_Type(Integer32):
    """Custom type hmtsTControlMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_HmtsTControlMaxDuration_Type.__name__ = "Integer32"
_HmtsTControlMaxDuration_Object = MibTableColumn
hmtsTControlMaxDuration = _HmtsTControlMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 5),
    _HmtsTControlMaxDuration_Type()
)
hmtsTControlMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsTControlMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    hmtsTControlMaxDuration.setUnits("1 s")


class _HmtsTControlContinuity_Type(Integer32):
    """Custom type hmtsTControlContinuity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("queued", 2),
          ("continuous", 3))
    )


_HmtsTControlContinuity_Type.__name__ = "Integer32"
_HmtsTControlContinuity_Object = MibTableColumn
hmtsTControlContinuity = _HmtsTControlContinuity_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 6),
    _HmtsTControlContinuity_Type()
)
hmtsTControlContinuity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsTControlContinuity.setStatus("current")
_HmtsTControlMulticastAddr_Type = MacAddress
_HmtsTControlMulticastAddr_Object = MibTableColumn
hmtsTControlMulticastAddr = _HmtsTControlMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 7),
    _HmtsTControlMulticastAddr_Type()
)
hmtsTControlMulticastAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsTControlMulticastAddr.setStatus("current")
_HmtsTControlRowStatus_Type = RowStatus
_HmtsTControlRowStatus_Object = MibTableColumn
hmtsTControlRowStatus = _HmtsTControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 3, 1, 1, 8),
    _HmtsTControlRowStatus_Type()
)
hmtsTControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsTControlRowStatus.setStatus("current")
_HmtsSnmpProtocolGroup_ObjectIdentity = ObjectIdentity
hmtsSnmpProtocolGroup = _HmtsSnmpProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 4)
)


class _HmtsSnmpTimeout_Type(Integer32):
    """Custom type hmtsSnmpTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HmtsSnmpTimeout_Type.__name__ = "Integer32"
_HmtsSnmpTimeout_Object = MibScalar
hmtsSnmpTimeout = _HmtsSnmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 4, 1),
    _HmtsSnmpTimeout_Type()
)
hmtsSnmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsSnmpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hmtsSnmpTimeout.setUnits("1 ms")


class _HmtsSnmpBroadcastDelay_Type(Integer32):
    """Custom type hmtsSnmpBroadcastDelay based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HmtsSnmpBroadcastDelay_Type.__name__ = "Integer32"
_HmtsSnmpBroadcastDelay_Object = MibScalar
hmtsSnmpBroadcastDelay = _HmtsSnmpBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 4, 2),
    _HmtsSnmpBroadcastDelay_Type()
)
hmtsSnmpBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsSnmpBroadcastDelay.setStatus("current")
if mibBuilder.loadTexts:
    hmtsSnmpBroadcastDelay.setUnits("1 ms")
_HmtsFwdPortTable_Object = MibTable
hmtsFwdPortTable = _HmtsFwdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hmtsFwdPortTable.setStatus("current")
_HmtsFwdPortEntry_Object = MibTableRow
hmtsFwdPortEntry = _HmtsFwdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1)
)
hmtsFwdPortEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsFwdPortId"),
)
if mibBuilder.loadTexts:
    hmtsFwdPortEntry.setStatus("current")


class _HmtsFwdPortId_Type(DisplayString):
    """Custom type hmtsFwdPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HmtsFwdPortId_Type.__name__ = "DisplayString"
_HmtsFwdPortId_Object = MibTableColumn
hmtsFwdPortId = _HmtsFwdPortId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 1),
    _HmtsFwdPortId_Type()
)
hmtsFwdPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsFwdPortId.setStatus("current")
_HmtsFwdPortDescr_Type = DisplayString
_HmtsFwdPortDescr_Object = MibTableColumn
hmtsFwdPortDescr = _HmtsFwdPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 2),
    _HmtsFwdPortDescr_Type()
)
hmtsFwdPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsFwdPortDescr.setStatus("current")


class _HmtsFwdPortType_Type(Integer32):
    """Custom type hmtsFwdPortType based on Integer32"""
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
        *(("rf", 1),
          ("rs485", 2),
          ("rs232", 3),
          ("other", 4))
    )


_HmtsFwdPortType_Type.__name__ = "Integer32"
_HmtsFwdPortType_Object = MibTableColumn
hmtsFwdPortType = _HmtsFwdPortType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 3),
    _HmtsFwdPortType_Type()
)
hmtsFwdPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsFwdPortType.setStatus("current")


class _HmtsFwdPortAdminState_Type(Integer32):
    """Custom type hmtsFwdPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disableCarrierOn", 2),
          ("disableCarrierOff", 3))
    )


_HmtsFwdPortAdminState_Type.__name__ = "Integer32"
_HmtsFwdPortAdminState_Object = MibTableColumn
hmtsFwdPortAdminState = _HmtsFwdPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 4),
    _HmtsFwdPortAdminState_Type()
)
hmtsFwdPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsFwdPortAdminState.setStatus("current")


class _HmtsFwdPortOperState_Type(Integer32):
    """Custom type hmtsFwdPortOperState based on Integer32"""
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
        *(("noError", 1),
          ("noFreqAssgn", 2),
          ("freqUnlocked", 3),
          ("portComFailure", 4),
          ("otherError", 5))
    )


_HmtsFwdPortOperState_Type.__name__ = "Integer32"
_HmtsFwdPortOperState_Object = MibTableColumn
hmtsFwdPortOperState = _HmtsFwdPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 5),
    _HmtsFwdPortOperState_Type()
)
hmtsFwdPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsFwdPortOperState.setStatus("current")
_HmtsFwdHmtsFrequency_Type = Integer32
_HmtsFwdHmtsFrequency_Object = MibTableColumn
hmtsFwdHmtsFrequency = _HmtsFwdHmtsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 6),
    _HmtsFwdHmtsFrequency_Type()
)
hmtsFwdHmtsFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsFwdHmtsFrequency.setStatus("current")
if mibBuilder.loadTexts:
    hmtsFwdHmtsFrequency.setUnits("1 Hz")
_HmtsFwdXpndrFrequency_Type = Integer32
_HmtsFwdXpndrFrequency_Object = MibTableColumn
hmtsFwdXpndrFrequency = _HmtsFwdXpndrFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 7),
    _HmtsFwdXpndrFrequency_Type()
)
hmtsFwdXpndrFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsFwdXpndrFrequency.setStatus("current")
if mibBuilder.loadTexts:
    hmtsFwdXpndrFrequency.setUnits("1 Hz")
_HmtsFwdProvPwrLvl_Type = Integer32
_HmtsFwdProvPwrLvl_Object = MibTableColumn
hmtsFwdProvPwrLvl = _HmtsFwdProvPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 8),
    _HmtsFwdProvPwrLvl_Type()
)
hmtsFwdProvPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsFwdProvPwrLvl.setStatus("current")
if mibBuilder.loadTexts:
    hmtsFwdProvPwrLvl.setUnits("0.1 dBmV")
_HmtsFwdMaxPwrLvl_Type = Integer32
_HmtsFwdMaxPwrLvl_Object = MibTableColumn
hmtsFwdMaxPwrLvl = _HmtsFwdMaxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 9),
    _HmtsFwdMaxPwrLvl_Type()
)
hmtsFwdMaxPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsFwdMaxPwrLvl.setStatus("current")
if mibBuilder.loadTexts:
    hmtsFwdMaxPwrLvl.setUnits("0.1 dBmV")


class _HmtsFwdPollTime_Type(Integer32):
    """Custom type hmtsFwdPollTime based on Integer32"""
    defaultValue = 360


_HmtsFwdPollTime_Type.__name__ = "Integer32"
_HmtsFwdPollTime_Object = MibTableColumn
hmtsFwdPollTime = _HmtsFwdPollTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 5, 1, 10),
    _HmtsFwdPollTime_Type()
)
hmtsFwdPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsFwdPollTime.setStatus("current")
if mibBuilder.loadTexts:
    hmtsFwdPollTime.setUnits("1 s")
_HmtsRevPortTable_Object = MibTable
hmtsRevPortTable = _HmtsRevPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hmtsRevPortTable.setStatus("current")
_HmtsRevPortEntry_Object = MibTableRow
hmtsRevPortEntry = _HmtsRevPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1)
)
hmtsRevPortEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsRevPortId"),
)
if mibBuilder.loadTexts:
    hmtsRevPortEntry.setStatus("current")


class _HmtsRevPortId_Type(DisplayString):
    """Custom type hmtsRevPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HmtsRevPortId_Type.__name__ = "DisplayString"
_HmtsRevPortId_Object = MibTableColumn
hmtsRevPortId = _HmtsRevPortId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 1),
    _HmtsRevPortId_Type()
)
hmtsRevPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsRevPortId.setStatus("current")


class _HmtsRevFwdPortId_Type(DisplayString):
    """Custom type hmtsRevFwdPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HmtsRevFwdPortId_Type.__name__ = "DisplayString"
_HmtsRevFwdPortId_Object = MibTableColumn
hmtsRevFwdPortId = _HmtsRevFwdPortId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 2),
    _HmtsRevFwdPortId_Type()
)
hmtsRevFwdPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevFwdPortId.setStatus("current")
_HmtsRevPortDescr_Type = DisplayString
_HmtsRevPortDescr_Object = MibTableColumn
hmtsRevPortDescr = _HmtsRevPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 3),
    _HmtsRevPortDescr_Type()
)
hmtsRevPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsRevPortDescr.setStatus("current")


class _HmtsRevPortType_Type(Integer32):
    """Custom type hmtsRevPortType based on Integer32"""
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
        *(("rf", 1),
          ("rs485", 2),
          ("rs232", 3),
          ("other", 4))
    )


_HmtsRevPortType_Type.__name__ = "Integer32"
_HmtsRevPortType_Object = MibTableColumn
hmtsRevPortType = _HmtsRevPortType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 4),
    _HmtsRevPortType_Type()
)
hmtsRevPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsRevPortType.setStatus("current")


class _HmtsRevPortAdminState_Type(Integer32):
    """Custom type hmtsRevPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HmtsRevPortAdminState_Type.__name__ = "Integer32"
_HmtsRevPortAdminState_Object = MibTableColumn
hmtsRevPortAdminState = _HmtsRevPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 5),
    _HmtsRevPortAdminState_Type()
)
hmtsRevPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevPortAdminState.setStatus("current")


class _HmtsRevPortOperState_Type(Integer32):
    """Custom type hmtsRevPortOperState based on Integer32"""
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
        *(("noError", 1),
          ("noFreqAssgn", 2),
          ("freqUnlocked", 3),
          ("portComFailure", 4),
          ("otherError", 5))
    )


_HmtsRevPortOperState_Type.__name__ = "Integer32"
_HmtsRevPortOperState_Object = MibTableColumn
hmtsRevPortOperState = _HmtsRevPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 6),
    _HmtsRevPortOperState_Type()
)
hmtsRevPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsRevPortOperState.setStatus("current")
_HmtsRevFrequency_Type = Integer32
_HmtsRevFrequency_Object = MibTableColumn
hmtsRevFrequency = _HmtsRevFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 7),
    _HmtsRevFrequency_Type()
)
hmtsRevFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevFrequency.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRevFrequency.setUnits("1 Hz")
_HmtsRevMuteLvl_Type = Integer32
_HmtsRevMuteLvl_Object = MibTableColumn
hmtsRevMuteLvl = _HmtsRevMuteLvl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 8),
    _HmtsRevMuteLvl_Type()
)
hmtsRevMuteLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevMuteLvl.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRevMuteLvl.setUnits("0.1 dBmV")
_HmtsRevMulticastAddr_Type = MacAddress
_HmtsRevMulticastAddr_Object = MibTableColumn
hmtsRevMulticastAddr = _HmtsRevMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 9),
    _HmtsRevMulticastAddr_Type()
)
hmtsRevMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevMulticastAddr.setStatus("current")
_HmtsRevReturnLvl_Type = Integer32
_HmtsRevReturnLvl_Object = MibTableColumn
hmtsRevReturnLvl = _HmtsRevReturnLvl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 10),
    _HmtsRevReturnLvl_Type()
)
hmtsRevReturnLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsRevReturnLvl.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRevReturnLvl.setUnits("0.1 dBmV")
_HmtsRevCRCErrors_Type = Integer32
_HmtsRevCRCErrors_Object = MibTableColumn
hmtsRevCRCErrors = _HmtsRevCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 11),
    _HmtsRevCRCErrors_Type()
)
hmtsRevCRCErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevCRCErrors.setStatus("current")
_HmtsRevFrameErrors_Type = Integer32
_HmtsRevFrameErrors_Object = MibTableColumn
hmtsRevFrameErrors = _HmtsRevFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 12),
    _HmtsRevFrameErrors_Type()
)
hmtsRevFrameErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevFrameErrors.setStatus("current")


class _HmtsRevBackOffPeriod_Type(Integer32):
    """Custom type hmtsRevBackOffPeriod based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_HmtsRevBackOffPeriod_Type.__name__ = "Integer32"
_HmtsRevBackOffPeriod_Object = MibTableColumn
hmtsRevBackOffPeriod = _HmtsRevBackOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 13),
    _HmtsRevBackOffPeriod_Type()
)
hmtsRevBackOffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevBackOffPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRevBackOffPeriod.setUnits("1 ms")


class _HmtsRevACKTimeout_Type(Integer32):
    """Custom type hmtsRevACKTimeout based on Integer32"""
    defaultValue = 19

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmtsRevACKTimeout_Type.__name__ = "Integer32"
_HmtsRevACKTimeout_Object = MibTableColumn
hmtsRevACKTimeout = _HmtsRevACKTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 14),
    _HmtsRevACKTimeout_Type()
)
hmtsRevACKTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevACKTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hmtsRevACKTimeout.setUnits("1 ms")


class _HmtsRevMaxMACRetries_Type(Integer32):
    """Custom type hmtsRevMaxMACRetries based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmtsRevMaxMACRetries_Type.__name__ = "Integer32"
_HmtsRevMaxMACRetries_Object = MibTableColumn
hmtsRevMaxMACRetries = _HmtsRevMaxMACRetries_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 15),
    _HmtsRevMaxMACRetries_Type()
)
hmtsRevMaxMACRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevMaxMACRetries.setStatus("current")


class _HmtsRevBackOffMinExp_Type(Integer32):
    """Custom type hmtsRevBackOffMinExp based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HmtsRevBackOffMinExp_Type.__name__ = "Integer32"
_HmtsRevBackOffMinExp_Object = MibTableColumn
hmtsRevBackOffMinExp = _HmtsRevBackOffMinExp_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 16),
    _HmtsRevBackOffMinExp_Type()
)
hmtsRevBackOffMinExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevBackOffMinExp.setStatus("current")


class _HmtsRevBackOffMaxExp_Type(Integer32):
    """Custom type hmtsRevBackOffMaxExp based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HmtsRevBackOffMaxExp_Type.__name__ = "Integer32"
_HmtsRevBackOffMaxExp_Object = MibTableColumn
hmtsRevBackOffMaxExp = _HmtsRevBackOffMaxExp_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 2, 6, 1, 17),
    _HmtsRevBackOffMaxExp_Type()
)
hmtsRevBackOffMaxExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsRevBackOffMaxExp.setStatus("current")
_HmtsDeviceGroup_ObjectIdentity = ObjectIdentity
hmtsDeviceGroup = _HmtsDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3)
)
_HmtsDev_Type = Integer32
_HmtsDev_Object = MibScalar
hmtsDev = _HmtsDev_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 1),
    _HmtsDev_Type()
)
hmtsDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDev.setStatus("current")
_HmtsDevInErr_Type = Integer32
_HmtsDevInErr_Object = MibScalar
hmtsDevInErr = _HmtsDevInErr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 2),
    _HmtsDevInErr_Type()
)
hmtsDevInErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevInErr.setStatus("current")


class _HmtsDefaultCommString_Type(DisplayString):
    """Custom type hmtsDefaultCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HmtsDefaultCommString_Type.__name__ = "DisplayString"
_HmtsDefaultCommString_Object = MibScalar
hmtsDefaultCommString = _HmtsDefaultCommString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 3),
    _HmtsDefaultCommString_Type()
)
hmtsDefaultCommString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsDefaultCommString.setStatus("current")
_HmtsComStatAlarm_Type = HmtsComStatCodes
_HmtsComStatAlarm_Object = MibScalar
hmtsComStatAlarm = _HmtsComStatAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 4),
    _HmtsComStatAlarm_Type()
)
hmtsComStatAlarm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsComStatAlarm.setStatus("current")
_HmtsContNRespCount_Type = Integer32
_HmtsContNRespCount_Object = MibScalar
hmtsContNRespCount = _HmtsContNRespCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 5),
    _HmtsContNRespCount_Type()
)
hmtsContNRespCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsContNRespCount.setStatus("current")
_HmtsDevTable_Object = MibTable
hmtsDevTable = _HmtsDevTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    hmtsDevTable.setStatus("current")
_HmtsDevEntry_Object = MibTableRow
hmtsDevEntry = _HmtsDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1)
)
hmtsDevEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsDevPhysAddr"),
)
if mibBuilder.loadTexts:
    hmtsDevEntry.setStatus("current")
_HmtsDevPhysAddr_Type = MacAddress
_HmtsDevPhysAddr_Object = MibTableColumn
hmtsDevPhysAddr = _HmtsDevPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 1),
    _HmtsDevPhysAddr_Type()
)
hmtsDevPhysAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsDevPhysAddr.setStatus("current")
_HmtsDevIPAddr_Type = IpAddress
_HmtsDevIPAddr_Object = MibTableColumn
hmtsDevIPAddr = _HmtsDevIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 2),
    _HmtsDevIPAddr_Type()
)
hmtsDevIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsDevIPAddr.setStatus("current")


class _HmtsDevCommString_Type(DisplayString):
    """Custom type hmtsDevCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HmtsDevCommString_Type.__name__ = "DisplayString"
_HmtsDevCommString_Object = MibTableColumn
hmtsDevCommString = _HmtsDevCommString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 3),
    _HmtsDevCommString_Type()
)
hmtsDevCommString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsDevCommString.setStatus("current")


class _HmtsDevFwdPortId_Type(DisplayString):
    """Custom type hmtsDevFwdPortId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HmtsDevFwdPortId_Type.__name__ = "DisplayString"
_HmtsDevFwdPortId_Object = MibTableColumn
hmtsDevFwdPortId = _HmtsDevFwdPortId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 4),
    _HmtsDevFwdPortId_Type()
)
hmtsDevFwdPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevFwdPortId.setStatus("current")


class _HmtsDevRevPortId_Type(DisplayString):
    """Custom type hmtsDevRevPortId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HmtsDevRevPortId_Type.__name__ = "DisplayString"
_HmtsDevRevPortId_Object = MibTableColumn
hmtsDevRevPortId = _HmtsDevRevPortId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 5),
    _HmtsDevRevPortId_Type()
)
hmtsDevRevPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsDevRevPortId.setStatus("current")
_HmtsDevComStat_Type = HmtsComStatCodes
_HmtsDevComStat_Object = MibTableColumn
hmtsDevComStat = _HmtsDevComStat_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 6),
    _HmtsDevComStat_Type()
)
hmtsDevComStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevComStat.setStatus("current")
_HmtsDevReturnLvl_Type = Integer32
_HmtsDevReturnLvl_Object = MibTableColumn
hmtsDevReturnLvl = _HmtsDevReturnLvl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 7),
    _HmtsDevReturnLvl_Type()
)
hmtsDevReturnLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevReturnLvl.setStatus("current")
if mibBuilder.loadTexts:
    hmtsDevReturnLvl.setUnits("0.1 dBmV")
_HmtsDevLastStateChg_Type = Unsigned32
_HmtsDevLastStateChg_Object = MibTableColumn
hmtsDevLastStateChg = _HmtsDevLastStateChg_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 8),
    _HmtsDevLastStateChg_Type()
)
hmtsDevLastStateChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevLastStateChg.setStatus("current")
_HmtsDevLastRespTime_Type = Unsigned32
_HmtsDevLastRespTime_Object = MibTableColumn
hmtsDevLastRespTime = _HmtsDevLastRespTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 9),
    _HmtsDevLastRespTime_Type()
)
hmtsDevLastRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevLastRespTime.setStatus("current")
_HmtsDevRqstCount_Type = Integer32
_HmtsDevRqstCount_Object = MibTableColumn
hmtsDevRqstCount = _HmtsDevRqstCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 10),
    _HmtsDevRqstCount_Type()
)
hmtsDevRqstCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsDevRqstCount.setStatus("current")
_HmtsDevRespTimeoutCount_Type = Integer32
_HmtsDevRespTimeoutCount_Object = MibTableColumn
hmtsDevRespTimeoutCount = _HmtsDevRespTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 11),
    _HmtsDevRespTimeoutCount_Type()
)
hmtsDevRespTimeoutCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsDevRespTimeoutCount.setStatus("current")
_HmtsDevContNRespCount_Type = Integer32
_HmtsDevContNRespCount_Object = MibTableColumn
hmtsDevContNRespCount = _HmtsDevContNRespCount_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 12),
    _HmtsDevContNRespCount_Type()
)
hmtsDevContNRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevContNRespCount.setStatus("current")


class _HmtsDevRegStatus_Type(Integer32):
    """Custom type hmtsDevRegStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("registered", 1),
          ("registering", 2),
          ("notRegistered", 3))
    )


_HmtsDevRegStatus_Type.__name__ = "Integer32"
_HmtsDevRegStatus_Object = MibTableColumn
hmtsDevRegStatus = _HmtsDevRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 13),
    _HmtsDevRegStatus_Type()
)
hmtsDevRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevRegStatus.setStatus("current")
_HmtsDevRegTime_Type = Unsigned32
_HmtsDevRegTime_Object = MibTableColumn
hmtsDevRegTime = _HmtsDevRegTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 14),
    _HmtsDevRegTime_Type()
)
hmtsDevRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsDevRegTime.setStatus("current")
_HmtsDevRowStatus_Type = RowStatus
_HmtsDevRowStatus_Object = MibTableColumn
hmtsDevRowStatus = _HmtsDevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 6, 1, 15),
    _HmtsDevRowStatus_Type()
)
hmtsDevRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsDevRowStatus.setStatus("current")
_HmtsComFaultTable_Object = MibTable
hmtsComFaultTable = _HmtsComFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    hmtsComFaultTable.setStatus("current")
_HmtsComFaultEntry_Object = MibTableRow
hmtsComFaultEntry = _HmtsComFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 7, 1)
)
hmtsComFaultEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsComStatPhysAddr"),
)
if mibBuilder.loadTexts:
    hmtsComFaultEntry.setStatus("current")
_HmtsComStatPhysAddr_Type = MacAddress
_HmtsComStatPhysAddr_Object = MibTableColumn
hmtsComStatPhysAddr = _HmtsComStatPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 7, 1, 1),
    _HmtsComStatPhysAddr_Type()
)
hmtsComStatPhysAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsComStatPhysAddr.setStatus("current")
_HmtsComStat_Type = HmtsComStatCodes
_HmtsComStat_Object = MibTableColumn
hmtsComStat = _HmtsComStat_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 7, 1, 2),
    _HmtsComStat_Type()
)
hmtsComStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsComStat.setStatus("current")
_HmtsMulticastAddrTable_Object = MibTable
hmtsMulticastAddrTable = _HmtsMulticastAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    hmtsMulticastAddrTable.setStatus("current")
_HmtsMulticastAddrEntry_Object = MibTableRow
hmtsMulticastAddrEntry = _HmtsMulticastAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 8, 1)
)
hmtsMulticastAddrEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsMulticastPhysAddr"),
)
if mibBuilder.loadTexts:
    hmtsMulticastAddrEntry.setStatus("current")
_HmtsMulticastPhysAddr_Type = MacAddress
_HmtsMulticastPhysAddr_Object = MibTableColumn
hmtsMulticastPhysAddr = _HmtsMulticastPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 8, 1, 1),
    _HmtsMulticastPhysAddr_Type()
)
hmtsMulticastPhysAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsMulticastPhysAddr.setStatus("current")
_HmtsMulticastIPAddr_Type = IpAddress
_HmtsMulticastIPAddr_Object = MibTableColumn
hmtsMulticastIPAddr = _HmtsMulticastIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 8, 1, 2),
    _HmtsMulticastIPAddr_Type()
)
hmtsMulticastIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsMulticastIPAddr.setStatus("current")


class _HmtsMulticastCommString_Type(DisplayString):
    """Custom type hmtsMulticastCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HmtsMulticastCommString_Type.__name__ = "DisplayString"
_HmtsMulticastCommString_Object = MibTableColumn
hmtsMulticastCommString = _HmtsMulticastCommString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 8, 1, 3),
    _HmtsMulticastCommString_Type()
)
hmtsMulticastCommString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsMulticastCommString.setStatus("current")
_HmtsMulticastRowStatus_Type = RowStatus
_HmtsMulticastRowStatus_Object = MibTableColumn
hmtsMulticastRowStatus = _HmtsMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 3, 8, 1, 4),
    _HmtsMulticastRowStatus_Type()
)
hmtsMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsMulticastRowStatus.setStatus("current")
_HmtsIPGroup_ObjectIdentity = ObjectIdentity
hmtsIPGroup = _HmtsIPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4)
)


class _HmtsIPManagementMethod_Type(Integer32):
    """Custom type hmtsIPManagementMethod based on Integer32"""
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
        *(("client", 1),
          ("manualXp", 2),
          ("manualHmts", 3),
          ("automatic", 4))
    )


_HmtsIPManagementMethod_Type.__name__ = "Integer32"
_HmtsIPManagementMethod_Object = MibScalar
hmtsIPManagementMethod = _HmtsIPManagementMethod_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 1),
    _HmtsIPManagementMethod_Type()
)
hmtsIPManagementMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsIPManagementMethod.setStatus("current")
_HmtsIPDevTable_Object = MibTable
hmtsIPDevTable = _HmtsIPDevTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hmtsIPDevTable.setStatus("current")
_HmtsIPDevEntry_Object = MibTableRow
hmtsIPDevEntry = _HmtsIPDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 2, 1)
)
hmtsIPDevEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsIPDevAddr"),
)
if mibBuilder.loadTexts:
    hmtsIPDevEntry.setStatus("current")
_HmtsIPDevAddr_Type = IpAddress
_HmtsIPDevAddr_Object = MibTableColumn
hmtsIPDevAddr = _HmtsIPDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 2, 1, 1),
    _HmtsIPDevAddr_Type()
)
hmtsIPDevAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsIPDevAddr.setStatus("current")
_HmtsIPPhysAddr_Type = MacAddress
_HmtsIPPhysAddr_Object = MibTableColumn
hmtsIPPhysAddr = _HmtsIPPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 2, 1, 2),
    _HmtsIPPhysAddr_Type()
)
hmtsIPPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsIPPhysAddr.setStatus("current")
_HmtsNetAddrTable_Object = MibTable
hmtsNetAddrTable = _HmtsNetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hmtsNetAddrTable.setStatus("current")
_HmtsNetAddrEntry_Object = MibTableRow
hmtsNetAddrEntry = _HmtsNetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 3, 1)
)
hmtsNetAddrEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsNetStartAddr"),
)
if mibBuilder.loadTexts:
    hmtsNetAddrEntry.setStatus("current")
_HmtsNetStartAddr_Type = IpAddress
_HmtsNetStartAddr_Object = MibTableColumn
hmtsNetStartAddr = _HmtsNetStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 3, 1, 1),
    _HmtsNetStartAddr_Type()
)
hmtsNetStartAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsNetStartAddr.setStatus("current")
_HmtsNetEndAddr_Type = IpAddress
_HmtsNetEndAddr_Object = MibTableColumn
hmtsNetEndAddr = _HmtsNetEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 3, 1, 2),
    _HmtsNetEndAddr_Type()
)
hmtsNetEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsNetEndAddr.setStatus("current")
_HmtsNetMask_Type = IpAddress
_HmtsNetMask_Object = MibTableColumn
hmtsNetMask = _HmtsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 3, 1, 3),
    _HmtsNetMask_Type()
)
hmtsNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsNetMask.setStatus("current")
_HmtsNetRowStatus_Type = RowStatus
_HmtsNetRowStatus_Object = MibTableColumn
hmtsNetRowStatus = _HmtsNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 4, 3, 1, 4),
    _HmtsNetRowStatus_Type()
)
hmtsNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmtsNetRowStatus.setStatus("current")
_HmtsCommGroup_ObjectIdentity = ObjectIdentity
hmtsCommGroup = _HmtsCommGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 5)
)


class _HmtsCommManagementMethod_Type(Integer32):
    """Custom type hmtsCommManagementMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_HmtsCommManagementMethod_Type.__name__ = "Integer32"
_HmtsCommManagementMethod_Object = MibScalar
hmtsCommManagementMethod = _HmtsCommManagementMethod_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 5, 1),
    _HmtsCommManagementMethod_Type()
)
hmtsCommManagementMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmtsCommManagementMethod.setStatus("current")
_HmtsCommDevTable_Object = MibTable
hmtsCommDevTable = _HmtsCommDevTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hmtsCommDevTable.setStatus("current")
_HmtsCommDevEntry_Object = MibTableRow
hmtsCommDevEntry = _HmtsCommDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 5, 2, 1)
)
hmtsCommDevEntry.setIndexNames(
    (0, "SCTE-HMS-HMTS-MIB", "hmtsCommString"),
)
if mibBuilder.loadTexts:
    hmtsCommDevEntry.setStatus("current")


class _HmtsCommString_Type(DisplayString):
    """Custom type hmtsCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HmtsCommString_Type.__name__ = "DisplayString"
_HmtsCommString_Object = MibTableColumn
hmtsCommString = _HmtsCommString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 5, 2, 1, 1),
    _HmtsCommString_Type()
)
hmtsCommString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmtsCommString.setStatus("current")
_HmtsCommPhysAddr_Type = MacAddress
_HmtsCommPhysAddr_Object = MibTableColumn
hmtsCommPhysAddr = _HmtsCommPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 5, 2, 1, 2),
    _HmtsCommPhysAddr_Type()
)
hmtsCommPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmtsCommPhysAddr.setStatus("current")
_HeHMTSConformance_ObjectIdentity = ObjectIdentity
heHMTSConformance = _HeHMTSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2)
)
_HmtsCompliances_ObjectIdentity = ObjectIdentity
hmtsCompliances = _HmtsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 1)
)
_HmtsGroups_ObjectIdentity = ObjectIdentity
hmtsGroups = _HmtsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2)
)

# Managed Objects groups

hmtsReqManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 1)
)
hmtsReqManagementGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsRegInterval"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRegContinuity"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdPortAdminState"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdPortDescr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdPortOperState"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdPortType"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdHmtsFrequency"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdXpndrFrequency"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevPortAdminState"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevFwdPortId"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevPortDescr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevPortType"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevFrequency"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevPortOperState"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevReturnLvl"))
)
if mibBuilder.loadTexts:
    hmtsReqManagementGroup.setStatus("current")

hmtsReqDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 2)
)
hmtsReqDeviceGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsDev"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevInErr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDefaultCommString"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevComStat"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevIPAddr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevCommString"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevFwdPortId"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevRevPortId"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevReturnLvl"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevLastStateChg"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevLastRespTime"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevRqstCount"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevRespTimeoutCount"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevContNRespCount"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevRegStatus"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevRegTime"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDevRowStatus"),
        ("SCTE-HMS-HMTS-MIB", "hmtsComStat"),
        ("SCTE-HMS-HMTS-MIB", "hmtsMulticastRowStatus"))
)
if mibBuilder.loadTexts:
    hmtsReqDeviceGroup.setStatus("current")

hmtsIPDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 3)
)
hmtsIPDeviceGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsMulticastIPAddr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsIPManagementMethod"),
        ("SCTE-HMS-HMTS-MIB", "hmtsIPPhysAddr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsNetEndAddr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsNetMask"),
        ("SCTE-HMS-HMTS-MIB", "hmtsNetRowStatus"))
)
if mibBuilder.loadTexts:
    hmtsIPDeviceGroup.setStatus("current")

hmtsCommDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 4)
)
hmtsCommDeviceGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsDefaultCommString"),
        ("SCTE-HMS-HMTS-MIB", "hmtsMulticastCommString"),
        ("SCTE-HMS-HMTS-MIB", "hmtsCommManagementMethod"),
        ("SCTE-HMS-HMTS-MIB", "hmtsCommPhysAddr"))
)
if mibBuilder.loadTexts:
    hmtsCommDeviceGroup.setStatus("current")

hmtsInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 5)
)
hmtsInformationGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsAdminState"),
        ("SCTE-HMS-HMTS-MIB", "hmtsOperState"),
        ("SCTE-HMS-HMTS-MIB", "hmtsProxyType"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFreqSwitchMethod"),
        ("SCTE-HMS-HMTS-MIB", "hmtsModel"),
        ("SCTE-HMS-HMTS-MIB", "hmtsSerialNumber"),
        ("SCTE-HMS-HMTS-MIB", "hmtsSoftwareVersion"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTimeServerAddress"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTimeServerSyncInterval"))
)
if mibBuilder.loadTexts:
    hmtsInformationGroup.setStatus("current")

hmtsMacProtocolInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 6)
)
hmtsMacProtocolInformationGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsMacPduTimeout"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTalkPduTimeout"),
        ("SCTE-HMS-HMTS-MIB", "hmtsMacBroadcastDelay"),
        ("SCTE-HMS-HMTS-MIB", "hmtsAlarmDiscoveryMode"),
        ("SCTE-HMS-HMTS-MIB", "hmtsChnldescPduInt"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTimePduInt"),
        ("SCTE-HMS-HMTS-MIB", "hmtsDeviceAccessMode"))
)
if mibBuilder.loadTexts:
    hmtsMacProtocolInformationGroup.setStatus("current")

hmtsSnmpProtocolInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 7)
)
hmtsSnmpProtocolInformationGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsSnmpTimeout"),
        ("SCTE-HMS-HMTS-MIB", "hmtsSnmpBroadcastDelay"))
)
if mibBuilder.loadTexts:
    hmtsSnmpProtocolInformationGroup.setStatus("current")

hmtsExtendedRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 8)
)
hmtsExtendedRegistrationGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsRegMinDuration"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRegMaxDuration"))
)
if mibBuilder.loadTexts:
    hmtsExtendedRegistrationGroup.setStatus("current")

hmtsTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 9)
)
hmtsTrapControlGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsTControlInterval"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTControlMinDuration"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTControlChainId"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTControlContinuity"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTControlRowStatus"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTControlMulticastAddr"))
)
if mibBuilder.loadTexts:
    hmtsTrapControlGroup.setStatus("current")

hmtsExtendedTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 10)
)
hmtsExtendedTrapControlGroup.setObjects(
    ("SCTE-HMS-HMTS-MIB", "hmtsTControlMaxDuration")
)
if mibBuilder.loadTexts:
    hmtsExtendedTrapControlGroup.setStatus("current")

hmtsExtendedFwdPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 11)
)
hmtsExtendedFwdPortGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsFwdProvPwrLvl"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdMaxPwrLvl"),
        ("SCTE-HMS-HMTS-MIB", "hmtsFwdPollTime"))
)
if mibBuilder.loadTexts:
    hmtsExtendedFwdPortGroup.setStatus("current")

hmtsExtendedRevPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 12)
)
hmtsExtendedRevPortGroup.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsRevMuteLvl"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevMulticastAddr"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevFrameErrors"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevCRCErrors"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevBackOffPeriod"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevACKTimeout"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevMaxMACRetries"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevBackOffMinExp"),
        ("SCTE-HMS-HMTS-MIB", "hmtsRevBackOffMaxExp"))
)
if mibBuilder.loadTexts:
    hmtsExtendedRevPortGroup.setStatus("current")

hmtsEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 2, 13)
)
hmtsEventGroup.setObjects(
    ("SCTE-HMS-HMTS-MIB", "hmtsRegistrationFailedEvent")
)
if mibBuilder.loadTexts:
    hmtsEventGroup.setStatus("current")


# Notification objects

hmtsRegistrationFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 1, 0, 1)
)
hmtsRegistrationFailedEvent.setObjects(
    ("SCTE-HMS-HMTS-MIB", "hmtsDevComStat")
)
if mibBuilder.loadTexts:
    hmtsRegistrationFailedEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

heHMTSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3, 2, 2, 1, 1)
)
heHMTSCompliance.setObjects(
      *(("SCTE-HMS-HMTS-MIB", "hmtsInformationGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsMacProtocolInformationGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsSnmpProtocolInformationGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsReqManagementGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsReqDeviceGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsEventGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsIPDeviceGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsCommDeviceGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsExtendedRegistrationGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsTrapControlGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsExtendedTrapControlGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsExtendedFwdPortGroup"),
        ("SCTE-HMS-HMTS-MIB", "hmtsExtendedRevPortGroup"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonTime"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonAlarmDetectionControl"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonParamsGroup"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogGroup"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonNotificationsGroup"),
        ("ENTITY-MIB", "entityPhysicalGroup"),
        ("ENTITY-MIB", "entityPhysical2Group"),
        ("ENTITY-MIB", "entityGeneralGroup"),
        ("ENTITY-MIB", "entityNotificationsGroup"),
        ("SNMP-TARGET-MIB", "snmpTargetBasicGroup"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup"),
        ("SNMPv2-MIB", "systemGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "analogAlarmsGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "discreteAlarmsGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "currentAlarmsGroup"))
)
if mibBuilder.loadTexts:
    heHMTSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HMTS-MIB",
    **{"HmtsComStatCodes": HmtsComStatCodes,
       "heHMTSMIB": heHMTSMIB,
       "heHMTSObjects": heHMTSObjects,
       "hmtsNotifications": hmtsNotifications,
       "hmtsRegistrationFailedEvent": hmtsRegistrationFailedEvent,
       "hmtsInfoGroup": hmtsInfoGroup,
       "hmtsAdminState": hmtsAdminState,
       "hmtsOperState": hmtsOperState,
       "hmtsProxyType": hmtsProxyType,
       "hmtsFreqSwitchMethod": hmtsFreqSwitchMethod,
       "hmtsModel": hmtsModel,
       "hmtsSerialNumber": hmtsSerialNumber,
       "hmtsSoftwareVersion": hmtsSoftwareVersion,
       "hmtsTimeServerAddress": hmtsTimeServerAddress,
       "hmtsTimeServerSyncInterval": hmtsTimeServerSyncInterval,
       "hmtsManagementGroup": hmtsManagementGroup,
       "hmtsMacPduGroup": hmtsMacPduGroup,
       "hmtsMacPduTimeout": hmtsMacPduTimeout,
       "hmtsTalkPduTimeout": hmtsTalkPduTimeout,
       "hmtsMacBroadcastDelay": hmtsMacBroadcastDelay,
       "hmtsAlarmDiscoveryMode": hmtsAlarmDiscoveryMode,
       "hmtsChnldescPduInt": hmtsChnldescPduInt,
       "hmtsTimePduInt": hmtsTimePduInt,
       "hmtsDeviceAccessMode": hmtsDeviceAccessMode,
       "hmtsRegistrationGroup": hmtsRegistrationGroup,
       "hmtsRegInterval": hmtsRegInterval,
       "hmtsRegMinDuration": hmtsRegMinDuration,
       "hmtsRegMaxDuration": hmtsRegMaxDuration,
       "hmtsRegContinuity": hmtsRegContinuity,
       "hmtsSnmpTrapControlGroup": hmtsSnmpTrapControlGroup,
       "hmtsTrapControlTable": hmtsTrapControlTable,
       "hmtsTrapControlEntry": hmtsTrapControlEntry,
       "hmtsTControlId": hmtsTControlId,
       "hmtsTControlInterval": hmtsTControlInterval,
       "hmtsTControlChainId": hmtsTControlChainId,
       "hmtsTControlMinDuration": hmtsTControlMinDuration,
       "hmtsTControlMaxDuration": hmtsTControlMaxDuration,
       "hmtsTControlContinuity": hmtsTControlContinuity,
       "hmtsTControlMulticastAddr": hmtsTControlMulticastAddr,
       "hmtsTControlRowStatus": hmtsTControlRowStatus,
       "hmtsSnmpProtocolGroup": hmtsSnmpProtocolGroup,
       "hmtsSnmpTimeout": hmtsSnmpTimeout,
       "hmtsSnmpBroadcastDelay": hmtsSnmpBroadcastDelay,
       "hmtsFwdPortTable": hmtsFwdPortTable,
       "hmtsFwdPortEntry": hmtsFwdPortEntry,
       "hmtsFwdPortId": hmtsFwdPortId,
       "hmtsFwdPortDescr": hmtsFwdPortDescr,
       "hmtsFwdPortType": hmtsFwdPortType,
       "hmtsFwdPortAdminState": hmtsFwdPortAdminState,
       "hmtsFwdPortOperState": hmtsFwdPortOperState,
       "hmtsFwdHmtsFrequency": hmtsFwdHmtsFrequency,
       "hmtsFwdXpndrFrequency": hmtsFwdXpndrFrequency,
       "hmtsFwdProvPwrLvl": hmtsFwdProvPwrLvl,
       "hmtsFwdMaxPwrLvl": hmtsFwdMaxPwrLvl,
       "hmtsFwdPollTime": hmtsFwdPollTime,
       "hmtsRevPortTable": hmtsRevPortTable,
       "hmtsRevPortEntry": hmtsRevPortEntry,
       "hmtsRevPortId": hmtsRevPortId,
       "hmtsRevFwdPortId": hmtsRevFwdPortId,
       "hmtsRevPortDescr": hmtsRevPortDescr,
       "hmtsRevPortType": hmtsRevPortType,
       "hmtsRevPortAdminState": hmtsRevPortAdminState,
       "hmtsRevPortOperState": hmtsRevPortOperState,
       "hmtsRevFrequency": hmtsRevFrequency,
       "hmtsRevMuteLvl": hmtsRevMuteLvl,
       "hmtsRevMulticastAddr": hmtsRevMulticastAddr,
       "hmtsRevReturnLvl": hmtsRevReturnLvl,
       "hmtsRevCRCErrors": hmtsRevCRCErrors,
       "hmtsRevFrameErrors": hmtsRevFrameErrors,
       "hmtsRevBackOffPeriod": hmtsRevBackOffPeriod,
       "hmtsRevACKTimeout": hmtsRevACKTimeout,
       "hmtsRevMaxMACRetries": hmtsRevMaxMACRetries,
       "hmtsRevBackOffMinExp": hmtsRevBackOffMinExp,
       "hmtsRevBackOffMaxExp": hmtsRevBackOffMaxExp,
       "hmtsDeviceGroup": hmtsDeviceGroup,
       "hmtsDev": hmtsDev,
       "hmtsDevInErr": hmtsDevInErr,
       "hmtsDefaultCommString": hmtsDefaultCommString,
       "hmtsComStatAlarm": hmtsComStatAlarm,
       "hmtsContNRespCount": hmtsContNRespCount,
       "hmtsDevTable": hmtsDevTable,
       "hmtsDevEntry": hmtsDevEntry,
       "hmtsDevPhysAddr": hmtsDevPhysAddr,
       "hmtsDevIPAddr": hmtsDevIPAddr,
       "hmtsDevCommString": hmtsDevCommString,
       "hmtsDevFwdPortId": hmtsDevFwdPortId,
       "hmtsDevRevPortId": hmtsDevRevPortId,
       "hmtsDevComStat": hmtsDevComStat,
       "hmtsDevReturnLvl": hmtsDevReturnLvl,
       "hmtsDevLastStateChg": hmtsDevLastStateChg,
       "hmtsDevLastRespTime": hmtsDevLastRespTime,
       "hmtsDevRqstCount": hmtsDevRqstCount,
       "hmtsDevRespTimeoutCount": hmtsDevRespTimeoutCount,
       "hmtsDevContNRespCount": hmtsDevContNRespCount,
       "hmtsDevRegStatus": hmtsDevRegStatus,
       "hmtsDevRegTime": hmtsDevRegTime,
       "hmtsDevRowStatus": hmtsDevRowStatus,
       "hmtsComFaultTable": hmtsComFaultTable,
       "hmtsComFaultEntry": hmtsComFaultEntry,
       "hmtsComStatPhysAddr": hmtsComStatPhysAddr,
       "hmtsComStat": hmtsComStat,
       "hmtsMulticastAddrTable": hmtsMulticastAddrTable,
       "hmtsMulticastAddrEntry": hmtsMulticastAddrEntry,
       "hmtsMulticastPhysAddr": hmtsMulticastPhysAddr,
       "hmtsMulticastIPAddr": hmtsMulticastIPAddr,
       "hmtsMulticastCommString": hmtsMulticastCommString,
       "hmtsMulticastRowStatus": hmtsMulticastRowStatus,
       "hmtsIPGroup": hmtsIPGroup,
       "hmtsIPManagementMethod": hmtsIPManagementMethod,
       "hmtsIPDevTable": hmtsIPDevTable,
       "hmtsIPDevEntry": hmtsIPDevEntry,
       "hmtsIPDevAddr": hmtsIPDevAddr,
       "hmtsIPPhysAddr": hmtsIPPhysAddr,
       "hmtsNetAddrTable": hmtsNetAddrTable,
       "hmtsNetAddrEntry": hmtsNetAddrEntry,
       "hmtsNetStartAddr": hmtsNetStartAddr,
       "hmtsNetEndAddr": hmtsNetEndAddr,
       "hmtsNetMask": hmtsNetMask,
       "hmtsNetRowStatus": hmtsNetRowStatus,
       "hmtsCommGroup": hmtsCommGroup,
       "hmtsCommManagementMethod": hmtsCommManagementMethod,
       "hmtsCommDevTable": hmtsCommDevTable,
       "hmtsCommDevEntry": hmtsCommDevEntry,
       "hmtsCommString": hmtsCommString,
       "hmtsCommPhysAddr": hmtsCommPhysAddr,
       "heHMTSConformance": heHMTSConformance,
       "hmtsCompliances": hmtsCompliances,
       "heHMTSCompliance": heHMTSCompliance,
       "hmtsGroups": hmtsGroups,
       "hmtsReqManagementGroup": hmtsReqManagementGroup,
       "hmtsReqDeviceGroup": hmtsReqDeviceGroup,
       "hmtsIPDeviceGroup": hmtsIPDeviceGroup,
       "hmtsCommDeviceGroup": hmtsCommDeviceGroup,
       "hmtsInformationGroup": hmtsInformationGroup,
       "hmtsMacProtocolInformationGroup": hmtsMacProtocolInformationGroup,
       "hmtsSnmpProtocolInformationGroup": hmtsSnmpProtocolInformationGroup,
       "hmtsExtendedRegistrationGroup": hmtsExtendedRegistrationGroup,
       "hmtsTrapControlGroup": hmtsTrapControlGroup,
       "hmtsExtendedTrapControlGroup": hmtsExtendedTrapControlGroup,
       "hmtsExtendedFwdPortGroup": hmtsExtendedFwdPortGroup,
       "hmtsExtendedRevPortGroup": hmtsExtendedRevPortGroup,
       "hmtsEventGroup": hmtsEventGroup}
)
