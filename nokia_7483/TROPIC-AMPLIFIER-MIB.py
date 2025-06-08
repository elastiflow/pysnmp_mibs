# SNMP MIB module (TROPIC-AMPLIFIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-AMPLIFIER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:37 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tnAmplifierMIB,
 tnCardModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnAmplifierMIB",
    "tnCardModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(TnCommand,) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCommand")


# MODULE-IDENTITY

tnAmplifierMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tnAmplifierMibModule.setRevisions(
        ("2008-02-16 12:00",
         "2008-03-28 12:00",
         "2008-04-11 12:00",
         "2008-05-22 12:00",
         "2008-10-16 12:00",
         "2008-11-17 12:00",
         "2009-03-18 12:00",
         "2009-12-03 12:00",
         "2009-12-11 12:00",
         "2010-01-24 12:00",
         "2010-02-09 12:00",
         "2010-02-17 12:00",
         "2010-02-25 12:00",
         "2010-06-04 12:00",
         "2010-06-16 12:00",
         "2010-07-05 12:00",
         "2010-07-29 12:00",
         "2010-08-15 12:00",
         "2010-09-10 12:00",
         "2010-10-14 12:00",
         "2010-10-18 12:00",
         "2010-10-24 12:00",
         "2010-10-31 12:00",
         "2010-11-16 12:00",
         "2011-03-07 12:00",
         "2011-04-28 12:00",
         "2011-05-23 12:00",
         "2011-06-15 12:00",
         "2012-07-16 12:00",
         "2012-09-27 12:00",
         "2012-11-26 12:00",
         "2013-03-16 12:00",
         "2013-05-13 12:00",
         "2013-05-23 12:00",
         "2013-09-05 12:00",
         "2014-02-26 12:00",
         "2014-03-11 12:00",
         "2014-03-18 12:00",
         "2014-06-12 12:00",
         "2014-07-31 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnAmplifierConf_ObjectIdentity = ObjectIdentity
tnAmplifierConf = _TnAmplifierConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1)
)
_TnAmplifierGroups_ObjectIdentity = ObjectIdentity
tnAmplifierGroups = _TnAmplifierGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1)
)
_TnAmplifierPortConfigGroups_ObjectIdentity = ObjectIdentity
tnAmplifierPortConfigGroups = _TnAmplifierPortConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 1)
)
_TnAmplifierPortInfoGroups_ObjectIdentity = ObjectIdentity
tnAmplifierPortInfoGroups = _TnAmplifierPortInfoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 2)
)
_TnAmplifierCardInfoGroups_ObjectIdentity = ObjectIdentity
tnAmplifierCardInfoGroups = _TnAmplifierCardInfoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 3)
)
_TnAmplifierCardConfigGroups_ObjectIdentity = ObjectIdentity
tnAmplifierCardConfigGroups = _TnAmplifierCardConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 4)
)
_TnAmplifierCompliances_ObjectIdentity = ObjectIdentity
tnAmplifierCompliances = _TnAmplifierCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2)
)
_TnAmplifierPortConfigCompliances_ObjectIdentity = ObjectIdentity
tnAmplifierPortConfigCompliances = _TnAmplifierPortConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 1)
)
_TnAmplifierPortInfoCompliances_ObjectIdentity = ObjectIdentity
tnAmplifierPortInfoCompliances = _TnAmplifierPortInfoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 2)
)
_TnAmplifierCardInfoCompliances_ObjectIdentity = ObjectIdentity
tnAmplifierCardInfoCompliances = _TnAmplifierCardInfoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 3)
)
_TnAmplifierCardConfigCompliances_ObjectIdentity = ObjectIdentity
tnAmplifierCardConfigCompliances = _TnAmplifierCardConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 4)
)
_TnAmplifierPortConfig_ObjectIdentity = ObjectIdentity
tnAmplifierPortConfig = _TnAmplifierPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4)
)
_TnAmplifierPortConfigAttributeTotal_Type = Integer32
_TnAmplifierPortConfigAttributeTotal_Object = MibScalar
tnAmplifierPortConfigAttributeTotal = _TnAmplifierPortConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 1),
    _TnAmplifierPortConfigAttributeTotal_Type()
)
tnAmplifierPortConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortConfigAttributeTotal.setStatus("current")
_TnAmplifierPortConfigTable_Object = MibTable
tnAmplifierPortConfigTable = _TnAmplifierPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2)
)
if mibBuilder.loadTexts:
    tnAmplifierPortConfigTable.setStatus("current")
_TnAmplifierPortConfigEntry_Object = MibTableRow
tnAmplifierPortConfigEntry = _TnAmplifierPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1)
)
tnAmplifierPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierPortConfigEntry.setStatus("current")
_TnAmplifierPortPowerGain_Type = Unsigned32
_TnAmplifierPortPowerGain_Object = MibTableColumn
tnAmplifierPortPowerGain = _TnAmplifierPortPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 1),
    _TnAmplifierPortPowerGain_Type()
)
tnAmplifierPortPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGain.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGain.setUnits("mB")
_TnAmplifierPortPowerGainMin_Type = Unsigned32
_TnAmplifierPortPowerGainMin_Object = MibTableColumn
tnAmplifierPortPowerGainMin = _TnAmplifierPortPowerGainMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 2),
    _TnAmplifierPortPowerGainMin_Type()
)
tnAmplifierPortPowerGainMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGainMin.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGainMin.setUnits("mB")
_TnAmplifierPortPowerGainMax_Type = Unsigned32
_TnAmplifierPortPowerGainMax_Object = MibTableColumn
tnAmplifierPortPowerGainMax = _TnAmplifierPortPowerGainMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 3),
    _TnAmplifierPortPowerGainMax_Type()
)
tnAmplifierPortPowerGainMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGainMax.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGainMax.setUnits("mB")


class _TnAmplifierPortPowerGainBackoff_Type(Unsigned32):
    """Custom type tnAmplifierPortPowerGainBackoff based on Unsigned32"""
    defaultValue = 0


_TnAmplifierPortPowerGainBackoff_Type.__name__ = "Unsigned32"
_TnAmplifierPortPowerGainBackoff_Object = MibTableColumn
tnAmplifierPortPowerGainBackoff = _TnAmplifierPortPowerGainBackoff_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 4),
    _TnAmplifierPortPowerGainBackoff_Type()
)
tnAmplifierPortPowerGainBackoff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGainBackoff.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerGainBackoff.setUnits("mB")


class _TnAmplifierPortEnable_Type(TruthValue):
    """Custom type tnAmplifierPortEnable based on TruthValue"""
    defaultValue = 1


_TnAmplifierPortEnable_Type.__name__ = "TruthValue"
_TnAmplifierPortEnable_Object = MibTableColumn
tnAmplifierPortEnable = _TnAmplifierPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 5),
    _TnAmplifierPortEnable_Type()
)
tnAmplifierPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortEnable.setStatus("current")


class _TnAmplifierPortAutoReEnableMode_Type(TruthValue):
    """Custom type tnAmplifierPortAutoReEnableMode based on TruthValue"""
    defaultValue = 1


_TnAmplifierPortAutoReEnableMode_Type.__name__ = "TruthValue"
_TnAmplifierPortAutoReEnableMode_Object = MibTableColumn
tnAmplifierPortAutoReEnableMode = _TnAmplifierPortAutoReEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 6),
    _TnAmplifierPortAutoReEnableMode_Type()
)
tnAmplifierPortAutoReEnableMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortAutoReEnableMode.setStatus("current")
_TnAmplifierPortPowerSpanRepairMargin_Type = Unsigned32
_TnAmplifierPortPowerSpanRepairMargin_Object = MibTableColumn
tnAmplifierPortPowerSpanRepairMargin = _TnAmplifierPortPowerSpanRepairMargin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 8),
    _TnAmplifierPortPowerSpanRepairMargin_Type()
)
tnAmplifierPortPowerSpanRepairMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerSpanRepairMargin.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerSpanRepairMargin.setUnits("mB")


class _TnAmplifierPortPowerDeltaMax_Type(Unsigned32):
    """Custom type tnAmplifierPortPowerDeltaMax based on Unsigned32"""
    defaultValue = 0


_TnAmplifierPortPowerDeltaMax_Type.__name__ = "Unsigned32"
_TnAmplifierPortPowerDeltaMax_Object = MibTableColumn
tnAmplifierPortPowerDeltaMax = _TnAmplifierPortPowerDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 9),
    _TnAmplifierPortPowerDeltaMax_Type()
)
tnAmplifierPortPowerDeltaMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerDeltaMax.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerDeltaMax.setUnits("mB")
_TnAmplifierPortTargetTilt_Type = Integer32
_TnAmplifierPortTargetTilt_Object = MibTableColumn
tnAmplifierPortTargetTilt = _TnAmplifierPortTargetTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 10),
    _TnAmplifierPortTargetTilt_Type()
)
tnAmplifierPortTargetTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortTargetTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortTargetTilt.setUnits("mB")


