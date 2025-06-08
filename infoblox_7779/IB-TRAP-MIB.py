# SNMP MIB module (IB-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/infoblox_7779/IB-TRAP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:44:05 2025
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

(IbNode,
 IbString,
 ibTrapOne) = mibBuilder.importSymbols(
    "IB-SMI-MIB",
    "IbNode",
    "IbString",
    "ibTrapOne")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ibTrapOneModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ibTrapOneModule.setRevisions(
        ("2010-10-10 00:00",
         "2010-05-21 00:00",
         "2010-04-16 00:00",
         "2010-03-23 00:00",
         "2008-02-28 00:00",
         "2008-02-04 00:00",
         "2005-04-17 00:00",
         "2005-01-10 00:00",
         "2004-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IbState(TextualConvention, Integer32):
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ha-active", 1),
          ("ha-passive", 2),
          ("ha-initial", 3),
          ("grid-connected", 4),
          ("grid-disconnected", 5),
          ("enet-link-up", 6),
          ("enet-link-down", 7),
          ("replication-online", 8),
          ("replication-offline", 9),
          ("replication-snapshotting", 10),
          ("service-up", 11),
          ("service-down", 12),
          ("ha-replication-online", 13),
          ("ha-replication-offline", 14),
          ("ntp-sync-up", 15),
          ("ntp-sync-down", 16),
          ("ms-server-up", 17),
          ("ms-server-down", 18),
          ("ms-service-up", 19),
          ("ms-service-down", 20),
          ("nac-server-group-down", 21),
          ("nac-server-group-up", 22))
    )



class IbProbableCause(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              11,
              12,
              13,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              44,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006)
        )
    )
    namedValues = NamedValues(
        *(("ibClear", 0),
          ("ibUnknown", 1),
          ("ibPrimaryDiskFailure", 2),
          ("ibFanFailure-old", 3),
          ("ibPowerSupplyFailure", 4),
          ("ibDBFailure", 5),
          ("ibApacheSoftwareFailure", 6),
          ("ibSerialConsoleFailure", 7),
          ("ibControldSoftwareFailure", 11),
          ("ibUpgradeFailure", 12),
          ("ibSNMPDFailure", 13),
          ("ibSSHDSoftwareFailure", 15),
          ("ibNTPDSoftwareFailure", 16),
          ("ibClusterdSoftwarFailure", 17),
          ("ibLCDSoftwareFailure", 18),
          ("ibDHCPdSoftwareFailure", 19),
          ("ibNamedSoftwareFailure", 20),
          ("ibAuthServerGroupDown", 21),
          ("ibAuthServerGroupUp", 22),
          ("ibNTLMSoftwareFailure", 24),
          ("ibNetBIOSDaemonFailure", 25),
          ("ibWindowBindDaemonFailure", 26),
          ("ibTFTPDSoftwareFailure", 27),
          ("ibUNUSED28", 28),
          ("ibBackupSoftwareFailure", 29),
          ("ibBackupDatabaseSoftwareFailure", 30),
          ("ibBackupModuleSoftwareFailure", 31),
          ("ibBackupSizeSoftwareFailure", 32),
          ("ibBackupLockSoftwareFailure", 33),
          ("ibHTTPFileDistSoftwareFailure", 34),
          ("ibOSPFSoftwareFailure", 35),
          ("ibAuthDHCPNamedSoftwareFailure", 36),
          ("ibFan1Failure", 37),
          ("ibFan2Failure", 38),
          ("ibFan3Failure", 39),
          ("ibFan1OK", 40),
          ("ibFan2OK", 41),
          ("ibFan3OK", 42),
          ("ibFTPDSoftwareFailure", 44),
          ("ibPowerSupplyOK", 46),
          ("ibWebUISoftwareFailure", 47),
          ("ibUNUSED48", 48),
          ("ibADAgentSyncFailure", 49),
          ("ibIFMAPSoftwareFailure", 50),
          ("ibCaptivePortalSoftwareFailure", 51),
          ("ibDuplicateIPAddressFailure", 52),
          ("ibBGPSoftwareFailure", 53),
          ("ibRAIDIsOptimal", 3001),
          ("ibRAIDIsDegraded", 3002),
          ("ibRAIDIsRebuilding", 3003),
          ("ibRAIDStatusUnknown", 3004),
          ("ibRAIDBatteryIsOK", 3005),
          ("ibRAIDBatteryFailed", 3006))
    )



# MIB Managed Objects in the order of their OIDs

_IbNotificationVarBind_ObjectIdentity = ObjectIdentity
ibNotificationVarBind = _IbNotificationVarBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2)
)
_IbNodeName_Type = IbNode
_IbNodeName_Object = MibScalar
ibNodeName = _IbNodeName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 1),
    _IbNodeName_Type()
)
ibNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibNodeName.setStatus("current")


class _IbTrapSeverity_Type(Integer32):
    """Custom type ibTrapSeverity based on Integer32"""
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
        *(("indetermined", 1),
          ("info", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_IbTrapSeverity_Type.__name__ = "Integer32"
_IbTrapSeverity_Object = MibScalar
ibTrapSeverity = _IbTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 2),
    _IbTrapSeverity_Type()
)
ibTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibTrapSeverity.setStatus("current")


class _IbObjectName_Type(DisplayString):
    """Custom type ibObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IbObjectName_Type.__name__ = "DisplayString"
_IbObjectName_Object = MibScalar
ibObjectName = _IbObjectName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 3),
    _IbObjectName_Type()
)
ibObjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibObjectName.setStatus("current")
_IbProbableCause_Type = IbProbableCause
_IbProbableCause_Object = MibScalar
ibProbableCause = _IbProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 4),
    _IbProbableCause_Type()
)
ibProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibProbableCause.setStatus("current")


class _IbSubsystemName_Type(DisplayString):
    """Custom type ibSubsystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IbSubsystemName_Type.__name__ = "DisplayString"
