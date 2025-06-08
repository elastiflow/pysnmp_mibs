# SNMP MIB module (BELAIR-SYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-SYSTEM.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairGeneric,
 belairModules) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairGeneric",
    "belairModules")

(BelAirAdminState,
 BelAirAlarmId,
 BelAirAlarmObjectIndex,
 BelAirCardType,
 BelAirSeverity,
 BelAirSoftwareBank) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState",
    "BelAirAlarmId",
    "BelAirAlarmObjectIndex",
    "BelAirCardType",
    "BelAirSeverity",
    "BelAirSoftwareBank")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

belairSystemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 1, 4)
)
if mibBuilder.loadTexts:
    belairSystemModule.setRevisions(
        ("2009-05-01 11:30",
         "2008-12-10 14:00",
         "2008-11-17 10:05",
         "2008-09-23 13:45",
         "2008-06-03 18:40",
         "2008-03-06 13:00",
         "2007-05-18 17:05",
         "2006-10-18 14:30",
         "2006-08-03 14:40",
         "2006-02-24 18:41",
         "2006-01-13 17:00",
         "2005-11-24 17:35",
         "2005-04-01 09:50",
         "2005-03-22 16:30",
         "2004-09-21 15:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairSystem_ObjectIdentity = ObjectIdentity
belairSystem = _BelairSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1)
)
if mibBuilder.loadTexts:
    belairSystem.setStatus("current")
_BelairSysObjects_ObjectIdentity = ObjectIdentity
belairSysObjects = _BelairSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1)
)
if mibBuilder.loadTexts:
    belairSysObjects.setStatus("current")
_BelairSysPeripheral_ObjectIdentity = ObjectIdentity
belairSysPeripheral = _BelairSysPeripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    belairSysPeripheral.setStatus("current")
_BelairSysASMPresent_Type = TruthValue
_BelairSysASMPresent_Object = MibScalar
belairSysASMPresent = _BelairSysASMPresent_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 1, 1),
    _BelairSysASMPresent_Type()
)
belairSysASMPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysASMPresent.setStatus("current")
_BelairSysAdmin_ObjectIdentity = ObjectIdentity
belairSysAdmin = _BelairSysAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    belairSysAdmin.setStatus("current")
_BelairSysFtpServer_Type = IpAddress
_BelairSysFtpServer_Object = MibScalar
belairSysFtpServer = _BelairSysFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 1),
    _BelairSysFtpServer_Type()
)
belairSysFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysFtpServer.setStatus("current")


class _BelairSysFtpUserId_Type(OctetString):
    """Custom type belairSysFtpUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BelairSysFtpUserId_Type.__name__ = "OctetString"
_BelairSysFtpUserId_Object = MibScalar
belairSysFtpUserId = _BelairSysFtpUserId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 2),
    _BelairSysFtpUserId_Type()
)
belairSysFtpUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysFtpUserId.setStatus("current")


class _BelairSysFtpPassword_Type(OctetString):
    """Custom type belairSysFtpPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BelairSysFtpPassword_Type.__name__ = "OctetString"
_BelairSysFtpPassword_Object = MibScalar
belairSysFtpPassword = _BelairSysFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 3),
    _BelairSysFtpPassword_Type()
)
belairSysFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysFtpPassword.setStatus("current")


class _BelairSysFtpRemotePath_Type(OctetString):
    """Custom type belairSysFtpRemotePath based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairSysFtpRemotePath_Type.__name__ = "OctetString"
_BelairSysFtpRemotePath_Object = MibScalar
belairSysFtpRemotePath = _BelairSysFtpRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 4),
    _BelairSysFtpRemotePath_Type()
)
belairSysFtpRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysFtpRemotePath.setStatus("current")
_BelairSysTftpServer_Type = IpAddress
_BelairSysTftpServer_Object = MibScalar
belairSysTftpServer = _BelairSysTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 5),
    _BelairSysTftpServer_Type()
)
belairSysTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysTftpServer.setStatus("current")


class _BelairSysTftpRemotePath_Type(OctetString):
    """Custom type belairSysTftpRemotePath based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairSysTftpRemotePath_Type.__name__ = "OctetString"
_BelairSysTftpRemotePath_Object = MibScalar
belairSysTftpRemotePath = _BelairSysTftpRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 6),
    _BelairSysTftpRemotePath_Type()
)
belairSysTftpRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysTftpRemotePath.setStatus("current")
_BelairSysSntpServer_Type = IpAddress
_BelairSysSntpServer_Object = MibScalar
belairSysSntpServer = _BelairSysSntpServer_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 7),
    _BelairSysSntpServer_Type()
)
belairSysSntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysSntpServer.setStatus("current")
_BelairSysSntpEnabled_Type = TruthValue
_BelairSysSntpEnabled_Object = MibScalar
belairSysSntpEnabled = _BelairSysSntpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 8),
    _BelairSysSntpEnabled_Type()
)
belairSysSntpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysSntpEnabled.setStatus("current")


