# SNMP MIB module (TROPIC-GMPLS-LSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-GMPLS-LSP-MIB.mib
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

tnGmplsLspMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    tnGmplsLspMibModule.setRevisions(
        ("2013-08-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmGmplsLspProtectionState(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("normal", 2),
          ("failed", 3),
          ("noBackup", 4),
          ("restored", 5),
          ("restoredNoBackup", 6),
          ("apeInProgress", 7),
          ("failedButConnected", 8),
          ("restoring", 9),
          ("failedNoReroutePossible", 10),
          ("prepareSoftReroute", 11),
          ("softReroutingInProgress", 12))
    )



# MIB Managed Objects in the order of their OIDs

_TnGmplsLspMIB_ObjectIdentity = ObjectIdentity
tnGmplsLspMIB = _TnGmplsLspMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3)
)
_TnGmplsLspObjs_ObjectIdentity = ObjectIdentity
tnGmplsLspObjs = _TnGmplsLspObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1)
)
_TnGmplsLspAttributeTotal_Type = Integer32
_TnGmplsLspAttributeTotal_Object = MibScalar
tnGmplsLspAttributeTotal = _TnGmplsLspAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 1),
    _TnGmplsLspAttributeTotal_Type()
)
tnGmplsLspAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspAttributeTotal.setStatus("current")
_TnGmplsLspTable_Object = MibTable
tnGmplsLspTable = _TnGmplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tnGmplsLspTable.setStatus("current")
_TnGmplsLspEntry_Object = MibTableRow
tnGmplsLspEntry = _TnGmplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1)
)
tnGmplsLspEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSrcLspId"),
)
if mibBuilder.loadTexts:
    tnGmplsLspEntry.setStatus("current")
_TnGmplsLspSrcLspId_Type = Unsigned32
_TnGmplsLspSrcLspId_Object = MibTableColumn
tnGmplsLspSrcLspId = _TnGmplsLspSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 1),
    _TnGmplsLspSrcLspId_Type()
)
tnGmplsLspSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspSrcLspId.setStatus("current")
_TnGmplsLspDescr_Type = DisplayString
_TnGmplsLspDescr_Object = MibTableColumn
tnGmplsLspDescr = _TnGmplsLspDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 2),
    _TnGmplsLspDescr_Type()
)
tnGmplsLspDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspDescr.setStatus("current")
_TnGmplsLspIngressResource_Type = DisplayString
_TnGmplsLspIngressResource_Object = MibTableColumn
tnGmplsLspIngressResource = _TnGmplsLspIngressResource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 3),
    _TnGmplsLspIngressResource_Type()
)
tnGmplsLspIngressResource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspIngressResource.setStatus("current")
_TnGmplsLspEgressResource_Type = DisplayString
_TnGmplsLspEgressResource_Object = MibTableColumn
tnGmplsLspEgressResource = _TnGmplsLspEgressResource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 4),
    _TnGmplsLspEgressResource_Type()
)
tnGmplsLspEgressResource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspEgressResource.setStatus("current")
_TnGmplsLspDestLsrId_Type = Unsigned32
_TnGmplsLspDestLsrId_Object = MibTableColumn
tnGmplsLspDestLsrId = _TnGmplsLspDestLsrId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 5),
    _TnGmplsLspDestLsrId_Type()
)
tnGmplsLspDestLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspDestLsrId.setStatus("current")


class _TnGmplsLspSetupPrio_Type(Integer32):
    """Custom type tnGmplsLspSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TnGmplsLspSetupPrio_Type.__name__ = "Integer32"
_TnGmplsLspSetupPrio_Object = MibTableColumn
tnGmplsLspSetupPrio = _TnGmplsLspSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 6),
    _TnGmplsLspSetupPrio_Type()
)
tnGmplsLspSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspSetupPrio.setStatus("current")


class _TnGmplsLspHoldingPrio_Type(Integer32):
    """Custom type tnGmplsLspHoldingPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TnGmplsLspHoldingPrio_Type.__name__ = "Integer32"
_TnGmplsLspHoldingPrio_Object = MibTableColumn
tnGmplsLspHoldingPrio = _TnGmplsLspHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 7),
    _TnGmplsLspHoldingPrio_Type()
)
tnGmplsLspHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspHoldingPrio.setStatus("current")


class _TnGmplsLspDirectionType_Type(Integer32):
    """Custom type tnGmplsLspDirectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bidirectional", 1)
    )


_TnGmplsLspDirectionType_Type.__name__ = "Integer32"
_TnGmplsLspDirectionType_Object = MibTableColumn
tnGmplsLspDirectionType = _TnGmplsLspDirectionType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 8),
    _TnGmplsLspDirectionType_Type()
)
tnGmplsLspDirectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspDirectionType.setStatus("current")


class _TnGmplsLspTrafficType_Type(Integer32):
    """Custom type tnGmplsLspTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("och", 8)
    )


_TnGmplsLspTrafficType_Type.__name__ = "Integer32"
_TnGmplsLspTrafficType_Object = MibTableColumn
tnGmplsLspTrafficType = _TnGmplsLspTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 9),
    _TnGmplsLspTrafficType_Type()
)
tnGmplsLspTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspTrafficType.setStatus("current")


class _TnGmplsLspProtectionType_Type(Integer32):
    """Custom type tnGmplsLspProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 1),
          ("sbr", 2),
          ("guaranteed", 3),
          ("osncp", 6),
          ("oprc", 7))
    )


_TnGmplsLspProtectionType_Type.__name__ = "Integer32"
_TnGmplsLspProtectionType_Object = MibTableColumn
tnGmplsLspProtectionType = _TnGmplsLspProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 10),
    _TnGmplsLspProtectionType_Type()
)
tnGmplsLspProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspProtectionType.setStatus("current")


class _TnGmplsLspReversionMode_Type(Integer32):
    """Custom type tnGmplsLspReversionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_TnGmplsLspReversionMode_Type.__name__ = "Integer32"
_TnGmplsLspReversionMode_Object = MibTableColumn
tnGmplsLspReversionMode = _TnGmplsLspReversionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 11),
    _TnGmplsLspReversionMode_Type()
)
tnGmplsLspReversionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspReversionMode.setStatus("current")


class _TnGmplsLspIncludeAnyAffinity_Type(Unsigned32):
    """Custom type tnGmplsLspIncludeAnyAffinity based on Unsigned32"""
    defaultValue = 0


_TnGmplsLspIncludeAnyAffinity_Type.__name__ = "Unsigned32"
_TnGmplsLspIncludeAnyAffinity_Object = MibTableColumn
tnGmplsLspIncludeAnyAffinity = _TnGmplsLspIncludeAnyAffinity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 12),
    _TnGmplsLspIncludeAnyAffinity_Type()
)
tnGmplsLspIncludeAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspIncludeAnyAffinity.setStatus("current")


