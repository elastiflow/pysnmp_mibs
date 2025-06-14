# SNMP MIB module (CISCO-DMN-DSG-PRGMENTRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DMN-DSG-PRGMENTRY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:04:33 2025
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGProgramEntry = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    ciscoDSGProgramEntry.setRevisions(
        ("2010-10-13 08:00",
         "2010-08-30 11:00",
         "2010-06-17 06:00",
         "2010-05-25 16:30",
         "2010-05-07 06:30",
         "2010-03-22 05:00",
         "2010-02-12 15:00",
         "2009-11-22 15:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProgramEntryTable_ObjectIdentity = ObjectIdentity
programEntryTable = _ProgramEntryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2)
)
_ProgramEntryControlTable_Object = MibTable
programEntryControlTable = _ProgramEntryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    programEntryControlTable.setStatus("current")
_ProgramEntryControlEntry_Object = MibTableRow
programEntryControlEntry = _ProgramEntryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1)
)
programEntryControlEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryControlIndex"),
)
if mibBuilder.loadTexts:
    programEntryControlEntry.setStatus("current")


class _ProgramEntryControlIndex_Type(Integer32):
    """Custom type programEntryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ProgramEntryControlIndex_Type.__name__ = "Integer32"
_ProgramEntryControlIndex_Object = MibTableColumn
programEntryControlIndex = _ProgramEntryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 1),
    _ProgramEntryControlIndex_Type()
)
programEntryControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    programEntryControlIndex.setStatus("current")


class _ProgramEntryControlChNum_Type(Integer32):
    """Custom type programEntryControlChNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ProgramEntryControlChNum_Type.__name__ = "Integer32"
_ProgramEntryControlChNum_Object = MibTableColumn
programEntryControlChNum = _ProgramEntryControlChNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 2),
    _ProgramEntryControlChNum_Type()
)
programEntryControlChNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    programEntryControlChNum.setStatus("current")


class _ProgramEntryControlChCmd_Type(Integer32):
    """Custom type programEntryControlChCmd based on Integer32"""
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
        *(("switch", 1),
          ("up", 2),
          ("down", 3),
          ("last", 4),
          ("writeOnly", 5))
    )


_ProgramEntryControlChCmd_Type.__name__ = "Integer32"
_ProgramEntryControlChCmd_Object = MibTableColumn
programEntryControlChCmd = _ProgramEntryControlChCmd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 4),
    _ProgramEntryControlChCmd_Type()
)
programEntryControlChCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    programEntryControlChCmd.setStatus("current")


class _ProgramEntryControlResourceId_Type(Unsigned32):
    """Custom type programEntryControlResourceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ProgramEntryControlResourceId_Type.__name__ = "Unsigned32"
_ProgramEntryControlResourceId_Object = MibTableColumn
programEntryControlResourceId = _ProgramEntryControlResourceId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 5),
    _ProgramEntryControlResourceId_Type()
)
programEntryControlResourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    programEntryControlResourceId.setStatus("current")
_ProgramEntryStatusTable_Object = MibTable
programEntryStatusTable = _ProgramEntryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2)
)
if mibBuilder.loadTexts:
    programEntryStatusTable.setStatus("current")
_ProgramEntryStatusEntry_Object = MibTableRow
programEntryStatusEntry = _ProgramEntryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1)
)
programEntryStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryStatusIndex"),
)
if mibBuilder.loadTexts:
    programEntryStatusEntry.setStatus("current")


class _ProgramEntryStatusIndex_Type(Integer32):
    """Custom type programEntryStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ProgramEntryStatusIndex_Type.__name__ = "Integer32"
_ProgramEntryStatusIndex_Object = MibTableColumn
programEntryStatusIndex = _ProgramEntryStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 1),
    _ProgramEntryStatusIndex_Type()
)
programEntryStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    programEntryStatusIndex.setStatus("current")


class _ProgramEntryStatusChName_Type(DisplayString):
    """Custom type programEntryStatusChName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ProgramEntryStatusChName_Type.__name__ = "DisplayString"
_ProgramEntryStatusChName_Object = MibTableColumn
programEntryStatusChName = _ProgramEntryStatusChName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 2),
    _ProgramEntryStatusChName_Type()
)
programEntryStatusChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusChName.setStatus("current")


class _ProgramEntryStatusCAAuth_Type(Integer32):
    """Custom type programEntryStatusCAAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ProgramEntryStatusCAAuth_Type.__name__ = "Integer32"
_ProgramEntryStatusCAAuth_Object = MibTableColumn
programEntryStatusCAAuth = _ProgramEntryStatusCAAuth_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 3),
    _ProgramEntryStatusCAAuth_Type()
)
programEntryStatusCAAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusCAAuth.setStatus("current")


