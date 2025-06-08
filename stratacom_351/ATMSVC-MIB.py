# SNMP MIB module (ATMSVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/ATMSVC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:03:53 2025
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

(lastSequenceNumber,) = mibBuilder.importSymbols(
    "RTM-MIB",
    "lastSequenceNumber")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_InsAgents_ObjectIdentity = ObjectIdentity
insAgents = _InsAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200)
)
_Ins_ObjectIdentity = ObjectIdentity
ins = _Ins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1)
)
_Aps_ObjectIdentity = ObjectIdentity
aps = _Aps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10)
)
_ApsTrapSupportGroup_ObjectIdentity = ObjectIdentity
apsTrapSupportGroup = _ApsTrapSupportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1)
)


class _ApsName_Type(DisplayString):
    """Custom type apsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ApsName_Type.__name__ = "DisplayString"
_ApsName_Object = MibScalar
apsName = _ApsName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 1),
    _ApsName_Type()
)
apsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsName.setStatus("mandatory")


class _ApsAdminStatus_Type(Integer32):
    """Custom type apsAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("outOfService", 1),
          ("inService", 2))
    )


_ApsAdminStatus_Type.__name__ = "Integer32"
_ApsAdminStatus_Object = MibScalar
apsAdminStatus = _ApsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 2),
    _ApsAdminStatus_Type()
)
apsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsAdminStatus.setStatus("mandatory")


class _ApsOperStatus_Type(Integer32):
    """Custom type apsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("outOfService", 1),
          ("inService", 2))
    )


_ApsOperStatus_Type.__name__ = "Integer32"
_ApsOperStatus_Object = MibScalar
apsOperStatus = _ApsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 3),
    _ApsOperStatus_Type()
)
apsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsOperStatus.setStatus("mandatory")


class _ApsAdminRole_Type(Integer32):
    """Custom type apsAdminRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("standby", 2),
          ("standalone", 3))
    )


_ApsAdminRole_Type.__name__ = "Integer32"
_ApsAdminRole_Object = MibScalar
apsAdminRole = _ApsAdminRole_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 4),
    _ApsAdminRole_Type()
)
apsAdminRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsAdminRole.setStatus("mandatory")


class _ApsOperRole_Type(Integer32):
    """Custom type apsOperRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("standby", 2),
          ("standalone", 3))
    )


_ApsOperRole_Type.__name__ = "Integer32"
_ApsOperRole_Object = MibScalar
apsOperRole = _ApsOperRole_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 5),
    _ApsOperRole_Type()
)
apsOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsOperRole.setStatus("mandatory")


class _ApsNodeName_Type(DisplayString):
    """Custom type apsNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ApsNodeName_Type.__name__ = "DisplayString"
_ApsNodeName_Object = MibScalar
apsNodeName = _ApsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 6),
    _ApsNodeName_Type()
)
apsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsNodeName.setStatus("mandatory")
_ApsPortDesc_Type = Integer32
_ApsPortDesc_Object = MibScalar
apsPortDesc = _ApsPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 7),
    _ApsPortDesc_Type()
)
apsPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPortDesc.setStatus("mandatory")


class _ApsPortType_Type(Integer32):
    """Custom type apsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni30", 0),
          ("uni31", 1),
          ("uni40", 2),
          ("iisp", 3))
    )


_ApsPortType_Type.__name__ = "Integer32"
_ApsPortType_Object = MibScalar
apsPortType = _ApsPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 8),
    _ApsPortType_Type()
)
apsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPortType.setStatus("mandatory")


class _ApsShelfName_Type(DisplayString):
    """Custom type apsShelfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ApsShelfName_Type.__name__ = "DisplayString"
_ApsShelfName_Object = MibScalar
apsShelfName = _ApsShelfName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 9),
    _ApsShelfName_Type()
)
apsShelfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsShelfName.setStatus("mandatory")
_ApsCardDesc_Type = Integer32
_ApsCardDesc_Object = MibScalar
apsCardDesc = _ApsCardDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 10),
    _ApsCardDesc_Type()
)
apsCardDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsCardDesc.setStatus("mandatory")


