# SNMP MIB module (TROPIC-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-SOFTWARE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnSoftwareMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSoftwareMIB",
    "tnSystemModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmTransferProtocol,
 TnCommand,
 TropicShelfIndexType,
 TropicSlotIndexType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmTransferProtocol",
    "TnCommand",
    "TropicShelfIndexType",
    "TropicSlotIndexType")


# MODULE-IDENTITY

tnSoftwareMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnSoftwareMibModule.setRevisions(
        ("2008-05-02 12:00",
         "2008-05-29 12:00",
         "2008-12-17 12:00",
         "2009-02-01 12:00",
         "2009-02-05 12:00",
         "2009-02-07 12:00",
         "2009-03-02 12:00",
         "2009-03-15 12:00",
         "2009-03-18 12:00",
         "2009-03-31 12:00",
         "2009-09-25 12:00",
         "2009-11-01 12:00",
         "2009-12-10 12:00",
         "2010-01-04 12:00",
         "2010-02-17 12:00",
         "2010-05-07 12:00",
         "2010-05-10 12:00",
         "2010-06-04 12:00",
         "2010-06-25 12:00",
         "2010-07-20 12:00",
         "2010-09-10 12:00",
         "2010-09-20 12:00",
         "2010-09-24 12:00",
         "2010-09-28 12:00",
         "2010-10-17 12:00",
         "2010-10-18 12:00",
         "2010-10-19 12:00",
         "2010-11-10 12:00",
         "2011-03-28 12:00",
         "2011-05-04 12:00",
         "2011-05-17 12:00",
         "2011-06-07 12:00",
         "2011-06-13 12:00",
         "2011-06-30 12:00",
         "2011-07-07 12:00",
         "2011-07-19 12:00",
         "2011-08-31 12:00",
         "2011-09-06 12:00",
         "2011-09-16 12:00",
         "2011-11-14 12:00",
         "2011-11-21 12:00",
         "2012-01-10 12:00",
         "2012-01-18 12:00",
         "2012-01-19 12:00",
         "2012-02-12 12:00",
         "2012-03-18 12:00",
         "2012-03-29 12:00",
         "2012-04-24 12:00",
         "2012-04-27 12:00",
         "2012-05-18 12:00",
         "2012-06-18 12:00",
         "2012-07-24 12:00",
         "2012-08-28 12:00",
         "2013-03-07 12:00",
         "2013-03-16 12:00",
         "2013-04-11 12:00",
         "2013-04-19 12:00",
         "2013-05-21 12:00",
         "2013-05-24 12:00",
         "2013-06-24 12:00",
         "2013-08-12 12:00",
         "2013-09-04 12:00",
         "2003-09-13 12:00",
         "2013-10-07 12:00",
         "2013-10-10 12:00",
         "2013-11-06 12:00",
         "2013-11-25 12:00",
         "2013-12-20 12:00",
         "2014-01-21 12:00",
         "2014-02-03 12:00",
         "2014-02-19 12:00",
         "2014-03-30 12:00",
         "2014-05-06 12:00",
         "2014-06-23 12:00",
         "2014-07-07 12:00",
         "2014-08-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicSwControl(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("unknown", 2),
          ("audit", 3),
          ("activate", 4),
          ("upgradeAuto", 5),
          ("commit", 6),
          ("backout", 7),
          ("load", 8),
          ("cardActivate", 9),
          ("cardLoad", 10),
          ("autoInstall", 11))
    )



class TropicSwBank(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("application0", 2),
          ("application1", 3),
          ("userBoot", 4),
          ("emergencyBoot", 5))
    )



class TropicSwLastOperationStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("completed", 1),
          ("inProgress", 2),
          ("failure", 3),
          ("none", 4))
    )



class TropicSwLastOperationResult(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TropicSwLastOperationPercentCompleted(TextualConvention, Unsigned32):
    status = "current"


class AluWdmPortGroupMode(TextualConvention, Integer32):
    status = "current"
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
        *(("pwrSv", 1),
          ("oth", 2),
          ("ethSth", 3),
          ("eth", 4),
          ("sth", 5),
          ("fc", 6))
    )



# MIB Managed Objects in the order of their OIDs

_TnSoftwareConf_ObjectIdentity = ObjectIdentity
tnSoftwareConf = _TnSoftwareConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1)
)
_TnSoftwareGroups_ObjectIdentity = ObjectIdentity
tnSoftwareGroups = _TnSoftwareGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1)
)
_TnSoftwareCompliances_ObjectIdentity = ObjectIdentity
tnSoftwareCompliances = _TnSoftwareCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 2)
)
_TnSoftwareObjs_ObjectIdentity = ObjectIdentity
tnSoftwareObjs = _TnSoftwareObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2)
)
_TnSoftwareBasics_ObjectIdentity = ObjectIdentity
tnSoftwareBasics = _TnSoftwareBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1)
)
_TnSoftwareNode_ObjectIdentity = ObjectIdentity
tnSoftwareNode = _TnSoftwareNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1)
)


class _TnSwNodeReleaseRoot_Type(SnmpAdminString):
    """Custom type tnSwNodeReleaseRoot based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwNodeReleaseRoot_Type.__name__ = "SnmpAdminString"
_TnSwNodeReleaseRoot_Object = MibScalar
tnSwNodeReleaseRoot = _TnSwNodeReleaseRoot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 2),
    _TnSwNodeReleaseRoot_Type()
)
tnSwNodeReleaseRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeReleaseRoot.setStatus("current")
_TnSwNodeControl_Type = TropicSwControl
_TnSwNodeControl_Object = MibScalar
tnSwNodeControl = _TnSwNodeControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 3),
    _TnSwNodeControl_Type()
)
tnSwNodeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeControl.setStatus("current")


class _TnSwNodeCommittedRelease_Type(SnmpAdminString):
    """Custom type tnSwNodeCommittedRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwNodeCommittedRelease_Type.__name__ = "SnmpAdminString"
_TnSwNodeCommittedRelease_Object = MibScalar
tnSwNodeCommittedRelease = _TnSwNodeCommittedRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 5),
    _TnSwNodeCommittedRelease_Type()
)
tnSwNodeCommittedRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeCommittedRelease.setStatus("current")


