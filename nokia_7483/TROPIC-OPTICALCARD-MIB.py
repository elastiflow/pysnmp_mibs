# SNMP MIB module (TROPIC-OPTICALCARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-OPTICALCARD-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(tnCardModules,
 tnOpticalCardMIB) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnCardModules",
    "tnOpticalCardMIB")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(TnCommand,
 TropicLEDColorType,
 TropicLEDStateType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCommand",
    "TropicLEDColorType",
    "TropicLEDStateType")


# MODULE-IDENTITY

tnOpticalCardMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tnOpticalCardMibModule.setRevisions(
        ("2008-02-16 12:00",
         "2008-04-11 12:00",
         "2008-05-29 12:00",
         "2008-06-09 12:00",
         "2008-07-25 12:00",
         "2009-03-25 12:00",
         "2009-04-07 12:00",
         "2009-04-23 12:00",
         "2009-04-30 12:00",
         "2009-05-19 12:00",
         "2009-05-31 12:00",
         "2009-06-22 12:00",
         "2009-08-05 12:00",
         "2009-09-26 12:00",
         "2010-01-08 12:00",
         "2010-01-25 12:00",
         "2010-01-27 12:00",
         "2010-05-10 12:00",
         "2010-07-29 12:00",
         "2010-09-28 12:00",
         "2010-10-24 12:00",
         "2010-11-01 12:00",
         "2010-11-08 12:00",
         "2011-03-25 12:00",
         "2011-05-23 12:00",
         "2011-07-19 12:00",
         "2011-07-22 12:00",
         "2011-08-12 12:00",
         "2011-09-30 12:00",
         "2012-03-18 12:00",
         "2012-03-29 12:00",
         "2012-04-27 12:00",
         "2012-06-13 12:00",
         "2012-09-01 12:00",
         "2012-09-06 12:00",
         "2012-10-22 12:00",
         "2012-10-24 12:00",
         "2013-01-07 12:00",
         "2013-03-14 12:00",
         "2013-04-09 12:00",
         "2013-04-26 12:00",
         "2013-05-21 12:00",
         "2013-10-21 12:00",
         "2014-02-26 12:00",
         "2014-08-13 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmSonetSdhPpSectionIfType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("oc3", 2),
          ("oc12", 3),
          ("oc48", 4),
          ("stm1", 5),
          ("stm4", 6),
          ("stm16", 7))
    )



class AluWdmPcsSectionIfType(TextualConvention, Integer32):
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
          ("gige", 2),
          ("fc100", 3),
          ("fc200", 4),
          ("fc400", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TnOpticalCardConf_ObjectIdentity = ObjectIdentity
tnOpticalCardConf = _TnOpticalCardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1)
)
_TnOpticalCardGroups_ObjectIdentity = ObjectIdentity
tnOpticalCardGroups = _TnOpticalCardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1)
)
_TnOpticalCardCompliances_ObjectIdentity = ObjectIdentity
tnOpticalCardCompliances = _TnOpticalCardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 2)
)
_TnOpticalCardObjs_ObjectIdentity = ObjectIdentity
tnOpticalCardObjs = _TnOpticalCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2)
)
_TnOpticalCardTotal_Type = Integer32
_TnOpticalCardTotal_Object = MibScalar
tnOpticalCardTotal = _TnOpticalCardTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 1),
    _TnOpticalCardTotal_Type()
)
tnOpticalCardTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpticalCardTotal.setStatus("current")
_TnDcmCardTable_Object = MibTable
tnDcmCardTable = _TnDcmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    tnDcmCardTable.setStatus("current")
_TnDcmCardEntry_Object = MibTableRow
tnDcmCardEntry = _TnDcmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1)
)
tnDcmCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnDcmCardEntry.setStatus("current")


class _TnDcmCardProgrammedCompensationDistance_Type(Unsigned32):
    """Custom type tnDcmCardProgrammedCompensationDistance based on Unsigned32"""
    defaultValue = 0


_TnDcmCardProgrammedCompensationDistance_Type.__name__ = "Unsigned32"
_TnDcmCardProgrammedCompensationDistance_Object = MibTableColumn
tnDcmCardProgrammedCompensationDistance = _TnDcmCardProgrammedCompensationDistance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 1),
    _TnDcmCardProgrammedCompensationDistance_Type()
)
tnDcmCardProgrammedCompensationDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDcmCardProgrammedCompensationDistance.setStatus("current")
if mibBuilder.loadTexts:
    tnDcmCardProgrammedCompensationDistance.setUnits("km")
_TnDcmCardPresentCompensationDistance_Type = Unsigned32
_TnDcmCardPresentCompensationDistance_Object = MibTableColumn
tnDcmCardPresentCompensationDistance = _TnDcmCardPresentCompensationDistance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 2),
    _TnDcmCardPresentCompensationDistance_Type()
)
tnDcmCardPresentCompensationDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardPresentCompensationDistance.setStatus("current")
if mibBuilder.loadTexts:
    tnDcmCardPresentCompensationDistance.setUnits("km")


class _TnDcmCardSize_Type(SnmpAdminString):
    """Custom type tnDcmCardSize based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardSize_Type.__name__ = "SnmpAdminString"
_TnDcmCardSize_Object = MibTableColumn
tnDcmCardSize = _TnDcmCardSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 3),
    _TnDcmCardSize_Type()
)
tnDcmCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardSize.setStatus("current")


class _TnDcmCardFiberType_Type(SnmpAdminString):
    """Custom type tnDcmCardFiberType based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardFiberType_Type.__name__ = "SnmpAdminString"
_TnDcmCardFiberType_Object = MibTableColumn
tnDcmCardFiberType = _TnDcmCardFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 4),
    _TnDcmCardFiberType_Type()
)
tnDcmCardFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardFiberType.setStatus("current")


class _TnDcmCardAverageInsertionLoss_Type(SnmpAdminString):
    """Custom type tnDcmCardAverageInsertionLoss based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardAverageInsertionLoss_Type.__name__ = "SnmpAdminString"
_TnDcmCardAverageInsertionLoss_Object = MibTableColumn
tnDcmCardAverageInsertionLoss = _TnDcmCardAverageInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 5),
    _TnDcmCardAverageInsertionLoss_Type()
)
tnDcmCardAverageInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardAverageInsertionLoss.setStatus("current")


class _TnDcmCardInsertionLossSlope_Type(SnmpAdminString):
    """Custom type tnDcmCardInsertionLossSlope based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardInsertionLossSlope_Type.__name__ = "SnmpAdminString"
_TnDcmCardInsertionLossSlope_Object = MibTableColumn
tnDcmCardInsertionLossSlope = _TnDcmCardInsertionLossSlope_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 6),
    _TnDcmCardInsertionLossSlope_Type()
)
tnDcmCardInsertionLossSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardInsertionLossSlope.setStatus("current")


class _TnDcmCardAverageInsertionLossPad_Type(SnmpAdminString):
    """Custom type tnDcmCardAverageInsertionLossPad based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardAverageInsertionLossPad_Type.__name__ = "SnmpAdminString"
_TnDcmCardAverageInsertionLossPad_Object = MibTableColumn
tnDcmCardAverageInsertionLossPad = _TnDcmCardAverageInsertionLossPad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 7),
    _TnDcmCardAverageInsertionLossPad_Type()
)
tnDcmCardAverageInsertionLossPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardAverageInsertionLossPad.setStatus("current")


class _TnDcmCardInsertionLossSlopePad_Type(SnmpAdminString):
    """Custom type tnDcmCardInsertionLossSlopePad based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardInsertionLossSlopePad_Type.__name__ = "SnmpAdminString"
_TnDcmCardInsertionLossSlopePad_Object = MibTableColumn
tnDcmCardInsertionLossSlopePad = _TnDcmCardInsertionLossSlopePad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 8),
    _TnDcmCardInsertionLossSlopePad_Type()
)
tnDcmCardInsertionLossSlopePad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardInsertionLossSlopePad.setStatus("current")


class _TnDcmCardTotalDispTilt_Type(SnmpAdminString):
    """Custom type tnDcmCardTotalDispTilt based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardTotalDispTilt_Type.__name__ = "SnmpAdminString"
_TnDcmCardTotalDispTilt_Object = MibTableColumn
tnDcmCardTotalDispTilt = _TnDcmCardTotalDispTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 9),
    _TnDcmCardTotalDispTilt_Type()
)
tnDcmCardTotalDispTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardTotalDispTilt.setStatus("current")


class _TnDcmCardDispFiberLength_Type(SnmpAdminString):
    """Custom type tnDcmCardDispFiberLength based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardDispFiberLength_Type.__name__ = "SnmpAdminString"
_TnDcmCardDispFiberLength_Object = MibTableColumn
tnDcmCardDispFiberLength = _TnDcmCardDispFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 10),
    _TnDcmCardDispFiberLength_Type()
)
tnDcmCardDispFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardDispFiberLength.setStatus("current")