class _ConfigFailureCause_Type(Integer32):
    """Custom type configFailureCause based on Integer32"""
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
        *(("readSocketErr", 1),
          ("writeSocketErr", 2),
          ("otherSocketErr", 3),
          ("readDbErr", 4),
          ("writeDbErr", 5),
          ("otherDbErr", 6))
    )


_ConfigFailureCause_Type.__name__ = "Integer32"
_ConfigFailureCause_Object = MibScalar
configFailureCause = _ConfigFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 11),
    _ConfigFailureCause_Type()
)
configFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFailureCause.setStatus("mandatory")


class _AggregateSeverity_Type(Integer32):
    """Custom type aggregateSeverity based on Integer32"""
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
        *(("informational", 1),
          ("minor", 2),
          ("major", 3),
          ("fatal", 4))
    )


_AggregateSeverity_Type.__name__ = "Integer32"
_AggregateSeverity_Object = MibScalar
aggregateSeverity = _AggregateSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 12),
    _AggregateSeverity_Type()
)
aggregateSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateSeverity.setStatus("mandatory")


class _RednApsName_Type(DisplayString):
    """Custom type rednApsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RednApsName_Type.__name__ = "DisplayString"
_RednApsName_Object = MibScalar
rednApsName = _RednApsName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 13),
    _RednApsName_Type()
)
rednApsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rednApsName.setStatus("mandatory")


class _ApsLayerName_Type(DisplayString):
    """Custom type apsLayerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ApsLayerName_Type.__name__ = "DisplayString"
_ApsLayerName_Object = MibScalar
apsLayerName = _ApsLayerName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 1, 14),
    _ApsLayerName_Type()
)
apsLayerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsLayerName.setStatus("mandatory")
_ApsTraps_ObjectIdentity = ObjectIdentity
apsTraps = _ApsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2)
)
_ApsTrapSeverityTable_Object = MibTable
apsTrapSeverityTable = _ApsTrapSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    apsTrapSeverityTable.setStatus("mandatory")
_ApsTrapSeverityEntry_Object = MibTableRow
apsTrapSeverityEntry = _ApsTrapSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 1, 1)
)
apsTrapSeverityEntry.setIndexNames(
    (0, "ATMSVC-MIB", "apsTrapIndex"),
)
if mibBuilder.loadTexts:
    apsTrapSeverityEntry.setStatus("mandatory")


