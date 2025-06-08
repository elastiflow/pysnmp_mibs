# SNMP MIB module (CALIX-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-PM-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:18:56 2025
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

(calixManagement,
 calixModules) = mibBuilder.importSymbols(
    "CALIX-SMI",
    "calixManagement",
    "calixModules")

(InterfaceIndex,
 OcWidth,
 Pst,
 StsWidth,
 Tl1Aid) = mibBuilder.importSymbols(
    "CALIX-TC",
    "InterfaceIndex",
    "OcWidth",
    "Pst",
    "StsWidth",
    "Tl1Aid")

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
 NotificationType,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "NotificationType",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

calixPmMod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 1, 3)
)
if mibBuilder.loadTexts:
    calixPmMod.setRevisions(
        ("2002-01-28 00:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PerfBinCount(TextualConvention, Gauge32):
    status = "current"


class PmBinNumber(TextualConvention, Integer32):
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
              101,
              102,
              103,
              104,
              105,
              106,
              107)
        )
    )
    namedValues = NamedValues(
        *(("qhbin1", 1),
          ("qhbin2", 2),
          ("qhbin3", 3),
          ("qhbin4", 4),
          ("qhbin5", 5),
          ("qhbin6", 6),
          ("qhbin7", 7),
          ("qhbin8", 8),
          ("qhbin9", 9),
          ("qhbin10", 10),
          ("qhbin11", 11),
          ("qhbin12", 12),
          ("qhbin13", 13),
          ("qhbin14", 14),
          ("qhbin15", 15),
          ("qhbin16", 16),
          ("qhbin17", 17),
          ("qhbin18", 18),
          ("qhbin19", 19),
          ("qhbin20", 20),
          ("qhbin21", 21),
          ("qhbin22", 22),
          ("qhbin23", 23),
          ("qhbin24", 24),
          ("qhbin25", 25),
          ("qhbin26", 26),
          ("qhbin27", 27),
          ("qhbin28", 28),
          ("qhbin29", 29),
          ("qhbin30", 30),
          ("qhbin31", 31),
          ("qhbin32", 32),
          ("daybin1", 101),
          ("daybin2", 102),
          ("daybin3", 103),
          ("daybin4", 104),
          ("daybin5", 105),
          ("daybin6", 106),
          ("daybin7", 107))
    )



class PmValidity(TextualConvention, Integer32):
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
        *(("pmAdjusted", 1),
          ("pmCompleted", 2),
          ("pmLonger", 3),
          ("pmNotAvailable", 4),
          ("pmPartial", 5),
          ("pmInvalid", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CalixPmMIB_ObjectIdentity = ObjectIdentity
calixPmMIB = _CalixPmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3)
)
_CalixAdslNePm_ObjectIdentity = ObjectIdentity
calixAdslNePm = _CalixAdslNePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1)
)
_CalixAdslNePmTable_Object = MibTable
calixAdslNePmTable = _CalixAdslNePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    calixAdslNePmTable.setStatus("current")
_CalixAdslNePmEntry_Object = MibTableRow
calixAdslNePmEntry = _CalixAdslNePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1)
)
calixAdslNePmEntry.setIndexNames(
    (0, "CALIX-PM-MIB", "calixIfIndex"),
    (0, "CALIX-PM-MIB", "calixAdslPmBinNumber"),
)
if mibBuilder.loadTexts:
    calixAdslNePmEntry.setStatus("current")