_IbSubsystemName_Object = MibScalar
ibSubsystemName = _IbSubsystemName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 5),
    _IbSubsystemName_Type()
)
ibSubsystemName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibSubsystemName.setStatus("current")
_IbCurThresholdValue_Type = Integer32
_IbCurThresholdValue_Object = MibScalar
ibCurThresholdValue = _IbCurThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 6),
    _IbCurThresholdValue_Type()
)
ibCurThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibCurThresholdValue.setStatus("current")
_IbThresholdHigh_Type = Integer32
_IbThresholdHigh_Object = MibScalar
ibThresholdHigh = _IbThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 7),
    _IbThresholdHigh_Type()
)
ibThresholdHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibThresholdHigh.setStatus("current")
_IbThresholdLow_Type = Integer32
_IbThresholdLow_Object = MibScalar
ibThresholdLow = _IbThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 8),
    _IbThresholdLow_Type()
)
ibThresholdLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibThresholdLow.setStatus("current")
_IbPreviousState_Type = IbState
_IbPreviousState_Object = MibScalar
ibPreviousState = _IbPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 9),
    _IbPreviousState_Type()
)
ibPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibPreviousState.setStatus("current")
_IbCurrentState_Type = IbState
_IbCurrentState_Object = MibScalar
ibCurrentState = _IbCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 10),
    _IbCurrentState_Type()
)
ibCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibCurrentState.setStatus("current")
_IbTrapDesc_Type = IbString
_IbTrapDesc_Object = MibScalar
ibTrapDesc = _IbTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 2, 11),
    _IbTrapDesc_Type()
)
ibTrapDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibTrapDesc.setStatus("current")

# Managed Objects groups


# Notification objects

ibEquipmentFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 1, 1, 0)
)
ibEquipmentFailureTrap.setObjects(
      *(("IB-TRAP-MIB", "ibNodeName"),
        ("IB-TRAP-MIB", "ibTrapSeverity"),
        ("IB-TRAP-MIB", "ibObjectName"),
        ("IB-TRAP-MIB", "ibProbableCause"),
        ("IB-TRAP-MIB", "ibTrapDesc"))
)
if mibBuilder.loadTexts:
    ibEquipmentFailureTrap.setStatus(
        "current"
    )

ibProcessingFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 1, 2, 0)
)
ibProcessingFailureTrap.setObjects(
      *(("IB-TRAP-MIB", "ibNodeName"),
        ("IB-TRAP-MIB", "ibTrapSeverity"),
        ("IB-TRAP-MIB", "ibSubsystemName"),
        ("IB-TRAP-MIB", "ibProbableCause"),
        ("IB-TRAP-MIB", "ibTrapDesc"))
)
if mibBuilder.loadTexts:
    ibProcessingFailureTrap.setStatus(
        "current"
    )

ibThresholdCrossingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 1, 3, 0)
)
ibThresholdCrossingEvent.setObjects(
      *(("IB-TRAP-MIB", "ibNodeName"),
        ("IB-TRAP-MIB", "ibObjectName"),
        ("IB-TRAP-MIB", "ibCurThresholdValue"),
        ("IB-TRAP-MIB", "ibThresholdHigh"),
        ("IB-TRAP-MIB", "ibThresholdLow"),
        ("IB-TRAP-MIB", "ibTrapDesc"))
)
if mibBuilder.loadTexts:
    ibThresholdCrossingEvent.setStatus(
        "current"
    )

ibStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 1, 4, 0)
)
ibStateChangeEvent.setObjects(
      *(("IB-TRAP-MIB", "ibNodeName"),
        ("IB-TRAP-MIB", "ibObjectName"),
        ("IB-TRAP-MIB", "ibPreviousState"),
        ("IB-TRAP-MIB", "ibCurrentState"),
        ("IB-TRAP-MIB", "ibTrapDesc"))
)
if mibBuilder.loadTexts:
    ibStateChangeEvent.setStatus(
        "current"
    )

ibProcStartStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1, 1, 5, 0)
)
ibProcStartStopTrap.setObjects(
      *(("IB-TRAP-MIB", "ibNodeName"),
        ("IB-TRAP-MIB", "ibSubsystemName"),
        ("IB-TRAP-MIB", "ibTrapDesc"))
)
if mibBuilder.loadTexts:
    ibProcStartStopTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-TRAP-MIB",
    **{"IbState": IbState,
       "IbProbableCause": IbProbableCause,
       "ibTrapOneModule": ibTrapOneModule,
       "ibEquipmentFailureTrap": ibEquipmentFailureTrap,
       "ibProcessingFailureTrap": ibProcessingFailureTrap,
       "ibThresholdCrossingEvent": ibThresholdCrossingEvent,
       "ibStateChangeEvent": ibStateChangeEvent,
       "ibProcStartStopTrap": ibProcStartStopTrap,
       "ibNotificationVarBind": ibNotificationVarBind,
       "ibNodeName": ibNodeName,
       "ibTrapSeverity": ibTrapSeverity,
       "ibObjectName": ibObjectName,
       "ibProbableCause": ibProbableCause,
       "ibSubsystemName": ibSubsystemName,
       "ibCurThresholdValue": ibCurThresholdValue,
       "ibThresholdHigh": ibThresholdHigh,
       "ibThresholdLow": ibThresholdLow,
       "ibPreviousState": ibPreviousState,
       "ibCurrentState": ibCurrentState,
       "ibTrapDesc": ibTrapDesc}
)