class _TnSwNodeWorkingRelease_Type(SnmpAdminString):
    """Custom type tnSwNodeWorkingRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwNodeWorkingRelease_Type.__name__ = "SnmpAdminString"
_TnSwNodeWorkingRelease_Object = MibScalar
tnSwNodeWorkingRelease = _TnSwNodeWorkingRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 6),
    _TnSwNodeWorkingRelease_Type()
)
tnSwNodeWorkingRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeWorkingRelease.setStatus("current")


class _TnSwNodeForce_Type(Integer32):
    """Custom type tnSwNodeForce based on Integer32"""
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
          ("false", 2),
          ("true", 3))
    )


_TnSwNodeForce_Type.__name__ = "Integer32"
_TnSwNodeForce_Object = MibScalar
tnSwNodeForce = _TnSwNodeForce_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 7),
    _TnSwNodeForce_Type()
)
tnSwNodeForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeForce.setStatus("current")


class _TnSwNodeNoBackup_Type(Integer32):
    """Custom type tnSwNodeNoBackup based on Integer32"""
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
          ("false", 2),
          ("true", 3))
    )


_TnSwNodeNoBackup_Type.__name__ = "Integer32"
_TnSwNodeNoBackup_Object = MibScalar
tnSwNodeNoBackup = _TnSwNodeNoBackup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 8),
    _TnSwNodeNoBackup_Type()
)
tnSwNodeNoBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeNoBackup.setStatus("current")
_TnSwNodeUpgradePathAvailable_Type = TruthValue
_TnSwNodeUpgradePathAvailable_Object = MibScalar
tnSwNodeUpgradePathAvailable = _TnSwNodeUpgradePathAvailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 9),
    _TnSwNodeUpgradePathAvailable_Type()
)
tnSwNodeUpgradePathAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeUpgradePathAvailable.setStatus("current")
_TnSwNodeLastControlOperation_Type = TropicSwControl
_TnSwNodeLastControlOperation_Object = MibScalar
tnSwNodeLastControlOperation = _TnSwNodeLastControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 10),
    _TnSwNodeLastControlOperation_Type()
)
tnSwNodeLastControlOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperation.setStatus("current")
_TnSwNodeControlAbort_Type = TnCommand
_TnSwNodeControlAbort_Object = MibScalar
tnSwNodeControlAbort = _TnSwNodeControlAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 11),
    _TnSwNodeControlAbort_Type()
)
tnSwNodeControlAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeControlAbort.setStatus("current")
_TnSwNodeLastControlOperationStatus_Type = TropicSwLastOperationStatus
_TnSwNodeLastControlOperationStatus_Object = MibScalar
tnSwNodeLastControlOperationStatus = _TnSwNodeLastControlOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 12),
    _TnSwNodeLastControlOperationStatus_Type()
)
tnSwNodeLastControlOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationStatus.setStatus("current")
_TnSwNodeLastControlOperationResult_Type = TropicSwLastOperationResult
_TnSwNodeLastControlOperationResult_Object = MibScalar
tnSwNodeLastControlOperationResult = _TnSwNodeLastControlOperationResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 13),
    _TnSwNodeLastControlOperationResult_Type()
)
tnSwNodeLastControlOperationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationResult.setStatus("current")
_TnSwNodeLastControlOperationIntegerResult_Type = Integer32
_TnSwNodeLastControlOperationIntegerResult_Object = MibScalar
tnSwNodeLastControlOperationIntegerResult = _TnSwNodeLastControlOperationIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 14),
    _TnSwNodeLastControlOperationIntegerResult_Type()
)
tnSwNodeLastControlOperationIntegerResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationIntegerResult.setStatus("current")
_TnSwNodeLastControlOperationPercentCompleted_Type = TropicSwLastOperationPercentCompleted
_TnSwNodeLastControlOperationPercentCompleted_Object = MibScalar
tnSwNodeLastControlOperationPercentCompleted = _TnSwNodeLastControlOperationPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 15),
    _TnSwNodeLastControlOperationPercentCompleted_Type()
)
tnSwNodeLastControlOperationPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeLastControlOperationPercentCompleted.setStatus("current")
_TnSwNodeLastAuditTimeStamp_Type = Unsigned32
_TnSwNodeLastAuditTimeStamp_Object = MibScalar
tnSwNodeLastAuditTimeStamp = _TnSwNodeLastAuditTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 16),
    _TnSwNodeLastAuditTimeStamp_Type()
)
tnSwNodeLastAuditTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeLastAuditTimeStamp.setStatus("current")


class _TnSwNodeWorkingReleaseDir_Type(SnmpAdminString):
    """Custom type tnSwNodeWorkingReleaseDir based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwNodeWorkingReleaseDir_Type.__name__ = "SnmpAdminString"
_TnSwNodeWorkingReleaseDir_Object = MibScalar
tnSwNodeWorkingReleaseDir = _TnSwNodeWorkingReleaseDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 18),
    _TnSwNodeWorkingReleaseDir_Type()
)
tnSwNodeWorkingReleaseDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeWorkingReleaseDir.setStatus("current")


class _TnSwNodeActiveRelease_Type(SnmpAdminString):
    """Custom type tnSwNodeActiveRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnSwNodeActiveRelease_Type.__name__ = "SnmpAdminString"
_TnSwNodeActiveRelease_Object = MibScalar
tnSwNodeActiveRelease = _TnSwNodeActiveRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 19),
    _TnSwNodeActiveRelease_Type()
)
tnSwNodeActiveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodeActiveRelease.setStatus("current")
_TnSwNodeSwdlServerProtocol_Type = AluWdmTransferProtocol
_TnSwNodeSwdlServerProtocol_Object = MibScalar
tnSwNodeSwdlServerProtocol = _TnSwNodeSwdlServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 20),
    _TnSwNodeSwdlServerProtocol_Type()
)
tnSwNodeSwdlServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerProtocol.setStatus("current")
_TnSwNodeSwdlServerIp_Type = IpAddress
_TnSwNodeSwdlServerIp_Object = MibScalar
tnSwNodeSwdlServerIp = _TnSwNodeSwdlServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 21),
    _TnSwNodeSwdlServerIp_Type()
)
tnSwNodeSwdlServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerIp.setStatus("current")


class _TnSwNodeSwdlServerUserId_Type(SnmpAdminString):
    """Custom type tnSwNodeSwdlServerUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSwNodeSwdlServerUserId_Type.__name__ = "SnmpAdminString"