_CalixIfIndex_Type = InterfaceIndex
_CalixIfIndex_Object = MibTableColumn
calixIfIndex = _CalixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 1),
    _CalixIfIndex_Type()
)
calixIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixIfIndex.setStatus("current")
_CalixAdslPmBinNumber_Type = PmBinNumber
_CalixAdslPmBinNumber_Object = MibTableColumn
calixAdslPmBinNumber = _CalixAdslPmBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 2),
    _CalixAdslPmBinNumber_Type()
)
calixAdslPmBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslPmBinNumber.setStatus("current")
_CalixAdslNePmTl1Aid_Type = Tl1Aid
_CalixAdslNePmTl1Aid_Object = MibTableColumn
calixAdslNePmTl1Aid = _CalixAdslNePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 3),
    _CalixAdslNePmTl1Aid_Type()
)
calixAdslNePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmTl1Aid.setStatus("current")
_CalixAdslNePmValidity_Type = PmValidity
_CalixAdslNePmValidity_Object = MibTableColumn
calixAdslNePmValidity = _CalixAdslNePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 4),
    _CalixAdslNePmValidity_Type()
)
calixAdslNePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmValidity.setStatus("current")
_CalixAdslNePmCvfL_Type = PerfBinCount
_CalixAdslNePmCvfL_Object = MibTableColumn
calixAdslNePmCvfL = _CalixAdslNePmCvfL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 5),
    _CalixAdslNePmCvfL_Type()
)
calixAdslNePmCvfL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmCvfL.setStatus("current")
_CalixAdslNePmCviL_Type = PerfBinCount
_CalixAdslNePmCviL_Object = MibTableColumn
calixAdslNePmCviL = _CalixAdslNePmCviL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 6),
    _CalixAdslNePmCviL_Type()
)
calixAdslNePmCviL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmCviL.setStatus("current")
_CalixAdslNePmEcfL_Type = PerfBinCount
_CalixAdslNePmEcfL_Object = MibTableColumn
calixAdslNePmEcfL = _CalixAdslNePmEcfL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 7),
    _CalixAdslNePmEcfL_Type()
)
calixAdslNePmEcfL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmEcfL.setStatus("current")
_CalixAdslNePmEciL_Type = PerfBinCount
_CalixAdslNePmEciL_Object = MibTableColumn
calixAdslNePmEciL = _CalixAdslNePmEciL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 8),
    _CalixAdslNePmEciL_Type()
)
calixAdslNePmEciL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmEciL.setStatus("current")
_CalixAdslNePmEcsL_Type = PerfBinCount
_CalixAdslNePmEcsL_Object = MibTableColumn
calixAdslNePmEcsL = _CalixAdslNePmEcsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 9),
    _CalixAdslNePmEcsL_Type()
)
calixAdslNePmEcsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmEcsL.setStatus("current")
_CalixAdslNePmEsL_Type = PerfBinCount
_CalixAdslNePmEsL_Object = MibTableColumn
calixAdslNePmEsL = _CalixAdslNePmEsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 10),
    _CalixAdslNePmEsL_Type()
)
calixAdslNePmEsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmEsL.setStatus("current")
_CalixAdslNePmFr_Type = PerfBinCount
_CalixAdslNePmFr_Object = MibTableColumn
calixAdslNePmFr = _CalixAdslNePmFr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 11),
    _CalixAdslNePmFr_Type()
)
calixAdslNePmFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmFr.setStatus("current")
_CalixAdslNePmFrf_Type = PerfBinCount
_CalixAdslNePmFrf_Object = MibTableColumn
calixAdslNePmFrf = _CalixAdslNePmFrf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 12),
    _CalixAdslNePmFrf_Type()
)
calixAdslNePmFrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmFrf.setStatus("current")
_CalixAdslNePmHecccfP_Type = PerfBinCount
_CalixAdslNePmHecccfP_Object = MibTableColumn
calixAdslNePmHecccfP = _CalixAdslNePmHecccfP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 13),
    _CalixAdslNePmHecccfP_Type()
)
calixAdslNePmHecccfP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmHecccfP.setStatus("current")
_CalixAdslNePmHeccciP_Type = PerfBinCount
_CalixAdslNePmHeccciP_Object = MibTableColumn
calixAdslNePmHeccciP = _CalixAdslNePmHeccciP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 14),
    _CalixAdslNePmHeccciP_Type()
)
calixAdslNePmHeccciP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmHeccciP.setStatus("current")
_CalixAdslNePmHeccvfP_Type = PerfBinCount
_CalixAdslNePmHeccvfP_Object = MibTableColumn
calixAdslNePmHeccvfP = _CalixAdslNePmHeccvfP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 15),
    _CalixAdslNePmHeccvfP_Type()
)
calixAdslNePmHeccvfP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmHeccvfP.setStatus("current")
_CalixAdslNePmHeccviP_Type = PerfBinCount
_CalixAdslNePmHeccviP_Object = MibTableColumn
calixAdslNePmHeccviP = _CalixAdslNePmHeccviP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 16),
    _CalixAdslNePmHeccviP_Type()
)
calixAdslNePmHeccviP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmHeccviP.setStatus("current")
_CalixAdslNePmIngTcc0P_Type = PerfBinCount
_CalixAdslNePmIngTcc0P_Object = MibTableColumn
calixAdslNePmIngTcc0P = _CalixAdslNePmIngTcc0P_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 17),
    _CalixAdslNePmIngTcc0P_Type()
)
calixAdslNePmIngTcc0P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmIngTcc0P.setStatus("current")
_CalixAdslNePmIngTcc1P_Type = PerfBinCount
_CalixAdslNePmIngTcc1P_Object = MibTableColumn
calixAdslNePmIngTcc1P = _CalixAdslNePmIngTcc1P_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 18),
    _CalixAdslNePmIngTcc1P_Type()
)
calixAdslNePmIngTcc1P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmIngTcc1P.setStatus("current")
_CalixAdslNePmLossL_Type = PerfBinCount
_CalixAdslNePmLossL_Object = MibTableColumn
calixAdslNePmLossL = _CalixAdslNePmLossL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 19),
    _CalixAdslNePmLossL_Type()
)
calixAdslNePmLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmLossL.setStatus("current")
_CalixAdslNePmSesL_Type = PerfBinCount
_CalixAdslNePmSesL_Object = MibTableColumn
calixAdslNePmSesL = _CalixAdslNePmSesL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 20),
    _CalixAdslNePmSesL_Type()
)
calixAdslNePmSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmSesL.setStatus("current")
_CalixAdslNePmTcc0Pe_Type = PerfBinCount
_CalixAdslNePmTcc0Pe_Object = MibTableColumn
calixAdslNePmTcc0Pe = _CalixAdslNePmTcc0Pe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 21),
    _CalixAdslNePmTcc0Pe_Type()
)
calixAdslNePmTcc0Pe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmTcc0Pe.setStatus("current")
_CalixAdslNePmTcc1Pe_Type = PerfBinCount
_CalixAdslNePmTcc1Pe_Object = MibTableColumn
calixAdslNePmTcc1Pe = _CalixAdslNePmTcc1Pe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 22),
    _CalixAdslNePmTcc1Pe_Type()
)
calixAdslNePmTcc1Pe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmTcc1Pe.setStatus("current")
_CalixAdslNePmUasL_Type = PerfBinCount
_CalixAdslNePmUasL_Object = MibTableColumn
calixAdslNePmUasL = _CalixAdslNePmUasL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1, 1, 23),
    _CalixAdslNePmUasL_Type()
)
calixAdslNePmUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslNePmUasL.setStatus("current")
_CalixAdslFePm_ObjectIdentity = ObjectIdentity
calixAdslFePm = _CalixAdslFePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2)
)
_CalixAdslFePmTable_Object = MibTable
calixAdslFePmTable = _CalixAdslFePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    calixAdslFePmTable.setStatus("current")
_CalixAdslFePmEntry_Object = MibTableRow
calixAdslFePmEntry = _CalixAdslFePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    calixAdslFePmEntry.setStatus("current")
_CalixAdslFePmTl1Aid_Type = Tl1Aid
_CalixAdslFePmTl1Aid_Object = MibTableColumn
calixAdslFePmTl1Aid = _CalixAdslFePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 1),
    _CalixAdslFePmTl1Aid_Type()
)
calixAdslFePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmTl1Aid.setStatus("current")
_CalixAdslFePmValidity_Type = PmValidity
_CalixAdslFePmValidity_Object = MibTableColumn
calixAdslFePmValidity = _CalixAdslFePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 2),
    _CalixAdslFePmValidity_Type()
)
calixAdslFePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmValidity.setStatus("current")
_CalixAdslFePmCvfL_Type = PerfBinCount
_CalixAdslFePmCvfL_Object = MibTableColumn
calixAdslFePmCvfL = _CalixAdslFePmCvfL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 3),
    _CalixAdslFePmCvfL_Type()
)
calixAdslFePmCvfL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmCvfL.setStatus("current")
_CalixAdslFePmCviL_Type = PerfBinCount
_CalixAdslFePmCviL_Object = MibTableColumn
calixAdslFePmCviL = _CalixAdslFePmCviL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 4),
    _CalixAdslFePmCviL_Type()
)
calixAdslFePmCviL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmCviL.setStatus("current")
_CalixAdslFePmEcfL_Type = PerfBinCount
_CalixAdslFePmEcfL_Object = MibTableColumn
calixAdslFePmEcfL = _CalixAdslFePmEcfL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 5),
    _CalixAdslFePmEcfL_Type()
)
calixAdslFePmEcfL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmEcfL.setStatus("current")
_CalixAdslFePmEciL_Type = PerfBinCount
_CalixAdslFePmEciL_Object = MibTableColumn
calixAdslFePmEciL = _CalixAdslFePmEciL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 6),
    _CalixAdslFePmEciL_Type()
)
calixAdslFePmEciL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmEciL.setStatus("current")
_CalixAdslFePmEcsL_Type = PerfBinCount
_CalixAdslFePmEcsL_Object = MibTableColumn
calixAdslFePmEcsL = _CalixAdslFePmEcsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 7),
    _CalixAdslFePmEcsL_Type()
)
calixAdslFePmEcsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmEcsL.setStatus("current")
_CalixAdslFePmEsL_Type = PerfBinCount
_CalixAdslFePmEsL_Object = MibTableColumn
calixAdslFePmEsL = _CalixAdslFePmEsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 8),
    _CalixAdslFePmEsL_Type()
)
calixAdslFePmEsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmEsL.setStatus("current")
_CalixAdslFePmSesL_Type = PerfBinCount
_CalixAdslFePmSesL_Object = MibTableColumn
calixAdslFePmSesL = _CalixAdslFePmSesL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 9),
    _CalixAdslFePmSesL_Type()
)
calixAdslFePmSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmSesL.setStatus("current")
_CalixAdslFePmUasL_Type = PerfBinCount
_CalixAdslFePmUasL_Object = MibTableColumn
calixAdslFePmUasL = _CalixAdslFePmUasL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1, 1, 10),
    _CalixAdslFePmUasL_Type()
)
calixAdslFePmUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslFePmUasL.setStatus("current")
_CalixDs1NePm_ObjectIdentity = ObjectIdentity
calixDs1NePm = _CalixDs1NePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3)
)
_CalixDs1NePmTable_Object = MibTable
calixDs1NePmTable = _CalixDs1NePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    calixDs1NePmTable.setStatus("current")
_CalixDs1NePmEntry_Object = MibTableRow
calixDs1NePmEntry = _CalixDs1NePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1)
)
calixDs1NePmEntry.setIndexNames(
    (0, "CALIX-PM-MIB", "calixIfIndex"),
    (0, "CALIX-PM-MIB", "calixDs1PmBinNumber"),
)
if mibBuilder.loadTexts:
    calixDs1NePmEntry.setStatus("current")