class _TnAmplifierPortFunction_Type(Integer32):
    """Custom type tnAmplifierPortFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("other", 3))
    )


_TnAmplifierPortFunction_Type.__name__ = "Integer32"
_TnAmplifierPortFunction_Object = MibTableColumn
tnAmplifierPortFunction = _TnAmplifierPortFunction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 11),
    _TnAmplifierPortFunction_Type()
)
tnAmplifierPortFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortFunction.setStatus("current")


class _TnAmplifierPortAprDisable_Type(TruthValue):
    """Custom type tnAmplifierPortAprDisable based on TruthValue"""
    defaultValue = 2


_TnAmplifierPortAprDisable_Type.__name__ = "TruthValue"
_TnAmplifierPortAprDisable_Object = MibTableColumn
tnAmplifierPortAprDisable = _TnAmplifierPortAprDisable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 12),
    _TnAmplifierPortAprDisable_Type()
)
tnAmplifierPortAprDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortAprDisable.setStatus("current")


class _TnAmplifierPortSRSTiltACoeffDCM_Type(Integer32):
    """Custom type tnAmplifierPortSRSTiltACoeffDCM based on Integer32"""
    defaultValue = 0


_TnAmplifierPortSRSTiltACoeffDCM_Type.__name__ = "Integer32"
_TnAmplifierPortSRSTiltACoeffDCM_Object = MibTableColumn
tnAmplifierPortSRSTiltACoeffDCM = _TnAmplifierPortSRSTiltACoeffDCM_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 13),
    _TnAmplifierPortSRSTiltACoeffDCM_Type()
)
tnAmplifierPortSRSTiltACoeffDCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortSRSTiltACoeffDCM.setStatus("current")


class _TnAmplifierPortMaxFlatGainOffset_Type(Integer32):
    """Custom type tnAmplifierPortMaxFlatGainOffset based on Integer32"""
    defaultValue = 0


_TnAmplifierPortMaxFlatGainOffset_Type.__name__ = "Integer32"
_TnAmplifierPortMaxFlatGainOffset_Object = MibTableColumn
tnAmplifierPortMaxFlatGainOffset = _TnAmplifierPortMaxFlatGainOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 14),
    _TnAmplifierPortMaxFlatGainOffset_Type()
)
tnAmplifierPortMaxFlatGainOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortMaxFlatGainOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortMaxFlatGainOffset.setUnits("mB")


class _TnAmplifierPortGainTilt_Type(Integer32):
    """Custom type tnAmplifierPortGainTilt based on Integer32"""
    defaultValue = 0


_TnAmplifierPortGainTilt_Type.__name__ = "Integer32"
_TnAmplifierPortGainTilt_Object = MibTableColumn
tnAmplifierPortGainTilt = _TnAmplifierPortGainTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 15),
    _TnAmplifierPortGainTilt_Type()
)
tnAmplifierPortGainTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortGainTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortGainTilt.setUnits("mB")


class _TnAmplifierPortAprHoldOffTime_Type(Integer32):
    """Custom type tnAmplifierPortAprHoldOffTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("time0ms", 1),
          ("time250ms", 4))
    )


_TnAmplifierPortAprHoldOffTime_Type.__name__ = "Integer32"
_TnAmplifierPortAprHoldOffTime_Object = MibTableColumn
tnAmplifierPortAprHoldOffTime = _TnAmplifierPortAprHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 16),
    _TnAmplifierPortAprHoldOffTime_Type()
)
tnAmplifierPortAprHoldOffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortAprHoldOffTime.setStatus("current")


class _TnAmplifierPortLosMode_Type(Integer32):
    """Custom type tnAmplifierPortLosMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("losn", 2))
    )


_TnAmplifierPortLosMode_Type.__name__ = "Integer32"
_TnAmplifierPortLosMode_Object = MibTableColumn
tnAmplifierPortLosMode = _TnAmplifierPortLosMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 17),
    _TnAmplifierPortLosMode_Type()
)
tnAmplifierPortLosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortLosMode.setStatus("current")


class _TnAmplifierPortSignalFailThreshold_Type(Unsigned32):
    """Custom type tnAmplifierPortSignalFailThreshold based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TnAmplifierPortSignalFailThreshold_Type.__name__ = "Unsigned32"
_TnAmplifierPortSignalFailThreshold_Object = MibTableColumn
tnAmplifierPortSignalFailThreshold = _TnAmplifierPortSignalFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 18),
    _TnAmplifierPortSignalFailThreshold_Type()
)
tnAmplifierPortSignalFailThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortSignalFailThreshold.setStatus("current")


class _TnAmplifierPortSignalDegradeThreshold_Type(Unsigned32):
    """Custom type tnAmplifierPortSignalDegradeThreshold based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TnAmplifierPortSignalDegradeThreshold_Type.__name__ = "Unsigned32"
_TnAmplifierPortSignalDegradeThreshold_Object = MibTableColumn
tnAmplifierPortSignalDegradeThreshold = _TnAmplifierPortSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 19),
    _TnAmplifierPortSignalDegradeThreshold_Type()
)
tnAmplifierPortSignalDegradeThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortSignalDegradeThreshold.setStatus("current")


class _TnAmplifierPortVoaSet_Type(Unsigned32):
    """Custom type tnAmplifierPortVoaSet based on Unsigned32"""
    defaultValue = 0


_TnAmplifierPortVoaSet_Type.__name__ = "Unsigned32"
_TnAmplifierPortVoaSet_Object = MibTableColumn
tnAmplifierPortVoaSet = _TnAmplifierPortVoaSet_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 20),
    _TnAmplifierPortVoaSet_Type()
)
tnAmplifierPortVoaSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortVoaSet.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortVoaSet.setUnits("mBm")


class _TnAmplifierPortGainRange_Type(Integer32):
    """Custom type tnAmplifierPortGainRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_TnAmplifierPortGainRange_Type.__name__ = "Integer32"
_TnAmplifierPortGainRange_Object = MibTableColumn
tnAmplifierPortGainRange = _TnAmplifierPortGainRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 21),
    _TnAmplifierPortGainRange_Type()
)
tnAmplifierPortGainRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortGainRange.setStatus("current")


class _TnAmplifierPortAprMode_Type(Integer32):
    """Custom type tnAmplifierPortAprMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 2))
    )


_TnAmplifierPortAprMode_Type.__name__ = "Integer32"
_TnAmplifierPortAprMode_Object = MibTableColumn
tnAmplifierPortAprMode = _TnAmplifierPortAprMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 22),
    _TnAmplifierPortAprMode_Type()
)
tnAmplifierPortAprMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortAprMode.setStatus("current")


class _TnAmplifierPortOperatingMode_Type(Integer32):
    """Custom type tnAmplifierPortOperatingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gain", 1),
          ("power", 2))
    )


_TnAmplifierPortOperatingMode_Type.__name__ = "Integer32"
_TnAmplifierPortOperatingMode_Object = MibTableColumn
tnAmplifierPortOperatingMode = _TnAmplifierPortOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 23),
    _TnAmplifierPortOperatingMode_Type()
)
tnAmplifierPortOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortOperatingMode.setStatus("current")


class _TnAmplifierPortSignalPowerTarget_Type(Integer32):
    """Custom type tnAmplifierPortSignalPowerTarget based on Integer32"""
    defaultValue = 300


_TnAmplifierPortSignalPowerTarget_Type.__name__ = "Integer32"
_TnAmplifierPortSignalPowerTarget_Object = MibTableColumn
tnAmplifierPortSignalPowerTarget = _TnAmplifierPortSignalPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 2, 1, 24),
    _TnAmplifierPortSignalPowerTarget_Type()
)
tnAmplifierPortSignalPowerTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierPortSignalPowerTarget.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortSignalPowerTarget.setUnits("mBm")
_TnAmplifierHybridPortConfigAttributeTotal_Type = Integer32
_TnAmplifierHybridPortConfigAttributeTotal_Object = MibScalar
tnAmplifierHybridPortConfigAttributeTotal = _TnAmplifierHybridPortConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 3),
    _TnAmplifierHybridPortConfigAttributeTotal_Type()
)
tnAmplifierHybridPortConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortConfigAttributeTotal.setStatus("current")
_TnAmplifierHybridPortConfigTable_Object = MibTable
tnAmplifierHybridPortConfigTable = _TnAmplifierHybridPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 4)
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortConfigTable.setStatus("current")
_TnAmplifierHybridPortConfigEntry_Object = MibTableRow
tnAmplifierHybridPortConfigEntry = _TnAmplifierHybridPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 4, 1)
)
tnAmplifierHybridPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortConfigEntry.setStatus("current")


class _TnAmplifierHybridPortVoaAttenuation_Type(Unsigned32):
    """Custom type tnAmplifierHybridPortVoaAttenuation based on Unsigned32"""
    defaultValue = 0


_TnAmplifierHybridPortVoaAttenuation_Type.__name__ = "Unsigned32"
_TnAmplifierHybridPortVoaAttenuation_Object = MibTableColumn
tnAmplifierHybridPortVoaAttenuation = _TnAmplifierHybridPortVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 4, 1, 1),
    _TnAmplifierHybridPortVoaAttenuation_Type()
)
tnAmplifierHybridPortVoaAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortVoaAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortVoaAttenuation.setUnits("mB")


class _TnAmplifierHybridPortInitialMidLoss_Type(Unsigned32):
    """Custom type tnAmplifierHybridPortInitialMidLoss based on Unsigned32"""
    defaultValue = 60


_TnAmplifierHybridPortInitialMidLoss_Type.__name__ = "Unsigned32"
_TnAmplifierHybridPortInitialMidLoss_Object = MibTableColumn
tnAmplifierHybridPortInitialMidLoss = _TnAmplifierHybridPortInitialMidLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 4, 1, 2),
    _TnAmplifierHybridPortInitialMidLoss_Type()
)
tnAmplifierHybridPortInitialMidLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInitialMidLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInitialMidLoss.setUnits("mB")


class _TnAmplifierHybridPortInitialAgcTargetGain_Type(Unsigned32):
    """Custom type tnAmplifierHybridPortInitialAgcTargetGain based on Unsigned32"""
    defaultValue = 1000


_TnAmplifierHybridPortInitialAgcTargetGain_Type.__name__ = "Unsigned32"
_TnAmplifierHybridPortInitialAgcTargetGain_Object = MibTableColumn
tnAmplifierHybridPortInitialAgcTargetGain = _TnAmplifierHybridPortInitialAgcTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 4, 1, 3),
    _TnAmplifierHybridPortInitialAgcTargetGain_Type()
)
tnAmplifierHybridPortInitialAgcTargetGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInitialAgcTargetGain.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInitialAgcTargetGain.setUnits("mB")


class _TnAmplifierHybridPortVoaMinAttenuation_Type(Unsigned32):
    """Custom type tnAmplifierHybridPortVoaMinAttenuation based on Unsigned32"""
    defaultValue = 0