_TnSwNodeSwdlServerUserId_Object = MibScalar
tnSwNodeSwdlServerUserId = _TnSwNodeSwdlServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 22),
    _TnSwNodeSwdlServerUserId_Type()
)
tnSwNodeSwdlServerUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerUserId.setStatus("current")


class _TnSwNodeSwdlServerPassword_Type(SnmpAdminString):
    """Custom type tnSwNodeSwdlServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSwNodeSwdlServerPassword_Type.__name__ = "SnmpAdminString"
_TnSwNodeSwdlServerPassword_Object = MibScalar
tnSwNodeSwdlServerPassword = _TnSwNodeSwdlServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 23),
    _TnSwNodeSwdlServerPassword_Type()
)
tnSwNodeSwdlServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodeSwdlServerPassword.setStatus("current")


class _TnSwNodePartialLoadCommand_Type(Integer32):
    """Custom type tnSwNodePartialLoadCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("partialLoad", 2),
          ("forceDownload", 3))
    )


_TnSwNodePartialLoadCommand_Type.__name__ = "Integer32"
_TnSwNodePartialLoadCommand_Object = MibScalar
tnSwNodePartialLoadCommand = _TnSwNodePartialLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 25),
    _TnSwNodePartialLoadCommand_Type()
)
tnSwNodePartialLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadCommand.setStatus("current")


class _TnSwNodePartialLoadSupportedCardTypes_Type(SnmpAdminString):
    """Custom type tnSwNodePartialLoadSupportedCardTypes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSwNodePartialLoadSupportedCardTypes_Type.__name__ = "SnmpAdminString"
_TnSwNodePartialLoadSupportedCardTypes_Object = MibScalar
tnSwNodePartialLoadSupportedCardTypes = _TnSwNodePartialLoadSupportedCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 26),
    _TnSwNodePartialLoadSupportedCardTypes_Type()
)
tnSwNodePartialLoadSupportedCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadSupportedCardTypes.setStatus("current")


class _TnSwNodePartialLoadImgInstalledCardTypes_Type(SnmpAdminString):
    """Custom type tnSwNodePartialLoadImgInstalledCardTypes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSwNodePartialLoadImgInstalledCardTypes_Type.__name__ = "SnmpAdminString"
_TnSwNodePartialLoadImgInstalledCardTypes_Object = MibScalar
tnSwNodePartialLoadImgInstalledCardTypes = _TnSwNodePartialLoadImgInstalledCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 27),
    _TnSwNodePartialLoadImgInstalledCardTypes_Type()
)
tnSwNodePartialLoadImgInstalledCardTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadImgInstalledCardTypes.setStatus("current")


class _TnSwNodePartialLoadImgToBeInstalledCardTypes_Type(SnmpAdminString):
    """Custom type tnSwNodePartialLoadImgToBeInstalledCardTypes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSwNodePartialLoadImgToBeInstalledCardTypes_Type.__name__ = "SnmpAdminString"
_TnSwNodePartialLoadImgToBeInstalledCardTypes_Object = MibScalar
tnSwNodePartialLoadImgToBeInstalledCardTypes = _TnSwNodePartialLoadImgToBeInstalledCardTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 28),
    _TnSwNodePartialLoadImgToBeInstalledCardTypes_Type()
)
tnSwNodePartialLoadImgToBeInstalledCardTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadImgToBeInstalledCardTypes.setStatus("current")
_TnSwNodePartialLoadActionResult_Type = TropicSwLastOperationResult
_TnSwNodePartialLoadActionResult_Object = MibScalar
tnSwNodePartialLoadActionResult = _TnSwNodePartialLoadActionResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 29),
    _TnSwNodePartialLoadActionResult_Type()
)
tnSwNodePartialLoadActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadActionResult.setStatus("current")
_TnSwNodePartialLoadActionPercentCompleted_Type = TropicSwLastOperationPercentCompleted
_TnSwNodePartialLoadActionPercentCompleted_Object = MibScalar
tnSwNodePartialLoadActionPercentCompleted = _TnSwNodePartialLoadActionPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 1, 30),
    _TnSwNodePartialLoadActionPercentCompleted_Type()
)
tnSwNodePartialLoadActionPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwNodePartialLoadActionPercentCompleted.setStatus("current")
_TnSwCardTable_Object = MibTable
tnSwCardTable = _TnSwCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnSwCardTable.setStatus("current")
_TnSwCardEntry_Object = MibTableRow
tnSwCardEntry = _TnSwCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1)
)
tnSwCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSwCardEntry.setStatus("current")


class _TnSwCardAppBank0_Type(SnmpAdminString):
    """Custom type tnSwCardAppBank0 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_TnSwCardAppBank0_Type.__name__ = "SnmpAdminString"
_TnSwCardAppBank0_Object = MibTableColumn
tnSwCardAppBank0 = _TnSwCardAppBank0_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 1),
    _TnSwCardAppBank0_Type()
)
tnSwCardAppBank0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardAppBank0.setStatus("current")


class _TnSwCardAppBank1_Type(SnmpAdminString):
    """Custom type tnSwCardAppBank1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_TnSwCardAppBank1_Type.__name__ = "SnmpAdminString"
_TnSwCardAppBank1_Object = MibTableColumn
tnSwCardAppBank1 = _TnSwCardAppBank1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 2),
    _TnSwCardAppBank1_Type()
)
tnSwCardAppBank1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardAppBank1.setStatus("current")


class _TnSwCardEmergBootBank_Type(SnmpAdminString):
    """Custom type tnSwCardEmergBootBank based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_TnSwCardEmergBootBank_Type.__name__ = "SnmpAdminString"