class _TnGmplsLspExcludeAnyAffinity_Type(Unsigned32):
    """Custom type tnGmplsLspExcludeAnyAffinity based on Unsigned32"""
    defaultValue = 0


_TnGmplsLspExcludeAnyAffinity_Type.__name__ = "Unsigned32"
_TnGmplsLspExcludeAnyAffinity_Object = MibTableColumn
tnGmplsLspExcludeAnyAffinity = _TnGmplsLspExcludeAnyAffinity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 13),
    _TnGmplsLspExcludeAnyAffinity_Type()
)
tnGmplsLspExcludeAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspExcludeAnyAffinity.setStatus("current")


class _TnGmplsLspConnectionType_Type(Integer32):
    """Custom type tnGmplsLspConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("spc", 1)
    )


_TnGmplsLspConnectionType_Type.__name__ = "Integer32"
_TnGmplsLspConnectionType_Object = MibTableColumn
tnGmplsLspConnectionType = _TnGmplsLspConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 14),
    _TnGmplsLspConnectionType_Type()
)
tnGmplsLspConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspConnectionType.setStatus("current")


class _TnGmplsLspAdminStatus_Type(Integer32):
    """Custom type tnGmplsLspAdminStatus based on Integer32"""
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


_TnGmplsLspAdminStatus_Type.__name__ = "Integer32"
_TnGmplsLspAdminStatus_Object = MibTableColumn
tnGmplsLspAdminStatus = _TnGmplsLspAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 15),
    _TnGmplsLspAdminStatus_Type()
)
tnGmplsLspAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspAdminStatus.setStatus("current")
_TnGmplsLspDiversityLspList_Type = DisplayString
_TnGmplsLspDiversityLspList_Object = MibTableColumn
tnGmplsLspDiversityLspList = _TnGmplsLspDiversityLspList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 16),
    _TnGmplsLspDiversityLspList_Type()
)
tnGmplsLspDiversityLspList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspDiversityLspList.setStatus("current")


class _TnGmplsLspLatencyThreshold_Type(Unsigned32):
    """Custom type tnGmplsLspLatencyThreshold based on Unsigned32"""
    defaultValue = 0


_TnGmplsLspLatencyThreshold_Type.__name__ = "Unsigned32"
_TnGmplsLspLatencyThreshold_Object = MibTableColumn
tnGmplsLspLatencyThreshold = _TnGmplsLspLatencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 17),
    _TnGmplsLspLatencyThreshold_Type()
)
tnGmplsLspLatencyThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspLatencyThreshold.setStatus("current")


class _TnGmplsLspMaxHopsConstraint_Type(Unsigned32):
    """Custom type tnGmplsLspMaxHopsConstraint based on Unsigned32"""
    defaultValue = 0


_TnGmplsLspMaxHopsConstraint_Type.__name__ = "Unsigned32"
_TnGmplsLspMaxHopsConstraint_Object = MibTableColumn
tnGmplsLspMaxHopsConstraint = _TnGmplsLspMaxHopsConstraint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 18),
    _TnGmplsLspMaxHopsConstraint_Type()
)
tnGmplsLspMaxHopsConstraint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspMaxHopsConstraint.setStatus("current")


class _TnGmplsLspActions_Type(Integer32):
    """Custom type tnGmplsLspActions based on Integer32"""
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
          ("moveToMainNominal", 2),
          ("moveToSpareNominal", 3),
          ("moveToInactiveBackup", 4),
          ("moveToMainBackup", 5),
          ("moveToSpareBackup", 6))
    )


_TnGmplsLspActions_Type.__name__ = "Integer32"
_TnGmplsLspActions_Object = MibTableColumn
tnGmplsLspActions = _TnGmplsLspActions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 19),
    _TnGmplsLspActions_Type()
)
tnGmplsLspActions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspActions.setStatus("current")
_TnGmplsLspProtectionStateMain_Type = AluWdmGmplsLspProtectionState
_TnGmplsLspProtectionStateMain_Object = MibTableColumn
tnGmplsLspProtectionStateMain = _TnGmplsLspProtectionStateMain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 20),
    _TnGmplsLspProtectionStateMain_Type()
)
tnGmplsLspProtectionStateMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspProtectionStateMain.setStatus("current")
_TnGmplsLspProtectionStateSpare_Type = AluWdmGmplsLspProtectionState
_TnGmplsLspProtectionStateSpare_Object = MibTableColumn
tnGmplsLspProtectionStateSpare = _TnGmplsLspProtectionStateSpare_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 21),
    _TnGmplsLspProtectionStateSpare_Type()
)
tnGmplsLspProtectionStateSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspProtectionStateSpare.setStatus("current")


class _TnGmplsLspReversionState_Type(Integer32):
    """Custom type tnGmplsLspReversionState based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("nA", 1),
          ("rTR", 2),
          ("notRTR", 3),
          ("revBlocked", 4),
          ("revPreempt", 5),
          ("mainNASpareNA", 6),
          ("mainNASpareRTR", 7),
          ("mainNASpareNotRTR", 8),
          ("mainNASpareRevBlocked", 9),
          ("mainNASpareRevPreempt", 10),
          ("mainRTRSpareNA", 11),
          ("mainRTRSpareRTR", 12),
          ("mainRTRSpareNotRTR", 13),
          ("mainRTRSpareRevBlocked", 14),
          ("mainRTRSpareRevPreempt", 15),
          ("mainNotRTRSpareNA", 16),
          ("mainNotRTRSpareRTR", 17),
          ("mainNotRTRSpareNotRTR", 18),
          ("mainNotRTRSpareRevBlocked", 19),
          ("mainNotRTRSpareRevPreempt", 20),
          ("mainRevBlockedSpareNA", 21),
          ("mainRevBlockedSpareRTR", 22),
          ("mainRevBlockedSpareNotRTR", 23),
          ("mainRevBlockedSpareRevBlocked", 24),
          ("mainRevBlockedSpareRevPreempt", 25),
          ("mainRevPreemptSpareNA", 26),
          ("mainRevPreemptSpareRTR", 27),
          ("mainRevPreemptSpareNotRTR", 28),
          ("mainRevPreemptSpareRevBlocked", 29),
          ("mainRevPreemptSpareRevPreempt", 30))
    )