_CalixDs1PmBinNumber_Type = PmBinNumber
_CalixDs1PmBinNumber_Object = MibTableColumn
calixDs1PmBinNumber = _CalixDs1PmBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 1),
    _CalixDs1PmBinNumber_Type()
)
calixDs1PmBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1PmBinNumber.setStatus("current")
_CalixDs1NePmTl1Aid_Type = Tl1Aid
_CalixDs1NePmTl1Aid_Object = MibTableColumn
calixDs1NePmTl1Aid = _CalixDs1NePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 2),
    _CalixDs1NePmTl1Aid_Type()
)
calixDs1NePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmTl1Aid.setStatus("current")
_CalixDs1NePmValidity_Type = PmValidity
_CalixDs1NePmValidity_Object = MibTableColumn
calixDs1NePmValidity = _CalixDs1NePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 3),
    _CalixDs1NePmValidity_Type()
)
calixDs1NePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmValidity.setStatus("current")
_CalixDs1NePmCssP_Type = PerfBinCount
_CalixDs1NePmCssP_Object = MibTableColumn
calixDs1NePmCssP = _CalixDs1NePmCssP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 4),
    _CalixDs1NePmCssP_Type()
)
calixDs1NePmCssP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmCssP.setStatus("current")
_CalixDs1NePmCvL_Type = PerfBinCount
_CalixDs1NePmCvL_Object = MibTableColumn
calixDs1NePmCvL = _CalixDs1NePmCvL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 5),
    _CalixDs1NePmCvL_Type()
)
calixDs1NePmCvL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmCvL.setStatus("current")
_CalixDs1NePmCvP_Type = PerfBinCount
_CalixDs1NePmCvP_Object = MibTableColumn
calixDs1NePmCvP = _CalixDs1NePmCvP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 6),
    _CalixDs1NePmCvP_Type()
)
calixDs1NePmCvP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmCvP.setStatus("current")
_CalixDs1NePmEsL_Type = PerfBinCount
_CalixDs1NePmEsL_Object = MibTableColumn
calixDs1NePmEsL = _CalixDs1NePmEsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 7),
    _CalixDs1NePmEsL_Type()
)
calixDs1NePmEsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmEsL.setStatus("current")
_CalixDs1NePmEsP_Type = PerfBinCount
_CalixDs1NePmEsP_Object = MibTableColumn
calixDs1NePmEsP = _CalixDs1NePmEsP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 8),
    _CalixDs1NePmEsP_Type()
)
calixDs1NePmEsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmEsP.setStatus("current")
_CalixDs1NePmFcP_Type = PerfBinCount
_CalixDs1NePmFcP_Object = MibTableColumn
calixDs1NePmFcP = _CalixDs1NePmFcP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 9),
    _CalixDs1NePmFcP_Type()
)
calixDs1NePmFcP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmFcP.setStatus("current")
_CalixDs1NePmLossL_Type = PerfBinCount
_CalixDs1NePmLossL_Object = MibTableColumn
calixDs1NePmLossL = _CalixDs1NePmLossL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 10),
    _CalixDs1NePmLossL_Type()
)
calixDs1NePmLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmLossL.setStatus("current")
_CalixDs1NePmSasP_Type = PerfBinCount
_CalixDs1NePmSasP_Object = MibTableColumn
calixDs1NePmSasP = _CalixDs1NePmSasP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 11),
    _CalixDs1NePmSasP_Type()
)
calixDs1NePmSasP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmSasP.setStatus("current")
_CalixDs1NePmSesL_Type = PerfBinCount
_CalixDs1NePmSesL_Object = MibTableColumn
calixDs1NePmSesL = _CalixDs1NePmSesL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 12),
    _CalixDs1NePmSesL_Type()
)
calixDs1NePmSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmSesL.setStatus("current")
_CalixDs1NePmSesP_Type = PerfBinCount
_CalixDs1NePmSesP_Object = MibTableColumn
calixDs1NePmSesP = _CalixDs1NePmSesP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 13),
    _CalixDs1NePmSesP_Type()
)
calixDs1NePmSesP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmSesP.setStatus("current")
_CalixDs1NePmUasP_Type = PerfBinCount
_CalixDs1NePmUasP_Object = MibTableColumn
calixDs1NePmUasP = _CalixDs1NePmUasP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 3, 1, 1, 14),
    _CalixDs1NePmUasP_Type()
)
calixDs1NePmUasP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1NePmUasP.setStatus("current")
_CalixDs1FePm_ObjectIdentity = ObjectIdentity
calixDs1FePm = _CalixDs1FePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4)
)
_CalixDs1FePmTable_Object = MibTable
calixDs1FePmTable = _CalixDs1FePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    calixDs1FePmTable.setStatus("current")
_CalixDs1FePmEntry_Object = MibTableRow
calixDs1FePmEntry = _CalixDs1FePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    calixDs1FePmEntry.setStatus("current")
_CalixDs1FePmTl1Aid_Type = Tl1Aid
_CalixDs1FePmTl1Aid_Object = MibTableColumn
calixDs1FePmTl1Aid = _CalixDs1FePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 1),
    _CalixDs1FePmTl1Aid_Type()
)
calixDs1FePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmTl1Aid.setStatus("current")
_CalixDs1FePmValidity_Type = PmValidity
_CalixDs1FePmValidity_Object = MibTableColumn
calixDs1FePmValidity = _CalixDs1FePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 2),
    _CalixDs1FePmValidity_Type()
)
calixDs1FePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmValidity.setStatus("current")
_CalixDs1FePmCssP_Type = PerfBinCount
_CalixDs1FePmCssP_Object = MibTableColumn
calixDs1FePmCssP = _CalixDs1FePmCssP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 3),
    _CalixDs1FePmCssP_Type()
)
calixDs1FePmCssP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmCssP.setStatus("current")
_CalixDs1FePmCvP_Type = PerfBinCount
_CalixDs1FePmCvP_Object = MibTableColumn
calixDs1FePmCvP = _CalixDs1FePmCvP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 4),
    _CalixDs1FePmCvP_Type()
)
calixDs1FePmCvP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmCvP.setStatus("current")
_CalixDs1FePmEsL_Type = PerfBinCount
_CalixDs1FePmEsL_Object = MibTableColumn
calixDs1FePmEsL = _CalixDs1FePmEsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 5),
    _CalixDs1FePmEsL_Type()
)
calixDs1FePmEsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmEsL.setStatus("current")
_CalixDs1FePmEsP_Type = PerfBinCount
_CalixDs1FePmEsP_Object = MibTableColumn
calixDs1FePmEsP = _CalixDs1FePmEsP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 6),
    _CalixDs1FePmEsP_Type()
)
calixDs1FePmEsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmEsP.setStatus("current")
_CalixDs1FePmFcP_Type = PerfBinCount
_CalixDs1FePmFcP_Object = MibTableColumn
calixDs1FePmFcP = _CalixDs1FePmFcP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 7),
    _CalixDs1FePmFcP_Type()
)
calixDs1FePmFcP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmFcP.setStatus("current")
_CalixDs1FePmSefsP_Type = PerfBinCount
_CalixDs1FePmSefsP_Object = MibTableColumn
calixDs1FePmSefsP = _CalixDs1FePmSefsP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 8),
    _CalixDs1FePmSefsP_Type()
)
calixDs1FePmSefsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmSefsP.setStatus("current")
_CalixDs1FePmSesP_Type = PerfBinCount
_CalixDs1FePmSesP_Object = MibTableColumn
calixDs1FePmSesP = _CalixDs1FePmSesP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 9),
    _CalixDs1FePmSesP_Type()
)
calixDs1FePmSesP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmSesP.setStatus("current")
_CalixDs1FePmUasP_Type = PerfBinCount
_CalixDs1FePmUasP_Object = MibTableColumn
calixDs1FePmUasP = _CalixDs1FePmUasP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 4, 1, 1, 10),
    _CalixDs1FePmUasP_Type()
)
calixDs1FePmUasP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1FePmUasP.setStatus("current")
_CalixDs3NePm_ObjectIdentity = ObjectIdentity
calixDs3NePm = _CalixDs3NePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5)
)
_CalixDs3NePmTable_Object = MibTable
calixDs3NePmTable = _CalixDs3NePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    calixDs3NePmTable.setStatus("current")
_CalixDs3NePmEntry_Object = MibTableRow
calixDs3NePmEntry = _CalixDs3NePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1)
)
calixDs3NePmEntry.setIndexNames(
    (0, "CALIX-PM-MIB", "calixIfIndex"),
    (0, "CALIX-PM-MIB", "calixDs3PmBinNumber"),
)
if mibBuilder.loadTexts:
    calixDs3NePmEntry.setStatus("current")
