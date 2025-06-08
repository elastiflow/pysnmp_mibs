# SNMP MIB module (TROPIC-GMPLS-DPIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-GMPLS-DPIF-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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

(tnGmplsMIBModules,
 tnGmplsObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnGmplsMIBModules",
    "tnGmplsObjs")


# MODULE-IDENTITY

tnGmplsDpifMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    tnGmplsDpifMibModule.setRevisions(
        ("2013-06-27 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnGmplsDpifMIB_ObjectIdentity = ObjectIdentity
tnGmplsDpifMIB = _TnGmplsDpifMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2)
)
_TnGmplsDpifObjs_ObjectIdentity = ObjectIdentity
tnGmplsDpifObjs = _TnGmplsDpifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1)
)
_TnGmplsDpifAttributeTotal_Type = Integer32
_TnGmplsDpifAttributeTotal_Object = MibScalar
tnGmplsDpifAttributeTotal = _TnGmplsDpifAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 1),
    _TnGmplsDpifAttributeTotal_Type()
)
tnGmplsDpifAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsDpifAttributeTotal.setStatus("current")
_TnGmplsDBLinkTable_Object = MibTable
tnGmplsDBLinkTable = _TnGmplsDBLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnGmplsDBLinkTable.setStatus("current")
_TnGmplsDBLinkEntry_Object = MibTableRow
tnGmplsDBLinkEntry = _TnGmplsDBLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1)
)
tnGmplsDBLinkEntry.setIndexNames(
    (0, "TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkIfId"),
)
if mibBuilder.loadTexts:
    tnGmplsDBLinkEntry.setStatus("current")
_TnGmplsDBLinkIfId_Type = Unsigned32
_TnGmplsDBLinkIfId_Object = MibTableColumn
tnGmplsDBLinkIfId = _TnGmplsDBLinkIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 1),
    _TnGmplsDBLinkIfId_Type()
)
tnGmplsDBLinkIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsDBLinkIfId.setStatus("current")
_TnGmplsDBLinkRemoteIfId_Type = Unsigned32
_TnGmplsDBLinkRemoteIfId_Object = MibTableColumn
tnGmplsDBLinkRemoteIfId = _TnGmplsDBLinkRemoteIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 2),
    _TnGmplsDBLinkRemoteIfId_Type()
)
tnGmplsDBLinkRemoteIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkRemoteIfId.setStatus("current")
_TnGmplsDBLinkName_Type = DisplayString
_TnGmplsDBLinkName_Object = MibTableColumn
tnGmplsDBLinkName = _TnGmplsDBLinkName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 3),
    _TnGmplsDBLinkName_Type()
)
tnGmplsDBLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkName.setStatus("current")


class _TnGmplsDBLinkType_Type(Integer32):
    """Custom type tnGmplsDBLinkType based on Integer32"""
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
        *(("drop", 1),
          ("nni", 2),
          ("enni", 3),
          ("ennig", 4),
          ("uni", 5),
          ("unistar", 6),
          ("regen3R", 7))
    )


_TnGmplsDBLinkType_Type.__name__ = "Integer32"
_TnGmplsDBLinkType_Object = MibTableColumn
tnGmplsDBLinkType = _TnGmplsDBLinkType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 4),
    _TnGmplsDBLinkType_Type()
)
tnGmplsDBLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkType.setStatus("current")
_TnGmplsDBLinkTEId_Type = Unsigned32
_TnGmplsDBLinkTEId_Object = MibTableColumn
tnGmplsDBLinkTEId = _TnGmplsDBLinkTEId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 5),
    _TnGmplsDBLinkTEId_Type()
)
tnGmplsDBLinkTEId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkTEId.setStatus("current")


class _TnGmplsDBLinkACD_Type(Integer32):
    """Custom type tnGmplsDBLinkACD based on Integer32"""
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
        *(("empty", 1),
          ("cp", 2),
          ("cpmp", 3),
          ("mp", 4))
    )


_TnGmplsDBLinkACD_Type.__name__ = "Integer32"
_TnGmplsDBLinkACD_Object = MibTableColumn
tnGmplsDBLinkACD = _TnGmplsDBLinkACD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 6),
    _TnGmplsDBLinkACD_Type()
)
tnGmplsDBLinkACD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkACD.setStatus("current")
_TnGmplsDBLinkUseInFiber_Type = TruthValue
_TnGmplsDBLinkUseInFiber_Object = MibTableColumn
tnGmplsDBLinkUseInFiber = _TnGmplsDBLinkUseInFiber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 7),
    _TnGmplsDBLinkUseInFiber_Type()
)
tnGmplsDBLinkUseInFiber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkUseInFiber.setStatus("current")
_TnGmplsDBLinkWTR_Type = Unsigned32
_TnGmplsDBLinkWTR_Object = MibTableColumn
tnGmplsDBLinkWTR = _TnGmplsDBLinkWTR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 8),
    _TnGmplsDBLinkWTR_Type()
)
tnGmplsDBLinkWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkWTR.setStatus("current")


