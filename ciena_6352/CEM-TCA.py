# SNMP MIB module (CEM-TCA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-TCA.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cnTcaModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 17)
)
if mibBuilder.loadTexts:
    cnTcaModule.setRevisions(
        ("2002-02-21 13:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnTcaProfileType(TextualConvention, Integer32):
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
        *(("cnTcaProfile1", 1),
          ("cnTcaProfile2", 2),
          ("cnTcaProfile3", 3),
          ("cnTcaProfile4", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CnTca15MinOc3ProfileTable_Object = MibTable
cnTca15MinOc3ProfileTable = _CnTca15MinOc3ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1)
)
if mibBuilder.loadTexts:
    cnTca15MinOc3ProfileTable.setStatus("current")
_CnTca15MinOc3ProfileEntry_Object = MibTableRow
cnTca15MinOc3ProfileEntry = _CnTca15MinOc3ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1)
)
cnTca15MinOc3ProfileEntry.setIndexNames(
    (0, "CEM-TCA", "cnTca15MinOc3Profile"),
)
if mibBuilder.loadTexts:
    cnTca15MinOc3ProfileEntry.setStatus("current")
_CnTca15MinOc3Profile_Type = CnTcaProfileType
_CnTca15MinOc3Profile_Object = MibTableColumn
cnTca15MinOc3Profile = _CnTca15MinOc3Profile_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 1),
    _CnTca15MinOc3Profile_Type()
)
cnTca15MinOc3Profile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTca15MinOc3Profile.setStatus("current")
_CnTca15MinOc3CVs_Type = Integer32
_CnTca15MinOc3CVs_Object = MibTableColumn
cnTca15MinOc3CVs = _CnTca15MinOc3CVs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 2),
    _CnTca15MinOc3CVs_Type()
)
cnTca15MinOc3CVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinOc3CVs.setStatus("current")
_CnTca15MinOc3PESs_Type = Integer32
_CnTca15MinOc3PESs_Object = MibTableColumn
cnTca15MinOc3PESs = _CnTca15MinOc3PESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 3),
    _CnTca15MinOc3PESs_Type()
)
cnTca15MinOc3PESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinOc3PESs.setStatus("current")
_CnTca15MinOc3PSESs_Type = Integer32
_CnTca15MinOc3PSESs_Object = MibTableColumn
cnTca15MinOc3PSESs = _CnTca15MinOc3PSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 4),
    _CnTca15MinOc3PSESs_Type()
)
cnTca15MinOc3PSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinOc3PSESs.setStatus("current")
_CnTca15MinOc3LUASs_Type = Integer32
_CnTca15MinOc3LUASs_Object = MibTableColumn
cnTca15MinOc3LUASs = _CnTca15MinOc3LUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 5),
    _CnTca15MinOc3LUASs_Type()
)
cnTca15MinOc3LUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinOc3LUASs.setStatus("current")
_CnTca15MinOc3PUASs_Type = Integer32
_CnTca15MinOc3PUASs_Object = MibTableColumn
cnTca15MinOc3PUASs = _CnTca15MinOc3PUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 6),
    _CnTca15MinOc3PUASs_Type()
)
cnTca15MinOc3PUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinOc3PUASs.setStatus("current")