class _TnDcmCardPMD_Type(SnmpAdminString):
    """Custom type tnDcmCardPMD based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardPMD_Type.__name__ = "SnmpAdminString"
_TnDcmCardPMD_Object = MibTableColumn
tnDcmCardPMD = _TnDcmCardPMD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 11),
    _TnDcmCardPMD_Type()
)
tnDcmCardPMD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardPMD.setStatus("current")


class _TnDcmCardProvisionedFiberType_Type(Integer32):
    """Custom type tnDcmCardProvisionedFiberType based on Integer32"""
    defaultValue = 1

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
        *(("ssmf", 1),
          ("eleaf", 2),
          ("twrs", 3),
          ("ssmfb", 4),
          ("eleafb", 5))
    )


_TnDcmCardProvisionedFiberType_Type.__name__ = "Integer32"
_TnDcmCardProvisionedFiberType_Object = MibTableColumn
tnDcmCardProvisionedFiberType = _TnDcmCardProvisionedFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 12),
    _TnDcmCardProvisionedFiberType_Type()
)
tnDcmCardProvisionedFiberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDcmCardProvisionedFiberType.setStatus("current")
_TnPowerControlCardTable_Object = MibTable
tnPowerControlCardTable = _TnPowerControlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8)
)
if mibBuilder.loadTexts:
    tnPowerControlCardTable.setStatus("current")
_TnPowerControlCardEntry_Object = MibTableRow
tnPowerControlCardEntry = _TnPowerControlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1)
)
tnPowerControlCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerControlCardEntry.setStatus("current")


class _TnPowerControlCardCapabilityProgrammed_Type(TruthValue):
    """Custom type tnPowerControlCardCapabilityProgrammed based on TruthValue"""
    defaultValue = 1


_TnPowerControlCardCapabilityProgrammed_Type.__name__ = "TruthValue"
_TnPowerControlCardCapabilityProgrammed_Object = MibTableColumn
tnPowerControlCardCapabilityProgrammed = _TnPowerControlCardCapabilityProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1, 1),
    _TnPowerControlCardCapabilityProgrammed_Type()
)
tnPowerControlCardCapabilityProgrammed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerControlCardCapabilityProgrammed.setStatus("current")


class _TnPowerControlCardCapabilityPresent_Type(TruthValue):
    """Custom type tnPowerControlCardCapabilityPresent based on TruthValue"""
    defaultValue = 1


_TnPowerControlCardCapabilityPresent_Type.__name__ = "TruthValue"
_TnPowerControlCardCapabilityPresent_Object = MibTableColumn
tnPowerControlCardCapabilityPresent = _TnPowerControlCardCapabilityPresent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1, 2),
    _TnPowerControlCardCapabilityPresent_Type()
)
tnPowerControlCardCapabilityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerControlCardCapabilityPresent.setStatus("current")
_TnPowerControlCardCapabilityInUse_Type = TruthValue
_TnPowerControlCardCapabilityInUse_Object = MibTableColumn
tnPowerControlCardCapabilityInUse = _TnPowerControlCardCapabilityInUse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1, 3),
    _TnPowerControlCardCapabilityInUse_Type()
)
tnPowerControlCardCapabilityInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerControlCardCapabilityInUse.setStatus("current")
_TnWssCardTable_Object = MibTable
tnWssCardTable = _TnWssCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9)
)
if mibBuilder.loadTexts:
    tnWssCardTable.setStatus("current")
_TnWssCardEntry_Object = MibTableRow
tnWssCardEntry = _TnWssCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1)
)
tnWssCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnWssCardEntry.setStatus("current")


class _TnWssCardAddPathTargetPower_Type(Integer32):
    """Custom type tnWssCardAddPathTargetPower based on Integer32"""
    defaultValue = 130


_TnWssCardAddPathTargetPower_Type.__name__ = "Integer32"
_TnWssCardAddPathTargetPower_Object = MibTableColumn
tnWssCardAddPathTargetPower = _TnWssCardAddPathTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 1),
    _TnWssCardAddPathTargetPower_Type()
)
tnWssCardAddPathTargetPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAddPathTargetPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardAddPathTargetPower.setUnits("mBm")


class _TnWssCardAddPathEgressPower_Type(Integer32):
    """Custom type tnWssCardAddPathEgressPower based on Integer32"""
    defaultValue = -900


_TnWssCardAddPathEgressPower_Type.__name__ = "Integer32"
_TnWssCardAddPathEgressPower_Object = MibTableColumn
tnWssCardAddPathEgressPower = _TnWssCardAddPathEgressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 2),
    _TnWssCardAddPathEgressPower_Type()
)
tnWssCardAddPathEgressPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAddPathEgressPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardAddPathEgressPower.setUnits("mBm")


class _TnWssCardAddPathTotalChannel_Type(Unsigned32):
    """Custom type tnWssCardAddPathTotalChannel based on Unsigned32"""
    defaultValue = 12


_TnWssCardAddPathTotalChannel_Type.__name__ = "Unsigned32"
_TnWssCardAddPathTotalChannel_Object = MibTableColumn
tnWssCardAddPathTotalChannel = _TnWssCardAddPathTotalChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 3),
    _TnWssCardAddPathTotalChannel_Type()
)
tnWssCardAddPathTotalChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAddPathTotalChannel.setStatus("current")


class _TnWssCardReservedDegree_Type(Unsigned32):
    """Custom type tnWssCardReservedDegree based on Unsigned32"""
    defaultValue = 2


_TnWssCardReservedDegree_Type.__name__ = "Unsigned32"
_TnWssCardReservedDegree_Object = MibTableColumn
tnWssCardReservedDegree = _TnWssCardReservedDegree_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 4),
    _TnWssCardReservedDegree_Type()
)
tnWssCardReservedDegree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardReservedDegree.setStatus("current")


class _TnWssCardLnsEnable_Type(Integer32):
    """Custom type tnWssCardLnsEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_TnWssCardLnsEnable_Type.__name__ = "Integer32"
_TnWssCardLnsEnable_Object = MibTableColumn
tnWssCardLnsEnable = _TnWssCardLnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 5),
    _TnWssCardLnsEnable_Type()
)
tnWssCardLnsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardLnsEnable.setStatus("current")
_TnWssCardLnsPower_Type = Integer32
_TnWssCardLnsPower_Object = MibTableColumn
tnWssCardLnsPower = _TnWssCardLnsPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 6),
    _TnWssCardLnsPower_Type()
)
tnWssCardLnsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWssCardLnsPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardLnsPower.setUnits("mBm")


class _TnWssCardAdBlockLevelAdd_Type(Unsigned32):
    """Custom type tnWssCardAdBlockLevelAdd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnWssCardAdBlockLevelAdd_Type.__name__ = "Unsigned32"
_TnWssCardAdBlockLevelAdd_Object = MibTableColumn
tnWssCardAdBlockLevelAdd = _TnWssCardAdBlockLevelAdd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 9),
    _TnWssCardAdBlockLevelAdd_Type()
)
tnWssCardAdBlockLevelAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAdBlockLevelAdd.setStatus("current")


class _TnWssCardAdBlockLevelDrop_Type(Unsigned32):
    """Custom type tnWssCardAdBlockLevelDrop based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnWssCardAdBlockLevelDrop_Type.__name__ = "Unsigned32"
_TnWssCardAdBlockLevelDrop_Object = MibTableColumn
tnWssCardAdBlockLevelDrop = _TnWssCardAdBlockLevelDrop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 10),
    _TnWssCardAdBlockLevelDrop_Type()
)
tnWssCardAdBlockLevelDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAdBlockLevelDrop.setStatus("current")
_TnSfdCardTable_Object = MibTable
tnSfdCardTable = _TnSfdCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10)
)
if mibBuilder.loadTexts:
    tnSfdCardTable.setStatus("current")
_TnSfdCardEntry_Object = MibTableRow
tnSfdCardEntry = _TnSfdCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10, 1)
)
tnSfdCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSfdCardEntry.setStatus("current")


class _TnSfdCardAverageMuxInsertionLoss_Type(SnmpAdminString):
    """Custom type tnSfdCardAverageMuxInsertionLoss based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSfdCardAverageMuxInsertionLoss_Type.__name__ = "SnmpAdminString"
_TnSfdCardAverageMuxInsertionLoss_Object = MibTableColumn
tnSfdCardAverageMuxInsertionLoss = _TnSfdCardAverageMuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10, 1, 1),
    _TnSfdCardAverageMuxInsertionLoss_Type()
)
tnSfdCardAverageMuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfdCardAverageMuxInsertionLoss.setStatus("current")


class _TnSfdCardAverageDemuxInsertionLoss_Type(SnmpAdminString):
    """Custom type tnSfdCardAverageDemuxInsertionLoss based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSfdCardAverageDemuxInsertionLoss_Type.__name__ = "SnmpAdminString"
_TnSfdCardAverageDemuxInsertionLoss_Object = MibTableColumn
tnSfdCardAverageDemuxInsertionLoss = _TnSfdCardAverageDemuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10, 1, 2),
    _TnSfdCardAverageDemuxInsertionLoss_Type()
)
tnSfdCardAverageDemuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfdCardAverageDemuxInsertionLoss.setStatus("current")
_TnSonetSdhPpSectionCardTable_Object = MibTable
tnSonetSdhPpSectionCardTable = _TnSonetSdhPpSectionCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11)
)
if mibBuilder.loadTexts:
    tnSonetSdhPpSectionCardTable.setStatus("current")
