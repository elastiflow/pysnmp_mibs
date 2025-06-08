# SNMP MIB module (INFINERA-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/infinera_21296/INFINERA-TRAP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:16 2025
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

(ems,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "ems")

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

emsEvent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EmsEventConformance_ObjectIdentity = ObjectIdentity
emsEventConformance = _EmsEventConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6)
)
_EmsEventObjGroups_ObjectIdentity = ObjectIdentity
emsEventObjGroups = _EmsEventObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 1)
)
_EmsEventNotifGroups_ObjectIdentity = ObjectIdentity
emsEventNotifGroups = _EmsEventNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 2)
)
_EmsAlarmTable_Object = MibTable
emsAlarmTable = _EmsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2)
)
if mibBuilder.loadTexts:
    emsAlarmTable.setStatus("current")
_EmsAlarmEntry_Object = MibTableRow
emsAlarmEntry = _EmsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1)
)
emsAlarmEntry.setIndexNames(
    (0, "INFINERA-TRAP-MIB", "emsNotificationId"),
)
if mibBuilder.loadTexts:
    emsAlarmEntry.setStatus("current")


class _EmsNotificationId_Type(Integer32):
    """Custom type emsNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EmsNotificationId_Type.__name__ = "Integer32"
_EmsNotificationId_Object = MibTableColumn
emsNotificationId = _EmsNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 1),
    _EmsNotificationId_Type()
)
emsNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    emsNotificationId.setStatus("current")


class _NeNotificationId_Type(Integer32):
    """Custom type neNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NeNotificationId_Type.__name__ = "Integer32"
_NeNotificationId_Object = MibTableColumn
neNotificationId = _NeNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 2),
    _NeNotificationId_Type()
)
neNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNotificationId.setStatus("current")
_EmsTime_Type = DisplayString
_EmsTime_Object = MibTableColumn
emsTime = _EmsTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 3),
    _EmsTime_Type()
)
emsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsTime.setStatus("current")
_NeTime_Type = DisplayString
_NeTime_Object = MibTableColumn
neTime = _NeTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 4),
    _NeTime_Type()
)
neTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTime.setStatus("current")


class _EmsName_Type(DisplayString):
    """Custom type emsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_EmsName_Type.__name__ = "DisplayString"
_EmsName_Object = MibTableColumn
emsName = _EmsName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 5),
    _EmsName_Type()
)
emsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsName.setStatus("current")


class _NeName_Type(DisplayString):
    """Custom type neName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_NeName_Type.__name__ = "DisplayString"
_NeName_Object = MibTableColumn
neName = _NeName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 6),
    _NeName_Type()
)
neName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neName.setStatus("current")


class _NeNodeId_Type(DisplayString):
    """Custom type neNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_NeNodeId_Type.__name__ = "DisplayString"
_NeNodeId_Object = MibTableColumn
neNodeId = _NeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 7),
    _NeNodeId_Type()
)
neNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNodeId.setStatus("current")
_ObjectType_Type = DisplayString
_ObjectType_Object = MibTableColumn
objectType = _ObjectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 8),
    _ObjectType_Type()
)
objectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectType.setStatus("current")
_ObjectName_Type = DisplayString
_ObjectName_Object = MibTableColumn
objectName = _ObjectName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 9),
    _ObjectName_Type()
)
objectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectName.setStatus("current")


class _SessionNotificationId_Type(Integer32):
    """Custom type sessionNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SessionNotificationId_Type.__name__ = "Integer32"
_SessionNotificationId_Object = MibTableColumn
sessionNotificationId = _SessionNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 10),
    _SessionNotificationId_Type()
)
sessionNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionNotificationId.setStatus("current")
_NeProbableCause_Type = DisplayString
_NeProbableCause_Object = MibTableColumn
neProbableCause = _NeProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 11),
    _NeProbableCause_Type()
)
neProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neProbableCause.setStatus("current")
_EmsProbableCause_Type = DisplayString
_EmsProbableCause_Object = MibTableColumn
emsProbableCause = _EmsProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 12),
    _EmsProbableCause_Type()
)
emsProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsProbableCause.setStatus("current")


class _PerceivedSeverity_Type(Integer32):
    """Custom type perceivedSeverity based on Integer32"""
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
        *(("psIndeterminate", 1),
          ("psCritical", 2),
          ("psMajor", 3),
          ("psMinor", 4),
          ("psWarning", 5),
          ("psCleared", 6))
    )


_PerceivedSeverity_Type.__name__ = "Integer32"
_PerceivedSeverity_Object = MibTableColumn
perceivedSeverity = _PerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 13),
    _PerceivedSeverity_Type()
)
perceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perceivedSeverity.setStatus("current")


class _AssertedSeverity_Type(Integer32):
    """Custom type assertedSeverity based on Integer32"""
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
        *(("psIndeterminate", 1),
          ("psCritical", 2),
          ("psMajor", 3),
          ("psMinor", 4),
          ("psWarning", 5),
          ("psCleared", 6))
    )


_AssertedSeverity_Type.__name__ = "Integer32"
_AssertedSeverity_Object = MibTableColumn
assertedSeverity = _AssertedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 14),
    _AssertedSeverity_Type()
)
assertedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assertedSeverity.setStatus("current")


class _ServiceAffecting_Type(Integer32):
    """Custom type serviceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("saUnknown", 1),
          ("saServiceAffecting", 2),
          ("saNonServiceAffecting", 3))
    )


_ServiceAffecting_Type.__name__ = "Integer32"
_ServiceAffecting_Object = MibTableColumn
serviceAffecting = _ServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 15),
    _ServiceAffecting_Type()
)
serviceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceAffecting.setStatus("current")


class _ProbableCauseDescription_Type(DisplayString):
    """Custom type probableCauseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProbableCauseDescription_Type.__name__ = "DisplayString"