class _CnTca15MinOc3ProfileName_Type(OctetString):
    """Custom type cnTca15MinOc3ProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnTca15MinOc3ProfileName_Type.__name__ = "OctetString"
_CnTca15MinOc3ProfileName_Object = MibTableColumn
cnTca15MinOc3ProfileName = _CnTca15MinOc3ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 7),
    _CnTca15MinOc3ProfileName_Type()
)
cnTca15MinOc3ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinOc3ProfileName.setStatus("current")
_CnTca15MinOc3RowStatus_Type = RowStatus
_CnTca15MinOc3RowStatus_Object = MibTableColumn
cnTca15MinOc3RowStatus = _CnTca15MinOc3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 1, 1, 8),
    _CnTca15MinOc3RowStatus_Type()
)
cnTca15MinOc3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinOc3RowStatus.setStatus("current")
_CnTca24HrOc3ProfileTable_Object = MibTable
cnTca24HrOc3ProfileTable = _CnTca24HrOc3ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2)
)
if mibBuilder.loadTexts:
    cnTca24HrOc3ProfileTable.setStatus("current")
_CnTca24HrOc3ProfileEntry_Object = MibTableRow
cnTca24HrOc3ProfileEntry = _CnTca24HrOc3ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1)
)
cnTca24HrOc3ProfileEntry.setIndexNames(
    (0, "CEM-TCA", "cnTca24HrOc3Profile"),
)
if mibBuilder.loadTexts:
    cnTca24HrOc3ProfileEntry.setStatus("current")
_CnTca24HrOc3Profile_Type = CnTcaProfileType
_CnTca24HrOc3Profile_Object = MibTableColumn
cnTca24HrOc3Profile = _CnTca24HrOc3Profile_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 1),
    _CnTca24HrOc3Profile_Type()
)
cnTca24HrOc3Profile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTca24HrOc3Profile.setStatus("current")
_CnTca24HrOc3CVs_Type = Integer32
_CnTca24HrOc3CVs_Object = MibTableColumn
cnTca24HrOc3CVs = _CnTca24HrOc3CVs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 2),
    _CnTca24HrOc3CVs_Type()
)
cnTca24HrOc3CVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrOc3CVs.setStatus("current")
_CnTca24HrOc3PESs_Type = Integer32
_CnTca24HrOc3PESs_Object = MibTableColumn
cnTca24HrOc3PESs = _CnTca24HrOc3PESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 3),
    _CnTca24HrOc3PESs_Type()
)
cnTca24HrOc3PESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrOc3PESs.setStatus("current")
_CnTca24HrOc3PSESs_Type = Integer32
_CnTca24HrOc3PSESs_Object = MibTableColumn
cnTca24HrOc3PSESs = _CnTca24HrOc3PSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 4),
    _CnTca24HrOc3PSESs_Type()
)
cnTca24HrOc3PSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrOc3PSESs.setStatus("current")
_CnTca24HrOc3LUASs_Type = Integer32
_CnTca24HrOc3LUASs_Object = MibTableColumn
cnTca24HrOc3LUASs = _CnTca24HrOc3LUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 5),
    _CnTca24HrOc3LUASs_Type()
)
cnTca24HrOc3LUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrOc3LUASs.setStatus("current")
_CnTca24HrOc3PUASs_Type = Integer32
_CnTca24HrOc3PUASs_Object = MibTableColumn
cnTca24HrOc3PUASs = _CnTca24HrOc3PUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 6),
    _CnTca24HrOc3PUASs_Type()
)
cnTca24HrOc3PUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrOc3PUASs.setStatus("current")


class _CnTca24HrOc3ProfileName_Type(OctetString):
    """Custom type cnTca24HrOc3ProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnTca24HrOc3ProfileName_Type.__name__ = "OctetString"
_CnTca24HrOc3ProfileName_Object = MibTableColumn
cnTca24HrOc3ProfileName = _CnTca24HrOc3ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 7),
    _CnTca24HrOc3ProfileName_Type()
)
cnTca24HrOc3ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrOc3ProfileName.setStatus("current")
_CnTca24HrOc3RowStatus_Type = RowStatus
_CnTca24HrOc3RowStatus_Object = MibTableColumn
cnTca24HrOc3RowStatus = _CnTca24HrOc3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 2, 1, 8),
    _CnTca24HrOc3RowStatus_Type()
)
cnTca24HrOc3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrOc3RowStatus.setStatus("current")
_CnTca15MinT1ProfileTable_Object = MibTable
cnTca15MinT1ProfileTable = _CnTca15MinT1ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3)
)
if mibBuilder.loadTexts:
    cnTca15MinT1ProfileTable.setStatus("current")
_CnTca15MinT1ProfileEntry_Object = MibTableRow
cnTca15MinT1ProfileEntry = _CnTca15MinT1ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1)
)
cnTca15MinT1ProfileEntry.setIndexNames(
    (0, "CEM-TCA", "cnTca15MinT1Profile"),
)
if mibBuilder.loadTexts:
    cnTca15MinT1ProfileEntry.setStatus("current")
