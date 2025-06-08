# SNMP MIB module (EKT-CUSTOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/elkomtech_44730/EKT-CUSTOM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:06:13 2025
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

_Elkomtech_ObjectIdentity = ObjectIdentity
elkomtech = _Elkomtech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 0)
)
_ExtDevices_ObjectIdentity = ObjectIdentity
extDevices = _ExtDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10)
)
_FlairIndicator_ObjectIdentity = ObjectIdentity
flairIndicator = _FlairIndicator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1)
)
_FlairIndDgn_ObjectIdentity = ObjectIdentity
flairIndDgn = _FlairIndDgn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 1)
)


class _DgnFlairIndLinkState_Type(Integer32):
    """Custom type dgnFlairIndLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("lost", 1))
    )


_DgnFlairIndLinkState_Type.__name__ = "Integer32"
_DgnFlairIndLinkState_Object = MibScalar
dgnFlairIndLinkState = _DgnFlairIndLinkState_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 1, 1),
    _DgnFlairIndLinkState_Type()
)
dgnFlairIndLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnFlairIndLinkState.setStatus("current")
_FlairIndMea_ObjectIdentity = ObjectIdentity
flairIndMea = _FlairIndMea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 2)
)
_Msr0_Type = Integer32
_Msr0_Object = MibScalar
msr0 = _Msr0_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 2, 1),
    _Msr0_Type()
)
msr0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msr0.setStatus("current")
_Msr1_Type = Integer32
_Msr1_Object = MibScalar
msr1 = _Msr1_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 2, 2),
    _Msr1_Type()
)
msr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msr1.setStatus("current")
_Msr2_Type = Integer32
_Msr2_Object = MibScalar
msr2 = _Msr2_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 2, 3),
    _Msr2_Type()
)
msr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msr2.setStatus("current")
_Msr3_Type = Integer32
_Msr3_Object = MibScalar
msr3 = _Msr3_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 2, 4),
    _Msr3_Type()
)
msr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msr3.setStatus("current")
_Msr4_Type = Integer32
_Msr4_Object = MibScalar
msr4 = _Msr4_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 1, 2, 5),
    _Msr4_Type()
)
msr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msr4.setStatus("current")
_EnergyMeter_ObjectIdentity = ObjectIdentity
energyMeter = _EnergyMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6)
)
_Dgn_ObjectIdentity = ObjectIdentity
dgn = _Dgn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1)
)


class _DgnEnergyMeterLinkState_Type(Integer32):
    """Custom type dgnEnergyMeterLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("lost", 1))
    )


_DgnEnergyMeterLinkState_Type.__name__ = "Integer32"
_DgnEnergyMeterLinkState_Object = MibScalar
dgnEnergyMeterLinkState = _DgnEnergyMeterLinkState_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 1),
    _DgnEnergyMeterLinkState_Type()
)
dgnEnergyMeterLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnEnergyMeterLinkState.setStatus("current")


class _DgnPowerDown_Type(Integer32):
    """Custom type dgnPowerDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnPowerDown_Type.__name__ = "Integer32"
_DgnPowerDown_Object = MibScalar
dgnPowerDown = _DgnPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 2),
    _DgnPowerDown_Type()
)
dgnPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnPowerDown.setStatus("current")


class _DgnPowerUp_Type(Integer32):
    """Custom type dgnPowerUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnPowerUp_Type.__name__ = "Integer32"
_DgnPowerUp_Object = MibScalar
dgnPowerUp = _DgnPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 3),
    _DgnPowerUp_Type()
)
dgnPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnPowerUp.setStatus("current")


class _DgnEnergyMeterVL1Loss_Type(Integer32):
    """Custom type dgnEnergyMeterVL1Loss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnEnergyMeterVL1Loss_Type.__name__ = "Integer32"
_DgnEnergyMeterVL1Loss_Object = MibScalar
dgnEnergyMeterVL1Loss = _DgnEnergyMeterVL1Loss_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 4),
    _DgnEnergyMeterVL1Loss_Type()
)
dgnEnergyMeterVL1Loss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnEnergyMeterVL1Loss.setStatus("current")


class _DgnEnergyMeterVL2Loss_Type(Integer32):
    """Custom type dgnEnergyMeterVL2Loss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnEnergyMeterVL2Loss_Type.__name__ = "Integer32"