_TnSwCardEmergBootBank_Object = MibTableColumn
tnSwCardEmergBootBank = _TnSwCardEmergBootBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 3),
    _TnSwCardEmergBootBank_Type()
)
tnSwCardEmergBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardEmergBootBank.setStatus("current")


class _TnSwCardUserBootBank_Type(SnmpAdminString):
    """Custom type tnSwCardUserBootBank based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_TnSwCardUserBootBank_Type.__name__ = "SnmpAdminString"
_TnSwCardUserBootBank_Object = MibTableColumn
tnSwCardUserBootBank = _TnSwCardUserBootBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 4),
    _TnSwCardUserBootBank_Type()
)
tnSwCardUserBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardUserBootBank.setStatus("current")
_TnSwCardActiveBank_Type = TropicSwBank
_TnSwCardActiveBank_Object = MibTableColumn
tnSwCardActiveBank = _TnSwCardActiveBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 5),
    _TnSwCardActiveBank_Type()
)
tnSwCardActiveBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardActiveBank.setStatus("current")
_TnSwCardNextBootBank_Type = TropicSwBank
_TnSwCardNextBootBank_Object = MibTableColumn
tnSwCardNextBootBank = _TnSwCardNextBootBank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 6),
    _TnSwCardNextBootBank_Type()
)
tnSwCardNextBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwCardNextBootBank.setStatus("current")
_TnSwCardBankToActivate_Type = TropicSwBank
_TnSwCardBankToActivate_Object = MibTableColumn
tnSwCardBankToActivate = _TnSwCardBankToActivate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 7),
    _TnSwCardBankToActivate_Type()
)
tnSwCardBankToActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardBankToActivate.setStatus("current")


class _TnSwCardBankToLoad_Type(Integer32):
    """Custom type tnSwCardBankToLoad based on Integer32"""
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
          ("application", 2),
          ("boot", 3))
    )


_TnSwCardBankToLoad_Type.__name__ = "Integer32"
_TnSwCardBankToLoad_Object = MibTableColumn
tnSwCardBankToLoad = _TnSwCardBankToLoad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 8),
    _TnSwCardBankToLoad_Type()
)
tnSwCardBankToLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardBankToLoad.setStatus("current")
_TnSwCardControl_Type = TropicSwControl
_TnSwCardControl_Object = MibTableColumn
tnSwCardControl = _TnSwCardControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 9),
    _TnSwCardControl_Type()
)
tnSwCardControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardControl.setStatus("current")


class _TnSwCardReleaseDir_Type(SnmpAdminString):
    """Custom type tnSwCardReleaseDir based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwCardReleaseDir_Type.__name__ = "SnmpAdminString"
_TnSwCardReleaseDir_Object = MibTableColumn
tnSwCardReleaseDir = _TnSwCardReleaseDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 2, 1, 17),
    _TnSwCardReleaseDir_Type()
)
tnSwCardReleaseDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCardReleaseDir.setStatus("current")
_TnSwAuditScriptTable_Object = MibTable
tnSwAuditScriptTable = _TnSwAuditScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnSwAuditScriptTable.setStatus("current")
_TnSwAuditScriptEntry_Object = MibTableRow
tnSwAuditScriptEntry = _TnSwAuditScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1)
)
tnSwAuditScriptEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnSwAuditScriptStage"),
    (0, "TROPIC-SOFTWARE-MIB", "tnSwAuditScriptStep"),
)
if mibBuilder.loadTexts:
    tnSwAuditScriptEntry.setStatus("current")
_TnSwAuditScriptStage_Type = Unsigned32
_TnSwAuditScriptStage_Object = MibTableColumn
tnSwAuditScriptStage = _TnSwAuditScriptStage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 1),
    _TnSwAuditScriptStage_Type()
)
tnSwAuditScriptStage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSwAuditScriptStage.setStatus("current")
_TnSwAuditScriptStep_Type = Unsigned32
_TnSwAuditScriptStep_Object = MibTableColumn
tnSwAuditScriptStep = _TnSwAuditScriptStep_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 2),
    _TnSwAuditScriptStep_Type()
)
tnSwAuditScriptStep.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSwAuditScriptStep.setStatus("current")
_TnSwAuditScriptShelf_Type = TropicShelfIndexType
_TnSwAuditScriptShelf_Object = MibTableColumn
tnSwAuditScriptShelf = _TnSwAuditScriptShelf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 3),
    _TnSwAuditScriptShelf_Type()
)
tnSwAuditScriptShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptShelf.setStatus("current")
_TnSwAuditScriptSlot_Type = TropicSlotIndexType
_TnSwAuditScriptSlot_Object = MibTableColumn
tnSwAuditScriptSlot = _TnSwAuditScriptSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 4),
    _TnSwAuditScriptSlot_Type()
)
tnSwAuditScriptSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptSlot.setStatus("current")
_TnSwAuditScriptCardType_Type = ObjectIdentifier
_TnSwAuditScriptCardType_Object = MibTableColumn
tnSwAuditScriptCardType = _TnSwAuditScriptCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 5),
    _TnSwAuditScriptCardType_Type()
)
tnSwAuditScriptCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptCardType.setStatus("current")


class _TnSwAuditScriptAction_Type(SnmpAdminString):
    """Custom type tnSwAuditScriptAction based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwAuditScriptAction_Type.__name__ = "SnmpAdminString"
_TnSwAuditScriptAction_Object = MibTableColumn
tnSwAuditScriptAction = _TnSwAuditScriptAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 7),
    _TnSwAuditScriptAction_Type()
)
tnSwAuditScriptAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptAction.setStatus("current")


class _TnSwAuditScriptActionStatus_Type(SnmpAdminString):
    """Custom type tnSwAuditScriptActionStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSwAuditScriptActionStatus_Type.__name__ = "SnmpAdminString"