class _TnGmplsDBLinkAdminStatus_Type(Integer32):
    """Custom type tnGmplsDBLinkAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("shuttingdown", 3))
    )


_TnGmplsDBLinkAdminStatus_Type.__name__ = "Integer32"
_TnGmplsDBLinkAdminStatus_Object = MibTableColumn
tnGmplsDBLinkAdminStatus = _TnGmplsDBLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 9),
    _TnGmplsDBLinkAdminStatus_Type()
)
tnGmplsDBLinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkAdminStatus.setStatus("current")


class _TnGmplsDBLinkOperationalState_Type(Integer32):
    """Custom type tnGmplsDBLinkOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsDBLinkOperationalState_Type.__name__ = "Integer32"
_TnGmplsDBLinkOperationalState_Object = MibTableColumn
tnGmplsDBLinkOperationalState = _TnGmplsDBLinkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 10),
    _TnGmplsDBLinkOperationalState_Type()
)
tnGmplsDBLinkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsDBLinkOperationalState.setStatus("current")


class _TnGmplsDBLinkMaintState_Type(Integer32):
    """Custom type tnGmplsDBLinkMaintState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("linkMaintenance", 6))
    )


_TnGmplsDBLinkMaintState_Type.__name__ = "Integer32"
_TnGmplsDBLinkMaintState_Object = MibTableColumn
tnGmplsDBLinkMaintState = _TnGmplsDBLinkMaintState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 11),
    _TnGmplsDBLinkMaintState_Type()
)
tnGmplsDBLinkMaintState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkMaintState.setStatus("current")


class _TnGmplsDBLinkAlarmState_Type(Integer32):
    """Custom type tnGmplsDBLinkAlarmState based on Integer32"""
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
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("localAlarm", 1),
          ("remoteAlarm", 2),
          ("itcAlarm", 3),
          ("hardwareUnavailable", 4),
          ("neUnavailable", 5),
          ("disabled", 6),
          ("dbDown", 7),
          ("allDBDown", 8),
          ("cpDown", 9),
          ("linkSummaryMismatch", 10),
          ("remoteDBDown", 11),
          ("hardwareClash", 12),
          ("otherMgrConnection", 13),
          ("localWTR", 14),
          ("remoteWTR", 15),
          ("localSDAlarm", 16),
          ("remoteSDAlarm", 17),
          ("dbAlarm", 18),
          ("hardwareDegraded", 19),
          ("localOTUAlarm", 20),
          ("hardwareUnavailableOTU", 21),
          ("ltcer", 22),
          ("ue", 23),
          ("tca", 24),
          ("noAlarm", 25))
    )


_TnGmplsDBLinkAlarmState_Type.__name__ = "Integer32"
_TnGmplsDBLinkAlarmState_Object = MibTableColumn
tnGmplsDBLinkAlarmState = _TnGmplsDBLinkAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 12),
    _TnGmplsDBLinkAlarmState_Type()
)
tnGmplsDBLinkAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsDBLinkAlarmState.setStatus("current")
_TnGmplsDBLink3RIndex_Type = Unsigned32
_TnGmplsDBLink3RIndex_Object = MibTableColumn
tnGmplsDBLink3RIndex = _TnGmplsDBLink3RIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 13),
    _TnGmplsDBLink3RIndex_Type()
)
tnGmplsDBLink3RIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsDBLink3RIndex.setStatus("current")
_TnGmplsDBLinkRowStatus_Type = RowStatus
_TnGmplsDBLinkRowStatus_Object = MibTableColumn
tnGmplsDBLinkRowStatus = _TnGmplsDBLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 2, 1, 14),
    _TnGmplsDBLinkRowStatus_Type()
)
tnGmplsDBLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsDBLinkRowStatus.setStatus("current")
_TnGmplsTELinkTable_Object = MibTable
tnGmplsTELinkTable = _TnGmplsTELinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnGmplsTELinkTable.setStatus("current")
_TnGmplsTELinkEntry_Object = MibTableRow
tnGmplsTELinkEntry = _TnGmplsTELinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1)
)
tnGmplsTELinkEntry.setIndexNames(
    (0, "TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkIfId"),
)
if mibBuilder.loadTexts:
    tnGmplsTELinkEntry.setStatus("current")


class _TnGmplsTELinkIfId_Type(Unsigned32):
    """Custom type tnGmplsTELinkIfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000, 999999),
    )