_CalixDs3PmBinNumber_Type = PmBinNumber
_CalixDs3PmBinNumber_Object = MibTableColumn
calixDs3PmBinNumber = _CalixDs3PmBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 1),
    _CalixDs3PmBinNumber_Type()
)
calixDs3PmBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3PmBinNumber.setStatus("current")
_CalixDs3NePmTl1Aid_Type = Tl1Aid
_CalixDs3NePmTl1Aid_Object = MibTableColumn
calixDs3NePmTl1Aid = _CalixDs3NePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 2),
    _CalixDs3NePmTl1Aid_Type()
)
calixDs3NePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmTl1Aid.setStatus("current")
_CalixDs3NePmValidity_Type = PmValidity
_CalixDs3NePmValidity_Object = MibTableColumn
calixDs3NePmValidity = _CalixDs3NePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 3),
    _CalixDs3NePmValidity_Type()
)
calixDs3NePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmValidity.setStatus("current")
_CalixDs3NePmAissP_Type = PerfBinCount
_CalixDs3NePmAissP_Object = MibTableColumn
calixDs3NePmAissP = _CalixDs3NePmAissP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 4),
    _CalixDs3NePmAissP_Type()
)
calixDs3NePmAissP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmAissP.setStatus("current")
_CalixDs3NePmAissPe_Type = PerfBinCount
_CalixDs3NePmAissPe_Object = MibTableColumn
calixDs3NePmAissPe = _CalixDs3NePmAissPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 5),
    _CalixDs3NePmAissPe_Type()
)
calixDs3NePmAissPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmAissPe.setStatus("current")
_CalixDs3NePmCvCpP_Type = PerfBinCount
_CalixDs3NePmCvCpP_Object = MibTableColumn
calixDs3NePmCvCpP = _CalixDs3NePmCvCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 6),
    _CalixDs3NePmCvCpP_Type()
)
calixDs3NePmCvCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmCvCpP.setStatus("current")
_CalixDs3NePmCvCpPe_Type = PerfBinCount
_CalixDs3NePmCvCpPe_Object = MibTableColumn
calixDs3NePmCvCpPe = _CalixDs3NePmCvCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 7),
    _CalixDs3NePmCvCpPe_Type()
)
calixDs3NePmCvCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmCvCpPe.setStatus("current")
_CalixDs3NePmCvL_Type = PerfBinCount
_CalixDs3NePmCvL_Object = MibTableColumn
calixDs3NePmCvL = _CalixDs3NePmCvL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 8),
    _CalixDs3NePmCvL_Type()
)
calixDs3NePmCvL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmCvL.setStatus("current")
_CalixDs3NePmCvpP_Type = PerfBinCount
_CalixDs3NePmCvpP_Object = MibTableColumn
calixDs3NePmCvpP = _CalixDs3NePmCvpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 9),
    _CalixDs3NePmCvpP_Type()
)
calixDs3NePmCvpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmCvpP.setStatus("current")
_CalixDs3NePmCvpPe_Type = PerfBinCount
_CalixDs3NePmCvpPe_Object = MibTableColumn
calixDs3NePmCvpPe = _CalixDs3NePmCvpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 10),
    _CalixDs3NePmCvpPe_Type()
)
calixDs3NePmCvpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmCvpPe.setStatus("current")
_CalixDs3NePmDscc_Type = PerfBinCount
_CalixDs3NePmDscc_Object = MibTableColumn
calixDs3NePmDscc = _CalixDs3NePmDscc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 11),
    _CalixDs3NePmDscc_Type()
)
calixDs3NePmDscc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmDscc.setStatus("current")
_CalixDs3NePmDscce_Type = PerfBinCount
_CalixDs3NePmDscce_Object = MibTableColumn
calixDs3NePmDscce = _CalixDs3NePmDscce_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 12),
    _CalixDs3NePmDscce_Type()
)
calixDs3NePmDscce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmDscce.setStatus("current")
_CalixDs3NePmEsCpP_Type = PerfBinCount
_CalixDs3NePmEsCpP_Object = MibTableColumn
calixDs3NePmEsCpP = _CalixDs3NePmEsCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 13),
    _CalixDs3NePmEsCpP_Type()
)
calixDs3NePmEsCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmEsCpP.setStatus("current")
_CalixDs3NePmEsCpPe_Type = PerfBinCount
_CalixDs3NePmEsCpPe_Object = MibTableColumn
calixDs3NePmEsCpPe = _CalixDs3NePmEsCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 14),
    _CalixDs3NePmEsCpPe_Type()
)
calixDs3NePmEsCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmEsCpPe.setStatus("current")
_CalixDs3NePmEsL_Type = PerfBinCount
_CalixDs3NePmEsL_Object = MibTableColumn
calixDs3NePmEsL = _CalixDs3NePmEsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 15),
    _CalixDs3NePmEsL_Type()
)
calixDs3NePmEsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmEsL.setStatus("current")
_CalixDs3NePmEspP_Type = PerfBinCount
_CalixDs3NePmEspP_Object = MibTableColumn
calixDs3NePmEspP = _CalixDs3NePmEspP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 16),
    _CalixDs3NePmEspP_Type()
)
calixDs3NePmEspP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmEspP.setStatus("current")
_CalixDs3NePmEspPe_Type = PerfBinCount
_CalixDs3NePmEspPe_Object = MibTableColumn
calixDs3NePmEspPe = _CalixDs3NePmEspPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 17),
    _CalixDs3NePmEspPe_Type()
)
calixDs3NePmEspPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmEspPe.setStatus("current")
_CalixDs3NePmEsPlcp_Type = PerfBinCount
_CalixDs3NePmEsPlcp_Object = MibTableColumn
calixDs3NePmEsPlcp = _CalixDs3NePmEsPlcp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 18),
    _CalixDs3NePmEsPlcp_Type()
)
calixDs3NePmEsPlcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmEsPlcp.setStatus("current")
_CalixDs3NePmFcP_Type = PerfBinCount
_CalixDs3NePmFcP_Object = MibTableColumn
calixDs3NePmFcP = _CalixDs3NePmFcP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 19),
    _CalixDs3NePmFcP_Type()
)
calixDs3NePmFcP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmFcP.setStatus("current")
_CalixDs3NePmFcPe_Type = PerfBinCount
_CalixDs3NePmFcPe_Object = MibTableColumn
calixDs3NePmFcPe = _CalixDs3NePmFcPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 20),
    _CalixDs3NePmFcPe_Type()
)
calixDs3NePmFcPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmFcPe.setStatus("current")
_CalixDs3NePmHecc_Type = PerfBinCount
_CalixDs3NePmHecc_Object = MibTableColumn
calixDs3NePmHecc = _CalixDs3NePmHecc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 21),
    _CalixDs3NePmHecc_Type()
)
calixDs3NePmHecc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmHecc.setStatus("current")
_CalixDs3NePmHecce_Type = PerfBinCount
_CalixDs3NePmHecce_Object = MibTableColumn
calixDs3NePmHecce = _CalixDs3NePmHecce_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 22),
    _CalixDs3NePmHecce_Type()
)
calixDs3NePmHecce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmHecce.setStatus("current")
_CalixDs3NePmHecuc_Type = PerfBinCount
_CalixDs3NePmHecuc_Object = MibTableColumn
calixDs3NePmHecuc = _CalixDs3NePmHecuc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 23),
    _CalixDs3NePmHecuc_Type()
)
calixDs3NePmHecuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmHecuc.setStatus("current")
_CalixDs3NePmHecuce_Type = PerfBinCount
_CalixDs3NePmHecuce_Object = MibTableColumn
calixDs3NePmHecuce = _CalixDs3NePmHecuce_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 24),
    _CalixDs3NePmHecuce_Type()
)
calixDs3NePmHecuce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmHecuce.setStatus("current")
_CalixDs3NePmLcds_Type = PerfBinCount
_CalixDs3NePmLcds_Object = MibTableColumn
calixDs3NePmLcds = _CalixDs3NePmLcds_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 25),
    _CalixDs3NePmLcds_Type()
)
calixDs3NePmLcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmLcds.setStatus("current")
_CalixDs3NePmLcdse_Type = PerfBinCount
_CalixDs3NePmLcdse_Object = MibTableColumn
calixDs3NePmLcdse = _CalixDs3NePmLcdse_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 26),
    _CalixDs3NePmLcdse_Type()
)
calixDs3NePmLcdse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmLcdse.setStatus("current")
_CalixDs3NePmLossL_Type = PerfBinCount
_CalixDs3NePmLossL_Object = MibTableColumn
calixDs3NePmLossL = _CalixDs3NePmLossL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 27),
    _CalixDs3NePmLossL_Type()
)
calixDs3NePmLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmLossL.setStatus("current")
_CalixDs3NePmSasP_Type = PerfBinCount
_CalixDs3NePmSasP_Object = MibTableColumn
calixDs3NePmSasP = _CalixDs3NePmSasP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 28),
    _CalixDs3NePmSasP_Type()
)
calixDs3NePmSasP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmSasP.setStatus("current")
_CalixDs3NePmSasPe_Type = PerfBinCount
_CalixDs3NePmSasPe_Object = MibTableColumn
calixDs3NePmSasPe = _CalixDs3NePmSasPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 29),
    _CalixDs3NePmSasPe_Type()
)
calixDs3NePmSasPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmSasPe.setStatus("current")
_CalixDs3NePmSesCpP_Type = PerfBinCount
_CalixDs3NePmSesCpP_Object = MibTableColumn
calixDs3NePmSesCpP = _CalixDs3NePmSesCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 30),
    _CalixDs3NePmSesCpP_Type()
)
calixDs3NePmSesCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmSesCpP.setStatus("current")
_CalixDs3NePmSesCpPe_Type = PerfBinCount
_CalixDs3NePmSesCpPe_Object = MibTableColumn
calixDs3NePmSesCpPe = _CalixDs3NePmSesCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 31),
    _CalixDs3NePmSesCpPe_Type()
)
calixDs3NePmSesCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmSesCpPe.setStatus("current")
_CalixDs3NePmSesL_Type = PerfBinCount
_CalixDs3NePmSesL_Object = MibTableColumn
calixDs3NePmSesL = _CalixDs3NePmSesL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 32),
    _CalixDs3NePmSesL_Type()
)
calixDs3NePmSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmSesL.setStatus("current")
_CalixDs3NePmSespP_Type = PerfBinCount
_CalixDs3NePmSespP_Object = MibTableColumn
calixDs3NePmSespP = _CalixDs3NePmSespP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 33),
    _CalixDs3NePmSespP_Type()
)
calixDs3NePmSespP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmSespP.setStatus("current")
_CalixDs3NePmSespPe_Type = PerfBinCount
_CalixDs3NePmSespPe_Object = MibTableColumn
calixDs3NePmSespPe = _CalixDs3NePmSespPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 34),
    _CalixDs3NePmSespPe_Type()
)
calixDs3NePmSespPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmSespPe.setStatus("current")
_CalixDs3NePmUasCpP_Type = PerfBinCount
_CalixDs3NePmUasCpP_Object = MibTableColumn
calixDs3NePmUasCpP = _CalixDs3NePmUasCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 35),
    _CalixDs3NePmUasCpP_Type()
)
calixDs3NePmUasCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmUasCpP.setStatus("current")
_CalixDs3NePmUasCpPe_Type = PerfBinCount
_CalixDs3NePmUasCpPe_Object = MibTableColumn
calixDs3NePmUasCpPe = _CalixDs3NePmUasCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 36),
    _CalixDs3NePmUasCpPe_Type()
)
calixDs3NePmUasCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmUasCpPe.setStatus("current")
_CalixDs3NePmUaspP_Type = PerfBinCount
_CalixDs3NePmUaspP_Object = MibTableColumn
calixDs3NePmUaspP = _CalixDs3NePmUaspP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 37),
    _CalixDs3NePmUaspP_Type()
)
calixDs3NePmUaspP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmUaspP.setStatus("current")
_CalixDs3NePmUaspPe_Type = PerfBinCount
_CalixDs3NePmUaspPe_Object = MibTableColumn
calixDs3NePmUaspPe = _CalixDs3NePmUaspPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 38),
    _CalixDs3NePmUaspPe_Type()
)
calixDs3NePmUaspPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmUaspPe.setStatus("current")
_CalixDs3NePmUtcc_Type = PerfBinCount
_CalixDs3NePmUtcc_Object = MibTableColumn
calixDs3NePmUtcc = _CalixDs3NePmUtcc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 39),
    _CalixDs3NePmUtcc_Type()
)
calixDs3NePmUtcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmUtcc.setStatus("current")
_CalixDs3NePmUtcce_Type = PerfBinCount
_CalixDs3NePmUtcce_Object = MibTableColumn
calixDs3NePmUtcce = _CalixDs3NePmUtcce_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 5, 1, 1, 40),
    _CalixDs3NePmUtcce_Type()
)
calixDs3NePmUtcce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3NePmUtcce.setStatus("current")
_CalixDs3FePm_ObjectIdentity = ObjectIdentity
calixDs3FePm = _CalixDs3FePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6)
)
_CalixDs3FePmTable_Object = MibTable
calixDs3FePmTable = _CalixDs3FePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    calixDs3FePmTable.setStatus("current")
_CalixDs3FePmEntry_Object = MibTableRow
calixDs3FePmEntry = _CalixDs3FePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    calixDs3FePmEntry.setStatus("current")
_CalixDs3FePmTl1Aid_Type = Tl1Aid
_CalixDs3FePmTl1Aid_Object = MibTableColumn
calixDs3FePmTl1Aid = _CalixDs3FePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 1),
    _CalixDs3FePmTl1Aid_Type()
)
calixDs3FePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmTl1Aid.setStatus("current")
_CalixDs3FePmValidity_Type = PmValidity
_CalixDs3FePmValidity_Object = MibTableColumn
calixDs3FePmValidity = _CalixDs3FePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 2),
    _CalixDs3FePmValidity_Type()
)
calixDs3FePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmValidity.setStatus("current")
_CalixDs3FePmCvCpP_Type = PerfBinCount
_CalixDs3FePmCvCpP_Object = MibTableColumn
calixDs3FePmCvCpP = _CalixDs3FePmCvCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 3),
    _CalixDs3FePmCvCpP_Type()
)
calixDs3FePmCvCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmCvCpP.setStatus("current")
_CalixDs3FePmCvCpPe_Type = PerfBinCount
_CalixDs3FePmCvCpPe_Object = MibTableColumn
calixDs3FePmCvCpPe = _CalixDs3FePmCvCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 4),
    _CalixDs3FePmCvCpPe_Type()
)
calixDs3FePmCvCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmCvCpPe.setStatus("current")
_CalixDs3FePmEsCpP_Type = PerfBinCount
_CalixDs3FePmEsCpP_Object = MibTableColumn
calixDs3FePmEsCpP = _CalixDs3FePmEsCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 5),
    _CalixDs3FePmEsCpP_Type()
)
calixDs3FePmEsCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmEsCpP.setStatus("current")
_CalixDs3FePmEsCpPe_Type = PerfBinCount
_CalixDs3FePmEsCpPe_Object = MibTableColumn
calixDs3FePmEsCpPe = _CalixDs3FePmEsCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 6),
    _CalixDs3FePmEsCpPe_Type()
)
calixDs3FePmEsCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmEsCpPe.setStatus("current")
_CalixDs3FePmEsPlcp_Type = PerfBinCount
_CalixDs3FePmEsPlcp_Object = MibTableColumn
calixDs3FePmEsPlcp = _CalixDs3FePmEsPlcp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 7),
    _CalixDs3FePmEsPlcp_Type()
)
calixDs3FePmEsPlcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmEsPlcp.setStatus("current")
_CalixDs3FePmFcCpP_Type = PerfBinCount
_CalixDs3FePmFcCpP_Object = MibTableColumn
calixDs3FePmFcCpP = _CalixDs3FePmFcCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 8),
    _CalixDs3FePmFcCpP_Type()
)
calixDs3FePmFcCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmFcCpP.setStatus("current")
_CalixDs3FePmFcCpPe_Type = PerfBinCount
_CalixDs3FePmFcCpPe_Object = MibTableColumn
calixDs3FePmFcCpPe = _CalixDs3FePmFcCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 9),
    _CalixDs3FePmFcCpPe_Type()
)
calixDs3FePmFcCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmFcCpPe.setStatus("current")
_CalixDs3FePmSasCpP_Type = PerfBinCount
_CalixDs3FePmSasCpP_Object = MibTableColumn
calixDs3FePmSasCpP = _CalixDs3FePmSasCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 10),
    _CalixDs3FePmSasCpP_Type()
)
calixDs3FePmSasCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmSasCpP.setStatus("current")
_CalixDs3FePmSasCpPe_Type = PerfBinCount
_CalixDs3FePmSasCpPe_Object = MibTableColumn
calixDs3FePmSasCpPe = _CalixDs3FePmSasCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 11),
    _CalixDs3FePmSasCpPe_Type()
)
calixDs3FePmSasCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmSasCpPe.setStatus("current")
_CalixDs3FePmSesCpP_Type = PerfBinCount
_CalixDs3FePmSesCpP_Object = MibTableColumn
calixDs3FePmSesCpP = _CalixDs3FePmSesCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 12),
    _CalixDs3FePmSesCpP_Type()
)
calixDs3FePmSesCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmSesCpP.setStatus("current")
_CalixDs3FePmSesCpPe_Type = PerfBinCount
_CalixDs3FePmSesCpPe_Object = MibTableColumn
calixDs3FePmSesCpPe = _CalixDs3FePmSesCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 13),
    _CalixDs3FePmSesCpPe_Type()
)
calixDs3FePmSesCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmSesCpPe.setStatus("current")
_CalixDs3FePmUasCpP_Type = PerfBinCount
_CalixDs3FePmUasCpP_Object = MibTableColumn
calixDs3FePmUasCpP = _CalixDs3FePmUasCpP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 14),
    _CalixDs3FePmUasCpP_Type()
)
calixDs3FePmUasCpP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmUasCpP.setStatus("current")
_CalixDs3FePmUasCpPe_Type = PerfBinCount
_CalixDs3FePmUasCpPe_Object = MibTableColumn
calixDs3FePmUasCpPe = _CalixDs3FePmUasCpPe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 6, 1, 1, 15),
    _CalixDs3FePmUasCpPe_Type()
)
calixDs3FePmUasCpPe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3FePmUasCpPe.setStatus("current")
_CalixOcNePm_ObjectIdentity = ObjectIdentity
calixOcNePm = _CalixOcNePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7)
)
_CalixOcNePmTable_Object = MibTable
calixOcNePmTable = _CalixOcNePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    calixOcNePmTable.setStatus("current")
_CalixOcNePmEntry_Object = MibTableRow
calixOcNePmEntry = _CalixOcNePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1)
)
calixOcNePmEntry.setIndexNames(
    (0, "CALIX-PM-MIB", "calixIfIndex"),
    (0, "CALIX-PM-MIB", "calixOcPmBinNumber"),
)
if mibBuilder.loadTexts:
    calixOcNePmEntry.setStatus("current")