_TnGmplsLspReversionState_Type.__name__ = "Integer32"
_TnGmplsLspReversionState_Object = MibTableColumn
tnGmplsLspReversionState = _TnGmplsLspReversionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 22),
    _TnGmplsLspReversionState_Type()
)
tnGmplsLspReversionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspReversionState.setStatus("current")
_TnGmplsLspSRGViolation_Type = TruthValue
_TnGmplsLspSRGViolation_Object = MibTableColumn
tnGmplsLspSRGViolation = _TnGmplsLspSRGViolation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 23),
    _TnGmplsLspSRGViolation_Type()
)
tnGmplsLspSRGViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspSRGViolation.setStatus("current")
_TnGmplsLspColorViolation_Type = TruthValue
_TnGmplsLspColorViolation_Object = MibTableColumn
tnGmplsLspColorViolation = _TnGmplsLspColorViolation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 24),
    _TnGmplsLspColorViolation_Type()
)
tnGmplsLspColorViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspColorViolation.setStatus("current")
_TnGmplsLspOptFsbltyViolation_Type = TruthValue
_TnGmplsLspOptFsbltyViolation_Object = MibTableColumn
tnGmplsLspOptFsbltyViolation = _TnGmplsLspOptFsbltyViolation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 25),
    _TnGmplsLspOptFsbltyViolation_Type()
)
tnGmplsLspOptFsbltyViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspOptFsbltyViolation.setStatus("current")
_TnGmplsLspQoSViolation_Type = TruthValue
_TnGmplsLspQoSViolation_Object = MibTableColumn
tnGmplsLspQoSViolation = _TnGmplsLspQoSViolation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 26),
    _TnGmplsLspQoSViolation_Type()
)
tnGmplsLspQoSViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspQoSViolation.setStatus("current")
_TnGmplsLspLatencyViolation_Type = TruthValue
_TnGmplsLspLatencyViolation_Object = MibTableColumn
tnGmplsLspLatencyViolation = _TnGmplsLspLatencyViolation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 2, 1, 27),
    _TnGmplsLspLatencyViolation_Type()
)
tnGmplsLspLatencyViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspLatencyViolation.setStatus("current")
_TnGmplsLspFlowTable_Object = MibTable
tnGmplsLspFlowTable = _TnGmplsLspFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tnGmplsLspFlowTable.setStatus("current")
_TnGmplsLspFlowEntry_Object = MibTableRow
tnGmplsLspFlowEntry = _TnGmplsLspFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 3, 1)
)
tnGmplsLspFlowEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspFlowSrcLspId"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspFlowType"),
)
if mibBuilder.loadTexts:
    tnGmplsLspFlowEntry.setStatus("current")
_TnGmplsLspFlowSrcLspId_Type = Unsigned32
_TnGmplsLspFlowSrcLspId_Object = MibTableColumn
tnGmplsLspFlowSrcLspId = _TnGmplsLspFlowSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 3, 1, 1),
    _TnGmplsLspFlowSrcLspId_Type()
)
tnGmplsLspFlowSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspFlowSrcLspId.setStatus("current")


class _TnGmplsLspFlowType_Type(Integer32):
    """Custom type tnGmplsLspFlowType based on Integer32"""
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
        *(("main", 1),
          ("spare", 2),
          ("backupMain", 3),
          ("backupSpare", 4),
          ("backupInactive", 5))
    )


_TnGmplsLspFlowType_Type.__name__ = "Integer32"
_TnGmplsLspFlowType_Object = MibTableColumn
tnGmplsLspFlowType = _TnGmplsLspFlowType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 3, 1, 2),
    _TnGmplsLspFlowType_Type()
)
tnGmplsLspFlowType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspFlowType.setStatus("current")


class _TnGmplsLspFlowState_Type(Integer32):
    """Custom type tnGmplsLspFlowState based on Integer32"""
    defaultValue = 1

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
        *(("undef", 1),
          ("up", 2),
          ("down", 3),
          ("degraded", 4))
    )


_TnGmplsLspFlowState_Type.__name__ = "Integer32"
_TnGmplsLspFlowState_Object = MibTableColumn
tnGmplsLspFlowState = _TnGmplsLspFlowState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 3, 1, 3),
    _TnGmplsLspFlowState_Type()
)
tnGmplsLspFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspFlowState.setStatus("current")
_TnGmplsLspFlowId_Type = Unsigned32
_TnGmplsLspFlowId_Object = MibTableColumn
tnGmplsLspFlowId = _TnGmplsLspFlowId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 3, 1, 4),
    _TnGmplsLspFlowId_Type()
)
tnGmplsLspFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspFlowId.setStatus("current")
_TnGmplsLspCHopTable_Object = MibTable
tnGmplsLspCHopTable = _TnGmplsLspCHopTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tnGmplsLspCHopTable.setStatus("current")
_TnGmplsLspCHopEntry_Object = MibTableRow
tnGmplsLspCHopEntry = _TnGmplsLspCHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4, 1)
)
tnGmplsLspCHopEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspCHopSrcLspId"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspCHopRouteType"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspCHopIndex"),
)
if mibBuilder.loadTexts:
    tnGmplsLspCHopEntry.setStatus("current")
_TnGmplsLspCHopSrcLspId_Type = Unsigned32
_TnGmplsLspCHopSrcLspId_Object = MibTableColumn
tnGmplsLspCHopSrcLspId = _TnGmplsLspCHopSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4, 1, 1),
    _TnGmplsLspCHopSrcLspId_Type()
)
tnGmplsLspCHopSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspCHopSrcLspId.setStatus("current")


class _TnGmplsLspCHopRouteType_Type(Integer32):
    """Custom type tnGmplsLspCHopRouteType based on Integer32"""
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
        *(("main", 1),
          ("spare", 2),
          ("backup", 3),
          ("backupSpare", 4),
          ("backupInactive", 5))
    )