_ProbableCauseDescription_Object = MibTableColumn
probableCauseDescription = _ProbableCauseDescription_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 16),
    _ProbableCauseDescription_Type()
)
probableCauseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probableCauseDescription.setStatus("current")


class _Category_Type(Integer32):
    """Custom type category based on Integer32"""
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
        *(("unknown", 1),
          ("equipment", 2),
          ("facility", 3),
          ("communications", 4),
          ("softwareProcessing", 5),
          ("environmental", 6),
          ("qualityOfService", 7),
          ("ems", 8))
    )


_Category_Type.__name__ = "Integer32"
_Category_Object = MibTableColumn
category = _Category_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 17),
    _Category_Type()
)
category.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    category.setStatus("current")
_ProposedRepairActions_Type = DisplayString
_ProposedRepairActions_Object = MibTableColumn
proposedRepairActions = _ProposedRepairActions_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 18),
    _ProposedRepairActions_Type()
)
proposedRepairActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proposedRepairActions.setStatus("current")
_AdditionalText_Type = DisplayString
_AdditionalText_Object = MibTableColumn
additionalText = _AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 19),
    _AdditionalText_Type()
)
additionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    additionalText.setStatus("current")


class _EmsCorrelationId_Type(Integer32):
    """Custom type emsCorrelationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EmsCorrelationId_Type.__name__ = "Integer32"
_EmsCorrelationId_Object = MibTableColumn
emsCorrelationId = _EmsCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 20),
    _EmsCorrelationId_Type()
)
emsCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsCorrelationId.setStatus("current")


class _NeCorrelationId_Type(Integer32):
    """Custom type neCorrelationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NeCorrelationId_Type.__name__ = "Integer32"
_NeCorrelationId_Object = MibTableColumn
neCorrelationId = _NeCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 2, 1, 21),
    _NeCorrelationId_Type()
)
neCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neCorrelationId.setStatus("current")
_EmsAuditTable_Object = MibTable
emsAuditTable = _EmsAuditTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3)
)
if mibBuilder.loadTexts:
    emsAuditTable.setStatus("current")
_EmsAuditEntry_Object = MibTableRow
emsAuditEntry = _EmsAuditEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1)
)
emsAuditEntry.setIndexNames(
    (0, "INFINERA-TRAP-MIB", "auditEmsNotificationId"),
)
if mibBuilder.loadTexts:
    emsAuditEntry.setStatus("current")


class _AuditEmsNotificationId_Type(Integer32):
    """Custom type auditEmsNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuditEmsNotificationId_Type.__name__ = "Integer32"
_AuditEmsNotificationId_Object = MibTableColumn
auditEmsNotificationId = _AuditEmsNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 1),
    _AuditEmsNotificationId_Type()
)
auditEmsNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    auditEmsNotificationId.setStatus("current")


class _AuditNeNotificationId_Type(Integer32):
    """Custom type auditNeNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuditNeNotificationId_Type.__name__ = "Integer32"
_AuditNeNotificationId_Object = MibTableColumn
auditNeNotificationId = _AuditNeNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 2),
    _AuditNeNotificationId_Type()
)
auditNeNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditNeNotificationId.setStatus("current")
_AuditEmsTime_Type = DisplayString
_AuditEmsTime_Object = MibTableColumn
auditEmsTime = _AuditEmsTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 3),
    _AuditEmsTime_Type()
)
auditEmsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditEmsTime.setStatus("current")
_AuditNeTime_Type = DisplayString
_AuditNeTime_Object = MibTableColumn
auditNeTime = _AuditNeTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 4),
    _AuditNeTime_Type()
)
auditNeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditNeTime.setStatus("current")


class _AuditEmsName_Type(DisplayString):
    """Custom type auditEmsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_AuditEmsName_Type.__name__ = "DisplayString"
_AuditEmsName_Object = MibTableColumn
auditEmsName = _AuditEmsName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 5),
    _AuditEmsName_Type()
)
auditEmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditEmsName.setStatus("current")


class _AuditNeName_Type(DisplayString):
    """Custom type auditNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AuditNeName_Type.__name__ = "DisplayString"
_AuditNeName_Object = MibTableColumn
auditNeName = _AuditNeName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 6),
    _AuditNeName_Type()
)
auditNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditNeName.setStatus("current")


class _AuditNeNodeId_Type(DisplayString):
    """Custom type auditNeNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AuditNeNodeId_Type.__name__ = "DisplayString"
_AuditNeNodeId_Object = MibTableColumn
auditNeNodeId = _AuditNeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 7),
    _AuditNeNodeId_Type()
)
auditNeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditNeNodeId.setStatus("current")
_AuditObjectType_Type = DisplayString
_AuditObjectType_Object = MibTableColumn
auditObjectType = _AuditObjectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 8),
    _AuditObjectType_Type()
)
auditObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditObjectType.setStatus("current")
_AuditObjectName_Type = DisplayString
_AuditObjectName_Object = MibTableColumn
auditObjectName = _AuditObjectName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 9),
    _AuditObjectName_Type()
)
auditObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditObjectName.setStatus("current")


class _AuditAccountName_Type(DisplayString):
    """Custom type auditAccountName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuditAccountName_Type.__name__ = "DisplayString"
_AuditAccountName_Object = MibTableColumn
auditAccountName = _AuditAccountName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 10),
    _AuditAccountName_Type()
)
auditAccountName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditAccountName.setStatus("current")