_TnSonetSdhPpSectionCardEntry_Object = MibTableRow
tnSonetSdhPpSectionCardEntry = _TnSonetSdhPpSectionCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1)
)
tnSonetSdhPpSectionCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSonetSdhPpSectionCardEntry.setStatus("current")
_TnSonetSdhPpSection1Port_Type = Unsigned32
_TnSonetSdhPpSection1Port_Object = MibTableColumn
tnSonetSdhPpSection1Port = _TnSonetSdhPpSection1Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 1),
    _TnSonetSdhPpSection1Port_Type()
)
tnSonetSdhPpSection1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection1Port.setStatus("current")
_TnSonetSdhPpSection2Port_Type = Unsigned32
_TnSonetSdhPpSection2Port_Object = MibTableColumn
tnSonetSdhPpSection2Port = _TnSonetSdhPpSection2Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 2),
    _TnSonetSdhPpSection2Port_Type()
)
tnSonetSdhPpSection2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection2Port.setStatus("current")
_TnSonetSdhPpSection3Port_Type = Unsigned32
_TnSonetSdhPpSection3Port_Object = MibTableColumn
tnSonetSdhPpSection3Port = _TnSonetSdhPpSection3Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 3),
    _TnSonetSdhPpSection3Port_Type()
)
tnSonetSdhPpSection3Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection3Port.setStatus("current")
_TnSonetSdhPpSection4Port_Type = Unsigned32
_TnSonetSdhPpSection4Port_Object = MibTableColumn
tnSonetSdhPpSection4Port = _TnSonetSdhPpSection4Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 4),
    _TnSonetSdhPpSection4Port_Type()
)
tnSonetSdhPpSection4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection4Port.setStatus("current")
_TnSonetSdhPpSection5Port_Type = Unsigned32
_TnSonetSdhPpSection5Port_Object = MibTableColumn
tnSonetSdhPpSection5Port = _TnSonetSdhPpSection5Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 5),
    _TnSonetSdhPpSection5Port_Type()
)
tnSonetSdhPpSection5Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection5Port.setStatus("current")
_TnSonetSdhPpSection6Port_Type = Unsigned32
_TnSonetSdhPpSection6Port_Object = MibTableColumn
tnSonetSdhPpSection6Port = _TnSonetSdhPpSection6Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 6),
    _TnSonetSdhPpSection6Port_Type()
)
tnSonetSdhPpSection6Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection6Port.setStatus("current")
_TnSonetSdhPpSection7Port_Type = Unsigned32
_TnSonetSdhPpSection7Port_Object = MibTableColumn
tnSonetSdhPpSection7Port = _TnSonetSdhPpSection7Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 7),
    _TnSonetSdhPpSection7Port_Type()
)
tnSonetSdhPpSection7Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection7Port.setStatus("current")
_TnSonetSdhPpSection8Port_Type = Unsigned32
_TnSonetSdhPpSection8Port_Object = MibTableColumn
tnSonetSdhPpSection8Port = _TnSonetSdhPpSection8Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 8),
    _TnSonetSdhPpSection8Port_Type()
)
tnSonetSdhPpSection8Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection8Port.setStatus("current")
_TnSonetSdhPpSection1IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection1IfType_Object = MibTableColumn
tnSonetSdhPpSection1IfType = _TnSonetSdhPpSection1IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 9),
    _TnSonetSdhPpSection1IfType_Type()
)
tnSonetSdhPpSection1IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection1IfType.setStatus("current")
_TnSonetSdhPpSection2IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection2IfType_Object = MibTableColumn
tnSonetSdhPpSection2IfType = _TnSonetSdhPpSection2IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 10),
    _TnSonetSdhPpSection2IfType_Type()
)
tnSonetSdhPpSection2IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection2IfType.setStatus("current")
_TnSonetSdhPpSection3IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection3IfType_Object = MibTableColumn
tnSonetSdhPpSection3IfType = _TnSonetSdhPpSection3IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 11),
    _TnSonetSdhPpSection3IfType_Type()
)
tnSonetSdhPpSection3IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection3IfType.setStatus("current")
_TnSonetSdhPpSection4IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection4IfType_Object = MibTableColumn
tnSonetSdhPpSection4IfType = _TnSonetSdhPpSection4IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 12),
    _TnSonetSdhPpSection4IfType_Type()
)
tnSonetSdhPpSection4IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection4IfType.setStatus("current")
_TnSonetSdhPpSection5IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection5IfType_Object = MibTableColumn
tnSonetSdhPpSection5IfType = _TnSonetSdhPpSection5IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 13),
    _TnSonetSdhPpSection5IfType_Type()
)
tnSonetSdhPpSection5IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection5IfType.setStatus("current")
_TnSonetSdhPpSection6IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection6IfType_Object = MibTableColumn
tnSonetSdhPpSection6IfType = _TnSonetSdhPpSection6IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 14),
    _TnSonetSdhPpSection6IfType_Type()
)
tnSonetSdhPpSection6IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection6IfType.setStatus("current")
_TnSonetSdhPpSection7IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection7IfType_Object = MibTableColumn
tnSonetSdhPpSection7IfType = _TnSonetSdhPpSection7IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 15),
    _TnSonetSdhPpSection7IfType_Type()
)
tnSonetSdhPpSection7IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection7IfType.setStatus("current")
_TnSonetSdhPpSection8IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection8IfType_Object = MibTableColumn
tnSonetSdhPpSection8IfType = _TnSonetSdhPpSection8IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 16),
    _TnSonetSdhPpSection8IfType_Type()
)
tnSonetSdhPpSection8IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection8IfType.setStatus("current")
_TnPcsSectionCardTable_Object = MibTable
tnPcsSectionCardTable = _TnPcsSectionCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12)
)
if mibBuilder.loadTexts:
    tnPcsSectionCardTable.setStatus("current")
_TnPcsSectionCardEntry_Object = MibTableRow
tnPcsSectionCardEntry = _TnPcsSectionCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1)
)
tnPcsSectionCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPcsSectionCardEntry.setStatus("current")
_TnPcsSection1Port_Type = Unsigned32
_TnPcsSection1Port_Object = MibTableColumn
tnPcsSection1Port = _TnPcsSection1Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 1),
    _TnPcsSection1Port_Type()
)
tnPcsSection1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection1Port.setStatus("current")
_TnPcsSection2Port_Type = Unsigned32
_TnPcsSection2Port_Object = MibTableColumn
tnPcsSection2Port = _TnPcsSection2Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 2),
    _TnPcsSection2Port_Type()
)
tnPcsSection2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection2Port.setStatus("current")
_TnPcsSection3Port_Type = Unsigned32
_TnPcsSection3Port_Object = MibTableColumn
tnPcsSection3Port = _TnPcsSection3Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 3),
    _TnPcsSection3Port_Type()
)
tnPcsSection3Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection3Port.setStatus("current")
_TnPcsSection4Port_Type = Unsigned32
_TnPcsSection4Port_Object = MibTableColumn
tnPcsSection4Port = _TnPcsSection4Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 4),
    _TnPcsSection4Port_Type()
)
tnPcsSection4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection4Port.setStatus("current")
_TnPcsSection5Port_Type = Unsigned32
_TnPcsSection5Port_Object = MibTableColumn
tnPcsSection5Port = _TnPcsSection5Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 5),
    _TnPcsSection5Port_Type()
)
tnPcsSection5Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection5Port.setStatus("current")
_TnPcsSection6Port_Type = Unsigned32
_TnPcsSection6Port_Object = MibTableColumn
tnPcsSection6Port = _TnPcsSection6Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 6),
    _TnPcsSection6Port_Type()
)
tnPcsSection6Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection6Port.setStatus("current")
_TnPcsSection7Port_Type = Unsigned32
_TnPcsSection7Port_Object = MibTableColumn
tnPcsSection7Port = _TnPcsSection7Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 7),
    _TnPcsSection7Port_Type()
)
tnPcsSection7Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection7Port.setStatus("current")
_TnPcsSection8Port_Type = Unsigned32
_TnPcsSection8Port_Object = MibTableColumn
tnPcsSection8Port = _TnPcsSection8Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 8),
    _TnPcsSection8Port_Type()
)
tnPcsSection8Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection8Port.setStatus("current")
_TnPcsSection9Port_Type = Unsigned32
_TnPcsSection9Port_Object = MibTableColumn
tnPcsSection9Port = _TnPcsSection9Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 9),
    _TnPcsSection9Port_Type()
)
tnPcsSection9Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection9Port.setStatus("current")
_TnPcsSection10Port_Type = Unsigned32
_TnPcsSection10Port_Object = MibTableColumn
tnPcsSection10Port = _TnPcsSection10Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 10),
    _TnPcsSection10Port_Type()
)
tnPcsSection10Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection10Port.setStatus("current")
_TnPcsSection1IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection1IfType_Object = MibTableColumn
tnPcsSection1IfType = _TnPcsSection1IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 11),
    _TnPcsSection1IfType_Type()
)
tnPcsSection1IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection1IfType.setStatus("current")
_TnPcsSection2IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection2IfType_Object = MibTableColumn
tnPcsSection2IfType = _TnPcsSection2IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 12),
    _TnPcsSection2IfType_Type()
)
tnPcsSection2IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection2IfType.setStatus("current")
_TnPcsSection3IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection3IfType_Object = MibTableColumn
tnPcsSection3IfType = _TnPcsSection3IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 13),
    _TnPcsSection3IfType_Type()
)
tnPcsSection3IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection3IfType.setStatus("current")
_TnPcsSection4IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection4IfType_Object = MibTableColumn
tnPcsSection4IfType = _TnPcsSection4IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 14),
    _TnPcsSection4IfType_Type()
)
tnPcsSection4IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection4IfType.setStatus("current")
_TnPcsSection5IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection5IfType_Object = MibTableColumn
tnPcsSection5IfType = _TnPcsSection5IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 15),
    _TnPcsSection5IfType_Type()
)
tnPcsSection5IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection5IfType.setStatus("current")
_TnPcsSection6IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection6IfType_Object = MibTableColumn
tnPcsSection6IfType = _TnPcsSection6IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 16),
    _TnPcsSection6IfType_Type()
)
tnPcsSection6IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection6IfType.setStatus("current")
_TnPcsSection7IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection7IfType_Object = MibTableColumn
tnPcsSection7IfType = _TnPcsSection7IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 17),
    _TnPcsSection7IfType_Type()
)
tnPcsSection7IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection7IfType.setStatus("current")
_TnPcsSection8IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection8IfType_Object = MibTableColumn
tnPcsSection8IfType = _TnPcsSection8IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 18),
    _TnPcsSection8IfType_Type()
)
tnPcsSection8IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection8IfType.setStatus("current")
_TnPcsSection9IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection9IfType_Object = MibTableColumn
tnPcsSection9IfType = _TnPcsSection9IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 19),
    _TnPcsSection9IfType_Type()
)
tnPcsSection9IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection9IfType.setStatus("current")
_TnPcsSection10IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection10IfType_Object = MibTableColumn
tnPcsSection10IfType = _TnPcsSection10IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 20),
    _TnPcsSection10IfType_Type()
)
tnPcsSection10IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection10IfType.setStatus("current")
_Tn11dpge12CardTable_Object = MibTable
tn11dpge12CardTable = _Tn11dpge12CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14)
)
if mibBuilder.loadTexts:
    tn11dpge12CardTable.setStatus("current")