_CnTca15MinT1Profile_Type = CnTcaProfileType
_CnTca15MinT1Profile_Object = MibTableColumn
cnTca15MinT1Profile = _CnTca15MinT1Profile_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 1),
    _CnTca15MinT1Profile_Type()
)
cnTca15MinT1Profile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTca15MinT1Profile.setStatus("current")
_CnTca15MinT1LCVs_Type = Integer32
_CnTca15MinT1LCVs_Object = MibTableColumn
cnTca15MinT1LCVs = _CnTca15MinT1LCVs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 2),
    _CnTca15MinT1LCVs_Type()
)
cnTca15MinT1LCVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1LCVs.setStatus("current")
_CnTca15MinT1PCVs_Type = Integer32
_CnTca15MinT1PCVs_Object = MibTableColumn
cnTca15MinT1PCVs = _CnTca15MinT1PCVs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 3),
    _CnTca15MinT1PCVs_Type()
)
cnTca15MinT1PCVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1PCVs.setStatus("current")
_CnTca15MinT1PCVFEs_Type = Integer32
_CnTca15MinT1PCVFEs_Object = MibTableColumn
cnTca15MinT1PCVFEs = _CnTca15MinT1PCVFEs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 4),
    _CnTca15MinT1PCVFEs_Type()
)
cnTca15MinT1PCVFEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1PCVFEs.setStatus("current")
_CnTca15MinT1CSSs_Type = Integer32
_CnTca15MinT1CSSs_Object = MibTableColumn
cnTca15MinT1CSSs = _CnTca15MinT1CSSs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 5),
    _CnTca15MinT1CSSs_Type()
)
cnTca15MinT1CSSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1CSSs.setStatus("current")
_CnTca15MinT1SASs_Type = Integer32
_CnTca15MinT1SASs_Object = MibTableColumn
cnTca15MinT1SASs = _CnTca15MinT1SASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 6),
    _CnTca15MinT1SASs_Type()
)
cnTca15MinT1SASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1SASs.setStatus("current")
_CnTca15MinT1LESs_Type = Integer32
_CnTca15MinT1LESs_Object = MibTableColumn
cnTca15MinT1LESs = _CnTca15MinT1LESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 7),
    _CnTca15MinT1LESs_Type()
)
cnTca15MinT1LESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1LESs.setStatus("current")
_CnTca15MinT1PESs_Type = Integer32
_CnTca15MinT1PESs_Object = MibTableColumn
cnTca15MinT1PESs = _CnTca15MinT1PESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 8),
    _CnTca15MinT1PESs_Type()
)
cnTca15MinT1PESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1PESs.setStatus("current")
_CnTca15MinT1LSESs_Type = Integer32
_CnTca15MinT1LSESs_Object = MibTableColumn
cnTca15MinT1LSESs = _CnTca15MinT1LSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 9),
    _CnTca15MinT1LSESs_Type()
)
cnTca15MinT1LSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1LSESs.setStatus("current")
_CnTca15MinT1PSESs_Type = Integer32
_CnTca15MinT1PSESs_Object = MibTableColumn
cnTca15MinT1PSESs = _CnTca15MinT1PSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 10),
    _CnTca15MinT1PSESs_Type()
)
cnTca15MinT1PSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1PSESs.setStatus("current")
_CnTca15MinT1PUASs_Type = Integer32
_CnTca15MinT1PUASs_Object = MibTableColumn
cnTca15MinT1PUASs = _CnTca15MinT1PUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 11),
    _CnTca15MinT1PUASs_Type()
)
cnTca15MinT1PUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1PUASs.setStatus("current")