class _AuditClientHostName_Type(DisplayString):
    """Custom type auditClientHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuditClientHostName_Type.__name__ = "DisplayString"
_AuditClientHostName_Object = MibTableColumn
auditClientHostName = _AuditClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 11),
    _AuditClientHostName_Type()
)
auditClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditClientHostName.setStatus("current")


class _AuditOperationName_Type(DisplayString):
    """Custom type auditOperationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuditOperationName_Type.__name__ = "DisplayString"
_AuditOperationName_Object = MibTableColumn
auditOperationName = _AuditOperationName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 12),
    _AuditOperationName_Type()
)
auditOperationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditOperationName.setStatus("current")


class _AuditOperationStatus_Type(DisplayString):
    """Custom type auditOperationStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuditOperationStatus_Type.__name__ = "DisplayString"
_AuditOperationStatus_Object = MibTableColumn
auditOperationStatus = _AuditOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 13),
    _AuditOperationStatus_Type()
)
auditOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditOperationStatus.setStatus("current")
_AuditParamList_Type = DisplayString
_AuditParamList_Object = MibTableColumn
auditParamList = _AuditParamList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 3, 1, 14),
    _AuditParamList_Type()
)
auditParamList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditParamList.setStatus("current")
_EmsAdminTable_Object = MibTable
emsAdminTable = _EmsAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4)
)
if mibBuilder.loadTexts:
    emsAdminTable.setStatus("current")
_EmsAdminEntry_Object = MibTableRow
emsAdminEntry = _EmsAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1)
)
emsAdminEntry.setIndexNames(
    (0, "INFINERA-TRAP-MIB", "adminEmsNotificationId"),
)
if mibBuilder.loadTexts:
    emsAdminEntry.setStatus("current")


class _AdminEmsNotificationId_Type(Integer32):
    """Custom type adminEmsNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdminEmsNotificationId_Type.__name__ = "Integer32"
_AdminEmsNotificationId_Object = MibTableColumn
adminEmsNotificationId = _AdminEmsNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 1),
    _AdminEmsNotificationId_Type()
)
adminEmsNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adminEmsNotificationId.setStatus("current")


class _AdminNeNotificationId_Type(Integer32):
    """Custom type adminNeNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdminNeNotificationId_Type.__name__ = "Integer32"
_AdminNeNotificationId_Object = MibTableColumn
adminNeNotificationId = _AdminNeNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 2),
    _AdminNeNotificationId_Type()
)
adminNeNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNeNotificationId.setStatus("current")
_AdminEmsTime_Type = DisplayString
_AdminEmsTime_Object = MibTableColumn
adminEmsTime = _AdminEmsTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 3),
    _AdminEmsTime_Type()
)
adminEmsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminEmsTime.setStatus("current")
_AdminNeTime_Type = DisplayString
_AdminNeTime_Object = MibTableColumn
adminNeTime = _AdminNeTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 4),
    _AdminNeTime_Type()
)
adminNeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNeTime.setStatus("current")


class _AdminEmsName_Type(DisplayString):
    """Custom type adminEmsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_AdminEmsName_Type.__name__ = "DisplayString"
_AdminEmsName_Object = MibTableColumn
adminEmsName = _AdminEmsName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 5),
    _AdminEmsName_Type()
)
adminEmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminEmsName.setStatus("current")


class _AdminNeName_Type(DisplayString):
    """Custom type adminNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AdminNeName_Type.__name__ = "DisplayString"
_AdminNeName_Object = MibTableColumn
adminNeName = _AdminNeName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 6),
    _AdminNeName_Type()
)
adminNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNeName.setStatus("current")


class _AdminNeNodeId_Type(DisplayString):
    """Custom type adminNeNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AdminNeNodeId_Type.__name__ = "DisplayString"
_AdminNeNodeId_Object = MibTableColumn
adminNeNodeId = _AdminNeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 7),
    _AdminNeNodeId_Type()
)
adminNeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNeNodeId.setStatus("current")
_AdminObjectType_Type = DisplayString
_AdminObjectType_Object = MibTableColumn
adminObjectType = _AdminObjectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 8),
    _AdminObjectType_Type()
)
adminObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminObjectType.setStatus("current")
_AdminObjectName_Type = DisplayString
_AdminObjectName_Object = MibTableColumn
adminObjectName = _AdminObjectName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 9),
    _AdminObjectName_Type()
)
adminObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminObjectName.setStatus("current")


class _AdminCause_Type(DisplayString):
    """Custom type adminCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdminCause_Type.__name__ = "DisplayString"
_AdminCause_Object = MibTableColumn
adminCause = _AdminCause_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 4, 1, 10),
    _AdminCause_Type()
)
adminCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminCause.setStatus("current")
_EmsSecurityTable_Object = MibTable
emsSecurityTable = _EmsSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5)
)
if mibBuilder.loadTexts:
    emsSecurityTable.setStatus("current")
_EmsSecurityEntry_Object = MibTableRow
emsSecurityEntry = _EmsSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1)
)
emsSecurityEntry.setIndexNames(
    (0, "INFINERA-TRAP-MIB", "securityEmsNotificationId"),
)
if mibBuilder.loadTexts:
    emsSecurityEntry.setStatus("current")


class _SecurityEmsNotificationId_Type(Integer32):
    """Custom type securityEmsNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SecurityEmsNotificationId_Type.__name__ = "Integer32"
_SecurityEmsNotificationId_Object = MibTableColumn
securityEmsNotificationId = _SecurityEmsNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 1),
    _SecurityEmsNotificationId_Type()
)
securityEmsNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    securityEmsNotificationId.setStatus("current")