_Tn11dpge12CardEntry_Object = MibTableRow
tn11dpge12CardEntry = _Tn11dpge12CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14, 1)
)
tn11dpge12CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn11dpge12CardEntry.setStatus("current")


class _Tn11dpge12CardRateMode_Type(Integer32):
    """Custom type tn11dpge12CardRateMode based on Integer32"""
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
        *(("fullRate", 1),
          ("subRate", 2),
          ("qinqRate", 3))
    )


_Tn11dpge12CardRateMode_Type.__name__ = "Integer32"
_Tn11dpge12CardRateMode_Object = MibTableColumn
tn11dpge12CardRateMode = _Tn11dpge12CardRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14, 1, 1),
    _Tn11dpge12CardRateMode_Type()
)
tn11dpge12CardRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpge12CardRateMode.setStatus("current")
_Tn11dpge12QINQModeTPID_Type = Unsigned32
_Tn11dpge12QINQModeTPID_Object = MibTableColumn
tn11dpge12QINQModeTPID = _Tn11dpge12QINQModeTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14, 1, 2),
    _Tn11dpge12QINQModeTPID_Type()
)
tn11dpge12QINQModeTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpge12QINQModeTPID.setStatus("current")
_TnSfcCardTable_Object = MibTable
tnSfcCardTable = _TnSfcCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 15)
)
if mibBuilder.loadTexts:
    tnSfcCardTable.setStatus("current")
_TnSfcCardEntry_Object = MibTableRow
tnSfcCardEntry = _TnSfcCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 15, 1)
)
tnSfcCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSfcCardEntry.setStatus("current")


class _TnSfcCardFiberMode_Type(Integer32):
    """Custom type tnSfcCardFiberMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoFiber", 1),
          ("oneFiberMux", 2))
    )


_TnSfcCardFiberMode_Type.__name__ = "Integer32"
_TnSfcCardFiberMode_Object = MibTableColumn
tnSfcCardFiberMode = _TnSfcCardFiberMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 15, 1, 1),
    _TnSfcCardFiberMode_Type()
)
tnSfcCardFiberMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSfcCardFiberMode.setStatus("current")
_Tn4dpa4CardTable_Object = MibTable
tn4dpa4CardTable = _Tn4dpa4CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 16)
)
if mibBuilder.loadTexts:
    tn4dpa4CardTable.setStatus("deprecated")
_Tn4dpa4CardEntry_Object = MibTableRow
tn4dpa4CardEntry = _Tn4dpa4CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 16, 1)
)
tn4dpa4CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn4dpa4CardEntry.setStatus("deprecated")


class _Tn4dpa4CardFunctionMode_Type(Integer32):
    """Custom type tn4dpa4CardFunctionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flexMux", 1),
          ("dualTran", 2))
    )


_Tn4dpa4CardFunctionMode_Type.__name__ = "Integer32"
_Tn4dpa4CardFunctionMode_Object = MibTableColumn
tn4dpa4CardFunctionMode = _Tn4dpa4CardFunctionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 16, 1, 1),
    _Tn4dpa4CardFunctionMode_Type()
)
tn4dpa4CardFunctionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn4dpa4CardFunctionMode.setStatus("deprecated")
_TnOpsaCardTable_Object = MibTable
tnOpsaCardTable = _TnOpsaCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 17)
)
if mibBuilder.loadTexts:
    tnOpsaCardTable.setStatus("deprecated")
_TnOpsaCardEntry_Object = MibTableRow
tnOpsaCardEntry = _TnOpsaCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 17, 1)
)
tnOpsaCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnOpsaCardEntry.setStatus("deprecated")


class _TnOpsaProtectionMode_Type(Integer32):
    """Custom type tnOpsaProtectionMode based on Integer32"""
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
        *(("ochp", 1),
          ("olp", 2),
          ("omsp", 3),
          ("otup", 4))
    )


_TnOpsaProtectionMode_Type.__name__ = "Integer32"
_TnOpsaProtectionMode_Object = MibTableColumn
tnOpsaProtectionMode = _TnOpsaProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 17, 1, 1),
    _TnOpsaProtectionMode_Type()
)
tnOpsaProtectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOpsaProtectionMode.setStatus("deprecated")
_Tn11dpe12eCardTable_Object = MibTable
tn11dpe12eCardTable = _Tn11dpe12eCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18)
)
if mibBuilder.loadTexts:
    tn11dpe12eCardTable.setStatus("current")
_Tn11dpe12eCardEntry_Object = MibTableRow
tn11dpe12eCardEntry = _Tn11dpe12eCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1)
)
tn11dpe12eCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn11dpe12eCardEntry.setStatus("current")


class _Tn11dpe12eCardRateMode_Type(Integer32):
    """Custom type tn11dpe12eCardRateMode based on Integer32"""
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
        *(("fullRate", 1),
          ("subRate", 2),
          ("qinqRate", 3))
    )


_Tn11dpe12eCardRateMode_Type.__name__ = "Integer32"
_Tn11dpe12eCardRateMode_Object = MibTableColumn
tn11dpe12eCardRateMode = _Tn11dpe12eCardRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 1),
    _Tn11dpe12eCardRateMode_Type()
)
tn11dpe12eCardRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eCardRateMode.setStatus("current")
_Tn11dpe12eQINQModeTPID1_Type = Unsigned32
_Tn11dpe12eQINQModeTPID1_Object = MibTableColumn
tn11dpe12eQINQModeTPID1 = _Tn11dpe12eQINQModeTPID1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 2),
    _Tn11dpe12eQINQModeTPID1_Type()
)
tn11dpe12eQINQModeTPID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID1.setStatus("current")
_Tn11dpe12eQINQModeTPID2_Type = Unsigned32
_Tn11dpe12eQINQModeTPID2_Object = MibTableColumn
tn11dpe12eQINQModeTPID2 = _Tn11dpe12eQINQModeTPID2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 3),
    _Tn11dpe12eQINQModeTPID2_Type()
)
tn11dpe12eQINQModeTPID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID2.setStatus("current")
_Tn11dpe12eQINQModeTPID3_Type = Unsigned32
_Tn11dpe12eQINQModeTPID3_Object = MibTableColumn
tn11dpe12eQINQModeTPID3 = _Tn11dpe12eQINQModeTPID3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 4),
    _Tn11dpe12eQINQModeTPID3_Type()
)
tn11dpe12eQINQModeTPID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID3.setStatus("current")
_Tn11dpe12eQINQModeTPID4_Type = Unsigned32
_Tn11dpe12eQINQModeTPID4_Object = MibTableColumn
tn11dpe12eQINQModeTPID4 = _Tn11dpe12eQINQModeTPID4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 5),
    _Tn11dpe12eQINQModeTPID4_Type()
)
tn11dpe12eQINQModeTPID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID4.setStatus("current")


class _Tn11dpe12eQINQModeFlowCm_Type(Integer32):
    """Custom type tn11dpe12eQINQModeFlowCm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apspcc", 1),
          ("ccm", 2))
    )


_Tn11dpe12eQINQModeFlowCm_Type.__name__ = "Integer32"
_Tn11dpe12eQINQModeFlowCm_Object = MibTableColumn
tn11dpe12eQINQModeFlowCm = _Tn11dpe12eQINQModeFlowCm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 6),
    _Tn11dpe12eQINQModeFlowCm_Type()
)
tn11dpe12eQINQModeFlowCm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeFlowCm.setStatus("current")
_Tn1dpp24mCardTable_Object = MibTable
tn1dpp24mCardTable = _Tn1dpp24mCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19)
)
if mibBuilder.loadTexts:
    tn1dpp24mCardTable.setStatus("current")
_Tn1dpp24mCardEntry_Object = MibTableRow
tn1dpp24mCardEntry = _Tn1dpp24mCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19, 1)
)
tn1dpp24mCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn1dpp24mCardEntry.setStatus("current")


class _Tn1dpp24mCardFunctionMode_Type(Integer32):
    """Custom type tn1dpp24mCardFunctionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_Tn1dpp24mCardFunctionMode_Type.__name__ = "Integer32"
_Tn1dpp24mCardFunctionMode_Object = MibTableColumn
tn1dpp24mCardFunctionMode = _Tn1dpp24mCardFunctionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19, 1, 1),
    _Tn1dpp24mCardFunctionMode_Type()
)
tn1dpp24mCardFunctionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn1dpp24mCardFunctionMode.setStatus("current")