class _BelairSysSntpStatus_Type(Integer32):
    """Custom type belairSysSntpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2),
          ("failed", 3))
    )


_BelairSysSntpStatus_Type.__name__ = "Integer32"
_BelairSysSntpStatus_Object = MibScalar
belairSysSntpStatus = _BelairSysSntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 9),
    _BelairSysSntpStatus_Type()
)
belairSysSntpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysSntpStatus.setStatus("current")
_BelairSysReboot_Type = TruthValue
_BelairSysReboot_Object = MibScalar
belairSysReboot = _BelairSysReboot_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 10),
    _BelairSysReboot_Type()
)
belairSysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysReboot.setStatus("current")


class _BelairSysConfigSaveAction_Type(Integer32):
    """Custom type belairSysConfigSaveAction based on Integer32"""
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
        *(("localSave", 1),
          ("tftpSave", 2),
          ("ftpSave", 3),
          ("noSave", 4))
    )


_BelairSysConfigSaveAction_Type.__name__ = "Integer32"
_BelairSysConfigSaveAction_Object = MibScalar
belairSysConfigSaveAction = _BelairSysConfigSaveAction_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 11),
    _BelairSysConfigSaveAction_Type()
)
belairSysConfigSaveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysConfigSaveAction.setStatus("current")


class _BelairSysConfigSaveStatus_Type(Integer32):
    """Custom type belairSysConfigSaveStatus based on Integer32"""
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
        *(("inprogress", 1),
          ("successfull", 2),
          ("failed", 3),
          ("idle", 4))
    )


_BelairSysConfigSaveStatus_Type.__name__ = "Integer32"
_BelairSysConfigSaveStatus_Object = MibScalar
belairSysConfigSaveStatus = _BelairSysConfigSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 12),
    _BelairSysConfigSaveStatus_Type()
)
belairSysConfigSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysConfigSaveStatus.setStatus("current")


class _BelairSysConfigRestoreAction_Type(Integer32):
    """Custom type belairSysConfigRestoreAction based on Integer32"""
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
        *(("localRestore", 1),
          ("tftpRestore", 2),
          ("ftpRestore", 3),
          ("noRestore", 4))
    )


_BelairSysConfigRestoreAction_Type.__name__ = "Integer32"
_BelairSysConfigRestoreAction_Object = MibScalar
belairSysConfigRestoreAction = _BelairSysConfigRestoreAction_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 13),
    _BelairSysConfigRestoreAction_Type()
)
belairSysConfigRestoreAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysConfigRestoreAction.setStatus("current")


class _BelairSysConfigRestoreStatus_Type(Integer32):
    """Custom type belairSysConfigRestoreStatus based on Integer32"""
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
        *(("inprogress", 1),
          ("successfull", 2),
          ("failed", 3),
          ("idle", 4))
    )


_BelairSysConfigRestoreStatus_Type.__name__ = "Integer32"
_BelairSysConfigRestoreStatus_Object = MibScalar
belairSysConfigRestoreStatus = _BelairSysConfigRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 14),
    _BelairSysConfigRestoreStatus_Type()
)
belairSysConfigRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysConfigRestoreStatus.setStatus("current")
_BelairSysLastConfigChange_Type = TimeTicks
_BelairSysLastConfigChange_Object = MibScalar
belairSysLastConfigChange = _BelairSysLastConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 15),
    _BelairSysLastConfigChange_Type()
)
belairSysLastConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysLastConfigChange.setStatus("current")
_BelairSysConfigUnsaved_Type = TruthValue
_BelairSysConfigUnsaved_Object = MibScalar
belairSysConfigUnsaved = _BelairSysConfigUnsaved_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 16),
    _BelairSysConfigUnsaved_Type()
)
belairSysConfigUnsaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysConfigUnsaved.setStatus("current")


class _BelairSysLastRebootType_Type(Integer32):
    """Custom type belairSysLastRebootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("warm", 2),
          ("unknown", 3))
    )


_BelairSysLastRebootType_Type.__name__ = "Integer32"
_BelairSysLastRebootType_Object = MibScalar
belairSysLastRebootType = _BelairSysLastRebootType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 17),
    _BelairSysLastRebootType_Type()
)
belairSysLastRebootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysLastRebootType.setStatus("current")


class _BelairSysLastRebootReason_Type(Integer32):
    """Custom type belairSysLastRebootReason based on Integer32"""
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
        *(("watchdog", 1),
          ("autonomous", 2),
          ("user", 3),
          ("unknown", 4))
    )


_BelairSysLastRebootReason_Type.__name__ = "Integer32"
_BelairSysLastRebootReason_Object = MibScalar
belairSysLastRebootReason = _BelairSysLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 2, 18),
    _BelairSysLastRebootReason_Type()
)
belairSysLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysLastRebootReason.setStatus("current")
_BelairSysSoftwareMgmt_ObjectIdentity = ObjectIdentity
belairSysSoftwareMgmt = _BelairSysSoftwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    belairSysSoftwareMgmt.setStatus("current")
_BelairSwMgmtActiveBank_Type = BelAirSoftwareBank
_BelairSwMgmtActiveBank_Object = MibScalar
belairSwMgmtActiveBank = _BelairSwMgmtActiveBank_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 1),
    _BelairSwMgmtActiveBank_Type()
)
belairSwMgmtActiveBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSwMgmtActiveBank.setStatus("current")
_BelairSwMgmtNextBank_Type = BelAirSoftwareBank
_BelairSwMgmtNextBank_Object = MibScalar
belairSwMgmtNextBank = _BelairSwMgmtNextBank_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 2),
    _BelairSwMgmtNextBank_Type()
)
belairSwMgmtNextBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSwMgmtNextBank.setStatus("current")


class _BelairSwMgmtAction_Type(Integer32):
    """Custom type belairSwMgmtAction based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("startDownload", 2),
          ("commitLoad", 3),
          ("switchBank", 4),
          ("undoSwitchBank", 5),
          ("startDownloadFtp", 6),
          ("cancelDownload", 7),
          ("init", 8))
    )


_BelairSwMgmtAction_Type.__name__ = "Integer32"
_BelairSwMgmtAction_Object = MibScalar
belairSwMgmtAction = _BelairSwMgmtAction_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 3),
    _BelairSwMgmtAction_Type()
)
belairSwMgmtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSwMgmtAction.setStatus("current")


class _BelairSwMgmtStatus_Type(Integer32):
    """Custom type belairSwMgmtStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("downloadInProgress", 1),
          ("downloadComplete", 2),
          ("downloadFailed", 3),
          ("commitInProgress", 4),
          ("commitComplete", 5),
          ("idle", 6),
          ("commitFailed", 7),
          ("downloadCanceled", 8),
          ("downloadCancelFailed", 9))
    )