class _ProgramEntryStatusCAEncry_Type(Integer32):
    """Custom type programEntryStatusCAEncry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2),
          ("unkn", 3))
    )


_ProgramEntryStatusCAEncry_Type.__name__ = "Integer32"
_ProgramEntryStatusCAEncry_Object = MibTableColumn
programEntryStatusCAEncry = _ProgramEntryStatusCAEncry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 4),
    _ProgramEntryStatusCAEncry_Type()
)
programEntryStatusCAEncry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusCAEncry.setStatus("current")


class _ProgramEntryStatusCAScram_Type(Integer32):
    """Custom type programEntryStatusCAScram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ProgramEntryStatusCAScram_Type.__name__ = "Integer32"
_ProgramEntryStatusCAScram_Object = MibTableColumn
programEntryStatusCAScram = _ProgramEntryStatusCAScram_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 5),
    _ProgramEntryStatusCAScram_Type()
)
programEntryStatusCAScram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusCAScram.setStatus("current")


class _ProgramEntryStatusCAID_Type(Integer32):
    """Custom type programEntryStatusCAID based on Integer32"""
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
              63)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fta", 2),
          ("powervu", 3),
          ("biss1", 4),
          ("biss2", 5),
          ("biss3", 6),
          ("standardized", 7),
          ("canalplus", 8),
          ("ccett", 9),
          ("deutscheTel", 10),
          ("eurodec", 11),
          ("franceTel", 12),
          ("iredeto", 13),
          ("jerroldGi", 14),
          ("matraComm", 15),
          ("nds", 16),
          ("nokia", 17),
          ("norwegianTel", 18),
          ("ntl", 19),
          ("philips", 20),
          ("sony", 21),
          ("tandbergTv", 22),
          ("thomson", 23),
          ("tvCom", 24),
          ("hptCroatian", 25),
          ("hrtCroatian", 26),
          ("ibm", 27),
          ("nera", 28),
          ("betaTechnik", 29),
          ("kudelski", 30),
          ("titanIS", 31),
          ("telefonica", 32),
          ("stentor", 33),
          ("tadiranScopus", 34),
          ("barco", 35),
          ("starguideDN", 36),
          ("mentorDS", 37),
          ("european", 38),
          ("polycipher", 39),
          ("generalIns", 40),
          ("telemann", 41),
          ("cryptoworks", 42),
          ("tsinghua", 43),
          ("easycas", 44),
          ("alphacrypt", 45),
          ("dvnHoldings", 46),
          ("shanghaiADT", 47),
          ("shenzhenKing", 48),
          ("sky", 49),
          ("dreamcrypt", 50),
          ("thalescrypt", 51),
          ("runcom", 52),
          ("sidsa", 53),
          ("beijingCom", 54),
          ("latens", 55),
          ("xcrypt", 56),
          ("beijingDig", 57),
          ("widevineTec", 58),
          ("skTel", 59),
          ("enigmaSys", 60),
          ("reserved", 61),
          ("ruscrypt", 62),
          ("other", 63))
    )


_ProgramEntryStatusCAID_Type.__name__ = "Integer32"
_ProgramEntryStatusCAID_Object = MibTableColumn
programEntryStatusCAID = _ProgramEntryStatusCAID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 6),
    _ProgramEntryStatusCAID_Type()
)
programEntryStatusCAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusCAID.setStatus("current")


class _ProgramEntryStatusSRStatus_Type(Integer32):
    """Custom type programEntryStatusSRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("primary", 2),
          ("alternate", 3))
    )


_ProgramEntryStatusSRStatus_Type.__name__ = "Integer32"
_ProgramEntryStatusSRStatus_Object = MibTableColumn
programEntryStatusSRStatus = _ProgramEntryStatusSRStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 7),
    _ProgramEntryStatusSRStatus_Type()
)
programEntryStatusSRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusSRStatus.setStatus("current")


class _ProgramEntryStatusSRType_Type(Integer32):
    """Custom type programEntryStatusSRType based on Integer32"""
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
        *(("none", 1),
          ("scheduled", 2),
          ("ca", 3),
          ("cuetrigger", 4))
    )


_ProgramEntryStatusSRType_Type.__name__ = "Integer32"
_ProgramEntryStatusSRType_Object = MibTableColumn
programEntryStatusSRType = _ProgramEntryStatusSRType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 8),
    _ProgramEntryStatusSRType_Type()
)
programEntryStatusSRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusSRType.setStatus("current")


class _ProgramEntryStatusSRStartTime_Type(DisplayString):
    """Custom type programEntryStatusSRStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProgramEntryStatusSRStartTime_Type.__name__ = "DisplayString"