_TnGmplsLspCHopRouteType_Type.__name__ = "Integer32"
_TnGmplsLspCHopRouteType_Object = MibTableColumn
tnGmplsLspCHopRouteType = _TnGmplsLspCHopRouteType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4, 1, 2),
    _TnGmplsLspCHopRouteType_Type()
)
tnGmplsLspCHopRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspCHopRouteType.setStatus("current")
_TnGmplsLspCHopIndex_Type = Unsigned32
_TnGmplsLspCHopIndex_Object = MibTableColumn
tnGmplsLspCHopIndex = _TnGmplsLspCHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4, 1, 3),
    _TnGmplsLspCHopIndex_Type()
)
tnGmplsLspCHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspCHopIndex.setStatus("current")
_TnGmplsLspCHopSubnodeId_Type = Unsigned32
_TnGmplsLspCHopSubnodeId_Object = MibTableColumn
tnGmplsLspCHopSubnodeId = _TnGmplsLspCHopSubnodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4, 1, 4),
    _TnGmplsLspCHopSubnodeId_Type()
)
tnGmplsLspCHopSubnodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspCHopSubnodeId.setStatus("current")
_TnGmplsLspCHopInResource_Type = DisplayString
_TnGmplsLspCHopInResource_Object = MibTableColumn
tnGmplsLspCHopInResource = _TnGmplsLspCHopInResource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4, 1, 5),
    _TnGmplsLspCHopInResource_Type()
)
tnGmplsLspCHopInResource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspCHopInResource.setStatus("current")
_TnGmplsLspCHopOutResource_Type = DisplayString
_TnGmplsLspCHopOutResource_Object = MibTableColumn
tnGmplsLspCHopOutResource = _TnGmplsLspCHopOutResource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 4, 1, 6),
    _TnGmplsLspCHopOutResource_Type()
)
tnGmplsLspCHopOutResource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspCHopOutResource.setStatus("current")
_TnGmplsLspAHopTable_Object = MibTable
tnGmplsLspAHopTable = _TnGmplsLspAHopTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tnGmplsLspAHopTable.setStatus("current")
_TnGmplsLspAHopEntry_Object = MibTableRow
tnGmplsLspAHopEntry = _TnGmplsLspAHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5, 1)
)
tnGmplsLspAHopEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAHopSrcLspId"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAHopRouteType"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAHopIndex"),
)
if mibBuilder.loadTexts:
    tnGmplsLspAHopEntry.setStatus("current")
_TnGmplsLspAHopSrcLspId_Type = Unsigned32
_TnGmplsLspAHopSrcLspId_Object = MibTableColumn
tnGmplsLspAHopSrcLspId = _TnGmplsLspAHopSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5, 1, 1),
    _TnGmplsLspAHopSrcLspId_Type()
)
tnGmplsLspAHopSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspAHopSrcLspId.setStatus("current")


class _TnGmplsLspAHopRouteType_Type(Integer32):
    """Custom type tnGmplsLspAHopRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("spare", 2),
          ("backupInactive", 5))
    )


_TnGmplsLspAHopRouteType_Type.__name__ = "Integer32"
_TnGmplsLspAHopRouteType_Object = MibTableColumn
tnGmplsLspAHopRouteType = _TnGmplsLspAHopRouteType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5, 1, 2),
    _TnGmplsLspAHopRouteType_Type()
)
tnGmplsLspAHopRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspAHopRouteType.setStatus("current")
_TnGmplsLspAHopIndex_Type = Unsigned32
_TnGmplsLspAHopIndex_Object = MibTableColumn
tnGmplsLspAHopIndex = _TnGmplsLspAHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5, 1, 3),
    _TnGmplsLspAHopIndex_Type()
)
tnGmplsLspAHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspAHopIndex.setStatus("current")
_TnGmplsLspAHopSubnodeId_Type = Unsigned32
_TnGmplsLspAHopSubnodeId_Object = MibTableColumn
tnGmplsLspAHopSubnodeId = _TnGmplsLspAHopSubnodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5, 1, 4),
    _TnGmplsLspAHopSubnodeId_Type()
)
tnGmplsLspAHopSubnodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspAHopSubnodeId.setStatus("current")
_TnGmplsLspAHopInResource_Type = DisplayString
_TnGmplsLspAHopInResource_Object = MibTableColumn
tnGmplsLspAHopInResource = _TnGmplsLspAHopInResource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5, 1, 5),
    _TnGmplsLspAHopInResource_Type()
)
tnGmplsLspAHopInResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspAHopInResource.setStatus("current")
_TnGmplsLspAHopOutResource_Type = DisplayString
_TnGmplsLspAHopOutResource_Object = MibTableColumn
tnGmplsLspAHopOutResource = _TnGmplsLspAHopOutResource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 5, 1, 6),
    _TnGmplsLspAHopOutResource_Type()
)
tnGmplsLspAHopOutResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspAHopOutResource.setStatus("current")
_TnGmplsLspExcludeTable_Object = MibTable
tnGmplsLspExcludeTable = _TnGmplsLspExcludeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    tnGmplsLspExcludeTable.setStatus("current")
_TnGmplsLspExcludeEntry_Object = MibTableRow
tnGmplsLspExcludeEntry = _TnGmplsLspExcludeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 6, 1)
)
tnGmplsLspExcludeEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspExcludeSrcLspId"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspExcludeIndex"),
)
if mibBuilder.loadTexts:
    tnGmplsLspExcludeEntry.setStatus("current")
_TnGmplsLspExcludeSrcLspId_Type = Unsigned32
_TnGmplsLspExcludeSrcLspId_Object = MibTableColumn
tnGmplsLspExcludeSrcLspId = _TnGmplsLspExcludeSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 6, 1, 1),
    _TnGmplsLspExcludeSrcLspId_Type()
)
tnGmplsLspExcludeSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspExcludeSrcLspId.setStatus("current")
_TnGmplsLspExcludeIndex_Type = Unsigned32
_TnGmplsLspExcludeIndex_Object = MibTableColumn
tnGmplsLspExcludeIndex = _TnGmplsLspExcludeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 6, 1, 2),
    _TnGmplsLspExcludeIndex_Type()
)
tnGmplsLspExcludeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspExcludeIndex.setStatus("current")
_TnGmplsLspExcludeSubnodeId_Type = Unsigned32
_TnGmplsLspExcludeSubnodeId_Object = MibTableColumn
tnGmplsLspExcludeSubnodeId = _TnGmplsLspExcludeSubnodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 6, 1, 3),
    _TnGmplsLspExcludeSubnodeId_Type()
)
tnGmplsLspExcludeSubnodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspExcludeSubnodeId.setStatus("current")
_TnGmplsLspExcludeTELink_Type = Unsigned32
_TnGmplsLspExcludeTELink_Object = MibTableColumn
tnGmplsLspExcludeTELink = _TnGmplsLspExcludeTELink_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 6, 1, 4),
    _TnGmplsLspExcludeTELink_Type()
)
tnGmplsLspExcludeTELink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspExcludeTELink.setStatus("current")
_TnGmplsLspExcludeDBLink_Type = Unsigned32
_TnGmplsLspExcludeDBLink_Object = MibTableColumn
tnGmplsLspExcludeDBLink = _TnGmplsLspExcludeDBLink_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 6, 1, 5),
    _TnGmplsLspExcludeDBLink_Type()
)
tnGmplsLspExcludeDBLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspExcludeDBLink.setStatus("current")
_TnGmplsLspTransactionTable_Object = MibTable
tnGmplsLspTransactionTable = _TnGmplsLspTransactionTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    tnGmplsLspTransactionTable.setStatus("current")
_TnGmplsLspTransactionEntry_Object = MibTableRow
tnGmplsLspTransactionEntry = _TnGmplsLspTransactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 7, 1)
)
tnGmplsLspTransactionEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspTransactionSrcLspId"),
)
if mibBuilder.loadTexts:
    tnGmplsLspTransactionEntry.setStatus("current")
_TnGmplsLspTransactionSrcLspId_Type = Unsigned32
_TnGmplsLspTransactionSrcLspId_Object = MibTableColumn
tnGmplsLspTransactionSrcLspId = _TnGmplsLspTransactionSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 7, 1, 1),
    _TnGmplsLspTransactionSrcLspId_Type()
)
tnGmplsLspTransactionSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspTransactionSrcLspId.setStatus("current")


class _TnGmplsLspTransaction_Type(Integer32):
    """Custom type tnGmplsLspTransaction based on Integer32"""
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
        *(("na", 1),
          ("commit", 2),
          ("rollback", 3),
          ("delete", 4))
    )


_TnGmplsLspTransaction_Type.__name__ = "Integer32"
_TnGmplsLspTransaction_Object = MibTableColumn
tnGmplsLspTransaction = _TnGmplsLspTransaction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 7, 1, 2),
    _TnGmplsLspTransaction_Type()
)
tnGmplsLspTransaction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspTransaction.setStatus("current")


class _TnGmplsLspTransactionState_Type(Integer32):
    """Custom type tnGmplsLspTransactionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("commit", 2),
          ("pending", 3))
    )