_TnSwAuditScriptActionStatus_Object = MibTableColumn
tnSwAuditScriptActionStatus = _TnSwAuditScriptActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 8),
    _TnSwAuditScriptActionStatus_Type()
)
tnSwAuditScriptActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptActionStatus.setStatus("current")
_TnSwAuditScriptActionResult_Type = TropicSwLastOperationResult
_TnSwAuditScriptActionResult_Object = MibTableColumn
tnSwAuditScriptActionResult = _TnSwAuditScriptActionResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 9),
    _TnSwAuditScriptActionResult_Type()
)
tnSwAuditScriptActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptActionResult.setStatus("current")
_TnSwAuditScriptActionPercentCompleted_Type = TropicSwLastOperationPercentCompleted
_TnSwAuditScriptActionPercentCompleted_Object = MibTableColumn
tnSwAuditScriptActionPercentCompleted = _TnSwAuditScriptActionPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 10),
    _TnSwAuditScriptActionPercentCompleted_Type()
)
tnSwAuditScriptActionPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptActionPercentCompleted.setStatus("current")
_TnSwAuditScriptResultTimeStamp_Type = Unsigned32
_TnSwAuditScriptResultTimeStamp_Object = MibTableColumn
tnSwAuditScriptResultTimeStamp = _TnSwAuditScriptResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 3, 1, 11),
    _TnSwAuditScriptResultTimeStamp_Type()
)
tnSwAuditScriptResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSwAuditScriptResultTimeStamp.setStatus("current")
_TnSwCpldTable_Object = MibTable
tnSwCpldTable = _TnSwCpldTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnSwCpldTable.setStatus("current")
_TnSwCpldEntry_Object = MibTableRow
tnSwCpldEntry = _TnSwCpldEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 4, 1)
)
tnSwCpldEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSwCpldEntry.setStatus("current")


class _TnSwCpldProgramControl_Type(Integer32):
    """Custom type tnSwCpldProgramControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("gentle", 2),
          ("force", 3))
    )


_TnSwCpldProgramControl_Type.__name__ = "Integer32"
_TnSwCpldProgramControl_Object = MibTableColumn
tnSwCpldProgramControl = _TnSwCpldProgramControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 4, 1, 1),
    _TnSwCpldProgramControl_Type()
)
tnSwCpldProgramControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSwCpldProgramControl.setStatus("current")
_TnFwCardTable_Object = MibTable
tnFwCardTable = _TnFwCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnFwCardTable.setStatus("current")
_TnFwCardEntry_Object = MibTableRow
tnFwCardEntry = _TnFwCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1)
)
tnFwCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnFwCardEntry.setStatus("current")


class _TnFwCardCurrentBundle_Type(SnmpAdminString):
    """Custom type tnFwCardCurrentBundle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnFwCardCurrentBundle_Type.__name__ = "SnmpAdminString"
_TnFwCardCurrentBundle_Object = MibTableColumn
tnFwCardCurrentBundle = _TnFwCardCurrentBundle_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 1),
    _TnFwCardCurrentBundle_Type()
)
tnFwCardCurrentBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardCurrentBundle.setStatus("current")
_TnFwCardLoadedAt_Type = Unsigned32
_TnFwCardLoadedAt_Object = MibTableColumn
tnFwCardLoadedAt = _TnFwCardLoadedAt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 2),
    _TnFwCardLoadedAt_Type()
)
tnFwCardLoadedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardLoadedAt.setStatus("current")


class _TnFwCardLoadBundle_Type(SnmpAdminString):
    """Custom type tnFwCardLoadBundle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnFwCardLoadBundle_Type.__name__ = "SnmpAdminString"
_TnFwCardLoadBundle_Object = MibTableColumn
tnFwCardLoadBundle = _TnFwCardLoadBundle_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 3),
    _TnFwCardLoadBundle_Type()
)
tnFwCardLoadBundle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFwCardLoadBundle.setStatus("current")
_TnFwCardProvisionedAt_Type = Unsigned32
_TnFwCardProvisionedAt_Object = MibTableColumn
tnFwCardProvisionedAt = _TnFwCardProvisionedAt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 4),
    _TnFwCardProvisionedAt_Type()
)
tnFwCardProvisionedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardProvisionedAt.setStatus("current")


class _TnFwCardLoadState_Type(Integer32):
    """Custom type tnFwCardLoadState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("loaded", 2),
          ("init1", 3),
          ("init2", 4),
          ("init3", 5),
          ("init4", 6),
          ("init5", 7),
          ("init6", 8),
          ("init7", 9),
          ("init8", 10),
          ("init9", 11),
          ("init10", 12),
          ("failed", 13),
          ("timeOut", 14))
    )


_TnFwCardLoadState_Type.__name__ = "Integer32"
_TnFwCardLoadState_Object = MibTableColumn
tnFwCardLoadState = _TnFwCardLoadState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 5),
    _TnFwCardLoadState_Type()
)
tnFwCardLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardLoadState.setStatus("current")
_TnFwCardWatchDog_Type = Unsigned32
_TnFwCardWatchDog_Object = MibTableColumn
tnFwCardWatchDog = _TnFwCardWatchDog_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 6),
    _TnFwCardWatchDog_Type()
)
tnFwCardWatchDog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardWatchDog.setStatus("current")