_ProgramEntryStatusSRStartTime_Object = MibTableColumn
programEntryStatusSRStartTime = _ProgramEntryStatusSRStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 9),
    _ProgramEntryStatusSRStartTime_Type()
)
programEntryStatusSRStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusSRStartTime.setStatus("current")


class _ProgramEntryStatusSREndTime_Type(DisplayString):
    """Custom type programEntryStatusSREndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProgramEntryStatusSREndTime_Type.__name__ = "DisplayString"
_ProgramEntryStatusSREndTime_Object = MibTableColumn
programEntryStatusSREndTime = _ProgramEntryStatusSREndTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 10),
    _ProgramEntryStatusSREndTime_Type()
)
programEntryStatusSREndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusSREndTime.setStatus("current")


class _ProgramEntryStatusPRGMStatus_Type(Integer32):
    """Custom type programEntryStatusPRGMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_ProgramEntryStatusPRGMStatus_Type.__name__ = "Integer32"
_ProgramEntryStatusPRGMStatus_Object = MibTableColumn
programEntryStatusPRGMStatus = _ProgramEntryStatusPRGMStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 11),
    _ProgramEntryStatusPRGMStatus_Type()
)
programEntryStatusPRGMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusPRGMStatus.setStatus("current")


class _ProgramEntryStatusPMTPID_Type(DisplayString):
    """Custom type programEntryStatusPMTPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProgramEntryStatusPMTPID_Type.__name__ = "DisplayString"
_ProgramEntryStatusPMTPID_Object = MibTableColumn
programEntryStatusPMTPID = _ProgramEntryStatusPMTPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 12),
    _ProgramEntryStatusPMTPID_Type()
)
programEntryStatusPMTPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusPMTPID.setStatus("current")


class _ProgramEntryStatusPCRPID_Type(DisplayString):
    """Custom type programEntryStatusPCRPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProgramEntryStatusPCRPID_Type.__name__ = "DisplayString"
_ProgramEntryStatusPCRPID_Object = MibTableColumn
programEntryStatusPCRPID = _ProgramEntryStatusPCRPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 13),
    _ProgramEntryStatusPCRPID_Type()
)
programEntryStatusPCRPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryStatusPCRPID.setStatus("current")
_ProgramEntryPIDTable_Object = MibTable
programEntryPIDTable = _ProgramEntryPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    programEntryPIDTable.setStatus("current")
_ProgramEntryPIDEntry_Object = MibTableRow
programEntryPIDEntry = _ProgramEntryPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1)
)
programEntryPIDEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryPIDPEIndex"),
    (0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryPIDIndex"),
)
if mibBuilder.loadTexts:
    programEntryPIDEntry.setStatus("current")


class _ProgramEntryPIDPEIndex_Type(Integer32):
    """Custom type programEntryPIDPEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 138),
    )


_ProgramEntryPIDPEIndex_Type.__name__ = "Integer32"
_ProgramEntryPIDPEIndex_Object = MibTableColumn
programEntryPIDPEIndex = _ProgramEntryPIDPEIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 1),
    _ProgramEntryPIDPEIndex_Type()
)
programEntryPIDPEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    programEntryPIDPEIndex.setStatus("current")


class _ProgramEntryPIDIndex_Type(Integer32):
    """Custom type programEntryPIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 138),
    )


_ProgramEntryPIDIndex_Type.__name__ = "Integer32"
_ProgramEntryPIDIndex_Object = MibTableColumn
programEntryPIDIndex = _ProgramEntryPIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 2),
    _ProgramEntryPIDIndex_Type()
)
programEntryPIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    programEntryPIDIndex.setStatus("current")