_CalixOcPmBinNumber_Type = PmBinNumber
_CalixOcPmBinNumber_Object = MibTableColumn
calixOcPmBinNumber = _CalixOcPmBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 1),
    _CalixOcPmBinNumber_Type()
)
calixOcPmBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcPmBinNumber.setStatus("current")
_CalixOcNePmTl1Aid_Type = Tl1Aid
_CalixOcNePmTl1Aid_Object = MibTableColumn
calixOcNePmTl1Aid = _CalixOcNePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 2),
    _CalixOcNePmTl1Aid_Type()
)
calixOcNePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmTl1Aid.setStatus("current")
_CalixOcNePmOcWidth_Type = OcWidth
_CalixOcNePmOcWidth_Object = MibTableColumn
calixOcNePmOcWidth = _CalixOcNePmOcWidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 3),
    _CalixOcNePmOcWidth_Type()
)
calixOcNePmOcWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmOcWidth.setStatus("current")
_CalixOcNePmValidity_Type = PmValidity
_CalixOcNePmValidity_Object = MibTableColumn
calixOcNePmValidity = _CalixOcNePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 4),
    _CalixOcNePmValidity_Type()
)
calixOcNePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmValidity.setStatus("current")
_CalixOcNePmCvL_Type = PerfBinCount
_CalixOcNePmCvL_Object = MibTableColumn
calixOcNePmCvL = _CalixOcNePmCvL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 5),
    _CalixOcNePmCvL_Type()
)
calixOcNePmCvL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmCvL.setStatus("current")
_CalixOcNePmCvS_Type = PerfBinCount
_CalixOcNePmCvS_Object = MibTableColumn
calixOcNePmCvS = _CalixOcNePmCvS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 6),
    _CalixOcNePmCvS_Type()
)
calixOcNePmCvS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmCvS.setStatus("current")
_CalixOcNePmEsL_Type = PerfBinCount
_CalixOcNePmEsL_Object = MibTableColumn
calixOcNePmEsL = _CalixOcNePmEsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 7),
    _CalixOcNePmEsL_Type()
)
calixOcNePmEsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmEsL.setStatus("current")
_CalixOcNePmEsS_Type = PerfBinCount
_CalixOcNePmEsS_Object = MibTableColumn
calixOcNePmEsS = _CalixOcNePmEsS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 8),
    _CalixOcNePmEsS_Type()
)
calixOcNePmEsS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmEsS.setStatus("current")
_CalixOcNePmFcL_Type = PerfBinCount
_CalixOcNePmFcL_Object = MibTableColumn
calixOcNePmFcL = _CalixOcNePmFcL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 9),
    _CalixOcNePmFcL_Type()
)
calixOcNePmFcL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmFcL.setStatus("current")
_CalixOcNePmPsc_Type = PerfBinCount
_CalixOcNePmPsc_Object = MibTableColumn
calixOcNePmPsc = _CalixOcNePmPsc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 10),
    _CalixOcNePmPsc_Type()
)
calixOcNePmPsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmPsc.setStatus("current")
_CalixOcNePmPsd_Type = PerfBinCount
_CalixOcNePmPsd_Object = MibTableColumn
calixOcNePmPsd = _CalixOcNePmPsd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 11),
    _CalixOcNePmPsd_Type()
)
calixOcNePmPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmPsd.setStatus("current")
_CalixOcNePmSefsS_Type = PerfBinCount
_CalixOcNePmSefsS_Object = MibTableColumn
calixOcNePmSefsS = _CalixOcNePmSefsS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 12),
    _CalixOcNePmSefsS_Type()
)
calixOcNePmSefsS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmSefsS.setStatus("current")
_CalixOcNePmSesL_Type = PerfBinCount
_CalixOcNePmSesL_Object = MibTableColumn
calixOcNePmSesL = _CalixOcNePmSesL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 13),
    _CalixOcNePmSesL_Type()
)
calixOcNePmSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmSesL.setStatus("current")
_CalixOcNePmSesS_Type = PerfBinCount
_CalixOcNePmSesS_Object = MibTableColumn
calixOcNePmSesS = _CalixOcNePmSesS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 14),
    _CalixOcNePmSesS_Type()
)
calixOcNePmSesS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmSesS.setStatus("current")
_CalixOcNePmUasL_Type = PerfBinCount
_CalixOcNePmUasL_Object = MibTableColumn
calixOcNePmUasL = _CalixOcNePmUasL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 7, 1, 1, 15),
    _CalixOcNePmUasL_Type()
)
calixOcNePmUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcNePmUasL.setStatus("current")
_CalixOcFePm_ObjectIdentity = ObjectIdentity
calixOcFePm = _CalixOcFePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8)
)
_CalixOcFePmTable_Object = MibTable
calixOcFePmTable = _CalixOcFePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    calixOcFePmTable.setStatus("current")
_CalixOcFePmEntry_Object = MibTableRow
calixOcFePmEntry = _CalixOcFePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    calixOcFePmEntry.setStatus("current")
_CalixOcFePmTl1Aid_Type = Tl1Aid
_CalixOcFePmTl1Aid_Object = MibTableColumn
calixOcFePmTl1Aid = _CalixOcFePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1, 1),
    _CalixOcFePmTl1Aid_Type()
)
calixOcFePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcFePmTl1Aid.setStatus("current")
_CalixOcFePmValidity_Type = PmValidity
_CalixOcFePmValidity_Object = MibTableColumn
calixOcFePmValidity = _CalixOcFePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1, 2),
    _CalixOcFePmValidity_Type()
)
calixOcFePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcFePmValidity.setStatus("current")
_CalixOcFePmCvL_Type = PerfBinCount
_CalixOcFePmCvL_Object = MibTableColumn
calixOcFePmCvL = _CalixOcFePmCvL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1, 3),
    _CalixOcFePmCvL_Type()
)
calixOcFePmCvL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcFePmCvL.setStatus("current")
_CalixOcFePmEsL_Type = PerfBinCount
_CalixOcFePmEsL_Object = MibTableColumn
calixOcFePmEsL = _CalixOcFePmEsL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1, 4),
    _CalixOcFePmEsL_Type()
)
calixOcFePmEsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcFePmEsL.setStatus("current")
_CalixOcFePmFcL_Type = PerfBinCount
_CalixOcFePmFcL_Object = MibTableColumn
calixOcFePmFcL = _CalixOcFePmFcL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1, 5),
    _CalixOcFePmFcL_Type()
)
calixOcFePmFcL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcFePmFcL.setStatus("current")
_CalixOcFePmSesL_Type = PerfBinCount
_CalixOcFePmSesL_Object = MibTableColumn
calixOcFePmSesL = _CalixOcFePmSesL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1, 6),
    _CalixOcFePmSesL_Type()
)
calixOcFePmSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcFePmSesL.setStatus("current")
_CalixOcFePmUasL_Type = PerfBinCount
_CalixOcFePmUasL_Object = MibTableColumn
calixOcFePmUasL = _CalixOcFePmUasL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 8, 1, 1, 7),
    _CalixOcFePmUasL_Type()
)
calixOcFePmUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcFePmUasL.setStatus("current")
_CalixStsNePm_ObjectIdentity = ObjectIdentity
calixStsNePm = _CalixStsNePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9)
)
_CalixStsNePmTable_Object = MibTable
calixStsNePmTable = _CalixStsNePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    calixStsNePmTable.setStatus("current")
_CalixStsNePmEntry_Object = MibTableRow
calixStsNePmEntry = _CalixStsNePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1)
)
calixStsNePmEntry.setIndexNames(
    (0, "CALIX-PM-MIB", "calixIfIndex"),
    (0, "CALIX-PM-MIB", "calixStsPmBinNumber"),
)
if mibBuilder.loadTexts:
    calixStsNePmEntry.setStatus("current")