_TnGmplsTELinkIfId_Type.__name__ = "Unsigned32"
_TnGmplsTELinkIfId_Object = MibTableColumn
tnGmplsTELinkIfId = _TnGmplsTELinkIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 1),
    _TnGmplsTELinkIfId_Type()
)
tnGmplsTELinkIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsTELinkIfId.setStatus("current")
_TnGmplsTELinkRemoteIfId_Type = Unsigned32
_TnGmplsTELinkRemoteIfId_Object = MibTableColumn
tnGmplsTELinkRemoteIfId = _TnGmplsTELinkRemoteIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 2),
    _TnGmplsTELinkRemoteIfId_Type()
)
tnGmplsTELinkRemoteIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkRemoteIfId.setStatus("current")
_TnGmplsTELinkRemoteSubnodeId_Type = Unsigned32
_TnGmplsTELinkRemoteSubnodeId_Object = MibTableColumn
tnGmplsTELinkRemoteSubnodeId = _TnGmplsTELinkRemoteSubnodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 3),
    _TnGmplsTELinkRemoteSubnodeId_Type()
)
tnGmplsTELinkRemoteSubnodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkRemoteSubnodeId.setStatus("current")
_TnGmplsTELinkRemoteCPNodeId_Type = InetAddressIPv4
_TnGmplsTELinkRemoteCPNodeId_Object = MibTableColumn
tnGmplsTELinkRemoteCPNodeId = _TnGmplsTELinkRemoteCPNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 4),
    _TnGmplsTELinkRemoteCPNodeId_Type()
)
tnGmplsTELinkRemoteCPNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkRemoteCPNodeId.setStatus("current")
_TnGmplsTELinkTNA_Type = InetAddressIPv4
_TnGmplsTELinkTNA_Object = MibTableColumn
tnGmplsTELinkTNA = _TnGmplsTELinkTNA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 5),
    _TnGmplsTELinkTNA_Type()
)
tnGmplsTELinkTNA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkTNA.setStatus("current")
_TnGmplsTELinkName_Type = DisplayString
_TnGmplsTELinkName_Object = MibTableColumn
tnGmplsTELinkName = _TnGmplsTELinkName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 6),
    _TnGmplsTELinkName_Type()
)
tnGmplsTELinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkName.setStatus("current")


class _TnGmplsTELinkMetric_Type(Unsigned32):
    """Custom type tnGmplsTELinkMetric based on Unsigned32"""
    defaultValue = 20


_TnGmplsTELinkMetric_Type.__name__ = "Unsigned32"
_TnGmplsTELinkMetric_Object = MibTableColumn
tnGmplsTELinkMetric = _TnGmplsTELinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 7),
    _TnGmplsTELinkMetric_Type()
)
tnGmplsTELinkMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkMetric.setStatus("current")


class _TnGmplsTELinkColor_Type(Unsigned32):
    """Custom type tnGmplsTELinkColor based on Unsigned32"""
    defaultValue = 0


_TnGmplsTELinkColor_Type.__name__ = "Unsigned32"
_TnGmplsTELinkColor_Object = MibTableColumn
tnGmplsTELinkColor = _TnGmplsTELinkColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 8),
    _TnGmplsTELinkColor_Type()
)
tnGmplsTELinkColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkColor.setStatus("current")
_TnGmplsTELinkSRLG_Type = DisplayString
_TnGmplsTELinkSRLG_Object = MibTableColumn
tnGmplsTELinkSRLG = _TnGmplsTELinkSRLG_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 9),
    _TnGmplsTELinkSRLG_Type()
)
tnGmplsTELinkSRLG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkSRLG.setStatus("current")


class _TnGmplsTELinkLatency_Type(Unsigned32):
    """Custom type tnGmplsTELinkLatency based on Unsigned32"""
    defaultValue = 0


_TnGmplsTELinkLatency_Type.__name__ = "Unsigned32"
_TnGmplsTELinkLatency_Object = MibTableColumn
tnGmplsTELinkLatency = _TnGmplsTELinkLatency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 10),
    _TnGmplsTELinkLatency_Type()
)
tnGmplsTELinkLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkLatency.setStatus("current")