class _SecurityNeNotificationId_Type(Integer32):
    """Custom type securityNeNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SecurityNeNotificationId_Type.__name__ = "Integer32"
_SecurityNeNotificationId_Object = MibTableColumn
securityNeNotificationId = _SecurityNeNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 2),
    _SecurityNeNotificationId_Type()
)
securityNeNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityNeNotificationId.setStatus("current")
_SecurityEmsTime_Type = DisplayString
_SecurityEmsTime_Object = MibTableColumn
securityEmsTime = _SecurityEmsTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 3),
    _SecurityEmsTime_Type()
)
securityEmsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityEmsTime.setStatus("current")
_SecurityNeTime_Type = DisplayString
_SecurityNeTime_Object = MibTableColumn
securityNeTime = _SecurityNeTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 4),
    _SecurityNeTime_Type()
)
securityNeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityNeTime.setStatus("current")


class _SecurityEmsName_Type(DisplayString):
    """Custom type securityEmsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_SecurityEmsName_Type.__name__ = "DisplayString"
_SecurityEmsName_Object = MibTableColumn
securityEmsName = _SecurityEmsName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 5),
    _SecurityEmsName_Type()
)
securityEmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityEmsName.setStatus("current")


class _SecurityNeName_Type(DisplayString):
    """Custom type securityNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SecurityNeName_Type.__name__ = "DisplayString"
_SecurityNeName_Object = MibTableColumn
securityNeName = _SecurityNeName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 6),
    _SecurityNeName_Type()
)
securityNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityNeName.setStatus("current")


class _SecurityNeNodeId_Type(DisplayString):
    """Custom type securityNeNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SecurityNeNodeId_Type.__name__ = "DisplayString"
_SecurityNeNodeId_Object = MibTableColumn
securityNeNodeId = _SecurityNeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 7),
    _SecurityNeNodeId_Type()
)
securityNeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityNeNodeId.setStatus("current")
_SecurityObjectType_Type = DisplayString
_SecurityObjectType_Object = MibTableColumn
securityObjectType = _SecurityObjectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 8),
    _SecurityObjectType_Type()
)
securityObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityObjectType.setStatus("current")
_SecurityObjectName_Type = DisplayString
_SecurityObjectName_Object = MibTableColumn
securityObjectName = _SecurityObjectName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 9),
    _SecurityObjectName_Type()
)
securityObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityObjectName.setStatus("current")


class _SecurityAccountName_Type(DisplayString):
    """Custom type securityAccountName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SecurityAccountName_Type.__name__ = "DisplayString"
_SecurityAccountName_Object = MibTableColumn
securityAccountName = _SecurityAccountName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 10),
    _SecurityAccountName_Type()
)
securityAccountName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAccountName.setStatus("current")


class _SecurityClientHostName_Type(DisplayString):
    """Custom type securityClientHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SecurityClientHostName_Type.__name__ = "DisplayString"
_SecurityClientHostName_Object = MibTableColumn
securityClientHostName = _SecurityClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 11),
    _SecurityClientHostName_Type()
)
securityClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityClientHostName.setStatus("current")


class _SecurityCause_Type(DisplayString):
    """Custom type securityCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SecurityCause_Type.__name__ = "DisplayString"
_SecurityCause_Object = MibTableColumn
securityCause = _SecurityCause_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 5, 1, 12),
    _SecurityCause_Type()
)
securityCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityCause.setStatus("current")
_EmsTCATable_Object = MibTable
emsTCATable = _EmsTCATable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6)
)
if mibBuilder.loadTexts:
    emsTCATable.setStatus("current")
_EmsTCAEntry_Object = MibTableRow
emsTCAEntry = _EmsTCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1)
)
emsTCAEntry.setIndexNames(
    (0, "INFINERA-TRAP-MIB", "tcaEmsNotificationId"),
)
if mibBuilder.loadTexts:
    emsTCAEntry.setStatus("current")


class _TcaEmsNotificationId_Type(Integer32):
    """Custom type tcaEmsNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TcaEmsNotificationId_Type.__name__ = "Integer32"
_TcaEmsNotificationId_Object = MibTableColumn
tcaEmsNotificationId = _TcaEmsNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 1),
    _TcaEmsNotificationId_Type()
)
tcaEmsNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tcaEmsNotificationId.setStatus("current")


class _TcaNeNotificationId_Type(Integer32):
    """Custom type tcaNeNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TcaNeNotificationId_Type.__name__ = "Integer32"
_TcaNeNotificationId_Object = MibTableColumn
tcaNeNotificationId = _TcaNeNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 2),
    _TcaNeNotificationId_Type()
)
tcaNeNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaNeNotificationId.setStatus("current")
_TcaEmsTime_Type = DisplayString
_TcaEmsTime_Object = MibTableColumn
tcaEmsTime = _TcaEmsTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 3),
    _TcaEmsTime_Type()
)
tcaEmsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaEmsTime.setStatus("current")
_TcaNeTime_Type = DisplayString
_TcaNeTime_Object = MibTableColumn
tcaNeTime = _TcaNeTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 4),
    _TcaNeTime_Type()
)
tcaNeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaNeTime.setStatus("current")


class _TcaEmsName_Type(DisplayString):
    """Custom type tcaEmsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_TcaEmsName_Type.__name__ = "DisplayString"
_TcaEmsName_Object = MibTableColumn
tcaEmsName = _TcaEmsName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 5),
    _TcaEmsName_Type()
)
tcaEmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaEmsName.setStatus("current")


class _TcaNeName_Type(DisplayString):
    """Custom type tcaNeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TcaNeName_Type.__name__ = "DisplayString"
_TcaNeName_Object = MibTableColumn
tcaNeName = _TcaNeName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 6),
    _TcaNeName_Type()
)
tcaNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaNeName.setStatus("current")


class _TcaNeNodeId_Type(DisplayString):
    """Custom type tcaNeNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TcaNeNodeId_Type.__name__ = "DisplayString"