_TnAmplifierHybridPortVoaMinAttenuation_Type.__name__ = "Unsigned32"
_TnAmplifierHybridPortVoaMinAttenuation_Object = MibTableColumn
tnAmplifierHybridPortVoaMinAttenuation = _TnAmplifierHybridPortVoaMinAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 4, 1, 4),
    _TnAmplifierHybridPortVoaMinAttenuation_Type()
)
tnAmplifierHybridPortVoaMinAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortVoaMinAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortVoaMinAttenuation.setUnits("mB")


class _TnAmplifierHybridPortVoaMaxAttenuation_Type(Unsigned32):
    """Custom type tnAmplifierHybridPortVoaMaxAttenuation based on Unsigned32"""
    defaultValue = 2000


_TnAmplifierHybridPortVoaMaxAttenuation_Type.__name__ = "Unsigned32"
_TnAmplifierHybridPortVoaMaxAttenuation_Object = MibTableColumn
tnAmplifierHybridPortVoaMaxAttenuation = _TnAmplifierHybridPortVoaMaxAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 4, 4, 1, 5),
    _TnAmplifierHybridPortVoaMaxAttenuation_Type()
)
tnAmplifierHybridPortVoaMaxAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortVoaMaxAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortVoaMaxAttenuation.setUnits("mB")
_TnAmplifierPortInfo_ObjectIdentity = ObjectIdentity
tnAmplifierPortInfo = _TnAmplifierPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5)
)
_TnAmplifierPortInfoAttributeTotal_Type = Integer32
_TnAmplifierPortInfoAttributeTotal_Object = MibScalar
tnAmplifierPortInfoAttributeTotal = _TnAmplifierPortInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 1),
    _TnAmplifierPortInfoAttributeTotal_Type()
)
tnAmplifierPortInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortInfoAttributeTotal.setStatus("current")
_TnAmplifierPortInfoTable_Object = MibTable
tnAmplifierPortInfoTable = _TnAmplifierPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2)
)
if mibBuilder.loadTexts:
    tnAmplifierPortInfoTable.setStatus("current")
_TnAmplifierPortInfoEntry_Object = MibTableRow
tnAmplifierPortInfoEntry = _TnAmplifierPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1)
)
tnAmplifierPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierPortInfoEntry.setStatus("current")


class _TnAmplifierPortInternalAmpModuleTemperature_Type(Integer32):
    """Custom type tnAmplifierPortInternalAmpModuleTemperature based on Integer32"""
    defaultValue = 30


_TnAmplifierPortInternalAmpModuleTemperature_Type.__name__ = "Integer32"
_TnAmplifierPortInternalAmpModuleTemperature_Object = MibTableColumn
tnAmplifierPortInternalAmpModuleTemperature = _TnAmplifierPortInternalAmpModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 1),
    _TnAmplifierPortInternalAmpModuleTemperature_Type()
)
tnAmplifierPortInternalAmpModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortInternalAmpModuleTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortInternalAmpModuleTemperature.setUnits("Celsius")
_TnAmplifierPortPowerIn_Type = Integer32
_TnAmplifierPortPowerIn_Object = MibTableColumn
tnAmplifierPortPowerIn = _TnAmplifierPortPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 2),
    _TnAmplifierPortPowerIn_Type()
)
tnAmplifierPortPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerIn.setUnits("mBm")
_TnAmplifierPortPowerOut_Type = Integer32
_TnAmplifierPortPowerOut_Object = MibTableColumn
tnAmplifierPortPowerOut = _TnAmplifierPortPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 3),
    _TnAmplifierPortPowerOut_Type()
)
tnAmplifierPortPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortPowerOut.setUnits("mBm")
_TnAmplifierPortSignalPowerOut_Type = Integer32
_TnAmplifierPortSignalPowerOut_Object = MibTableColumn
tnAmplifierPortSignalPowerOut = _TnAmplifierPortSignalPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 4),
    _TnAmplifierPortSignalPowerOut_Type()
)
tnAmplifierPortSignalPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortSignalPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortSignalPowerOut.setUnits("mBm")
_TnAmplifierPortInputToOutputGain_Type = Integer32
_TnAmplifierPortInputToOutputGain_Object = MibTableColumn
tnAmplifierPortInputToOutputGain = _TnAmplifierPortInputToOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 5),
    _TnAmplifierPortInputToOutputGain_Type()
)
tnAmplifierPortInputToOutputGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortInputToOutputGain.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortInputToOutputGain.setUnits("mB")


class _TnAmplifierPortDCMInPower_Type(Integer32):
    """Custom type tnAmplifierPortDCMInPower based on Integer32"""
    defaultValue = -9900


_TnAmplifierPortDCMInPower_Type.__name__ = "Integer32"
_TnAmplifierPortDCMInPower_Object = MibTableColumn
tnAmplifierPortDCMInPower = _TnAmplifierPortDCMInPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 6),
    _TnAmplifierPortDCMInPower_Type()
)
tnAmplifierPortDCMInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortDCMInPower.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortDCMInPower.setUnits("mBm")


class _TnAmplifierPortDCMOutPower_Type(Integer32):
    """Custom type tnAmplifierPortDCMOutPower based on Integer32"""
    defaultValue = -9900


_TnAmplifierPortDCMOutPower_Type.__name__ = "Integer32"
_TnAmplifierPortDCMOutPower_Object = MibTableColumn
tnAmplifierPortDCMOutPower = _TnAmplifierPortDCMOutPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 7),
    _TnAmplifierPortDCMOutPower_Type()
)
tnAmplifierPortDCMOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortDCMOutPower.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortDCMOutPower.setUnits("mBm")
_TnAmplifierPortActualTilt_Type = Integer32
_TnAmplifierPortActualTilt_Object = MibTableColumn
tnAmplifierPortActualTilt = _TnAmplifierPortActualTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 8),
    _TnAmplifierPortActualTilt_Type()
)
tnAmplifierPortActualTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortActualTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortActualTilt.setUnits("mB")


class _TnAmplifierPortWtOcmMonitorPortOut_Type(Unsigned32):
    """Custom type tnAmplifierPortWtOcmMonitorPortOut based on Unsigned32"""
    defaultValue = 0


_TnAmplifierPortWtOcmMonitorPortOut_Type.__name__ = "Unsigned32"
_TnAmplifierPortWtOcmMonitorPortOut_Object = MibTableColumn
tnAmplifierPortWtOcmMonitorPortOut = _TnAmplifierPortWtOcmMonitorPortOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 9),
    _TnAmplifierPortWtOcmMonitorPortOut_Type()
)
tnAmplifierPortWtOcmMonitorPortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortWtOcmMonitorPortOut.setStatus("current")


class _TnAmplifierPortOSCTxPowerIn_Type(Integer32):
    """Custom type tnAmplifierPortOSCTxPowerIn based on Integer32"""
    defaultValue = -9900


_TnAmplifierPortOSCTxPowerIn_Type.__name__ = "Integer32"
_TnAmplifierPortOSCTxPowerIn_Object = MibTableColumn
tnAmplifierPortOSCTxPowerIn = _TnAmplifierPortOSCTxPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 10),
    _TnAmplifierPortOSCTxPowerIn_Type()
)
tnAmplifierPortOSCTxPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortOSCTxPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortOSCTxPowerIn.setUnits("mBm")


class _TnAmplifierPortOSCTxPowerOut_Type(Integer32):
    """Custom type tnAmplifierPortOSCTxPowerOut based on Integer32"""
    defaultValue = -9900


_TnAmplifierPortOSCTxPowerOut_Type.__name__ = "Integer32"
_TnAmplifierPortOSCTxPowerOut_Object = MibTableColumn
tnAmplifierPortOSCTxPowerOut = _TnAmplifierPortOSCTxPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 11),
    _TnAmplifierPortOSCTxPowerOut_Type()
)
tnAmplifierPortOSCTxPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortOSCTxPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierPortOSCTxPowerOut.setUnits("mBm")


class _TnAmplifierPortTestingActive_Type(TruthValue):
    """Custom type tnAmplifierPortTestingActive based on TruthValue"""
    defaultValue = 2


_TnAmplifierPortTestingActive_Type.__name__ = "TruthValue"
_TnAmplifierPortTestingActive_Object = MibTableColumn
tnAmplifierPortTestingActive = _TnAmplifierPortTestingActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 2, 1, 12),
    _TnAmplifierPortTestingActive_Type()
)
tnAmplifierPortTestingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierPortTestingActive.setStatus("current")
_TnAmplifierMeshPortInfoAttributeTotal_Type = Integer32
_TnAmplifierMeshPortInfoAttributeTotal_Object = MibScalar
tnAmplifierMeshPortInfoAttributeTotal = _TnAmplifierMeshPortInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 3),
    _TnAmplifierMeshPortInfoAttributeTotal_Type()
)
tnAmplifierMeshPortInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshPortInfoAttributeTotal.setStatus("current")
_TnAmplifierMeshPortInfoTable_Object = MibTable
tnAmplifierMeshPortInfoTable = _TnAmplifierMeshPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 4)
)
if mibBuilder.loadTexts:
    tnAmplifierMeshPortInfoTable.setStatus("current")
_TnAmplifierMeshPortInfoEntry_Object = MibTableRow
tnAmplifierMeshPortInfoEntry = _TnAmplifierMeshPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 4, 1)
)
tnAmplifierMeshPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierMeshPortInfoEntry.setStatus("current")


class _TnAmplifierMeshPortPowerOut_Type(Integer32):
    """Custom type tnAmplifierMeshPortPowerOut based on Integer32"""
    defaultValue = -9900


_TnAmplifierMeshPortPowerOut_Type.__name__ = "Integer32"
_TnAmplifierMeshPortPowerOut_Object = MibTableColumn
tnAmplifierMeshPortPowerOut = _TnAmplifierMeshPortPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 4, 1, 1),
    _TnAmplifierMeshPortPowerOut_Type()
)
tnAmplifierMeshPortPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshPortPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshPortPowerOut.setUnits("mBm")


class _TnAmplifierMeshPortSignalPowerOut_Type(Integer32):
    """Custom type tnAmplifierMeshPortSignalPowerOut based on Integer32"""
    defaultValue = -9900