class _Tn1dpp24mCardImpedance_Type(Integer32):
    """Custom type tn1dpp24mCardImpedance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imp75ohm", 1),
          ("imp120ohm", 2))
    )


_Tn1dpp24mCardImpedance_Type.__name__ = "Integer32"
_Tn1dpp24mCardImpedance_Object = MibTableColumn
tn1dpp24mCardImpedance = _Tn1dpp24mCardImpedance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19, 1, 2),
    _Tn1dpp24mCardImpedance_Type()
)
tn1dpp24mCardImpedance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn1dpp24mCardImpedance.setStatus("current")
_Tn43sca1CardTable_Object = MibTable
tn43sca1CardTable = _Tn43sca1CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 20)
)
if mibBuilder.loadTexts:
    tn43sca1CardTable.setStatus("deprecated")
_Tn43sca1CardEntry_Object = MibTableRow
tn43sca1CardEntry = _Tn43sca1CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 20, 1)
)
tn43sca1CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn43sca1CardEntry.setStatus("deprecated")


class _Tn43sca1CardFunctionMode_Type(Integer32):
    """Custom type tn43sca1CardFunctionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonetSdh", 1),
          ("otu3", 2))
    )


_Tn43sca1CardFunctionMode_Type.__name__ = "Integer32"
_Tn43sca1CardFunctionMode_Object = MibTableColumn
tn43sca1CardFunctionMode = _Tn43sca1CardFunctionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 20, 1, 1),
    _Tn43sca1CardFunctionMode_Type()
)
tn43sca1CardFunctionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn43sca1CardFunctionMode.setStatus("deprecated")
_TnOpsCardTable_Object = MibTable
tnOpsCardTable = _TnOpsCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 21)
)
if mibBuilder.loadTexts:
    tnOpsCardTable.setStatus("current")
_TnOpsCardEntry_Object = MibTableRow
tnOpsCardEntry = _TnOpsCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 21, 1)
)
tnOpsCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnOpsCardEntry.setStatus("current")


class _TnOpsCardProtectionMode_Type(Integer32):
    """Custom type tnOpsCardProtectionMode based on Integer32"""
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
        *(("ochp", 1),
          ("olp", 2),
          ("omsp", 3),
          ("otup", 4))
    )


_TnOpsCardProtectionMode_Type.__name__ = "Integer32"
_TnOpsCardProtectionMode_Object = MibTableColumn
tnOpsCardProtectionMode = _TnOpsCardProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 21, 1, 1),
    _TnOpsCardProtectionMode_Type()
)
tnOpsCardProtectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOpsCardProtectionMode.setStatus("current")
_Tn11dpe12aCardTable_Object = MibTable
tn11dpe12aCardTable = _Tn11dpe12aCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22)
)
if mibBuilder.loadTexts:
    tn11dpe12aCardTable.setStatus("current")
_Tn11dpe12aCardEntry_Object = MibTableRow
tn11dpe12aCardEntry = _Tn11dpe12aCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1)
)
tn11dpe12aCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn11dpe12aCardEntry.setStatus("current")


class _Tn11dpe12aCardRateMode_Type(Integer32):
    """Custom type tn11dpe12aCardRateMode based on Integer32"""
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
        *(("fullRate", 1),
          ("subRate", 2),
          ("qinqRate", 3))
    )


_Tn11dpe12aCardRateMode_Type.__name__ = "Integer32"
_Tn11dpe12aCardRateMode_Object = MibTableColumn
tn11dpe12aCardRateMode = _Tn11dpe12aCardRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 1),
    _Tn11dpe12aCardRateMode_Type()
)
tn11dpe12aCardRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardRateMode.setStatus("current")
_Tn11dpe12aCardQINQModeTPID1_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID1_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID1 = _Tn11dpe12aCardQINQModeTPID1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 2),
    _Tn11dpe12aCardQINQModeTPID1_Type()
)
tn11dpe12aCardQINQModeTPID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID1.setStatus("current")
_Tn11dpe12aCardQINQModeTPID2_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID2_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID2 = _Tn11dpe12aCardQINQModeTPID2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 3),
    _Tn11dpe12aCardQINQModeTPID2_Type()
)
tn11dpe12aCardQINQModeTPID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID2.setStatus("current")
_Tn11dpe12aCardQINQModeTPID3_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID3_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID3 = _Tn11dpe12aCardQINQModeTPID3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 4),
    _Tn11dpe12aCardQINQModeTPID3_Type()
)
tn11dpe12aCardQINQModeTPID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID3.setStatus("current")
_Tn11dpe12aCardQINQModeTPID4_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID4_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID4 = _Tn11dpe12aCardQINQModeTPID4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 5),
    _Tn11dpe12aCardQINQModeTPID4_Type()
)
tn11dpe12aCardQINQModeTPID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID4.setStatus("current")


class _Tn11dpe12aCardLBMInterval_Type(Unsigned32):
    """Custom type tn11dpe12aCardLBMInterval based on Unsigned32"""
    defaultValue = 1000


_Tn11dpe12aCardLBMInterval_Type.__name__ = "Unsigned32"
_Tn11dpe12aCardLBMInterval_Object = MibTableColumn
tn11dpe12aCardLBMInterval = _Tn11dpe12aCardLBMInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 6),
    _Tn11dpe12aCardLBMInterval_Type()
)
tn11dpe12aCardLBMInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBMInterval.setStatus("current")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBMInterval.setUnits("ms")


class _Tn11dpe12aCardLBRTimeout_Type(Unsigned32):
    """Custom type tn11dpe12aCardLBRTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Tn11dpe12aCardLBRTimeout_Type.__name__ = "Unsigned32"
_Tn11dpe12aCardLBRTimeout_Object = MibTableColumn
tn11dpe12aCardLBRTimeout = _Tn11dpe12aCardLBRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 7),
    _Tn11dpe12aCardLBRTimeout_Type()
)
tn11dpe12aCardLBRTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBRTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBRTimeout.setUnits("seconds")


class _Tn11dpe12aCardFlowCm_Type(Integer32):
    """Custom type tn11dpe12aCardFlowCm based on Integer32"""
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
        *(("apspcc", 1),
          ("ccm", 2),
          ("csf", 3))
    )


_Tn11dpe12aCardFlowCm_Type.__name__ = "Integer32"
_Tn11dpe12aCardFlowCm_Object = MibTableColumn
tn11dpe12aCardFlowCm = _Tn11dpe12aCardFlowCm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 8),
    _Tn11dpe12aCardFlowCm_Type()
)
tn11dpe12aCardFlowCm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardFlowCm.setStatus("current")


class _Tn11dpe12aCardSLRTimeout_Type(Unsigned32):
    """Custom type tn11dpe12aCardSLRTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Tn11dpe12aCardSLRTimeout_Type.__name__ = "Unsigned32"
_Tn11dpe12aCardSLRTimeout_Object = MibTableColumn
tn11dpe12aCardSLRTimeout = _Tn11dpe12aCardSLRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 9),
    _Tn11dpe12aCardSLRTimeout_Type()
)
tn11dpe12aCardSLRTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardSLRTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tn11dpe12aCardSLRTimeout.setUnits("seconds")