class _TnFwCardProvisioningInfo_Type(SnmpAdminString):
    """Custom type tnFwCardProvisioningInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnFwCardProvisioningInfo_Type.__name__ = "SnmpAdminString"
_TnFwCardProvisioningInfo_Object = MibTableColumn
tnFwCardProvisioningInfo = _TnFwCardProvisioningInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 5, 1, 7),
    _TnFwCardProvisioningInfo_Type()
)
tnFwCardProvisioningInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwCardProvisioningInfo.setStatus("current")
_TnInstalledFwTable_Object = MibTable
tnInstalledFwTable = _TnInstalledFwTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnInstalledFwTable.setStatus("current")
_TnInstalledFwEntry_Object = MibTableRow
tnInstalledFwEntry = _TnInstalledFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1)
)
tnInstalledFwEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwCardType"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwFileName"),
)
if mibBuilder.loadTexts:
    tnInstalledFwEntry.setStatus("current")
_TnInstalledFwCardType_Type = Unsigned32
_TnInstalledFwCardType_Object = MibTableColumn
tnInstalledFwCardType = _TnInstalledFwCardType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1, 1),
    _TnInstalledFwCardType_Type()
)
tnInstalledFwCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwCardType.setStatus("current")
_TnInstalledFwFileName_Type = SnmpAdminString
_TnInstalledFwFileName_Object = MibTableColumn
tnInstalledFwFileName = _TnInstalledFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1, 2),
    _TnInstalledFwFileName_Type()
)
tnInstalledFwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInstalledFwFileName.setStatus("current")
_TnInstalledFwIsDefault_Type = TruthValue
_TnInstalledFwIsDefault_Object = MibTableColumn
tnInstalledFwIsDefault = _TnInstalledFwIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 6, 1, 3),
    _TnInstalledFwIsDefault_Type()
)
tnInstalledFwIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInstalledFwIsDefault.setStatus("current")
_TnPortGroupTable_Object = MibTable
tnPortGroupTable = _TnPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnPortGroupTable.setStatus("current")
_TnPortGroupEntry_Object = MibTableRow
tnPortGroupEntry = _TnPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1)
)
tnPortGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPortGroupEntry.setStatus("current")
_TnPortGroupMode_Type = AluWdmPortGroupMode
_TnPortGroupMode_Object = MibTableColumn
tnPortGroupMode = _TnPortGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1, 1),
    _TnPortGroupMode_Type()
)
tnPortGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortGroupMode.setStatus("current")


class _TnPortGroupFwDownload_Type(SnmpAdminString):
    """Custom type tnPortGroupFwDownload based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPortGroupFwDownload_Type.__name__ = "SnmpAdminString"
_TnPortGroupFwDownload_Object = MibTableColumn
tnPortGroupFwDownload = _TnPortGroupFwDownload_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1, 2),
    _TnPortGroupFwDownload_Type()
)
tnPortGroupFwDownload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortGroupFwDownload.setStatus("current")


class _TnPortGroupFwCurrent_Type(SnmpAdminString):
    """Custom type tnPortGroupFwCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPortGroupFwCurrent_Type.__name__ = "SnmpAdminString"
_TnPortGroupFwCurrent_Object = MibTableColumn
tnPortGroupFwCurrent = _TnPortGroupFwCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 7, 1, 3),
    _TnPortGroupFwCurrent_Type()
)
tnPortGroupFwCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortGroupFwCurrent.setStatus("current")
_TnInstalledFwPortGroupTable_Object = MibTable
tnInstalledFwPortGroupTable = _TnInstalledFwPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupTable.setStatus("current")
_TnInstalledFwPortGroupEntry_Object = MibTableRow
tnInstalledFwPortGroupEntry = _TnInstalledFwPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1)
)
tnInstalledFwPortGroupEntry.setIndexNames(
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwCardType"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwFileName"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupMode"),
    (0, "TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupFw"),
)
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupEntry.setStatus("current")
_TnInstalledFwPortGroupMode_Type = AluWdmPortGroupMode
_TnInstalledFwPortGroupMode_Object = MibTableColumn
tnInstalledFwPortGroupMode = _TnInstalledFwPortGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1, 1),
    _TnInstalledFwPortGroupMode_Type()
)
tnInstalledFwPortGroupMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupMode.setStatus("current")


class _TnInstalledFwPortGroupFw_Type(SnmpAdminString):
    """Custom type tnInstalledFwPortGroupFw based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnInstalledFwPortGroupFw_Type.__name__ = "SnmpAdminString"
_TnInstalledFwPortGroupFw_Object = MibTableColumn
tnInstalledFwPortGroupFw = _TnInstalledFwPortGroupFw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1, 2),
    _TnInstalledFwPortGroupFw_Type()
)
tnInstalledFwPortGroupFw.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupFw.setStatus("current")
_TnInstalledFwPortGroupIsDefault_Type = TruthValue
_TnInstalledFwPortGroupIsDefault_Object = MibTableColumn
tnInstalledFwPortGroupIsDefault = _TnInstalledFwPortGroupIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 8, 1, 3),
    _TnInstalledFwPortGroupIsDefault_Type()
)
tnInstalledFwPortGroupIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupIsDefault.setStatus("current")
_TnFwHitlessCardTable_Object = MibTable
tnFwHitlessCardTable = _TnFwHitlessCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnFwHitlessCardTable.setStatus("current")
_TnFwHitlessCardEntry_Object = MibTableRow
tnFwHitlessCardEntry = _TnFwHitlessCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1)
)
tnFwHitlessCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnFwHitlessCardEntry.setStatus("current")
_TnFwHitlessCardTrigger_Type = TruthValue
_TnFwHitlessCardTrigger_Object = MibTableColumn
tnFwHitlessCardTrigger = _TnFwHitlessCardTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1, 1),
    _TnFwHitlessCardTrigger_Type()
)
tnFwHitlessCardTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFwHitlessCardTrigger.setStatus("current")