_BelairSwMgmtStatus_Type.__name__ = "Integer32"
_BelairSwMgmtStatus_Object = MibScalar
belairSwMgmtStatus = _BelairSwMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 4),
    _BelairSwMgmtStatus_Type()
)
belairSwMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSwMgmtStatus.setStatus("current")
_BelairSwImageTable_Object = MibTable
belairSwImageTable = _BelairSwImageTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    belairSwImageTable.setStatus("current")
_BelairSwImageEntry_Object = MibTableRow
belairSwImageEntry = _BelairSwImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 5, 1)
)
belairSwImageEntry.setIndexNames(
    (0, "BELAIR-SYSTEM", "belairSwImageBank"),
)
if mibBuilder.loadTexts:
    belairSwImageEntry.setStatus("current")
_BelairSwImageBank_Type = BelAirSoftwareBank
_BelairSwImageBank_Object = MibTableColumn
belairSwImageBank = _BelairSwImageBank_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 5, 1, 1),
    _BelairSwImageBank_Type()
)
belairSwImageBank.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairSwImageBank.setStatus("current")


class _BelairSwImageDescription_Type(OctetString):
    """Custom type belairSwImageDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BelairSwImageDescription_Type.__name__ = "OctetString"
_BelairSwImageDescription_Object = MibTableColumn
belairSwImageDescription = _BelairSwImageDescription_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 5, 1, 2),
    _BelairSwImageDescription_Type()
)
belairSwImageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSwImageDescription.setStatus("current")
_BelairAutoUpgradeEnabled_Type = TruthValue
_BelairAutoUpgradeEnabled_Object = MibScalar
belairAutoUpgradeEnabled = _BelairAutoUpgradeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 3, 6),
    _BelairAutoUpgradeEnabled_Type()
)
belairAutoUpgradeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairAutoUpgradeEnabled.setStatus("current")
_BelairCardTable_Object = MibTable
belairCardTable = _BelairCardTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    belairCardTable.setStatus("current")
_BelairCardEntry_Object = MibTableRow
belairCardEntry = _BelairCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1)
)
belairCardEntry.setIndexNames(
    (0, "BELAIR-SYSTEM", "belairCardType"),
    (0, "BELAIR-SYSTEM", "belairCardIndex"),
)
if mibBuilder.loadTexts:
    belairCardEntry.setStatus("current")
_BelairCardType_Type = BelAirCardType
_BelairCardType_Object = MibTableColumn
belairCardType = _BelairCardType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 1),
    _BelairCardType_Type()
)
belairCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCardType.setStatus("current")


class _BelairCardIndex_Type(Integer32):
    """Custom type belairCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BelairCardIndex_Type.__name__ = "Integer32"
_BelairCardIndex_Object = MibTableColumn
belairCardIndex = _BelairCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 2),
    _BelairCardIndex_Type()
)
belairCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCardIndex.setStatus("current")
_BelairCardAdminStatus_Type = BelAirAdminState
_BelairCardAdminStatus_Object = MibTableColumn
belairCardAdminStatus = _BelairCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 3),
    _BelairCardAdminStatus_Type()
)
belairCardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCardAdminStatus.setStatus("current")


class _BelairCardOperStatus_Type(Integer32):
    """Custom type belairCardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_BelairCardOperStatus_Type.__name__ = "Integer32"
_BelairCardOperStatus_Object = MibTableColumn
belairCardOperStatus = _BelairCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 4),
    _BelairCardOperStatus_Type()
)
belairCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCardOperStatus.setStatus("current")


class _BelairCardDescription_Type(OctetString):
    """Custom type belairCardDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BelairCardDescription_Type.__name__ = "OctetString"
_BelairCardDescription_Object = MibTableColumn
belairCardDescription = _BelairCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 5),
    _BelairCardDescription_Type()
)
belairCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCardDescription.setStatus("current")


class _BelairCardHwVariant_Type(Integer32):
    """Custom type belairCardHwVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BelairCardHwVariant_Type.__name__ = "Integer32"
_BelairCardHwVariant_Object = MibTableColumn
belairCardHwVariant = _BelairCardHwVariant_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 6),
    _BelairCardHwVariant_Type()
)
belairCardHwVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCardHwVariant.setStatus("current")


class _BelairCardSerialNumber_Type(OctetString):
    """Custom type belairCardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BelairCardSerialNumber_Type.__name__ = "OctetString"
_BelairCardSerialNumber_Object = MibTableColumn
belairCardSerialNumber = _BelairCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 7),
    _BelairCardSerialNumber_Type()
)
belairCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCardSerialNumber.setStatus("current")


class _BelairCardMfgCode_Type(OctetString):
    """Custom type belairCardMfgCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BelairCardMfgCode_Type.__name__ = "OctetString"
_BelairCardMfgCode_Object = MibTableColumn
belairCardMfgCode = _BelairCardMfgCode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 4, 1, 8),
    _BelairCardMfgCode_Type()
)
belairCardMfgCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairCardMfgCode.setStatus("current")
_BelairAlarms_ObjectIdentity = ObjectIdentity
belairAlarms = _BelairAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    belairAlarms.setStatus("current")
_BelairActiveAlarmTable_Object = MibTable
belairActiveAlarmTable = _BelairActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    belairActiveAlarmTable.setStatus("current")
_BelairActiveAlarmEntry_Object = MibTableRow
belairActiveAlarmEntry = _BelairActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1)
)
belairActiveAlarmEntry.setIndexNames(
    (0, "BELAIR-SYSTEM", "belairActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    belairActiveAlarmEntry.setStatus("current")
_BelairActiveAlarmId_Type = BelAirAlarmId
_BelairActiveAlarmId_Object = MibTableColumn
belairActiveAlarmId = _BelairActiveAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 1),
    _BelairActiveAlarmId_Type()
)
belairActiveAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairActiveAlarmId.setStatus("current")
_BelairActiveAlarmObject_Type = ObjectIdentifier
_BelairActiveAlarmObject_Object = MibTableColumn
belairActiveAlarmObject = _BelairActiveAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 2),
    _BelairActiveAlarmObject_Type()
)
belairActiveAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairActiveAlarmObject.setStatus("deprecated")
_BelairActiveAlarmObjectType_Type = BelAirAlarmObjectIndex
_BelairActiveAlarmObjectType_Object = MibTableColumn
belairActiveAlarmObjectType = _BelairActiveAlarmObjectType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 3),
    _BelairActiveAlarmObjectType_Type()
)
belairActiveAlarmObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairActiveAlarmObjectType.setStatus("deprecated")
_BelairActiveAlarmTime_Type = DateAndTime
_BelairActiveAlarmTime_Object = MibTableColumn
belairActiveAlarmTime = _BelairActiveAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 4),
    _BelairActiveAlarmTime_Type()
)
belairActiveAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairActiveAlarmTime.setStatus("current")
_BelairActiveAlarmSeverity_Type = BelAirSeverity
_BelairActiveAlarmSeverity_Object = MibTableColumn
belairActiveAlarmSeverity = _BelairActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 5),
    _BelairActiveAlarmSeverity_Type()
)
belairActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairActiveAlarmSeverity.setStatus("current")


class _BelairActiveAlarmDescription_Type(OctetString):
    """Custom type belairActiveAlarmDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BelairActiveAlarmDescription_Type.__name__ = "OctetString"
