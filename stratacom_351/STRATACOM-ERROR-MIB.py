# SNMP MIB module (STRATACOM-ERROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/STRATACOM-ERROR-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:11:01 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_StrmErrors_ObjectIdentity = ObjectIdentity
strmErrors = _StrmErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 910)
)
_StrmErrStatusLastIndex_Type = Integer32
_StrmErrStatusLastIndex_Object = MibScalar
strmErrStatusLastIndex = _StrmErrStatusLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 910, 1),
    _StrmErrStatusLastIndex_Type()
)
strmErrStatusLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strmErrStatusLastIndex.setStatus("mandatory")
_StrmErrStatusTable_Object = MibTable
strmErrStatusTable = _StrmErrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 910, 2)
)
if mibBuilder.loadTexts:
    strmErrStatusTable.setStatus("mandatory")
_StrmErrStatusTableEntry_Object = MibTableRow
strmErrStatusTableEntry = _StrmErrStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 910, 2, 1)
)
strmErrStatusTableEntry.setIndexNames(
    (0, "STRATACOM-ERROR-MIB", "strmErrReqId"),
)
if mibBuilder.loadTexts:
    strmErrStatusTableEntry.setStatus("mandatory")
_StrmErrReqId_Type = Integer32
_StrmErrReqId_Object = MibTableColumn
strmErrReqId = _StrmErrReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 910, 2, 1, 1),
    _StrmErrReqId_Type()
)
strmErrReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strmErrReqId.setStatus("mandatory")


class _StrmErrCode_Type(Integer32):
    """Custom type strmErrCode based on Integer32"""
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
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("existErr", 2),
          ("syntaxErr", 3),
          ("resourceErr", 4),
          ("databaseLocked", 5),
          ("otherErr", 6),
          ("wrongType", 7),
          ("wrongLength", 8),
          ("wrongEncoding", 9),
          ("wrongValue", 10),
          ("noCreation", 11),
          ("inconsistentValue", 12),
          ("resourceUnavailable", 13),
          ("commitFailed", 14),
          ("undoFailed", 15),
          ("authorizationError", 16),
          ("notWritable", 17),
          ("inconsistentName", 18),
          ("featureDisabled", 19),
          ("m32Problem", 20),
          ("sarProblem", 21),
          ("bnmProblem", 22),
          ("ascUpdFailed", 23),
          ("lineEnabled", 24),
          ("lineDisabled", 25),
          ("lmMismatch", 26),
          ("lineHasPorts", 27),
          ("portEnabled", 28),
          ("portDisable", 29),
          ("portHasChan", 30),
          ("chanEnabled", 31),
          ("chanDisabled", 32),
          ("dlciEnabled", 33),
          ("dlciDisabled", 34),
          ("segOverSubscribed", 35),
          ("segNotOverSubscribed", 36),
          ("portVpiVciInUse", 37),
          ("invalidPrimarySlot", 38),
          ("invalidSecondarySlot", 39),
          ("linkFull", 40),
          ("primaryDuplicate", 41),
          ("secondaryDuplicate", 42),
          ("primaryNotPresent", 43),
          ("secondaryNotPresent", 44),
          ("srmNotPresent", 45),
          ("invalidCommand", 46),
          ("invalidCardType", 47),
          ("featureMismatch", 48),
          ("lmiEnabled", 49),
          ("dlciUsed", 50),
          ("invalidRedType", 51),
          ("bertResourcesNotFree", 52),
          ("bertResourcesNotReady", 53),
          ("bertSlotEmpty", 54),
          ("bertUnsupportedCard", 55),
          ("bertNotOwner", 56),
          ("bertStartFailed", 57),
          ("bertModFailed", 58),
          ("bertDelFailed", 59),
          ("bertUnsupportedType", 60),
          ("bertWrongParams", 61),
          ("bertUnableToFree", 62),
          ("bertGeneralError", 63),
          ("portInLoopback", 64),
          ("invalidT3LineNum", 65),
          ("invalidT1LineNum", 66),
          ("invalidSlotNum", 67),
          ("invalidLineNum", 68),
          ("notEnoughLine", 69),
          ("lineInUse", 70),
          ("t3NotEnabled", 71),
          ("smNotPresent", 72),
          ("smNotPrimary", 73),
          ("srm3t3NotPresent", 74),
          ("lineInLoopback", 75),
          ("lineInconsistentLoopback", 76),
          ("lineLoopNotAllowed", 77),
          ("versionMismatch", 78),
          ("portOutOfService", 79),
          ("lineOutOfService", 80),
          ("bertNotConfigured", 81),
          ("bertConfigurationIncomplete", 82),
          ("testAlreadyOn", 83),
          ("testNotOn", 84),
          ("loopUpFailure", 85),
          ("loopDownFailure", 86),
          ("bertPatternSyncFailure", 87))
    )


_StrmErrCode_Type.__name__ = "Integer32"
_StrmErrCode_Object = MibTableColumn
strmErrCode = _StrmErrCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 910, 2, 1, 2),
    _StrmErrCode_Type()
)
strmErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strmErrCode.setStatus("mandatory")
_StrmErrStatusDesc_Type = DisplayString
_StrmErrStatusDesc_Object = MibTableColumn
strmErrStatusDesc = _StrmErrStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 910, 2, 1, 3),
    _StrmErrStatusDesc_Type()
)
strmErrStatusDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strmErrStatusDesc.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STRATACOM-ERROR-MIB",
    **{"stratacom": stratacom,
       "strmErrors": strmErrors,
       "strmErrStatusLastIndex": strmErrStatusLastIndex,
       "strmErrStatusTable": strmErrStatusTable,
       "strmErrStatusTableEntry": strmErrStatusTableEntry,
       "strmErrReqId": strmErrReqId,
       "strmErrCode": strmErrCode,
       "strmErrStatusDesc": strmErrStatusDesc}
)