_TcaNeNodeId_Object = MibTableColumn
tcaNeNodeId = _TcaNeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 7),
    _TcaNeNodeId_Type()
)
tcaNeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaNeNodeId.setStatus("current")
_TcaObjectType_Type = DisplayString
_TcaObjectType_Object = MibTableColumn
tcaObjectType = _TcaObjectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 8),
    _TcaObjectType_Type()
)
tcaObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaObjectType.setStatus("current")
_TcaObjectName_Type = DisplayString
_TcaObjectName_Object = MibTableColumn
tcaObjectName = _TcaObjectName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 9),
    _TcaObjectName_Type()
)
tcaObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaObjectName.setStatus("current")


class _TcaClearableState_Type(Integer32):
    """Custom type tcaClearableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearable", 1),
          ("nonclearable", 2))
    )


_TcaClearableState_Type.__name__ = "Integer32"
_TcaClearableState_Object = MibTableColumn
tcaClearableState = _TcaClearableState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 10),
    _TcaClearableState_Type()
)
tcaClearableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaClearableState.setStatus("current")


class _TcaParameterName_Type(DisplayString):
    """Custom type tcaParameterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TcaParameterName_Type.__name__ = "DisplayString"
_TcaParameterName_Object = MibTableColumn
tcaParameterName = _TcaParameterName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 11),
    _TcaParameterName_Type()
)
tcaParameterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaParameterName.setStatus("current")


class _TcaLocation_Type(DisplayString):
    """Custom type tcaLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TcaLocation_Type.__name__ = "DisplayString"
_TcaLocation_Object = MibTableColumn
tcaLocation = _TcaLocation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 12),
    _TcaLocation_Type()
)
tcaLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaLocation.setStatus("current")


class _TcaThresholdType_Type(DisplayString):
    """Custom type tcaThresholdType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TcaThresholdType_Type.__name__ = "DisplayString"
_TcaThresholdType_Object = MibTableColumn
tcaThresholdType = _TcaThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 13),
    _TcaThresholdType_Type()
)
tcaThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaThresholdType.setStatus("current")


class _TcaThresholdValue_Type(DisplayString):
    """Custom type tcaThresholdValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TcaThresholdValue_Type.__name__ = "DisplayString"
_TcaThresholdValue_Object = MibTableColumn
tcaThresholdValue = _TcaThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 14),
    _TcaThresholdValue_Type()
)
tcaThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaThresholdValue.setStatus("current")


class _TcaCurrentValue_Type(DisplayString):
    """Custom type tcaCurrentValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TcaCurrentValue_Type.__name__ = "DisplayString"
_TcaCurrentValue_Object = MibTableColumn
tcaCurrentValue = _TcaCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 15),
    _TcaCurrentValue_Type()
)
tcaCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaCurrentValue.setStatus("current")


class _TcaGranularity_Type(DisplayString):
    """Custom type tcaGranularity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TcaGranularity_Type.__name__ = "DisplayString"
_TcaGranularity_Object = MibTableColumn
tcaGranularity = _TcaGranularity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 16),
    _TcaGranularity_Type()
)
tcaGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaGranularity.setStatus("current")


class _TcaPerceivedSeverity_Type(Integer32):
    """Custom type tcaPerceivedSeverity based on Integer32"""
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
        *(("psIndeterminate", 1),
          ("psCritical", 2),
          ("psMajor", 3),
          ("psMinor", 4),
          ("psWarning", 5),
          ("psCleared", 6))
    )


_TcaPerceivedSeverity_Type.__name__ = "Integer32"
_TcaPerceivedSeverity_Object = MibTableColumn
tcaPerceivedSeverity = _TcaPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 17),
    _TcaPerceivedSeverity_Type()
)
tcaPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaPerceivedSeverity.setStatus("current")


class _TcaAssertedSeverity_Type(Integer32):
    """Custom type tcaAssertedSeverity based on Integer32"""
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
        *(("psIndeterminate", 1),
          ("psCritical", 2),
          ("psMajor", 3),
          ("psMinor", 4),
          ("psWarning", 5),
          ("psCleared", 6))
    )


_TcaAssertedSeverity_Type.__name__ = "Integer32"
_TcaAssertedSeverity_Object = MibTableColumn
tcaAssertedSeverity = _TcaAssertedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 18),
    _TcaAssertedSeverity_Type()
)
tcaAssertedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaAssertedSeverity.setStatus("current")


class _TcaNeCorrelationId_Type(Integer32):
    """Custom type tcaNeCorrelationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TcaNeCorrelationId_Type.__name__ = "Integer32"
_TcaNeCorrelationId_Object = MibTableColumn
tcaNeCorrelationId = _TcaNeCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 6, 1, 19),
    _TcaNeCorrelationId_Type()
)
tcaNeCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaNeCorrelationId.setStatus("current")

# Managed Objects groups

emsAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 1, 1)
)
emsAlarmGroup.setObjects(
      *(("INFINERA-TRAP-MIB", "neCorrelationId"),
        ("INFINERA-TRAP-MIB", "emsCorrelationId"),
        ("INFINERA-TRAP-MIB", "additionalText"),
        ("INFINERA-TRAP-MIB", "proposedRepairActions"),
        ("INFINERA-TRAP-MIB", "category"),
        ("INFINERA-TRAP-MIB", "probableCauseDescription"),
        ("INFINERA-TRAP-MIB", "serviceAffecting"),
        ("INFINERA-TRAP-MIB", "assertedSeverity"),
        ("INFINERA-TRAP-MIB", "perceivedSeverity"),
        ("INFINERA-TRAP-MIB", "emsProbableCause"),
        ("INFINERA-TRAP-MIB", "neProbableCause"),
        ("INFINERA-TRAP-MIB", "sessionNotificationId"),
        ("INFINERA-TRAP-MIB", "objectName"),
        ("INFINERA-TRAP-MIB", "objectType"),
        ("INFINERA-TRAP-MIB", "neNodeId"),
        ("INFINERA-TRAP-MIB", "neName"),
        ("INFINERA-TRAP-MIB", "neNotificationId"),
        ("INFINERA-TRAP-MIB", "emsName"),
        ("INFINERA-TRAP-MIB", "neTime"),
        ("INFINERA-TRAP-MIB", "emsTime"),
        ("INFINERA-TRAP-MIB", "emsNotificationId"))
)
if mibBuilder.loadTexts:
    emsAlarmGroup.setStatus("current")

emsAuditGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 1, 2)
)
emsAuditGroup.setObjects(
      *(("INFINERA-TRAP-MIB", "auditEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "auditNeNotificationId"),
        ("INFINERA-TRAP-MIB", "auditEmsTime"),
        ("INFINERA-TRAP-MIB", "auditNeTime"),
        ("INFINERA-TRAP-MIB", "auditEmsName"),
        ("INFINERA-TRAP-MIB", "auditNeName"),
        ("INFINERA-TRAP-MIB", "auditNeNodeId"),
        ("INFINERA-TRAP-MIB", "auditObjectType"),
        ("INFINERA-TRAP-MIB", "auditObjectName"),
        ("INFINERA-TRAP-MIB", "auditAccountName"),
        ("INFINERA-TRAP-MIB", "auditClientHostName"),
        ("INFINERA-TRAP-MIB", "auditOperationName"),
        ("INFINERA-TRAP-MIB", "auditOperationStatus"),
        ("INFINERA-TRAP-MIB", "auditParamList"))
)
if mibBuilder.loadTexts:
    emsAuditGroup.setStatus("current")

emsAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 1, 3)
)
emsAdminGroup.setObjects(
      *(("INFINERA-TRAP-MIB", "adminEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "adminNeNotificationId"),
        ("INFINERA-TRAP-MIB", "adminEmsTime"),
        ("INFINERA-TRAP-MIB", "adminNeTime"),
        ("INFINERA-TRAP-MIB", "adminEmsName"),
        ("INFINERA-TRAP-MIB", "adminNeName"),
        ("INFINERA-TRAP-MIB", "adminNeNodeId"),
        ("INFINERA-TRAP-MIB", "adminObjectType"),
        ("INFINERA-TRAP-MIB", "adminObjectName"),
        ("INFINERA-TRAP-MIB", "adminCause"))
)
if mibBuilder.loadTexts:
    emsAdminGroup.setStatus("current")

emsSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 1, 4)
)
emsSecurityGroup.setObjects(
      *(("INFINERA-TRAP-MIB", "securityEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "securityNeNotificationId"),
        ("INFINERA-TRAP-MIB", "securityEmsTime"),
        ("INFINERA-TRAP-MIB", "securityNeTime"),
        ("INFINERA-TRAP-MIB", "securityEmsName"),
        ("INFINERA-TRAP-MIB", "securityNeName"),
        ("INFINERA-TRAP-MIB", "securityNeNodeId"),
        ("INFINERA-TRAP-MIB", "securityObjectType"),
        ("INFINERA-TRAP-MIB", "securityObjectName"),
        ("INFINERA-TRAP-MIB", "securityAccountName"),
        ("INFINERA-TRAP-MIB", "securityClientHostName"),
        ("INFINERA-TRAP-MIB", "securityCause"))
)
if mibBuilder.loadTexts:
    emsSecurityGroup.setStatus("current")

emsTCAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 1, 5)
)
emsTCAGroup.setObjects(
      *(("INFINERA-TRAP-MIB", "tcaEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "tcaNeNotificationId"),
        ("INFINERA-TRAP-MIB", "tcaEmsTime"),
        ("INFINERA-TRAP-MIB", "tcaNeTime"),
        ("INFINERA-TRAP-MIB", "tcaEmsName"),
        ("INFINERA-TRAP-MIB", "tcaNeName"),
        ("INFINERA-TRAP-MIB", "tcaNeNodeId"),
        ("INFINERA-TRAP-MIB", "tcaObjectType"),
        ("INFINERA-TRAP-MIB", "tcaObjectName"),
        ("INFINERA-TRAP-MIB", "tcaClearableState"),
        ("INFINERA-TRAP-MIB", "tcaParameterName"),
        ("INFINERA-TRAP-MIB", "tcaLocation"),
        ("INFINERA-TRAP-MIB", "tcaThresholdType"),
        ("INFINERA-TRAP-MIB", "tcaThresholdValue"),
        ("INFINERA-TRAP-MIB", "tcaCurrentValue"),
        ("INFINERA-TRAP-MIB", "tcaGranularity"),
        ("INFINERA-TRAP-MIB", "tcaPerceivedSeverity"),
        ("INFINERA-TRAP-MIB", "tcaAssertedSeverity"),
        ("INFINERA-TRAP-MIB", "tcaNeCorrelationId"))
)
if mibBuilder.loadTexts:
    emsTCAGroup.setStatus("current")


# Notification objects

emsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 1)
)
emsAlarm.setObjects(
      *(("INFINERA-TRAP-MIB", "emsNotificationId"),
        ("INFINERA-TRAP-MIB", "neNotificationId"),
        ("INFINERA-TRAP-MIB", "emsTime"),
        ("INFINERA-TRAP-MIB", "neTime"),
        ("INFINERA-TRAP-MIB", "emsName"),
        ("INFINERA-TRAP-MIB", "neName"),
        ("INFINERA-TRAP-MIB", "neNodeId"),
        ("INFINERA-TRAP-MIB", "objectType"),
        ("INFINERA-TRAP-MIB", "objectName"),
        ("INFINERA-TRAP-MIB", "sessionNotificationId"),
        ("INFINERA-TRAP-MIB", "emsProbableCause"),
        ("INFINERA-TRAP-MIB", "neProbableCause"),
        ("INFINERA-TRAP-MIB", "perceivedSeverity"),
        ("INFINERA-TRAP-MIB", "assertedSeverity"),
        ("INFINERA-TRAP-MIB", "serviceAffecting"),
        ("INFINERA-TRAP-MIB", "category"),
        ("INFINERA-TRAP-MIB", "probableCauseDescription"),
        ("INFINERA-TRAP-MIB", "proposedRepairActions"),
        ("INFINERA-TRAP-MIB", "additionalText"),
        ("INFINERA-TRAP-MIB", "emsCorrelationId"),
        ("INFINERA-TRAP-MIB", "neCorrelationId"))
)
if mibBuilder.loadTexts:
    emsAlarm.setStatus(
        "current"
    )

emsAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 2)
)
emsAudit.setObjects(
      *(("INFINERA-TRAP-MIB", "auditEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "auditNeNotificationId"),
        ("INFINERA-TRAP-MIB", "auditEmsTime"),
        ("INFINERA-TRAP-MIB", "auditNeTime"),
        ("INFINERA-TRAP-MIB", "auditEmsName"),
        ("INFINERA-TRAP-MIB", "auditNeName"),
        ("INFINERA-TRAP-MIB", "auditNeNodeId"),
        ("INFINERA-TRAP-MIB", "auditObjectType"),
        ("INFINERA-TRAP-MIB", "auditObjectName"),
        ("INFINERA-TRAP-MIB", "auditAccountName"),
        ("INFINERA-TRAP-MIB", "auditClientHostName"),
        ("INFINERA-TRAP-MIB", "auditOperationName"),
        ("INFINERA-TRAP-MIB", "auditOperationStatus"),
        ("INFINERA-TRAP-MIB", "auditParamList"),
        ("INFINERA-TRAP-MIB", "sessionNotificationId"))
)
if mibBuilder.loadTexts:
    emsAudit.setStatus(
        "current"
    )

emsAdmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 3)
)
emsAdmin.setObjects(
      *(("INFINERA-TRAP-MIB", "adminEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "adminNeNotificationId"),
        ("INFINERA-TRAP-MIB", "adminEmsTime"),
        ("INFINERA-TRAP-MIB", "adminNeTime"),
        ("INFINERA-TRAP-MIB", "adminEmsName"),
        ("INFINERA-TRAP-MIB", "adminNeName"),
        ("INFINERA-TRAP-MIB", "adminNeNodeId"),
        ("INFINERA-TRAP-MIB", "adminObjectType"),
        ("INFINERA-TRAP-MIB", "adminObjectName"),
        ("INFINERA-TRAP-MIB", "adminCause"),
        ("INFINERA-TRAP-MIB", "sessionNotificationId"))
)
if mibBuilder.loadTexts:
    emsAdmin.setStatus(
        "current"
    )

emsSecurity = NotificationType(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 4)
)
emsSecurity.setObjects(
      *(("INFINERA-TRAP-MIB", "securityEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "securityNeNotificationId"),
        ("INFINERA-TRAP-MIB", "securityEmsTime"),
        ("INFINERA-TRAP-MIB", "securityNeTime"),
        ("INFINERA-TRAP-MIB", "securityEmsName"),
        ("INFINERA-TRAP-MIB", "securityNeName"),
        ("INFINERA-TRAP-MIB", "securityNeNodeId"),
        ("INFINERA-TRAP-MIB", "securityObjectType"),
        ("INFINERA-TRAP-MIB", "securityObjectName"),
        ("INFINERA-TRAP-MIB", "securityAccountName"),
        ("INFINERA-TRAP-MIB", "securityClientHostName"),
        ("INFINERA-TRAP-MIB", "securityCause"),
        ("INFINERA-TRAP-MIB", "sessionNotificationId"))
)
if mibBuilder.loadTexts:
    emsSecurity.setStatus(
        "current"
    )

emsTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 5)
)
emsTCA.setObjects(
      *(("INFINERA-TRAP-MIB", "tcaEmsNotificationId"),
        ("INFINERA-TRAP-MIB", "tcaNeNotificationId"),
        ("INFINERA-TRAP-MIB", "tcaEmsTime"),
        ("INFINERA-TRAP-MIB", "tcaNeTime"),
        ("INFINERA-TRAP-MIB", "tcaEmsName"),
        ("INFINERA-TRAP-MIB", "tcaNeName"),
        ("INFINERA-TRAP-MIB", "tcaNeNodeId"),
        ("INFINERA-TRAP-MIB", "tcaObjectType"),
        ("INFINERA-TRAP-MIB", "tcaObjectName"),
        ("INFINERA-TRAP-MIB", "tcaClearableState"),
        ("INFINERA-TRAP-MIB", "tcaParameterName"),
        ("INFINERA-TRAP-MIB", "tcaLocation"),
        ("INFINERA-TRAP-MIB", "tcaThresholdType"),
        ("INFINERA-TRAP-MIB", "tcaThresholdValue"),
        ("INFINERA-TRAP-MIB", "tcaCurrentValue"),
        ("INFINERA-TRAP-MIB", "tcaGranularity"),
        ("INFINERA-TRAP-MIB", "tcaPerceivedSeverity"),
        ("INFINERA-TRAP-MIB", "tcaAssertedSeverity"),
        ("INFINERA-TRAP-MIB", "tcaNeCorrelationId"),
        ("INFINERA-TRAP-MIB", "sessionNotificationId"))
)
if mibBuilder.loadTexts:
    emsTCA.setStatus(
        "current"
    )