_CalixStsPmBinNumber_Type = PmBinNumber
_CalixStsPmBinNumber_Object = MibTableColumn
calixStsPmBinNumber = _CalixStsPmBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 1),
    _CalixStsPmBinNumber_Type()
)
calixStsPmBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsPmBinNumber.setStatus("current")
_CalixStsNePmTl1Aid_Type = Tl1Aid
_CalixStsNePmTl1Aid_Object = MibTableColumn
calixStsNePmTl1Aid = _CalixStsNePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 2),
    _CalixStsNePmTl1Aid_Type()
)
calixStsNePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmTl1Aid.setStatus("current")
_CalixStsNePmStsWidth_Type = StsWidth
_CalixStsNePmStsWidth_Object = MibTableColumn
calixStsNePmStsWidth = _CalixStsNePmStsWidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 3),
    _CalixStsNePmStsWidth_Type()
)
calixStsNePmStsWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmStsWidth.setStatus("current")
_CalixStsNePmValidity_Type = PmValidity
_CalixStsNePmValidity_Object = MibTableColumn
calixStsNePmValidity = _CalixStsNePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 4),
    _CalixStsNePmValidity_Type()
)
calixStsNePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmValidity.setStatus("current")
_CalixStsNePmCvP_Type = PerfBinCount
_CalixStsNePmCvP_Object = MibTableColumn
calixStsNePmCvP = _CalixStsNePmCvP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 6),
    _CalixStsNePmCvP_Type()
)
calixStsNePmCvP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmCvP.setStatus("current")
_CalixStsNePmEsP_Type = PerfBinCount
_CalixStsNePmEsP_Object = MibTableColumn
calixStsNePmEsP = _CalixStsNePmEsP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 7),
    _CalixStsNePmEsP_Type()
)
calixStsNePmEsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmEsP.setStatus("current")
_CalixStsNePmFcP_Type = PerfBinCount
_CalixStsNePmFcP_Object = MibTableColumn
calixStsNePmFcP = _CalixStsNePmFcP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 8),
    _CalixStsNePmFcP_Type()
)
calixStsNePmFcP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmFcP.setStatus("current")
_CalixStsNePmSesP_Type = PerfBinCount
_CalixStsNePmSesP_Object = MibTableColumn
calixStsNePmSesP = _CalixStsNePmSesP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 9),
    _CalixStsNePmSesP_Type()
)
calixStsNePmSesP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmSesP.setStatus("current")
_CalixStsNePmUasP_Type = PerfBinCount
_CalixStsNePmUasP_Object = MibTableColumn
calixStsNePmUasP = _CalixStsNePmUasP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 9, 1, 1, 10),
    _CalixStsNePmUasP_Type()
)
calixStsNePmUasP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsNePmUasP.setStatus("current")
_CalixStsFePm_ObjectIdentity = ObjectIdentity
calixStsFePm = _CalixStsFePm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10)
)
_CalixStsFePmTable_Object = MibTable
calixStsFePmTable = _CalixStsFePmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11)
)
if mibBuilder.loadTexts:
    calixStsFePmTable.setStatus("current")