_TnGmplsLspTransactionState_Type.__name__ = "Integer32"
_TnGmplsLspTransactionState_Object = MibTableColumn
tnGmplsLspTransactionState = _TnGmplsLspTransactionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 7, 1, 3),
    _TnGmplsLspTransactionState_Type()
)
tnGmplsLspTransactionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspTransactionState.setStatus("current")
_TnGmplsLspToPortTable_Object = MibTable
tnGmplsLspToPortTable = _TnGmplsLspToPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    tnGmplsLspToPortTable.setStatus("current")
_TnGmplsLspToPortEntry_Object = MibTableRow
tnGmplsLspToPortEntry = _TnGmplsLspToPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 8, 1)
)
tnGmplsLspToPortEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspDBLinkIfId"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspLTPSrcLspId"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSrcLsrId"),
)
if mibBuilder.loadTexts:
    tnGmplsLspToPortEntry.setStatus("current")
_TnGmplsLspDBLinkIfId_Type = Unsigned32
_TnGmplsLspDBLinkIfId_Object = MibTableColumn
tnGmplsLspDBLinkIfId = _TnGmplsLspDBLinkIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 8, 1, 1),
    _TnGmplsLspDBLinkIfId_Type()
)
tnGmplsLspDBLinkIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspDBLinkIfId.setStatus("current")
_TnGmplsLspLTPSrcLspId_Type = Unsigned32
_TnGmplsLspLTPSrcLspId_Object = MibTableColumn
tnGmplsLspLTPSrcLspId = _TnGmplsLspLTPSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 8, 1, 2),
    _TnGmplsLspLTPSrcLspId_Type()
)
tnGmplsLspLTPSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspLTPSrcLspId.setStatus("current")
_TnGmplsLspSrcLsrId_Type = Unsigned32
_TnGmplsLspSrcLsrId_Object = MibTableColumn
tnGmplsLspSrcLsrId = _TnGmplsLspSrcLsrId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 8, 1, 3),
    _TnGmplsLspSrcLsrId_Type()
)
tnGmplsLspSrcLsrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspSrcLsrId.setStatus("current")
_TnGmplsLspName_Type = DisplayString
_TnGmplsLspName_Object = MibTableColumn
tnGmplsLspName = _TnGmplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 8, 1, 4),
    _TnGmplsLspName_Type()
)
tnGmplsLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspName.setStatus("current")
_TnGmplsLspSncpMgmtTable_Object = MibTable
tnGmplsLspSncpMgmtTable = _TnGmplsLspSncpMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 9)
)
if mibBuilder.loadTexts:
    tnGmplsLspSncpMgmtTable.setStatus("current")
_TnGmplsLspSncpMgmtEntry_Object = MibTableRow
tnGmplsLspSncpMgmtEntry = _TnGmplsLspSncpMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 9, 1)
)
tnGmplsLspSncpMgmtEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSncpCtpResource"),
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSncpDirection"),
)
if mibBuilder.loadTexts:
    tnGmplsLspSncpMgmtEntry.setStatus("current")


class _TnGmplsLspSncpCtpResource_Type(OctetString):
    """Custom type tnGmplsLspSncpCtpResource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_TnGmplsLspSncpCtpResource_Type.__name__ = "OctetString"
_TnGmplsLspSncpCtpResource_Object = MibTableColumn
tnGmplsLspSncpCtpResource = _TnGmplsLspSncpCtpResource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 9, 1, 1),
    _TnGmplsLspSncpCtpResource_Type()
)
tnGmplsLspSncpCtpResource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspSncpCtpResource.setStatus("current")


class _TnGmplsLspSncpDirection_Type(Integer32):
    """Custom type tnGmplsLspSncpDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("internal", 2))
    )


_TnGmplsLspSncpDirection_Type.__name__ = "Integer32"
_TnGmplsLspSncpDirection_Object = MibTableColumn
tnGmplsLspSncpDirection = _TnGmplsLspSncpDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 9, 1, 2),
    _TnGmplsLspSncpDirection_Type()
)
tnGmplsLspSncpDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspSncpDirection.setStatus("current")


class _TnGmplsLspSncpCmd_Type(Integer32):
    """Custom type tnGmplsLspSncpCmd based on Integer32"""
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
        *(("na", 1),
          ("manualMain", 2),
          ("manualSpare", 3),
          ("forceMain", 4),
          ("forceSpare", 5),
          ("release", 6))
    )


_TnGmplsLspSncpCmd_Type.__name__ = "Integer32"
_TnGmplsLspSncpCmd_Object = MibTableColumn
tnGmplsLspSncpCmd = _TnGmplsLspSncpCmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 9, 1, 3),
    _TnGmplsLspSncpCmd_Type()
)
tnGmplsLspSncpCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspSncpCmd.setStatus("current")


class _TnGmplsLspSncpState_Type(Integer32):
    """Custom type tnGmplsLspSncpState based on Integer32"""
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
        *(("na", 1),
          ("mainSelected", 2),
          ("spareSelected", 3),
          ("mainSelectedSpareFailed", 4),
          ("spareSelectedMainFailed", 5),
          ("bothFailed", 6),
          ("nonUniform", 7),
          ("unknown", 8))
    )