_TnAmplifierMeshPortSignalPowerOut_Type.__name__ = "Integer32"
_TnAmplifierMeshPortSignalPowerOut_Object = MibTableColumn
tnAmplifierMeshPortSignalPowerOut = _TnAmplifierMeshPortSignalPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 4, 1, 2),
    _TnAmplifierMeshPortSignalPowerOut_Type()
)
tnAmplifierMeshPortSignalPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshPortSignalPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshPortSignalPowerOut.setUnits("mBm")


class _TnAmplifierMeshPortInputToOutputGain_Type(Integer32):
    """Custom type tnAmplifierMeshPortInputToOutputGain based on Integer32"""
    defaultValue = 700


_TnAmplifierMeshPortInputToOutputGain_Type.__name__ = "Integer32"
_TnAmplifierMeshPortInputToOutputGain_Object = MibTableColumn
tnAmplifierMeshPortInputToOutputGain = _TnAmplifierMeshPortInputToOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 4, 1, 3),
    _TnAmplifierMeshPortInputToOutputGain_Type()
)
tnAmplifierMeshPortInputToOutputGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshPortInputToOutputGain.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshPortInputToOutputGain.setUnits("mB")
_TnAmplifierHybridPortInfoAttributeTotal_Type = Integer32
_TnAmplifierHybridPortInfoAttributeTotal_Object = MibScalar
tnAmplifierHybridPortInfoAttributeTotal = _TnAmplifierHybridPortInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 5),
    _TnAmplifierHybridPortInfoAttributeTotal_Type()
)
tnAmplifierHybridPortInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInfoAttributeTotal.setStatus("current")
_TnAmplifierHybridPortInfoTable_Object = MibTable
tnAmplifierHybridPortInfoTable = _TnAmplifierHybridPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 6)
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInfoTable.setStatus("current")
_TnAmplifierHybridPortInfoEntry_Object = MibTableRow
tnAmplifierHybridPortInfoEntry = _TnAmplifierHybridPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 6, 1)
)
tnAmplifierHybridPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInfoEntry.setStatus("current")
_TnAmplifierHybridPortInternalAmpModuleTemperature_Type = Unsigned32
_TnAmplifierHybridPortInternalAmpModuleTemperature_Object = MibTableColumn
tnAmplifierHybridPortInternalAmpModuleTemperature = _TnAmplifierHybridPortInternalAmpModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 5, 6, 1, 1),
    _TnAmplifierHybridPortInternalAmpModuleTemperature_Type()
)
tnAmplifierHybridPortInternalAmpModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInternalAmpModuleTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInternalAmpModuleTemperature.setUnits("Celsius")
_TnAmplifierCardInfo_ObjectIdentity = ObjectIdentity
tnAmplifierCardInfo = _TnAmplifierCardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6)
)
_TnAmplifierCardInfoAttributeTotal_Type = Integer32
_TnAmplifierCardInfoAttributeTotal_Object = MibScalar
tnAmplifierCardInfoAttributeTotal = _TnAmplifierCardInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 1),
    _TnAmplifierCardInfoAttributeTotal_Type()
)
tnAmplifierCardInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardInfoAttributeTotal.setStatus("current")
_TnAmplifierCardInfoTable_Object = MibTable
tnAmplifierCardInfoTable = _TnAmplifierCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2)
)
if mibBuilder.loadTexts:
    tnAmplifierCardInfoTable.setStatus("current")
_TnAmplifierCardInfoEntry_Object = MibTableRow
tnAmplifierCardInfoEntry = _TnAmplifierCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1)
)
tnAmplifierCardInfoEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierCardInfoEntry.setStatus("current")
_TnAmplifierCardOAMPump1Temperature_Type = Integer32
_TnAmplifierCardOAMPump1Temperature_Object = MibTableColumn
tnAmplifierCardOAMPump1Temperature = _TnAmplifierCardOAMPump1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 1),
    _TnAmplifierCardOAMPump1Temperature_Type()
)
tnAmplifierCardOAMPump1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump1Temperature.setUnits("Celsius")
_TnAmplifierCardOAMPump2Temperature_Type = Integer32
_TnAmplifierCardOAMPump2Temperature_Object = MibTableColumn
tnAmplifierCardOAMPump2Temperature = _TnAmplifierCardOAMPump2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 2),
    _TnAmplifierCardOAMPump2Temperature_Type()
)
tnAmplifierCardOAMPump2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump2Temperature.setUnits("Celsius")
_TnAmplifierCardOAMPump3Temperature_Type = Integer32
_TnAmplifierCardOAMPump3Temperature_Object = MibTableColumn
tnAmplifierCardOAMPump3Temperature = _TnAmplifierCardOAMPump3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 3),
    _TnAmplifierCardOAMPump3Temperature_Type()
)
tnAmplifierCardOAMPump3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump3Temperature.setUnits("Celsius")
_TnAmplifierCardOAMPump1Bias_Type = Integer32
_TnAmplifierCardOAMPump1Bias_Object = MibTableColumn
tnAmplifierCardOAMPump1Bias = _TnAmplifierCardOAMPump1Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 4),
    _TnAmplifierCardOAMPump1Bias_Type()
)
tnAmplifierCardOAMPump1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump1Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump1Bias.setUnits("mA")
_TnAmplifierCardOAMPump2Bias_Type = Integer32
_TnAmplifierCardOAMPump2Bias_Object = MibTableColumn
tnAmplifierCardOAMPump2Bias = _TnAmplifierCardOAMPump2Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 5),
    _TnAmplifierCardOAMPump2Bias_Type()
)
tnAmplifierCardOAMPump2Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump2Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump2Bias.setUnits("mA")
_TnAmplifierCardOAMPump3Bias_Type = Integer32
_TnAmplifierCardOAMPump3Bias_Object = MibTableColumn
tnAmplifierCardOAMPump3Bias = _TnAmplifierCardOAMPump3Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 6),
    _TnAmplifierCardOAMPump3Bias_Type()
)
tnAmplifierCardOAMPump3Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump3Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump3Bias.setUnits("mA")


class _TnAmplifierCardOptIntSpanLoss_Type(Integer32):
    """Custom type tnAmplifierCardOptIntSpanLoss based on Integer32"""
    defaultValue = 9900


_TnAmplifierCardOptIntSpanLoss_Type.__name__ = "Integer32"
_TnAmplifierCardOptIntSpanLoss_Object = MibTableColumn
tnAmplifierCardOptIntSpanLoss = _TnAmplifierCardOptIntSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 7),
    _TnAmplifierCardOptIntSpanLoss_Type()
)
tnAmplifierCardOptIntSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntSpanLoss.setUnits("mB")
_TnAmplifierCardOAMPump4Temperature_Type = Integer32
_TnAmplifierCardOAMPump4Temperature_Object = MibTableColumn
tnAmplifierCardOAMPump4Temperature = _TnAmplifierCardOAMPump4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 8),
    _TnAmplifierCardOAMPump4Temperature_Type()
)
tnAmplifierCardOAMPump4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump4Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump4Temperature.setUnits("Celsius")
_TnAmplifierCardOAMPump5Temperature_Type = Integer32
_TnAmplifierCardOAMPump5Temperature_Object = MibTableColumn
tnAmplifierCardOAMPump5Temperature = _TnAmplifierCardOAMPump5Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 9),
    _TnAmplifierCardOAMPump5Temperature_Type()
)
tnAmplifierCardOAMPump5Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump5Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump5Temperature.setUnits("Celsius")
_TnAmplifierCardOAMPump6Temperature_Type = Integer32
_TnAmplifierCardOAMPump6Temperature_Object = MibTableColumn
tnAmplifierCardOAMPump6Temperature = _TnAmplifierCardOAMPump6Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 10),
    _TnAmplifierCardOAMPump6Temperature_Type()
)
tnAmplifierCardOAMPump6Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump6Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump6Temperature.setUnits("Celsius")
_TnAmplifierCardOAMPump4Bias_Type = Integer32
_TnAmplifierCardOAMPump4Bias_Object = MibTableColumn
tnAmplifierCardOAMPump4Bias = _TnAmplifierCardOAMPump4Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 11),
    _TnAmplifierCardOAMPump4Bias_Type()
)
tnAmplifierCardOAMPump4Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump4Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump4Bias.setUnits("mA")
_TnAmplifierCardOAMPump5Bias_Type = Integer32
_TnAmplifierCardOAMPump5Bias_Object = MibTableColumn
tnAmplifierCardOAMPump5Bias = _TnAmplifierCardOAMPump5Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 12),
    _TnAmplifierCardOAMPump5Bias_Type()
)
tnAmplifierCardOAMPump5Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump5Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump5Bias.setUnits("mA")
_TnAmplifierCardOAMPump6Bias_Type = Integer32
_TnAmplifierCardOAMPump6Bias_Object = MibTableColumn
tnAmplifierCardOAMPump6Bias = _TnAmplifierCardOAMPump6Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 2, 1, 13),
    _TnAmplifierCardOAMPump6Bias_Type()
)
tnAmplifierCardOAMPump6Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump6Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOAMPump6Bias.setUnits("mA")
_TnAmplifierMeshCardInfoAttributeTotal_Type = Integer32
_TnAmplifierMeshCardInfoAttributeTotal_Object = MibScalar
tnAmplifierMeshCardInfoAttributeTotal = _TnAmplifierMeshCardInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 3),
    _TnAmplifierMeshCardInfoAttributeTotal_Type()
)
tnAmplifierMeshCardInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInfoAttributeTotal.setStatus("current")
_TnAmplifierMeshCardInfoTable_Object = MibTable
tnAmplifierMeshCardInfoTable = _TnAmplifierMeshCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4)
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInfoTable.setStatus("current")
_TnAmplifierMeshCardInfoEntry_Object = MibTableRow
tnAmplifierMeshCardInfoEntry = _TnAmplifierMeshCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1)
)
tnAmplifierMeshCardInfoEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInfoEntry.setStatus("current")


class _TnAmplifierMeshCardInternalTemperature_Type(Integer32):
    """Custom type tnAmplifierMeshCardInternalTemperature based on Integer32"""
    defaultValue = 30


