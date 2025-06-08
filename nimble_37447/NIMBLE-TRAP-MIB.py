# SNMP MIB module (NIMBLE-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nimble_37447/NIMBLE-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:45:49 2025
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

(nimble,) = mibBuilder.importSymbols(
    "NIMBLE-MIB",
    "nimble")

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

nimble_traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2)
)
if mibBuilder.loadTexts:
    nimble_traps.setRevisions(
        ("2014-06-13 00:00",
         "2014-05-09 00:00",
         "2012-07-12 00:00",
         "2012-06-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrapObjects_ObjectIdentity = ObjectIdentity
trapObjects = _TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1)
)
_Trapvariables_ObjectIdentity = ObjectIdentity
trapvariables = _Trapvariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1)
)


class _TrapMsg_Type(DisplayString):
    """Custom type trapMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapMsg_Type.__name__ = "DisplayString"
_TrapMsg_Object = MibScalar
trapMsg = _TrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 1),
    _TrapMsg_Type()
)
trapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMsg.setStatus("current")
_TrapSeverity_Type = DisplayString
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 2),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_TrapOriginatorName_Type = DisplayString
_TrapOriginatorName_Object = MibScalar
trapOriginatorName = _TrapOriginatorName_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 3),
    _TrapOriginatorName_Type()
)
trapOriginatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorName.setStatus("current")
_TrapOriginatorSerialNumber_Type = DisplayString
_TrapOriginatorSerialNumber_Object = MibScalar
trapOriginatorSerialNumber = _TrapOriginatorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 4),
    _TrapOriginatorSerialNumber_Type()
)
trapOriginatorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorSerialNumber.setStatus("current")
_TrapOriginatorGroupName_Type = DisplayString
_TrapOriginatorGroupName_Object = MibScalar
trapOriginatorGroupName = _TrapOriginatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 5),
    _TrapOriginatorGroupName_Type()
)
trapOriginatorGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorGroupName.setStatus("current")
_TrapOriginatorGroupID_Type = DisplayString
_TrapOriginatorGroupID_Object = MibScalar
trapOriginatorGroupID = _TrapOriginatorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 6),
    _TrapOriginatorGroupID_Type()
)
trapOriginatorGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorGroupID.setStatus("current")
_TrapTarget_Type = DisplayString
_TrapTarget_Object = MibScalar
trapTarget = _TrapTarget_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 7),
    _TrapTarget_Type()
)
trapTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTarget.setStatus("current")
_TrapTargetType_Type = DisplayString
_TrapTargetType_Object = MibScalar
trapTargetType = _TrapTargetType_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 8),
    _TrapTargetType_Type()
)
trapTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTargetType.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2)
)

# Managed Objects groups


# Notification objects

nimbleDsdRedEntry0101Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 65)
)
nimbleDsdRedEntry0101Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdRedEntry0101Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdGcBehindSpaceRedExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 66)
)
nimbleDsdGcBehindSpaceRedExit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdGcBehindSpaceRedExit.setStatus(
        "current"
    )

nimbleDsdSpaceCrit0103Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 67)
)
nimbleDsdSpaceCrit0103Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceCrit0103Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdSpaceUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 68)
)
nimbleDsdSpaceUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceUtilizationHigh.setStatus(
        "current"
    )

nimbleDsdSpaceUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 69)
)
nimbleDsdSpaceUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceUtilizationOk.setStatus(
        "current"
    )

nimbleDsdSpaceUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 70)
)
nimbleDsdSpaceUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceUtilizationCrit.setStatus(
        "current"
    )

nimbleDsdSpaceRedEntry0107Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 71)
)
nimbleDsdSpaceRedEntry0107Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceRedEntry0107Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdSpaceCrit0110Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 72)
)
nimbleDsdSpaceCrit0110Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceCrit0110Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdGcBehindSpaceRedEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 73)
)
nimbleDsdGcBehindSpaceRedEntry.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdGcBehindSpaceRedEntry.setStatus(
        "current"
    )

nimbleDsdGcBehindSpaceCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 74)
)
nimbleDsdGcBehindSpaceCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdGcBehindSpaceCrit.setStatus(
        "current"
    )

nimbleDsdSpaceDenyWrite = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 75)
)
nimbleDsdSpaceDenyWrite.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceDenyWrite.setStatus(
        "current"
    )

nimbleDsdSpaceRedEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 76)
)
nimbleDsdSpaceRedEntry.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceRedEntry.setStatus(
        "current"
    )

nimbleDsdSpaceRedExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 77)
)
nimbleDsdSpaceRedExit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceRedExit.setStatus(
        "current"
    )

nimbleDsdSpaceCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 78)
)
nimbleDsdSpaceCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceCrit.setStatus(
        "current"
    )

nimbleCtrlrException = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2001)
)
nimbleCtrlrException.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrException.setStatus(
        "current"
    )

nimbleCtrlrTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2002)
)
nimbleCtrlrTakeover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrTakeover.setStatus(
        "current"
    )

nimbleCtrlrStandbyAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2003)
)
nimbleCtrlrStandbyAvail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyAvail.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2004)
)
nimbleCtrlrStandbyUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavail.setStatus(
        "current"
    )

nimbleCtrlrExcessiveRestarts = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2005)
)
nimbleCtrlrExcessiveRestarts.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrExcessiveRestarts.setStatus(
        "current"
    )

nimbleServiceReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2006)
)
nimbleServiceReboot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceReboot.setStatus(
        "current"
    )

nimbleUserReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2007)
)
nimbleUserReboot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserReboot.setStatus(
        "current"
    )

nimbleUserRebootFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2008)
)
nimbleUserRebootFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserRebootFailed.setStatus(
        "current"
    )

nimbleUserHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2009)
)
nimbleUserHalt.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserHalt.setStatus(
        "current"
    )

nimbleUserHaltFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2010)
)
nimbleUserHaltFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserHaltFailed.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavailInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2011)
)
nimbleCtrlrStandbyUnavailInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailInfo.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavailWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2012)
)
nimbleCtrlrStandbyUnavailWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailWarn.setStatus(
        "current"
    )

nimbleCtrlrExceptionWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2013)
)
nimbleCtrlrExceptionWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrExceptionWarn.setStatus(
        "current"
    )

nimbleCtrlrExceptionCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2014)
)
nimbleCtrlrExceptionCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrExceptionCrit.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavailWarnTimeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2015)
)
nimbleCtrlrStandbyUnavailWarnTimeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailWarnTimeDeprecated.setStatus(
        "obsolete"
    )

nimbleCtrlrStandbyUnavailWarnTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2016)
)
nimbleCtrlrStandbyUnavailWarnTime.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailWarnTime.setStatus(
        "current"
    )

nimbleCtrlrTakeoverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2017)
)
nimbleCtrlrTakeoverWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrTakeoverWarn.setStatus(
        "current"
    )

nimbleCtrlrFailoverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2018)
)
nimbleCtrlrFailoverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailoverDeprecated.setStatus(
        "obsolete"
    )

nimbleCtrlrFailoverDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2019)
)
nimbleCtrlrFailoverDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailoverDeprecated2.setStatus(
        "obsolete"
    )

nimbleCtrlrWatchdogDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2020)
)
nimbleCtrlrWatchdogDisabled.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrWatchdogDisabled.setStatus(
        "current"
    )

nimbleCtrlrFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2021)
)
nimbleCtrlrFailover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailover.setStatus(
        "current"
    )

nimbleCtrlrFailoverAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2022)
)
nimbleCtrlrFailoverAttempt.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailoverAttempt.setStatus(
        "current"
    )

nimbleCtrlrFailoverFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2023)
)
nimbleCtrlrFailoverFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailoverFail.setStatus(
        "current"
    )

nimbleCtrlrFailoverSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2024)
)
nimbleCtrlrFailoverSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailoverSuccess.setStatus(
        "current"
    )

nimbleCtrlrRaidAssemblyErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2025)
)
nimbleCtrlrRaidAssemblyErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrRaidAssemblyErr.setStatus(
        "current"
    )

nimbleCtrlrRaidAssemblyDeg = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2026)
)
nimbleCtrlrRaidAssemblyDeg.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrRaidAssemblyDeg.setStatus(
        "current"
    )

nimbleCtrlrDegradedMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2027)
)
nimbleCtrlrDegradedMode.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrDegradedMode.setStatus(
        "current"
    )

nimbleCtrlrRebootUnexpected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2028)
)
nimbleCtrlrRebootUnexpected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrRebootUnexpected.setStatus(
        "current"
    )

nimbleUserHaltArrayFailedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2029)
)
nimbleUserHaltArrayFailedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserHaltArrayFailedDeprecated.setStatus(
        "obsolete"
    )

nimbleUserRebootArrayFailedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2030)
)
nimbleUserRebootArrayFailedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserRebootArrayFailedDeprecated.setStatus(
        "obsolete"
    )

nimbleUserHaltArrayFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2031)
)
nimbleUserHaltArrayFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserHaltArrayFailed.setStatus(
        "current"
    )

nimbleUserRebootArrayFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2032)
)
nimbleUserRebootArrayFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserRebootArrayFailed.setStatus(
        "current"
    )

nimbleServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2101)
)
nimbleServiceStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceStarted.setStatus(
        "current"
    )

nimbleServiceDeadRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2102)
)
nimbleServiceDeadRestart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceDeadRestart.setStatus(
        "current"
    )

nimbleServiceDeadNoRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2103)
)
nimbleServiceDeadNoRestart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceDeadNoRestart.setStatus(
        "current"
    )

nimbleServiceCreateTunnelDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2104)
)
nimbleServiceCreateTunnelDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceCreateTunnelDeprecated.setStatus(
        "obsolete"
    )

nimbleServiceTerminateTunnelDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2105)
)
nimbleServiceTerminateTunnelDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceTerminateTunnelDeprecated.setStatus(
        "obsolete"
    )

nimbleServiceEssentialStoppedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2106)
)
nimbleServiceEssentialStoppedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEssentialStoppedDeprecated.setStatus(
        "obsolete"
    )

nimbleServiceEssentialStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2107)
)
nimbleServiceEssentialStopped.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEssentialStopped.setStatus(
        "current"
    )

nimbleServiceEmailAlertFailedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2108)
)
nimbleServiceEmailAlertFailedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEmailAlertFailedDeprecated.setStatus(
        "obsolete"
    )

nimbleServiceEmailAlertFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2109)
)
nimbleServiceEmailAlertFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEmailAlertFailed.setStatus(
        "current"
    )

nimbleServiceManuallyDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2110)
)
nimbleServiceManuallyDisabled.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceManuallyDisabled.setStatus(
        "current"
    )

nimbleServiceCreateTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2111)
)
nimbleServiceCreateTunnel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceCreateTunnel.setStatus(
        "current"
    )

nimbleServiceTerminateTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2112)
)
nimbleServiceTerminateTunnel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceTerminateTunnel.setStatus(
        "current"
    )

nimbleTestDbg = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5000)
)
nimbleTestDbg.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestDbg.setStatus(
        "current"
    )

nimbleTestInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5001)
)
nimbleTestInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestInfo.setStatus(
        "current"
    )

nimbleTestErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5002)
)
nimbleTestErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestErr.setStatus(
        "current"
    )

nimbleTestNot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5003)
)
nimbleTestNot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestNot.setStatus(
        "current"
    )

nimbleTestNoteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5004)
)
nimbleTestNoteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestNoteDeprecated.setStatus(
        "obsolete"
    )

nimbleTestWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5005)
)
nimbleTestWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestWarn.setStatus(
        "current"
    )

nimbleTestCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5006)
)
nimbleTestCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestCrit.setStatus(
        "current"
    )

nimbleTestNote = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5007)
)
nimbleTestNote.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestNote.setStatus(
        "current"
    )

nimbleUpdateUnpackFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6000)
)
nimbleUpdateUnpackFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnpackFail.setStatus(
        "current"
    )

nimbleUpdateStartedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6001)
)
nimbleUpdateStartedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateStartedDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateRevert = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6002)
)
nimbleUpdateRevert.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateRevert.setStatus(
        "current"
    )

nimbleUpdateSuccessDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6003)
)
nimbleUpdateSuccessDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateSuccessDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6004)
)
nimbleUpdateRollback.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateRollback.setStatus(
        "current"
    )

nimbleUpdatePrecheckFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6005)
)
nimbleUpdatePrecheckFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePrecheckFail.setStatus(
        "current"
    )

nimbleUpdateFailMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6007)
)
nimbleUpdateFailMsg.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailMsg.setStatus(
        "current"
    )

nimbleUpdateUnpackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6008)
)
nimbleUpdateUnpackStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnpackStarted.setStatus(
        "current"
    )

nimbleUpdateUnpackDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6009)
)
nimbleUpdateUnpackDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnpackDone.setStatus(
        "current"
    )

nimbleUpdateSwitchRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6010)
)
nimbleUpdateSwitchRoot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateSwitchRoot.setStatus(
        "current"
    )

nimbleUpdateDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6011)
)
nimbleUpdateDownloadFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateDownloadFailed.setStatus(
        "current"
    )

nimbleUpdateFailTmpFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6012)
)
nimbleUpdateFailTmpFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailTmpFsFull.setStatus(
        "current"
    )

nimbleUpdateFailScratchFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6013)
)
nimbleUpdateFailScratchFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailScratchFsFull.setStatus(
        "current"
    )

nimbleUpdateFailVarFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6014)
)
nimbleUpdateFailVarFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailVarFsFull.setStatus(
        "current"
    )

nimbleUpdateFailConfigFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6015)
)
nimbleUpdateFailConfigFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailConfigFsFull.setStatus(
        "current"
    )

nimbleUpdateFailUsbFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6016)
)
nimbleUpdateFailUsbFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailUsbFsFull.setStatus(
        "current"
    )

nimbleUpdatePkgNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6017)
)
nimbleUpdatePkgNotFound.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgNotFound.setStatus(
        "current"
    )

nimbleUpdatePkgWrongSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6018)
)
nimbleUpdatePkgWrongSig.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgWrongSig.setStatus(
        "current"
    )

nimbleUpdatePkgWrongCksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6019)
)
nimbleUpdatePkgWrongCksum.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgWrongCksum.setStatus(
        "current"
    )

nimbleUpdateNetDegradeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6020)
)
nimbleUpdateNetDegradeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateNetDegradeDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateDisallowSoloDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6021)
)
nimbleUpdateDisallowSoloDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateDisallowSoloDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateDisallowSolo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6022)
)
nimbleUpdateDisallowSolo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateDisallowSolo.setStatus(
        "current"
    )

nimbleUpdateNetDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6023)
)
nimbleUpdateNetDegrade.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateNetDegrade.setStatus(
        "current"
    )

nimbleUpdateRaidDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6024)
)
nimbleUpdateRaidDegrade.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateRaidDegrade.setStatus(
        "current"
    )

nimbleUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6025)
)
nimbleUpdateStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateStarted.setStatus(
        "current"
    )

nimbleUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6026)
)
nimbleUpdateSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateSuccess.setStatus(
        "current"
    )

nimbleUpdatePkgSignatureCheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6027)
)
nimbleUpdatePkgSignatureCheckFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgSignatureCheckFailure.setStatus(
        "current"
    )

nimbleUpdatePkgMalformed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6028)
)
nimbleUpdatePkgMalformed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgMalformed.setStatus(
        "current"
    )

nimbleDownloadDnsFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6401)
)
nimbleDownloadDnsFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDownloadDnsFail.setStatus(
        "current"
    )

nimbleAutoDownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6402)
)
nimbleAutoDownloadFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAutoDownloadFail.setStatus(
        "current"
    )

nimbleAutoDownloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6403)
)
nimbleAutoDownloadSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAutoDownloadSuccess.setStatus(
        "current"
    )

nimbleUpdateArrayUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6501)
)
nimbleUpdateArrayUnreachable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateArrayUnreachable.setStatus(
        "current"
    )

nimbleUpdateArrayFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6502)
)
nimbleUpdateArrayFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateArrayFailed.setStatus(
        "current"
    )

nimbleUpdateArrayTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6503)
)
nimbleUpdateArrayTimedOut.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateArrayTimedOut.setStatus(
        "current"
    )

nimbleUpdateIqnConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6504)
)
nimbleUpdateIqnConflict.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateIqnConflict.setStatus(
        "current"
    )

nimbleUpdateNwtVersionOutdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6505)
)
nimbleUpdateNwtVersionOutdated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateNwtVersionOutdated.setStatus(
        "current"
    )

nimbleArrayUnreachableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10010)
)
nimbleArrayUnreachableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUnreachableDeprecated.setStatus(
        "obsolete"
    )

nimbleArrayReachableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10011)
)
nimbleArrayReachableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayReachableDeprecated.setStatus(
        "obsolete"
    )

nimbleArrayUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10012)
)
nimbleArrayUnreachable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUnreachable.setStatus(
        "current"
    )

nimbleArrayReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10013)
)
nimbleArrayReachable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayReachable.setStatus(
        "current"
    )

nimbleUserClearedSysCacheDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10101)
)
nimbleUserClearedSysCacheDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserClearedSysCacheDeprecated.setStatus(
        "obsolete"
    )

nimbleHostTypeMisconfiguredDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10102)
)
nimbleHostTypeMisconfiguredDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHostTypeMisconfiguredDeprecated.setStatus(
        "obsolete"
    )

nimbleHostTypeMisconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10103)
)
nimbleHostTypeMisconfigured.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHostTypeMisconfigured.setStatus(
        "current"
    )

nimbleVolSpcCurWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10200)
)
nimbleVolSpcCurWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurWarningUp.setStatus(
        "current"
    )

nimbleVolSpcCurWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10201)
)
nimbleVolSpcCurWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurWarningDown.setStatus(
        "current"
    )

nimbleVolSpcCurQuotaUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10202)
)
nimbleVolSpcCurQuotaUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurQuotaUpDeprecated.setStatus(
        "obsolete"
    )

nimbleVolSpcCurQuotaDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10203)
)
nimbleVolSpcCurQuotaDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurQuotaDownDeprecated.setStatus(
        "obsolete"
    )

nimbleVolSpcSnapWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10204)
)
nimbleVolSpcSnapWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapWarningUp.setStatus(
        "current"
    )

nimbleVolSpcSnapWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10205)
)
nimbleVolSpcSnapWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapWarningDown.setStatus(
        "current"
    )

nimbleVolSpcSnapQuotaUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10206)
)
nimbleVolSpcSnapQuotaUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapQuotaUp.setStatus(
        "current"
    )

nimbleVolSpcSnapQuotaDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10207)
)
nimbleVolSpcSnapQuotaDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapQuotaDown.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10208)
)
nimbleGmVolSpcCurCritUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurCritDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10209)
)
nimbleGmVolSpcCurCritDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSnapSpcCurCritUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10210)
)
nimbleGmSnapSpcCurCritUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSnapSpcCurCritDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10211)
)
nimbleGmSnapSpcCurCritDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurQuotaOfflineDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10212)
)
nimbleGmVolSpcCurQuotaOfflineDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaOfflineDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurQuotaSetDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10213)
)
nimbleGmVolSpcCurQuotaSetDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaSetDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcSnapQuotaOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10214)
)
nimbleGmVolSpcSnapQuotaOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaOffline.setStatus(
        "current"
    )

nimbleGmVolSpcSnapQuotaSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10215)
)
nimbleGmVolSpcSnapQuotaSet.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaSet.setStatus(
        "current"
    )

nimbleGmVolSpcCurReserveOfflineDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10216)
)
nimbleGmVolSpcCurReserveOfflineDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurReserveOfflineDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurReserveSetDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10217)
)
nimbleGmVolSpcCurReserveSetDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurReserveSetDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcSnapReserveOfflineDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10218)
)
nimbleGmVolSpcSnapReserveOfflineDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapReserveOfflineDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcSnapReserveSetDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10219)
)
nimbleGmVolSpcSnapReserveSetDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapReserveSetDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10220)
)
nimbleGmVolSpcCurWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurWarningUp.setStatus(
        "current"
    )

nimbleGmVolSpcCurWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10221)
)
nimbleGmVolSpcCurWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurWarningDown.setStatus(
        "current"
    )

nimbleGmVolSpcCurQuotaUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10222)
)
nimbleGmVolSpcCurQuotaUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurQuotaDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10223)
)
nimbleGmVolSpcCurQuotaDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcSnapWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10224)
)
nimbleGmVolSpcSnapWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapWarningUp.setStatus(
        "current"
    )

nimbleGmVolSpcSnapWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10225)
)
nimbleGmVolSpcSnapWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapWarningDown.setStatus(
        "current"
    )

nimbleGmVolSpcSnapQuotaUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10226)
)
nimbleGmVolSpcSnapQuotaUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcSnapQuotaDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10227)
)
nimbleGmVolSpcSnapQuotaDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaDownDeprecated.setStatus(
        "obsolete"
    )

nimbleVolAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10228)
)
nimbleVolAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolAttrSyncDelay.setStatus(
        "current"
    )

nimbleGmPoolArrAssgnDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10229)
)
nimbleGmPoolArrAssgnDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrAssgnDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolArrUnassgnDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10230)
)
nimbleGmPoolArrUnassgnDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgnDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurCritUpUnlimDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10231)
)
nimbleGmVolSpcCurCritUpUnlimDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUpUnlimDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSnapSpcCurCritUpUnlimDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10232)
)
nimbleGmSnapSpcCurCritUpUnlimDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritUpUnlimDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcReserveUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10233)
)
nimbleGmVolSpcReserveUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcReserveUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcReserveDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10234)
)
nimbleGmVolSpcReserveDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcReserveDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSnapSpcReserveUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10235)
)
nimbleGmSnapSpcReserveUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcReserveUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSnapSpcReserveDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10236)
)
nimbleGmSnapSpcReserveDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcReserveDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolMrgDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10240)
)
nimbleGmPoolMrgDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolMrgDeprecated.setStatus(
        "obsolete"
    )

nimbleVolAttrSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10241)
)
nimbleVolAttrSyncSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolAttrSyncSuccess.setStatus(
        "current"
    )

nimbleSnapAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10242)
)
nimbleSnapAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSnapAttrSyncDelay.setStatus(
        "current"
    )

nimbleSnapAttrSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10243)
)
nimbleSnapAttrSyncSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSnapAttrSyncSuccess.setStatus(
        "current"
    )

nimbleGroupAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10244)
)
nimbleGroupAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGroupAttrSyncDelay.setStatus(
        "current"
    )

nimbleGroupAttrSyncComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10245)
)
nimbleGroupAttrSyncComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGroupAttrSyncComplete.setStatus(
        "current"
    )

nimbleGlCtrlrAttrSyncDelayDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10246)
)
nimbleGlCtrlrAttrSyncDelayDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncDelayDeprecated.setStatus(
        "obsolete"
    )

nimbleGlCtrlrAttrSyncCompleteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10247)
)
nimbleGlCtrlrAttrSyncCompleteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncCompleteDeprecated.setStatus(
        "obsolete"
    )

nimbleGlCtrlrAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10248)
)
nimbleGlCtrlrAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncDelay.setStatus(
        "current"
    )

nimbleGlCtrlrAttrSyncComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10249)
)
nimbleGlCtrlrAttrSyncComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncComplete.setStatus(
        "current"
    )

nimbleVolMoveComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10250)
)
nimbleVolMoveComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolMoveComplete.setStatus(
        "current"
    )

nimbleVolMoveAbortComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10251)
)
nimbleVolMoveAbortComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolMoveAbortComplete.setStatus(
        "current"
    )

nimbleGmPoolArrUnassgnCompleteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10252)
)
nimbleGmPoolArrUnassgnCompleteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgnCompleteDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolArrUnassgnComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10253)
)
nimbleGmPoolArrUnassgnComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgnComplete.setStatus(
        "current"
    )

nimbleGmPoolArrAssgn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10256)
)
nimbleGmPoolArrAssgn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrAssgn.setStatus(
        "current"
    )

nimbleGmPoolArrUnassgn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10257)
)
nimbleGmPoolArrUnassgn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgn.setStatus(
        "current"
    )

nimbleGmPoolMrg = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10260)
)
nimbleGmPoolMrg.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolMrg.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritUpNonWritableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10261)
)
nimbleGmVolSpcCurCritUpNonWritableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUpNonWritableDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurQuotaNonWritableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10262)
)
nimbleGmVolSpcCurQuotaNonWritableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaNonWritableDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSnapSpcCurCritUpNonWritableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10263)
)
nimbleGmSnapSpcCurCritUpNonWritableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritUpNonWritableDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcSnapQuotaNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10264)
)
nimbleGmVolSpcSnapQuotaNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaNonWritable.setStatus(
        "current"
    )

nimbleGmVolSpcCurReserveNonWritableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10265)
)
nimbleGmVolSpcCurReserveNonWritableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurReserveNonWritableDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcSnapReserveNonWritableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10266)
)
nimbleGmVolSpcSnapReserveNonWritableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapReserveNonWritableDeprecated.setStatus(
        "obsolete"
    )

nimbleEncryptionNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10267)
)
nimbleEncryptionNotActive.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionNotActive.setStatus(
        "current"
    )

nimbleEncryptionMasterKeyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10268)
)
nimbleEncryptionMasterKeyRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionMasterKeyRemoved.setStatus(
        "current"
    )

nimbleEncryptionModeSecured = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10269)
)
nimbleEncryptionModeSecured.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionModeSecured.setStatus(
        "current"
    )

nimbleEncryptionModeAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10270)
)
nimbleEncryptionModeAvailable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionModeAvailable.setStatus(
        "current"
    )

nimbleEncryptionMasterKeyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10271)
)
nimbleEncryptionMasterKeyCreated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionMasterKeyCreated.setStatus(
        "current"
    )

nimbleEncryptionPassphraseModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10272)
)
nimbleEncryptionPassphraseModified.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionPassphraseModified.setStatus(
        "current"
    )

nimbleEncryptionCipherModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10273)
)
nimbleEncryptionCipherModified.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionCipherModified.setStatus(
        "current"
    )

nimbleEncryptionScopeModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10274)
)
nimbleEncryptionScopeModified.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionScopeModified.setStatus(
        "current"
    )

nimbleEncryptionActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10275)
)
nimbleEncryptionActive.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionActive.setStatus(
        "current"
    )

nimbleEncryptionSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10276)
)
nimbleEncryptionSlow.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionSlow.setStatus(
        "current"
    )

nimbleEncryptionActiveMasterKeyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10277)
)
nimbleEncryptionActiveMasterKeyRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionActiveMasterKeyRemoved.setStatus(
        "current"
    )

nimbleGmVolSerialCollisionOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10278)
)
nimbleGmVolSerialCollisionOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSerialCollisionOffline.setStatus(
        "current"
    )

nimbleGmSnapSerialCollisionOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10279)
)
nimbleGmSnapSerialCollisionOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSerialCollisionOffline.setStatus(
        "current"
    )

nimbleIgrpSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10280)
)
nimbleIgrpSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIgrpSyncDelay.setStatus(
        "current"
    )

nimbleIgrpSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10281)
)
nimbleIgrpSyncSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIgrpSyncSuccess.setStatus(
        "current"
    )

nimbleGmPinCacheInsufficientDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10282)
)
nimbleGmPinCacheInsufficientDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPinCacheInsufficientDeprecated.setStatus(
        "obsolete"
    )

nimbleFolderAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10283)
)
nimbleFolderAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFolderAttrSyncDelay.setStatus(
        "current"
    )

nimbleFolderAttrSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10284)
)
nimbleFolderAttrSyncSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFolderAttrSyncSuccess.setStatus(
        "current"
    )

nimbleGmVolFolderLimitOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10285)
)
nimbleGmVolFolderLimitOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolFolderLimitOffline.setStatus(
        "current"
    )

nimbleGmVolFolderLimitNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10286)
)
nimbleGmVolFolderLimitNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolFolderLimitNonWritable.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceUtilizationCritDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10287)
)
nimbleGmFolderUsedSpaceUtilizationCritDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationCritDeprecated.setStatus(
        "obsolete"
    )

nimbleGmFolderUsedSpaceUtilizationHighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10288)
)
nimbleGmFolderUsedSpaceUtilizationHighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationHighDeprecated.setStatus(
        "obsolete"
    )

nimbleGmFolderUsedSpaceUtilizationInfoDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10289)
)
nimbleGmFolderUsedSpaceUtilizationInfoDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationInfoDeprecated.setStatus(
        "obsolete"
    )

nimbleGmFolderUsedSpaceUtilizationOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10290)
)
nimbleGmFolderUsedSpaceUtilizationOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationOkDeprecated.setStatus(
        "obsolete"
    )

nimbleGmFolderUsedSpaceReplicationStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10291)
)
nimbleGmFolderUsedSpaceReplicationStopped.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceReplicationStopped.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceReplicationStoppedUpstreamDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10292)
)
nimbleGmFolderUsedSpaceReplicationStoppedUpstreamDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceReplicationStoppedUpstreamDeprecated.setStatus(
        "obsolete"
    )

nimbleGmFolderUsedSpaceReplicationOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10293)
)
nimbleGmFolderUsedSpaceReplicationOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceReplicationOkDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurProvisionOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10294)
)
nimbleGmVolSpcCurProvisionOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurProvisionOffline.setStatus(
        "current"
    )

nimbleGmVolSpcCurProvisionNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10295)
)
nimbleGmVolSpcCurProvisionNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurProvisionNonWritable.setStatus(
        "current"
    )

nimbleVolReserveConversionToProvisioningLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10296)
)
nimbleVolReserveConversionToProvisioningLevel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolReserveConversionToProvisioningLevel.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10297)
)
nimbleGmFolderUsedSpaceUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationCrit.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10298)
)
nimbleGmFolderUsedSpaceUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationHigh.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceUtilizationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10299)
)
nimbleGmFolderUsedSpaceUtilizationInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationInfo.setStatus(
        "current"
    )

nimbleSchedSnapSucceededDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10300)
)
nimbleSchedSnapSucceededDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceededDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10301)
)
nimbleSchedSnapFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailed.setStatus(
        "current"
    )

nimbleSchedSnapSkippedExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10302)
)
nimbleSchedSnapSkippedExists.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSkippedExists.setStatus(
        "current"
    )

nimbleSchedSnapSkippedHandover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10303)
)
nimbleSchedSnapSkippedHandover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSkippedHandover.setStatus(
        "current"
    )

nimbleSchedSnapSucceededLagInfoDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10304)
)
nimbleSchedSnapSucceededLagInfoDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceededLagInfoDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareCredentialDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10305)
)
nimbleSchedSnapFailedVmwareCredentialDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareCredentialDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10306)
)
nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10307)
)
nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionResetDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10308)
)
nimbleSchedSnapFailedVmwareConnectionResetDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionResetDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10309)
)
nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionSocketDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10310)
)
nimbleSchedSnapFailedVmwareConnectionSocketDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionSocketDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10311)
)
nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareDisabledDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10312)
)
nimbleSchedSnapFailedVmwareDisabledDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDisabledDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareObjectnfDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10313)
)
nimbleSchedSnapFailedVmwareObjectnfDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareObjectnfDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwarePermissionDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10314)
)
nimbleSchedSnapFailedVmwarePermissionDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwarePermissionDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareUkhostDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10315)
)
nimbleSchedSnapFailedVmwareUkhostDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUkhostDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareEncodingPlainDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10316)
)
nimbleSchedSnapFailedVmwareEncodingPlainDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareEncodingPlainDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareNullDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10317)
)
nimbleSchedSnapFailedVmwareNullDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareNullDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareDcnotfoundDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10318)
)
nimbleSchedSnapFailedVmwareDcnotfoundDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDcnotfoundDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareVolsnemptyDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10319)
)
nimbleSchedSnapFailedVmwareVolsnemptyDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareVolsnemptyDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareUnknownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10320)
)
nimbleSchedSnapFailedVmwareUnknownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareBsizeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10321)
)
nimbleSchedSnapFailedVmwareBsizeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareBsizeDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10322)
)
nimbleSchedSnapSucceeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceeded.setStatus(
        "current"
    )

nimbleSchedSnapSucceededLagInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10323)
)
nimbleSchedSnapSucceededLagInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceededLagInfo.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10324)
)
nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareTimeoutDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10325)
)
nimbleSchedSnapFailedVmwareTimeoutDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareTimeoutDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10326)
)
nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10327)
)
nimbleSchedSnapFallback.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFallback.setStatus(
        "current"
    )

nimbleSchedSnapFailedUnknownReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10328)
)
nimbleSchedSnapFailedUnknownReason.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedUnknownReason.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwarePermissionPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10340)
)
nimbleSchedSnapFailedVmwarePermissionPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwarePermissionPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareObjectnfPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10341)
)
nimbleSchedSnapFailedVmwareObjectnfPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareObjectnfPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareEncodingPlainPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10342)
)
nimbleSchedSnapFailedVmwareEncodingPlainPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareEncodingPlainPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareNullPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10343)
)
nimbleSchedSnapFailedVmwareNullPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareNullPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareDcnotfoundPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10344)
)
nimbleSchedSnapFailedVmwareDcnotfoundPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDcnotfoundPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareVolsnemptyPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10345)
)
nimbleSchedSnapFailedVmwareVolsnemptyPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareVolsnemptyPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10346)
)
nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareBsizePerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10347)
)
nimbleSchedSnapFailedVmwareBsizePerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareBsizePerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareDisabledPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10348)
)
nimbleSchedSnapFailedVmwareDisabledPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDisabledPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareTimeoutPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10349)
)
nimbleSchedSnapFailedVmwareTimeoutPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareTimeoutPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10350)
)
nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10351)
)
nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareInvalidVcenter = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10352)
)
nimbleSchedSnapFailedVmwareInvalidVcenter.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareInvalidVcenter.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10353)
)
nimbleSchedSnapFailedVmwareBusy.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareBusy.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10354)
)
nimbleSchedSnapFailedVssIncompatible.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssIncompatible.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareCredentialNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10355)
)
nimbleSchedSnapFailedVmwareCredentialNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareCredentialNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionTimeoutNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10356)
)
nimbleSchedSnapFailedVmwareConnectionTimeoutNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionTimeoutNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionRefusedNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10357)
)
nimbleSchedSnapFailedVmwareConnectionRefusedNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionRefusedNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionResetNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10358)
)
nimbleSchedSnapFailedVmwareConnectionResetNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionResetNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionNorouteNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10359)
)
nimbleSchedSnapFailedVmwareConnectionNorouteNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionNorouteNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionSocketNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10360)
)
nimbleSchedSnapFailedVmwareConnectionSocketNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionSocketNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionUnreachableNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10361)
)
nimbleSchedSnapFailedVmwareConnectionUnreachableNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionUnreachableNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUkhostNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10362)
)
nimbleSchedSnapFailedVmwareUkhostNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUkhostNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionUnknownNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10363)
)
nimbleSchedSnapFailedVmwareConnectionUnknownNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionUnknownNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareTimeoutNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10364)
)
nimbleSchedSnapFailedVmwareTimeoutNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareTimeoutNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUnknownNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10365)
)
nimbleSchedSnapFailedVmwareUnknownNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUnknownPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10366)
)
nimbleSchedSnapFailedVmwareUnknownPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareQuiescingVmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10367)
)
nimbleSchedSnapFailedVmwareQuiescingVmFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareQuiescingVmFailed.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareLeftoverSnapshot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10368)
)
nimbleSchedSnapFailedVmwareLeftoverSnapshot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareLeftoverSnapshot.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericConnectionTimeoutNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10370)
)
nimbleSchedSnapFailedGenericConnectionTimeoutNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericConnectionTimeoutNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericConnectionNorouteNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10371)
)
nimbleSchedSnapFailedGenericConnectionNorouteNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericConnectionNorouteNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericConnectionRefusedNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10372)
)
nimbleSchedSnapFailedGenericConnectionRefusedNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericConnectionRefusedNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericConnectionSocketNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10373)
)
nimbleSchedSnapFailedGenericConnectionSocketNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericConnectionSocketNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericCredentialNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10374)
)
nimbleSchedSnapFailedGenericCredentialNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericCredentialNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericUkhostNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10375)
)
nimbleSchedSnapFailedGenericUkhostNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericUkhostNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericConnectionUnknownNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10376)
)
nimbleSchedSnapFailedGenericConnectionUnknownNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericConnectionUnknownNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericAgentError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10377)
)
nimbleSchedSnapFailedGenericAgentError.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericAgentError.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericTimeoutNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10378)
)
nimbleSchedSnapFailedGenericTimeoutNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericTimeoutNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10379)
)
nimbleSchedSnapFailedGenericBusy.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericBusy.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssWriterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10380)
)
nimbleSchedSnapFailedVssWriterFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssWriterFailure.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssNonTerminatingWriterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10381)
)
nimbleSchedSnapFailedVssNonTerminatingWriterFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssNonTerminatingWriterFailure.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssVolcollConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10382)
)
nimbleSchedSnapFailedVssVolcollConfigError.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssVolcollConfigError.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssSnapVerificationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10383)
)
nimbleSchedSnapFailedVssSnapVerificationError.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssSnapVerificationError.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssPreviousSnapInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10384)
)
nimbleSchedSnapFailedVssPreviousSnapInProgress.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssPreviousSnapInProgress.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssSnapFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10385)
)
nimbleSchedSnapFailedVssSnapFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssSnapFailure.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssBadCookie = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10386)
)
nimbleSchedSnapFailedVssBadCookie.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssBadCookie.setStatus(
        "current"
    )

nimbleSchedSnapFailedGenericUnknownNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10387)
)
nimbleSchedSnapFailedGenericUnknownNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedGenericUnknownNw.setStatus(
        "current"
    )

nimbleVssVolcollConfigWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10388)
)
nimbleVssVolcollConfigWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVssVolcollConfigWarn.setStatus(
        "current"
    )

nimbleApplicationServerLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10396)
)
nimbleApplicationServerLoginFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleApplicationServerLoginFailed.setStatus(
        "current"
    )

nimbleApplicationServerLoginSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10397)
)
nimbleApplicationServerLoginSucceeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleApplicationServerLoginSucceeded.setStatus(
        "current"
    )

nimbleVvolManagementConnectionDisrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10398)
)
nimbleVvolManagementConnectionDisrupted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVvolManagementConnectionDisrupted.setStatus(
        "current"
    )

nimbleVvolManagementConnectionReestablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10399)
)
nimbleVvolManagementConnectionReestablished.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVvolManagementConnectionReestablished.setStatus(
        "current"
    )

nimbleGmSpaceReserveWarnUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10401)
)
nimbleGmSpaceReserveWarnUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveWarnUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSpaceReserveWarnDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10402)
)
nimbleGmSpaceReserveWarnDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveWarnDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSpaceReserveCritUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10403)
)
nimbleGmSpaceReserveCritUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveCritUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSpaceReserveCritDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10404)
)
nimbleGmSpaceReserveCritDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveCritDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmSpaceUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10405)
)
nimbleGmSpaceUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationOk.setStatus(
        "current"
    )

nimbleGmSpaceUtilizationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10406)
)
nimbleGmSpaceUtilizationInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationInfo.setStatus(
        "current"
    )

nimbleGmSpaceUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10407)
)
nimbleGmSpaceUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationHigh.setStatus(
        "current"
    )

nimbleGmSpaceUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10408)
)
nimbleGmSpaceUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationCrit.setStatus(
        "current"
    )

nimbleGmPoolSpaceReserveWarnUpDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10409)
)
nimbleGmPoolSpaceReserveWarnUpDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnUpDeprecated2.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveWarnDownDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10410)
)
nimbleGmPoolSpaceReserveWarnDownDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnDownDeprecated2.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveCritUpDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10411)
)
nimbleGmPoolSpaceReserveCritUpDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritUpDeprecated2.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveCritDownDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10412)
)
nimbleGmPoolSpaceReserveCritDownDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritDownDeprecated2.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10413)
)
nimbleGmPoolSpaceUtilizationOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationOkDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationInfoDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10414)
)
nimbleGmPoolSpaceUtilizationInfoDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationInfoDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationHighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10415)
)
nimbleGmPoolSpaceUtilizationHighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationHighDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationCritDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10416)
)
nimbleGmPoolSpaceUtilizationCritDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationCritDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveWarnUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10417)
)
nimbleGmPoolSpaceReserveWarnUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveWarnDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10418)
)
nimbleGmPoolSpaceReserveWarnDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveCritUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10419)
)
nimbleGmPoolSpaceReserveCritUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveCritDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10420)
)
nimbleGmPoolSpaceReserveCritDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10421)
)
nimbleGmPoolSpaceUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationOk.setStatus(
        "current"
    )

nimbleGmPoolSpaceUtilizationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10422)
)
nimbleGmPoolSpaceUtilizationInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationInfo.setStatus(
        "current"
    )

nimbleGmPoolSpaceUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10423)
)
nimbleGmPoolSpaceUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationHigh.setStatus(
        "current"
    )

nimbleGmPoolSpaceUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10424)
)
nimbleGmPoolSpaceUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationCrit.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10427)
)
nimbleGmVolSpcCurCritUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUp.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10428)
)
nimbleGmVolSpcCurCritDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritDown.setStatus(
        "current"
    )

nimbleGmVolSpcCurLimitOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10429)
)
nimbleGmVolSpcCurLimitOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurLimitOffline.setStatus(
        "current"
    )

nimbleGmVolSpcCurLimitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10430)
)
nimbleGmVolSpcCurLimitUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurLimitUp.setStatus(
        "current"
    )

nimbleGmVolSpcCurLimitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10431)
)
nimbleGmVolSpcCurLimitDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurLimitDown.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritUpUnlim = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10432)
)
nimbleGmVolSpcCurCritUpUnlim.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUpUnlim.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritUpNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10433)
)
nimbleGmVolSpcCurCritUpNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUpNonWritable.setStatus(
        "current"
    )

nimbleGmVolSpcCurLimitNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10434)
)
nimbleGmVolSpcCurLimitNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurLimitNonWritable.setStatus(
        "current"
    )

nimbleGmPoolSpaceProvisionWarnUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10435)
)
nimbleGmPoolSpaceProvisionWarnUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceProvisionWarnUp.setStatus(
        "current"
    )

nimbleGmPoolSpaceProvisionWarnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10436)
)
nimbleGmPoolSpaceProvisionWarnDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceProvisionWarnDown.setStatus(
        "current"
    )

nimbleGmPoolSpaceProvisionCritUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10437)
)
nimbleGmPoolSpaceProvisionCritUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceProvisionCritUp.setStatus(
        "current"
    )

nimbleGmPoolSpaceProvisionCritDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10438)
)
nimbleGmPoolSpaceProvisionCritDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceProvisionCritDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceProvisionCritDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10439)
)
nimbleGmPoolSpaceProvisionCritDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceProvisionCritDown.setStatus(
        "current"
    )

nimbleLimitMaxOverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10500)
)
nimbleLimitMaxOverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxOverDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitMaxUnderDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10501)
)
nimbleLimitMaxUnderDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxUnderDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitWarnOverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10502)
)
nimbleLimitWarnOverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnOverDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitWarnUnderDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10503)
)
nimbleLimitWarnUnderDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnUnderDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitMaxOverWithContextDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10504)
)
nimbleLimitMaxOverWithContextDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxOverWithContextDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitMaxUnderWithContextDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10505)
)
nimbleLimitMaxUnderWithContextDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxUnderWithContextDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitWarnOverWithContextDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10506)
)
nimbleLimitWarnOverWithContextDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnOverWithContextDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitWarnUnderWithContextDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10507)
)
nimbleLimitWarnUnderWithContextDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnUnderWithContextDeprecated.setStatus(
        "obsolete"
    )

nimbleLimitMaxOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10510)
)
nimbleLimitMaxOver.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxOver.setStatus(
        "current"
    )

nimbleLimitMaxUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10511)
)
nimbleLimitMaxUnder.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxUnder.setStatus(
        "current"
    )

nimbleLimitWarnOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10512)
)
nimbleLimitWarnOver.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnOver.setStatus(
        "current"
    )

nimbleLimitWarnUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10513)
)
nimbleLimitWarnUnder.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnUnder.setStatus(
        "current"
    )

nimbleLimitMaxOverWithContext = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10514)
)
nimbleLimitMaxOverWithContext.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxOverWithContext.setStatus(
        "current"
    )

nimbleLimitMaxUnderWithContext = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10515)
)
nimbleLimitMaxUnderWithContext.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxUnderWithContext.setStatus(
        "current"
    )

nimbleLimitWarnOverWithContext = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10516)
)
nimbleLimitWarnOverWithContext.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnOverWithContext.setStatus(
        "current"
    )

nimbleLimitWarnUnderWithContext = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10517)
)
nimbleLimitWarnUnderWithContext.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnUnderWithContext.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10600)
)
nimbleGmFolderUsedSpaceUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceUtilizationOk.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceReplicationStoppedUpstream = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10601)
)
nimbleGmFolderUsedSpaceReplicationStoppedUpstream.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceReplicationStoppedUpstream.setStatus(
        "current"
    )

nimbleGmFolderUsedSpaceReplicationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10602)
)
nimbleGmFolderUsedSpaceReplicationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmFolderUsedSpaceReplicationOk.setStatus(
        "current"
    )

nimbleReplSnapcollSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11000)
)
nimbleReplSnapcollSucceeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapcollSucceeded.setStatus(
        "current"
    )

nimbleReplSnapcollDelayedInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11001)
)
nimbleReplSnapcollDelayedInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapcollDelayedInfo.setStatus(
        "current"
    )

nimbleReplSnapcollDelayedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11002)
)
nimbleReplSnapcollDelayedWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapcollDelayedWarn.setStatus(
        "current"
    )

nimbleReplPartnerSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11003)
)
nimbleReplPartnerSyncFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerSyncFail.setStatus(
        "current"
    )

nimbleReplBranchPinned = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11004)
)
nimbleReplBranchPinned.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchPinned.setStatus(
        "current"
    )

nimbleReplHandoverCompletedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11005)
)
nimbleReplHandoverCompletedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverCompletedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplMultiArrayGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11006)
)
nimbleReplMultiArrayGroup.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplMultiArrayGroup.setStatus(
        "current"
    )

nimbleReplPartnerMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11007)
)
nimbleReplPartnerMisconfiguration.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerMisconfiguration.setStatus(
        "current"
    )

nimbleReplSnapshotCorrectedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11008)
)
nimbleReplSnapshotCorrectedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrectedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplCbrRequestedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11009)
)
nimbleReplCbrRequestedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrRequestedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplCbrNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11010)
)
nimbleReplCbrNeeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrNeeded.setStatus(
        "current"
    )

nimbleReplSnapshotCorrectedDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11011)
)
nimbleReplSnapshotCorrectedDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrectedDeprecated2.setStatus(
        "obsolete"
    )

nimbleReplCbrRequestedDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11012)
)
nimbleReplCbrRequestedDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrRequestedDeprecated2.setStatus(
        "obsolete"
    )

nimbleReplPartnerAuthFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11013)
)
nimbleReplPartnerAuthFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerAuthFailDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSnapshotCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11014)
)
nimbleReplSnapshotCorrected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrected.setStatus(
        "current"
    )

nimbleReplCbrRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11015)
)
nimbleReplCbrRequested.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrRequested.setStatus(
        "current"
    )

nimbleReplPartnerAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11016)
)
nimbleReplPartnerAuthFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerAuthFail.setStatus(
        "current"
    )

nimbleReplVolumeResynchronize = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11017)
)
nimbleReplVolumeResynchronize.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolumeResynchronize.setStatus(
        "current"
    )

nimbleReplHandoverAbortedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11018)
)
nimbleReplHandoverAbortedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverAbortedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplHandoverCompletedOfflineDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11019)
)
nimbleReplHandoverCompletedOfflineDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverCompletedOfflineDeprecated.setStatus(
        "obsolete"
    )

nimbleReplHandoverAbortedOfflineDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11020)
)
nimbleReplHandoverAbortedOfflineDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverAbortedOfflineDeprecated.setStatus(
        "obsolete"
    )

nimbleReplProtpolDeletionFailedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11021)
)
nimbleReplProtpolDeletionFailedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplProtpolDeletionFailedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplBranchpointTrimmedNocommonDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11022)
)
nimbleReplBranchpointTrimmedNocommonDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchpointTrimmedNocommonDeprecated.setStatus(
        "obsolete"
    )

nimbleReplBranchpointTrimmedCommonDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11023)
)
nimbleReplBranchpointTrimmedCommonDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchpointTrimmedCommonDeprecated.setStatus(
        "obsolete"
    )

nimbleReplVolumeAutoResynchronize = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11024)
)
nimbleReplVolumeAutoResynchronize.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolumeAutoResynchronize.setStatus(
        "current"
    )

nimbleReplVolumeCorrectedNoErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11025)
)
nimbleReplVolumeCorrectedNoErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolumeCorrectedNoErr.setStatus(
        "current"
    )

nimbleReplPartnerUnsupportedVssAppId = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11026)
)
nimbleReplPartnerUnsupportedVssAppId.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerUnsupportedVssAppId.setStatus(
        "current"
    )

nimbleReplBranchInconsistentDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11027)
)
nimbleReplBranchInconsistentDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchInconsistentDeprecated.setStatus(
        "obsolete"
    )

nimbleReplPoolPartnerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11028)
)
nimbleReplPoolPartnerCreated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPoolPartnerCreated.setStatus(
        "current"
    )

nimbleReplPartnerOosyncDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11031)
)
nimbleReplPartnerOosyncDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerOosyncDeprecated.setStatus(
        "obsolete"
    )

nimbleReplPartnerInsyncDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11032)
)
nimbleReplPartnerInsyncDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerInsyncDeprecated.setStatus(
        "obsolete"
    )

nimbleReplVolcolOosyncDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11033)
)
nimbleReplVolcolOosyncDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolcolOosyncDeprecated.setStatus(
        "obsolete"
    )

nimbleReplVolcolInsyncDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11034)
)
nimbleReplVolcolInsyncDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolcolInsyncDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeHasAcls = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11035)
)
nimbleReplSrepVolumeHasAcls.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeHasAcls.setStatus(
        "current"
    )

nimbleReplSrepVolumeAclsRemovedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11036)
)
nimbleReplSrepVolumeAclsRemovedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeAclsRemovedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepProtpolMgmtOosyncDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11037)
)
nimbleReplSrepProtpolMgmtOosyncDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepProtpolMgmtOosyncDeprecated.setStatus(
        "obsolete"
    )

nimbleReplPoolPartnerCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11038)
)
nimbleReplPoolPartnerCreationFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPoolPartnerCreationFailed.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11039)
)
nimbleReplSrepVolumeDnstrOnline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrOnline.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrOfflineDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11040)
)
nimbleReplSrepVolumeDnstrOfflineDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrOfflineDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrOnlineRenamedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11041)
)
nimbleReplSrepVolumeDnstrOnlineRenamedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrOnlineRenamedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11042)
)
nimbleReplSrepVolumeDnstrSizeMismatch.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrSizeMismatch.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrResized = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11043)
)
nimbleReplSrepVolumeDnstrResized.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrResized.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrSizeMismatchDeletedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11044)
)
nimbleReplSrepVolumeDnstrSizeMismatchDeletedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrSizeMismatchDeletedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrSizeMismatchRenamedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11045)
)
nimbleReplSrepVolumeDnstrSizeMismatchRenamedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrSizeMismatchRenamedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrAgentTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11046)
)
nimbleReplSrepVolumeDnstrAgentTypeMismatch.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrAgentTypeMismatch.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrAgentTypeUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11047)
)
nimbleReplSrepVolumeDnstrAgentTypeUpdated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrAgentTypeUpdated.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrAgentTypeMismatchDeletedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11048)
)
nimbleReplSrepVolumeDnstrAgentTypeMismatchDeletedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrAgentTypeMismatchDeletedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11049)
)
nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11050)
)
nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrIscsiTargetScopeUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11051)
)
nimbleReplSrepVolumeDnstrIscsiTargetScopeUpdated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrIscsiTargetScopeUpdated.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeletedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11052)
)
nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeletedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeletedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11053)
)
nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrNoCommonSnap = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11054)
)
nimbleReplSrepVolumeDnstrNoCommonSnap.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrNoCommonSnap.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrNoCommonSnapDeletedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11055)
)
nimbleReplSrepVolumeDnstrNoCommonSnapDeletedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrNoCommonSnapDeletedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepVolumeDnstrNoCommonSnapRenamedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11056)
)
nimbleReplSrepVolumeDnstrNoCommonSnapRenamedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrNoCommonSnapRenamedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepAsoSwitchoverSuccessfulDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11057)
)
nimbleReplSrepAsoSwitchoverSuccessfulDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepAsoSwitchoverSuccessfulDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepAsoSwitchoverBlockedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11058)
)
nimbleReplSrepAsoSwitchoverBlockedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepAsoSwitchoverBlockedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSrepProtpolMgmtOosync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11059)
)
nimbleReplSrepProtpolMgmtOosync.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepProtpolMgmtOosync.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11060)
)
nimbleReplSrepVolumeDnstrOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrOffline.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrOnlineRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11061)
)
nimbleReplSrepVolumeDnstrOnlineRenamed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrOnlineRenamed.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrSizeMismatchDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11062)
)
nimbleReplSrepVolumeDnstrSizeMismatchDeleted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrSizeMismatchDeleted.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrSizeMismatchRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11063)
)
nimbleReplSrepVolumeDnstrSizeMismatchRenamed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrSizeMismatchRenamed.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrAgentTypeMismatchDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11064)
)
nimbleReplSrepVolumeDnstrAgentTypeMismatchDeleted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrAgentTypeMismatchDeleted.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11065)
)
nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamed.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11066)
)
nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalid.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalid.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11067)
)
nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeleted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeleted.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11068)
)
nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamed.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrNoCommonSnapDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11069)
)
nimbleReplSrepVolumeDnstrNoCommonSnapDeleted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrNoCommonSnapDeleted.setStatus(
        "current"
    )

nimbleReplSrepVolumeDnstrNoCommonSnapRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11070)
)
nimbleReplSrepVolumeDnstrNoCommonSnapRenamed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeDnstrNoCommonSnapRenamed.setStatus(
        "current"
    )

nimbleReplSrepAsoSwitchoverBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11071)
)
nimbleReplSrepAsoSwitchoverBlocked.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepAsoSwitchoverBlocked.setStatus(
        "current"
    )

nimbleReplSrepVolumeAclsRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11072)
)
nimbleReplSrepVolumeAclsRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepVolumeAclsRemoved.setStatus(
        "current"
    )

nimbleReplPartnerOosync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11073)
)
nimbleReplPartnerOosync.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerOosync.setStatus(
        "current"
    )

nimbleReplPartnerInsync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11074)
)
nimbleReplPartnerInsync.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerInsync.setStatus(
        "current"
    )

nimbleReplVolcolOosync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11075)
)
nimbleReplVolcolOosync.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolcolOosync.setStatus(
        "current"
    )

nimbleReplVolcolInsync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11076)
)
nimbleReplVolcolInsync.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolcolInsync.setStatus(
        "current"
    )

nimbleReplSrepAsoSwitchoverSuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11077)
)
nimbleReplSrepAsoSwitchoverSuccessful.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepAsoSwitchoverSuccessful.setStatus(
        "current"
    )

nimbleReplSrepProtpolRecmFreqSchedMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11080)
)
nimbleReplSrepProtpolRecmFreqSchedMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepProtpolRecmFreqSchedMissing.setStatus(
        "current"
    )

nimbleReplSrepProtpolRecmFreqSchedImplemented = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11081)
)
nimbleReplSrepProtpolRecmFreqSchedImplemented.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepProtpolRecmFreqSchedImplemented.setStatus(
        "current"
    )

nimbleReplSrepProtpolRecmFreqNoReplVols = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11082)
)
nimbleReplSrepProtpolRecmFreqNoReplVols.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSrepProtpolRecmFreqNoReplVols.setStatus(
        "current"
    )

nimbleReplBranchInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11083)
)
nimbleReplBranchInconsistent.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchInconsistent.setStatus(
        "current"
    )

nimbleReplSnapshotCorrectedFromBranchInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11084)
)
nimbleReplSnapshotCorrectedFromBranchInconsistency.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrectedFromBranchInconsistency.setStatus(
        "current"
    )

nimbleReplSnapshotCorrectedFromBranchInconsistencyNoErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11085)
)
nimbleReplSnapshotCorrectedFromBranchInconsistencyNoErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrectedFromBranchInconsistencyNoErr.setStatus(
        "current"
    )

nimbleReplHandoverCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11200)
)
nimbleReplHandoverCompleted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverCompleted.setStatus(
        "current"
    )

nimbleReplHandoverAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11201)
)
nimbleReplHandoverAborted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverAborted.setStatus(
        "current"
    )

nimbleReplHandoverCompletedOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11202)
)
nimbleReplHandoverCompletedOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverCompletedOffline.setStatus(
        "current"
    )

nimbleReplHandoverAbortedOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11203)
)
nimbleReplHandoverAbortedOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverAbortedOffline.setStatus(
        "current"
    )

nimbleReplProtpolDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11204)
)
nimbleReplProtpolDeletionFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplProtpolDeletionFailed.setStatus(
        "current"
    )

nimbleReplBranchpointTrimmedNocommon = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11205)
)
nimbleReplBranchpointTrimmedNocommon.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchpointTrimmedNocommon.setStatus(
        "current"
    )

nimbleReplBranchpointTrimmedCommon = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11206)
)
nimbleReplBranchpointTrimmedCommon.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchpointTrimmedCommon.setStatus(
        "current"
    )

nimbleOvertempShutdownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12000)
)
nimbleOvertempShutdownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleOvertempShutdownDeprecated.setStatus(
        "obsolete"
    )

nimbleCtrlrOvertempDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12001)
)
nimbleCtrlrOvertempDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrOvertempDeprecated.setStatus(
        "obsolete"
    )

nimbleBackplaneOvertempDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12002)
)
nimbleBackplaneOvertempDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBackplaneOvertempDeprecated.setStatus(
        "obsolete"
    )

nimbleHsFlashSizeUnsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12003)
)
nimbleHsFlashSizeUnsupported.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHsFlashSizeUnsupported.setStatus(
        "current"
    )

nimbleHsFlashSizeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12004)
)
nimbleHsFlashSizeNormal.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHsFlashSizeNormal.setStatus(
        "current"
    )

nimbleIscsiErroneousItorConnsDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12057)
)
nimbleIscsiErroneousItorConnsDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiErroneousItorConnsDeprecated.setStatus(
        "obsolete"
    )

nimbleDiskFailedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12100)
)
nimbleDiskFailedCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFailedCrit.setStatus(
        "current"
    )

nimbleDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12101)
)
nimbleDiskFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFailed.setStatus(
        "current"
    )

nimbleDiskAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12102)
)
nimbleDiskAbsent.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskAbsent.setStatus(
        "current"
    )

nimbleDiskAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12103)
)
nimbleDiskAdded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskAdded.setStatus(
        "current"
    )

nimbleDiskRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12104)
)
nimbleDiskRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskRemoved.setStatus(
        "current"
    )

nimbleSsdFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12105)
)
nimbleSsdFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdFailed.setStatus(
        "current"
    )

nimbleSsdAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12106)
)
nimbleSsdAbsent.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAbsent.setStatus(
        "current"
    )

nimbleSsdAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12107)
)
nimbleSsdAdded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAdded.setStatus(
        "current"
    )

nimbleSsdRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12108)
)
nimbleSsdRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdRemoved.setStatus(
        "current"
    )

nimbleDiskInvalidLabel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12109)
)
nimbleDiskInvalidLabel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskInvalidLabel.setStatus(
        "current"
    )

nimbleSsdInvalidLabel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12110)
)
nimbleSsdInvalidLabel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdInvalidLabel.setStatus(
        "current"
    )

nimbleDiskSizeMismatchDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12111)
)
nimbleDiskSizeMismatchDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskSizeMismatchDeprecated.setStatus(
        "obsolete"
    )

nimbleHddFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12112)
)
nimbleHddFailedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedV2.setStatus(
        "current"
    )

nimbleHddAbsentV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12113)
)
nimbleHddAbsentV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddAbsentV2.setStatus(
        "current"
    )

nimbleHddAddedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12114)
)
nimbleHddAddedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddAddedV2.setStatus(
        "current"
    )

nimbleHddRemovedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12115)
)
nimbleHddRemovedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddRemovedV2.setStatus(
        "current"
    )

nimbleSsdFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12116)
)
nimbleSsdFailedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdFailedV2.setStatus(
        "current"
    )

nimbleSsdAbsentV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12117)
)
nimbleSsdAbsentV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAbsentV2.setStatus(
        "current"
    )

nimbleSsdAddedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12118)
)
nimbleSsdAddedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAddedV2.setStatus(
        "current"
    )

nimbleSsdRemovedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12119)
)
nimbleSsdRemovedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdRemovedV2.setStatus(
        "current"
    )

nimbleSsdLastOne = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12120)
)
nimbleSsdLastOne.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdLastOne.setStatus(
        "current"
    )

nimbleHddFailedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12121)
)
nimbleHddFailedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedV3.setStatus(
        "current"
    )

nimbleHddAddedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12122)
)
nimbleHddAddedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddAddedV3.setStatus(
        "current"
    )

nimbleHddRemovedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12123)
)
nimbleHddRemovedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddRemovedV3.setStatus(
        "current"
    )

nimbleSsdFailedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12124)
)
nimbleSsdFailedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdFailedV3.setStatus(
        "current"
    )

nimbleSsdAddedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12125)
)
nimbleSsdAddedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAddedV3.setStatus(
        "current"
    )

nimbleSsdRemovedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12126)
)
nimbleSsdRemovedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdRemovedV3.setStatus(
        "current"
    )

nimbleDiskSizeMismatchV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12127)
)
nimbleDiskSizeMismatchV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskSizeMismatchV2.setStatus(
        "current"
    )

nimbleSsdSizeMismatchV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12128)
)
nimbleSsdSizeMismatchV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdSizeMismatchV2.setStatus(
        "current"
    )

nimbleHddFailedAfsDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12129)
)
nimbleHddFailedAfsDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedAfsDeprecated.setStatus(
        "obsolete"
    )

nimbleHddFailedAfs = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12130)
)
nimbleHddFailedAfs.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedAfs.setStatus(
        "current"
    )

nimbleSsdNone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12131)
)
nimbleSsdNone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdNone.setStatus(
        "current"
    )

nimbleDiskMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12132)
)
nimbleDiskMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskMissing.setStatus(
        "current"
    )

nimbleDiskDiagRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12133)
)
nimbleDiskDiagRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskDiagRemoved.setStatus(
        "current"
    )

nimbleDfcSsdFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12134)
)
nimbleDfcSsdFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcSsdFailed.setStatus(
        "current"
    )

nimbleDfcSsdAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12135)
)
nimbleDfcSsdAdded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcSsdAdded.setStatus(
        "current"
    )

nimbleDfcSsdRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12136)
)
nimbleDfcSsdRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcSsdRemoved.setStatus(
        "current"
    )

nimbleDfcDiskSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12137)
)
nimbleDfcDiskSizeMismatch.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcDiskSizeMismatch.setStatus(
        "current"
    )

nimbleDfcSsdSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12138)
)
nimbleDfcSsdSizeMismatch.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcSsdSizeMismatch.setStatus(
        "current"
    )

nimbleDfcHddFailedAfs = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12139)
)
nimbleDfcHddFailedAfs.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcHddFailedAfs.setStatus(
        "current"
    )

nimbleDfcDiskDiagRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12140)
)
nimbleDfcDiskDiagRemoved.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcDiskDiagRemoved.setStatus(
        "current"
    )

nimbleDfcSsdAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12141)
)
nimbleDfcSsdAbsent.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDfcSsdAbsent.setStatus(
        "current"
    )

nimbleSsdAbsentV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12142)
)
nimbleSsdAbsentV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAbsentV3.setStatus(
        "current"
    )

nimbleHddAbsentV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12143)
)
nimbleHddAbsentV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddAbsentV3.setStatus(
        "current"
    )

nimbleIposerFwUpdateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12144)
)
nimbleIposerFwUpdateStart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIposerFwUpdateStart.setStatus(
        "current"
    )

nimbleIposerFwUpdateSucceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12145)
)
nimbleIposerFwUpdateSucceed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIposerFwUpdateSucceed.setStatus(
        "current"
    )

nimbleIposerFwUpdateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12146)
)
nimbleIposerFwUpdateFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIposerFwUpdateFail.setStatus(
        "current"
    )

nimbleScmFailedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12147)
)
nimbleScmFailedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleScmFailedV3.setStatus(
        "current"
    )

nimbleScmAddedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12148)
)
nimbleScmAddedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleScmAddedV3.setStatus(
        "current"
    )

nimbleScmAbsentV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12150)
)
nimbleScmAbsentV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleScmAbsentV3.setStatus(
        "current"
    )

nimbleAfturboWithScm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12151)
)
nimbleAfturboWithScm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAfturboWithScm.setStatus(
        "current"
    )

nimbleAfturboDegradeToAfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12152)
)
nimbleAfturboDegradeToAfa.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAfturboDegradeToAfa.setStatus(
        "current"
    )

nimbleScmHighTemperatureV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12153)
)
nimbleScmHighTemperatureV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleScmHighTemperatureV3.setStatus(
        "current"
    )

nimbleScmCrithighTemperatureV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12154)
)
nimbleScmCrithighTemperatureV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleScmCrithighTemperatureV3.setStatus(
        "current"
    )

nimbleScmTemperatureCritOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12155)
)
nimbleScmTemperatureCritOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleScmTemperatureCritOk.setStatus(
        "current"
    )

nimbleScmTemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12156)
)
nimbleScmTemperatureOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleScmTemperatureOk.setStatus(
        "current"
    )

nimbleIpIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12200)
)
nimbleIpIfDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDown.setStatus(
        "current"
    )

nimbleIpIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12201)
)
nimbleIpIfUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfUp.setStatus(
        "current"
    )

nimbleIpIfGroupUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12202)
)
nimbleIpIfGroupUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfGroupUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfDataUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12203)
)
nimbleIpIfDataUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDataUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfCantFailoverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12204)
)
nimbleIpIfCantFailoverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfCantFailoverDeprecated.setStatus(
        "obsolete"
    )

nimbleSubnetNicMigrationDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12205)
)
nimbleSubnetNicMigrationDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSubnetNicMigrationDeprecated.setStatus(
        "obsolete"
    )

nimbleSubnetNicMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12206)
)
nimbleSubnetNicMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSubnetNicMissingDeprecated.setStatus(
        "obsolete"
    )

nimbleIpNicMigrationDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12207)
)
nimbleIpNicMigrationDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpNicMigrationDeprecated.setStatus(
        "obsolete"
    )

nimbleIpNicMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12208)
)
nimbleIpNicMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpNicMissingDeprecated.setStatus(
        "obsolete"
    )

nimbleRouteNicMigrationDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12209)
)
nimbleRouteNicMigrationDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRouteNicMigrationDeprecated.setStatus(
        "obsolete"
    )

nimbleRouteNicMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12210)
)
nimbleRouteNicMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRouteNicMissingDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfFailoverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12211)
)
nimbleIpIfFailoverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfFailoverDeprecated.setStatus(
        "obsolete"
    )

nimbleIpDupFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12212)
)
nimbleIpDupFound.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpDupFound.setStatus(
        "current"
    )

nimbleIpIfDiscoveryUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12213)
)
nimbleIpIfDiscoveryUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDiscoveryUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfTargetUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12214)
)
nimbleIpIfTargetUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfTargetUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfGroupUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12215)
)
nimbleIpIfGroupUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfGroupUnavail.setStatus(
        "current"
    )

nimbleIpIfDiscoveryUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12216)
)
nimbleIpIfDiscoveryUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDiscoveryUnavail.setStatus(
        "current"
    )

nimbleIpIfTargetUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12217)
)
nimbleIpIfTargetUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfTargetUnavail.setStatus(
        "current"
    )

nimbleIpIfDataUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12218)
)
nimbleIpIfDataUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDataUnavail.setStatus(
        "current"
    )

nimbleIpIfIscsiDataUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12219)
)
nimbleIpIfIscsiDataUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfIscsiDataUnavail.setStatus(
        "current"
    )

nimbleIpIfClusterDataUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12220)
)
nimbleIpIfClusterDataUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfClusterDataUnavail.setStatus(
        "current"
    )

nimbleUnresponsiveNicDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12221)
)
nimbleUnresponsiveNicDetected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUnresponsiveNicDetected.setStatus(
        "current"
    )

nimbleIpIfCantFailoverDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12222)
)
nimbleIpIfCantFailoverDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfCantFailoverDeprecated2.setStatus(
        "obsolete"
    )

nimbleIpIfCantFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12223)
)
nimbleIpIfCantFailover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfCantFailover.setStatus(
        "current"
    )

nimbleNicMigrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12224)
)
nimbleNicMigrationFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNicMigrationFailed.setStatus(
        "current"
    )

nimbleNicPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12225)
)
nimbleNicPortUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNicPortUp.setStatus(
        "current"
    )

nimbleNicPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12226)
)
nimbleNicPortDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNicPortDown.setStatus(
        "current"
    )

nimbleSensorLinearWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12301)
)
nimbleSensorLinearWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorLinearWarn.setStatus(
        "current"
    )

nimbleSensorLinearClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12302)
)
nimbleSensorLinearClear.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorLinearClear.setStatus(
        "current"
    )

nimbleSensorBoolWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12303)
)
nimbleSensorBoolWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorBoolWarn.setStatus(
        "current"
    )

nimbleSensorBoolClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12304)
)
nimbleSensorBoolClear.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorBoolClear.setStatus(
        "current"
    )

nimbleSensorDoesNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12305)
)
nimbleSensorDoesNotExist.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorDoesNotExist.setStatus(
        "current"
    )

nimbleNvramBattDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12306)
)
nimbleNvramBattDisabled.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattDisabled.setStatus(
        "current"
    )

nimbleNvramBattDisabledCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12307)
)
nimbleNvramBattDisabledCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattDisabledCrit.setStatus(
        "current"
    )

nimbleNvramBattOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12308)
)
nimbleNvramBattOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattOk.setStatus(
        "current"
    )

nimbleTempSensorHighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12310)
)
nimbleTempSensorHighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated.setStatus(
        "obsolete"
    )

nimbleTempSensorLowDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12311)
)
nimbleTempSensorLowDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorLowDeprecated.setStatus(
        "obsolete"
    )

nimbleTempSensorOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12312)
)
nimbleTempSensorOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOkDeprecated.setStatus(
        "obsolete"
    )

nimbleTempSensorMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12313)
)
nimbleTempSensorMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorMissingDeprecated.setStatus(
        "obsolete"
    )

nimbleTempSensorOperationalDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12314)
)
nimbleTempSensorOperationalDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOperationalDeprecated.setStatus(
        "obsolete"
    )

nimbleFanSensorHighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12315)
)
nimbleFanSensorHighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorHighDeprecated.setStatus(
        "obsolete"
    )

nimbleFanSensorLowDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12316)
)
nimbleFanSensorLowDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorLowDeprecated.setStatus(
        "obsolete"
    )

nimbleFanSensorOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12317)
)
nimbleFanSensorOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorOkDeprecated.setStatus(
        "obsolete"
    )

nimbleFanSensorStoppedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12318)
)
nimbleFanSensorStoppedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorStoppedDeprecated.setStatus(
        "obsolete"
    )

nimbleFanSensorMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12319)
)
nimbleFanSensorMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorMissingDeprecated.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12320)
)
nimblePwrSupplySensorFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorFailDeprecated.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12321)
)
nimblePwrSupplySensorMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorMissingDeprecated.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12322)
)
nimblePwrSupplySensorOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorOkDeprecated.setStatus(
        "obsolete"
    )

nimbleTempSensorHighDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12323)
)
nimbleTempSensorHighDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated2.setStatus(
        "obsolete"
    )

nimbleTempSensorLowDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12324)
)
nimbleTempSensorLowDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorLowDeprecated2.setStatus(
        "obsolete"
    )

nimbleTempSensorOkDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12325)
)
nimbleTempSensorOkDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOkDeprecated2.setStatus(
        "obsolete"
    )

nimbleTempSensorMissingDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12326)
)
nimbleTempSensorMissingDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorMissingDeprecated2.setStatus(
        "obsolete"
    )

nimbleTempSensorOperationalDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12327)
)
nimbleTempSensorOperationalDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOperationalDeprecated2.setStatus(
        "obsolete"
    )

nimbleFanSensorHighDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12328)
)
nimbleFanSensorHighDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorHighDeprecated2.setStatus(
        "obsolete"
    )

nimbleFanSensorLowDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12329)
)
nimbleFanSensorLowDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorLowDeprecated2.setStatus(
        "obsolete"
    )

nimbleFanSensorOkDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12330)
)
nimbleFanSensorOkDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorOkDeprecated2.setStatus(
        "obsolete"
    )

nimbleFanSensorStoppedDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12331)
)
nimbleFanSensorStoppedDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorStoppedDeprecated2.setStatus(
        "obsolete"
    )

nimbleFanSensorMissingDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12332)
)
nimbleFanSensorMissingDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorMissingDeprecated2.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorFailDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12333)
)
nimblePwrSupplySensorFailDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorFailDeprecated2.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorMissingDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12334)
)
nimblePwrSupplySensorMissingDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorMissingDeprecated2.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorOkDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12335)
)
nimblePwrSupplySensorOkDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorOkDeprecated2.setStatus(
        "obsolete"
    )

nimbleTempSensorHighDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12336)
)
nimbleTempSensorHighDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated3.setStatus(
        "obsolete"
    )

nimbleTempSensorLowDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12337)
)
nimbleTempSensorLowDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorLowDeprecated3.setStatus(
        "obsolete"
    )

nimbleTempSensorOkDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12338)
)
nimbleTempSensorOkDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOkDeprecated3.setStatus(
        "obsolete"
    )

nimbleTempSensorMissingDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12339)
)
nimbleTempSensorMissingDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorMissingDeprecated3.setStatus(
        "obsolete"
    )

nimbleTempSensorOperationalDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12340)
)
nimbleTempSensorOperationalDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOperationalDeprecated3.setStatus(
        "obsolete"
    )

nimbleFanSensorHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12341)
)
nimbleFanSensorHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorHigh.setStatus(
        "current"
    )

nimbleFanSensorLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12342)
)
nimbleFanSensorLow.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorLow.setStatus(
        "current"
    )

nimbleFanSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12343)
)
nimbleFanSensorOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorOk.setStatus(
        "current"
    )

nimbleFanSensorStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12344)
)
nimbleFanSensorStopped.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorStopped.setStatus(
        "current"
    )

nimbleFanSensorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12345)
)
nimbleFanSensorMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorMissing.setStatus(
        "current"
    )

nimblePwrSupplySensorFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12346)
)
nimblePwrSupplySensorFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorFail.setStatus(
        "current"
    )

nimblePwrSupplySensorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12347)
)
nimblePwrSupplySensorMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorMissing.setStatus(
        "current"
    )

nimblePwrSupplySensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12348)
)
nimblePwrSupplySensorOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorOk.setStatus(
        "current"
    )

nimblePsuIncorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12349)
)
nimblePsuIncorrect.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePsuIncorrect.setStatus(
        "current"
    )

nimblePsuOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12350)
)
nimblePsuOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePsuOk.setStatus(
        "current"
    )

nimblePwrSupplySensorAcLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12351)
)
nimblePwrSupplySensorAcLoss.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorAcLoss.setStatus(
        "current"
    )

nimblePwrSupplySensorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12352)
)
nimblePwrSupplySensorFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorFailed.setStatus(
        "current"
    )

nimbleTempSensorLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12353)
)
nimbleTempSensorLow.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorLow.setStatus(
        "current"
    )

nimbleTempSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12354)
)
nimbleTempSensorOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOk.setStatus(
        "current"
    )

nimbleTempSensorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12355)
)
nimbleTempSensorMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorMissing.setStatus(
        "current"
    )

nimbleTempSensorOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12356)
)
nimbleTempSensorOperational.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOperational.setStatus(
        "current"
    )

nimbleRaidDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12400)
)
nimbleRaidDegraded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDegraded.setStatus(
        "current"
    )

nimbleRaidRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12401)
)
nimbleRaidRebuildStart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildStart.setStatus(
        "current"
    )

nimbleRaidRebuildDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12402)
)
nimbleRaidRebuildDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildDone.setStatus(
        "current"
    )

nimbleRaidRebuildFailRead = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12403)
)
nimbleRaidRebuildFailRead.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFailRead.setStatus(
        "current"
    )

nimbleRaidRebuildFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12404)
)
nimbleRaidRebuildFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFail.setStatus(
        "current"
    )

nimbleRaidDisksMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12405)
)
nimbleRaidDisksMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDisksMissing.setStatus(
        "current"
    )

nimbleRaidSpare = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12406)
)
nimbleRaidSpare.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidSpare.setStatus(
        "current"
    )

nimbleRaidAssemblyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12407)
)
nimbleRaidAssemblyFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidAssemblyFailed.setStatus(
        "current"
    )

nimbleRaidDegradedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12408)
)
nimbleRaidDegradedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDegradedV2.setStatus(
        "current"
    )

nimbleRaidRebuildStartV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12409)
)
nimbleRaidRebuildStartV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildStartV2.setStatus(
        "current"
    )

nimbleRaidRebuildDoneV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12410)
)
nimbleRaidRebuildDoneV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildDoneV2.setStatus(
        "current"
    )

nimbleRaidRebuildFailReadV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12411)
)
nimbleRaidRebuildFailReadV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFailReadV2.setStatus(
        "current"
    )

nimbleRaidRebuildFailV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12412)
)
nimbleRaidRebuildFailV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFailV2.setStatus(
        "current"
    )

nimbleRaidDisksMissingV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12413)
)
nimbleRaidDisksMissingV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDisksMissingV2.setStatus(
        "current"
    )

nimbleRaidSpareV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12414)
)
nimbleRaidSpareV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidSpareV2.setStatus(
        "current"
    )

nimbleRaidAssemblyFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12415)
)
nimbleRaidAssemblyFailedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidAssemblyFailedV2.setStatus(
        "current"
    )

nimbleRaidRebuildScheduledV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12416)
)
nimbleRaidRebuildScheduledV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildScheduledV2.setStatus(
        "current"
    )

nimbleRaidRebuildStopV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12417)
)
nimbleRaidRebuildStopV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildStopV2.setStatus(
        "current"
    )

nimbleRaidRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12418)
)
nimbleRaidRedundancy.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRedundancy.setStatus(
        "current"
    )

nimbleIscsiMultiInitiatorDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12500)
)
nimbleIscsiMultiInitiatorDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiMultiInitiatorDeprecated.setStatus(
        "obsolete"
    )

nimbleIscsiConnHardLimitDeprecated1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12501)
)
nimbleIscsiConnHardLimitDeprecated1.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiConnHardLimitDeprecated1.setStatus(
        "obsolete"
    )

nimbleIscsiUnalignedOpsDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12502)
)
nimbleIscsiUnalignedOpsDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiUnalignedOpsDeprecated.setStatus(
        "obsolete"
    )

nimbleIscsiMultiInitiator = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12503)
)
nimbleIscsiMultiInitiator.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiMultiInitiator.setStatus(
        "current"
    )

nimbleIscsiConnHardLimitDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12504)
)
nimbleIscsiConnHardLimitDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiConnHardLimitDeprecated2.setStatus(
        "obsolete"
    )

nimbleIscsiUnalignedOps = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12505)
)
nimbleIscsiUnalignedOps.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiUnalignedOps.setStatus(
        "current"
    )

nimbleIscsiConnHardLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12506)
)
nimbleIscsiConnHardLimit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiConnHardLimit.setStatus(
        "current"
    )

nimbleIscsiErroneousItorConns = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12508)
)
nimbleIscsiErroneousItorConns.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiErroneousItorConns.setStatus(
        "current"
    )

nimbleNvramBattCharging = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12601)
)
nimbleNvramBattCharging.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattCharging.setStatus(
        "current"
    )

nimbleNvramBattCharged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12602)
)
nimbleNvramBattCharged.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattCharged.setStatus(
        "current"
    )

nimbleNvramFpgaVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12603)
)
nimbleNvramFpgaVersion.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramFpgaVersion.setStatus(
        "current"
    )

nimbleNvramMbeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12604)
)
nimbleNvramMbeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramMbeDeprecated.setStatus(
        "obsolete"
    )

nimbleNvramSbeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12605)
)
nimbleNvramSbeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramSbeDeprecated.setStatus(
        "obsolete"
    )

nimbleNvramMbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12606)
)
nimbleNvramMbe.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramMbe.setStatus(
        "current"
    )

nimbleNvramSbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12607)
)
nimbleNvramSbe.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramSbe.setStatus(
        "current"
    )

nimbleNvdimmReservedBlocksWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12608)
)
nimbleNvdimmReservedBlocksWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmReservedBlocksWarn.setStatus(
        "current"
    )

nimbleNvdimmReservedBlocksCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12609)
)
nimbleNvdimmReservedBlocksCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmReservedBlocksCrit.setStatus(
        "current"
    )

nimbleNvdimmUltracapDischargedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12610)
)
nimbleNvdimmUltracapDischargedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmUltracapDischargedDeprecated.setStatus(
        "obsolete"
    )

nimbleNtbBadLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12611)
)
nimbleNtbBadLink.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNtbBadLink.setStatus(
        "current"
    )

nimbleNvdimmUltracapDischargedDeprecated1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12612)
)
nimbleNvdimmUltracapDischargedDeprecated1.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmUltracapDischargedDeprecated1.setStatus(
        "obsolete"
    )

nimbleNvramMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12613)
)
nimbleNvramMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramMissing.setStatus(
        "current"
    )

nimbleNvdimmUltracapDischargedDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12614)
)
nimbleNvdimmUltracapDischargedDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmUltracapDischargedDeprecated2.setStatus(
        "obsolete"
    )

nimbleEncryptionKeysMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12615)
)
nimbleEncryptionKeysMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEncryptionKeysMissing.setStatus(
        "current"
    )

nimbleNvdimmUltracapDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12616)
)
nimbleNvdimmUltracapDischarged.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmUltracapDischarged.setStatus(
        "current"
    )

nimbleShelfCtrlrSide = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12701)
)
nimbleShelfCtrlrSide.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfCtrlrSide.setStatus(
        "current"
    )

nimbleShelfSesErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12702)
)
nimbleShelfSesErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesErr.setStatus(
        "current"
    )

nimbleShelfDiskSasLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12703)
)
nimbleShelfDiskSasLink.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskSasLink.setStatus(
        "current"
    )

nimbleShelfDiskCountDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12704)
)
nimbleShelfDiskCountDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskCountDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfInvalidEeprom = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12705)
)
nimbleShelfInvalidEeprom.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfInvalidEeprom.setStatus(
        "current"
    )

nimbleShelfWrongSasPortDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12706)
)
nimbleShelfWrongSasPortDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfWrongSasPortDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfSasLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12707)
)
nimbleShelfSasLink.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasLink.setStatus(
        "current"
    )

nimbleShelfSasExpErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12708)
)
nimbleShelfSasExpErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasExpErr.setStatus(
        "current"
    )

nimbleShelfCtrlrLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12709)
)
nimbleShelfCtrlrLoop.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfCtrlrLoop.setStatus(
        "current"
    )

nimbleShelfMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12710)
)
nimbleShelfMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfMissing.setStatus(
        "current"
    )

nimbleShelfOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12711)
)
nimbleShelfOrder.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfOrder.setStatus(
        "current"
    )

nimbleShelfSesMshipErrDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12712)
)
nimbleShelfSesMshipErrDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfFailoverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12713)
)
nimbleShelfFailoverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfFailoverDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfNewShelf = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12714)
)
nimbleShelfNewShelf.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfNewShelf.setStatus(
        "current"
    )

nimbleShelfDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12715)
)
nimbleShelfDisconnect.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDisconnect.setStatus(
        "current"
    )

nimbleShelfChassisSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12716)
)
nimbleShelfChassisSwap.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfChassisSwap.setStatus(
        "current"
    )

nimbleShelfLocIdOverLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12717)
)
nimbleShelfLocIdOverLimit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfLocIdOverLimit.setStatus(
        "current"
    )

nimbleShelfActivatedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12718)
)
nimbleShelfActivatedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfActivatedDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12719)
)
nimbleShelfReconnect.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfReconnect.setStatus(
        "current"
    )

nimbleShelfSasLinkDisabledDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12720)
)
nimbleShelfSasLinkDisabledDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasLinkDisabledDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfDiskSasLinkErrDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12721)
)
nimbleShelfDiskSasLinkErrDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskSasLinkErrDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfWrongSasPortDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12730)
)
nimbleShelfWrongSasPortDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfWrongSasPortDeprecated2.setStatus(
        "obsolete"
    )

nimbleShelfSesMshipErrDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12731)
)
nimbleShelfSesMshipErrDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated2.setStatus(
        "obsolete"
    )

nimbleShelfSasLinkDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12732)
)
nimbleShelfSasLinkDisabled.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasLinkDisabled.setStatus(
        "current"
    )

nimbleShelfDiskSasLinkErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12733)
)
nimbleShelfDiskSasLinkErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskSasLinkErr.setStatus(
        "current"
    )

nimbleShelfWrongSasPortDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12734)
)
nimbleShelfWrongSasPortDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfWrongSasPortDeprecated3.setStatus(
        "obsolete"
    )

nimbleShelfSesMshipErrDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12735)
)
nimbleShelfSesMshipErrDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated3.setStatus(
        "obsolete"
    )

nimbleShelfSesMshipErrDeprecated4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12736)
)
nimbleShelfSesMshipErrDeprecated4.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated4.setStatus(
        "obsolete"
    )

nimbleShelfActivatedV2Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12737)
)
nimbleShelfActivatedV2Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfActivatedV2Deprecated.setStatus(
        "obsolete"
    )

nimbleShelfSesMshipErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12738)
)
nimbleShelfSesMshipErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErr.setStatus(
        "current"
    )

nimbleShelfActivatedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12739)
)
nimbleShelfActivatedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfActivatedV2.setStatus(
        "current"
    )

nimbleShelfIpmiMshipErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12740)
)
nimbleShelfIpmiMshipErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfIpmiMshipErr.setStatus(
        "current"
    )

nimbleShelfWrongSasPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12741)
)
nimbleShelfWrongSasPort.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfWrongSasPort.setStatus(
        "current"
    )

nimbleShelfBadDiskPhy = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12742)
)
nimbleShelfBadDiskPhy.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfBadDiskPhy.setStatus(
        "current"
    )

nimbleShelfBadInterconnectDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12743)
)
nimbleShelfBadInterconnectDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfBadInterconnectDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfBadInterconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12744)
)
nimbleShelfBadInterconnect.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfBadInterconnect.setStatus(
        "current"
    )

nimbleShelfDiskCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12745)
)
nimbleShelfDiskCount.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskCount.setStatus(
        "current"
    )

nimbleShelfBadCutlassDiskPhy = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12746)
)
nimbleShelfBadCutlassDiskPhy.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfBadCutlassDiskPhy.setStatus(
        "current"
    )

nimbleShelfEvacuationInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12747)
)
nimbleShelfEvacuationInitiated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationInitiated.setStatus(
        "current"
    )

nimbleShelfEvacuationComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12748)
)
nimbleShelfEvacuationComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationComplete.setStatus(
        "current"
    )

nimbleShelfEvacuationPausedByUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12749)
)
nimbleShelfEvacuationPausedByUser.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationPausedByUser.setStatus(
        "current"
    )

nimbleShelfEvacuationResumedByUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12750)
)
nimbleShelfEvacuationResumedByUser.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationResumedByUser.setStatus(
        "current"
    )

nimbleShelfEvacuationCancelByUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12751)
)
nimbleShelfEvacuationCancelByUser.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationCancelByUser.setStatus(
        "current"
    )

nimbleShelfEvacuationFailSpaceUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12752)
)
nimbleShelfEvacuationFailSpaceUsage.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationFailSpaceUsage.setStatus(
        "current"
    )

nimbleShelfEvacuationFailSpaceRed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12753)
)
nimbleShelfEvacuationFailSpaceRed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationFailSpaceRed.setStatus(
        "current"
    )

nimbleShelfEvacuationFailSpaceResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12754)
)
nimbleShelfEvacuationFailSpaceResume.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationFailSpaceResume.setStatus(
        "current"
    )

nimbleShelfEvacuationFailSpaceRedResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12755)
)
nimbleShelfEvacuationFailSpaceRedResume.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationFailSpaceRedResume.setStatus(
        "current"
    )

nimbleShelfEvacuationFailDataMove = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12756)
)
nimbleShelfEvacuationFailDataMove.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfEvacuationFailDataMove.setStatus(
        "current"
    )

nimblePhysMemMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12901)
)
nimblePhysMemMismatch.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePhysMemMismatch.setStatus(
        "current"
    )

nimbleVolSysLimitWarnEnter = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13101)
)
nimbleVolSysLimitWarnEnter.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSysLimitWarnEnter.setStatus(
        "current"
    )

nimbleVolSysLimitWarnExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13102)
)
nimbleVolSysLimitWarnExit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSysLimitWarnExit.setStatus(
        "current"
    )

nimbleGmTakeoverSuccessDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13501)
)
nimbleGmTakeoverSuccessDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverSuccessDeprecated.setStatus(
        "obsolete"
    )

nimbleGmTakeoverRejectByArrayDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13502)
)
nimbleGmTakeoverRejectByArrayDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverRejectByArrayDeprecated.setStatus(
        "obsolete"
    )

nimbleGmTakeoverRejectByArrayDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13503)
)
nimbleGmTakeoverRejectByArrayDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverRejectByArrayDeprecated2.setStatus(
        "obsolete"
    )

nimbleGmTakeoverSuccessDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13504)
)
nimbleGmTakeoverSuccessDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverSuccessDeprecated2.setStatus(
        "obsolete"
    )

nimbleGmTakeoverSuccessDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13505)
)
nimbleGmTakeoverSuccessDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverSuccessDeprecated3.setStatus(
        "obsolete"
    )

nimbleGmMigrateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13506)
)
nimbleGmMigrateFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmMigrateFailure.setStatus(
        "current"
    )

nimbleGmTakeoverSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13507)
)
nimbleGmTakeoverSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverSuccess.setStatus(
        "current"
    )

nimbleGmTakeoverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13508)
)
nimbleGmTakeoverFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverFailure.setStatus(
        "current"
    )

nimbleGmSuccessfullySetupBgl = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13509)
)
nimbleGmSuccessfullySetupBgl.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSuccessfullySetupBgl.setStatus(
        "current"
    )

nimbleGmNoBglAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13510)
)
nimbleGmNoBglAvailable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmNoBglAvailable.setStatus(
        "current"
    )

nimbleGmBglOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13511)
)
nimbleGmBglOutOfSync.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmBglOutOfSync.setStatus(
        "current"
    )

nimbleGmGlSplitBrain = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13512)
)
nimbleGmGlSplitBrain.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGlSplitBrain.setStatus(
        "current"
    )

nimbleGmTakeoverAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13513)
)
nimbleGmTakeoverAttempt.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverAttempt.setStatus(
        "current"
    )

nimbleGmTakeoverNotifyLeaderRoleDelayDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13514)
)
nimbleGmTakeoverNotifyLeaderRoleDelayDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverNotifyLeaderRoleDelayDeprecated.setStatus(
        "obsolete"
    )

nimbleGmTakeoverNotifyLeaderRoleComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13515)
)
nimbleGmTakeoverNotifyLeaderRoleComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverNotifyLeaderRoleComplete.setStatus(
        "current"
    )

nimbleGmNoSmip = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13516)
)
nimbleGmNoSmip.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmNoSmip.setStatus(
        "current"
    )

nimbleGmSmipConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13517)
)
nimbleGmSmipConfigured.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSmipConfigured.setStatus(
        "current"
    )

nimbleGmSmipNotNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13518)
)
nimbleGmSmipNotNeeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSmipNotNeeded.setStatus(
        "current"
    )

nimbleGmBglInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13519)
)
nimbleGmBglInSync.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmBglInSync.setStatus(
        "current"
    )

nimbleGmNoBglPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13520)
)
nimbleGmNoBglPossible.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmNoBglPossible.setStatus(
        "current"
    )

nimbleGmNoArrayFoundWithSameLimitAsGlDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13521)
)
nimbleGmNoArrayFoundWithSameLimitAsGlDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmNoArrayFoundWithSameLimitAsGlDeprecated.setStatus(
        "obsolete"
    )

nimbleGmWitnessDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13522)
)
nimbleGmWitnessDisconnected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmWitnessDisconnected.setStatus(
        "current"
    )

nimbleGmWitnessConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13523)
)
nimbleGmWitnessConnected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmWitnessConnected.setStatus(
        "current"
    )

nimbleGmQuorumPeerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13524)
)
nimbleGmQuorumPeerFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumPeerFailure.setStatus(
        "current"
    )

nimbleGmQuorumPeerSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13525)
)
nimbleGmQuorumPeerSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumPeerSuccess.setStatus(
        "current"
    )

nimbleGmQuorumLocalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13526)
)
nimbleGmQuorumLocalFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumLocalFailure.setStatus(
        "current"
    )

nimbleGmQuorumLocalSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13527)
)
nimbleGmQuorumLocalSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumLocalSuccess.setStatus(
        "current"
    )

nimbleGmQuorumSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13528)
)
nimbleGmQuorumSetupFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumSetupFailure.setStatus(
        "current"
    )

nimbleGmQuorumSetupSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13529)
)
nimbleGmQuorumSetupSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumSetupSuccess.setStatus(
        "current"
    )

nimbleGmAutoShutoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13530)
)
nimbleGmAutoShutoff.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmAutoShutoff.setStatus(
        "current"
    )

nimbleGmQuorumWitnessUuidChangeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13531)
)
nimbleGmQuorumWitnessUuidChangeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumWitnessUuidChangeDeprecated.setStatus(
        "obsolete"
    )

nimbleGmQuorumTeardownSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13532)
)
nimbleGmQuorumTeardownSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumTeardownSuccess.setStatus(
        "current"
    )

nimbleGmTakeoverNotifyLeaderRoleDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13533)
)
nimbleGmTakeoverNotifyLeaderRoleDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverNotifyLeaderRoleDelay.setStatus(
        "current"
    )

nimbleGmNoArrayFoundWithSameLimitAsGl = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13534)
)
nimbleGmNoArrayFoundWithSameLimitAsGl.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmNoArrayFoundWithSameLimitAsGl.setStatus(
        "current"
    )

nimbleGmQuorumWitnessUuidChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13535)
)
nimbleGmQuorumWitnessUuidChange.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmQuorumWitnessUuidChange.setStatus(
        "current"
    )

nimbleGmGrpMrgDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13601)
)
nimbleGmGrpMrgDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgDone.setStatus(
        "current"
    )

nimbleGmGrpQscFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13602)
)
nimbleGmGrpQscFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpQscFail.setStatus(
        "current"
    )

nimbleGmGrpMrgRollbackDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13603)
)
nimbleGmGrpMrgRollbackDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgRollbackDone.setStatus(
        "current"
    )

nimbleGmGrpMrgReassFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13604)
)
nimbleGmGrpMrgReassFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgReassFail.setStatus(
        "current"
    )

nimbleGmGrpMrgDbFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13605)
)
nimbleGmGrpMrgDbFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgDbFail.setStatus(
        "current"
    )

nimbleGmBinMigContAbortDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13701)
)
nimbleGmBinMigContAbortDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmBinMigContAbortDeprecated.setStatus(
        "obsolete"
    )

nimbleGmBinMigContAbortDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13702)
)
nimbleGmBinMigContAbortDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmBinMigContAbortDeprecated2.setStatus(
        "obsolete"
    )

nimbleGmBinMigContAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13703)
)
nimbleGmBinMigContAbort.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmBinMigContAbort.setStatus(
        "current"
    )

nimbleCsmodelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14000)
)
nimbleCsmodelChanged.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCsmodelChanged.setStatus(
        "current"
    )

nimbleCsmodelUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14001)
)
nimbleCsmodelUnknown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCsmodelUnknown.setStatus(
        "current"
    )

nimbleTempSensorHighDeprecated4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14002)
)
nimbleTempSensorHighDeprecated4.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated4.setStatus(
        "obsolete"
    )

nimbleOvertempShutdownDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14003)
)
nimbleOvertempShutdownDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleOvertempShutdownDeprecated2.setStatus(
        "obsolete"
    )

nimbleCtrlrOvertemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14004)
)
nimbleCtrlrOvertemp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrOvertemp.setStatus(
        "current"
    )

nimbleBackplaneOvertemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14005)
)
nimbleBackplaneOvertemp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBackplaneOvertemp.setStatus(
        "current"
    )

nimbleTempSensorHighDeprecated5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14006)
)
nimbleTempSensorHighDeprecated5.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated5.setStatus(
        "obsolete"
    )

nimbleTempSensorCrithighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14007)
)
nimbleTempSensorCrithighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorCrithighDeprecated.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorCallsupportDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14008)
)
nimblePwrSupplySensorCallsupportDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorCallsupportDeprecated.setStatus(
        "obsolete"
    )

nimbleOvertempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14009)
)
nimbleOvertempShutdown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleOvertempShutdown.setStatus(
        "current"
    )

nimblePwrSupplySensorCallsupportDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14010)
)
nimblePwrSupplySensorCallsupportDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorCallsupportDeprecated2.setStatus(
        "obsolete"
    )

nimbleTempSensorHighDeprecated6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14011)
)
nimbleTempSensorHighDeprecated6.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated6.setStatus(
        "obsolete"
    )

nimbleTempSensorCrithighDeprecated1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14012)
)
nimbleTempSensorCrithighDeprecated1.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorCrithighDeprecated1.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorCallsupportDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14013)
)
nimblePwrSupplySensorCallsupportDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorCallsupportDeprecated3.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorCallsupportDeprecated4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14014)
)
nimblePwrSupplySensorCallsupportDeprecated4.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorCallsupportDeprecated4.setStatus(
        "obsolete"
    )

nimbleTempSensorCrithighDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14015)
)
nimbleTempSensorCrithighDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorCrithighDeprecated2.setStatus(
        "obsolete"
    )

nimbleTempAmbientCrithigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14016)
)
nimbleTempAmbientCrithigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempAmbientCrithigh.setStatus(
        "current"
    )

nimbleTempAmbientHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14017)
)
nimbleTempAmbientHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempAmbientHigh.setStatus(
        "current"
    )

nimbleTempAmbientOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14018)
)
nimbleTempAmbientOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempAmbientOk.setStatus(
        "current"
    )

nimbleTempAmbientClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14019)
)
nimbleTempAmbientClear.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempAmbientClear.setStatus(
        "current"
    )

nimbleTempSensorHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14020)
)
nimbleTempSensorHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHigh.setStatus(
        "current"
    )

nimbleTempSensorCrithigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14021)
)
nimbleTempSensorCrithigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorCrithigh.setStatus(
        "current"
    )

nimbleTempOvertempCrithigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14022)
)
nimbleTempOvertempCrithigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempOvertempCrithigh.setStatus(
        "current"
    )

nimbleTempOvertempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14023)
)
nimbleTempOvertempOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempOvertempOk.setStatus(
        "current"
    )

nimblePwrSupplySensorCallsupport = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14024)
)
nimblePwrSupplySensorCallsupport.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorCallsupport.setStatus(
        "current"
    )

nimbleUpdateUnknownFirmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14200)
)
nimbleUpdateUnknownFirmware.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnknownFirmware.setStatus(
        "current"
    )

nimbleDiskFwUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14201)
)
nimbleDiskFwUpdateStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFwUpdateStarted.setStatus(
        "current"
    )

nimbleDiskFwUptodate = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14202)
)
nimbleDiskFwUptodate.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFwUptodate.setStatus(
        "current"
    )

nimbleDiskFwUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14203)
)
nimbleDiskFwUpdateFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFwUpdateFailed.setStatus(
        "current"
    )

nimbleDiskFwUpdateDeferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14204)
)
nimbleDiskFwUpdateDeferred.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFwUpdateDeferred.setStatus(
        "current"
    )

nimbleFcLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14400)
)
nimbleFcLinkUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcLinkUp.setStatus(
        "current"
    )

nimbleFcLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14401)
)
nimbleFcLinkDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcLinkDown.setStatus(
        "current"
    )

nimbleFcLinkNotConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14402)
)
nimbleFcLinkNotConnected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcLinkNotConnected.setStatus(
        "current"
    )

nimbleFcFabricUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14403)
)
nimbleFcFabricUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcFabricUp.setStatus(
        "current"
    )

nimbleFcNoFabric = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14404)
)
nimbleFcNoFabric.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcNoFabric.setStatus(
        "current"
    )

nimbleFcHbaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14405)
)
nimbleFcHbaFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcHbaFailure.setStatus(
        "current"
    )

nimbleFcAsymmetricControllerConnectivityDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14406)
)
nimbleFcAsymmetricControllerConnectivityDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcAsymmetricControllerConnectivityDeprecated.setStatus(
        "obsolete"
    )

nimbleFcAsymmetricControllerConnectivityOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14407)
)
nimbleFcAsymmetricControllerConnectivityOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcAsymmetricControllerConnectivityOkDeprecated.setStatus(
        "obsolete"
    )

nimbleFcAsymmetricControllerConnectivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14408)
)
nimbleFcAsymmetricControllerConnectivity.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcAsymmetricControllerConnectivity.setStatus(
        "current"
    )

nimbleFcAsymmetricControllerConnectivityOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14409)
)
nimbleFcAsymmetricControllerConnectivityOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcAsymmetricControllerConnectivityOk.setStatus(
        "current"
    )

nimbleFcPortLoginLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14410)
)
nimbleFcPortLoginLimitExceeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcPortLoginLimitExceeded.setStatus(
        "current"
    )

nimbleFcTdzNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14411)
)
nimbleFcTdzNotSupported.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcTdzNotSupported.setStatus(
        "current"
    )

nimbleFcTdzNotEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14412)
)
nimbleFcTdzNotEnabled.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcTdzNotEnabled.setStatus(
        "current"
    )

nimbleEventPurgingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14700)
)
nimbleEventPurgingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEventPurgingDeprecated.setStatus(
        "obsolete"
    )

nimbleEventWarnOverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14701)
)
nimbleEventWarnOverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEventWarnOverDeprecated.setStatus(
        "obsolete"
    )

nimbleAuditLogPurgingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14702)
)
nimbleAuditLogPurgingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAuditLogPurgingDeprecated.setStatus(
        "obsolete"
    )

nimbleAuditLogWarnOverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14703)
)
nimbleAuditLogWarnOverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAuditLogWarnOverDeprecated.setStatus(
        "obsolete"
    )

nimbleEventPurging = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14704)
)
nimbleEventPurging.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEventPurging.setStatus(
        "current"
    )

nimbleEventWarnOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14705)
)
nimbleEventWarnOver.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEventWarnOver.setStatus(
        "current"
    )

nimbleAuditLogPurging = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14706)
)
nimbleAuditLogPurging.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAuditLogPurging.setStatus(
        "current"
    )

nimbleAuditLogWarnOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14707)
)
nimbleAuditLogWarnOver.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAuditLogWarnOver.setStatus(
        "current"
    )

nimbleAuditLogRootLoginSuccessDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14800)
)
nimbleAuditLogRootLoginSuccessDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAuditLogRootLoginSuccessDeprecated.setStatus(
        "obsolete"
    )

nimbleAuditLogRootLoginFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14801)
)
nimbleAuditLogRootLoginFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAuditLogRootLoginFailDeprecated.setStatus(
        "obsolete"
    )

nimbleAdLocalPingFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14802)
)
nimbleAdLocalPingFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAdLocalPingFailDeprecated.setStatus(
        "obsolete"
    )

nimbleAdRemotePingFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14803)
)
nimbleAdRemotePingFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAdRemotePingFailDeprecated.setStatus(
        "obsolete"
    )

nimbleAdTrustFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14804)
)
nimbleAdTrustFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAdTrustFailDeprecated.setStatus(
        "obsolete"
    )

nimbleAdCommunicationSuccessDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14805)
)
nimbleAdCommunicationSuccessDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAdCommunicationSuccessDeprecated.setStatus(
        "obsolete"
    )

nimbleRootLoginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14806)
)
nimbleRootLoginSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRootLoginSuccess.setStatus(
        "current"
    )

nimbleRootLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14807)
)
nimbleRootLoginFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRootLoginFail.setStatus(
        "current"
    )

nimbleNsupportLoginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14808)
)
nimbleNsupportLoginSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNsupportLoginSuccess.setStatus(
        "current"
    )

nimbleNsupportLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14809)
)
nimbleNsupportLoginFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNsupportLoginFail.setStatus(
        "current"
    )

nimbleSuRootSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14810)
)
nimbleSuRootSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSuRootSuccess.setStatus(
        "current"
    )

nimbleSuRootFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14811)
)
nimbleSuRootFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSuRootFail.setStatus(
        "current"
    )

nimbleInvalidRoleLoginDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14812)
)
nimbleInvalidRoleLoginDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleInvalidRoleLoginDeprecated.setStatus(
        "obsolete"
    )

nimbleBglLoginSuccessDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14813)
)
nimbleBglLoginSuccessDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBglLoginSuccessDeprecated.setStatus(
        "obsolete"
    )

nimbleBglLoginFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14814)
)
nimbleBglLoginFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBglLoginFailDeprecated.setStatus(
        "obsolete"
    )

nimbleBglLoginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14815)
)
nimbleBglLoginSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBglLoginSuccess.setStatus(
        "current"
    )

nimbleBglLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14816)
)
nimbleBglLoginFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBglLoginFail.setStatus(
        "current"
    )

nimbleDsdPinCacheDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14850)
)
nimbleDsdPinCacheDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdPinCacheDone.setStatus(
        "current"
    )

nimbleDsdPinCacheDsdRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14851)
)
nimbleDsdPinCacheDsdRestart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdPinCacheDsdRestart.setStatus(
        "current"
    )

nimbleDsdPinCacheSsdIssue = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14852)
)
nimbleDsdPinCacheSsdIssue.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdPinCacheSsdIssue.setStatus(
        "current"
    )

nimbleDsdPinCacheInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14853)
)
nimbleDsdPinCacheInternalError.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdPinCacheInternalError.setStatus(
        "current"
    )

nimbleDsdPinCacheOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14854)
)
nimbleDsdPinCacheOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdPinCacheOk.setStatus(
        "current"
    )

nimbleDsdPinCacheLowFdr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14855)
)
nimbleDsdPinCacheLowFdr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdPinCacheLowFdr.setStatus(
        "current"
    )

nimbleArrayDedupeUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14856)
)
nimbleArrayDedupeUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayDedupeUtilizationOk.setStatus(
        "current"
    )

nimbleArrayDedupeUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14857)
)
nimbleArrayDedupeUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayDedupeUtilizationHigh.setStatus(
        "current"
    )

nimbleArrayDedupeUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14858)
)
nimbleArrayDedupeUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayDedupeUtilizationCrit.setStatus(
        "current"
    )

nimbleAdTrustFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14859)
)
nimbleAdTrustFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleAdTrustFail.setStatus(
        "current"
    )

nimbleUnmanagedSnapDeleteSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14860)
)
nimbleUnmanagedSnapDeleteSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUnmanagedSnapDeleteSuccess.setStatus(
        "current"
    )

nimbleCertificateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14861)
)
nimbleCertificateWarning.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCertificateWarning.setStatus(
        "current"
    )

nimbleCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14862)
)
nimbleCertificateExpired.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCertificateExpired.setStatus(
        "current"
    )

nimbleArrayFdrNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14863)
)
nimbleArrayFdrNormal.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayFdrNormal.setStatus(
        "current"
    )

nimbleArrayLowFdrWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14864)
)
nimbleArrayLowFdrWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayLowFdrWarn.setStatus(
        "current"
    )

nimbleArrayLowFdrCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14865)
)
nimbleArrayLowFdrCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayLowFdrCrit.setStatus(
        "current"
    )

nimbleArrayConfigFdrNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14866)
)
nimbleArrayConfigFdrNormal.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayConfigFdrNormal.setStatus(
        "current"
    )

nimbleArrayConfigFdrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14867)
)
nimbleArrayConfigFdrLow.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayConfigFdrLow.setStatus(
        "current"
    )

nimbleArrayDedupeMinConfigRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14868)
)
nimbleArrayDedupeMinConfigRestore.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayDedupeMinConfigRestore.setStatus(
        "current"
    )

nimbleArrayDedupeMinFdr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14869)
)
nimbleArrayDedupeMinFdr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayDedupeMinFdr.setStatus(
        "current"
    )

nimbleArrayDedupeMinSsdCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14870)
)
nimbleArrayDedupeMinSsdCount.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayDedupeMinSsdCount.setStatus(
        "current"
    )

nimbleMaxSessionsLowMemPlat = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14871)
)
nimbleMaxSessionsLowMemPlat.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleMaxSessionsLowMemPlat.setStatus(
        "current"
    )

nimbleUserAcctAuthLockDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14872)
)
nimbleUserAcctAuthLockDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserAcctAuthLockDeprecated.setStatus(
        "obsolete"
    )

nimbleMaxSessionsGroupDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14873)
)
nimbleMaxSessionsGroupDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleMaxSessionsGroupDeprecated.setStatus(
        "obsolete"
    )

nimbleMaxSessionsLoginFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14874)
)
nimbleMaxSessionsLoginFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleMaxSessionsLoginFailDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSrepSnapSucceededDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14875)
)
nimbleSchedSrepSnapSucceededDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSrepSnapSucceededDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSrepSnapSucceededUpstreamFailedDownstreamDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14876)
)
nimbleSchedSrepSnapSucceededUpstreamFailedDownstreamDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSrepSnapSucceededUpstreamFailedDownstreamDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSrepSnapFailedUnknownReasonDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14877)
)
nimbleSchedSrepSnapFailedUnknownReasonDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSrepSnapFailedUnknownReasonDeprecated.setStatus(
        "obsolete"
    )

nimbleReplVolResynchronizationNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14878)
)
nimbleReplVolResynchronizationNeeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplVolResynchronizationNeeded.setStatus(
        "current"
    )

nimbleInvalidRoleLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14879)
)
nimbleInvalidRoleLogin.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleInvalidRoleLogin.setStatus(
        "current"
    )

nimbleUserAcctAuthLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14880)
)
nimbleUserAcctAuthLock.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserAcctAuthLock.setStatus(
        "current"
    )

nimbleMaxSessionsGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14881)
)
nimbleMaxSessionsGroup.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleMaxSessionsGroup.setStatus(
        "current"
    )

nimbleMaxSessionsLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14882)
)
nimbleMaxSessionsLoginFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleMaxSessionsLoginFail.setStatus(
        "current"
    )

nimbleSchedSrepSnapSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14883)
)
nimbleSchedSrepSnapSucceeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSrepSnapSucceeded.setStatus(
        "current"
    )

nimbleSchedSrepSnapSucceededUpstreamFailedDownstream = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14884)
)
nimbleSchedSrepSnapSucceededUpstreamFailedDownstream.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSrepSnapSucceededUpstreamFailedDownstream.setStatus(
        "current"
    )

nimbleSchedSrepSnapFailedUnknownReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14885)
)
nimbleSchedSrepSnapFailedUnknownReason.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSrepSnapFailedUnknownReason.setStatus(
        "current"
    )

nimbleReplAbortedReplThrottledBandwidthZero = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14886)
)
nimbleReplAbortedReplThrottledBandwidthZero.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplAbortedReplThrottledBandwidthZero.setStatus(
        "current"
    )

nimbleReplResumedReplThrottledBandwidthNonZero = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14887)
)
nimbleReplResumedReplThrottledBandwidthNonZero.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplResumedReplThrottledBandwidthNonZero.setStatus(
        "current"
    )

nimbleArrayUpgradePrecheckFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15000)
)
nimbleArrayUpgradePrecheckFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradePrecheckFail.setStatus(
        "current"
    )

nimbleArrayUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15001)
)
nimbleArrayUpgradeStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradeStarted.setStatus(
        "current"
    )

nimbleArrayUpgradePaused = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15002)
)
nimbleArrayUpgradePaused.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradePaused.setStatus(
        "current"
    )

nimbleArrayUpgradeResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15003)
)
nimbleArrayUpgradeResumed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradeResumed.setStatus(
        "current"
    )

nimbleArrayUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15004)
)
nimbleArrayUpgradeFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradeFailed.setStatus(
        "current"
    )

nimbleArrayUpgradeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15005)
)
nimbleArrayUpgradeComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradeComplete.setStatus(
        "current"
    )

nimbleArrayUpgradeAborting = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15006)
)
nimbleArrayUpgradeAborting.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradeAborting.setStatus(
        "current"
    )

nimbleArrayUpgradeAbortFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15007)
)
nimbleArrayUpgradeAbortFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradeAbortFailed.setStatus(
        "current"
    )

nimbleArrayUpgradeAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 15008)
)
nimbleArrayUpgradeAborted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUpgradeAborted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NIMBLE-TRAP-MIB",
    **{"nimble-traps": nimble_traps,
       "trapObjects": trapObjects,
       "trapvariables": trapvariables,
       "trapMsg": trapMsg,
       "trapSeverity": trapSeverity,
       "trapOriginatorName": trapOriginatorName,
       "trapOriginatorSerialNumber": trapOriginatorSerialNumber,
       "trapOriginatorGroupName": trapOriginatorGroupName,
       "trapOriginatorGroupID": trapOriginatorGroupID,
       "trapTarget": trapTarget,
       "trapTargetType": trapTargetType,
       "traps": traps,
       "nimbleDsdRedEntry0101Deprecated": nimbleDsdRedEntry0101Deprecated,
       "nimbleDsdGcBehindSpaceRedExit": nimbleDsdGcBehindSpaceRedExit,
       "nimbleDsdSpaceCrit0103Deprecated": nimbleDsdSpaceCrit0103Deprecated,
       "nimbleDsdSpaceUtilizationHigh": nimbleDsdSpaceUtilizationHigh,
       "nimbleDsdSpaceUtilizationOk": nimbleDsdSpaceUtilizationOk,
       "nimbleDsdSpaceUtilizationCrit": nimbleDsdSpaceUtilizationCrit,
       "nimbleDsdSpaceRedEntry0107Deprecated": nimbleDsdSpaceRedEntry0107Deprecated,
       "nimbleDsdSpaceCrit0110Deprecated": nimbleDsdSpaceCrit0110Deprecated,
       "nimbleDsdGcBehindSpaceRedEntry": nimbleDsdGcBehindSpaceRedEntry,
       "nimbleDsdGcBehindSpaceCrit": nimbleDsdGcBehindSpaceCrit,
       "nimbleDsdSpaceDenyWrite": nimbleDsdSpaceDenyWrite,
       "nimbleDsdSpaceRedEntry": nimbleDsdSpaceRedEntry,
       "nimbleDsdSpaceRedExit": nimbleDsdSpaceRedExit,
       "nimbleDsdSpaceCrit": nimbleDsdSpaceCrit,
       "nimbleCtrlrException": nimbleCtrlrException,
       "nimbleCtrlrTakeover": nimbleCtrlrTakeover,
       "nimbleCtrlrStandbyAvail": nimbleCtrlrStandbyAvail,
       "nimbleCtrlrStandbyUnavail": nimbleCtrlrStandbyUnavail,
       "nimbleCtrlrExcessiveRestarts": nimbleCtrlrExcessiveRestarts,
       "nimbleServiceReboot": nimbleServiceReboot,
       "nimbleUserReboot": nimbleUserReboot,
       "nimbleUserRebootFailed": nimbleUserRebootFailed,
       "nimbleUserHalt": nimbleUserHalt,
       "nimbleUserHaltFailed": nimbleUserHaltFailed,
       "nimbleCtrlrStandbyUnavailInfo": nimbleCtrlrStandbyUnavailInfo,
       "nimbleCtrlrStandbyUnavailWarn": nimbleCtrlrStandbyUnavailWarn,
       "nimbleCtrlrExceptionWarn": nimbleCtrlrExceptionWarn,
       "nimbleCtrlrExceptionCrit": nimbleCtrlrExceptionCrit,
       "nimbleCtrlrStandbyUnavailWarnTimeDeprecated": nimbleCtrlrStandbyUnavailWarnTimeDeprecated,
       "nimbleCtrlrStandbyUnavailWarnTime": nimbleCtrlrStandbyUnavailWarnTime,
       "nimbleCtrlrTakeoverWarn": nimbleCtrlrTakeoverWarn,
       "nimbleCtrlrFailoverDeprecated": nimbleCtrlrFailoverDeprecated,
       "nimbleCtrlrFailoverDeprecated2": nimbleCtrlrFailoverDeprecated2,
       "nimbleCtrlrWatchdogDisabled": nimbleCtrlrWatchdogDisabled,
       "nimbleCtrlrFailover": nimbleCtrlrFailover,
       "nimbleCtrlrFailoverAttempt": nimbleCtrlrFailoverAttempt,
       "nimbleCtrlrFailoverFail": nimbleCtrlrFailoverFail,
       "nimbleCtrlrFailoverSuccess": nimbleCtrlrFailoverSuccess,
       "nimbleCtrlrRaidAssemblyErr": nimbleCtrlrRaidAssemblyErr,
       "nimbleCtrlrRaidAssemblyDeg": nimbleCtrlrRaidAssemblyDeg,
       "nimbleCtrlrDegradedMode": nimbleCtrlrDegradedMode,
       "nimbleCtrlrRebootUnexpected": nimbleCtrlrRebootUnexpected,
       "nimbleUserHaltArrayFailedDeprecated": nimbleUserHaltArrayFailedDeprecated,
       "nimbleUserRebootArrayFailedDeprecated": nimbleUserRebootArrayFailedDeprecated,
       "nimbleUserHaltArrayFailed": nimbleUserHaltArrayFailed,
       "nimbleUserRebootArrayFailed": nimbleUserRebootArrayFailed,
       "nimbleServiceStarted": nimbleServiceStarted,
       "nimbleServiceDeadRestart": nimbleServiceDeadRestart,
       "nimbleServiceDeadNoRestart": nimbleServiceDeadNoRestart,
       "nimbleServiceCreateTunnelDeprecated": nimbleServiceCreateTunnelDeprecated,
       "nimbleServiceTerminateTunnelDeprecated": nimbleServiceTerminateTunnelDeprecated,
       "nimbleServiceEssentialStoppedDeprecated": nimbleServiceEssentialStoppedDeprecated,
       "nimbleServiceEssentialStopped": nimbleServiceEssentialStopped,
       "nimbleServiceEmailAlertFailedDeprecated": nimbleServiceEmailAlertFailedDeprecated,
       "nimbleServiceEmailAlertFailed": nimbleServiceEmailAlertFailed,
       "nimbleServiceManuallyDisabled": nimbleServiceManuallyDisabled,
       "nimbleServiceCreateTunnel": nimbleServiceCreateTunnel,
       "nimbleServiceTerminateTunnel": nimbleServiceTerminateTunnel,
       "nimbleTestDbg": nimbleTestDbg,
       "nimbleTestInfo": nimbleTestInfo,
       "nimbleTestErr": nimbleTestErr,
       "nimbleTestNot": nimbleTestNot,
       "nimbleTestNoteDeprecated": nimbleTestNoteDeprecated,
       "nimbleTestWarn": nimbleTestWarn,
       "nimbleTestCrit": nimbleTestCrit,
       "nimbleTestNote": nimbleTestNote,
       "nimbleUpdateUnpackFail": nimbleUpdateUnpackFail,
       "nimbleUpdateStartedDeprecated": nimbleUpdateStartedDeprecated,
       "nimbleUpdateRevert": nimbleUpdateRevert,
       "nimbleUpdateSuccessDeprecated": nimbleUpdateSuccessDeprecated,
       "nimbleUpdateRollback": nimbleUpdateRollback,
       "nimbleUpdatePrecheckFail": nimbleUpdatePrecheckFail,
       "nimbleUpdateFailMsg": nimbleUpdateFailMsg,
       "nimbleUpdateUnpackStarted": nimbleUpdateUnpackStarted,
       "nimbleUpdateUnpackDone": nimbleUpdateUnpackDone,
       "nimbleUpdateSwitchRoot": nimbleUpdateSwitchRoot,
       "nimbleUpdateDownloadFailed": nimbleUpdateDownloadFailed,
       "nimbleUpdateFailTmpFsFull": nimbleUpdateFailTmpFsFull,
       "nimbleUpdateFailScratchFsFull": nimbleUpdateFailScratchFsFull,
       "nimbleUpdateFailVarFsFull": nimbleUpdateFailVarFsFull,
       "nimbleUpdateFailConfigFsFull": nimbleUpdateFailConfigFsFull,
       "nimbleUpdateFailUsbFsFull": nimbleUpdateFailUsbFsFull,
       "nimbleUpdatePkgNotFound": nimbleUpdatePkgNotFound,
       "nimbleUpdatePkgWrongSig": nimbleUpdatePkgWrongSig,
       "nimbleUpdatePkgWrongCksum": nimbleUpdatePkgWrongCksum,
       "nimbleUpdateNetDegradeDeprecated": nimbleUpdateNetDegradeDeprecated,
       "nimbleUpdateDisallowSoloDeprecated": nimbleUpdateDisallowSoloDeprecated,
       "nimbleUpdateDisallowSolo": nimbleUpdateDisallowSolo,
       "nimbleUpdateNetDegrade": nimbleUpdateNetDegrade,
       "nimbleUpdateRaidDegrade": nimbleUpdateRaidDegrade,
       "nimbleUpdateStarted": nimbleUpdateStarted,
       "nimbleUpdateSuccess": nimbleUpdateSuccess,
       "nimbleUpdatePkgSignatureCheckFailure": nimbleUpdatePkgSignatureCheckFailure,
       "nimbleUpdatePkgMalformed": nimbleUpdatePkgMalformed,
       "nimbleDownloadDnsFail": nimbleDownloadDnsFail,
       "nimbleAutoDownloadFail": nimbleAutoDownloadFail,
       "nimbleAutoDownloadSuccess": nimbleAutoDownloadSuccess,
       "nimbleUpdateArrayUnreachable": nimbleUpdateArrayUnreachable,
       "nimbleUpdateArrayFailed": nimbleUpdateArrayFailed,
       "nimbleUpdateArrayTimedOut": nimbleUpdateArrayTimedOut,
       "nimbleUpdateIqnConflict": nimbleUpdateIqnConflict,
       "nimbleUpdateNwtVersionOutdated": nimbleUpdateNwtVersionOutdated,
       "nimbleArrayUnreachableDeprecated": nimbleArrayUnreachableDeprecated,
       "nimbleArrayReachableDeprecated": nimbleArrayReachableDeprecated,
       "nimbleArrayUnreachable": nimbleArrayUnreachable,
       "nimbleArrayReachable": nimbleArrayReachable,
       "nimbleUserClearedSysCacheDeprecated": nimbleUserClearedSysCacheDeprecated,
       "nimbleHostTypeMisconfiguredDeprecated": nimbleHostTypeMisconfiguredDeprecated,
       "nimbleHostTypeMisconfigured": nimbleHostTypeMisconfigured,
       "nimbleVolSpcCurWarningUp": nimbleVolSpcCurWarningUp,
       "nimbleVolSpcCurWarningDown": nimbleVolSpcCurWarningDown,
       "nimbleVolSpcCurQuotaUpDeprecated": nimbleVolSpcCurQuotaUpDeprecated,
       "nimbleVolSpcCurQuotaDownDeprecated": nimbleVolSpcCurQuotaDownDeprecated,
       "nimbleVolSpcSnapWarningUp": nimbleVolSpcSnapWarningUp,
       "nimbleVolSpcSnapWarningDown": nimbleVolSpcSnapWarningDown,
       "nimbleVolSpcSnapQuotaUp": nimbleVolSpcSnapQuotaUp,
       "nimbleVolSpcSnapQuotaDown": nimbleVolSpcSnapQuotaDown,
       "nimbleGmVolSpcCurCritUpDeprecated": nimbleGmVolSpcCurCritUpDeprecated,
       "nimbleGmVolSpcCurCritDownDeprecated": nimbleGmVolSpcCurCritDownDeprecated,
       "nimbleGmSnapSpcCurCritUpDeprecated": nimbleGmSnapSpcCurCritUpDeprecated,
       "nimbleGmSnapSpcCurCritDownDeprecated": nimbleGmSnapSpcCurCritDownDeprecated,
       "nimbleGmVolSpcCurQuotaOfflineDeprecated": nimbleGmVolSpcCurQuotaOfflineDeprecated,
       "nimbleGmVolSpcCurQuotaSetDeprecated": nimbleGmVolSpcCurQuotaSetDeprecated,
       "nimbleGmVolSpcSnapQuotaOffline": nimbleGmVolSpcSnapQuotaOffline,
       "nimbleGmVolSpcSnapQuotaSet": nimbleGmVolSpcSnapQuotaSet,
       "nimbleGmVolSpcCurReserveOfflineDeprecated": nimbleGmVolSpcCurReserveOfflineDeprecated,
       "nimbleGmVolSpcCurReserveSetDeprecated": nimbleGmVolSpcCurReserveSetDeprecated,
       "nimbleGmVolSpcSnapReserveOfflineDeprecated": nimbleGmVolSpcSnapReserveOfflineDeprecated,
       "nimbleGmVolSpcSnapReserveSetDeprecated": nimbleGmVolSpcSnapReserveSetDeprecated,
       "nimbleGmVolSpcCurWarningUp": nimbleGmVolSpcCurWarningUp,
       "nimbleGmVolSpcCurWarningDown": nimbleGmVolSpcCurWarningDown,
       "nimbleGmVolSpcCurQuotaUpDeprecated": nimbleGmVolSpcCurQuotaUpDeprecated,
       "nimbleGmVolSpcCurQuotaDownDeprecated": nimbleGmVolSpcCurQuotaDownDeprecated,
       "nimbleGmVolSpcSnapWarningUp": nimbleGmVolSpcSnapWarningUp,
       "nimbleGmVolSpcSnapWarningDown": nimbleGmVolSpcSnapWarningDown,
       "nimbleGmVolSpcSnapQuotaUpDeprecated": nimbleGmVolSpcSnapQuotaUpDeprecated,
       "nimbleGmVolSpcSnapQuotaDownDeprecated": nimbleGmVolSpcSnapQuotaDownDeprecated,
       "nimbleVolAttrSyncDelay": nimbleVolAttrSyncDelay,
       "nimbleGmPoolArrAssgnDeprecated": nimbleGmPoolArrAssgnDeprecated,
       "nimbleGmPoolArrUnassgnDeprecated": nimbleGmPoolArrUnassgnDeprecated,
       "nimbleGmVolSpcCurCritUpUnlimDeprecated": nimbleGmVolSpcCurCritUpUnlimDeprecated,
       "nimbleGmSnapSpcCurCritUpUnlimDeprecated": nimbleGmSnapSpcCurCritUpUnlimDeprecated,
       "nimbleGmVolSpcReserveUpDeprecated": nimbleGmVolSpcReserveUpDeprecated,
       "nimbleGmVolSpcReserveDownDeprecated": nimbleGmVolSpcReserveDownDeprecated,
       "nimbleGmSnapSpcReserveUpDeprecated": nimbleGmSnapSpcReserveUpDeprecated,
       "nimbleGmSnapSpcReserveDownDeprecated": nimbleGmSnapSpcReserveDownDeprecated,
       "nimbleGmPoolMrgDeprecated": nimbleGmPoolMrgDeprecated,
       "nimbleVolAttrSyncSuccess": nimbleVolAttrSyncSuccess,
       "nimbleSnapAttrSyncDelay": nimbleSnapAttrSyncDelay,
       "nimbleSnapAttrSyncSuccess": nimbleSnapAttrSyncSuccess,
       "nimbleGroupAttrSyncDelay": nimbleGroupAttrSyncDelay,
       "nimbleGroupAttrSyncComplete": nimbleGroupAttrSyncComplete,
       "nimbleGlCtrlrAttrSyncDelayDeprecated": nimbleGlCtrlrAttrSyncDelayDeprecated,
       "nimbleGlCtrlrAttrSyncCompleteDeprecated": nimbleGlCtrlrAttrSyncCompleteDeprecated,
       "nimbleGlCtrlrAttrSyncDelay": nimbleGlCtrlrAttrSyncDelay,
       "nimbleGlCtrlrAttrSyncComplete": nimbleGlCtrlrAttrSyncComplete,
       "nimbleVolMoveComplete": nimbleVolMoveComplete,
       "nimbleVolMoveAbortComplete": nimbleVolMoveAbortComplete,
       "nimbleGmPoolArrUnassgnCompleteDeprecated": nimbleGmPoolArrUnassgnCompleteDeprecated,
       "nimbleGmPoolArrUnassgnComplete": nimbleGmPoolArrUnassgnComplete,
       "nimbleGmPoolArrAssgn": nimbleGmPoolArrAssgn,
       "nimbleGmPoolArrUnassgn": nimbleGmPoolArrUnassgn,
       "nimbleGmPoolMrg": nimbleGmPoolMrg,
       "nimbleGmVolSpcCurCritUpNonWritableDeprecated": nimbleGmVolSpcCurCritUpNonWritableDeprecated,
       "nimbleGmVolSpcCurQuotaNonWritableDeprecated": nimbleGmVolSpcCurQuotaNonWritableDeprecated,
       "nimbleGmSnapSpcCurCritUpNonWritableDeprecated": nimbleGmSnapSpcCurCritUpNonWritableDeprecated,
       "nimbleGmVolSpcSnapQuotaNonWritable": nimbleGmVolSpcSnapQuotaNonWritable,
       "nimbleGmVolSpcCurReserveNonWritableDeprecated": nimbleGmVolSpcCurReserveNonWritableDeprecated,
       "nimbleGmVolSpcSnapReserveNonWritableDeprecated": nimbleGmVolSpcSnapReserveNonWritableDeprecated,
       "nimbleEncryptionNotActive": nimbleEncryptionNotActive,
       "nimbleEncryptionMasterKeyRemoved": nimbleEncryptionMasterKeyRemoved,
       "nimbleEncryptionModeSecured": nimbleEncryptionModeSecured,
       "nimbleEncryptionModeAvailable": nimbleEncryptionModeAvailable,
       "nimbleEncryptionMasterKeyCreated": nimbleEncryptionMasterKeyCreated,
       "nimbleEncryptionPassphraseModified": nimbleEncryptionPassphraseModified,
       "nimbleEncryptionCipherModified": nimbleEncryptionCipherModified,
       "nimbleEncryptionScopeModified": nimbleEncryptionScopeModified,
       "nimbleEncryptionActive": nimbleEncryptionActive,
       "nimbleEncryptionSlow": nimbleEncryptionSlow,
       "nimbleEncryptionActiveMasterKeyRemoved": nimbleEncryptionActiveMasterKeyRemoved,
       "nimbleGmVolSerialCollisionOffline": nimbleGmVolSerialCollisionOffline,
       "nimbleGmSnapSerialCollisionOffline": nimbleGmSnapSerialCollisionOffline,
       "nimbleIgrpSyncDelay": nimbleIgrpSyncDelay,
       "nimbleIgrpSyncSuccess": nimbleIgrpSyncSuccess,
       "nimbleGmPinCacheInsufficientDeprecated": nimbleGmPinCacheInsufficientDeprecated,
       "nimbleFolderAttrSyncDelay": nimbleFolderAttrSyncDelay,
       "nimbleFolderAttrSyncSuccess": nimbleFolderAttrSyncSuccess,
       "nimbleGmVolFolderLimitOffline": nimbleGmVolFolderLimitOffline,
       "nimbleGmVolFolderLimitNonWritable": nimbleGmVolFolderLimitNonWritable,
       "nimbleGmFolderUsedSpaceUtilizationCritDeprecated": nimbleGmFolderUsedSpaceUtilizationCritDeprecated,
       "nimbleGmFolderUsedSpaceUtilizationHighDeprecated": nimbleGmFolderUsedSpaceUtilizationHighDeprecated,
       "nimbleGmFolderUsedSpaceUtilizationInfoDeprecated": nimbleGmFolderUsedSpaceUtilizationInfoDeprecated,
       "nimbleGmFolderUsedSpaceUtilizationOkDeprecated": nimbleGmFolderUsedSpaceUtilizationOkDeprecated,
       "nimbleGmFolderUsedSpaceReplicationStopped": nimbleGmFolderUsedSpaceReplicationStopped,
       "nimbleGmFolderUsedSpaceReplicationStoppedUpstreamDeprecated": nimbleGmFolderUsedSpaceReplicationStoppedUpstreamDeprecated,
       "nimbleGmFolderUsedSpaceReplicationOkDeprecated": nimbleGmFolderUsedSpaceReplicationOkDeprecated,
       "nimbleGmVolSpcCurProvisionOffline": nimbleGmVolSpcCurProvisionOffline,
       "nimbleGmVolSpcCurProvisionNonWritable": nimbleGmVolSpcCurProvisionNonWritable,
       "nimbleVolReserveConversionToProvisioningLevel": nimbleVolReserveConversionToProvisioningLevel,
       "nimbleGmFolderUsedSpaceUtilizationCrit": nimbleGmFolderUsedSpaceUtilizationCrit,
       "nimbleGmFolderUsedSpaceUtilizationHigh": nimbleGmFolderUsedSpaceUtilizationHigh,
       "nimbleGmFolderUsedSpaceUtilizationInfo": nimbleGmFolderUsedSpaceUtilizationInfo,
       "nimbleSchedSnapSucceededDeprecated": nimbleSchedSnapSucceededDeprecated,
       "nimbleSchedSnapFailed": nimbleSchedSnapFailed,
       "nimbleSchedSnapSkippedExists": nimbleSchedSnapSkippedExists,
       "nimbleSchedSnapSkippedHandover": nimbleSchedSnapSkippedHandover,
       "nimbleSchedSnapSucceededLagInfoDeprecated": nimbleSchedSnapSucceededLagInfoDeprecated,
       "nimbleSchedSnapFailedVmwareCredentialDeprecated": nimbleSchedSnapFailedVmwareCredentialDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated": nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated": nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionResetDeprecated": nimbleSchedSnapFailedVmwareConnectionResetDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated": nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionSocketDeprecated": nimbleSchedSnapFailedVmwareConnectionSocketDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated": nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated,
       "nimbleSchedSnapFailedVmwareDisabledDeprecated": nimbleSchedSnapFailedVmwareDisabledDeprecated,
       "nimbleSchedSnapFailedVmwareObjectnfDeprecated": nimbleSchedSnapFailedVmwareObjectnfDeprecated,
       "nimbleSchedSnapFailedVmwarePermissionDeprecated": nimbleSchedSnapFailedVmwarePermissionDeprecated,
       "nimbleSchedSnapFailedVmwareUkhostDeprecated": nimbleSchedSnapFailedVmwareUkhostDeprecated,
       "nimbleSchedSnapFailedVmwareEncodingPlainDeprecated": nimbleSchedSnapFailedVmwareEncodingPlainDeprecated,
       "nimbleSchedSnapFailedVmwareNullDeprecated": nimbleSchedSnapFailedVmwareNullDeprecated,
       "nimbleSchedSnapFailedVmwareDcnotfoundDeprecated": nimbleSchedSnapFailedVmwareDcnotfoundDeprecated,
       "nimbleSchedSnapFailedVmwareVolsnemptyDeprecated": nimbleSchedSnapFailedVmwareVolsnemptyDeprecated,
       "nimbleSchedSnapFailedVmwareUnknownDeprecated": nimbleSchedSnapFailedVmwareUnknownDeprecated,
       "nimbleSchedSnapFailedVmwareBsizeDeprecated": nimbleSchedSnapFailedVmwareBsizeDeprecated,
       "nimbleSchedSnapSucceeded": nimbleSchedSnapSucceeded,
       "nimbleSchedSnapSucceededLagInfo": nimbleSchedSnapSucceededLagInfo,
       "nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo": nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo,
       "nimbleSchedSnapFailedVmwareTimeoutDeprecated": nimbleSchedSnapFailedVmwareTimeoutDeprecated,
       "nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated": nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated,
       "nimbleSchedSnapFallback": nimbleSchedSnapFallback,
       "nimbleSchedSnapFailedUnknownReason": nimbleSchedSnapFailedUnknownReason,
       "nimbleSchedSnapFailedVmwarePermissionPerVm": nimbleSchedSnapFailedVmwarePermissionPerVm,
       "nimbleSchedSnapFailedVmwareObjectnfPerVm": nimbleSchedSnapFailedVmwareObjectnfPerVm,
       "nimbleSchedSnapFailedVmwareEncodingPlainPerVm": nimbleSchedSnapFailedVmwareEncodingPlainPerVm,
       "nimbleSchedSnapFailedVmwareNullPerVm": nimbleSchedSnapFailedVmwareNullPerVm,
       "nimbleSchedSnapFailedVmwareDcnotfoundPerVm": nimbleSchedSnapFailedVmwareDcnotfoundPerVm,
       "nimbleSchedSnapFailedVmwareVolsnemptyPerVm": nimbleSchedSnapFailedVmwareVolsnemptyPerVm,
       "nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated": nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated,
       "nimbleSchedSnapFailedVmwareBsizePerVm": nimbleSchedSnapFailedVmwareBsizePerVm,
       "nimbleSchedSnapFailedVmwareDisabledPerVm": nimbleSchedSnapFailedVmwareDisabledPerVm,
       "nimbleSchedSnapFailedVmwareTimeoutPerVm": nimbleSchedSnapFailedVmwareTimeoutPerVm,
       "nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm": nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm,
       "nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm": nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm,
       "nimbleSchedSnapFailedVmwareInvalidVcenter": nimbleSchedSnapFailedVmwareInvalidVcenter,
       "nimbleSchedSnapFailedVmwareBusy": nimbleSchedSnapFailedVmwareBusy,
       "nimbleSchedSnapFailedVssIncompatible": nimbleSchedSnapFailedVssIncompatible,
       "nimbleSchedSnapFailedVmwareCredentialNw": nimbleSchedSnapFailedVmwareCredentialNw,
       "nimbleSchedSnapFailedVmwareConnectionTimeoutNw": nimbleSchedSnapFailedVmwareConnectionTimeoutNw,
       "nimbleSchedSnapFailedVmwareConnectionRefusedNw": nimbleSchedSnapFailedVmwareConnectionRefusedNw,
       "nimbleSchedSnapFailedVmwareConnectionResetNw": nimbleSchedSnapFailedVmwareConnectionResetNw,
       "nimbleSchedSnapFailedVmwareConnectionNorouteNw": nimbleSchedSnapFailedVmwareConnectionNorouteNw,
       "nimbleSchedSnapFailedVmwareConnectionSocketNw": nimbleSchedSnapFailedVmwareConnectionSocketNw,
       "nimbleSchedSnapFailedVmwareConnectionUnreachableNw": nimbleSchedSnapFailedVmwareConnectionUnreachableNw,
       "nimbleSchedSnapFailedVmwareUkhostNw": nimbleSchedSnapFailedVmwareUkhostNw,
       "nimbleSchedSnapFailedVmwareConnectionUnknownNw": nimbleSchedSnapFailedVmwareConnectionUnknownNw,
       "nimbleSchedSnapFailedVmwareTimeoutNw": nimbleSchedSnapFailedVmwareTimeoutNw,
       "nimbleSchedSnapFailedVmwareUnknownNw": nimbleSchedSnapFailedVmwareUnknownNw,
       "nimbleSchedSnapFailedVmwareUnknownPerVm": nimbleSchedSnapFailedVmwareUnknownPerVm,
       "nimbleSchedSnapFailedVmwareQuiescingVmFailed": nimbleSchedSnapFailedVmwareQuiescingVmFailed,
       "nimbleSchedSnapFailedVmwareLeftoverSnapshot": nimbleSchedSnapFailedVmwareLeftoverSnapshot,
       "nimbleSchedSnapFailedGenericConnectionTimeoutNw": nimbleSchedSnapFailedGenericConnectionTimeoutNw,
       "nimbleSchedSnapFailedGenericConnectionNorouteNw": nimbleSchedSnapFailedGenericConnectionNorouteNw,
       "nimbleSchedSnapFailedGenericConnectionRefusedNw": nimbleSchedSnapFailedGenericConnectionRefusedNw,
       "nimbleSchedSnapFailedGenericConnectionSocketNw": nimbleSchedSnapFailedGenericConnectionSocketNw,
       "nimbleSchedSnapFailedGenericCredentialNw": nimbleSchedSnapFailedGenericCredentialNw,
       "nimbleSchedSnapFailedGenericUkhostNw": nimbleSchedSnapFailedGenericUkhostNw,
       "nimbleSchedSnapFailedGenericConnectionUnknownNw": nimbleSchedSnapFailedGenericConnectionUnknownNw,
       "nimbleSchedSnapFailedGenericAgentError": nimbleSchedSnapFailedGenericAgentError,
       "nimbleSchedSnapFailedGenericTimeoutNw": nimbleSchedSnapFailedGenericTimeoutNw,
       "nimbleSchedSnapFailedGenericBusy": nimbleSchedSnapFailedGenericBusy,
       "nimbleSchedSnapFailedVssWriterFailure": nimbleSchedSnapFailedVssWriterFailure,
       "nimbleSchedSnapFailedVssNonTerminatingWriterFailure": nimbleSchedSnapFailedVssNonTerminatingWriterFailure,
       "nimbleSchedSnapFailedVssVolcollConfigError": nimbleSchedSnapFailedVssVolcollConfigError,
       "nimbleSchedSnapFailedVssSnapVerificationError": nimbleSchedSnapFailedVssSnapVerificationError,
       "nimbleSchedSnapFailedVssPreviousSnapInProgress": nimbleSchedSnapFailedVssPreviousSnapInProgress,
       "nimbleSchedSnapFailedVssSnapFailure": nimbleSchedSnapFailedVssSnapFailure,
       "nimbleSchedSnapFailedVssBadCookie": nimbleSchedSnapFailedVssBadCookie,
       "nimbleSchedSnapFailedGenericUnknownNw": nimbleSchedSnapFailedGenericUnknownNw,
       "nimbleVssVolcollConfigWarn": nimbleVssVolcollConfigWarn,
       "nimbleApplicationServerLoginFailed": nimbleApplicationServerLoginFailed,
       "nimbleApplicationServerLoginSucceeded": nimbleApplicationServerLoginSucceeded,
       "nimbleVvolManagementConnectionDisrupted": nimbleVvolManagementConnectionDisrupted,
       "nimbleVvolManagementConnectionReestablished": nimbleVvolManagementConnectionReestablished,
       "nimbleGmSpaceReserveWarnUpDeprecated": nimbleGmSpaceReserveWarnUpDeprecated,
       "nimbleGmSpaceReserveWarnDownDeprecated": nimbleGmSpaceReserveWarnDownDeprecated,
       "nimbleGmSpaceReserveCritUpDeprecated": nimbleGmSpaceReserveCritUpDeprecated,
       "nimbleGmSpaceReserveCritDownDeprecated": nimbleGmSpaceReserveCritDownDeprecated,
       "nimbleGmSpaceUtilizationOk": nimbleGmSpaceUtilizationOk,
       "nimbleGmSpaceUtilizationInfo": nimbleGmSpaceUtilizationInfo,
       "nimbleGmSpaceUtilizationHigh": nimbleGmSpaceUtilizationHigh,
       "nimbleGmSpaceUtilizationCrit": nimbleGmSpaceUtilizationCrit,
       "nimbleGmPoolSpaceReserveWarnUpDeprecated2": nimbleGmPoolSpaceReserveWarnUpDeprecated2,
       "nimbleGmPoolSpaceReserveWarnDownDeprecated2": nimbleGmPoolSpaceReserveWarnDownDeprecated2,
       "nimbleGmPoolSpaceReserveCritUpDeprecated2": nimbleGmPoolSpaceReserveCritUpDeprecated2,
       "nimbleGmPoolSpaceReserveCritDownDeprecated2": nimbleGmPoolSpaceReserveCritDownDeprecated2,
       "nimbleGmPoolSpaceUtilizationOkDeprecated": nimbleGmPoolSpaceUtilizationOkDeprecated,
       "nimbleGmPoolSpaceUtilizationInfoDeprecated": nimbleGmPoolSpaceUtilizationInfoDeprecated,
       "nimbleGmPoolSpaceUtilizationHighDeprecated": nimbleGmPoolSpaceUtilizationHighDeprecated,
       "nimbleGmPoolSpaceUtilizationCritDeprecated": nimbleGmPoolSpaceUtilizationCritDeprecated,
       "nimbleGmPoolSpaceReserveWarnUpDeprecated": nimbleGmPoolSpaceReserveWarnUpDeprecated,
       "nimbleGmPoolSpaceReserveWarnDownDeprecated": nimbleGmPoolSpaceReserveWarnDownDeprecated,
       "nimbleGmPoolSpaceReserveCritUpDeprecated": nimbleGmPoolSpaceReserveCritUpDeprecated,
       "nimbleGmPoolSpaceReserveCritDownDeprecated": nimbleGmPoolSpaceReserveCritDownDeprecated,
       "nimbleGmPoolSpaceUtilizationOk": nimbleGmPoolSpaceUtilizationOk,
       "nimbleGmPoolSpaceUtilizationInfo": nimbleGmPoolSpaceUtilizationInfo,
       "nimbleGmPoolSpaceUtilizationHigh": nimbleGmPoolSpaceUtilizationHigh,
       "nimbleGmPoolSpaceUtilizationCrit": nimbleGmPoolSpaceUtilizationCrit,
       "nimbleGmVolSpcCurCritUp": nimbleGmVolSpcCurCritUp,
       "nimbleGmVolSpcCurCritDown": nimbleGmVolSpcCurCritDown,
       "nimbleGmVolSpcCurLimitOffline": nimbleGmVolSpcCurLimitOffline,
       "nimbleGmVolSpcCurLimitUp": nimbleGmVolSpcCurLimitUp,
       "nimbleGmVolSpcCurLimitDown": nimbleGmVolSpcCurLimitDown,
       "nimbleGmVolSpcCurCritUpUnlim": nimbleGmVolSpcCurCritUpUnlim,
       "nimbleGmVolSpcCurCritUpNonWritable": nimbleGmVolSpcCurCritUpNonWritable,
       "nimbleGmVolSpcCurLimitNonWritable": nimbleGmVolSpcCurLimitNonWritable,
       "nimbleGmPoolSpaceProvisionWarnUp": nimbleGmPoolSpaceProvisionWarnUp,
       "nimbleGmPoolSpaceProvisionWarnDown": nimbleGmPoolSpaceProvisionWarnDown,
       "nimbleGmPoolSpaceProvisionCritUp": nimbleGmPoolSpaceProvisionCritUp,
       "nimbleGmPoolSpaceProvisionCritDownDeprecated": nimbleGmPoolSpaceProvisionCritDownDeprecated,
       "nimbleGmPoolSpaceProvisionCritDown": nimbleGmPoolSpaceProvisionCritDown,
       "nimbleLimitMaxOverDeprecated": nimbleLimitMaxOverDeprecated,
       "nimbleLimitMaxUnderDeprecated": nimbleLimitMaxUnderDeprecated,
       "nimbleLimitWarnOverDeprecated": nimbleLimitWarnOverDeprecated,
       "nimbleLimitWarnUnderDeprecated": nimbleLimitWarnUnderDeprecated,
       "nimbleLimitMaxOverWithContextDeprecated": nimbleLimitMaxOverWithContextDeprecated,
       "nimbleLimitMaxUnderWithContextDeprecated": nimbleLimitMaxUnderWithContextDeprecated,
       "nimbleLimitWarnOverWithContextDeprecated": nimbleLimitWarnOverWithContextDeprecated,
       "nimbleLimitWarnUnderWithContextDeprecated": nimbleLimitWarnUnderWithContextDeprecated,
       "nimbleLimitMaxOver": nimbleLimitMaxOver,
       "nimbleLimitMaxUnder": nimbleLimitMaxUnder,
       "nimbleLimitWarnOver": nimbleLimitWarnOver,
       "nimbleLimitWarnUnder": nimbleLimitWarnUnder,
       "nimbleLimitMaxOverWithContext": nimbleLimitMaxOverWithContext,
       "nimbleLimitMaxUnderWithContext": nimbleLimitMaxUnderWithContext,
       "nimbleLimitWarnOverWithContext": nimbleLimitWarnOverWithContext,
       "nimbleLimitWarnUnderWithContext": nimbleLimitWarnUnderWithContext,
       "nimbleGmFolderUsedSpaceUtilizationOk": nimbleGmFolderUsedSpaceUtilizationOk,
       "nimbleGmFolderUsedSpaceReplicationStoppedUpstream": nimbleGmFolderUsedSpaceReplicationStoppedUpstream,
       "nimbleGmFolderUsedSpaceReplicationOk": nimbleGmFolderUsedSpaceReplicationOk,
       "nimbleReplSnapcollSucceeded": nimbleReplSnapcollSucceeded,
       "nimbleReplSnapcollDelayedInfo": nimbleReplSnapcollDelayedInfo,
       "nimbleReplSnapcollDelayedWarn": nimbleReplSnapcollDelayedWarn,
       "nimbleReplPartnerSyncFail": nimbleReplPartnerSyncFail,
       "nimbleReplBranchPinned": nimbleReplBranchPinned,
       "nimbleReplHandoverCompletedDeprecated": nimbleReplHandoverCompletedDeprecated,
       "nimbleReplMultiArrayGroup": nimbleReplMultiArrayGroup,
       "nimbleReplPartnerMisconfiguration": nimbleReplPartnerMisconfiguration,
       "nimbleReplSnapshotCorrectedDeprecated": nimbleReplSnapshotCorrectedDeprecated,
       "nimbleReplCbrRequestedDeprecated": nimbleReplCbrRequestedDeprecated,
       "nimbleReplCbrNeeded": nimbleReplCbrNeeded,
       "nimbleReplSnapshotCorrectedDeprecated2": nimbleReplSnapshotCorrectedDeprecated2,
       "nimbleReplCbrRequestedDeprecated2": nimbleReplCbrRequestedDeprecated2,
       "nimbleReplPartnerAuthFailDeprecated": nimbleReplPartnerAuthFailDeprecated,
       "nimbleReplSnapshotCorrected": nimbleReplSnapshotCorrected,
       "nimbleReplCbrRequested": nimbleReplCbrRequested,
       "nimbleReplPartnerAuthFail": nimbleReplPartnerAuthFail,
       "nimbleReplVolumeResynchronize": nimbleReplVolumeResynchronize,
       "nimbleReplHandoverAbortedDeprecated": nimbleReplHandoverAbortedDeprecated,
       "nimbleReplHandoverCompletedOfflineDeprecated": nimbleReplHandoverCompletedOfflineDeprecated,
       "nimbleReplHandoverAbortedOfflineDeprecated": nimbleReplHandoverAbortedOfflineDeprecated,
       "nimbleReplProtpolDeletionFailedDeprecated": nimbleReplProtpolDeletionFailedDeprecated,
       "nimbleReplBranchpointTrimmedNocommonDeprecated": nimbleReplBranchpointTrimmedNocommonDeprecated,
       "nimbleReplBranchpointTrimmedCommonDeprecated": nimbleReplBranchpointTrimmedCommonDeprecated,
       "nimbleReplVolumeAutoResynchronize": nimbleReplVolumeAutoResynchronize,
       "nimbleReplVolumeCorrectedNoErr": nimbleReplVolumeCorrectedNoErr,
       "nimbleReplPartnerUnsupportedVssAppId": nimbleReplPartnerUnsupportedVssAppId,
       "nimbleReplBranchInconsistentDeprecated": nimbleReplBranchInconsistentDeprecated,
       "nimbleReplPoolPartnerCreated": nimbleReplPoolPartnerCreated,
       "nimbleReplPartnerOosyncDeprecated": nimbleReplPartnerOosyncDeprecated,
       "nimbleReplPartnerInsyncDeprecated": nimbleReplPartnerInsyncDeprecated,
       "nimbleReplVolcolOosyncDeprecated": nimbleReplVolcolOosyncDeprecated,
       "nimbleReplVolcolInsyncDeprecated": nimbleReplVolcolInsyncDeprecated,
       "nimbleReplSrepVolumeHasAcls": nimbleReplSrepVolumeHasAcls,
       "nimbleReplSrepVolumeAclsRemovedDeprecated": nimbleReplSrepVolumeAclsRemovedDeprecated,
       "nimbleReplSrepProtpolMgmtOosyncDeprecated": nimbleReplSrepProtpolMgmtOosyncDeprecated,
       "nimbleReplPoolPartnerCreationFailed": nimbleReplPoolPartnerCreationFailed,
       "nimbleReplSrepVolumeDnstrOnline": nimbleReplSrepVolumeDnstrOnline,
       "nimbleReplSrepVolumeDnstrOfflineDeprecated": nimbleReplSrepVolumeDnstrOfflineDeprecated,
       "nimbleReplSrepVolumeDnstrOnlineRenamedDeprecated": nimbleReplSrepVolumeDnstrOnlineRenamedDeprecated,
       "nimbleReplSrepVolumeDnstrSizeMismatch": nimbleReplSrepVolumeDnstrSizeMismatch,
       "nimbleReplSrepVolumeDnstrResized": nimbleReplSrepVolumeDnstrResized,
       "nimbleReplSrepVolumeDnstrSizeMismatchDeletedDeprecated": nimbleReplSrepVolumeDnstrSizeMismatchDeletedDeprecated,
       "nimbleReplSrepVolumeDnstrSizeMismatchRenamedDeprecated": nimbleReplSrepVolumeDnstrSizeMismatchRenamedDeprecated,
       "nimbleReplSrepVolumeDnstrAgentTypeMismatch": nimbleReplSrepVolumeDnstrAgentTypeMismatch,
       "nimbleReplSrepVolumeDnstrAgentTypeUpdated": nimbleReplSrepVolumeDnstrAgentTypeUpdated,
       "nimbleReplSrepVolumeDnstrAgentTypeMismatchDeletedDeprecated": nimbleReplSrepVolumeDnstrAgentTypeMismatchDeletedDeprecated,
       "nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamedDeprecated": nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamedDeprecated,
       "nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeprecated": nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeprecated,
       "nimbleReplSrepVolumeDnstrIscsiTargetScopeUpdated": nimbleReplSrepVolumeDnstrIscsiTargetScopeUpdated,
       "nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeletedDeprecated": nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeletedDeprecated,
       "nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamedDeprecated": nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamedDeprecated,
       "nimbleReplSrepVolumeDnstrNoCommonSnap": nimbleReplSrepVolumeDnstrNoCommonSnap,
       "nimbleReplSrepVolumeDnstrNoCommonSnapDeletedDeprecated": nimbleReplSrepVolumeDnstrNoCommonSnapDeletedDeprecated,
       "nimbleReplSrepVolumeDnstrNoCommonSnapRenamedDeprecated": nimbleReplSrepVolumeDnstrNoCommonSnapRenamedDeprecated,
       "nimbleReplSrepAsoSwitchoverSuccessfulDeprecated": nimbleReplSrepAsoSwitchoverSuccessfulDeprecated,
       "nimbleReplSrepAsoSwitchoverBlockedDeprecated": nimbleReplSrepAsoSwitchoverBlockedDeprecated,
       "nimbleReplSrepProtpolMgmtOosync": nimbleReplSrepProtpolMgmtOosync,
       "nimbleReplSrepVolumeDnstrOffline": nimbleReplSrepVolumeDnstrOffline,
       "nimbleReplSrepVolumeDnstrOnlineRenamed": nimbleReplSrepVolumeDnstrOnlineRenamed,
       "nimbleReplSrepVolumeDnstrSizeMismatchDeleted": nimbleReplSrepVolumeDnstrSizeMismatchDeleted,
       "nimbleReplSrepVolumeDnstrSizeMismatchRenamed": nimbleReplSrepVolumeDnstrSizeMismatchRenamed,
       "nimbleReplSrepVolumeDnstrAgentTypeMismatchDeleted": nimbleReplSrepVolumeDnstrAgentTypeMismatchDeleted,
       "nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamed": nimbleReplSrepVolumeDnstrAgentTypeMismatchRenamed,
       "nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalid": nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalid,
       "nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeleted": nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidDeleted,
       "nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamed": nimbleReplSrepVolumeDnstrIscsiTargetScopeInvalidRenamed,
       "nimbleReplSrepVolumeDnstrNoCommonSnapDeleted": nimbleReplSrepVolumeDnstrNoCommonSnapDeleted,
       "nimbleReplSrepVolumeDnstrNoCommonSnapRenamed": nimbleReplSrepVolumeDnstrNoCommonSnapRenamed,
       "nimbleReplSrepAsoSwitchoverBlocked": nimbleReplSrepAsoSwitchoverBlocked,
       "nimbleReplSrepVolumeAclsRemoved": nimbleReplSrepVolumeAclsRemoved,
       "nimbleReplPartnerOosync": nimbleReplPartnerOosync,
       "nimbleReplPartnerInsync": nimbleReplPartnerInsync,
       "nimbleReplVolcolOosync": nimbleReplVolcolOosync,
       "nimbleReplVolcolInsync": nimbleReplVolcolInsync,
       "nimbleReplSrepAsoSwitchoverSuccessful": nimbleReplSrepAsoSwitchoverSuccessful,
       "nimbleReplSrepProtpolRecmFreqSchedMissing": nimbleReplSrepProtpolRecmFreqSchedMissing,
       "nimbleReplSrepProtpolRecmFreqSchedImplemented": nimbleReplSrepProtpolRecmFreqSchedImplemented,
       "nimbleReplSrepProtpolRecmFreqNoReplVols": nimbleReplSrepProtpolRecmFreqNoReplVols,
       "nimbleReplBranchInconsistent": nimbleReplBranchInconsistent,
       "nimbleReplSnapshotCorrectedFromBranchInconsistency": nimbleReplSnapshotCorrectedFromBranchInconsistency,
       "nimbleReplSnapshotCorrectedFromBranchInconsistencyNoErr": nimbleReplSnapshotCorrectedFromBranchInconsistencyNoErr,
       "nimbleReplHandoverCompleted": nimbleReplHandoverCompleted,
       "nimbleReplHandoverAborted": nimbleReplHandoverAborted,
       "nimbleReplHandoverCompletedOffline": nimbleReplHandoverCompletedOffline,
       "nimbleReplHandoverAbortedOffline": nimbleReplHandoverAbortedOffline,
       "nimbleReplProtpolDeletionFailed": nimbleReplProtpolDeletionFailed,
       "nimbleReplBranchpointTrimmedNocommon": nimbleReplBranchpointTrimmedNocommon,
       "nimbleReplBranchpointTrimmedCommon": nimbleReplBranchpointTrimmedCommon,
       "nimbleOvertempShutdownDeprecated": nimbleOvertempShutdownDeprecated,
       "nimbleCtrlrOvertempDeprecated": nimbleCtrlrOvertempDeprecated,
       "nimbleBackplaneOvertempDeprecated": nimbleBackplaneOvertempDeprecated,
       "nimbleHsFlashSizeUnsupported": nimbleHsFlashSizeUnsupported,
       "nimbleHsFlashSizeNormal": nimbleHsFlashSizeNormal,
       "nimbleIscsiErroneousItorConnsDeprecated": nimbleIscsiErroneousItorConnsDeprecated,
       "nimbleDiskFailedCrit": nimbleDiskFailedCrit,
       "nimbleDiskFailed": nimbleDiskFailed,
       "nimbleDiskAbsent": nimbleDiskAbsent,
       "nimbleDiskAdded": nimbleDiskAdded,
       "nimbleDiskRemoved": nimbleDiskRemoved,
       "nimbleSsdFailed": nimbleSsdFailed,
       "nimbleSsdAbsent": nimbleSsdAbsent,
       "nimbleSsdAdded": nimbleSsdAdded,
       "nimbleSsdRemoved": nimbleSsdRemoved,
       "nimbleDiskInvalidLabel": nimbleDiskInvalidLabel,
       "nimbleSsdInvalidLabel": nimbleSsdInvalidLabel,
       "nimbleDiskSizeMismatchDeprecated": nimbleDiskSizeMismatchDeprecated,
       "nimbleHddFailedV2": nimbleHddFailedV2,
       "nimbleHddAbsentV2": nimbleHddAbsentV2,
       "nimbleHddAddedV2": nimbleHddAddedV2,
       "nimbleHddRemovedV2": nimbleHddRemovedV2,
       "nimbleSsdFailedV2": nimbleSsdFailedV2,
       "nimbleSsdAbsentV2": nimbleSsdAbsentV2,
       "nimbleSsdAddedV2": nimbleSsdAddedV2,
       "nimbleSsdRemovedV2": nimbleSsdRemovedV2,
       "nimbleSsdLastOne": nimbleSsdLastOne,
       "nimbleHddFailedV3": nimbleHddFailedV3,
       "nimbleHddAddedV3": nimbleHddAddedV3,
       "nimbleHddRemovedV3": nimbleHddRemovedV3,
       "nimbleSsdFailedV3": nimbleSsdFailedV3,
       "nimbleSsdAddedV3": nimbleSsdAddedV3,
       "nimbleSsdRemovedV3": nimbleSsdRemovedV3,
       "nimbleDiskSizeMismatchV2": nimbleDiskSizeMismatchV2,
       "nimbleSsdSizeMismatchV2": nimbleSsdSizeMismatchV2,
       "nimbleHddFailedAfsDeprecated": nimbleHddFailedAfsDeprecated,
       "nimbleHddFailedAfs": nimbleHddFailedAfs,
       "nimbleSsdNone": nimbleSsdNone,
       "nimbleDiskMissing": nimbleDiskMissing,
       "nimbleDiskDiagRemoved": nimbleDiskDiagRemoved,
       "nimbleDfcSsdFailed": nimbleDfcSsdFailed,
       "nimbleDfcSsdAdded": nimbleDfcSsdAdded,
       "nimbleDfcSsdRemoved": nimbleDfcSsdRemoved,
       "nimbleDfcDiskSizeMismatch": nimbleDfcDiskSizeMismatch,
       "nimbleDfcSsdSizeMismatch": nimbleDfcSsdSizeMismatch,
       "nimbleDfcHddFailedAfs": nimbleDfcHddFailedAfs,
       "nimbleDfcDiskDiagRemoved": nimbleDfcDiskDiagRemoved,
       "nimbleDfcSsdAbsent": nimbleDfcSsdAbsent,
       "nimbleSsdAbsentV3": nimbleSsdAbsentV3,
       "nimbleHddAbsentV3": nimbleHddAbsentV3,
       "nimbleIposerFwUpdateStart": nimbleIposerFwUpdateStart,
       "nimbleIposerFwUpdateSucceed": nimbleIposerFwUpdateSucceed,
       "nimbleIposerFwUpdateFail": nimbleIposerFwUpdateFail,
       "nimbleScmFailedV3": nimbleScmFailedV3,
       "nimbleScmAddedV3": nimbleScmAddedV3,
       "nimbleScmAbsentV3": nimbleScmAbsentV3,
       "nimbleAfturboWithScm": nimbleAfturboWithScm,
       "nimbleAfturboDegradeToAfa": nimbleAfturboDegradeToAfa,
       "nimbleScmHighTemperatureV3": nimbleScmHighTemperatureV3,
       "nimbleScmCrithighTemperatureV3": nimbleScmCrithighTemperatureV3,
       "nimbleScmTemperatureCritOk": nimbleScmTemperatureCritOk,
       "nimbleScmTemperatureOk": nimbleScmTemperatureOk,
       "nimbleIpIfDown": nimbleIpIfDown,
       "nimbleIpIfUp": nimbleIpIfUp,
       "nimbleIpIfGroupUnavailDeprecated": nimbleIpIfGroupUnavailDeprecated,
       "nimbleIpIfDataUnavailDeprecated": nimbleIpIfDataUnavailDeprecated,
       "nimbleIpIfCantFailoverDeprecated": nimbleIpIfCantFailoverDeprecated,
       "nimbleSubnetNicMigrationDeprecated": nimbleSubnetNicMigrationDeprecated,
       "nimbleSubnetNicMissingDeprecated": nimbleSubnetNicMissingDeprecated,
       "nimbleIpNicMigrationDeprecated": nimbleIpNicMigrationDeprecated,
       "nimbleIpNicMissingDeprecated": nimbleIpNicMissingDeprecated,
       "nimbleRouteNicMigrationDeprecated": nimbleRouteNicMigrationDeprecated,
       "nimbleRouteNicMissingDeprecated": nimbleRouteNicMissingDeprecated,
       "nimbleIpIfFailoverDeprecated": nimbleIpIfFailoverDeprecated,
       "nimbleIpDupFound": nimbleIpDupFound,
       "nimbleIpIfDiscoveryUnavailDeprecated": nimbleIpIfDiscoveryUnavailDeprecated,
       "nimbleIpIfTargetUnavailDeprecated": nimbleIpIfTargetUnavailDeprecated,
       "nimbleIpIfGroupUnavail": nimbleIpIfGroupUnavail,
       "nimbleIpIfDiscoveryUnavail": nimbleIpIfDiscoveryUnavail,
       "nimbleIpIfTargetUnavail": nimbleIpIfTargetUnavail,
       "nimbleIpIfDataUnavail": nimbleIpIfDataUnavail,
       "nimbleIpIfIscsiDataUnavail": nimbleIpIfIscsiDataUnavail,
       "nimbleIpIfClusterDataUnavail": nimbleIpIfClusterDataUnavail,
       "nimbleUnresponsiveNicDetected": nimbleUnresponsiveNicDetected,
       "nimbleIpIfCantFailoverDeprecated2": nimbleIpIfCantFailoverDeprecated2,
       "nimbleIpIfCantFailover": nimbleIpIfCantFailover,
       "nimbleNicMigrationFailed": nimbleNicMigrationFailed,
       "nimbleNicPortUp": nimbleNicPortUp,
       "nimbleNicPortDown": nimbleNicPortDown,
       "nimbleSensorLinearWarn": nimbleSensorLinearWarn,
       "nimbleSensorLinearClear": nimbleSensorLinearClear,
       "nimbleSensorBoolWarn": nimbleSensorBoolWarn,
       "nimbleSensorBoolClear": nimbleSensorBoolClear,
       "nimbleSensorDoesNotExist": nimbleSensorDoesNotExist,
       "nimbleNvramBattDisabled": nimbleNvramBattDisabled,
       "nimbleNvramBattDisabledCrit": nimbleNvramBattDisabledCrit,
       "nimbleNvramBattOk": nimbleNvramBattOk,
       "nimbleTempSensorHighDeprecated": nimbleTempSensorHighDeprecated,
       "nimbleTempSensorLowDeprecated": nimbleTempSensorLowDeprecated,
       "nimbleTempSensorOkDeprecated": nimbleTempSensorOkDeprecated,
       "nimbleTempSensorMissingDeprecated": nimbleTempSensorMissingDeprecated,
       "nimbleTempSensorOperationalDeprecated": nimbleTempSensorOperationalDeprecated,
       "nimbleFanSensorHighDeprecated": nimbleFanSensorHighDeprecated,
       "nimbleFanSensorLowDeprecated": nimbleFanSensorLowDeprecated,
       "nimbleFanSensorOkDeprecated": nimbleFanSensorOkDeprecated,
       "nimbleFanSensorStoppedDeprecated": nimbleFanSensorStoppedDeprecated,
       "nimbleFanSensorMissingDeprecated": nimbleFanSensorMissingDeprecated,
       "nimblePwrSupplySensorFailDeprecated": nimblePwrSupplySensorFailDeprecated,
       "nimblePwrSupplySensorMissingDeprecated": nimblePwrSupplySensorMissingDeprecated,
       "nimblePwrSupplySensorOkDeprecated": nimblePwrSupplySensorOkDeprecated,
       "nimbleTempSensorHighDeprecated2": nimbleTempSensorHighDeprecated2,
       "nimbleTempSensorLowDeprecated2": nimbleTempSensorLowDeprecated2,
       "nimbleTempSensorOkDeprecated2": nimbleTempSensorOkDeprecated2,
       "nimbleTempSensorMissingDeprecated2": nimbleTempSensorMissingDeprecated2,
       "nimbleTempSensorOperationalDeprecated2": nimbleTempSensorOperationalDeprecated2,
       "nimbleFanSensorHighDeprecated2": nimbleFanSensorHighDeprecated2,
       "nimbleFanSensorLowDeprecated2": nimbleFanSensorLowDeprecated2,
       "nimbleFanSensorOkDeprecated2": nimbleFanSensorOkDeprecated2,
       "nimbleFanSensorStoppedDeprecated2": nimbleFanSensorStoppedDeprecated2,
       "nimbleFanSensorMissingDeprecated2": nimbleFanSensorMissingDeprecated2,
       "nimblePwrSupplySensorFailDeprecated2": nimblePwrSupplySensorFailDeprecated2,
       "nimblePwrSupplySensorMissingDeprecated2": nimblePwrSupplySensorMissingDeprecated2,
       "nimblePwrSupplySensorOkDeprecated2": nimblePwrSupplySensorOkDeprecated2,
       "nimbleTempSensorHighDeprecated3": nimbleTempSensorHighDeprecated3,
       "nimbleTempSensorLowDeprecated3": nimbleTempSensorLowDeprecated3,
       "nimbleTempSensorOkDeprecated3": nimbleTempSensorOkDeprecated3,
       "nimbleTempSensorMissingDeprecated3": nimbleTempSensorMissingDeprecated3,
       "nimbleTempSensorOperationalDeprecated3": nimbleTempSensorOperationalDeprecated3,
       "nimbleFanSensorHigh": nimbleFanSensorHigh,
       "nimbleFanSensorLow": nimbleFanSensorLow,
       "nimbleFanSensorOk": nimbleFanSensorOk,
       "nimbleFanSensorStopped": nimbleFanSensorStopped,
       "nimbleFanSensorMissing": nimbleFanSensorMissing,
       "nimblePwrSupplySensorFail": nimblePwrSupplySensorFail,
       "nimblePwrSupplySensorMissing": nimblePwrSupplySensorMissing,
       "nimblePwrSupplySensorOk": nimblePwrSupplySensorOk,
       "nimblePsuIncorrect": nimblePsuIncorrect,
       "nimblePsuOk": nimblePsuOk,
       "nimblePwrSupplySensorAcLoss": nimblePwrSupplySensorAcLoss,
       "nimblePwrSupplySensorFailed": nimblePwrSupplySensorFailed,
       "nimbleTempSensorLow": nimbleTempSensorLow,
       "nimbleTempSensorOk": nimbleTempSensorOk,
       "nimbleTempSensorMissing": nimbleTempSensorMissing,
       "nimbleTempSensorOperational": nimbleTempSensorOperational,
       "nimbleRaidDegraded": nimbleRaidDegraded,
       "nimbleRaidRebuildStart": nimbleRaidRebuildStart,
       "nimbleRaidRebuildDone": nimbleRaidRebuildDone,
       "nimbleRaidRebuildFailRead": nimbleRaidRebuildFailRead,
       "nimbleRaidRebuildFail": nimbleRaidRebuildFail,
       "nimbleRaidDisksMissing": nimbleRaidDisksMissing,
       "nimbleRaidSpare": nimbleRaidSpare,
       "nimbleRaidAssemblyFailed": nimbleRaidAssemblyFailed,
       "nimbleRaidDegradedV2": nimbleRaidDegradedV2,
       "nimbleRaidRebuildStartV2": nimbleRaidRebuildStartV2,
       "nimbleRaidRebuildDoneV2": nimbleRaidRebuildDoneV2,
       "nimbleRaidRebuildFailReadV2": nimbleRaidRebuildFailReadV2,
       "nimbleRaidRebuildFailV2": nimbleRaidRebuildFailV2,
       "nimbleRaidDisksMissingV2": nimbleRaidDisksMissingV2,
       "nimbleRaidSpareV2": nimbleRaidSpareV2,
       "nimbleRaidAssemblyFailedV2": nimbleRaidAssemblyFailedV2,
       "nimbleRaidRebuildScheduledV2": nimbleRaidRebuildScheduledV2,
       "nimbleRaidRebuildStopV2": nimbleRaidRebuildStopV2,
       "nimbleRaidRedundancy": nimbleRaidRedundancy,
       "nimbleIscsiMultiInitiatorDeprecated": nimbleIscsiMultiInitiatorDeprecated,
       "nimbleIscsiConnHardLimitDeprecated1": nimbleIscsiConnHardLimitDeprecated1,
       "nimbleIscsiUnalignedOpsDeprecated": nimbleIscsiUnalignedOpsDeprecated,
       "nimbleIscsiMultiInitiator": nimbleIscsiMultiInitiator,
       "nimbleIscsiConnHardLimitDeprecated2": nimbleIscsiConnHardLimitDeprecated2,
       "nimbleIscsiUnalignedOps": nimbleIscsiUnalignedOps,
       "nimbleIscsiConnHardLimit": nimbleIscsiConnHardLimit,
       "nimbleIscsiErroneousItorConns": nimbleIscsiErroneousItorConns,
       "nimbleNvramBattCharging": nimbleNvramBattCharging,
       "nimbleNvramBattCharged": nimbleNvramBattCharged,
       "nimbleNvramFpgaVersion": nimbleNvramFpgaVersion,
       "nimbleNvramMbeDeprecated": nimbleNvramMbeDeprecated,
       "nimbleNvramSbeDeprecated": nimbleNvramSbeDeprecated,
       "nimbleNvramMbe": nimbleNvramMbe,
       "nimbleNvramSbe": nimbleNvramSbe,
       "nimbleNvdimmReservedBlocksWarn": nimbleNvdimmReservedBlocksWarn,
       "nimbleNvdimmReservedBlocksCrit": nimbleNvdimmReservedBlocksCrit,
       "nimbleNvdimmUltracapDischargedDeprecated": nimbleNvdimmUltracapDischargedDeprecated,
       "nimbleNtbBadLink": nimbleNtbBadLink,
       "nimbleNvdimmUltracapDischargedDeprecated1": nimbleNvdimmUltracapDischargedDeprecated1,
       "nimbleNvramMissing": nimbleNvramMissing,
       "nimbleNvdimmUltracapDischargedDeprecated2": nimbleNvdimmUltracapDischargedDeprecated2,
       "nimbleEncryptionKeysMissing": nimbleEncryptionKeysMissing,
       "nimbleNvdimmUltracapDischarged": nimbleNvdimmUltracapDischarged,
       "nimbleShelfCtrlrSide": nimbleShelfCtrlrSide,
       "nimbleShelfSesErr": nimbleShelfSesErr,
       "nimbleShelfDiskSasLink": nimbleShelfDiskSasLink,
       "nimbleShelfDiskCountDeprecated": nimbleShelfDiskCountDeprecated,
       "nimbleShelfInvalidEeprom": nimbleShelfInvalidEeprom,
       "nimbleShelfWrongSasPortDeprecated": nimbleShelfWrongSasPortDeprecated,
       "nimbleShelfSasLink": nimbleShelfSasLink,
       "nimbleShelfSasExpErr": nimbleShelfSasExpErr,
       "nimbleShelfCtrlrLoop": nimbleShelfCtrlrLoop,
       "nimbleShelfMissing": nimbleShelfMissing,
       "nimbleShelfOrder": nimbleShelfOrder,
       "nimbleShelfSesMshipErrDeprecated": nimbleShelfSesMshipErrDeprecated,
       "nimbleShelfFailoverDeprecated": nimbleShelfFailoverDeprecated,
       "nimbleShelfNewShelf": nimbleShelfNewShelf,
       "nimbleShelfDisconnect": nimbleShelfDisconnect,
       "nimbleShelfChassisSwap": nimbleShelfChassisSwap,
       "nimbleShelfLocIdOverLimit": nimbleShelfLocIdOverLimit,
       "nimbleShelfActivatedDeprecated": nimbleShelfActivatedDeprecated,
       "nimbleShelfReconnect": nimbleShelfReconnect,
       "nimbleShelfSasLinkDisabledDeprecated": nimbleShelfSasLinkDisabledDeprecated,
       "nimbleShelfDiskSasLinkErrDeprecated": nimbleShelfDiskSasLinkErrDeprecated,
       "nimbleShelfWrongSasPortDeprecated2": nimbleShelfWrongSasPortDeprecated2,
       "nimbleShelfSesMshipErrDeprecated2": nimbleShelfSesMshipErrDeprecated2,
       "nimbleShelfSasLinkDisabled": nimbleShelfSasLinkDisabled,
       "nimbleShelfDiskSasLinkErr": nimbleShelfDiskSasLinkErr,
       "nimbleShelfWrongSasPortDeprecated3": nimbleShelfWrongSasPortDeprecated3,
       "nimbleShelfSesMshipErrDeprecated3": nimbleShelfSesMshipErrDeprecated3,
       "nimbleShelfSesMshipErrDeprecated4": nimbleShelfSesMshipErrDeprecated4,
       "nimbleShelfActivatedV2Deprecated": nimbleShelfActivatedV2Deprecated,
       "nimbleShelfSesMshipErr": nimbleShelfSesMshipErr,
       "nimbleShelfActivatedV2": nimbleShelfActivatedV2,
       "nimbleShelfIpmiMshipErr": nimbleShelfIpmiMshipErr,
       "nimbleShelfWrongSasPort": nimbleShelfWrongSasPort,
       "nimbleShelfBadDiskPhy": nimbleShelfBadDiskPhy,
       "nimbleShelfBadInterconnectDeprecated": nimbleShelfBadInterconnectDeprecated,
       "nimbleShelfBadInterconnect": nimbleShelfBadInterconnect,
       "nimbleShelfDiskCount": nimbleShelfDiskCount,
       "nimbleShelfBadCutlassDiskPhy": nimbleShelfBadCutlassDiskPhy,
       "nimbleShelfEvacuationInitiated": nimbleShelfEvacuationInitiated,
       "nimbleShelfEvacuationComplete": nimbleShelfEvacuationComplete,
       "nimbleShelfEvacuationPausedByUser": nimbleShelfEvacuationPausedByUser,
       "nimbleShelfEvacuationResumedByUser": nimbleShelfEvacuationResumedByUser,
       "nimbleShelfEvacuationCancelByUser": nimbleShelfEvacuationCancelByUser,
       "nimbleShelfEvacuationFailSpaceUsage": nimbleShelfEvacuationFailSpaceUsage,
       "nimbleShelfEvacuationFailSpaceRed": nimbleShelfEvacuationFailSpaceRed,
       "nimbleShelfEvacuationFailSpaceResume": nimbleShelfEvacuationFailSpaceResume,
       "nimbleShelfEvacuationFailSpaceRedResume": nimbleShelfEvacuationFailSpaceRedResume,
       "nimbleShelfEvacuationFailDataMove": nimbleShelfEvacuationFailDataMove,
       "nimblePhysMemMismatch": nimblePhysMemMismatch,
       "nimbleVolSysLimitWarnEnter": nimbleVolSysLimitWarnEnter,
       "nimbleVolSysLimitWarnExit": nimbleVolSysLimitWarnExit,
       "nimbleGmTakeoverSuccessDeprecated": nimbleGmTakeoverSuccessDeprecated,
       "nimbleGmTakeoverRejectByArrayDeprecated": nimbleGmTakeoverRejectByArrayDeprecated,
       "nimbleGmTakeoverRejectByArrayDeprecated2": nimbleGmTakeoverRejectByArrayDeprecated2,
       "nimbleGmTakeoverSuccessDeprecated2": nimbleGmTakeoverSuccessDeprecated2,
       "nimbleGmTakeoverSuccessDeprecated3": nimbleGmTakeoverSuccessDeprecated3,
       "nimbleGmMigrateFailure": nimbleGmMigrateFailure,
       "nimbleGmTakeoverSuccess": nimbleGmTakeoverSuccess,
       "nimbleGmTakeoverFailure": nimbleGmTakeoverFailure,
       "nimbleGmSuccessfullySetupBgl": nimbleGmSuccessfullySetupBgl,
       "nimbleGmNoBglAvailable": nimbleGmNoBglAvailable,
       "nimbleGmBglOutOfSync": nimbleGmBglOutOfSync,
       "nimbleGmGlSplitBrain": nimbleGmGlSplitBrain,
       "nimbleGmTakeoverAttempt": nimbleGmTakeoverAttempt,
       "nimbleGmTakeoverNotifyLeaderRoleDelayDeprecated": nimbleGmTakeoverNotifyLeaderRoleDelayDeprecated,
       "nimbleGmTakeoverNotifyLeaderRoleComplete": nimbleGmTakeoverNotifyLeaderRoleComplete,
       "nimbleGmNoSmip": nimbleGmNoSmip,
       "nimbleGmSmipConfigured": nimbleGmSmipConfigured,
       "nimbleGmSmipNotNeeded": nimbleGmSmipNotNeeded,
       "nimbleGmBglInSync": nimbleGmBglInSync,
       "nimbleGmNoBglPossible": nimbleGmNoBglPossible,
       "nimbleGmNoArrayFoundWithSameLimitAsGlDeprecated": nimbleGmNoArrayFoundWithSameLimitAsGlDeprecated,
       "nimbleGmWitnessDisconnected": nimbleGmWitnessDisconnected,
       "nimbleGmWitnessConnected": nimbleGmWitnessConnected,
       "nimbleGmQuorumPeerFailure": nimbleGmQuorumPeerFailure,
       "nimbleGmQuorumPeerSuccess": nimbleGmQuorumPeerSuccess,
       "nimbleGmQuorumLocalFailure": nimbleGmQuorumLocalFailure,
       "nimbleGmQuorumLocalSuccess": nimbleGmQuorumLocalSuccess,
       "nimbleGmQuorumSetupFailure": nimbleGmQuorumSetupFailure,
       "nimbleGmQuorumSetupSuccess": nimbleGmQuorumSetupSuccess,
       "nimbleGmAutoShutoff": nimbleGmAutoShutoff,
       "nimbleGmQuorumWitnessUuidChangeDeprecated": nimbleGmQuorumWitnessUuidChangeDeprecated,
       "nimbleGmQuorumTeardownSuccess": nimbleGmQuorumTeardownSuccess,
       "nimbleGmTakeoverNotifyLeaderRoleDelay": nimbleGmTakeoverNotifyLeaderRoleDelay,
       "nimbleGmNoArrayFoundWithSameLimitAsGl": nimbleGmNoArrayFoundWithSameLimitAsGl,
       "nimbleGmQuorumWitnessUuidChange": nimbleGmQuorumWitnessUuidChange,
       "nimbleGmGrpMrgDone": nimbleGmGrpMrgDone,
       "nimbleGmGrpQscFail": nimbleGmGrpQscFail,
       "nimbleGmGrpMrgRollbackDone": nimbleGmGrpMrgRollbackDone,
       "nimbleGmGrpMrgReassFail": nimbleGmGrpMrgReassFail,
       "nimbleGmGrpMrgDbFail": nimbleGmGrpMrgDbFail,
       "nimbleGmBinMigContAbortDeprecated": nimbleGmBinMigContAbortDeprecated,
       "nimbleGmBinMigContAbortDeprecated2": nimbleGmBinMigContAbortDeprecated2,
       "nimbleGmBinMigContAbort": nimbleGmBinMigContAbort,
       "nimbleCsmodelChanged": nimbleCsmodelChanged,
       "nimbleCsmodelUnknown": nimbleCsmodelUnknown,
       "nimbleTempSensorHighDeprecated4": nimbleTempSensorHighDeprecated4,
       "nimbleOvertempShutdownDeprecated2": nimbleOvertempShutdownDeprecated2,
       "nimbleCtrlrOvertemp": nimbleCtrlrOvertemp,
       "nimbleBackplaneOvertemp": nimbleBackplaneOvertemp,
       "nimbleTempSensorHighDeprecated5": nimbleTempSensorHighDeprecated5,
       "nimbleTempSensorCrithighDeprecated": nimbleTempSensorCrithighDeprecated,
       "nimblePwrSupplySensorCallsupportDeprecated": nimblePwrSupplySensorCallsupportDeprecated,
       "nimbleOvertempShutdown": nimbleOvertempShutdown,
       "nimblePwrSupplySensorCallsupportDeprecated2": nimblePwrSupplySensorCallsupportDeprecated2,
       "nimbleTempSensorHighDeprecated6": nimbleTempSensorHighDeprecated6,
       "nimbleTempSensorCrithighDeprecated1": nimbleTempSensorCrithighDeprecated1,
       "nimblePwrSupplySensorCallsupportDeprecated3": nimblePwrSupplySensorCallsupportDeprecated3,
       "nimblePwrSupplySensorCallsupportDeprecated4": nimblePwrSupplySensorCallsupportDeprecated4,
       "nimbleTempSensorCrithighDeprecated2": nimbleTempSensorCrithighDeprecated2,
       "nimbleTempAmbientCrithigh": nimbleTempAmbientCrithigh,
       "nimbleTempAmbientHigh": nimbleTempAmbientHigh,
       "nimbleTempAmbientOk": nimbleTempAmbientOk,
       "nimbleTempAmbientClear": nimbleTempAmbientClear,
       "nimbleTempSensorHigh": nimbleTempSensorHigh,
       "nimbleTempSensorCrithigh": nimbleTempSensorCrithigh,
       "nimbleTempOvertempCrithigh": nimbleTempOvertempCrithigh,
       "nimbleTempOvertempOk": nimbleTempOvertempOk,
       "nimblePwrSupplySensorCallsupport": nimblePwrSupplySensorCallsupport,
       "nimbleUpdateUnknownFirmware": nimbleUpdateUnknownFirmware,
       "nimbleDiskFwUpdateStarted": nimbleDiskFwUpdateStarted,
       "nimbleDiskFwUptodate": nimbleDiskFwUptodate,
       "nimbleDiskFwUpdateFailed": nimbleDiskFwUpdateFailed,
       "nimbleDiskFwUpdateDeferred": nimbleDiskFwUpdateDeferred,
       "nimbleFcLinkUp": nimbleFcLinkUp,
       "nimbleFcLinkDown": nimbleFcLinkDown,
       "nimbleFcLinkNotConnected": nimbleFcLinkNotConnected,
       "nimbleFcFabricUp": nimbleFcFabricUp,
       "nimbleFcNoFabric": nimbleFcNoFabric,
       "nimbleFcHbaFailure": nimbleFcHbaFailure,
       "nimbleFcAsymmetricControllerConnectivityDeprecated": nimbleFcAsymmetricControllerConnectivityDeprecated,
       "nimbleFcAsymmetricControllerConnectivityOkDeprecated": nimbleFcAsymmetricControllerConnectivityOkDeprecated,
       "nimbleFcAsymmetricControllerConnectivity": nimbleFcAsymmetricControllerConnectivity,
       "nimbleFcAsymmetricControllerConnectivityOk": nimbleFcAsymmetricControllerConnectivityOk,
       "nimbleFcPortLoginLimitExceeded": nimbleFcPortLoginLimitExceeded,
       "nimbleFcTdzNotSupported": nimbleFcTdzNotSupported,
       "nimbleFcTdzNotEnabled": nimbleFcTdzNotEnabled,
       "nimbleEventPurgingDeprecated": nimbleEventPurgingDeprecated,
       "nimbleEventWarnOverDeprecated": nimbleEventWarnOverDeprecated,
       "nimbleAuditLogPurgingDeprecated": nimbleAuditLogPurgingDeprecated,
       "nimbleAuditLogWarnOverDeprecated": nimbleAuditLogWarnOverDeprecated,
       "nimbleEventPurging": nimbleEventPurging,
       "nimbleEventWarnOver": nimbleEventWarnOver,
       "nimbleAuditLogPurging": nimbleAuditLogPurging,
       "nimbleAuditLogWarnOver": nimbleAuditLogWarnOver,
       "nimbleAuditLogRootLoginSuccessDeprecated": nimbleAuditLogRootLoginSuccessDeprecated,
       "nimbleAuditLogRootLoginFailDeprecated": nimbleAuditLogRootLoginFailDeprecated,
       "nimbleAdLocalPingFailDeprecated": nimbleAdLocalPingFailDeprecated,
       "nimbleAdRemotePingFailDeprecated": nimbleAdRemotePingFailDeprecated,
       "nimbleAdTrustFailDeprecated": nimbleAdTrustFailDeprecated,
       "nimbleAdCommunicationSuccessDeprecated": nimbleAdCommunicationSuccessDeprecated,
       "nimbleRootLoginSuccess": nimbleRootLoginSuccess,
       "nimbleRootLoginFail": nimbleRootLoginFail,
       "nimbleNsupportLoginSuccess": nimbleNsupportLoginSuccess,
       "nimbleNsupportLoginFail": nimbleNsupportLoginFail,
       "nimbleSuRootSuccess": nimbleSuRootSuccess,
       "nimbleSuRootFail": nimbleSuRootFail,
       "nimbleInvalidRoleLoginDeprecated": nimbleInvalidRoleLoginDeprecated,
       "nimbleBglLoginSuccessDeprecated": nimbleBglLoginSuccessDeprecated,
       "nimbleBglLoginFailDeprecated": nimbleBglLoginFailDeprecated,
       "nimbleBglLoginSuccess": nimbleBglLoginSuccess,
       "nimbleBglLoginFail": nimbleBglLoginFail,
       "nimbleDsdPinCacheDone": nimbleDsdPinCacheDone,
       "nimbleDsdPinCacheDsdRestart": nimbleDsdPinCacheDsdRestart,
       "nimbleDsdPinCacheSsdIssue": nimbleDsdPinCacheSsdIssue,
       "nimbleDsdPinCacheInternalError": nimbleDsdPinCacheInternalError,
       "nimbleDsdPinCacheOk": nimbleDsdPinCacheOk,
       "nimbleDsdPinCacheLowFdr": nimbleDsdPinCacheLowFdr,
       "nimbleArrayDedupeUtilizationOk": nimbleArrayDedupeUtilizationOk,
       "nimbleArrayDedupeUtilizationHigh": nimbleArrayDedupeUtilizationHigh,
       "nimbleArrayDedupeUtilizationCrit": nimbleArrayDedupeUtilizationCrit,
       "nimbleAdTrustFail": nimbleAdTrustFail,
       "nimbleUnmanagedSnapDeleteSuccess": nimbleUnmanagedSnapDeleteSuccess,
       "nimbleCertificateWarning": nimbleCertificateWarning,
       "nimbleCertificateExpired": nimbleCertificateExpired,
       "nimbleArrayFdrNormal": nimbleArrayFdrNormal,
       "nimbleArrayLowFdrWarn": nimbleArrayLowFdrWarn,
       "nimbleArrayLowFdrCrit": nimbleArrayLowFdrCrit,
       "nimbleArrayConfigFdrNormal": nimbleArrayConfigFdrNormal,
       "nimbleArrayConfigFdrLow": nimbleArrayConfigFdrLow,
       "nimbleArrayDedupeMinConfigRestore": nimbleArrayDedupeMinConfigRestore,
       "nimbleArrayDedupeMinFdr": nimbleArrayDedupeMinFdr,
       "nimbleArrayDedupeMinSsdCount": nimbleArrayDedupeMinSsdCount,
       "nimbleMaxSessionsLowMemPlat": nimbleMaxSessionsLowMemPlat,
       "nimbleUserAcctAuthLockDeprecated": nimbleUserAcctAuthLockDeprecated,
       "nimbleMaxSessionsGroupDeprecated": nimbleMaxSessionsGroupDeprecated,
       "nimbleMaxSessionsLoginFailDeprecated": nimbleMaxSessionsLoginFailDeprecated,
       "nimbleSchedSrepSnapSucceededDeprecated": nimbleSchedSrepSnapSucceededDeprecated,
       "nimbleSchedSrepSnapSucceededUpstreamFailedDownstreamDeprecated": nimbleSchedSrepSnapSucceededUpstreamFailedDownstreamDeprecated,
       "nimbleSchedSrepSnapFailedUnknownReasonDeprecated": nimbleSchedSrepSnapFailedUnknownReasonDeprecated,
       "nimbleReplVolResynchronizationNeeded": nimbleReplVolResynchronizationNeeded,
       "nimbleInvalidRoleLogin": nimbleInvalidRoleLogin,
       "nimbleUserAcctAuthLock": nimbleUserAcctAuthLock,
       "nimbleMaxSessionsGroup": nimbleMaxSessionsGroup,
       "nimbleMaxSessionsLoginFail": nimbleMaxSessionsLoginFail,
       "nimbleSchedSrepSnapSucceeded": nimbleSchedSrepSnapSucceeded,
       "nimbleSchedSrepSnapSucceededUpstreamFailedDownstream": nimbleSchedSrepSnapSucceededUpstreamFailedDownstream,
       "nimbleSchedSrepSnapFailedUnknownReason": nimbleSchedSrepSnapFailedUnknownReason,
       "nimbleReplAbortedReplThrottledBandwidthZero": nimbleReplAbortedReplThrottledBandwidthZero,
       "nimbleReplResumedReplThrottledBandwidthNonZero": nimbleReplResumedReplThrottledBandwidthNonZero,
       "nimbleArrayUpgradePrecheckFail": nimbleArrayUpgradePrecheckFail,
       "nimbleArrayUpgradeStarted": nimbleArrayUpgradeStarted,
       "nimbleArrayUpgradePaused": nimbleArrayUpgradePaused,
       "nimbleArrayUpgradeResumed": nimbleArrayUpgradeResumed,
       "nimbleArrayUpgradeFailed": nimbleArrayUpgradeFailed,
       "nimbleArrayUpgradeComplete": nimbleArrayUpgradeComplete,
       "nimbleArrayUpgradeAborting": nimbleArrayUpgradeAborting,
       "nimbleArrayUpgradeAbortFailed": nimbleArrayUpgradeAbortFailed,
       "nimbleArrayUpgradeAborted": nimbleArrayUpgradeAborted}
)