class _TnGmplsTELinkAdminStatus_Type(Integer32):
    """Custom type tnGmplsTELinkAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("shuttingdown", 3))
    )


_TnGmplsTELinkAdminStatus_Type.__name__ = "Integer32"
_TnGmplsTELinkAdminStatus_Object = MibTableColumn
tnGmplsTELinkAdminStatus = _TnGmplsTELinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 11),
    _TnGmplsTELinkAdminStatus_Type()
)
tnGmplsTELinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkAdminStatus.setStatus("current")


class _TnGmplsTELinkOperationalState_Type(Integer32):
    """Custom type tnGmplsTELinkOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsTELinkOperationalState_Type.__name__ = "Integer32"
_TnGmplsTELinkOperationalState_Object = MibTableColumn
tnGmplsTELinkOperationalState = _TnGmplsTELinkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 12),
    _TnGmplsTELinkOperationalState_Type()
)
tnGmplsTELinkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsTELinkOperationalState.setStatus("current")


class _TnGmplsTELinkMaintState_Type(Integer32):
    """Custom type tnGmplsTELinkMaintState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("linkMaintenance", 6))
    )


_TnGmplsTELinkMaintState_Type.__name__ = "Integer32"
_TnGmplsTELinkMaintState_Object = MibTableColumn
tnGmplsTELinkMaintState = _TnGmplsTELinkMaintState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 13),
    _TnGmplsTELinkMaintState_Type()
)
tnGmplsTELinkMaintState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkMaintState.setStatus("current")


class _TnGmplsTELinkAlarmState_Type(Integer32):
    """Custom type tnGmplsTELinkAlarmState based on Integer32"""
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
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("localAlarm", 1),
          ("remoteAlarm", 2),
          ("itcAlarm", 3),
          ("hardwareUnavailable", 4),
          ("neUnavailable", 5),
          ("disabled", 6),
          ("dbDown", 7),
          ("allDBDown", 8),
          ("cpDown", 9),
          ("linkSummaryMismatch", 10),
          ("remoteDBDown", 11),
          ("hardwareClash", 12),
          ("otherMgrConnection", 13),
          ("localWTR", 14),
          ("remoteWTR", 15),
          ("localSDAlarm", 16),
          ("remoteSDAlarm", 17),
          ("dbAlarm", 18),
          ("hardwareDegraded", 19),
          ("localOTUAlarm", 20),
          ("hardwareUnavailableOTU", 21),
          ("ltcer", 22),
          ("ue", 23),
          ("tca", 24),
          ("noAlarm", 25))
    )


_TnGmplsTELinkAlarmState_Type.__name__ = "Integer32"
_TnGmplsTELinkAlarmState_Object = MibTableColumn
tnGmplsTELinkAlarmState = _TnGmplsTELinkAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 14),
    _TnGmplsTELinkAlarmState_Type()
)
tnGmplsTELinkAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsTELinkAlarmState.setStatus("current")
_TnGmplsTELinkRowStatus_Type = RowStatus
_TnGmplsTELinkRowStatus_Object = MibTableColumn
tnGmplsTELinkRowStatus = _TnGmplsTELinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 1, 3, 1, 15),
    _TnGmplsTELinkRowStatus_Type()
)
tnGmplsTELinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsTELinkRowStatus.setStatus("current")
_TnGmplsDpifConf_ObjectIdentity = ObjectIdentity
tnGmplsDpifConf = _TnGmplsDpifConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 3)
)
_TnGmplsDpifGroups_ObjectIdentity = ObjectIdentity
tnGmplsDpifGroups = _TnGmplsDpifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 3, 1)
)
_TnGmplsDpifCompliances_ObjectIdentity = ObjectIdentity
tnGmplsDpifCompliances = _TnGmplsDpifCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 3, 2)
)

# Managed Objects groups

tnGmplsDpifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 3, 1, 1)
)
tnGmplsDpifObjsGroup.setObjects(
    ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDpifAttributeTotal")
)
if mibBuilder.loadTexts:
    tnGmplsDpifObjsGroup.setStatus("current")

tnGmplsDBLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 3, 1, 2)
)
tnGmplsDBLinkGroup.setObjects(
      *(("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkIfId"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkRemoteIfId"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkName"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkType"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkTEId"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkACD"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkUseInFiber"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkWTR"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkAdminStatus"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkOperationalState"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkMaintState"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkAlarmState"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLink3RIndex"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsDBLinkGroup.setStatus("current")

tnGmplsTELinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 3, 1, 3)
)
tnGmplsTELinkGroup.setObjects(
      *(("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkIfId"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkRemoteIfId"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkRemoteSubnodeId"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkRemoteCPNodeId"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkTNA"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkName"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkMetric"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkColor"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkSRLG"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkLatency"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkAdminStatus"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkOperationalState"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkMaintState"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkAlarmState"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsTELinkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnGmplsDpifCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 2, 3, 2, 1)
)
tnGmplsDpifCompliance.setObjects(
      *(("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDpifObjsGroup"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsTELinkGroup"),
        ("TROPIC-GMPLS-DPIF-MIB", "tnGmplsDBLinkGroup"))
)
if mibBuilder.loadTexts:
    tnGmplsDpifCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GMPLS-DPIF-MIB",
    **{"tnGmplsDpifMibModule": tnGmplsDpifMibModule,
       "tnGmplsDpifMIB": tnGmplsDpifMIB,
       "tnGmplsDpifObjs": tnGmplsDpifObjs,
       "tnGmplsDpifAttributeTotal": tnGmplsDpifAttributeTotal,
       "tnGmplsDBLinkTable": tnGmplsDBLinkTable,
       "tnGmplsDBLinkEntry": tnGmplsDBLinkEntry,
       "tnGmplsDBLinkIfId": tnGmplsDBLinkIfId,
       "tnGmplsDBLinkRemoteIfId": tnGmplsDBLinkRemoteIfId,
       "tnGmplsDBLinkName": tnGmplsDBLinkName,
       "tnGmplsDBLinkType": tnGmplsDBLinkType,
       "tnGmplsDBLinkTEId": tnGmplsDBLinkTEId,
       "tnGmplsDBLinkACD": tnGmplsDBLinkACD,
       "tnGmplsDBLinkUseInFiber": tnGmplsDBLinkUseInFiber,
       "tnGmplsDBLinkWTR": tnGmplsDBLinkWTR,
       "tnGmplsDBLinkAdminStatus": tnGmplsDBLinkAdminStatus,
       "tnGmplsDBLinkOperationalState": tnGmplsDBLinkOperationalState,
       "tnGmplsDBLinkMaintState": tnGmplsDBLinkMaintState,
       "tnGmplsDBLinkAlarmState": tnGmplsDBLinkAlarmState,
       "tnGmplsDBLink3RIndex": tnGmplsDBLink3RIndex,
       "tnGmplsDBLinkRowStatus": tnGmplsDBLinkRowStatus,
       "tnGmplsTELinkTable": tnGmplsTELinkTable,
       "tnGmplsTELinkEntry": tnGmplsTELinkEntry,
       "tnGmplsTELinkIfId": tnGmplsTELinkIfId,
       "tnGmplsTELinkRemoteIfId": tnGmplsTELinkRemoteIfId,
       "tnGmplsTELinkRemoteSubnodeId": tnGmplsTELinkRemoteSubnodeId,
       "tnGmplsTELinkRemoteCPNodeId": tnGmplsTELinkRemoteCPNodeId,
       "tnGmplsTELinkTNA": tnGmplsTELinkTNA,
       "tnGmplsTELinkName": tnGmplsTELinkName,
       "tnGmplsTELinkMetric": tnGmplsTELinkMetric,
       "tnGmplsTELinkColor": tnGmplsTELinkColor,
       "tnGmplsTELinkSRLG": tnGmplsTELinkSRLG,
       "tnGmplsTELinkLatency": tnGmplsTELinkLatency,
       "tnGmplsTELinkAdminStatus": tnGmplsTELinkAdminStatus,
       "tnGmplsTELinkOperationalState": tnGmplsTELinkOperationalState,
       "tnGmplsTELinkMaintState": tnGmplsTELinkMaintState,
       "tnGmplsTELinkAlarmState": tnGmplsTELinkAlarmState,
       "tnGmplsTELinkRowStatus": tnGmplsTELinkRowStatus,
       "tnGmplsDpifConf": tnGmplsDpifConf,
       "tnGmplsDpifGroups": tnGmplsDpifGroups,
       "tnGmplsDpifObjsGroup": tnGmplsDpifObjsGroup,
       "tnGmplsDBLinkGroup": tnGmplsDBLinkGroup,
       "tnGmplsTELinkGroup": tnGmplsTELinkGroup,
       "tnGmplsDpifCompliances": tnGmplsDpifCompliances,
       "tnGmplsDpifCompliance": tnGmplsDpifCompliance}
)