_TnGmplsLspSncpState_Type.__name__ = "Integer32"
_TnGmplsLspSncpState_Object = MibTableColumn
tnGmplsLspSncpState = _TnGmplsLspSncpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 9, 1, 4),
    _TnGmplsLspSncpState_Type()
)
tnGmplsLspSncpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspSncpState.setStatus("current")
_TnGmplsLspSncpRowStatus_Type = RowStatus
_TnGmplsLspSncpRowStatus_Object = MibTableColumn
tnGmplsLspSncpRowStatus = _TnGmplsLspSncpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 9, 1, 5),
    _TnGmplsLspSncpRowStatus_Type()
)
tnGmplsLspSncpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsLspSncpRowStatus.setStatus("current")
_TnGmplsLspNextIndexTable_Object = MibTable
tnGmplsLspNextIndexTable = _TnGmplsLspNextIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    tnGmplsLspNextIndexTable.setStatus("current")
_TnGmplsLspNextIndexEntry_Object = MibTableRow
tnGmplsLspNextIndexEntry = _TnGmplsLspNextIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 10, 1)
)
tnGmplsLspNextIndexEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsLspNextIndexTableIndex"),
)
if mibBuilder.loadTexts:
    tnGmplsLspNextIndexEntry.setStatus("current")
_TnGmplsLspNextIndexTableIndex_Type = Unsigned32
_TnGmplsLspNextIndexTableIndex_Object = MibTableColumn
tnGmplsLspNextIndexTableIndex = _TnGmplsLspNextIndexTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 10, 1, 1),
    _TnGmplsLspNextIndexTableIndex_Type()
)
tnGmplsLspNextIndexTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsLspNextIndexTableIndex.setStatus("current")
_TnGmplsLspNextIndex_Type = Unsigned32
_TnGmplsLspNextIndex_Object = MibTableColumn
tnGmplsLspNextIndex = _TnGmplsLspNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 10, 1, 2),
    _TnGmplsLspNextIndex_Type()
)
tnGmplsLspNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsLspNextIndex.setStatus("current")
_TnGmplsMoveLspToTable_Object = MibTable
tnGmplsMoveLspToTable = _TnGmplsMoveLspToTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 11)
)
if mibBuilder.loadTexts:
    tnGmplsMoveLspToTable.setStatus("current")
_TnGmplsMoveLspToEntry_Object = MibTableRow
tnGmplsMoveLspToEntry = _TnGmplsMoveLspToEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 11, 1)
)
tnGmplsMoveLspToEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspToSrcLspId"),
)
if mibBuilder.loadTexts:
    tnGmplsMoveLspToEntry.setStatus("current")
_TnGmplsMoveLspToSrcLspId_Type = Unsigned32
_TnGmplsMoveLspToSrcLspId_Object = MibTableColumn
tnGmplsMoveLspToSrcLspId = _TnGmplsMoveLspToSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 11, 1, 1),
    _TnGmplsMoveLspToSrcLspId_Type()
)
tnGmplsMoveLspToSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsMoveLspToSrcLspId.setStatus("current")


class _TnGmplsMoveLspToCmd_Type(Integer32):
    """Custom type tnGmplsMoveLspToCmd based on Integer32"""
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
          ("moveToMainNominal", 2),
          ("moveToSpareNominal", 3),
          ("moveToInactiveBackup", 4),
          ("moveToMainBackup", 5),
          ("moveToSpareBackup", 6))
    )


_TnGmplsMoveLspToCmd_Type.__name__ = "Integer32"
_TnGmplsMoveLspToCmd_Object = MibTableColumn
tnGmplsMoveLspToCmd = _TnGmplsMoveLspToCmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 11, 1, 2),
    _TnGmplsMoveLspToCmd_Type()
)
tnGmplsMoveLspToCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsMoveLspToCmd.setStatus("current")
_TnGmplsMoveLspToRowStatus_Type = RowStatus
_TnGmplsMoveLspToRowStatus_Object = MibTableColumn
tnGmplsMoveLspToRowStatus = _TnGmplsMoveLspToRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 11, 1, 3),
    _TnGmplsMoveLspToRowStatus_Type()
)
tnGmplsMoveLspToRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsMoveLspToRowStatus.setStatus("current")
_TnGmplsMoveLspFromTable_Object = MibTable
tnGmplsMoveLspFromTable = _TnGmplsMoveLspFromTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 12)
)
if mibBuilder.loadTexts:
    tnGmplsMoveLspFromTable.setStatus("current")
_TnGmplsMoveLspFromEntry_Object = MibTableRow
tnGmplsMoveLspFromEntry = _TnGmplsMoveLspFromEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 12, 1)
)
tnGmplsMoveLspFromEntry.setIndexNames(
    (0, "TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspFromSrcLspId"),
)
if mibBuilder.loadTexts:
    tnGmplsMoveLspFromEntry.setStatus("current")
_TnGmplsMoveLspFromSrcLspId_Type = Unsigned32
_TnGmplsMoveLspFromSrcLspId_Object = MibTableColumn
tnGmplsMoveLspFromSrcLspId = _TnGmplsMoveLspFromSrcLspId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 12, 1, 1),
    _TnGmplsMoveLspFromSrcLspId_Type()
)
tnGmplsMoveLspFromSrcLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsMoveLspFromSrcLspId.setStatus("current")
_TnGmplsMoveLspFromLinks_Type = OctetString
_TnGmplsMoveLspFromLinks_Object = MibTableColumn
tnGmplsMoveLspFromLinks = _TnGmplsMoveLspFromLinks_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 12, 1, 2),
    _TnGmplsMoveLspFromLinks_Type()
)
tnGmplsMoveLspFromLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsMoveLspFromLinks.setStatus("current")


class _TnGmplsMoveLspFromCmd_Type(Integer32):
    """Custom type tnGmplsMoveLspFromCmd based on Integer32"""
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
          ("currentMain", 2),
          ("currentSpare", 3))
    )


_TnGmplsMoveLspFromCmd_Type.__name__ = "Integer32"
_TnGmplsMoveLspFromCmd_Object = MibTableColumn
tnGmplsMoveLspFromCmd = _TnGmplsMoveLspFromCmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 12, 1, 3),
    _TnGmplsMoveLspFromCmd_Type()
)
tnGmplsMoveLspFromCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsMoveLspFromCmd.setStatus("current")
_TnGmplsMoveLspFromRowStatus_Type = RowStatus
_TnGmplsMoveLspFromRowStatus_Object = MibTableColumn
tnGmplsMoveLspFromRowStatus = _TnGmplsMoveLspFromRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 1, 12, 1, 4),
    _TnGmplsMoveLspFromRowStatus_Type()
)
tnGmplsMoveLspFromRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsMoveLspFromRowStatus.setStatus("current")
_TnGmplsLspConf_ObjectIdentity = ObjectIdentity
tnGmplsLspConf = _TnGmplsLspConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3)
)
_TnGmplsLspGroups_ObjectIdentity = ObjectIdentity
tnGmplsLspGroups = _TnGmplsLspGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1)
)
_TnGmplsLspCompliances_ObjectIdentity = ObjectIdentity
tnGmplsLspCompliances = _TnGmplsLspCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 2)
)