class _ProgramEntryPIDTypeName_Type(DisplayString):
    """Custom type programEntryPIDTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProgramEntryPIDTypeName_Type.__name__ = "DisplayString"
_ProgramEntryPIDTypeName_Object = MibTableColumn
programEntryPIDTypeName = _ProgramEntryPIDTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 3),
    _ProgramEntryPIDTypeName_Type()
)
programEntryPIDTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryPIDTypeName.setStatus("current")


class _ProgramEntryPIDTypeDetail_Type(Integer32):
    """Custom type programEntryPIDTypeDetail based on Integer32"""
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
              42)
        )
    )
    namedValues = NamedValues(
        *(("pcr", 1),
          ("mpg1Vid", 2),
          ("mpg2Vid", 3),
          ("hdVid", 4),
          ("mpg4Vid", 5),
          ("iso422Vid", 6),
          ("h264Vid", 7),
          ("mpgAudL1", 8),
          ("mpg2AudL1", 9),
          ("mpgAudL2", 10),
          ("mpg2AudL2", 11),
          ("mpg4Aud", 12),
          ("dvbDolbyDigital", 13),
          ("dvbDolbyDigitalPlus", 14),
          ("atscDolbyDigital", 15),
          ("atscDolbyDigitalPlus", 16),
          ("aacLsAud", 17),
          ("haacLoAud", 18),
          ("haacAdAud", 19),
          ("dbeAud", 20),
          ("dtsAud", 21),
          ("dvbSubt", 22),
          ("saSubt", 23),
          ("dvbVbi", 24),
          ("saVbi", 25),
          ("dvbTtx", 26),
          ("scteDpi", 27),
          ("dvbMpe", 28),
          ("dvbAsyn", 29),
          ("dvbSyns", 30),
          ("dvbSynd", 31),
          ("dvbDcar", 32),
          ("dvbOcar", 33),
          ("saUtld", 34),
          ("saHsd", 35),
          ("saWbd", 36),
          ("saCddl", 37),
          ("ecm", 38),
          ("emm", 39),
          ("pmt", 40),
          ("unknown", 41),
          ("reserved", 42))
    )


_ProgramEntryPIDTypeDetail_Type.__name__ = "Integer32"
_ProgramEntryPIDTypeDetail_Object = MibTableColumn
programEntryPIDTypeDetail = _ProgramEntryPIDTypeDetail_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 4),
    _ProgramEntryPIDTypeDetail_Type()
)
programEntryPIDTypeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryPIDTypeDetail.setStatus("current")


class _ProgramEntryPIDValue_Type(DisplayString):
    """Custom type programEntryPIDValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProgramEntryPIDValue_Type.__name__ = "DisplayString"
_ProgramEntryPIDValue_Object = MibTableColumn
programEntryPIDValue = _ProgramEntryPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 5),
    _ProgramEntryPIDValue_Type()
)
programEntryPIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryPIDValue.setStatus("current")


class _ProgramEntryPIDPresent_Type(Integer32):
    """Custom type programEntryPIDPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ProgramEntryPIDPresent_Type.__name__ = "Integer32"
_ProgramEntryPIDPresent_Object = MibTableColumn
programEntryPIDPresent = _ProgramEntryPIDPresent_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 6),
    _ProgramEntryPIDPresent_Type()
)
programEntryPIDPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programEntryPIDPresent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-PRGMENTRY-MIB",
    **{"ciscoDSGProgramEntry": ciscoDSGProgramEntry,
       "programEntryTable": programEntryTable,
       "programEntryControlTable": programEntryControlTable,
       "programEntryControlEntry": programEntryControlEntry,
       "programEntryControlIndex": programEntryControlIndex,
       "programEntryControlChNum": programEntryControlChNum,
       "programEntryControlChCmd": programEntryControlChCmd,
       "programEntryControlResourceId": programEntryControlResourceId,
       "programEntryStatusTable": programEntryStatusTable,
       "programEntryStatusEntry": programEntryStatusEntry,
       "programEntryStatusIndex": programEntryStatusIndex,
       "programEntryStatusChName": programEntryStatusChName,
       "programEntryStatusCAAuth": programEntryStatusCAAuth,
       "programEntryStatusCAEncry": programEntryStatusCAEncry,
       "programEntryStatusCAScram": programEntryStatusCAScram,
       "programEntryStatusCAID": programEntryStatusCAID,
       "programEntryStatusSRStatus": programEntryStatusSRStatus,
       "programEntryStatusSRType": programEntryStatusSRType,
       "programEntryStatusSRStartTime": programEntryStatusSRStartTime,
       "programEntryStatusSREndTime": programEntryStatusSREndTime,
       "programEntryStatusPRGMStatus": programEntryStatusPRGMStatus,
       "programEntryStatusPMTPID": programEntryStatusPMTPID,
       "programEntryStatusPCRPID": programEntryStatusPCRPID,
       "programEntryPIDTable": programEntryPIDTable,
       "programEntryPIDEntry": programEntryPIDEntry,
       "programEntryPIDPEIndex": programEntryPIDPEIndex,
       "programEntryPIDIndex": programEntryPIDIndex,
       "programEntryPIDTypeName": programEntryPIDTypeName,
       "programEntryPIDTypeDetail": programEntryPIDTypeDetail,
       "programEntryPIDValue": programEntryPIDValue,
       "programEntryPIDPresent": programEntryPIDPresent}
)