_DgnEnergyMeterVL2Loss_Object = MibScalar
dgnEnergyMeterVL2Loss = _DgnEnergyMeterVL2Loss_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 5),
    _DgnEnergyMeterVL2Loss_Type()
)
dgnEnergyMeterVL2Loss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnEnergyMeterVL2Loss.setStatus("current")


class _DgnEnergyMeterVL3Loss_Type(Integer32):
    """Custom type dgnEnergyMeterVL3Loss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnEnergyMeterVL3Loss_Type.__name__ = "Integer32"
_DgnEnergyMeterVL3Loss_Object = MibScalar
dgnEnergyMeterVL3Loss = _DgnEnergyMeterVL3Loss_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 6),
    _DgnEnergyMeterVL3Loss_Type()
)
dgnEnergyMeterVL3Loss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnEnergyMeterVL3Loss.setStatus("current")


class _DgnVL1Dropped_Type(Integer32):
    """Custom type dgnVL1Dropped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnVL1Dropped_Type.__name__ = "Integer32"
_DgnVL1Dropped_Object = MibScalar
dgnVL1Dropped = _DgnVL1Dropped_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 7),
    _DgnVL1Dropped_Type()
)
dgnVL1Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnVL1Dropped.setStatus("current")


class _DgnVL2Dropped_Type(Integer32):
    """Custom type dgnVL2Dropped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnVL2Dropped_Type.__name__ = "Integer32"
_DgnVL2Dropped_Object = MibScalar
dgnVL2Dropped = _DgnVL2Dropped_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 8),
    _DgnVL2Dropped_Type()
)
dgnVL2Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnVL2Dropped.setStatus("current")


class _DgnVL3Dropped_Type(Integer32):
    """Custom type dgnVL3Dropped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnVL3Dropped_Type.__name__ = "Integer32"
_DgnVL3Dropped_Object = MibScalar
dgnVL3Dropped = _DgnVL3Dropped_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 9),
    _DgnVL3Dropped_Type()
)
dgnVL3Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnVL3Dropped.setStatus("current")


class _DgnVL1Ovr_Type(Integer32):
    """Custom type dgnVL1Ovr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnVL1Ovr_Type.__name__ = "Integer32"
_DgnVL1Ovr_Object = MibScalar
dgnVL1Ovr = _DgnVL1Ovr_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 10),
    _DgnVL1Ovr_Type()
)
dgnVL1Ovr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnVL1Ovr.setStatus("current")


class _DgnVL2Ovr_Type(Integer32):
    """Custom type dgnVL2Ovr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnVL2Ovr_Type.__name__ = "Integer32"
_DgnVL2Ovr_Object = MibScalar
dgnVL2Ovr = _DgnVL2Ovr_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 11),
    _DgnVL2Ovr_Type()
)
dgnVL2Ovr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnVL2Ovr.setStatus("current")