# Notifications groups

emsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3, 1, 6, 2, 1)
)
emsNotifGroup.setObjects(
      *(("INFINERA-TRAP-MIB", "emsTCA"),
        ("INFINERA-TRAP-MIB", "emsSecurity"),
        ("INFINERA-TRAP-MIB", "emsAdmin"),
        ("INFINERA-TRAP-MIB", "emsAudit"),
        ("INFINERA-TRAP-MIB", "emsAlarm"))
)
if mibBuilder.loadTexts:
    emsNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TRAP-MIB",
    **{"emsEvent": emsEvent,
       "emsAlarm": emsAlarm,
       "emsAudit": emsAudit,
       "emsAdmin": emsAdmin,
       "emsSecurity": emsSecurity,
       "emsTCA": emsTCA,
       "emsEventConformance": emsEventConformance,
       "emsEventObjGroups": emsEventObjGroups,
       "emsAlarmGroup": emsAlarmGroup,
       "emsAuditGroup": emsAuditGroup,
       "emsAdminGroup": emsAdminGroup,
       "emsSecurityGroup": emsSecurityGroup,
       "emsTCAGroup": emsTCAGroup,
       "emsEventNotifGroups": emsEventNotifGroups,
       "emsNotifGroup": emsNotifGroup,
       "emsAlarmTable": emsAlarmTable,
       "emsAlarmEntry": emsAlarmEntry,
       "emsNotificationId": emsNotificationId,
       "neNotificationId": neNotificationId,
       "emsTime": emsTime,
       "neTime": neTime,
       "emsName": emsName,
       "neName": neName,
       "neNodeId": neNodeId,
       "objectType": objectType,
       "objectName": objectName,
       "sessionNotificationId": sessionNotificationId,
       "neProbableCause": neProbableCause,
       "emsProbableCause": emsProbableCause,
       "perceivedSeverity": perceivedSeverity,
       "assertedSeverity": assertedSeverity,
       "serviceAffecting": serviceAffecting,
       "probableCauseDescription": probableCauseDescription,
       "category": category,
       "proposedRepairActions": proposedRepairActions,
       "additionalText": additionalText,
       "emsCorrelationId": emsCorrelationId,
       "neCorrelationId": neCorrelationId,
       "emsAuditTable": emsAuditTable,
       "emsAuditEntry": emsAuditEntry,
       "auditEmsNotificationId": auditEmsNotificationId,
       "auditNeNotificationId": auditNeNotificationId,
       "auditEmsTime": auditEmsTime,
       "auditNeTime": auditNeTime,
       "auditEmsName": auditEmsName,
       "auditNeName": auditNeName,
       "auditNeNodeId": auditNeNodeId,
       "auditObjectType": auditObjectType,
       "auditObjectName": auditObjectName,
       "auditAccountName": auditAccountName,
       "auditClientHostName": auditClientHostName,
       "auditOperationName": auditOperationName,
       "auditOperationStatus": auditOperationStatus,
       "auditParamList": auditParamList,
       "emsAdminTable": emsAdminTable,
       "emsAdminEntry": emsAdminEntry,
       "adminEmsNotificationId": adminEmsNotificationId,
       "adminNeNotificationId": adminNeNotificationId,
       "adminEmsTime": adminEmsTime,
       "adminNeTime": adminNeTime,
       "adminEmsName": adminEmsName,
       "adminNeName": adminNeName,
       "adminNeNodeId": adminNeNodeId,
       "adminObjectType": adminObjectType,
       "adminObjectName": adminObjectName,
       "adminCause": adminCause,
       "emsSecurityTable": emsSecurityTable,
       "emsSecurityEntry": emsSecurityEntry,
       "securityEmsNotificationId": securityEmsNotificationId,
       "securityNeNotificationId": securityNeNotificationId,
       "securityEmsTime": securityEmsTime,
       "securityNeTime": securityNeTime,
       "securityEmsName": securityEmsName,
       "securityNeName": securityNeName,
       "securityNeNodeId": securityNeNodeId,
       "securityObjectType": securityObjectType,
       "securityObjectName": securityObjectName,
       "securityAccountName": securityAccountName,
       "securityClientHostName": securityClientHostName,
       "securityCause": securityCause,
       "emsTCATable": emsTCATable,
       "emsTCAEntry": emsTCAEntry,
       "tcaEmsNotificationId": tcaEmsNotificationId,
       "tcaNeNotificationId": tcaNeNotificationId,
       "tcaEmsTime": tcaEmsTime,
       "tcaNeTime": tcaNeTime,
       "tcaEmsName": tcaEmsName,
       "tcaNeName": tcaNeName,
       "tcaNeNodeId": tcaNeNodeId,
       "tcaObjectType": tcaObjectType,
       "tcaObjectName": tcaObjectName,
       "tcaClearableState": tcaClearableState,
       "tcaParameterName": tcaParameterName,
       "tcaLocation": tcaLocation,
       "tcaThresholdType": tcaThresholdType,
       "tcaThresholdValue": tcaThresholdValue,
       "tcaCurrentValue": tcaCurrentValue,
       "tcaGranularity": tcaGranularity,
       "tcaPerceivedSeverity": tcaPerceivedSeverity,
       "tcaAssertedSeverity": tcaAssertedSeverity,
       "tcaNeCorrelationId": tcaNeCorrelationId}
)