class _CnTca15MinT1ProfileName_Type(OctetString):
    """Custom type cnTca15MinT1ProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnTca15MinT1ProfileName_Type.__name__ = "OctetString"
_CnTca15MinT1ProfileName_Object = MibTableColumn
cnTca15MinT1ProfileName = _CnTca15MinT1ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 12),
    _CnTca15MinT1ProfileName_Type()
)
cnTca15MinT1ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1ProfileName.setStatus("current")
_CnTca15MinT1RowStatus_Type = RowStatus
_CnTca15MinT1RowStatus_Object = MibTableColumn
cnTca15MinT1RowStatus = _CnTca15MinT1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 3, 1, 13),
    _CnTca15MinT1RowStatus_Type()
)
cnTca15MinT1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca15MinT1RowStatus.setStatus("current")
_CnTca24HrT1ProfileTable_Object = MibTable
cnTca24HrT1ProfileTable = _CnTca24HrT1ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4)
)
if mibBuilder.loadTexts:
    cnTca24HrT1ProfileTable.setStatus("current")
_CnTca24HrT1ProfileEntry_Object = MibTableRow
cnTca24HrT1ProfileEntry = _CnTca24HrT1ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1)
)
cnTca24HrT1ProfileEntry.setIndexNames(
    (0, "CEM-TCA", "cnTca24HrT1Profile"),
)
if mibBuilder.loadTexts:
    cnTca24HrT1ProfileEntry.setStatus("current")
_CnTca24HrT1Profile_Type = CnTcaProfileType
_CnTca24HrT1Profile_Object = MibTableColumn
cnTca24HrT1Profile = _CnTca24HrT1Profile_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 1),
    _CnTca24HrT1Profile_Type()
)
cnTca24HrT1Profile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTca24HrT1Profile.setStatus("current")
_CnTca24HrT1LCVs_Type = Integer32
_CnTca24HrT1LCVs_Object = MibTableColumn
cnTca24HrT1LCVs = _CnTca24HrT1LCVs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 2),
    _CnTca24HrT1LCVs_Type()
)
cnTca24HrT1LCVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1LCVs.setStatus("current")
_CnTca24HrT1PCVs_Type = Integer32
_CnTca24HrT1PCVs_Object = MibTableColumn
cnTca24HrT1PCVs = _CnTca24HrT1PCVs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 3),
    _CnTca24HrT1PCVs_Type()
)
cnTca24HrT1PCVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1PCVs.setStatus("current")
_CnTca24HrT1PCVFEs_Type = Integer32
_CnTca24HrT1PCVFEs_Object = MibTableColumn
cnTca24HrT1PCVFEs = _CnTca24HrT1PCVFEs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 4),
    _CnTca24HrT1PCVFEs_Type()
)
cnTca24HrT1PCVFEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1PCVFEs.setStatus("current")
_CnTca24HrT1CSSs_Type = Integer32
_CnTca24HrT1CSSs_Object = MibTableColumn
cnTca24HrT1CSSs = _CnTca24HrT1CSSs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 5),
    _CnTca24HrT1CSSs_Type()
)
cnTca24HrT1CSSs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1CSSs.setStatus("current")
_CnTca24HrT1SASs_Type = Integer32
_CnTca24HrT1SASs_Object = MibTableColumn
cnTca24HrT1SASs = _CnTca24HrT1SASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 6),
    _CnTca24HrT1SASs_Type()
)
cnTca24HrT1SASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1SASs.setStatus("current")
_CnTca24HrT1LESs_Type = Integer32
_CnTca24HrT1LESs_Object = MibTableColumn
cnTca24HrT1LESs = _CnTca24HrT1LESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 7),
    _CnTca24HrT1LESs_Type()
)
cnTca24HrT1LESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1LESs.setStatus("current")
_CnTca24HrT1PESs_Type = Integer32
_CnTca24HrT1PESs_Object = MibTableColumn
cnTca24HrT1PESs = _CnTca24HrT1PESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 8),
    _CnTca24HrT1PESs_Type()
)
cnTca24HrT1PESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1PESs.setStatus("current")
_CnTca24HrT1LSESs_Type = Integer32
_CnTca24HrT1LSESs_Object = MibTableColumn
cnTca24HrT1LSESs = _CnTca24HrT1LSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 9),
    _CnTca24HrT1LSESs_Type()
)
cnTca24HrT1LSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1LSESs.setStatus("current")
_CnTca24HrT1PSESs_Type = Integer32
_CnTca24HrT1PSESs_Object = MibTableColumn
cnTca24HrT1PSESs = _CnTca24HrT1PSESs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 10),
    _CnTca24HrT1PSESs_Type()
)
cnTca24HrT1PSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1PSESs.setStatus("current")
_CnTca24HrT1PUASs_Type = Integer32
_CnTca24HrT1PUASs_Object = MibTableColumn
cnTca24HrT1PUASs = _CnTca24HrT1PUASs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 11),
    _CnTca24HrT1PUASs_Type()
)
cnTca24HrT1PUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1PUASs.setStatus("current")


class _CnTca24HrT1ProfileName_Type(OctetString):
    """Custom type cnTca24HrT1ProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnTca24HrT1ProfileName_Type.__name__ = "OctetString"