_TnAmplifierMeshCardInternalTemperature_Type.__name__ = "Integer32"
_TnAmplifierMeshCardInternalTemperature_Object = MibTableColumn
tnAmplifierMeshCardInternalTemperature = _TnAmplifierMeshCardInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1, 1),
    _TnAmplifierMeshCardInternalTemperature_Type()
)
tnAmplifierMeshCardInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInternalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInternalTemperature.setUnits("Celsius")
_TnAmplifierMeshCardPowerIn_Type = Integer32
_TnAmplifierMeshCardPowerIn_Object = MibTableColumn
tnAmplifierMeshCardPowerIn = _TnAmplifierMeshCardPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1, 2),
    _TnAmplifierMeshCardPowerIn_Type()
)
tnAmplifierMeshCardPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerIn.setUnits("mBm")
_TnAmplifierMeshCardPowerOut_Type = Integer32
_TnAmplifierMeshCardPowerOut_Object = MibTableColumn
tnAmplifierMeshCardPowerOut = _TnAmplifierMeshCardPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1, 3),
    _TnAmplifierMeshCardPowerOut_Type()
)
tnAmplifierMeshCardPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerOut.setUnits("mBm")
_TnAmplifierMeshCardSignalPowerOut_Type = Integer32
_TnAmplifierMeshCardSignalPowerOut_Object = MibTableColumn
tnAmplifierMeshCardSignalPowerOut = _TnAmplifierMeshCardSignalPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1, 4),
    _TnAmplifierMeshCardSignalPowerOut_Type()
)
tnAmplifierMeshCardSignalPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardSignalPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardSignalPowerOut.setUnits("mBm")


class _TnAmplifierMeshCardInputToOutputGain_Type(Integer32):
    """Custom type tnAmplifierMeshCardInputToOutputGain based on Integer32"""
    defaultValue = 700


_TnAmplifierMeshCardInputToOutputGain_Type.__name__ = "Integer32"
_TnAmplifierMeshCardInputToOutputGain_Object = MibTableColumn
tnAmplifierMeshCardInputToOutputGain = _TnAmplifierMeshCardInputToOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1, 5),
    _TnAmplifierMeshCardInputToOutputGain_Type()
)
tnAmplifierMeshCardInputToOutputGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInputToOutputGain.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInputToOutputGain.setUnits("mB")
_TnAmplifierMeshCardGainTilt_Type = Integer32
_TnAmplifierMeshCardGainTilt_Object = MibTableColumn
tnAmplifierMeshCardGainTilt = _TnAmplifierMeshCardGainTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1, 6),
    _TnAmplifierMeshCardGainTilt_Type()
)
tnAmplifierMeshCardGainTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardGainTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardGainTilt.setUnits("mB")
_TnAmplifierMeshCardActualTilt_Type = Integer32
_TnAmplifierMeshCardActualTilt_Object = MibTableColumn
tnAmplifierMeshCardActualTilt = _TnAmplifierMeshCardActualTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 4, 1, 7),
    _TnAmplifierMeshCardActualTilt_Type()
)
tnAmplifierMeshCardActualTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardActualTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardActualTilt.setUnits("mB")
_TnAmplifierHybridCardInfoAttributeTotal_Type = Integer32
_TnAmplifierHybridCardInfoAttributeTotal_Object = MibScalar
tnAmplifierHybridCardInfoAttributeTotal = _TnAmplifierHybridCardInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 5),
    _TnAmplifierHybridCardInfoAttributeTotal_Type()
)
tnAmplifierHybridCardInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardInfoAttributeTotal.setStatus("current")
_TnAmplifierHybridCardInfoTable_Object = MibTable
tnAmplifierHybridCardInfoTable = _TnAmplifierHybridCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6)
)
if mibBuilder.loadTexts:
    tnAmplifierHybridCardInfoTable.setStatus("current")
_TnAmplifierHybridCardInfoEntry_Object = MibTableRow
tnAmplifierHybridCardInfoEntry = _TnAmplifierHybridCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1)
)
tnAmplifierHybridCardInfoEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierHybridCardInfoEntry.setStatus("current")
_TnAmplifierHybridCardOAMPump1Temperature_Type = Integer32
_TnAmplifierHybridCardOAMPump1Temperature_Object = MibTableColumn
tnAmplifierHybridCardOAMPump1Temperature = _TnAmplifierHybridCardOAMPump1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 1),
    _TnAmplifierHybridCardOAMPump1Temperature_Type()
)
tnAmplifierHybridCardOAMPump1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump1Temperature.setUnits("Celsius")
_TnAmplifierHybridCardOAMPump2Temperature_Type = Integer32
_TnAmplifierHybridCardOAMPump2Temperature_Object = MibTableColumn
tnAmplifierHybridCardOAMPump2Temperature = _TnAmplifierHybridCardOAMPump2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 2),
    _TnAmplifierHybridCardOAMPump2Temperature_Type()
)
tnAmplifierHybridCardOAMPump2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump2Temperature.setUnits("Celsius")


class _TnAmplifierHybridCardOAMPump1Bias_Type(Integer32):
    """Custom type tnAmplifierHybridCardOAMPump1Bias based on Integer32"""
    defaultValue = 0


_TnAmplifierHybridCardOAMPump1Bias_Type.__name__ = "Integer32"
_TnAmplifierHybridCardOAMPump1Bias_Object = MibTableColumn
tnAmplifierHybridCardOAMPump1Bias = _TnAmplifierHybridCardOAMPump1Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 3),
    _TnAmplifierHybridCardOAMPump1Bias_Type()
)
tnAmplifierHybridCardOAMPump1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump1Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump1Bias.setUnits("mA")


class _TnAmplifierHybridCardOAMPump2Bias_Type(Integer32):
    """Custom type tnAmplifierHybridCardOAMPump2Bias based on Integer32"""
    defaultValue = 0


_TnAmplifierHybridCardOAMPump2Bias_Type.__name__ = "Integer32"
_TnAmplifierHybridCardOAMPump2Bias_Object = MibTableColumn
tnAmplifierHybridCardOAMPump2Bias = _TnAmplifierHybridCardOAMPump2Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 4),
    _TnAmplifierHybridCardOAMPump2Bias_Type()
)
tnAmplifierHybridCardOAMPump2Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump2Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump2Bias.setUnits("mA")
_TnAmplifierHybridCardOAMPump3Temperature_Type = Integer32
_TnAmplifierHybridCardOAMPump3Temperature_Object = MibTableColumn
tnAmplifierHybridCardOAMPump3Temperature = _TnAmplifierHybridCardOAMPump3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 5),
    _TnAmplifierHybridCardOAMPump3Temperature_Type()
)
tnAmplifierHybridCardOAMPump3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump3Temperature.setUnits("Celsius")
_TnAmplifierHybridCardOAMPump4Temperature_Type = Integer32
_TnAmplifierHybridCardOAMPump4Temperature_Object = MibTableColumn
tnAmplifierHybridCardOAMPump4Temperature = _TnAmplifierHybridCardOAMPump4Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 6),
    _TnAmplifierHybridCardOAMPump4Temperature_Type()
)
tnAmplifierHybridCardOAMPump4Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump4Temperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump4Temperature.setUnits("Celsius")


class _TnAmplifierHybridCardOAMPump3Bias_Type(Integer32):
    """Custom type tnAmplifierHybridCardOAMPump3Bias based on Integer32"""
    defaultValue = 0


_TnAmplifierHybridCardOAMPump3Bias_Type.__name__ = "Integer32"
_TnAmplifierHybridCardOAMPump3Bias_Object = MibTableColumn
tnAmplifierHybridCardOAMPump3Bias = _TnAmplifierHybridCardOAMPump3Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 7),
    _TnAmplifierHybridCardOAMPump3Bias_Type()
)
tnAmplifierHybridCardOAMPump3Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump3Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump3Bias.setUnits("mA")


class _TnAmplifierHybridCardOAMPump4Bias_Type(Integer32):
    """Custom type tnAmplifierHybridCardOAMPump4Bias based on Integer32"""
    defaultValue = 0


_TnAmplifierHybridCardOAMPump4Bias_Type.__name__ = "Integer32"
_TnAmplifierHybridCardOAMPump4Bias_Object = MibTableColumn
tnAmplifierHybridCardOAMPump4Bias = _TnAmplifierHybridCardOAMPump4Bias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 6, 6, 1, 8),
    _TnAmplifierHybridCardOAMPump4Bias_Type()
)
tnAmplifierHybridCardOAMPump4Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump4Bias.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierHybridCardOAMPump4Bias.setUnits("mA")
_TnAmplifierCardConfig_ObjectIdentity = ObjectIdentity
tnAmplifierCardConfig = _TnAmplifierCardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7)
)
_TnAmplifierCardConfigAttributeTotal_Type = Integer32
_TnAmplifierCardConfigAttributeTotal_Object = MibScalar
tnAmplifierCardConfigAttributeTotal = _TnAmplifierCardConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 1),
    _TnAmplifierCardConfigAttributeTotal_Type()
)
tnAmplifierCardConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierCardConfigAttributeTotal.setStatus("current")
_TnAmplifierCardConfigTable_Object = MibTable
tnAmplifierCardConfigTable = _TnAmplifierCardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2)
)
if mibBuilder.loadTexts:
    tnAmplifierCardConfigTable.setStatus("current")
_TnAmplifierCardConfigEntry_Object = MibTableRow
tnAmplifierCardConfigEntry = _TnAmplifierCardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2, 1)
)
tnAmplifierCardConfigEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierCardConfigEntry.setStatus("current")


class _TnAmplifierCardOptIntDetection_Type(Integer32):
    """Custom type tnAmplifierCardOptIntDetection based on Integer32"""
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


_TnAmplifierCardOptIntDetection_Type.__name__ = "Integer32"
_TnAmplifierCardOptIntDetection_Object = MibTableColumn
tnAmplifierCardOptIntDetection = _TnAmplifierCardOptIntDetection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2, 1, 1),
    _TnAmplifierCardOptIntDetection_Type()
)
tnAmplifierCardOptIntDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntDetection.setStatus("current")