# Managed Objects groups

tnGmplsLspObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 1)
)
tnGmplsLspObjsGroup.setObjects(
    ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAttributeTotal")
)
if mibBuilder.loadTexts:
    tnGmplsLspObjsGroup.setStatus("current")

tnGmplsLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 2)
)
tnGmplsLspGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspDescr"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspIngressResource"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspEgressResource"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspDestLsrId"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSetupPrio"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspHoldingPrio"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspDirectionType"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspTrafficType"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspProtectionType"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspReversionMode"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspIncludeAnyAffinity"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspExcludeAnyAffinity"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspConnectionType"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAdminStatus"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspDiversityLspList"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspLatencyThreshold"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspMaxHopsConstraint"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspActions"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspProtectionStateMain"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspProtectionStateSpare"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspReversionState"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSRGViolation"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspColorViolation"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspOptFsbltyViolation"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspQoSViolation"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspLatencyViolation"))
)
if mibBuilder.loadTexts:
    tnGmplsLspGroup.setStatus("current")

tnGmplsLspFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 3)
)
tnGmplsLspFlowGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspFlowState"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspFlowId"))
)
if mibBuilder.loadTexts:
    tnGmplsLspFlowGroup.setStatus("current")

tnGmplsLspCHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 4)
)
tnGmplsLspCHopGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspCHopSubnodeId"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspCHopInResource"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspCHopOutResource"))
)
if mibBuilder.loadTexts:
    tnGmplsLspCHopGroup.setStatus("current")

tnGmplsLspAHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 5)
)
tnGmplsLspAHopGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAHopSubnodeId"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAHopInResource"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAHopOutResource"))
)
if mibBuilder.loadTexts:
    tnGmplsLspAHopGroup.setStatus("current")

tnGmplsLspExcludeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 6)
)
tnGmplsLspExcludeGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspExcludeSubnodeId"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspExcludeTELink"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspExcludeDBLink"))
)
if mibBuilder.loadTexts:
    tnGmplsLspExcludeGroup.setStatus("current")

tnGmplsLspTransactionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 7)
)
tnGmplsLspTransactionGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspTransaction"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspTransactionState"))
)
if mibBuilder.loadTexts:
    tnGmplsLspTransactionGroup.setStatus("current")

tnGmplsLspToPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 8)
)
tnGmplsLspToPortGroup.setObjects(
    ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspName")
)
if mibBuilder.loadTexts:
    tnGmplsLspToPortGroup.setStatus("current")

tnGmplsLspSncpMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 9)
)
tnGmplsLspSncpMgmtGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSncpCmd"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSncpState"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSncpRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsLspSncpMgmtGroup.setStatus("current")

tnGmplsLspNextIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 10)
)
tnGmplsLspNextIndexGroup.setObjects(
    ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspNextIndex")
)
if mibBuilder.loadTexts:
    tnGmplsLspNextIndexGroup.setStatus("current")

tnGmplsMoveLspToGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 11)
)
tnGmplsMoveLspToGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspToCmd"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspToRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsMoveLspToGroup.setStatus("current")

tnGmplsMoveLspFromGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 1, 12)
)
tnGmplsMoveLspFromGroup.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspFromLinks"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspFromCmd"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspFromRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsMoveLspFromGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnGmplsLspCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 3, 3, 2, 1)
)
tnGmplsLspCompliance.setObjects(
      *(("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspObjsGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspFlowGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspCHopGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspAHopGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspExcludeGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspTransactionGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspToPortGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspSncpMgmtGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsLspNextIndexGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspToGroup"),
        ("TROPIC-GMPLS-LSP-MIB", "tnGmplsMoveLspFromGroup"))
)
if mibBuilder.loadTexts:
    tnGmplsLspCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GMPLS-LSP-MIB",
    **{"AluWdmGmplsLspProtectionState": AluWdmGmplsLspProtectionState,
       "tnGmplsLspMibModule": tnGmplsLspMibModule,
       "tnGmplsLspMIB": tnGmplsLspMIB,
       "tnGmplsLspObjs": tnGmplsLspObjs,
       "tnGmplsLspAttributeTotal": tnGmplsLspAttributeTotal,
       "tnGmplsLspTable": tnGmplsLspTable,
       "tnGmplsLspEntry": tnGmplsLspEntry,
       "tnGmplsLspSrcLspId": tnGmplsLspSrcLspId,
       "tnGmplsLspDescr": tnGmplsLspDescr,
       "tnGmplsLspIngressResource": tnGmplsLspIngressResource,
       "tnGmplsLspEgressResource": tnGmplsLspEgressResource,
       "tnGmplsLspDestLsrId": tnGmplsLspDestLsrId,
       "tnGmplsLspSetupPrio": tnGmplsLspSetupPrio,
       "tnGmplsLspHoldingPrio": tnGmplsLspHoldingPrio,
       "tnGmplsLspDirectionType": tnGmplsLspDirectionType,
       "tnGmplsLspTrafficType": tnGmplsLspTrafficType,
       "tnGmplsLspProtectionType": tnGmplsLspProtectionType,
       "tnGmplsLspReversionMode": tnGmplsLspReversionMode,
       "tnGmplsLspIncludeAnyAffinity": tnGmplsLspIncludeAnyAffinity,
       "tnGmplsLspExcludeAnyAffinity": tnGmplsLspExcludeAnyAffinity,
       "tnGmplsLspConnectionType": tnGmplsLspConnectionType,
       "tnGmplsLspAdminStatus": tnGmplsLspAdminStatus,
       "tnGmplsLspDiversityLspList": tnGmplsLspDiversityLspList,
       "tnGmplsLspLatencyThreshold": tnGmplsLspLatencyThreshold,
       "tnGmplsLspMaxHopsConstraint": tnGmplsLspMaxHopsConstraint,
       "tnGmplsLspActions": tnGmplsLspActions,
       "tnGmplsLspProtectionStateMain": tnGmplsLspProtectionStateMain,
       "tnGmplsLspProtectionStateSpare": tnGmplsLspProtectionStateSpare,
       "tnGmplsLspReversionState": tnGmplsLspReversionState,
       "tnGmplsLspSRGViolation": tnGmplsLspSRGViolation,
       "tnGmplsLspColorViolation": tnGmplsLspColorViolation,
       "tnGmplsLspOptFsbltyViolation": tnGmplsLspOptFsbltyViolation,
       "tnGmplsLspQoSViolation": tnGmplsLspQoSViolation,
       "tnGmplsLspLatencyViolation": tnGmplsLspLatencyViolation,
       "tnGmplsLspFlowTable": tnGmplsLspFlowTable,
       "tnGmplsLspFlowEntry": tnGmplsLspFlowEntry,
       "tnGmplsLspFlowSrcLspId": tnGmplsLspFlowSrcLspId,
       "tnGmplsLspFlowType": tnGmplsLspFlowType,
       "tnGmplsLspFlowState": tnGmplsLspFlowState,
       "tnGmplsLspFlowId": tnGmplsLspFlowId,
       "tnGmplsLspCHopTable": tnGmplsLspCHopTable,
       "tnGmplsLspCHopEntry": tnGmplsLspCHopEntry,
       "tnGmplsLspCHopSrcLspId": tnGmplsLspCHopSrcLspId,
       "tnGmplsLspCHopRouteType": tnGmplsLspCHopRouteType,
       "tnGmplsLspCHopIndex": tnGmplsLspCHopIndex,
       "tnGmplsLspCHopSubnodeId": tnGmplsLspCHopSubnodeId,
       "tnGmplsLspCHopInResource": tnGmplsLspCHopInResource,
       "tnGmplsLspCHopOutResource": tnGmplsLspCHopOutResource,
       "tnGmplsLspAHopTable": tnGmplsLspAHopTable,
       "tnGmplsLspAHopEntry": tnGmplsLspAHopEntry,
       "tnGmplsLspAHopSrcLspId": tnGmplsLspAHopSrcLspId,
       "tnGmplsLspAHopRouteType": tnGmplsLspAHopRouteType,
       "tnGmplsLspAHopIndex": tnGmplsLspAHopIndex,
       "tnGmplsLspAHopSubnodeId": tnGmplsLspAHopSubnodeId,
       "tnGmplsLspAHopInResource": tnGmplsLspAHopInResource,
       "tnGmplsLspAHopOutResource": tnGmplsLspAHopOutResource,
       "tnGmplsLspExcludeTable": tnGmplsLspExcludeTable,
       "tnGmplsLspExcludeEntry": tnGmplsLspExcludeEntry,
       "tnGmplsLspExcludeSrcLspId": tnGmplsLspExcludeSrcLspId,
       "tnGmplsLspExcludeIndex": tnGmplsLspExcludeIndex,
       "tnGmplsLspExcludeSubnodeId": tnGmplsLspExcludeSubnodeId,
       "tnGmplsLspExcludeTELink": tnGmplsLspExcludeTELink,
       "tnGmplsLspExcludeDBLink": tnGmplsLspExcludeDBLink,
       "tnGmplsLspTransactionTable": tnGmplsLspTransactionTable,
       "tnGmplsLspTransactionEntry": tnGmplsLspTransactionEntry,
       "tnGmplsLspTransactionSrcLspId": tnGmplsLspTransactionSrcLspId,
       "tnGmplsLspTransaction": tnGmplsLspTransaction,
       "tnGmplsLspTransactionState": tnGmplsLspTransactionState,
       "tnGmplsLspToPortTable": tnGmplsLspToPortTable,
       "tnGmplsLspToPortEntry": tnGmplsLspToPortEntry,
       "tnGmplsLspDBLinkIfId": tnGmplsLspDBLinkIfId,
       "tnGmplsLspLTPSrcLspId": tnGmplsLspLTPSrcLspId,
       "tnGmplsLspSrcLsrId": tnGmplsLspSrcLsrId,
       "tnGmplsLspName": tnGmplsLspName,
       "tnGmplsLspSncpMgmtTable": tnGmplsLspSncpMgmtTable,
       "tnGmplsLspSncpMgmtEntry": tnGmplsLspSncpMgmtEntry,
       "tnGmplsLspSncpCtpResource": tnGmplsLspSncpCtpResource,
       "tnGmplsLspSncpDirection": tnGmplsLspSncpDirection,
       "tnGmplsLspSncpCmd": tnGmplsLspSncpCmd,
       "tnGmplsLspSncpState": tnGmplsLspSncpState,
       "tnGmplsLspSncpRowStatus": tnGmplsLspSncpRowStatus,
       "tnGmplsLspNextIndexTable": tnGmplsLspNextIndexTable,
       "tnGmplsLspNextIndexEntry": tnGmplsLspNextIndexEntry,
       "tnGmplsLspNextIndexTableIndex": tnGmplsLspNextIndexTableIndex,
       "tnGmplsLspNextIndex": tnGmplsLspNextIndex,
       "tnGmplsMoveLspToTable": tnGmplsMoveLspToTable,
       "tnGmplsMoveLspToEntry": tnGmplsMoveLspToEntry,
       "tnGmplsMoveLspToSrcLspId": tnGmplsMoveLspToSrcLspId,
       "tnGmplsMoveLspToCmd": tnGmplsMoveLspToCmd,
       "tnGmplsMoveLspToRowStatus": tnGmplsMoveLspToRowStatus,
       "tnGmplsMoveLspFromTable": tnGmplsMoveLspFromTable,
       "tnGmplsMoveLspFromEntry": tnGmplsMoveLspFromEntry,
       "tnGmplsMoveLspFromSrcLspId": tnGmplsMoveLspFromSrcLspId,
       "tnGmplsMoveLspFromLinks": tnGmplsMoveLspFromLinks,
       "tnGmplsMoveLspFromCmd": tnGmplsMoveLspFromCmd,
       "tnGmplsMoveLspFromRowStatus": tnGmplsMoveLspFromRowStatus,
       "tnGmplsLspConf": tnGmplsLspConf,
       "tnGmplsLspGroups": tnGmplsLspGroups,
       "tnGmplsLspObjsGroup": tnGmplsLspObjsGroup,
       "tnGmplsLspGroup": tnGmplsLspGroup,
       "tnGmplsLspFlowGroup": tnGmplsLspFlowGroup,
       "tnGmplsLspCHopGroup": tnGmplsLspCHopGroup,
       "tnGmplsLspAHopGroup": tnGmplsLspAHopGroup,
       "tnGmplsLspExcludeGroup": tnGmplsLspExcludeGroup,
       "tnGmplsLspTransactionGroup": tnGmplsLspTransactionGroup,
       "tnGmplsLspToPortGroup": tnGmplsLspToPortGroup,
       "tnGmplsLspSncpMgmtGroup": tnGmplsLspSncpMgmtGroup,
       "tnGmplsLspNextIndexGroup": tnGmplsLspNextIndexGroup,
       "tnGmplsMoveLspToGroup": tnGmplsMoveLspToGroup,
       "tnGmplsMoveLspFromGroup": tnGmplsMoveLspFromGroup,
       "tnGmplsLspCompliances": tnGmplsLspCompliances,
       "tnGmplsLspCompliance": tnGmplsLspCompliance}
)