class _ApsTrapIndex_Type(Integer32):
    """Custom type apsTrapIndex based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("apsStartUpTrap", 1),
          ("apsStateDown", 2),
          ("apsStateUp", 3),
          ("apsRoleChange", 4),
          ("rednApsNotAvailable", 5),
          ("rednApsAvailable", 6),
          ("apsNodeDown", 7),
          ("apsNodeUp", 8),
          ("apsPortDown", 9),
          ("apsPortUp", 10),
          ("axisShelfDown", 11),
          ("axisShelfUp", 12),
          ("slotVccFail", 13),
          ("slotVccUp", 14),
          ("annexGFail", 15),
          ("dbConfigError", 16),
          ("aggregateStatus", 17))
    )


_ApsTrapIndex_Type.__name__ = "Integer32"
_ApsTrapIndex_Object = MibTableColumn
apsTrapIndex = _ApsTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 1, 1, 1),
    _ApsTrapIndex_Type()
)
apsTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTrapIndex.setStatus("mandatory")


class _ApsTrapSeverity_Type(Integer32):
    """Custom type apsTrapSeverity based on Integer32"""
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
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_ApsTrapSeverity_Type.__name__ = "Integer32"
_ApsTrapSeverity_Object = MibTableColumn
apsTrapSeverity = _ApsTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 1, 1, 2),
    _ApsTrapSeverity_Type()
)
apsTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTrapSeverity.setStatus("mandatory")
_ApsTrapTimeStamp_Type = TimeTicks
_ApsTrapTimeStamp_Object = MibTableColumn
apsTrapTimeStamp = _ApsTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 1, 1, 3),
    _ApsTrapTimeStamp_Type()
)
apsTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTrapTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nicRdwrError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8020)
)
nicRdwrError.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"))
)
if mibBuilder.loadTexts:
    nicRdwrError.setStatus(
        ""
    )

nicRdwrOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8021)
)
nicRdwrOk.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"))
)
if mibBuilder.loadTexts:
    nicRdwrOk.setStatus(
        ""
    )

frQ922LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8022)
)
frQ922LinkDown.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsShelfName"))
)
if mibBuilder.loadTexts:
    frQ922LinkDown.setStatus(
        ""
    )

frQ922LinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8023)
)
frQ922LinkUp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsShelfName"))
)
if mibBuilder.loadTexts:
    frQ922LinkUp.setStatus(
        ""
    )

sigPvcBldFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8024)
)
sigPvcBldFail.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsPortDesc"),
        ("ATMSVC-MIB", "apsPortType"))
)
if mibBuilder.loadTexts:
    sigPvcBldFail.setStatus(
        ""
    )

frProtocolError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8025)
)
frProtocolError.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsShelfName"),
        ("ATMSVC-MIB", "apsLayerName"))
)
if mibBuilder.loadTexts:
    frProtocolError.setStatus(
        ""
    )

frStackEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8026)
)
frStackEnabled.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsPortDesc"),
        ("ATMSVC-MIB", "apsPortType"))
)
if mibBuilder.loadTexts:
    frStackEnabled.setStatus(
        ""
    )

frStackDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8027)
)
frStackDisabled.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsPortDesc"),
        ("ATMSVC-MIB", "apsPortType"))
)
if mibBuilder.loadTexts:
    frStackDisabled.setStatus(
        ""
    )

sysResFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8028)
)
sysResFail.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"))
)
if mibBuilder.loadTexts:
    sysResFail.setStatus(
        ""
    )

nicOpenError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8029)
)
nicOpenError.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"))
)
if mibBuilder.loadTexts:
    nicOpenError.setStatus(
        ""
    )

nicVccError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 0, 8030)
)
nicVccError.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"))
)
if mibBuilder.loadTexts:
    nicVccError.setStatus(
        ""
    )

apsStartUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8000)
)
apsStartUpTrap.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsOperStatus"),
        ("ATMSVC-MIB", "apsOperRole"))
)
if mibBuilder.loadTexts:
    apsStartUpTrap.setStatus(
        ""
    )

apsStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8001)
)
apsStateDown.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"))
)
if mibBuilder.loadTexts:
    apsStateDown.setStatus(
        ""
    )

apsStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8002)
)
apsStateUp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"))
)
if mibBuilder.loadTexts:
    apsStateUp.setStatus(
        ""
    )

apsRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8003)
)
apsRoleChange.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsOperRole"))
)
if mibBuilder.loadTexts:
    apsRoleChange.setStatus(
        ""
    )

rednApsNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8004)
)
rednApsNotAvailable.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "rednApsName"))
)
if mibBuilder.loadTexts:
    rednApsNotAvailable.setStatus(
        ""
    )

rednApsAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8005)
)
rednApsAvailable.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "rednApsName"))
)
if mibBuilder.loadTexts:
    rednApsAvailable.setStatus(
        ""
    )

apsNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8006)
)
apsNodeDown.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsNodeName"))
)
if mibBuilder.loadTexts:
    apsNodeDown.setStatus(
        ""
    )

apsNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8007)
)
apsNodeUp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsNodeName"))
)
if mibBuilder.loadTexts:
    apsNodeUp.setStatus(
        ""
    )

apsPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8008)
)
apsPortDown.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsPortDesc"),
        ("ATMSVC-MIB", "apsPortType"))
)
if mibBuilder.loadTexts:
    apsPortDown.setStatus(
        ""
    )

apsPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8009)
)
apsPortUp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsPortDesc"),
        ("ATMSVC-MIB", "apsPortType"))
)
if mibBuilder.loadTexts:
    apsPortUp.setStatus(
        ""
    )

axisShelfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8010)
)
axisShelfDown.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsShelfName"))
)
if mibBuilder.loadTexts:
    axisShelfDown.setStatus(
        ""
    )

axisShelfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8011)
)
axisShelfUp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsShelfName"))
)
if mibBuilder.loadTexts:
    axisShelfUp.setStatus(
        ""
    )

slotVccFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8012)
)
slotVccFail.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsNodeName"),
        ("ATMSVC-MIB", "apsCardDesc"))
)
if mibBuilder.loadTexts:
    slotVccFail.setStatus(
        ""
    )

slotVccUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8013)
)
slotVccUp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsNodeName"),
        ("ATMSVC-MIB", "apsCardDesc"))
)
if mibBuilder.loadTexts:
    slotVccUp.setStatus(
        ""
    )

annexGFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8014)
)
annexGFail.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "apsNodeName"))
)
if mibBuilder.loadTexts:
    annexGFail.setStatus(
        ""
    )

dbConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8015)
)
dbConfigError.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "configFailureCause"))
)
if mibBuilder.loadTexts:
    dbConfigError.setStatus(
        ""
    )

aggregateStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 10, 2, 0, 8016)
)
aggregateStatus.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("ATMSVC-MIB", "apsName"),
        ("ATMSVC-MIB", "apsTrapTimeStamp"),
        ("ATMSVC-MIB", "apsTrapSeverity"),
        ("ATMSVC-MIB", "aggregateSeverity"))
)
if mibBuilder.loadTexts:
    aggregateStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATMSVC-MIB",
    **{"stratacom": stratacom,
       "insAgents": insAgents,
       "ins": ins,
       "nicRdwrError": nicRdwrError,
       "nicRdwrOk": nicRdwrOk,
       "frQ922LinkDown": frQ922LinkDown,
       "frQ922LinkUp": frQ922LinkUp,
       "sigPvcBldFail": sigPvcBldFail,
       "frProtocolError": frProtocolError,
       "frStackEnabled": frStackEnabled,
       "frStackDisabled": frStackDisabled,
       "sysResFail": sysResFail,
       "nicOpenError": nicOpenError,
       "nicVccError": nicVccError,
       "aps": aps,
       "apsTrapSupportGroup": apsTrapSupportGroup,
       "apsName": apsName,
       "apsAdminStatus": apsAdminStatus,
       "apsOperStatus": apsOperStatus,
       "apsAdminRole": apsAdminRole,
       "apsOperRole": apsOperRole,
       "apsNodeName": apsNodeName,
       "apsPortDesc": apsPortDesc,
       "apsPortType": apsPortType,
       "apsShelfName": apsShelfName,
       "apsCardDesc": apsCardDesc,
       "configFailureCause": configFailureCause,
       "aggregateSeverity": aggregateSeverity,
       "rednApsName": rednApsName,
       "apsLayerName": apsLayerName,
       "apsTraps": apsTraps,
       "apsStartUpTrap": apsStartUpTrap,
       "apsStateDown": apsStateDown,
       "apsStateUp": apsStateUp,
       "apsRoleChange": apsRoleChange,
       "rednApsNotAvailable": rednApsNotAvailable,
       "rednApsAvailable": rednApsAvailable,
       "apsNodeDown": apsNodeDown,
       "apsNodeUp": apsNodeUp,
       "apsPortDown": apsPortDown,
       "apsPortUp": apsPortUp,
       "axisShelfDown": axisShelfDown,
       "axisShelfUp": axisShelfUp,
       "slotVccFail": slotVccFail,
       "slotVccUp": slotVccUp,
       "annexGFail": annexGFail,
       "dbConfigError": dbConfigError,
       "aggregateStatus": aggregateStatus,
       "apsTrapSeverityTable": apsTrapSeverityTable,
       "apsTrapSeverityEntry": apsTrapSeverityEntry,
       "apsTrapIndex": apsTrapIndex,
       "apsTrapSeverity": apsTrapSeverity,
       "apsTrapTimeStamp": apsTrapTimeStamp}
)