class _TnAmplifierCardOptIntBaseline_Type(Integer32):
    """Custom type tnAmplifierCardOptIntBaseline based on Integer32"""
    defaultValue = -100


_TnAmplifierCardOptIntBaseline_Type.__name__ = "Integer32"
_TnAmplifierCardOptIntBaseline_Object = MibTableColumn
tnAmplifierCardOptIntBaseline = _TnAmplifierCardOptIntBaseline_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2, 1, 2),
    _TnAmplifierCardOptIntBaseline_Type()
)
tnAmplifierCardOptIntBaseline.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntBaseline.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntBaseline.setUnits("mBm")


class _TnAmplifierCardOptIntLossThreshold_Type(Integer32):
    """Custom type tnAmplifierCardOptIntLossThreshold based on Integer32"""
    defaultValue = 150


_TnAmplifierCardOptIntLossThreshold_Type.__name__ = "Integer32"
_TnAmplifierCardOptIntLossThreshold_Object = MibTableColumn
tnAmplifierCardOptIntLossThreshold = _TnAmplifierCardOptIntLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2, 1, 3),
    _TnAmplifierCardOptIntLossThreshold_Type()
)
tnAmplifierCardOptIntLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntLossThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntLossThreshold.setUnits("mBm")


class _TnAmplifierCardOptIntPollPeriod_Type(Integer32):
    """Custom type tnAmplifierCardOptIntPollPeriod based on Integer32"""
    defaultValue = 30


_TnAmplifierCardOptIntPollPeriod_Type.__name__ = "Integer32"
_TnAmplifierCardOptIntPollPeriod_Object = MibTableColumn
tnAmplifierCardOptIntPollPeriod = _TnAmplifierCardOptIntPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2, 1, 4),
    _TnAmplifierCardOptIntPollPeriod_Type()
)
tnAmplifierCardOptIntPollPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntPollPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntPollPeriod.setUnits("seconds")


class _TnAmplifierCardOptIntClearAlarm_Type(TnCommand):
    """Custom type tnAmplifierCardOptIntClearAlarm based on TnCommand"""
    defaultValue = 1


_TnAmplifierCardOptIntClearAlarm_Type.__name__ = "TnCommand"
_TnAmplifierCardOptIntClearAlarm_Object = MibTableColumn
tnAmplifierCardOptIntClearAlarm = _TnAmplifierCardOptIntClearAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2, 1, 5),
    _TnAmplifierCardOptIntClearAlarm_Type()
)
tnAmplifierCardOptIntClearAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierCardOptIntClearAlarm.setStatus("current")


class _TnAmplifierCardAsonAddDropPlannedForOps_Type(TruthValue):
    """Custom type tnAmplifierCardAsonAddDropPlannedForOps based on TruthValue"""
    defaultValue = 2


_TnAmplifierCardAsonAddDropPlannedForOps_Type.__name__ = "TruthValue"
_TnAmplifierCardAsonAddDropPlannedForOps_Object = MibTableColumn
tnAmplifierCardAsonAddDropPlannedForOps = _TnAmplifierCardAsonAddDropPlannedForOps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 2, 1, 6),
    _TnAmplifierCardAsonAddDropPlannedForOps_Type()
)
tnAmplifierCardAsonAddDropPlannedForOps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierCardAsonAddDropPlannedForOps.setStatus("current")
_TnAmplifierMeshCardConfigAttributeTotal_Type = Integer32
_TnAmplifierMeshCardConfigAttributeTotal_Object = MibScalar
tnAmplifierMeshCardConfigAttributeTotal = _TnAmplifierMeshCardConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 3),
    _TnAmplifierMeshCardConfigAttributeTotal_Type()
)
tnAmplifierMeshCardConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardConfigAttributeTotal.setStatus("current")
_TnAmplifierMeshCardConfigTable_Object = MibTable
tnAmplifierMeshCardConfigTable = _TnAmplifierMeshCardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4)
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardConfigTable.setStatus("current")
_TnAmplifierMeshCardConfigEntry_Object = MibTableRow
tnAmplifierMeshCardConfigEntry = _TnAmplifierMeshCardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4, 1)
)
tnAmplifierMeshCardConfigEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardConfigEntry.setStatus("current")


class _TnAmplifierMeshCardPowerGain_Type(Unsigned32):
    """Custom type tnAmplifierMeshCardPowerGain based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 2400),
    )


_TnAmplifierMeshCardPowerGain_Type.__name__ = "Unsigned32"
_TnAmplifierMeshCardPowerGain_Object = MibTableColumn
tnAmplifierMeshCardPowerGain = _TnAmplifierMeshCardPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4, 1, 1),
    _TnAmplifierMeshCardPowerGain_Type()
)
tnAmplifierMeshCardPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerGain.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerGain.setUnits("mB")


class _TnAmplifierMeshCardPowerGainMin_Type(Unsigned32):
    """Custom type tnAmplifierMeshCardPowerGainMin based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 2400),
    )


_TnAmplifierMeshCardPowerGainMin_Type.__name__ = "Unsigned32"
_TnAmplifierMeshCardPowerGainMin_Object = MibTableColumn
tnAmplifierMeshCardPowerGainMin = _TnAmplifierMeshCardPowerGainMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4, 1, 2),
    _TnAmplifierMeshCardPowerGainMin_Type()
)
tnAmplifierMeshCardPowerGainMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerGainMin.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerGainMin.setUnits("mB")


class _TnAmplifierMeshCardPowerGainMax_Type(Unsigned32):
    """Custom type tnAmplifierMeshCardPowerGainMax based on Unsigned32"""
    defaultValue = 2400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 2400),
    )


_TnAmplifierMeshCardPowerGainMax_Type.__name__ = "Unsigned32"
_TnAmplifierMeshCardPowerGainMax_Object = MibTableColumn
tnAmplifierMeshCardPowerGainMax = _TnAmplifierMeshCardPowerGainMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4, 1, 3),
    _TnAmplifierMeshCardPowerGainMax_Type()
)
tnAmplifierMeshCardPowerGainMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerGainMax.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardPowerGainMax.setUnits("mB")


class _TnAmplifierMeshCardTargetTilt_Type(Integer32):
    """Custom type tnAmplifierMeshCardTargetTilt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 400),
    )


_TnAmplifierMeshCardTargetTilt_Type.__name__ = "Integer32"
_TnAmplifierMeshCardTargetTilt_Object = MibTableColumn
tnAmplifierMeshCardTargetTilt = _TnAmplifierMeshCardTargetTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4, 1, 4),
    _TnAmplifierMeshCardTargetTilt_Type()
)
tnAmplifierMeshCardTargetTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardTargetTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardTargetTilt.setUnits("mB")


class _TnAmplifierMeshCardVoaSet_Type(Unsigned32):
    """Custom type tnAmplifierMeshCardVoaSet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_TnAmplifierMeshCardVoaSet_Type.__name__ = "Unsigned32"
_TnAmplifierMeshCardVoaSet_Object = MibTableColumn
tnAmplifierMeshCardVoaSet = _TnAmplifierMeshCardVoaSet_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4, 1, 5),
    _TnAmplifierMeshCardVoaSet_Type()
)
tnAmplifierMeshCardVoaSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardVoaSet.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardVoaSet.setUnits("mBm")