_CalixStsFePmEntry_Object = MibTableRow
calixStsFePmEntry = _CalixStsFePmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12)
)
if mibBuilder.loadTexts:
    calixStsFePmEntry.setStatus("current")
_CalixStsFePmTl1Aid_Type = Tl1Aid
_CalixStsFePmTl1Aid_Object = MibTableColumn
calixStsFePmTl1Aid = _CalixStsFePmTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12, 1),
    _CalixStsFePmTl1Aid_Type()
)
calixStsFePmTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsFePmTl1Aid.setStatus("current")
_CalixStsFePmValidity_Type = PmValidity
_CalixStsFePmValidity_Object = MibTableColumn
calixStsFePmValidity = _CalixStsFePmValidity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12, 2),
    _CalixStsFePmValidity_Type()
)
calixStsFePmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsFePmValidity.setStatus("current")
_CalixStsFePmCvP_Type = PerfBinCount
_CalixStsFePmCvP_Object = MibTableColumn
calixStsFePmCvP = _CalixStsFePmCvP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12, 3),
    _CalixStsFePmCvP_Type()
)
calixStsFePmCvP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsFePmCvP.setStatus("current")
_CalixStsFePmEsP_Type = PerfBinCount
_CalixStsFePmEsP_Object = MibTableColumn
calixStsFePmEsP = _CalixStsFePmEsP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12, 4),
    _CalixStsFePmEsP_Type()
)
calixStsFePmEsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsFePmEsP.setStatus("current")
_CalixStsFePmFcP_Type = PerfBinCount
_CalixStsFePmFcP_Object = MibTableColumn
calixStsFePmFcP = _CalixStsFePmFcP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12, 5),
    _CalixStsFePmFcP_Type()
)
calixStsFePmFcP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsFePmFcP.setStatus("current")
_CalixStsFePmSesP_Type = PerfBinCount
_CalixStsFePmSesP_Object = MibTableColumn
calixStsFePmSesP = _CalixStsFePmSesP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12, 6),
    _CalixStsFePmSesP_Type()
)
calixStsFePmSesP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsFePmSesP.setStatus("current")
_CalixStsFePmUasP_Type = PerfBinCount
_CalixStsFePmUasP_Object = MibTableColumn
calixStsFePmUasP = _CalixStsFePmUasP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 10, 11, 12, 7),
    _CalixStsFePmUasP_Type()
)
calixStsFePmUasP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsFePmUasP.setStatus("current")
calixAdslNePmEntry.registerAugmentions(
    ("CALIX-PM-MIB",
     "calixAdslFePmEntry")
)
calixAdslFePmEntry.setIndexNames(*calixAdslNePmEntry.getIndexNames())
calixDs1NePmEntry.registerAugmentions(
    ("CALIX-PM-MIB",
     "calixDs1FePmEntry")
)
calixDs1FePmEntry.setIndexNames(*calixDs1NePmEntry.getIndexNames())
calixDs3NePmEntry.registerAugmentions(
    ("CALIX-PM-MIB",
     "calixDs3FePmEntry")
)
calixDs3FePmEntry.setIndexNames(*calixDs3NePmEntry.getIndexNames())
calixOcNePmEntry.registerAugmentions(
    ("CALIX-PM-MIB",
     "calixOcFePmEntry")
)
calixOcFePmEntry.setIndexNames(*calixOcNePmEntry.getIndexNames())
calixStsNePmEntry.registerAugmentions(
    ("CALIX-PM-MIB",
     "calixStsFePmEntry")
)
calixStsFePmEntry.setIndexNames(*calixStsNePmEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-PM-MIB",
    **{"PerfBinCount": PerfBinCount,
       "PmBinNumber": PmBinNumber,
       "PmValidity": PmValidity,
       "calixPmMod": calixPmMod,
       "calixPmMIB": calixPmMIB,
       "calixAdslNePm": calixAdslNePm,
       "calixAdslNePmTable": calixAdslNePmTable,
       "calixAdslNePmEntry": calixAdslNePmEntry,
       "calixIfIndex": calixIfIndex,
       "calixAdslPmBinNumber": calixAdslPmBinNumber,
       "calixAdslNePmTl1Aid": calixAdslNePmTl1Aid,
       "calixAdslNePmValidity": calixAdslNePmValidity,
       "calixAdslNePmCvfL": calixAdslNePmCvfL,
       "calixAdslNePmCviL": calixAdslNePmCviL,
       "calixAdslNePmEcfL": calixAdslNePmEcfL,
       "calixAdslNePmEciL": calixAdslNePmEciL,
       "calixAdslNePmEcsL": calixAdslNePmEcsL,
       "calixAdslNePmEsL": calixAdslNePmEsL,
       "calixAdslNePmFr": calixAdslNePmFr,
       "calixAdslNePmFrf": calixAdslNePmFrf,
       "calixAdslNePmHecccfP": calixAdslNePmHecccfP,
       "calixAdslNePmHeccciP": calixAdslNePmHeccciP,
       "calixAdslNePmHeccvfP": calixAdslNePmHeccvfP,
       "calixAdslNePmHeccviP": calixAdslNePmHeccviP,
       "calixAdslNePmIngTcc0P": calixAdslNePmIngTcc0P,
       "calixAdslNePmIngTcc1P": calixAdslNePmIngTcc1P,
       "calixAdslNePmLossL": calixAdslNePmLossL,
       "calixAdslNePmSesL": calixAdslNePmSesL,
       "calixAdslNePmTcc0Pe": calixAdslNePmTcc0Pe,
       "calixAdslNePmTcc1Pe": calixAdslNePmTcc1Pe,
       "calixAdslNePmUasL": calixAdslNePmUasL,
       "calixAdslFePm": calixAdslFePm,
       "calixAdslFePmTable": calixAdslFePmTable,
       "calixAdslFePmEntry": calixAdslFePmEntry,
       "calixAdslFePmTl1Aid": calixAdslFePmTl1Aid,
       "calixAdslFePmValidity": calixAdslFePmValidity,
       "calixAdslFePmCvfL": calixAdslFePmCvfL,
       "calixAdslFePmCviL": calixAdslFePmCviL,
       "calixAdslFePmEcfL": calixAdslFePmEcfL,
       "calixAdslFePmEciL": calixAdslFePmEciL,
       "calixAdslFePmEcsL": calixAdslFePmEcsL,
       "calixAdslFePmEsL": calixAdslFePmEsL,
       "calixAdslFePmSesL": calixAdslFePmSesL,
       "calixAdslFePmUasL": calixAdslFePmUasL,
       "calixDs1NePm": calixDs1NePm,
       "calixDs1NePmTable": calixDs1NePmTable,
       "calixDs1NePmEntry": calixDs1NePmEntry,
       "calixDs1PmBinNumber": calixDs1PmBinNumber,
       "calixDs1NePmTl1Aid": calixDs1NePmTl1Aid,
       "calixDs1NePmValidity": calixDs1NePmValidity,
       "calixDs1NePmCssP": calixDs1NePmCssP,
       "calixDs1NePmCvL": calixDs1NePmCvL,
       "calixDs1NePmCvP": calixDs1NePmCvP,
       "calixDs1NePmEsL": calixDs1NePmEsL,
       "calixDs1NePmEsP": calixDs1NePmEsP,
       "calixDs1NePmFcP": calixDs1NePmFcP,
       "calixDs1NePmLossL": calixDs1NePmLossL,
       "calixDs1NePmSasP": calixDs1NePmSasP,
       "calixDs1NePmSesL": calixDs1NePmSesL,
       "calixDs1NePmSesP": calixDs1NePmSesP,
       "calixDs1NePmUasP": calixDs1NePmUasP,
       "calixDs1FePm": calixDs1FePm,
       "calixDs1FePmTable": calixDs1FePmTable,
       "calixDs1FePmEntry": calixDs1FePmEntry,
       "calixDs1FePmTl1Aid": calixDs1FePmTl1Aid,
       "calixDs1FePmValidity": calixDs1FePmValidity,
       "calixDs1FePmCssP": calixDs1FePmCssP,
       "calixDs1FePmCvP": calixDs1FePmCvP,
       "calixDs1FePmEsL": calixDs1FePmEsL,
       "calixDs1FePmEsP": calixDs1FePmEsP,
       "calixDs1FePmFcP": calixDs1FePmFcP,
       "calixDs1FePmSefsP": calixDs1FePmSefsP,
       "calixDs1FePmSesP": calixDs1FePmSesP,
       "calixDs1FePmUasP": calixDs1FePmUasP,
       "calixDs3NePm": calixDs3NePm,
       "calixDs3NePmTable": calixDs3NePmTable,
       "calixDs3NePmEntry": calixDs3NePmEntry,
       "calixDs3PmBinNumber": calixDs3PmBinNumber,
       "calixDs3NePmTl1Aid": calixDs3NePmTl1Aid,
       "calixDs3NePmValidity": calixDs3NePmValidity,
       "calixDs3NePmAissP": calixDs3NePmAissP,
       "calixDs3NePmAissPe": calixDs3NePmAissPe,
       "calixDs3NePmCvCpP": calixDs3NePmCvCpP,
       "calixDs3NePmCvCpPe": calixDs3NePmCvCpPe,
       "calixDs3NePmCvL": calixDs3NePmCvL,
       "calixDs3NePmCvpP": calixDs3NePmCvpP,
       "calixDs3NePmCvpPe": calixDs3NePmCvpPe,
       "calixDs3NePmDscc": calixDs3NePmDscc,
       "calixDs3NePmDscce": calixDs3NePmDscce,
       "calixDs3NePmEsCpP": calixDs3NePmEsCpP,
       "calixDs3NePmEsCpPe": calixDs3NePmEsCpPe,
       "calixDs3NePmEsL": calixDs3NePmEsL,
       "calixDs3NePmEspP": calixDs3NePmEspP,
       "calixDs3NePmEspPe": calixDs3NePmEspPe,
       "calixDs3NePmEsPlcp": calixDs3NePmEsPlcp,
       "calixDs3NePmFcP": calixDs3NePmFcP,
       "calixDs3NePmFcPe": calixDs3NePmFcPe,
       "calixDs3NePmHecc": calixDs3NePmHecc,
       "calixDs3NePmHecce": calixDs3NePmHecce,
       "calixDs3NePmHecuc": calixDs3NePmHecuc,
       "calixDs3NePmHecuce": calixDs3NePmHecuce,
       "calixDs3NePmLcds": calixDs3NePmLcds,
       "calixDs3NePmLcdse": calixDs3NePmLcdse,
       "calixDs3NePmLossL": calixDs3NePmLossL,
       "calixDs3NePmSasP": calixDs3NePmSasP,
       "calixDs3NePmSasPe": calixDs3NePmSasPe,
       "calixDs3NePmSesCpP": calixDs3NePmSesCpP,
       "calixDs3NePmSesCpPe": calixDs3NePmSesCpPe,
       "calixDs3NePmSesL": calixDs3NePmSesL,
       "calixDs3NePmSespP": calixDs3NePmSespP,
       "calixDs3NePmSespPe": calixDs3NePmSespPe,
       "calixDs3NePmUasCpP": calixDs3NePmUasCpP,
       "calixDs3NePmUasCpPe": calixDs3NePmUasCpPe,
       "calixDs3NePmUaspP": calixDs3NePmUaspP,
       "calixDs3NePmUaspPe": calixDs3NePmUaspPe,
       "calixDs3NePmUtcc": calixDs3NePmUtcc,
       "calixDs3NePmUtcce": calixDs3NePmUtcce,
       "calixDs3FePm": calixDs3FePm,
       "calixDs3FePmTable": calixDs3FePmTable,
       "calixDs3FePmEntry": calixDs3FePmEntry,
       "calixDs3FePmTl1Aid": calixDs3FePmTl1Aid,
       "calixDs3FePmValidity": calixDs3FePmValidity,
       "calixDs3FePmCvCpP": calixDs3FePmCvCpP,
       "calixDs3FePmCvCpPe": calixDs3FePmCvCpPe,
       "calixDs3FePmEsCpP": calixDs3FePmEsCpP,
       "calixDs3FePmEsCpPe": calixDs3FePmEsCpPe,
       "calixDs3FePmEsPlcp": calixDs3FePmEsPlcp,
       "calixDs3FePmFcCpP": calixDs3FePmFcCpP,
       "calixDs3FePmFcCpPe": calixDs3FePmFcCpPe,
       "calixDs3FePmSasCpP": calixDs3FePmSasCpP,
       "calixDs3FePmSasCpPe": calixDs3FePmSasCpPe,
       "calixDs3FePmSesCpP": calixDs3FePmSesCpP,
       "calixDs3FePmSesCpPe": calixDs3FePmSesCpPe,
       "calixDs3FePmUasCpP": calixDs3FePmUasCpP,
       "calixDs3FePmUasCpPe": calixDs3FePmUasCpPe,
       "calixOcNePm": calixOcNePm,
       "calixOcNePmTable": calixOcNePmTable,
       "calixOcNePmEntry": calixOcNePmEntry,
       "calixOcPmBinNumber": calixOcPmBinNumber,
       "calixOcNePmTl1Aid": calixOcNePmTl1Aid,
       "calixOcNePmOcWidth": calixOcNePmOcWidth,
       "calixOcNePmValidity": calixOcNePmValidity,
       "calixOcNePmCvL": calixOcNePmCvL,
       "calixOcNePmCvS": calixOcNePmCvS,
       "calixOcNePmEsL": calixOcNePmEsL,
       "calixOcNePmEsS": calixOcNePmEsS,
       "calixOcNePmFcL": calixOcNePmFcL,
       "calixOcNePmPsc": calixOcNePmPsc,
       "calixOcNePmPsd": calixOcNePmPsd,
       "calixOcNePmSefsS": calixOcNePmSefsS,
       "calixOcNePmSesL": calixOcNePmSesL,
       "calixOcNePmSesS": calixOcNePmSesS,
       "calixOcNePmUasL": calixOcNePmUasL,
       "calixOcFePm": calixOcFePm,
       "calixOcFePmTable": calixOcFePmTable,
       "calixOcFePmEntry": calixOcFePmEntry,
       "calixOcFePmTl1Aid": calixOcFePmTl1Aid,
       "calixOcFePmValidity": calixOcFePmValidity,
       "calixOcFePmCvL": calixOcFePmCvL,
       "calixOcFePmEsL": calixOcFePmEsL,
       "calixOcFePmFcL": calixOcFePmFcL,
       "calixOcFePmSesL": calixOcFePmSesL,
       "calixOcFePmUasL": calixOcFePmUasL,
       "calixStsNePm": calixStsNePm,
       "calixStsNePmTable": calixStsNePmTable,
       "calixStsNePmEntry": calixStsNePmEntry,
       "calixStsPmBinNumber": calixStsPmBinNumber,
       "calixStsNePmTl1Aid": calixStsNePmTl1Aid,
       "calixStsNePmStsWidth": calixStsNePmStsWidth,
       "calixStsNePmValidity": calixStsNePmValidity,
       "calixStsNePmCvP": calixStsNePmCvP,
       "calixStsNePmEsP": calixStsNePmEsP,
       "calixStsNePmFcP": calixStsNePmFcP,
       "calixStsNePmSesP": calixStsNePmSesP,
       "calixStsNePmUasP": calixStsNePmUasP,
       "calixStsFePm": calixStsFePm,
       "calixStsFePmTable": calixStsFePmTable,
       "calixStsFePmEntry": calixStsFePmEntry,
       "calixStsFePmTl1Aid": calixStsFePmTl1Aid,
       "calixStsFePmValidity": calixStsFePmValidity,
       "calixStsFePmCvP": calixStsFePmCvP,
       "calixStsFePmEsP": calixStsFePmEsP,
       "calixStsFePmFcP": calixStsFePmFcP,
       "calixStsFePmSesP": calixStsFePmSesP,
       "calixStsFePmUasP": calixStsFePmUasP}
)