class _TnFwHitlessCardLoadState_Type(Integer32):
    """Custom type tnFwHitlessCardLoadState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("loaded", 2),
          ("initNsa1", 3),
          ("initNsa2", 4),
          ("initNsa3", 5),
          ("initNsa4", 6),
          ("initNsa5", 7),
          ("initNsa6", 8),
          ("initNsa7", 9),
          ("initNsa8", 10),
          ("initNsa9", 11),
          ("initNsa10", 12),
          ("failed", 13),
          ("timeOut", 14))
    )


_TnFwHitlessCardLoadState_Type.__name__ = "Integer32"
_TnFwHitlessCardLoadState_Object = MibTableColumn
tnFwHitlessCardLoadState = _TnFwHitlessCardLoadState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1, 2),
    _TnFwHitlessCardLoadState_Type()
)
tnFwHitlessCardLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwHitlessCardLoadState.setStatus("current")
_TnFwHitlessCardWatchDog_Type = Unsigned32
_TnFwHitlessCardWatchDog_Object = MibTableColumn
tnFwHitlessCardWatchDog = _TnFwHitlessCardWatchDog_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 2, 1, 9, 1, 3),
    _TnFwHitlessCardWatchDog_Type()
)
tnFwHitlessCardWatchDog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFwHitlessCardWatchDog.setStatus("current")

# Managed Objects groups

tnSwNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 1)
)
tnSwNodeGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwNodeReleaseRoot"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeControl"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeCommittedRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeWorkingRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeForce"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeNoBackup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeUpgradePathAvailable"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperation"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeControlAbort"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationStatus"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationIntegerResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastControlOperationPercentCompleted"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeLastAuditTimeStamp"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeWorkingReleaseDir"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeActiveRelease"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerProtocol"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerIp"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerUserId"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodeSwdlServerPassword"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadCommand"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadSupportedCardTypes"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadImgInstalledCardTypes"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadImgToBeInstalledCardTypes"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadActionResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwNodePartialLoadActionPercentCompleted"))
)
if mibBuilder.loadTexts:
    tnSwNodeGroup.setStatus("current")

tnSwCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 2)
)
tnSwCardGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwCardAppBank0"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardAppBank1"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardEmergBootBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardUserBootBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardActiveBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardNextBootBank"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardBankToActivate"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardBankToLoad"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardControl"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardReleaseDir"))
)
if mibBuilder.loadTexts:
    tnSwCardGroup.setStatus("current")

tnSwAuditScriptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 3)
)
tnSwAuditScriptGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptShelf"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptSlot"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptCardType"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptAction"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptActionStatus"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptActionResult"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptActionPercentCompleted"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptResultTimeStamp"))
)
if mibBuilder.loadTexts:
    tnSwAuditScriptGroup.setStatus("current")

tnSwCpldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 4)
)
tnSwCpldGroup.setObjects(
    ("TROPIC-SOFTWARE-MIB", "tnSwCpldProgramControl")
)
if mibBuilder.loadTexts:
    tnSwCpldGroup.setStatus("current")

tnFwCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 5)
)
tnFwCardGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnFwCardCurrentBundle"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardLoadedAt"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardLoadBundle"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardProvisionedAt"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardLoadState"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardWatchDog"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardProvisioningInfo"))
)
if mibBuilder.loadTexts:
    tnFwCardGroup.setStatus("current")

tnInstalledFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 6)
)
tnInstalledFwGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnInstalledFwCardType"),
        ("TROPIC-SOFTWARE-MIB", "tnInstalledFwFileName"),
        ("TROPIC-SOFTWARE-MIB", "tnInstalledFwIsDefault"))
)
if mibBuilder.loadTexts:
    tnInstalledFwGroup.setStatus("current")

tnPortGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 7)
)
tnPortGroupGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnPortGroupMode"),
        ("TROPIC-SOFTWARE-MIB", "tnPortGroupFwDownload"),
        ("TROPIC-SOFTWARE-MIB", "tnPortGroupFwCurrent"))
)
if mibBuilder.loadTexts:
    tnPortGroupGroup.setStatus("current")

tnInstalledFwPortGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 8)
)
tnInstalledFwPortGroupGroup.setObjects(
    ("TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupIsDefault")
)
if mibBuilder.loadTexts:
    tnInstalledFwPortGroupGroup.setStatus("current")

tnFwHitlessCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 1, 9)
)
tnFwHitlessCardGroup.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardTrigger"),
        ("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardLoadState"),
        ("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardWatchDog"))
)
if mibBuilder.loadTexts:
    tnFwHitlessCardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnSoftwareCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5, 1, 2, 1)
)
tnSoftwareCompliance.setObjects(
      *(("TROPIC-SOFTWARE-MIB", "tnSwNodeGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCardGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwAuditScriptGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnSwCpldGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnFwCardGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnInstalledFwGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnPortGroupGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnInstalledFwPortGroupGroup"),
        ("TROPIC-SOFTWARE-MIB", "tnFwHitlessCardGroup"))
)
if mibBuilder.loadTexts:
    tnSoftwareCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SOFTWARE-MIB",
    **{"TropicSwControl": TropicSwControl,
       "TropicSwBank": TropicSwBank,
       "TropicSwLastOperationStatus": TropicSwLastOperationStatus,
       "TropicSwLastOperationResult": TropicSwLastOperationResult,
       "TropicSwLastOperationPercentCompleted": TropicSwLastOperationPercentCompleted,
       "AluWdmPortGroupMode": AluWdmPortGroupMode,
       "tnSoftwareMibModule": tnSoftwareMibModule,
       "tnSoftwareConf": tnSoftwareConf,
       "tnSoftwareGroups": tnSoftwareGroups,
       "tnSwNodeGroup": tnSwNodeGroup,
       "tnSwCardGroup": tnSwCardGroup,
       "tnSwAuditScriptGroup": tnSwAuditScriptGroup,
       "tnSwCpldGroup": tnSwCpldGroup,
       "tnFwCardGroup": tnFwCardGroup,
       "tnInstalledFwGroup": tnInstalledFwGroup,
       "tnPortGroupGroup": tnPortGroupGroup,
       "tnInstalledFwPortGroupGroup": tnInstalledFwPortGroupGroup,
       "tnFwHitlessCardGroup": tnFwHitlessCardGroup,
       "tnSoftwareCompliances": tnSoftwareCompliances,
       "tnSoftwareCompliance": tnSoftwareCompliance,
       "tnSoftwareObjs": tnSoftwareObjs,
       "tnSoftwareBasics": tnSoftwareBasics,
       "tnSoftwareNode": tnSoftwareNode,
       "tnSwNodeReleaseRoot": tnSwNodeReleaseRoot,
       "tnSwNodeControl": tnSwNodeControl,
       "tnSwNodeCommittedRelease": tnSwNodeCommittedRelease,
       "tnSwNodeWorkingRelease": tnSwNodeWorkingRelease,
       "tnSwNodeForce": tnSwNodeForce,
       "tnSwNodeNoBackup": tnSwNodeNoBackup,
       "tnSwNodeUpgradePathAvailable": tnSwNodeUpgradePathAvailable,
       "tnSwNodeLastControlOperation": tnSwNodeLastControlOperation,
       "tnSwNodeControlAbort": tnSwNodeControlAbort,
       "tnSwNodeLastControlOperationStatus": tnSwNodeLastControlOperationStatus,
       "tnSwNodeLastControlOperationResult": tnSwNodeLastControlOperationResult,
       "tnSwNodeLastControlOperationIntegerResult": tnSwNodeLastControlOperationIntegerResult,
       "tnSwNodeLastControlOperationPercentCompleted": tnSwNodeLastControlOperationPercentCompleted,
       "tnSwNodeLastAuditTimeStamp": tnSwNodeLastAuditTimeStamp,
       "tnSwNodeWorkingReleaseDir": tnSwNodeWorkingReleaseDir,
       "tnSwNodeActiveRelease": tnSwNodeActiveRelease,
       "tnSwNodeSwdlServerProtocol": tnSwNodeSwdlServerProtocol,
       "tnSwNodeSwdlServerIp": tnSwNodeSwdlServerIp,
       "tnSwNodeSwdlServerUserId": tnSwNodeSwdlServerUserId,
       "tnSwNodeSwdlServerPassword": tnSwNodeSwdlServerPassword,
       "tnSwNodePartialLoadCommand": tnSwNodePartialLoadCommand,
       "tnSwNodePartialLoadSupportedCardTypes": tnSwNodePartialLoadSupportedCardTypes,
       "tnSwNodePartialLoadImgInstalledCardTypes": tnSwNodePartialLoadImgInstalledCardTypes,
       "tnSwNodePartialLoadImgToBeInstalledCardTypes": tnSwNodePartialLoadImgToBeInstalledCardTypes,
       "tnSwNodePartialLoadActionResult": tnSwNodePartialLoadActionResult,
       "tnSwNodePartialLoadActionPercentCompleted": tnSwNodePartialLoadActionPercentCompleted,
       "tnSwCardTable": tnSwCardTable,
       "tnSwCardEntry": tnSwCardEntry,
       "tnSwCardAppBank0": tnSwCardAppBank0,
       "tnSwCardAppBank1": tnSwCardAppBank1,
       "tnSwCardEmergBootBank": tnSwCardEmergBootBank,
       "tnSwCardUserBootBank": tnSwCardUserBootBank,
       "tnSwCardActiveBank": tnSwCardActiveBank,
       "tnSwCardNextBootBank": tnSwCardNextBootBank,
       "tnSwCardBankToActivate": tnSwCardBankToActivate,
       "tnSwCardBankToLoad": tnSwCardBankToLoad,
       "tnSwCardControl": tnSwCardControl,
       "tnSwCardReleaseDir": tnSwCardReleaseDir,
       "tnSwAuditScriptTable": tnSwAuditScriptTable,
       "tnSwAuditScriptEntry": tnSwAuditScriptEntry,
       "tnSwAuditScriptStage": tnSwAuditScriptStage,
       "tnSwAuditScriptStep": tnSwAuditScriptStep,
       "tnSwAuditScriptShelf": tnSwAuditScriptShelf,
       "tnSwAuditScriptSlot": tnSwAuditScriptSlot,
       "tnSwAuditScriptCardType": tnSwAuditScriptCardType,
       "tnSwAuditScriptAction": tnSwAuditScriptAction,
       "tnSwAuditScriptActionStatus": tnSwAuditScriptActionStatus,
       "tnSwAuditScriptActionResult": tnSwAuditScriptActionResult,
       "tnSwAuditScriptActionPercentCompleted": tnSwAuditScriptActionPercentCompleted,
       "tnSwAuditScriptResultTimeStamp": tnSwAuditScriptResultTimeStamp,
       "tnSwCpldTable": tnSwCpldTable,
       "tnSwCpldEntry": tnSwCpldEntry,
       "tnSwCpldProgramControl": tnSwCpldProgramControl,
       "tnFwCardTable": tnFwCardTable,
       "tnFwCardEntry": tnFwCardEntry,
       "tnFwCardCurrentBundle": tnFwCardCurrentBundle,
       "tnFwCardLoadedAt": tnFwCardLoadedAt,
       "tnFwCardLoadBundle": tnFwCardLoadBundle,
       "tnFwCardProvisionedAt": tnFwCardProvisionedAt,
       "tnFwCardLoadState": tnFwCardLoadState,
       "tnFwCardWatchDog": tnFwCardWatchDog,
       "tnFwCardProvisioningInfo": tnFwCardProvisioningInfo,
       "tnInstalledFwTable": tnInstalledFwTable,
       "tnInstalledFwEntry": tnInstalledFwEntry,
       "tnInstalledFwCardType": tnInstalledFwCardType,
       "tnInstalledFwFileName": tnInstalledFwFileName,
       "tnInstalledFwIsDefault": tnInstalledFwIsDefault,
       "tnPortGroupTable": tnPortGroupTable,
       "tnPortGroupEntry": tnPortGroupEntry,
       "tnPortGroupMode": tnPortGroupMode,
       "tnPortGroupFwDownload": tnPortGroupFwDownload,
       "tnPortGroupFwCurrent": tnPortGroupFwCurrent,
       "tnInstalledFwPortGroupTable": tnInstalledFwPortGroupTable,
       "tnInstalledFwPortGroupEntry": tnInstalledFwPortGroupEntry,
       "tnInstalledFwPortGroupMode": tnInstalledFwPortGroupMode,
       "tnInstalledFwPortGroupFw": tnInstalledFwPortGroupFw,
       "tnInstalledFwPortGroupIsDefault": tnInstalledFwPortGroupIsDefault,
       "tnFwHitlessCardTable": tnFwHitlessCardTable,
       "tnFwHitlessCardEntry": tnFwHitlessCardEntry,
       "tnFwHitlessCardTrigger": tnFwHitlessCardTrigger,
       "tnFwHitlessCardLoadState": tnFwHitlessCardLoadState,
       "tnFwHitlessCardWatchDog": tnFwHitlessCardWatchDog}
)