class _Tn11dpe12aCardCrossPackServiceSupported_Type(Integer32):
    """Custom type tn11dpe12aCardCrossPackServiceSupported based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Tn11dpe12aCardCrossPackServiceSupported_Type.__name__ = "Integer32"
_Tn11dpe12aCardCrossPackServiceSupported_Object = MibTableColumn
tn11dpe12aCardCrossPackServiceSupported = _Tn11dpe12aCardCrossPackServiceSupported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 10),
    _Tn11dpe12aCardCrossPackServiceSupported_Type()
)
tn11dpe12aCardCrossPackServiceSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardCrossPackServiceSupported.setStatus("current")
_TnCardFunctionModeTable_Object = MibTable
tnCardFunctionModeTable = _TnCardFunctionModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 23)
)
if mibBuilder.loadTexts:
    tnCardFunctionModeTable.setStatus("current")
_TnCardFunctionModeEntry_Object = MibTableRow
tnCardFunctionModeEntry = _TnCardFunctionModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 23, 1)
)
tnCardFunctionModeEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCardFunctionModeEntry.setStatus("current")


class _TnCardFunctionMode_Type(Integer32):
    """Custom type tnCardFunctionMode based on Integer32"""
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
        *(("flexMux", 1),
          ("dualTran", 2),
          ("sonetSdh", 3),
          ("otu3", 4),
          ("hundredGbe", 5),
          ("otu4", 6))
    )


_TnCardFunctionMode_Type.__name__ = "Integer32"
_TnCardFunctionMode_Object = MibTableColumn
tnCardFunctionMode = _TnCardFunctionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 23, 1, 1),
    _TnCardFunctionMode_Type()
)
tnCardFunctionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardFunctionMode.setStatus("current")
_Tn112pdm11CardTable_Object = MibTable
tn112pdm11CardTable = _Tn112pdm11CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24)
)
if mibBuilder.loadTexts:
    tn112pdm11CardTable.setStatus("current")
_Tn112pdm11CardEntry_Object = MibTableRow
tn112pdm11CardEntry = _Tn112pdm11CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24, 1)
)
tn112pdm11CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn112pdm11CardEntry.setStatus("current")


class _Tn112pdm11CardMaxDMNumbers_Type(Unsigned32):
    """Custom type tn112pdm11CardMaxDMNumbers based on Unsigned32"""
    defaultValue = 1


_Tn112pdm11CardMaxDMNumbers_Type.__name__ = "Unsigned32"
_Tn112pdm11CardMaxDMNumbers_Object = MibTableColumn
tn112pdm11CardMaxDMNumbers = _Tn112pdm11CardMaxDMNumbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24, 1, 1),
    _Tn112pdm11CardMaxDMNumbers_Type()
)
tn112pdm11CardMaxDMNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112pdm11CardMaxDMNumbers.setStatus("current")


class _Tn112pdm11CardUsedDMNumbers_Type(Unsigned32):
    """Custom type tn112pdm11CardUsedDMNumbers based on Unsigned32"""
    defaultValue = 0


_Tn112pdm11CardUsedDMNumbers_Type.__name__ = "Unsigned32"
_Tn112pdm11CardUsedDMNumbers_Object = MibTableColumn
tn112pdm11CardUsedDMNumbers = _Tn112pdm11CardUsedDMNumbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24, 1, 2),
    _Tn112pdm11CardUsedDMNumbers_Type()
)
tn112pdm11CardUsedDMNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112pdm11CardUsedDMNumbers.setStatus("current")
_TnPtpctlCardAttributeTotal_Type = Integer32
_TnPtpctlCardAttributeTotal_Object = MibScalar
tnPtpctlCardAttributeTotal = _TnPtpctlCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 25),
    _TnPtpctlCardAttributeTotal_Type()
)
tnPtpctlCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardAttributeTotal.setStatus("current")
_TnPtpctlCardTable_Object = MibTable
tnPtpctlCardTable = _TnPtpctlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26)
)
if mibBuilder.loadTexts:
    tnPtpctlCardTable.setStatus("current")
_TnPtpctlCardEntry_Object = MibTableRow
tnPtpctlCardEntry = _TnPtpctlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1)
)
tnPtpctlCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPtpctlCardEntry.setStatus("current")
_TnPtpctlCardEqpsLEDColor_Type = TropicLEDColorType
_TnPtpctlCardEqpsLEDColor_Object = MibTableColumn
tnPtpctlCardEqpsLEDColor = _TnPtpctlCardEqpsLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 1),
    _TnPtpctlCardEqpsLEDColor_Type()
)
tnPtpctlCardEqpsLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardEqpsLEDColor.setStatus("current")
_TnPtpctlCardEqpsLEDState_Type = TropicLEDStateType
_TnPtpctlCardEqpsLEDState_Object = MibTableColumn
tnPtpctlCardEqpsLEDState = _TnPtpctlCardEqpsLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 2),
    _TnPtpctlCardEqpsLEDState_Type()
)
tnPtpctlCardEqpsLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardEqpsLEDState.setStatus("current")
_TnPtpctlCardPtpLEDColor_Type = TropicLEDColorType
_TnPtpctlCardPtpLEDColor_Object = MibTableColumn
tnPtpctlCardPtpLEDColor = _TnPtpctlCardPtpLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 3),
    _TnPtpctlCardPtpLEDColor_Type()
)
tnPtpctlCardPtpLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardPtpLEDColor.setStatus("current")
_TnPtpctlCardPtpLEDState_Type = TropicLEDStateType
_TnPtpctlCardPtpLEDState_Object = MibTableColumn
tnPtpctlCardPtpLEDState = _TnPtpctlCardPtpLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 4),
    _TnPtpctlCardPtpLEDState_Type()
)
tnPtpctlCardPtpLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardPtpLEDState.setStatus("current")
_TnWtocmaCardAttributeTotal_Type = Integer32
_TnWtocmaCardAttributeTotal_Object = MibScalar
tnWtocmaCardAttributeTotal = _TnWtocmaCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 27),
    _TnWtocmaCardAttributeTotal_Type()
)
tnWtocmaCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmaCardAttributeTotal.setStatus("current")
_TnWtocmaCardTable_Object = MibTable
tnWtocmaCardTable = _TnWtocmaCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28)
)
if mibBuilder.loadTexts:
    tnWtocmaCardTable.setStatus("current")
_TnWtocmaCardEntry_Object = MibTableRow
tnWtocmaCardEntry = _TnWtocmaCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1)
)
tnWtocmaCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnWtocmaCardEntry.setStatus("current")


class _TnWtocmaCardOsnrScan_Type(TnCommand):
    """Custom type tnWtocmaCardOsnrScan based on TnCommand"""
    defaultValue = 1


_TnWtocmaCardOsnrScan_Type.__name__ = "TnCommand"
_TnWtocmaCardOsnrScan_Object = MibTableColumn
tnWtocmaCardOsnrScan = _TnWtocmaCardOsnrScan_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 1),
    _TnWtocmaCardOsnrScan_Type()
)
tnWtocmaCardOsnrScan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtocmaCardOsnrScan.setStatus("current")


class _TnWtocmaCardOsnrScanAbort_Type(TnCommand):
    """Custom type tnWtocmaCardOsnrScanAbort based on TnCommand"""
    defaultValue = 1


_TnWtocmaCardOsnrScanAbort_Type.__name__ = "TnCommand"
_TnWtocmaCardOsnrScanAbort_Object = MibTableColumn
tnWtocmaCardOsnrScanAbort = _TnWtocmaCardOsnrScanAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 2),
    _TnWtocmaCardOsnrScanAbort_Type()
)
tnWtocmaCardOsnrScanAbort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtocmaCardOsnrScanAbort.setStatus("current")


class _TnWtocmaCardOsnrScanStatus_Type(Integer32):
    """Custom type tnWtocmaCardOsnrScanStatus based on Integer32"""
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
        *(("notInProgress", 1),
          ("inProgress", 2),
          ("waiting", 3))
    )


_TnWtocmaCardOsnrScanStatus_Type.__name__ = "Integer32"
_TnWtocmaCardOsnrScanStatus_Object = MibTableColumn
tnWtocmaCardOsnrScanStatus = _TnWtocmaCardOsnrScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 3),
    _TnWtocmaCardOsnrScanStatus_Type()
)
tnWtocmaCardOsnrScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmaCardOsnrScanStatus.setStatus("current")


class _TnWtocmaCardDspState_Type(Integer32):
    """Custom type tnWtocmaCardDspState based on Integer32"""
    defaultValue = 1

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
        *(("newChan", 1),
          ("osnr", 2),
          ("osnrOnDemand", 3),
          ("misKeyedChan", 4),
          ("idle", 5))
    )


_TnWtocmaCardDspState_Type.__name__ = "Integer32"
_TnWtocmaCardDspState_Object = MibTableColumn
tnWtocmaCardDspState = _TnWtocmaCardDspState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 4),
    _TnWtocmaCardDspState_Type()
)
tnWtocmaCardDspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmaCardDspState.setStatus("current")
_TnCruCardAttributeTotal_Type = Integer32
_TnCruCardAttributeTotal_Object = MibScalar
tnCruCardAttributeTotal = _TnCruCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 29),
    _TnCruCardAttributeTotal_Type()
)
tnCruCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardAttributeTotal.setStatus("current")
_TnCruCardTable_Object = MibTable
tnCruCardTable = _TnCruCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30)
)
if mibBuilder.loadTexts:
    tnCruCardTable.setStatus("current")
_TnCruCardEntry_Object = MibTableRow
tnCruCardEntry = _TnCruCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1)
)
tnCruCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCruCardEntry.setStatus("current")


class _TnCruCardActivityState_Type(Integer32):
    """Custom type tnCruCardActivityState based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("unequipped", 2),
          ("active", 3),
          ("standbyTrackingToActive", 4),
          ("standbyNotTrackingToActive", 5))
    )


_TnCruCardActivityState_Type.__name__ = "Integer32"
_TnCruCardActivityState_Object = MibTableColumn
tnCruCardActivityState = _TnCruCardActivityState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1, 1),
    _TnCruCardActivityState_Type()
)
tnCruCardActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardActivityState.setStatus("current")
_TnCruCardEqpsLEDColor_Type = TropicLEDColorType
_TnCruCardEqpsLEDColor_Object = MibTableColumn
tnCruCardEqpsLEDColor = _TnCruCardEqpsLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1, 2),
    _TnCruCardEqpsLEDColor_Type()
)
tnCruCardEqpsLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardEqpsLEDColor.setStatus("current")
_TnCruCardEqpsLEDState_Type = TropicLEDStateType
_TnCruCardEqpsLEDState_Object = MibTableColumn
tnCruCardEqpsLEDState = _TnCruCardEqpsLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1, 3),
    _TnCruCardEqpsLEDState_Type()
)
tnCruCardEqpsLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardEqpsLEDState.setStatus("current")

# Managed Objects groups

tnOpticalCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 1)
)
tnOpticalCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnOpticalCardTotal")
)
if mibBuilder.loadTexts:
    tnOpticalCardScalarsGroup.setStatus("current")

tnDcmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 4)
)
tnDcmCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnDcmCardProgrammedCompensationDistance"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardPresentCompensationDistance"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardSize"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardFiberType"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardAverageInsertionLoss"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardInsertionLossSlope"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardAverageInsertionLossPad"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardInsertionLossSlopePad"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardTotalDispTilt"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardDispFiberLength"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardPMD"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardProvisionedFiberType"))
)
if mibBuilder.loadTexts:
    tnDcmCardGroup.setStatus("current")

tnPowerControlCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 8)
)
tnPowerControlCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardCapabilityProgrammed"),
        ("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardCapabilityPresent"),
        ("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardCapabilityInUse"))
)
if mibBuilder.loadTexts:
    tnPowerControlCardGroup.setStatus("current")

tnWssCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 9)
)
tnWssCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnWssCardAddPathTargetPower"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAddPathEgressPower"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAddPathTotalChannel"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardReservedDegree"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardLnsEnable"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardLnsPower"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAdBlockLevelAdd"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAdBlockLevelDrop"))
)
if mibBuilder.loadTexts:
    tnWssCardGroup.setStatus("current")

tnSfdCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 10)
)
tnSfdCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnSfdCardAverageMuxInsertionLoss"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfdCardAverageDemuxInsertionLoss"))
)
if mibBuilder.loadTexts:
    tnSfdCardGroup.setStatus("current")

tnSonetSdhPpSectionCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 11)
)
tnSonetSdhPpSectionCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection1Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection2Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection3Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection4Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection5Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection6Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection7Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection8Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection1IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection2IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection3IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection4IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection5IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection6IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection7IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection8IfType"))
)
if mibBuilder.loadTexts:
    tnSonetSdhPpSectionCardGroup.setStatus("current")

tnPcsSectionCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 12)
)
tnPcsSectionCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnPcsSection1Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection2Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection3Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection4Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection5Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection6Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection7Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection8Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection9Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection10Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection1IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection2IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection3IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection4IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection5IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection6IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection7IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection8IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection9IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection10IfType"))
)
if mibBuilder.loadTexts:
    tnPcsSectionCardGroup.setStatus("current")

tn11dpge12CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 14)
)
tn11dpge12CardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn11dpge12CardRateMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpge12QINQModeTPID"))
)
if mibBuilder.loadTexts:
    tn11dpge12CardGroup.setStatus("current")

tnSfcCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 15)
)
tnSfcCardGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnSfcCardFiberMode")
)
if mibBuilder.loadTexts:
    tnSfcCardGroup.setStatus("current")

tn4dpa4CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 16)
)
tn4dpa4CardGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tn4dpa4CardFunctionMode")
)
if mibBuilder.loadTexts:
    tn4dpa4CardGroup.setStatus("deprecated")

tnOpsaCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 17)
)
tnOpsaCardGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnOpsaProtectionMode")
)
if mibBuilder.loadTexts:
    tnOpsaCardGroup.setStatus("deprecated")

tn11dpe12eCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 18)
)
tn11dpe12eCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn11dpe12eCardRateMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID1"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID2"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID3"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID4"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeFlowCm"))
)
if mibBuilder.loadTexts:
    tn11dpe12eCardGroup.setStatus("current")

tn1dpp24mCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 19)
)
tn1dpp24mCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn1dpp24mCardFunctionMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn1dpp24mCardImpedance"))
)
if mibBuilder.loadTexts:
    tn1dpp24mCardGroup.setStatus("current")

tn43sca1CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 20)
)
tn43sca1CardGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tn43sca1CardFunctionMode")
)
if mibBuilder.loadTexts:
    tn43sca1CardGroup.setStatus("deprecated")

tnOpsCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 21)
)
tnOpsCardGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnOpsCardProtectionMode")
)
if mibBuilder.loadTexts:
    tnOpsCardGroup.setStatus("current")

tn11dpe12aCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 22)
)
tn11dpe12aCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardRateMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID1"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID2"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID3"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID4"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardLBMInterval"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardLBRTimeout"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardFlowCm"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardSLRTimeout"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardCrossPackServiceSupported"))
)
if mibBuilder.loadTexts:
    tn11dpe12aCardGroup.setStatus("current")

tnCardFunctionModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 23)
)
tnCardFunctionModeGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnCardFunctionMode")
)
if mibBuilder.loadTexts:
    tnCardFunctionModeGroup.setStatus("current")

tn112pdm11CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 24)
)
tn112pdm11CardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn112pdm11CardMaxDMNumbers"),
        ("TROPIC-OPTICALCARD-MIB", "tn112pdm11CardUsedDMNumbers"))
)
if mibBuilder.loadTexts:
    tn112pdm11CardGroup.setStatus("current")

tnPtpctlCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 25)
)
tnPtpctlCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPtpctlCardScalarsGroup.setStatus("current")

tnPtpctlCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 26)
)
tnPtpctlCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardEqpsLEDColor"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardEqpsLEDState"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardPtpLEDColor"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardPtpLEDState"))
)
if mibBuilder.loadTexts:
    tnPtpctlCardGroup.setStatus("current")

tnWtocmaCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 27)
)
tnWtocmaCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnWtocmaCardScalarsGroup.setStatus("current")

tnWtocmaCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 28)
)
tnWtocmaCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardOsnrScan"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardOsnrScanAbort"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardOsnrScanStatus"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardDspState"))
)
if mibBuilder.loadTexts:
    tnWtocmaCardGroup.setStatus("current")

tnCruCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 29)
)
tnCruCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnCruCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnCruCardScalarsGroup.setStatus("current")

tnCruCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 30)
)
tnCruCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnCruCardActivityState"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardEqpsLEDColor"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardEqpsLEDState"))
)
if mibBuilder.loadTexts:
    tnCruCardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnOpticalCardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 2, 1)
)
tnOpticalCardCompliance.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnOpticalCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfdCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSectionCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSectionCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpge12CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfcCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn4dpa4CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnOpsaCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn1dpp24mCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn43sca1CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnOpsCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCardFunctionModeGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn112pdm11CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardGroup"))
)
if mibBuilder.loadTexts:
    tnOpticalCardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-OPTICALCARD-MIB",
    **{"AluWdmSonetSdhPpSectionIfType": AluWdmSonetSdhPpSectionIfType,
       "AluWdmPcsSectionIfType": AluWdmPcsSectionIfType,
       "tnOpticalCardMibModule": tnOpticalCardMibModule,
       "tnOpticalCardConf": tnOpticalCardConf,
       "tnOpticalCardGroups": tnOpticalCardGroups,
       "tnOpticalCardScalarsGroup": tnOpticalCardScalarsGroup,
       "tnDcmCardGroup": tnDcmCardGroup,
       "tnPowerControlCardGroup": tnPowerControlCardGroup,
       "tnWssCardGroup": tnWssCardGroup,
       "tnSfdCardGroup": tnSfdCardGroup,
       "tnSonetSdhPpSectionCardGroup": tnSonetSdhPpSectionCardGroup,
       "tnPcsSectionCardGroup": tnPcsSectionCardGroup,
       "tn11dpge12CardGroup": tn11dpge12CardGroup,
       "tnSfcCardGroup": tnSfcCardGroup,
       "tn4dpa4CardGroup": tn4dpa4CardGroup,
       "tnOpsaCardGroup": tnOpsaCardGroup,
       "tn11dpe12eCardGroup": tn11dpe12eCardGroup,
       "tn1dpp24mCardGroup": tn1dpp24mCardGroup,
       "tn43sca1CardGroup": tn43sca1CardGroup,
       "tnOpsCardGroup": tnOpsCardGroup,
       "tn11dpe12aCardGroup": tn11dpe12aCardGroup,
       "tnCardFunctionModeGroup": tnCardFunctionModeGroup,
       "tn112pdm11CardGroup": tn112pdm11CardGroup,
       "tnPtpctlCardScalarsGroup": tnPtpctlCardScalarsGroup,
       "tnPtpctlCardGroup": tnPtpctlCardGroup,
       "tnWtocmaCardScalarsGroup": tnWtocmaCardScalarsGroup,
       "tnWtocmaCardGroup": tnWtocmaCardGroup,
       "tnCruCardScalarsGroup": tnCruCardScalarsGroup,
       "tnCruCardGroup": tnCruCardGroup,
       "tnOpticalCardCompliances": tnOpticalCardCompliances,
       "tnOpticalCardCompliance": tnOpticalCardCompliance,
       "tnOpticalCardObjs": tnOpticalCardObjs,
       "tnOpticalCardTotal": tnOpticalCardTotal,
       "tnDcmCardTable": tnDcmCardTable,
       "tnDcmCardEntry": tnDcmCardEntry,
       "tnDcmCardProgrammedCompensationDistance": tnDcmCardProgrammedCompensationDistance,
       "tnDcmCardPresentCompensationDistance": tnDcmCardPresentCompensationDistance,
       "tnDcmCardSize": tnDcmCardSize,
       "tnDcmCardFiberType": tnDcmCardFiberType,
       "tnDcmCardAverageInsertionLoss": tnDcmCardAverageInsertionLoss,
       "tnDcmCardInsertionLossSlope": tnDcmCardInsertionLossSlope,
       "tnDcmCardAverageInsertionLossPad": tnDcmCardAverageInsertionLossPad,
       "tnDcmCardInsertionLossSlopePad": tnDcmCardInsertionLossSlopePad,
       "tnDcmCardTotalDispTilt": tnDcmCardTotalDispTilt,
       "tnDcmCardDispFiberLength": tnDcmCardDispFiberLength,
       "tnDcmCardPMD": tnDcmCardPMD,
       "tnDcmCardProvisionedFiberType": tnDcmCardProvisionedFiberType,
       "tnPowerControlCardTable": tnPowerControlCardTable,
       "tnPowerControlCardEntry": tnPowerControlCardEntry,
       "tnPowerControlCardCapabilityProgrammed": tnPowerControlCardCapabilityProgrammed,
       "tnPowerControlCardCapabilityPresent": tnPowerControlCardCapabilityPresent,
       "tnPowerControlCardCapabilityInUse": tnPowerControlCardCapabilityInUse,
       "tnWssCardTable": tnWssCardTable,
       "tnWssCardEntry": tnWssCardEntry,
       "tnWssCardAddPathTargetPower": tnWssCardAddPathTargetPower,
       "tnWssCardAddPathEgressPower": tnWssCardAddPathEgressPower,
       "tnWssCardAddPathTotalChannel": tnWssCardAddPathTotalChannel,
       "tnWssCardReservedDegree": tnWssCardReservedDegree,
       "tnWssCardLnsEnable": tnWssCardLnsEnable,
       "tnWssCardLnsPower": tnWssCardLnsPower,
       "tnWssCardAdBlockLevelAdd": tnWssCardAdBlockLevelAdd,
       "tnWssCardAdBlockLevelDrop": tnWssCardAdBlockLevelDrop,
       "tnSfdCardTable": tnSfdCardTable,
       "tnSfdCardEntry": tnSfdCardEntry,
       "tnSfdCardAverageMuxInsertionLoss": tnSfdCardAverageMuxInsertionLoss,
       "tnSfdCardAverageDemuxInsertionLoss": tnSfdCardAverageDemuxInsertionLoss,
       "tnSonetSdhPpSectionCardTable": tnSonetSdhPpSectionCardTable,
       "tnSonetSdhPpSectionCardEntry": tnSonetSdhPpSectionCardEntry,
       "tnSonetSdhPpSection1Port": tnSonetSdhPpSection1Port,
       "tnSonetSdhPpSection2Port": tnSonetSdhPpSection2Port,
       "tnSonetSdhPpSection3Port": tnSonetSdhPpSection3Port,
       "tnSonetSdhPpSection4Port": tnSonetSdhPpSection4Port,
       "tnSonetSdhPpSection5Port": tnSonetSdhPpSection5Port,
       "tnSonetSdhPpSection6Port": tnSonetSdhPpSection6Port,
       "tnSonetSdhPpSection7Port": tnSonetSdhPpSection7Port,
       "tnSonetSdhPpSection8Port": tnSonetSdhPpSection8Port,
       "tnSonetSdhPpSection1IfType": tnSonetSdhPpSection1IfType,
       "tnSonetSdhPpSection2IfType": tnSonetSdhPpSection2IfType,
       "tnSonetSdhPpSection3IfType": tnSonetSdhPpSection3IfType,
       "tnSonetSdhPpSection4IfType": tnSonetSdhPpSection4IfType,
       "tnSonetSdhPpSection5IfType": tnSonetSdhPpSection5IfType,
       "tnSonetSdhPpSection6IfType": tnSonetSdhPpSection6IfType,
       "tnSonetSdhPpSection7IfType": tnSonetSdhPpSection7IfType,
       "tnSonetSdhPpSection8IfType": tnSonetSdhPpSection8IfType,
       "tnPcsSectionCardTable": tnPcsSectionCardTable,
       "tnPcsSectionCardEntry": tnPcsSectionCardEntry,
       "tnPcsSection1Port": tnPcsSection1Port,
       "tnPcsSection2Port": tnPcsSection2Port,
       "tnPcsSection3Port": tnPcsSection3Port,
       "tnPcsSection4Port": tnPcsSection4Port,
       "tnPcsSection5Port": tnPcsSection5Port,
       "tnPcsSection6Port": tnPcsSection6Port,
       "tnPcsSection7Port": tnPcsSection7Port,
       "tnPcsSection8Port": tnPcsSection8Port,
       "tnPcsSection9Port": tnPcsSection9Port,
       "tnPcsSection10Port": tnPcsSection10Port,
       "tnPcsSection1IfType": tnPcsSection1IfType,
       "tnPcsSection2IfType": tnPcsSection2IfType,
       "tnPcsSection3IfType": tnPcsSection3IfType,
       "tnPcsSection4IfType": tnPcsSection4IfType,
       "tnPcsSection5IfType": tnPcsSection5IfType,
       "tnPcsSection6IfType": tnPcsSection6IfType,
       "tnPcsSection7IfType": tnPcsSection7IfType,
       "tnPcsSection8IfType": tnPcsSection8IfType,
       "tnPcsSection9IfType": tnPcsSection9IfType,
       "tnPcsSection10IfType": tnPcsSection10IfType,
       "tn11dpge12CardTable": tn11dpge12CardTable,
       "tn11dpge12CardEntry": tn11dpge12CardEntry,
       "tn11dpge12CardRateMode": tn11dpge12CardRateMode,
       "tn11dpge12QINQModeTPID": tn11dpge12QINQModeTPID,
       "tnSfcCardTable": tnSfcCardTable,
       "tnSfcCardEntry": tnSfcCardEntry,
       "tnSfcCardFiberMode": tnSfcCardFiberMode,
       "tn4dpa4CardTable": tn4dpa4CardTable,
       "tn4dpa4CardEntry": tn4dpa4CardEntry,
       "tn4dpa4CardFunctionMode": tn4dpa4CardFunctionMode,
       "tnOpsaCardTable": tnOpsaCardTable,
       "tnOpsaCardEntry": tnOpsaCardEntry,
       "tnOpsaProtectionMode": tnOpsaProtectionMode,
       "tn11dpe12eCardTable": tn11dpe12eCardTable,
       "tn11dpe12eCardEntry": tn11dpe12eCardEntry,
       "tn11dpe12eCardRateMode": tn11dpe12eCardRateMode,
       "tn11dpe12eQINQModeTPID1": tn11dpe12eQINQModeTPID1,
       "tn11dpe12eQINQModeTPID2": tn11dpe12eQINQModeTPID2,
       "tn11dpe12eQINQModeTPID3": tn11dpe12eQINQModeTPID3,
       "tn11dpe12eQINQModeTPID4": tn11dpe12eQINQModeTPID4,
       "tn11dpe12eQINQModeFlowCm": tn11dpe12eQINQModeFlowCm,
       "tn1dpp24mCardTable": tn1dpp24mCardTable,
       "tn1dpp24mCardEntry": tn1dpp24mCardEntry,
       "tn1dpp24mCardFunctionMode": tn1dpp24mCardFunctionMode,
       "tn1dpp24mCardImpedance": tn1dpp24mCardImpedance,
       "tn43sca1CardTable": tn43sca1CardTable,
       "tn43sca1CardEntry": tn43sca1CardEntry,
       "tn43sca1CardFunctionMode": tn43sca1CardFunctionMode,
       "tnOpsCardTable": tnOpsCardTable,
       "tnOpsCardEntry": tnOpsCardEntry,
       "tnOpsCardProtectionMode": tnOpsCardProtectionMode,
       "tn11dpe12aCardTable": tn11dpe12aCardTable,
       "tn11dpe12aCardEntry": tn11dpe12aCardEntry,
       "tn11dpe12aCardRateMode": tn11dpe12aCardRateMode,
       "tn11dpe12aCardQINQModeTPID1": tn11dpe12aCardQINQModeTPID1,
       "tn11dpe12aCardQINQModeTPID2": tn11dpe12aCardQINQModeTPID2,
       "tn11dpe12aCardQINQModeTPID3": tn11dpe12aCardQINQModeTPID3,
       "tn11dpe12aCardQINQModeTPID4": tn11dpe12aCardQINQModeTPID4,
       "tn11dpe12aCardLBMInterval": tn11dpe12aCardLBMInterval,
       "tn11dpe12aCardLBRTimeout": tn11dpe12aCardLBRTimeout,
       "tn11dpe12aCardFlowCm": tn11dpe12aCardFlowCm,
       "tn11dpe12aCardSLRTimeout": tn11dpe12aCardSLRTimeout,
       "tn11dpe12aCardCrossPackServiceSupported": tn11dpe12aCardCrossPackServiceSupported,
       "tnCardFunctionModeTable": tnCardFunctionModeTable,
       "tnCardFunctionModeEntry": tnCardFunctionModeEntry,
       "tnCardFunctionMode": tnCardFunctionMode,
       "tn112pdm11CardTable": tn112pdm11CardTable,
       "tn112pdm11CardEntry": tn112pdm11CardEntry,
       "tn112pdm11CardMaxDMNumbers": tn112pdm11CardMaxDMNumbers,
       "tn112pdm11CardUsedDMNumbers": tn112pdm11CardUsedDMNumbers,
       "tnPtpctlCardAttributeTotal": tnPtpctlCardAttributeTotal,
       "tnPtpctlCardTable": tnPtpctlCardTable,
       "tnPtpctlCardEntry": tnPtpctlCardEntry,
       "tnPtpctlCardEqpsLEDColor": tnPtpctlCardEqpsLEDColor,
       "tnPtpctlCardEqpsLEDState": tnPtpctlCardEqpsLEDState,
       "tnPtpctlCardPtpLEDColor": tnPtpctlCardPtpLEDColor,
       "tnPtpctlCardPtpLEDState": tnPtpctlCardPtpLEDState,
       "tnWtocmaCardAttributeTotal": tnWtocmaCardAttributeTotal,
       "tnWtocmaCardTable": tnWtocmaCardTable,
       "tnWtocmaCardEntry": tnWtocmaCardEntry,
       "tnWtocmaCardOsnrScan": tnWtocmaCardOsnrScan,
       "tnWtocmaCardOsnrScanAbort": tnWtocmaCardOsnrScanAbort,
       "tnWtocmaCardOsnrScanStatus": tnWtocmaCardOsnrScanStatus,
       "tnWtocmaCardDspState": tnWtocmaCardDspState,
       "tnCruCardAttributeTotal": tnCruCardAttributeTotal,
       "tnCruCardTable": tnCruCardTable,
       "tnCruCardEntry": tnCruCardEntry,
       "tnCruCardActivityState": tnCruCardActivityState,
       "tnCruCardEqpsLEDColor": tnCruCardEqpsLEDColor,
       "tnCruCardEqpsLEDState": tnCruCardEqpsLEDState}
)