_CnTca24HrT1ProfileName_Object = MibTableColumn
cnTca24HrT1ProfileName = _CnTca24HrT1ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 12),
    _CnTca24HrT1ProfileName_Type()
)
cnTca24HrT1ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1ProfileName.setStatus("current")
_CnTca24HrT1RowStatus_Type = RowStatus
_CnTca24HrT1RowStatus_Object = MibTableColumn
cnTca24HrT1RowStatus = _CnTca24HrT1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 17, 4, 1, 13),
    _CnTca24HrT1RowStatus_Type()
)
cnTca24HrT1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnTca24HrT1RowStatus.setStatus("current")
_CnTcaConformance_ObjectIdentity = ObjectIdentity
cnTcaConformance = _CnTcaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 17, 5)
)

# Managed Objects groups

cnTcaOC3TcaObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 17, 5, 1)
)
cnTcaOC3TcaObjectsGroup.setObjects(
      *(("CEM-TCA", "cnTca15MinOc3CVs"),
        ("CEM-TCA", "cnTca15MinOc3PESs"),
        ("CEM-TCA", "cnTca15MinOc3PSESs"),
        ("CEM-TCA", "cnTca15MinOc3LUASs"),
        ("CEM-TCA", "cnTca15MinOc3PUASs"),
        ("CEM-TCA", "cnTca15MinOc3ProfileName"),
        ("CEM-TCA", "cnTca15MinOc3RowStatus"),
        ("CEM-TCA", "cnTca24HrOc3CVs"),
        ("CEM-TCA", "cnTca24HrOc3PESs"),
        ("CEM-TCA", "cnTca24HrOc3PSESs"),
        ("CEM-TCA", "cnTca24HrOc3LUASs"),
        ("CEM-TCA", "cnTca24HrOc3PUASs"),
        ("CEM-TCA", "cnTca24HrOc3ProfileName"),
        ("CEM-TCA", "cnTca24HrOc3RowStatus"))
)
if mibBuilder.loadTexts:
    cnTcaOC3TcaObjectsGroup.setStatus("current")

cnTcaT1TcaObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 17, 5, 2)
)
cnTcaT1TcaObjectsGroup.setObjects(
      *(("CEM-TCA", "cnTca15MinT1LCVs"),
        ("CEM-TCA", "cnTca15MinT1PCVs"),
        ("CEM-TCA", "cnTca15MinT1PCVFEs"),
        ("CEM-TCA", "cnTca15MinT1CSSs"),
        ("CEM-TCA", "cnTca15MinT1SASs"),
        ("CEM-TCA", "cnTca15MinT1LESs"),
        ("CEM-TCA", "cnTca15MinT1PESs"),
        ("CEM-TCA", "cnTca15MinT1LSESs"),
        ("CEM-TCA", "cnTca15MinT1PSESs"),
        ("CEM-TCA", "cnTca15MinT1PUASs"),
        ("CEM-TCA", "cnTca15MinT1ProfileName"),
        ("CEM-TCA", "cnTca15MinT1RowStatus"),
        ("CEM-TCA", "cnTca24HrT1LCVs"),
        ("CEM-TCA", "cnTca24HrT1PCVs"),
        ("CEM-TCA", "cnTca24HrT1PCVFEs"),
        ("CEM-TCA", "cnTca24HrT1CSSs"),
        ("CEM-TCA", "cnTca24HrT1SASs"),
        ("CEM-TCA", "cnTca24HrT1LESs"),
        ("CEM-TCA", "cnTca24HrT1PESs"),
        ("CEM-TCA", "cnTca24HrT1LSESs"),
        ("CEM-TCA", "cnTca24HrT1PSESs"),
        ("CEM-TCA", "cnTca24HrT1PUASs"),
        ("CEM-TCA", "cnTca24HrT1ProfileName"),
        ("CEM-TCA", "cnTca24HrT1RowStatus"))
)
if mibBuilder.loadTexts:
    cnTcaT1TcaObjectsGroup.setStatus("current")

