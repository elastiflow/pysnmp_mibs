# SNMP MIB module (DNOS-NSF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-NSF-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:25:39 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(agentInventoryUnitEntry,
 agentInventoryUnitNumber) = mibBuilder.importSymbols(
    "DNOS-INVENTORY-MIB",
    "agentInventoryUnitEntry",
    "agentInventoryUnitNumber")

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

fastPathNsf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46)
)
if mibBuilder.loadTexts:
    fastPathNsf.setRevisions(
        ("2011-01-26 00:00",
         "2009-04-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentNsfTraps_ObjectIdentity = ObjectIdentity
agentNsfTraps = _AgentNsfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 0)
)
_AgentNsfUnitTable_Object = MibTable
agentNsfUnitTable = _AgentNsfUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 1)
)
if mibBuilder.loadTexts:
    agentNsfUnitTable.setStatus("current")
_AgentNsfUnitEntry_Object = MibTableRow
agentNsfUnitEntry = _AgentNsfUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 1, 1)
)
if mibBuilder.loadTexts:
    agentNsfUnitEntry.setStatus("current")
_AgentNsfUnitSupport_Type = TruthValue
_AgentNsfUnitSupport_Object = MibTableColumn
agentNsfUnitSupport = _AgentNsfUnitSupport_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 1, 1, 1),
    _AgentNsfUnitSupport_Type()
)
agentNsfUnitSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfUnitSupport.setStatus("current")
_AgentNsfGroup_ObjectIdentity = ObjectIdentity
agentNsfGroup = _AgentNsfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2)
)


class _AgentNsfAdminStatus_Type(Integer32):
    """Custom type agentNsfAdminStatus based on Integer32"""
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


_AgentNsfAdminStatus_Type.__name__ = "Integer32"
_AgentNsfAdminStatus_Object = MibScalar
agentNsfAdminStatus = _AgentNsfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 1),
    _AgentNsfAdminStatus_Type()
)
agentNsfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNsfAdminStatus.setStatus("current")


class _AgentNsfOperStatus_Type(Integer32):
    """Custom type agentNsfOperStatus based on Integer32"""
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


_AgentNsfOperStatus_Type.__name__ = "Integer32"
_AgentNsfOperStatus_Object = MibScalar
agentNsfOperStatus = _AgentNsfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 2),
    _AgentNsfOperStatus_Type()
)
agentNsfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfOperStatus.setStatus("current")