class _DgnVL3Ovr_Type(Integer32):
    """Custom type dgnVL3Ovr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_DgnVL3Ovr_Type.__name__ = "Integer32"
_DgnVL3Ovr_Object = MibScalar
dgnVL3Ovr = _DgnVL3Ovr_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 1, 12),
    _DgnVL3Ovr_Type()
)
dgnVL3Ovr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgnVL3Ovr.setStatus("current")
_EnergyMeterMea_ObjectIdentity = ObjectIdentity
energyMeterMea = _EnergyMeterMea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2)
)
_MsrVL1_Type = OctetString
_MsrVL1_Object = MibScalar
msrVL1 = _MsrVL1_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 1),
    _MsrVL1_Type()
)
msrVL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrVL1.setStatus("current")
_MsrVL2_Type = OctetString
_MsrVL2_Object = MibScalar
msrVL2 = _MsrVL2_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 2),
    _MsrVL2_Type()
)
msrVL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrVL2.setStatus("current")
_MsrVL3_Type = OctetString
_MsrVL3_Object = MibScalar
msrVL3 = _MsrVL3_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 3),
    _MsrVL3_Type()
)
msrVL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrVL3.setStatus("current")
_MsrIL1_Type = OctetString
_MsrIL1_Object = MibScalar
msrIL1 = _MsrIL1_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 4),
    _MsrIL1_Type()
)
msrIL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrIL1.setStatus("current")
_MsrIL2_Type = OctetString
_MsrIL2_Object = MibScalar
msrIL2 = _MsrIL2_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 5),
    _MsrIL2_Type()
)
msrIL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrIL2.setStatus("current")
_MsrIL3_Type = OctetString
_MsrIL3_Object = MibScalar
msrIL3 = _MsrIL3_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 6),
    _MsrIL3_Type()
)
msrIL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrIL3.setStatus("current")
_MsrPtot_Type = OctetString
_MsrPtot_Object = MibScalar
msrPtot = _MsrPtot_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 7),
    _MsrPtot_Type()
)
msrPtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrPtot.setStatus("current")
_MsrQtot_Type = OctetString
_MsrQtot_Object = MibScalar
msrQtot = _MsrQtot_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 8),
    _MsrQtot_Type()
)
msrQtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrQtot.setStatus("current")
_MsrF_Type = OctetString
_MsrF_Object = MibScalar
msrF = _MsrF_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 2, 9),
    _MsrF_Type()
)
msrF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrF.setStatus("current")
_Ecv_ObjectIdentity = ObjectIdentity
ecv = _Ecv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 3)
)
_EcvEAi_Type = Integer32
_EcvEAi_Object = MibScalar
ecvEAi = _EcvEAi_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 3, 1),
    _EcvEAi_Type()
)
ecvEAi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecvEAi.setStatus("current")
_EcvEAe_Type = Integer32
_EcvEAe_Object = MibScalar
ecvEAe = _EcvEAe_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 3, 2),
    _EcvEAe_Type()
)
ecvEAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecvEAe.setStatus("current")
_EcvERQ1_Type = Integer32
_EcvERQ1_Object = MibScalar
ecvERQ1 = _EcvERQ1_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 3, 3),
    _EcvERQ1_Type()
)
ecvERQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecvERQ1.setStatus("current")
_EcvERQ2_Type = Integer32
_EcvERQ2_Object = MibScalar
ecvERQ2 = _EcvERQ2_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 3, 4),
    _EcvERQ2_Type()
)
ecvERQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecvERQ2.setStatus("current")
_EcvERQ3_Type = Integer32
_EcvERQ3_Object = MibScalar
ecvERQ3 = _EcvERQ3_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 3, 5),
    _EcvERQ3_Type()
)
ecvERQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecvERQ3.setStatus("current")
_EcvERQ4_Type = Integer32
_EcvERQ4_Object = MibScalar
ecvERQ4 = _EcvERQ4_Object(
    (1, 3, 6, 1, 4, 1, 44730, 10, 6, 3, 6),
    _EcvERQ4_Type()
)
ecvERQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecvERQ4.setStatus("current")

# Managed Objects groups


# Notification objects

flairCommStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 501)
)
flairCommStateTrap.setObjects(
    ("EKT-CUSTOM-MIB", "dgnFlairIndLinkState")
)
if mibBuilder.loadTexts:
    flairCommStateTrap.setStatus(
        "current"
    )

energyMeterCommState = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 502)
)
energyMeterCommState.setObjects(
    ("EKT-CUSTOM-MIB", "dgnEnergyMeterLinkState")
)
if mibBuilder.loadTexts:
    energyMeterCommState.setStatus(
        "current"
    )

energyMeterLossL1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 503)
)
energyMeterLossL1.setObjects(
    ("EKT-CUSTOM-MIB", "dgnEnergyMeterVL1Loss")
)
if mibBuilder.loadTexts:
    energyMeterLossL1.setStatus(
        "current"
    )

energyMeterLossL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 504)
)
energyMeterLossL2.setObjects(
    ("EKT-CUSTOM-MIB", "obj")
)
if mibBuilder.loadTexts:
    energyMeterLossL2.setStatus(
        "current"
    )

energyMeterLossL3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 505)
)
energyMeterLossL3.setObjects(
    ("EKT-CUSTOM-MIB", "dgnEnergyMeterVL3Loss")
)
if mibBuilder.loadTexts:
    energyMeterLossL3.setStatus(
        "current"
    )

energyMeterLowL1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 509)
)
energyMeterLowL1.setObjects(
    ("EKT-CUSTOM-MIB", "dgnVL1Dropped")
)
if mibBuilder.loadTexts:
    energyMeterLowL1.setStatus(
        "current"
    )

energyMeterLowL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 510)
)
energyMeterLowL2.setObjects(
    ("EKT-CUSTOM-MIB", "dgnEnergyMeterVL2Loss")
)
if mibBuilder.loadTexts:
    energyMeterLowL2.setStatus(
        "current"
    )

energyMeterLowL3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 511)
)
energyMeterLowL3.setObjects(
    ("EKT-CUSTOM-MIB", "dgnVL3Dropped")
)
if mibBuilder.loadTexts:
    energyMeterLowL3.setStatus(
        "current"
    )

energyMeterExceedL1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 512)
)
energyMeterExceedL1.setObjects(
    ("EKT-CUSTOM-MIB", "dgnVL1Ovr")
)
if mibBuilder.loadTexts:
    energyMeterExceedL1.setStatus(
        "current"
    )

energyMeterExceedL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 513)
)
energyMeterExceedL2.setObjects(
    ("EKT-CUSTOM-MIB", "dgnVL2Ovr")
)
if mibBuilder.loadTexts:
    energyMeterExceedL2.setStatus(
        "current"
    )

energyMeterExceedL3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 514)
)
energyMeterExceedL3.setObjects(
    ("EKT-CUSTOM-MIB", "dgnVL3Ovr")
)
if mibBuilder.loadTexts:
    energyMeterExceedL3.setStatus(
        "current"
    )

energyMeterPowerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 515)
)
energyMeterPowerUp.setObjects(
    ("EKT-CUSTOM-MIB", "dgnPowerUp")
)
if mibBuilder.loadTexts:
    energyMeterPowerUp.setStatus(
        "current"
    )

energyMeterPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 516)
)
energyMeterPowerDown.setObjects(
    ("EKT-CUSTOM-MIB", "dgnPowerDown")
)
if mibBuilder.loadTexts:
    energyMeterPowerDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKT-CUSTOM-MIB",
    **{"elkomtech": elkomtech,
       "traps": traps,
       "flairCommStateTrap": flairCommStateTrap,
       "energyMeterCommState": energyMeterCommState,
       "energyMeterLossL1": energyMeterLossL1,
       "energyMeterLossL2": energyMeterLossL2,
       "energyMeterLossL3": energyMeterLossL3,
       "energyMeterLowL1": energyMeterLowL1,
       "energyMeterLowL2": energyMeterLowL2,
       "energyMeterLowL3": energyMeterLowL3,
       "energyMeterExceedL1": energyMeterExceedL1,
       "energyMeterExceedL2": energyMeterExceedL2,
       "energyMeterExceedL3": energyMeterExceedL3,
       "energyMeterPowerUp": energyMeterPowerUp,
       "energyMeterPowerDown": energyMeterPowerDown,
       "extDevices": extDevices,
       "flairIndicator": flairIndicator,
       "flairIndDgn": flairIndDgn,
       "dgnFlairIndLinkState": dgnFlairIndLinkState,
       "flairIndMea": flairIndMea,
       "msr0": msr0,
       "msr1": msr1,
       "msr2": msr2,
       "msr3": msr3,
       "msr4": msr4,
       "energyMeter": energyMeter,
       "dgn": dgn,
       "dgnEnergyMeterLinkState": dgnEnergyMeterLinkState,
       "dgnPowerDown": dgnPowerDown,
       "dgnPowerUp": dgnPowerUp,
       "dgnEnergyMeterVL1Loss": dgnEnergyMeterVL1Loss,
       "dgnEnergyMeterVL2Loss": dgnEnergyMeterVL2Loss,
       "dgnEnergyMeterVL3Loss": dgnEnergyMeterVL3Loss,
       "dgnVL1Dropped": dgnVL1Dropped,
       "dgnVL2Dropped": dgnVL2Dropped,
       "dgnVL3Dropped": dgnVL3Dropped,
       "dgnVL1Ovr": dgnVL1Ovr,
       "dgnVL2Ovr": dgnVL2Ovr,
       "dgnVL3Ovr": dgnVL3Ovr,
       "energyMeterMea": energyMeterMea,
       "msrVL1": msrVL1,
       "msrVL2": msrVL2,
       "msrVL3": msrVL3,
       "msrIL1": msrIL1,
       "msrIL2": msrIL2,
       "msrIL3": msrIL3,
       "msrPtot": msrPtot,
       "msrQtot": msrQtot,
       "msrF": msrF,
       "ecv": ecv,
       "ecvEAi": ecvEAi,
       "ecvEAe": ecvEAe,
       "ecvERQ1": ecvERQ1,
       "ecvERQ2": ecvERQ2,
       "ecvERQ3": ecvERQ3,
       "ecvERQ4": ecvERQ4}
)