class _TnAmplifierMeshCardCommonEgressPower_Type(Integer32):
    """Custom type tnAmplifierMeshCardCommonEgressPower based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_TnAmplifierMeshCardCommonEgressPower_Type.__name__ = "Integer32"
_TnAmplifierMeshCardCommonEgressPower_Object = MibTableColumn
tnAmplifierMeshCardCommonEgressPower = _TnAmplifierMeshCardCommonEgressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 7, 4, 1, 6),
    _TnAmplifierMeshCardCommonEgressPower_Type()
)
tnAmplifierMeshCardCommonEgressPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardCommonEgressPower.setStatus("current")
if mibBuilder.loadTexts:
    tnAmplifierMeshCardCommonEgressPower.setUnits("mBm")

# Managed Objects groups

tnAmplifierPortConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 1, 1)
)
tnAmplifierPortConfigScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierPortConfigScalarsGroup.setStatus("current")

tnAmplifierPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 1, 2)
)
tnAmplifierPortConfigGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerGain"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerGainMin"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerGainMax"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerGainBackoff"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortEnable"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortAutoReEnableMode"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerSpanRepairMargin"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerDeltaMax"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortTargetTilt"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortFunction"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortAprDisable"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortSRSTiltACoeffDCM"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortMaxFlatGainOffset"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortGainTilt"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortAprHoldOffTime"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortLosMode"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortSignalFailThreshold"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortSignalDegradeThreshold"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortVoaSet"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortGainRange"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortAprMode"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortOperatingMode"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortSignalPowerTarget"))
)
if mibBuilder.loadTexts:
    tnAmplifierPortConfigGroup.setStatus("current")

tnAmplifierHybridPortConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 1, 3)
)
tnAmplifierHybridPortConfigScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortConfigScalarsGroup.setStatus("current")

tnAmplifierHybridPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 1, 4)
)
tnAmplifierHybridPortConfigGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortVoaAttenuation"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortInitialMidLoss"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortInitialAgcTargetGain"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortVoaMinAttenuation"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortVoaMaxAttenuation"))
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortConfigGroup.setStatus("current")

tnAmplifierPortInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 2, 1)
)
tnAmplifierPortInfoScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierPortInfoScalarsGroup.setStatus("current")

tnAmplifierPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 2, 2)
)
tnAmplifierPortInfoGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortInternalAmpModuleTemperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerIn"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortPowerOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortSignalPowerOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortInputToOutputGain"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortDCMInPower"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortDCMOutPower"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortActualTilt"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortWtOcmMonitorPortOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortOSCTxPowerIn"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortOSCTxPowerOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortTestingActive"))
)
if mibBuilder.loadTexts:
    tnAmplifierPortInfoGroup.setStatus("current")

tnAmplifierMeshPortInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 2, 3)
)
tnAmplifierMeshPortInfoScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshPortInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierMeshPortInfoScalarsGroup.setStatus("current")

tnAmplifierMeshPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 2, 4)
)
tnAmplifierMeshPortInfoGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshPortPowerOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshPortSignalPowerOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshPortInputToOutputGain"))
)
if mibBuilder.loadTexts:
    tnAmplifierMeshPortInfoGroup.setStatus("current")

tnAmplifierHybridPortInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 2, 5)
)
tnAmplifierHybridPortInfoScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInfoScalarsGroup.setStatus("current")

tnAmplifierHybridPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 2, 6)
)
tnAmplifierHybridPortInfoGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortInternalAmpModuleTemperature")
)
if mibBuilder.loadTexts:
    tnAmplifierHybridPortInfoGroup.setStatus("current")

tnAmplifierCardInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 3, 1)
)
tnAmplifierCardInfoScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierCardInfoScalarsGroup.setStatus("current")

tnAmplifierCardInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 3, 2)
)
tnAmplifierCardInfoGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump1Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump2Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump3Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump1Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump2Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump3Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOptIntSpanLoss"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump4Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump5Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump6Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump4Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump5Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOAMPump6Bias"))
)
if mibBuilder.loadTexts:
    tnAmplifierCardInfoGroup.setStatus("current")

tnAmplifierMeshCardInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 3, 3)
)
tnAmplifierMeshCardInfoScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInfoScalarsGroup.setStatus("current")

tnAmplifierMeshCardInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 3, 4)
)
tnAmplifierMeshCardInfoGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardInternalTemperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardPowerIn"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardPowerOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardSignalPowerOut"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardInputToOutputGain"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardGainTilt"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardActualTilt"))
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardInfoGroup.setStatus("current")

tnAmplifierHybridCardInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 3, 5)
)
tnAmplifierHybridCardInfoScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierHybridCardInfoScalarsGroup.setStatus("current")

tnAmplifierHybridCardInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 3, 6)
)
tnAmplifierHybridCardInfoGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump1Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump2Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump1Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump2Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump3Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump4Temperature"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump3Bias"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardOAMPump4Bias"))
)
if mibBuilder.loadTexts:
    tnAmplifierHybridCardInfoGroup.setStatus("current")

tnAmplifierCardConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 4, 1)
)
tnAmplifierCardConfigScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierCardConfigScalarsGroup.setStatus("current")

tnAmplifierCardConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 4, 2)
)
tnAmplifierCardConfigGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOptIntDetection"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOptIntBaseline"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOptIntLossThreshold"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOptIntPollPeriod"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardOptIntClearAlarm"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardAsonAddDropPlannedForOps"))
)
if mibBuilder.loadTexts:
    tnAmplifierCardConfigGroup.setStatus("current")

tnAmplifierMeshCardConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 4, 3)
)
tnAmplifierMeshCardConfigScalarsGroup.setObjects(
    ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardConfigScalarsGroup.setStatus("current")

tnAmplifierMeshCardConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 1, 4, 4)
)
tnAmplifierMeshCardConfigGroup.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardPowerGain"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardPowerGainMin"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardPowerGainMax"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardTargetTilt"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardVoaSet"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardCommonEgressPower"))
)
if mibBuilder.loadTexts:
    tnAmplifierMeshCardConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnAmplifierPortConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 1, 1)
)
tnAmplifierPortConfigCompliance.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortConfigScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortConfigGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortConfigScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortConfigGroup"))
)
if mibBuilder.loadTexts:
    tnAmplifierPortConfigCompliance.setStatus(
        "current"
    )

tnAmplifierPortInfoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 2, 1)
)
tnAmplifierPortInfoCompliance.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortInfoScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierPortInfoGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshPortInfoScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshPortInfoGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortInfoScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridPortInfoGroup"))
)
if mibBuilder.loadTexts:
    tnAmplifierPortInfoCompliance.setStatus(
        "current"
    )

tnAmplifierCardInfoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 3, 1)
)
tnAmplifierCardInfoCompliance.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardInfoScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardInfoGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardInfoScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardInfoGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardInfoScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierHybridCardInfoGroup"))
)
if mibBuilder.loadTexts:
    tnAmplifierCardInfoCompliance.setStatus(
        "current"
    )

tnAmplifierCardConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7, 1, 2, 4, 1)
)
tnAmplifierCardConfigCompliance.setObjects(
      *(("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardConfigScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierCardConfigGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardConfigScalarsGroup"),
        ("TROPIC-AMPLIFIER-MIB", "tnAmplifierMeshCardConfigGroup"))
)
if mibBuilder.loadTexts:
    tnAmplifierCardConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-AMPLIFIER-MIB",
    **{"tnAmplifierMibModule": tnAmplifierMibModule,
       "tnAmplifierConf": tnAmplifierConf,
       "tnAmplifierGroups": tnAmplifierGroups,
       "tnAmplifierPortConfigGroups": tnAmplifierPortConfigGroups,
       "tnAmplifierPortConfigScalarsGroup": tnAmplifierPortConfigScalarsGroup,
       "tnAmplifierPortConfigGroup": tnAmplifierPortConfigGroup,
       "tnAmplifierHybridPortConfigScalarsGroup": tnAmplifierHybridPortConfigScalarsGroup,
       "tnAmplifierHybridPortConfigGroup": tnAmplifierHybridPortConfigGroup,
       "tnAmplifierPortInfoGroups": tnAmplifierPortInfoGroups,
       "tnAmplifierPortInfoScalarsGroup": tnAmplifierPortInfoScalarsGroup,
       "tnAmplifierPortInfoGroup": tnAmplifierPortInfoGroup,
       "tnAmplifierMeshPortInfoScalarsGroup": tnAmplifierMeshPortInfoScalarsGroup,
       "tnAmplifierMeshPortInfoGroup": tnAmplifierMeshPortInfoGroup,
       "tnAmplifierHybridPortInfoScalarsGroup": tnAmplifierHybridPortInfoScalarsGroup,
       "tnAmplifierHybridPortInfoGroup": tnAmplifierHybridPortInfoGroup,
       "tnAmplifierCardInfoGroups": tnAmplifierCardInfoGroups,
       "tnAmplifierCardInfoScalarsGroup": tnAmplifierCardInfoScalarsGroup,
       "tnAmplifierCardInfoGroup": tnAmplifierCardInfoGroup,
       "tnAmplifierMeshCardInfoScalarsGroup": tnAmplifierMeshCardInfoScalarsGroup,
       "tnAmplifierMeshCardInfoGroup": tnAmplifierMeshCardInfoGroup,
       "tnAmplifierHybridCardInfoScalarsGroup": tnAmplifierHybridCardInfoScalarsGroup,
       "tnAmplifierHybridCardInfoGroup": tnAmplifierHybridCardInfoGroup,
       "tnAmplifierCardConfigGroups": tnAmplifierCardConfigGroups,
       "tnAmplifierCardConfigScalarsGroup": tnAmplifierCardConfigScalarsGroup,
       "tnAmplifierCardConfigGroup": tnAmplifierCardConfigGroup,
       "tnAmplifierMeshCardConfigScalarsGroup": tnAmplifierMeshCardConfigScalarsGroup,
       "tnAmplifierMeshCardConfigGroup": tnAmplifierMeshCardConfigGroup,
       "tnAmplifierCompliances": tnAmplifierCompliances,
       "tnAmplifierPortConfigCompliances": tnAmplifierPortConfigCompliances,
       "tnAmplifierPortConfigCompliance": tnAmplifierPortConfigCompliance,
       "tnAmplifierPortInfoCompliances": tnAmplifierPortInfoCompliances,
       "tnAmplifierPortInfoCompliance": tnAmplifierPortInfoCompliance,
       "tnAmplifierCardInfoCompliances": tnAmplifierCardInfoCompliances,
       "tnAmplifierCardInfoCompliance": tnAmplifierCardInfoCompliance,
       "tnAmplifierCardConfigCompliances": tnAmplifierCardConfigCompliances,
       "tnAmplifierCardConfigCompliance": tnAmplifierCardConfigCompliance,
       "tnAmplifierPortConfig": tnAmplifierPortConfig,
       "tnAmplifierPortConfigAttributeTotal": tnAmplifierPortConfigAttributeTotal,
       "tnAmplifierPortConfigTable": tnAmplifierPortConfigTable,
       "tnAmplifierPortConfigEntry": tnAmplifierPortConfigEntry,
       "tnAmplifierPortPowerGain": tnAmplifierPortPowerGain,
       "tnAmplifierPortPowerGainMin": tnAmplifierPortPowerGainMin,
       "tnAmplifierPortPowerGainMax": tnAmplifierPortPowerGainMax,
       "tnAmplifierPortPowerGainBackoff": tnAmplifierPortPowerGainBackoff,
       "tnAmplifierPortEnable": tnAmplifierPortEnable,
       "tnAmplifierPortAutoReEnableMode": tnAmplifierPortAutoReEnableMode,
       "tnAmplifierPortPowerSpanRepairMargin": tnAmplifierPortPowerSpanRepairMargin,
       "tnAmplifierPortPowerDeltaMax": tnAmplifierPortPowerDeltaMax,
       "tnAmplifierPortTargetTilt": tnAmplifierPortTargetTilt,
       "tnAmplifierPortFunction": tnAmplifierPortFunction,
       "tnAmplifierPortAprDisable": tnAmplifierPortAprDisable,
       "tnAmplifierPortSRSTiltACoeffDCM": tnAmplifierPortSRSTiltACoeffDCM,
       "tnAmplifierPortMaxFlatGainOffset": tnAmplifierPortMaxFlatGainOffset,
       "tnAmplifierPortGainTilt": tnAmplifierPortGainTilt,
       "tnAmplifierPortAprHoldOffTime": tnAmplifierPortAprHoldOffTime,
       "tnAmplifierPortLosMode": tnAmplifierPortLosMode,
       "tnAmplifierPortSignalFailThreshold": tnAmplifierPortSignalFailThreshold,
       "tnAmplifierPortSignalDegradeThreshold": tnAmplifierPortSignalDegradeThreshold,
       "tnAmplifierPortVoaSet": tnAmplifierPortVoaSet,
       "tnAmplifierPortGainRange": tnAmplifierPortGainRange,
       "tnAmplifierPortAprMode": tnAmplifierPortAprMode,
       "tnAmplifierPortOperatingMode": tnAmplifierPortOperatingMode,
       "tnAmplifierPortSignalPowerTarget": tnAmplifierPortSignalPowerTarget,
       "tnAmplifierHybridPortConfigAttributeTotal": tnAmplifierHybridPortConfigAttributeTotal,
       "tnAmplifierHybridPortConfigTable": tnAmplifierHybridPortConfigTable,
       "tnAmplifierHybridPortConfigEntry": tnAmplifierHybridPortConfigEntry,
       "tnAmplifierHybridPortVoaAttenuation": tnAmplifierHybridPortVoaAttenuation,
       "tnAmplifierHybridPortInitialMidLoss": tnAmplifierHybridPortInitialMidLoss,
       "tnAmplifierHybridPortInitialAgcTargetGain": tnAmplifierHybridPortInitialAgcTargetGain,
       "tnAmplifierHybridPortVoaMinAttenuation": tnAmplifierHybridPortVoaMinAttenuation,
       "tnAmplifierHybridPortVoaMaxAttenuation": tnAmplifierHybridPortVoaMaxAttenuation,
       "tnAmplifierPortInfo": tnAmplifierPortInfo,
       "tnAmplifierPortInfoAttributeTotal": tnAmplifierPortInfoAttributeTotal,
       "tnAmplifierPortInfoTable": tnAmplifierPortInfoTable,
       "tnAmplifierPortInfoEntry": tnAmplifierPortInfoEntry,
       "tnAmplifierPortInternalAmpModuleTemperature": tnAmplifierPortInternalAmpModuleTemperature,
       "tnAmplifierPortPowerIn": tnAmplifierPortPowerIn,
       "tnAmplifierPortPowerOut": tnAmplifierPortPowerOut,
       "tnAmplifierPortSignalPowerOut": tnAmplifierPortSignalPowerOut,
       "tnAmplifierPortInputToOutputGain": tnAmplifierPortInputToOutputGain,
       "tnAmplifierPortDCMInPower": tnAmplifierPortDCMInPower,
       "tnAmplifierPortDCMOutPower": tnAmplifierPortDCMOutPower,
       "tnAmplifierPortActualTilt": tnAmplifierPortActualTilt,
       "tnAmplifierPortWtOcmMonitorPortOut": tnAmplifierPortWtOcmMonitorPortOut,
       "tnAmplifierPortOSCTxPowerIn": tnAmplifierPortOSCTxPowerIn,
       "tnAmplifierPortOSCTxPowerOut": tnAmplifierPortOSCTxPowerOut,
       "tnAmplifierPortTestingActive": tnAmplifierPortTestingActive,
       "tnAmplifierMeshPortInfoAttributeTotal": tnAmplifierMeshPortInfoAttributeTotal,
       "tnAmplifierMeshPortInfoTable": tnAmplifierMeshPortInfoTable,
       "tnAmplifierMeshPortInfoEntry": tnAmplifierMeshPortInfoEntry,
       "tnAmplifierMeshPortPowerOut": tnAmplifierMeshPortPowerOut,
       "tnAmplifierMeshPortSignalPowerOut": tnAmplifierMeshPortSignalPowerOut,
       "tnAmplifierMeshPortInputToOutputGain": tnAmplifierMeshPortInputToOutputGain,
       "tnAmplifierHybridPortInfoAttributeTotal": tnAmplifierHybridPortInfoAttributeTotal,
       "tnAmplifierHybridPortInfoTable": tnAmplifierHybridPortInfoTable,
       "tnAmplifierHybridPortInfoEntry": tnAmplifierHybridPortInfoEntry,
       "tnAmplifierHybridPortInternalAmpModuleTemperature": tnAmplifierHybridPortInternalAmpModuleTemperature,
       "tnAmplifierCardInfo": tnAmplifierCardInfo,
       "tnAmplifierCardInfoAttributeTotal": tnAmplifierCardInfoAttributeTotal,
       "tnAmplifierCardInfoTable": tnAmplifierCardInfoTable,
       "tnAmplifierCardInfoEntry": tnAmplifierCardInfoEntry,
       "tnAmplifierCardOAMPump1Temperature": tnAmplifierCardOAMPump1Temperature,
       "tnAmplifierCardOAMPump2Temperature": tnAmplifierCardOAMPump2Temperature,
       "tnAmplifierCardOAMPump3Temperature": tnAmplifierCardOAMPump3Temperature,
       "tnAmplifierCardOAMPump1Bias": tnAmplifierCardOAMPump1Bias,
       "tnAmplifierCardOAMPump2Bias": tnAmplifierCardOAMPump2Bias,
       "tnAmplifierCardOAMPump3Bias": tnAmplifierCardOAMPump3Bias,
       "tnAmplifierCardOptIntSpanLoss": tnAmplifierCardOptIntSpanLoss,
       "tnAmplifierCardOAMPump4Temperature": tnAmplifierCardOAMPump4Temperature,
       "tnAmplifierCardOAMPump5Temperature": tnAmplifierCardOAMPump5Temperature,
       "tnAmplifierCardOAMPump6Temperature": tnAmplifierCardOAMPump6Temperature,
       "tnAmplifierCardOAMPump4Bias": tnAmplifierCardOAMPump4Bias,
       "tnAmplifierCardOAMPump5Bias": tnAmplifierCardOAMPump5Bias,
       "tnAmplifierCardOAMPump6Bias": tnAmplifierCardOAMPump6Bias,
       "tnAmplifierMeshCardInfoAttributeTotal": tnAmplifierMeshCardInfoAttributeTotal,
       "tnAmplifierMeshCardInfoTable": tnAmplifierMeshCardInfoTable,
       "tnAmplifierMeshCardInfoEntry": tnAmplifierMeshCardInfoEntry,
       "tnAmplifierMeshCardInternalTemperature": tnAmplifierMeshCardInternalTemperature,
       "tnAmplifierMeshCardPowerIn": tnAmplifierMeshCardPowerIn,
       "tnAmplifierMeshCardPowerOut": tnAmplifierMeshCardPowerOut,
       "tnAmplifierMeshCardSignalPowerOut": tnAmplifierMeshCardSignalPowerOut,
       "tnAmplifierMeshCardInputToOutputGain": tnAmplifierMeshCardInputToOutputGain,
       "tnAmplifierMeshCardGainTilt": tnAmplifierMeshCardGainTilt,
       "tnAmplifierMeshCardActualTilt": tnAmplifierMeshCardActualTilt,
       "tnAmplifierHybridCardInfoAttributeTotal": tnAmplifierHybridCardInfoAttributeTotal,
       "tnAmplifierHybridCardInfoTable": tnAmplifierHybridCardInfoTable,
       "tnAmplifierHybridCardInfoEntry": tnAmplifierHybridCardInfoEntry,
       "tnAmplifierHybridCardOAMPump1Temperature": tnAmplifierHybridCardOAMPump1Temperature,
       "tnAmplifierHybridCardOAMPump2Temperature": tnAmplifierHybridCardOAMPump2Temperature,
       "tnAmplifierHybridCardOAMPump1Bias": tnAmplifierHybridCardOAMPump1Bias,
       "tnAmplifierHybridCardOAMPump2Bias": tnAmplifierHybridCardOAMPump2Bias,
       "tnAmplifierHybridCardOAMPump3Temperature": tnAmplifierHybridCardOAMPump3Temperature,
       "tnAmplifierHybridCardOAMPump4Temperature": tnAmplifierHybridCardOAMPump4Temperature,
       "tnAmplifierHybridCardOAMPump3Bias": tnAmplifierHybridCardOAMPump3Bias,
       "tnAmplifierHybridCardOAMPump4Bias": tnAmplifierHybridCardOAMPump4Bias,
       "tnAmplifierCardConfig": tnAmplifierCardConfig,
       "tnAmplifierCardConfigAttributeTotal": tnAmplifierCardConfigAttributeTotal,
       "tnAmplifierCardConfigTable": tnAmplifierCardConfigTable,
       "tnAmplifierCardConfigEntry": tnAmplifierCardConfigEntry,
       "tnAmplifierCardOptIntDetection": tnAmplifierCardOptIntDetection,
       "tnAmplifierCardOptIntBaseline": tnAmplifierCardOptIntBaseline,
       "tnAmplifierCardOptIntLossThreshold": tnAmplifierCardOptIntLossThreshold,
       "tnAmplifierCardOptIntPollPeriod": tnAmplifierCardOptIntPollPeriod,
       "tnAmplifierCardOptIntClearAlarm": tnAmplifierCardOptIntClearAlarm,
       "tnAmplifierCardAsonAddDropPlannedForOps": tnAmplifierCardAsonAddDropPlannedForOps,
       "tnAmplifierMeshCardConfigAttributeTotal": tnAmplifierMeshCardConfigAttributeTotal,
       "tnAmplifierMeshCardConfigTable": tnAmplifierMeshCardConfigTable,
       "tnAmplifierMeshCardConfigEntry": tnAmplifierMeshCardConfigEntry,
       "tnAmplifierMeshCardPowerGain": tnAmplifierMeshCardPowerGain,
       "tnAmplifierMeshCardPowerGainMin": tnAmplifierMeshCardPowerGainMin,
       "tnAmplifierMeshCardPowerGainMax": tnAmplifierMeshCardPowerGainMax,
       "tnAmplifierMeshCardTargetTilt": tnAmplifierMeshCardTargetTilt,
       "tnAmplifierMeshCardVoaSet": tnAmplifierMeshCardVoaSet,
       "tnAmplifierMeshCardCommonEgressPower": tnAmplifierMeshCardCommonEgressPower}
)