_BelairActiveAlarmDescription_Object = MibTableColumn
belairActiveAlarmDescription = _BelairActiveAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 6),
    _BelairActiveAlarmDescription_Type()
)
belairActiveAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairActiveAlarmDescription.setStatus("current")


class _BelairActiveAlarmIndex_Type(Integer32):
    """Custom type belairActiveAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_BelairActiveAlarmIndex_Type.__name__ = "Integer32"
_BelairActiveAlarmIndex_Object = MibTableColumn
belairActiveAlarmIndex = _BelairActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 7),
    _BelairActiveAlarmIndex_Type()
)
belairActiveAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairActiveAlarmIndex.setStatus("current")
_BelairActiveAlarmInstanceOid_Type = VariablePointer
_BelairActiveAlarmInstanceOid_Object = MibTableColumn
belairActiveAlarmInstanceOid = _BelairActiveAlarmInstanceOid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 5, 1, 1, 8),
    _BelairActiveAlarmInstanceOid_Type()
)
belairActiveAlarmInstanceOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairActiveAlarmInstanceOid.setStatus("current")
_BelairEnvironment_ObjectIdentity = ObjectIdentity
belairEnvironment = _BelairEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    belairEnvironment.setStatus("current")
_BelairSysCurrentTemperature_Type = Integer32
_BelairSysCurrentTemperature_Object = MibScalar
belairSysCurrentTemperature = _BelairSysCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 1),
    _BelairSysCurrentTemperature_Type()
)
belairSysCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysCurrentTemperature.setStatus("current")
if mibBuilder.loadTexts:
    belairSysCurrentTemperature.setUnits("Celsius")
_BelairSysHighTempThreshold_Type = Integer32
_BelairSysHighTempThreshold_Object = MibScalar
belairSysHighTempThreshold = _BelairSysHighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 2),
    _BelairSysHighTempThreshold_Type()
)
belairSysHighTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysHighTempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    belairSysHighTempThreshold.setUnits("Celsius")
_BelairSysLowTempThreshold_Type = Integer32
_BelairSysLowTempThreshold_Object = MibScalar
belairSysLowTempThreshold = _BelairSysLowTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 3),
    _BelairSysLowTempThreshold_Type()
)
belairSysLowTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysLowTempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    belairSysLowTempThreshold.setUnits("Celsius")
_BelairSysCurrentHumidity_Type = Integer32
_BelairSysCurrentHumidity_Object = MibScalar
belairSysCurrentHumidity = _BelairSysCurrentHumidity_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 4),
    _BelairSysCurrentHumidity_Type()
)
belairSysCurrentHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysCurrentHumidity.setStatus("current")
if mibBuilder.loadTexts:
    belairSysCurrentHumidity.setUnits("%")
_BelairSysHighHumidityThreshold_Type = Integer32
_BelairSysHighHumidityThreshold_Object = MibScalar
belairSysHighHumidityThreshold = _BelairSysHighHumidityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 5),
    _BelairSysHighHumidityThreshold_Type()
)
belairSysHighHumidityThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysHighHumidityThreshold.setStatus("current")
if mibBuilder.loadTexts:
    belairSysHighHumidityThreshold.setUnits("%")


class _BelairSysBatteryStatus_Type(Integer32):
    """Custom type belairSysBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("lowVWarning", 2),
          ("lowVFailure", 3),
          ("active", 4),
          ("activeLowVWarning", 5),
          ("activeLowVFailure", 6),
          ("notPresent", 7))
    )


_BelairSysBatteryStatus_Type.__name__ = "Integer32"
_BelairSysBatteryStatus_Object = MibScalar
belairSysBatteryStatus = _BelairSysBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 6),
    _BelairSysBatteryStatus_Type()
)
belairSysBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysBatteryStatus.setStatus("current")
_BelairSysBatteryVoltage_Type = Integer32
_BelairSysBatteryVoltage_Object = MibScalar
belairSysBatteryVoltage = _BelairSysBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 7),
    _BelairSysBatteryVoltage_Type()
)
belairSysBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    belairSysBatteryVoltage.setUnits("mV")
_BelairSysBatteryLowThreshold_Type = Integer32
_BelairSysBatteryLowThreshold_Object = MibScalar
belairSysBatteryLowThreshold = _BelairSysBatteryLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 8),
    _BelairSysBatteryLowThreshold_Type()
)
belairSysBatteryLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairSysBatteryLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    belairSysBatteryLowThreshold.setUnits("mV")
_BelairSysBatteryEnabled_Type = TruthValue
_BelairSysBatteryEnabled_Object = MibScalar
belairSysBatteryEnabled = _BelairSysBatteryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 6, 9),
    _BelairSysBatteryEnabled_Type()
)
belairSysBatteryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairSysBatteryEnabled.setStatus("current")
_BelairTrapVarbindObjects_ObjectIdentity = ObjectIdentity
belairTrapVarbindObjects = _BelairTrapVarbindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    belairTrapVarbindObjects.setStatus("current")
_BelairTrapAlarmId_Type = BelAirAlarmId
_BelairTrapAlarmId_Object = MibScalar
belairTrapAlarmId = _BelairTrapAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 7, 1),
    _BelairTrapAlarmId_Type()
)
belairTrapAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairTrapAlarmId.setStatus("current")
_BelairTrapSeverity_Type = BelAirSeverity
_BelairTrapSeverity_Object = MibScalar
belairTrapSeverity = _BelairTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 7, 2),
    _BelairTrapSeverity_Type()
)
belairTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairTrapSeverity.setStatus("current")