cnTcacn1000ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 17, 5, 3)
)
cnTcacn1000ObjectsGroup.setObjects(
      *(("CEM-TCA", "cnTca15MinOc3CVs"),
        ("CEM-TCA", "cnTca15MinOc3PESs"),
        ("CEM-TCA", "cnTca15MinOc3PSESs"),
        ("CEM-TCA", "cnTca15MinOc3LUASs"),
        ("CEM-TCA", "cnTca15MinOc3PUASs"),
        ("CEM-TCA", "cnTca15MinOc3ProfileName"),
        ("CEM-TCA", "cnTca15MinOc3RowStatus"),
        ("CEM-TCA", "cnTca24HrOc3CVs"),
        ("CEM-TCA", "cnTca24HrOc3PESs"),
        ("CEM-TCA", "cnTca24HrOc3PSESs"),
        ("CEM-TCA", "cnTca24HrOc3LUASs"),
        ("CEM-TCA", "cnTca24HrOc3PUASs"),
        ("CEM-TCA", "cnTca24HrOc3ProfileName"),
        ("CEM-TCA", "cnTca24HrOc3RowStatus"),
        ("CEM-TCA", "cnTca15MinT1LCVs"),
        ("CEM-TCA", "cnTca15MinT1PCVs"),
        ("CEM-TCA", "cnTca15MinT1PCVFEs"),
        ("CEM-TCA", "cnTca15MinT1CSSs"),
        ("CEM-TCA", "cnTca15MinT1SASs"),
        ("CEM-TCA", "cnTca15MinT1LESs"),
        ("CEM-TCA", "cnTca15MinT1PESs"),
        ("CEM-TCA", "cnTca15MinT1LSESs"),
        ("CEM-TCA", "cnTca15MinT1PSESs"),
        ("CEM-TCA", "cnTca15MinT1PUASs"),
        ("CEM-TCA", "cnTca15MinT1ProfileName"),
        ("CEM-TCA", "cnTca15MinT1RowStatus"),
        ("CEM-TCA", "cnTca24HrT1LCVs"),
        ("CEM-TCA", "cnTca24HrT1PCVs"),
        ("CEM-TCA", "cnTca24HrT1PCVFEs"),
        ("CEM-TCA", "cnTca24HrT1CSSs"),
        ("CEM-TCA", "cnTca24HrT1SASs"),
        ("CEM-TCA", "cnTca24HrT1LESs"),
        ("CEM-TCA", "cnTca24HrT1PESs"),
        ("CEM-TCA", "cnTca24HrT1LSESs"),
        ("CEM-TCA", "cnTca24HrT1PSESs"),
        ("CEM-TCA", "cnTca24HrT1PUASs"),
        ("CEM-TCA", "cnTca24HrT1ProfileName"),
        ("CEM-TCA", "cnTca24HrT1RowStatus"))
)
if mibBuilder.loadTexts:
    cnTcacn1000ObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cnTcaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 17, 5, 4)
)
cnTcaCompliance.setObjects(
    ("CEM-TCA", "cnTcacn1000ObjectsGroup")
)
if mibBuilder.loadTexts:
    cnTcaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-TCA",
    **{"CnTcaProfileType": CnTcaProfileType,
       "cnTcaModule": cnTcaModule,
       "cnTca15MinOc3ProfileTable": cnTca15MinOc3ProfileTable,
       "cnTca15MinOc3ProfileEntry": cnTca15MinOc3ProfileEntry,
       "cnTca15MinOc3Profile": cnTca15MinOc3Profile,
       "cnTca15MinOc3CVs": cnTca15MinOc3CVs,
       "cnTca15MinOc3PESs": cnTca15MinOc3PESs,
       "cnTca15MinOc3PSESs": cnTca15MinOc3PSESs,
       "cnTca15MinOc3LUASs": cnTca15MinOc3LUASs,
       "cnTca15MinOc3PUASs": cnTca15MinOc3PUASs,
       "cnTca15MinOc3ProfileName": cnTca15MinOc3ProfileName,
       "cnTca15MinOc3RowStatus": cnTca15MinOc3RowStatus,
       "cnTca24HrOc3ProfileTable": cnTca24HrOc3ProfileTable,
       "cnTca24HrOc3ProfileEntry": cnTca24HrOc3ProfileEntry,
       "cnTca24HrOc3Profile": cnTca24HrOc3Profile,
       "cnTca24HrOc3CVs": cnTca24HrOc3CVs,
       "cnTca24HrOc3PESs": cnTca24HrOc3PESs,
       "cnTca24HrOc3PSESs": cnTca24HrOc3PSESs,
       "cnTca24HrOc3LUASs": cnTca24HrOc3LUASs,
       "cnTca24HrOc3PUASs": cnTca24HrOc3PUASs,
       "cnTca24HrOc3ProfileName": cnTca24HrOc3ProfileName,
       "cnTca24HrOc3RowStatus": cnTca24HrOc3RowStatus,
       "cnTca15MinT1ProfileTable": cnTca15MinT1ProfileTable,
       "cnTca15MinT1ProfileEntry": cnTca15MinT1ProfileEntry,
       "cnTca15MinT1Profile": cnTca15MinT1Profile,
       "cnTca15MinT1LCVs": cnTca15MinT1LCVs,
       "cnTca15MinT1PCVs": cnTca15MinT1PCVs,
       "cnTca15MinT1PCVFEs": cnTca15MinT1PCVFEs,
       "cnTca15MinT1CSSs": cnTca15MinT1CSSs,
       "cnTca15MinT1SASs": cnTca15MinT1SASs,
       "cnTca15MinT1LESs": cnTca15MinT1LESs,
       "cnTca15MinT1PESs": cnTca15MinT1PESs,
       "cnTca15MinT1LSESs": cnTca15MinT1LSESs,
       "cnTca15MinT1PSESs": cnTca15MinT1PSESs,
       "cnTca15MinT1PUASs": cnTca15MinT1PUASs,
       "cnTca15MinT1ProfileName": cnTca15MinT1ProfileName,
       "cnTca15MinT1RowStatus": cnTca15MinT1RowStatus,
       "cnTca24HrT1ProfileTable": cnTca24HrT1ProfileTable,
       "cnTca24HrT1ProfileEntry": cnTca24HrT1ProfileEntry,
       "cnTca24HrT1Profile": cnTca24HrT1Profile,
       "cnTca24HrT1LCVs": cnTca24HrT1LCVs,
       "cnTca24HrT1PCVs": cnTca24HrT1PCVs,
       "cnTca24HrT1PCVFEs": cnTca24HrT1PCVFEs,
       "cnTca24HrT1CSSs": cnTca24HrT1CSSs,
       "cnTca24HrT1SASs": cnTca24HrT1SASs,
       "cnTca24HrT1LESs": cnTca24HrT1LESs,
       "cnTca24HrT1PESs": cnTca24HrT1PESs,
       "cnTca24HrT1LSESs": cnTca24HrT1LSESs,
       "cnTca24HrT1PSESs": cnTca24HrT1PSESs,
       "cnTca24HrT1PUASs": cnTca24HrT1PUASs,
       "cnTca24HrT1ProfileName": cnTca24HrT1ProfileName,
       "cnTca24HrT1RowStatus": cnTca24HrT1RowStatus,
       "cnTcaConformance": cnTcaConformance,
       "cnTcaOC3TcaObjectsGroup": cnTcaOC3TcaObjectsGroup,
       "cnTcaT1TcaObjectsGroup": cnTcaT1TcaObjectsGroup,
       "cnTcacn1000ObjectsGroup": cnTcacn1000ObjectsGroup,
       "cnTcaCompliance": cnTcaCompliance}
)