class _AgentNsfLastStartupReason_Type(Integer32):
    """Custom type agentNsfLastStartupReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("power-on", 2),
          ("warm-admin-move", 3),
          ("cold-admin-move", 4),
          ("warm-auto-restart", 5),
          ("cold-auto-restart", 6))
    )


_AgentNsfLastStartupReason_Type.__name__ = "Integer32"
_AgentNsfLastStartupReason_Object = MibScalar
agentNsfLastStartupReason = _AgentNsfLastStartupReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 3),
    _AgentNsfLastStartupReason_Type()
)
agentNsfLastStartupReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfLastStartupReason.setStatus("current")
_AgentNsfTimeSinceLastRestart_Type = TimeTicks
_AgentNsfTimeSinceLastRestart_Object = MibScalar
agentNsfTimeSinceLastRestart = _AgentNsfTimeSinceLastRestart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 4),
    _AgentNsfTimeSinceLastRestart_Type()
)
agentNsfTimeSinceLastRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfTimeSinceLastRestart.setStatus("current")
_AgentNsfRestartInProgress_Type = TruthValue
_AgentNsfRestartInProgress_Object = MibScalar
agentNsfRestartInProgress = _AgentNsfRestartInProgress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 5),
    _AgentNsfRestartInProgress_Type()
)
agentNsfRestartInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfRestartInProgress.setStatus("current")
_AgentNsfWarmRestartReady_Type = TruthValue
_AgentNsfWarmRestartReady_Object = MibScalar
agentNsfWarmRestartReady = _AgentNsfWarmRestartReady_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 6),
    _AgentNsfWarmRestartReady_Type()
)
agentNsfWarmRestartReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfWarmRestartReady.setStatus("current")
_AgentNsfBackupConfigurationAge_Type = TimeTicks
_AgentNsfBackupConfigurationAge_Object = MibScalar
agentNsfBackupConfigurationAge = _AgentNsfBackupConfigurationAge_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 7),
    _AgentNsfBackupConfigurationAge_Type()
)
agentNsfBackupConfigurationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfBackupConfigurationAge.setStatus("current")


class _AgentNsfInitiateFailover_Type(Integer32):
    """Custom type agentNsfInitiateFailover based on Integer32"""
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


_AgentNsfInitiateFailover_Type.__name__ = "Integer32"
_AgentNsfInitiateFailover_Object = MibScalar
agentNsfInitiateFailover = _AgentNsfInitiateFailover_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 2, 8),
    _AgentNsfInitiateFailover_Type()
)
agentNsfInitiateFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNsfInitiateFailover.setStatus("current")
_AgentCheckpointStatsGroup_ObjectIdentity = ObjectIdentity
agentCheckpointStatsGroup = _AgentCheckpointStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3)
)


class _AgentCheckpointClearStatistics_Type(Integer32):
    """Custom type agentCheckpointClearStatistics based on Integer32"""
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


_AgentCheckpointClearStatistics_Type.__name__ = "Integer32"
_AgentCheckpointClearStatistics_Object = MibScalar
agentCheckpointClearStatistics = _AgentCheckpointClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3, 1),
    _AgentCheckpointClearStatistics_Type()
)
agentCheckpointClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCheckpointClearStatistics.setStatus("current")
_AgentCheckpointMessages_Type = Counter32
_AgentCheckpointMessages_Object = MibScalar
agentCheckpointMessages = _AgentCheckpointMessages_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3, 2),
    _AgentCheckpointMessages_Type()
)
agentCheckpointMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCheckpointMessages.setStatus("current")
_AgentCheckpointBytes_Type = Counter32
_AgentCheckpointBytes_Object = MibScalar
agentCheckpointBytes = _AgentCheckpointBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3, 3),
    _AgentCheckpointBytes_Type()
)
agentCheckpointBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCheckpointBytes.setStatus("current")
_AgentCheckpointTimeSinceCountersCleared_Type = TimeTicks
_AgentCheckpointTimeSinceCountersCleared_Object = MibScalar
agentCheckpointTimeSinceCountersCleared = _AgentCheckpointTimeSinceCountersCleared_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3, 4),
    _AgentCheckpointTimeSinceCountersCleared_Type()
)
agentCheckpointTimeSinceCountersCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCheckpointTimeSinceCountersCleared.setStatus("current")
_AgentCheckpointMessageRateInterval_Type = Unsigned32
_AgentCheckpointMessageRateInterval_Object = MibScalar
agentCheckpointMessageRateInterval = _AgentCheckpointMessageRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3, 5),
    _AgentCheckpointMessageRateInterval_Type()
)
agentCheckpointMessageRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCheckpointMessageRateInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentCheckpointMessageRateInterval.setUnits("seconds")
_AgentCheckpointMessageRate_Type = Gauge32
_AgentCheckpointMessageRate_Object = MibScalar
agentCheckpointMessageRate = _AgentCheckpointMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3, 6),
    _AgentCheckpointMessageRate_Type()
)
agentCheckpointMessageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCheckpointMessageRate.setStatus("current")
_AgentCheckpointHighestMessageRate_Type = Gauge32
_AgentCheckpointHighestMessageRate_Object = MibScalar
agentCheckpointHighestMessageRate = _AgentCheckpointHighestMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 3, 7),
    _AgentCheckpointHighestMessageRate_Type()
)
agentCheckpointHighestMessageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCheckpointHighestMessageRate.setStatus("current")
_AgentNsfOspfGroup_ObjectIdentity = ObjectIdentity
agentNsfOspfGroup = _AgentNsfOspfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4)
)


class _AgentNsfOspfSupportMode_Type(Integer32):
    """Custom type agentNsfOspfSupportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("planned", 2),
          ("always", 3))
    )


_AgentNsfOspfSupportMode_Type.__name__ = "Integer32"
_AgentNsfOspfSupportMode_Object = MibScalar
agentNsfOspfSupportMode = _AgentNsfOspfSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4, 1),
    _AgentNsfOspfSupportMode_Type()
)
agentNsfOspfSupportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNsfOspfSupportMode.setStatus("current")
_AgentNsfOspfRestartInterval_Type = Unsigned32
_AgentNsfOspfRestartInterval_Object = MibScalar
agentNsfOspfRestartInterval = _AgentNsfOspfRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4, 2),
    _AgentNsfOspfRestartInterval_Type()
)
agentNsfOspfRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNsfOspfRestartInterval.setStatus("current")


class _AgentNsfOspfRestartStatus_Type(Integer32):
    """Custom type agentNsfOspfRestartStatus based on Integer32"""
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
        *(("unknown", 1),
          ("not-restarting", 2),
          ("planned-restart", 3),
          ("unplanned-restart", 4))
    )


_AgentNsfOspfRestartStatus_Type.__name__ = "Integer32"
_AgentNsfOspfRestartStatus_Object = MibScalar
agentNsfOspfRestartStatus = _AgentNsfOspfRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4, 3),
    _AgentNsfOspfRestartStatus_Type()
)
agentNsfOspfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfOspfRestartStatus.setStatus("current")
_AgentNsfOspfRestartAge_Type = TimeTicks
_AgentNsfOspfRestartAge_Object = MibScalar
agentNsfOspfRestartAge = _AgentNsfOspfRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4, 4),
    _AgentNsfOspfRestartAge_Type()
)
agentNsfOspfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfOspfRestartAge.setStatus("current")