class _BelairTrapSequenceNumber_Type(Integer32):
    """Custom type belairTrapSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BelairTrapSequenceNumber_Type.__name__ = "Integer32"
_BelairTrapSequenceNumber_Object = MibScalar
belairTrapSequenceNumber = _BelairTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 7, 3),
    _BelairTrapSequenceNumber_Type()
)
belairTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairTrapSequenceNumber.setStatus("current")


class _BelairTrapDetailInfo_Type(OctetString):
    """Custom type belairTrapDetailInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BelairTrapDetailInfo_Type.__name__ = "OctetString"
_BelairTrapDetailInfo_Object = MibScalar
belairTrapDetailInfo = _BelairTrapDetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 7, 4),
    _BelairTrapDetailInfo_Type()
)
belairTrapDetailInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    belairTrapDetailInfo.setStatus("current")
_BelairTrapIpAddress_Type = IpAddress
_BelairTrapIpAddress_Object = MibScalar
belairTrapIpAddress = _BelairTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 7, 5),
    _BelairTrapIpAddress_Type()
)
belairTrapIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    belairTrapIpAddress.setStatus("current")
_BelairSysCoordinates_ObjectIdentity = ObjectIdentity
belairSysCoordinates = _BelairSysCoordinates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    belairSysCoordinates.setStatus("current")


class _BaSysLatitudeDegrees_Type(Integer32):
    """Custom type baSysLatitudeDegrees based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 90),
    )


_BaSysLatitudeDegrees_Type.__name__ = "Integer32"
_BaSysLatitudeDegrees_Object = MibScalar
baSysLatitudeDegrees = _BaSysLatitudeDegrees_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 1),
    _BaSysLatitudeDegrees_Type()
)
baSysLatitudeDegrees.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLatitudeDegrees.setStatus("current")


class _BaSysLatitudeMinutes_Type(Integer32):
    """Custom type baSysLatitudeMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_BaSysLatitudeMinutes_Type.__name__ = "Integer32"
_BaSysLatitudeMinutes_Object = MibScalar
baSysLatitudeMinutes = _BaSysLatitudeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 2),
    _BaSysLatitudeMinutes_Type()
)
baSysLatitudeMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLatitudeMinutes.setStatus("current")


class _BaSysLatitudeSeconds_Type(Integer32):
    """Custom type baSysLatitudeSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_BaSysLatitudeSeconds_Type.__name__ = "Integer32"
_BaSysLatitudeSeconds_Object = MibScalar
baSysLatitudeSeconds = _BaSysLatitudeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 3),
    _BaSysLatitudeSeconds_Type()
)
baSysLatitudeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLatitudeSeconds.setStatus("current")


class _BaSysLatitudeMilliSeconds_Type(Integer32):
    """Custom type baSysLatitudeMilliSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_BaSysLatitudeMilliSeconds_Type.__name__ = "Integer32"
_BaSysLatitudeMilliSeconds_Object = MibScalar
baSysLatitudeMilliSeconds = _BaSysLatitudeMilliSeconds_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 4),
    _BaSysLatitudeMilliSeconds_Type()
)
baSysLatitudeMilliSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLatitudeMilliSeconds.setStatus("current")


class _BaSysLongitudeDegrees_Type(Integer32):
    """Custom type baSysLongitudeDegrees based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180, 180),
    )


_BaSysLongitudeDegrees_Type.__name__ = "Integer32"
_BaSysLongitudeDegrees_Object = MibScalar
baSysLongitudeDegrees = _BaSysLongitudeDegrees_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 5),
    _BaSysLongitudeDegrees_Type()
)
baSysLongitudeDegrees.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLongitudeDegrees.setStatus("current")


class _BaSysLongitudeMinutes_Type(Integer32):
    """Custom type baSysLongitudeMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_BaSysLongitudeMinutes_Type.__name__ = "Integer32"
_BaSysLongitudeMinutes_Object = MibScalar
baSysLongitudeMinutes = _BaSysLongitudeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 6),
    _BaSysLongitudeMinutes_Type()
)
baSysLongitudeMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLongitudeMinutes.setStatus("current")


class _BaSysLongitudeSeconds_Type(Integer32):
    """Custom type baSysLongitudeSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_BaSysLongitudeSeconds_Type.__name__ = "Integer32"
_BaSysLongitudeSeconds_Object = MibScalar
baSysLongitudeSeconds = _BaSysLongitudeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 7),
    _BaSysLongitudeSeconds_Type()
)
baSysLongitudeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLongitudeSeconds.setStatus("current")


class _BaSysLongitudeMilliSeconds_Type(Integer32):
    """Custom type baSysLongitudeMilliSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_BaSysLongitudeMilliSeconds_Type.__name__ = "Integer32"
_BaSysLongitudeMilliSeconds_Object = MibScalar
baSysLongitudeMilliSeconds = _BaSysLongitudeMilliSeconds_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 8, 8),
    _BaSysLongitudeMilliSeconds_Type()
)
baSysLongitudeMilliSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysLongitudeMilliSeconds.setStatus("current")
_BelairCustomFieldTable_Object = MibTable
belairCustomFieldTable = _BelairCustomFieldTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    belairCustomFieldTable.setStatus("current")
_BelairCustomFieldEntry_Object = MibTableRow
belairCustomFieldEntry = _BelairCustomFieldEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 9, 1)
)
belairCustomFieldEntry.setIndexNames(
    (0, "BELAIR-SYSTEM", "belairCustomFieldIndex"),
)
if mibBuilder.loadTexts:
    belairCustomFieldEntry.setStatus("current")