class _AgentNsfOspfRestartExitReason_Type(Integer32):
    """Custom type agentNsfOspfRestartExitReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("in-progress", 2),
          ("completed", 3),
          ("timed-out", 4),
          ("topology-change", 5),
          ("manual-clear", 6))
    )


_AgentNsfOspfRestartExitReason_Type.__name__ = "Integer32"
_AgentNsfOspfRestartExitReason_Object = MibScalar
agentNsfOspfRestartExitReason = _AgentNsfOspfRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4, 5),
    _AgentNsfOspfRestartExitReason_Type()
)
agentNsfOspfRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNsfOspfRestartExitReason.setStatus("current")


class _AgentNsfOspfHelperSupportMode_Type(Integer32):
    """Custom type agentNsfOspfHelperSupportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("planned", 2),
          ("always", 3))
    )


_AgentNsfOspfHelperSupportMode_Type.__name__ = "Integer32"
_AgentNsfOspfHelperSupportMode_Object = MibScalar
agentNsfOspfHelperSupportMode = _AgentNsfOspfHelperSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4, 6),
    _AgentNsfOspfHelperSupportMode_Type()
)
agentNsfOspfHelperSupportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNsfOspfHelperSupportMode.setStatus("current")


class _AgentNsfOspfHelperStrictLSAChecking_Type(Integer32):
    """Custom type agentNsfOspfHelperStrictLSAChecking based on Integer32"""
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


_AgentNsfOspfHelperStrictLSAChecking_Type.__name__ = "Integer32"
_AgentNsfOspfHelperStrictLSAChecking_Object = MibScalar
agentNsfOspfHelperStrictLSAChecking = _AgentNsfOspfHelperStrictLSAChecking_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 4, 7),
    _AgentNsfOspfHelperStrictLSAChecking_Type()
)
agentNsfOspfHelperStrictLSAChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNsfOspfHelperStrictLSAChecking.setStatus("current")
agentInventoryUnitEntry.registerAugmentions(
    ("DNOS-NSF-MIB",
     "agentNsfUnitEntry")
)
agentNsfUnitEntry.setIndexNames(*agentInventoryUnitEntry.getIndexNames())

# Managed Objects groups


# Notification objects

agentNsfStackRestartComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 46, 0, 1)
)
agentNsfStackRestartComplete.setObjects(
      *(("DNOS-INVENTORY-MIB", "agentInventoryUnitNumber"),
        ("DNOS-NSF-MIB", "agentNsfLastStartupReason"))
)
if mibBuilder.loadTexts:
    agentNsfStackRestartComplete.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-NSF-MIB",
    **{"fastPathNsf": fastPathNsf,
       "agentNsfTraps": agentNsfTraps,
       "agentNsfStackRestartComplete": agentNsfStackRestartComplete,
       "agentNsfUnitTable": agentNsfUnitTable,
       "agentNsfUnitEntry": agentNsfUnitEntry,
       "agentNsfUnitSupport": agentNsfUnitSupport,
       "agentNsfGroup": agentNsfGroup,
       "agentNsfAdminStatus": agentNsfAdminStatus,
       "agentNsfOperStatus": agentNsfOperStatus,
       "agentNsfLastStartupReason": agentNsfLastStartupReason,
       "agentNsfTimeSinceLastRestart": agentNsfTimeSinceLastRestart,
       "agentNsfRestartInProgress": agentNsfRestartInProgress,
       "agentNsfWarmRestartReady": agentNsfWarmRestartReady,
       "agentNsfBackupConfigurationAge": agentNsfBackupConfigurationAge,
       "agentNsfInitiateFailover": agentNsfInitiateFailover,
       "agentCheckpointStatsGroup": agentCheckpointStatsGroup,
       "agentCheckpointClearStatistics": agentCheckpointClearStatistics,
       "agentCheckpointMessages": agentCheckpointMessages,
       "agentCheckpointBytes": agentCheckpointBytes,
       "agentCheckpointTimeSinceCountersCleared": agentCheckpointTimeSinceCountersCleared,
       "agentCheckpointMessageRateInterval": agentCheckpointMessageRateInterval,
       "agentCheckpointMessageRate": agentCheckpointMessageRate,
       "agentCheckpointHighestMessageRate": agentCheckpointHighestMessageRate,
       "agentNsfOspfGroup": agentNsfOspfGroup,
       "agentNsfOspfSupportMode": agentNsfOspfSupportMode,
       "agentNsfOspfRestartInterval": agentNsfOspfRestartInterval,
       "agentNsfOspfRestartStatus": agentNsfOspfRestartStatus,
       "agentNsfOspfRestartAge": agentNsfOspfRestartAge,
       "agentNsfOspfRestartExitReason": agentNsfOspfRestartExitReason,
       "agentNsfOspfHelperSupportMode": agentNsfOspfHelperSupportMode,
       "agentNsfOspfHelperStrictLSAChecking": agentNsfOspfHelperStrictLSAChecking}
)