class _BelairCustomFieldIndex_Type(Integer32):
    """Custom type belairCustomFieldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BelairCustomFieldIndex_Type.__name__ = "Integer32"
_BelairCustomFieldIndex_Object = MibTableColumn
belairCustomFieldIndex = _BelairCustomFieldIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 9, 1, 1),
    _BelairCustomFieldIndex_Type()
)
belairCustomFieldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairCustomFieldIndex.setStatus("current")


class _BelairCustomFieldValue_Type(OctetString):
    """Custom type belairCustomFieldValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BelairCustomFieldValue_Type.__name__ = "OctetString"
_BelairCustomFieldValue_Object = MibTableColumn
belairCustomFieldValue = _BelairCustomFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 9, 1, 2),
    _BelairCustomFieldValue_Type()
)
belairCustomFieldValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairCustomFieldValue.setStatus("current")
_BelairSysMemory_ObjectIdentity = ObjectIdentity
belairSysMemory = _BelairSysMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    belairSysMemory.setStatus("current")
_MemTotal_Type = Integer32
_MemTotal_Object = MibScalar
memTotal = _MemTotal_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 10, 1),
    _MemTotal_Type()
)
memTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotal.setStatus("current")
_MemFree_Type = Integer32
_MemFree_Object = MibScalar
memFree = _MemFree_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 10, 2),
    _MemFree_Type()
)
memFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFree.setStatus("current")
_MemBuffers_Type = Integer32
_MemBuffers_Object = MibScalar
memBuffers = _MemBuffers_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 10, 3),
    _MemBuffers_Type()
)
memBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBuffers.setStatus("current")
_MemCached_Type = Integer32
_MemCached_Object = MibScalar
memCached = _MemCached_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 1, 10, 4),
    _MemCached_Type()
)
memCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCached.setStatus("current")
_BelairSysTraps_ObjectIdentity = ObjectIdentity
belairSysTraps = _BelairSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2)
)
if mibBuilder.loadTexts:
    belairSysTraps.setStatus("current")
_BelairSysTrapsV2_ObjectIdentity = ObjectIdentity
belairSysTrapsV2 = _BelairSysTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0)
)
if mibBuilder.loadTexts:
    belairSysTrapsV2.setStatus("current")
_BelairSysConformance_ObjectIdentity = ObjectIdentity
belairSysConformance = _BelairSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 3)
)
if mibBuilder.loadTexts:
    belairSysConformance.setStatus("current")

# Managed Objects groups

belairSysObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 3, 2)
)
belairSysObjectGroup.setObjects(
      *(("BELAIR-SYSTEM", "belairSysFtpServer"),
        ("BELAIR-SYSTEM", "belairSysFtpUserId"),
        ("BELAIR-SYSTEM", "belairSysFtpPassword"),
        ("BELAIR-SYSTEM", "belairSysFtpRemotePath"),
        ("BELAIR-SYSTEM", "belairSysTftpServer"),
        ("BELAIR-SYSTEM", "belairSysTftpRemotePath"),
        ("BELAIR-SYSTEM", "belairSysSntpServer"),
        ("BELAIR-SYSTEM", "belairSysSntpEnabled"),
        ("BELAIR-SYSTEM", "belairSysSntpStatus"),
        ("BELAIR-SYSTEM", "belairSysReboot"),
        ("BELAIR-SYSTEM", "belairSwMgmtActiveBank"),
        ("BELAIR-SYSTEM", "belairSwMgmtNextBank"),
        ("BELAIR-SYSTEM", "belairSwMgmtAction"),
        ("BELAIR-SYSTEM", "belairSwMgmtStatus"),
        ("BELAIR-SYSTEM", "belairSwImageDescription"),
        ("BELAIR-SYSTEM", "belairActiveAlarmTime"),
        ("BELAIR-SYSTEM", "belairActiveAlarmSeverity"),
        ("BELAIR-SYSTEM", "belairActiveAlarmDescription"),
        ("BELAIR-SYSTEM", "belairSysCurrentTemperature"),
        ("BELAIR-SYSTEM", "belairSysHighTempThreshold"),
        ("BELAIR-SYSTEM", "belairSysLowTempThreshold"),
        ("BELAIR-SYSTEM", "belairSysCurrentHumidity"),
        ("BELAIR-SYSTEM", "belairSysHighHumidityThreshold"),
        ("BELAIR-SYSTEM", "belairSysBatteryStatus"),
        ("BELAIR-SYSTEM", "belairSysBatteryVoltage"),
        ("BELAIR-SYSTEM", "belairSysBatteryLowThreshold"),
        ("BELAIR-SYSTEM", "belairTrapAlarmId"),
        ("BELAIR-SYSTEM", "belairCardOperStatus"),
        ("BELAIR-SYSTEM", "belairCardAdminStatus"),
        ("BELAIR-SYSTEM", "belairActiveAlarmId"),
        ("BELAIR-SYSTEM", "belairActiveAlarmInstanceOid"),
        ("BELAIR-SYSTEM", "belairSysConfigRestoreStatus"),
        ("BELAIR-SYSTEM", "belairSysConfigRestoreAction"),
        ("BELAIR-SYSTEM", "belairSysConfigSaveStatus"),
        ("BELAIR-SYSTEM", "belairSysConfigSaveAction"),
        ("BELAIR-SYSTEM", "baSysLatitudeDegrees"),
        ("BELAIR-SYSTEM", "baSysLatitudeMinutes"),
        ("BELAIR-SYSTEM", "baSysLatitudeSeconds"),
        ("BELAIR-SYSTEM", "baSysLatitudeMilliSeconds"),
        ("BELAIR-SYSTEM", "baSysLongitudeDegrees"),
        ("BELAIR-SYSTEM", "baSysLongitudeMinutes"),
        ("BELAIR-SYSTEM", "baSysLongitudeSeconds"),
        ("BELAIR-SYSTEM", "baSysLongitudeMilliSeconds"),
        ("BELAIR-SYSTEM", "belairCardDescription"),
        ("BELAIR-SYSTEM", "belairCardHwVariant"),
        ("BELAIR-SYSTEM", "belairCardSerialNumber"),
        ("BELAIR-SYSTEM", "belairCardMfgCode"),
        ("BELAIR-SYSTEM", "belairSysBatteryEnabled"),
        ("BELAIR-SYSTEM", "belairTrapSequenceNumber"),
        ("BELAIR-SYSTEM", "belairSysLastConfigChange"),
        ("BELAIR-SYSTEM", "belairTrapDetailInfo"),
        ("BELAIR-SYSTEM", "belairTrapIpAddress"),
        ("BELAIR-SYSTEM", "belairSysConfigUnsaved"),
        ("BELAIR-SYSTEM", "belairCustomFieldValue"),
        ("BELAIR-SYSTEM", "memCached"),
        ("BELAIR-SYSTEM", "memBuffers"),
        ("BELAIR-SYSTEM", "memFree"),
        ("BELAIR-SYSTEM", "memTotal"),
        ("BELAIR-SYSTEM", "belairSysLastRebootReason"),
        ("BELAIR-SYSTEM", "belairSysLastRebootType"),
        ("BELAIR-SYSTEM", "belairAutoUpgradeEnabled"),
        ("BELAIR-SYSTEM", "belairTrapSeverity"),
        ("BELAIR-SYSTEM", "belairSysASMPresent"))
)
if mibBuilder.loadTexts:
    belairSysObjectGroup.setStatus("current")

belairSysDeprecatedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 3, 4)
)
belairSysDeprecatedObjectGroup.setObjects(
      *(("BELAIR-SYSTEM", "belairActiveAlarmObject"),
        ("BELAIR-SYSTEM", "belairActiveAlarmObjectType"))
)
if mibBuilder.loadTexts:
    belairSysDeprecatedObjectGroup.setStatus("deprecated")


# Notification objects

belairSntpOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 1)
)
belairSntpOperStatusChange.setObjects(
    ("BELAIR-SYSTEM", "belairSysSntpStatus")
)
if mibBuilder.loadTexts:
    belairSntpOperStatusChange.setStatus(
        "current"
    )

belairSwMgmtStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 2)
)
belairSwMgmtStatusChange.setObjects(
    ("BELAIR-SYSTEM", "belairSwMgmtStatus")
)
if mibBuilder.loadTexts:
    belairSwMgmtStatusChange.setStatus(
        "current"
    )

belairSysTemperatureChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 3)
)
belairSysTemperatureChange.setObjects(
    ("BELAIR-SYSTEM", "belairSysCurrentTemperature")
)
if mibBuilder.loadTexts:
    belairSysTemperatureChange.setStatus(
        "current"
    )

belairSysHumidityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 4)
)
belairSysHumidityChange.setObjects(
    ("BELAIR-SYSTEM", "belairSysCurrentHumidity")
)
if mibBuilder.loadTexts:
    belairSysHumidityChange.setStatus(
        "current"
    )

belairSysBatteryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 5)
)
belairSysBatteryStatusChange.setObjects(
    ("BELAIR-SYSTEM", "belairSysBatteryStatus")
)
if mibBuilder.loadTexts:
    belairSysBatteryStatusChange.setStatus(
        "current"
    )

belairSysGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    belairSysGenericTrap.setStatus(
        "current"
    )

belairCardStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 7)
)
belairCardStatusChange.setObjects(
      *(("BELAIR-SYSTEM", "belairCardAdminStatus"),
        ("BELAIR-SYSTEM", "belairCardOperStatus"))
)
if mibBuilder.loadTexts:
    belairCardStatusChange.setStatus(
        "current"
    )

belairConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 8)
)
belairConfigChange.setObjects(
    ("BELAIR-SYSTEM", "belairSysLastConfigChange")
)
if mibBuilder.loadTexts:
    belairConfigChange.setStatus(
        "current"
    )

belairAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 9)
)
belairAuthenticationFailure.setObjects(
      *(("BELAIR-SYSTEM", "belairTrapIpAddress"),
        ("BELAIR-SYSTEM", "belairTrapDetailInfo"))
)
if mibBuilder.loadTexts:
    belairAuthenticationFailure.setStatus(
        "current"
    )

belairGenericInterfaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 2, 0, 10)
)
belairGenericInterfaceTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    belairGenericInterfaceTrap.setStatus(
        "current"
    )


# Notifications groups

belairSysTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 3, 1, 3, 1)
)
belairSysTrapsGroup.setObjects(
      *(("BELAIR-SYSTEM", "belairSntpOperStatusChange"),
        ("BELAIR-SYSTEM", "belairSwMgmtStatusChange"),
        ("BELAIR-SYSTEM", "belairSysTemperatureChange"),
        ("BELAIR-SYSTEM", "belairSysHumidityChange"),
        ("BELAIR-SYSTEM", "belairSysBatteryStatusChange"),
        ("BELAIR-SYSTEM", "belairSysGenericTrap"),
        ("BELAIR-SYSTEM", "belairCardStatusChange"),
        ("BELAIR-SYSTEM", "belairConfigChange"),
        ("BELAIR-SYSTEM", "belairAuthenticationFailure"),
        ("BELAIR-SYSTEM", "belairGenericInterfaceTrap"))
)
if mibBuilder.loadTexts:
    belairSysTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-SYSTEM",
    **{"belairSystemModule": belairSystemModule,
       "belairSystem": belairSystem,
       "belairSysObjects": belairSysObjects,
       "belairSysPeripheral": belairSysPeripheral,
       "belairSysASMPresent": belairSysASMPresent,
       "belairSysAdmin": belairSysAdmin,
       "belairSysFtpServer": belairSysFtpServer,
       "belairSysFtpUserId": belairSysFtpUserId,
       "belairSysFtpPassword": belairSysFtpPassword,
       "belairSysFtpRemotePath": belairSysFtpRemotePath,
       "belairSysTftpServer": belairSysTftpServer,
       "belairSysTftpRemotePath": belairSysTftpRemotePath,
       "belairSysSntpServer": belairSysSntpServer,
       "belairSysSntpEnabled": belairSysSntpEnabled,
       "belairSysSntpStatus": belairSysSntpStatus,
       "belairSysReboot": belairSysReboot,
       "belairSysConfigSaveAction": belairSysConfigSaveAction,
       "belairSysConfigSaveStatus": belairSysConfigSaveStatus,
       "belairSysConfigRestoreAction": belairSysConfigRestoreAction,
       "belairSysConfigRestoreStatus": belairSysConfigRestoreStatus,
       "belairSysLastConfigChange": belairSysLastConfigChange,
       "belairSysConfigUnsaved": belairSysConfigUnsaved,
       "belairSysLastRebootType": belairSysLastRebootType,
       "belairSysLastRebootReason": belairSysLastRebootReason,
       "belairSysSoftwareMgmt": belairSysSoftwareMgmt,
       "belairSwMgmtActiveBank": belairSwMgmtActiveBank,
       "belairSwMgmtNextBank": belairSwMgmtNextBank,
       "belairSwMgmtAction": belairSwMgmtAction,
       "belairSwMgmtStatus": belairSwMgmtStatus,
       "belairSwImageTable": belairSwImageTable,
       "belairSwImageEntry": belairSwImageEntry,
       "belairSwImageBank": belairSwImageBank,
       "belairSwImageDescription": belairSwImageDescription,
       "belairAutoUpgradeEnabled": belairAutoUpgradeEnabled,
       "belairCardTable": belairCardTable,
       "belairCardEntry": belairCardEntry,
       "belairCardType": belairCardType,
       "belairCardIndex": belairCardIndex,
       "belairCardAdminStatus": belairCardAdminStatus,
       "belairCardOperStatus": belairCardOperStatus,
       "belairCardDescription": belairCardDescription,
       "belairCardHwVariant": belairCardHwVariant,
       "belairCardSerialNumber": belairCardSerialNumber,
       "belairCardMfgCode": belairCardMfgCode,
       "belairAlarms": belairAlarms,
       "belairActiveAlarmTable": belairActiveAlarmTable,
       "belairActiveAlarmEntry": belairActiveAlarmEntry,
       "belairActiveAlarmId": belairActiveAlarmId,
       "belairActiveAlarmObject": belairActiveAlarmObject,
       "belairActiveAlarmObjectType": belairActiveAlarmObjectType,
       "belairActiveAlarmTime": belairActiveAlarmTime,
       "belairActiveAlarmSeverity": belairActiveAlarmSeverity,
       "belairActiveAlarmDescription": belairActiveAlarmDescription,
       "belairActiveAlarmIndex": belairActiveAlarmIndex,
       "belairActiveAlarmInstanceOid": belairActiveAlarmInstanceOid,
       "belairEnvironment": belairEnvironment,
       "belairSysCurrentTemperature": belairSysCurrentTemperature,
       "belairSysHighTempThreshold": belairSysHighTempThreshold,
       "belairSysLowTempThreshold": belairSysLowTempThreshold,
       "belairSysCurrentHumidity": belairSysCurrentHumidity,
       "belairSysHighHumidityThreshold": belairSysHighHumidityThreshold,
       "belairSysBatteryStatus": belairSysBatteryStatus,
       "belairSysBatteryVoltage": belairSysBatteryVoltage,
       "belairSysBatteryLowThreshold": belairSysBatteryLowThreshold,
       "belairSysBatteryEnabled": belairSysBatteryEnabled,
       "belairTrapVarbindObjects": belairTrapVarbindObjects,
       "belairTrapAlarmId": belairTrapAlarmId,
       "belairTrapSeverity": belairTrapSeverity,
       "belairTrapSequenceNumber": belairTrapSequenceNumber,
       "belairTrapDetailInfo": belairTrapDetailInfo,
       "belairTrapIpAddress": belairTrapIpAddress,
       "belairSysCoordinates": belairSysCoordinates,
       "baSysLatitudeDegrees": baSysLatitudeDegrees,
       "baSysLatitudeMinutes": baSysLatitudeMinutes,
       "baSysLatitudeSeconds": baSysLatitudeSeconds,
       "baSysLatitudeMilliSeconds": baSysLatitudeMilliSeconds,
       "baSysLongitudeDegrees": baSysLongitudeDegrees,
       "baSysLongitudeMinutes": baSysLongitudeMinutes,
       "baSysLongitudeSeconds": baSysLongitudeSeconds,
       "baSysLongitudeMilliSeconds": baSysLongitudeMilliSeconds,
       "belairCustomFieldTable": belairCustomFieldTable,
       "belairCustomFieldEntry": belairCustomFieldEntry,
       "belairCustomFieldIndex": belairCustomFieldIndex,
       "belairCustomFieldValue": belairCustomFieldValue,
       "belairSysMemory": belairSysMemory,
       "memTotal": memTotal,
       "memFree": memFree,
       "memBuffers": memBuffers,
       "memCached": memCached,
       "belairSysTraps": belairSysTraps,
       "belairSysTrapsV2": belairSysTrapsV2,
       "belairSntpOperStatusChange": belairSntpOperStatusChange,
       "belairSwMgmtStatusChange": belairSwMgmtStatusChange,
       "belairSysTemperatureChange": belairSysTemperatureChange,
       "belairSysHumidityChange": belairSysHumidityChange,
       "belairSysBatteryStatusChange": belairSysBatteryStatusChange,
       "belairSysGenericTrap": belairSysGenericTrap,
       "belairCardStatusChange": belairCardStatusChange,
       "belairConfigChange": belairConfigChange,
       "belairAuthenticationFailure": belairAuthenticationFailure,
       "belairGenericInterfaceTrap": belairGenericInterfaceTrap,
       "belairSysConformance": belairSysConformance,
       "belairSysTrapsGroup": belairSysTrapsGroup,
       "belairSysObjectGroup": belairSysObjectGroup,
       "belairSysDeprecatedObjectGroup": belairSysDeprecatedObjectGroup}
)
