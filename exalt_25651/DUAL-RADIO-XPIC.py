# SNMP MIB module (DUAL-RADIO-XPIC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exalt_25651/DUAL-RADIO-XPIC.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:22:49 2025
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

(radioMonitor,
 systemConfig) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "radioMonitor",
    "systemConfig")

(AlarmLevelT,
 DualRadioXpicEnableT) = mibBuilder.importSymbols(
    "ExaltComm",
    "AlarmLevelT",
    "DualRadioXpicEnableT")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DrXpicEnable_Type = DualRadioXpicEnableT
_DrXpicEnable_Object = MibScalar
drXpicEnable = _DrXpicEnable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 190),
    _DrXpicEnable_Type()
)
drXpicEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drXpicEnable.setStatus("current")
_DrXpicStatus_ObjectIdentity = ObjectIdentity
drXpicStatus = _DrXpicStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6)
)
_DrXpicLocalStatus_ObjectIdentity = ObjectIdentity
drXpicLocalStatus = _DrXpicLocalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1)
)
_DrXpicLocalipAddress_Type = DisplayString
_DrXpicLocalipAddress_Object = MibScalar
drXpicLocalipAddress = _DrXpicLocalipAddress_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 1),
    _DrXpicLocalipAddress_Type()
)
drXpicLocalipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalipAddress.setStatus("current")
_DrXpicLocalXpicId_Type = DisplayString
_DrXpicLocalXpicId_Object = MibScalar
drXpicLocalXpicId = _DrXpicLocalXpicId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 2),
    _DrXpicLocalXpicId_Type()
)
drXpicLocalXpicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalXpicId.setStatus("current")
_DrXpicLocalPolarity_Type = DisplayString
_DrXpicLocalPolarity_Object = MibScalar
drXpicLocalPolarity = _DrXpicLocalPolarity_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 3),
    _DrXpicLocalPolarity_Type()
)
drXpicLocalPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalPolarity.setStatus("current")
_DrXpicLocalXcon2Alm_Type = AlarmLevelT
_DrXpicLocalXcon2Alm_Object = MibScalar
drXpicLocalXcon2Alm = _DrXpicLocalXcon2Alm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 4),
    _DrXpicLocalXcon2Alm_Type()
)
drXpicLocalXcon2Alm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalXcon2Alm.setStatus("current")
_DrXpicLocalXcon1Alm_Type = AlarmLevelT
_DrXpicLocalXcon1Alm_Object = MibScalar
drXpicLocalXcon1Alm = _DrXpicLocalXcon1Alm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 5),
    _DrXpicLocalXcon1Alm_Type()
)
drXpicLocalXcon1Alm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalXcon1Alm.setStatus("current")
_DrXpicLocalSynthesizerAlm_Type = AlarmLevelT
_DrXpicLocalSynthesizerAlm_Object = MibScalar
drXpicLocalSynthesizerAlm = _DrXpicLocalSynthesizerAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 6),
    _DrXpicLocalSynthesizerAlm_Type()
)
drXpicLocalSynthesizerAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalSynthesizerAlm.setStatus("current")
_DrXpicLocalTxPwrDiffAlm_Type = AlarmLevelT
_DrXpicLocalTxPwrDiffAlm_Object = MibScalar
drXpicLocalTxPwrDiffAlm = _DrXpicLocalTxPwrDiffAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 7),
    _DrXpicLocalTxPwrDiffAlm_Type()
)
drXpicLocalTxPwrDiffAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalTxPwrDiffAlm.setStatus("current")
_DrXpicLocalRslDiffAlm_Type = AlarmLevelT
_DrXpicLocalRslDiffAlm_Object = MibScalar
drXpicLocalRslDiffAlm = _DrXpicLocalRslDiffAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 8),
    _DrXpicLocalRslDiffAlm_Type()
)
drXpicLocalRslDiffAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalRslDiffAlm.setStatus("current")
_DrXpicLocalPolarityDoubleAlm_Type = AlarmLevelT
_DrXpicLocalPolarityDoubleAlm_Object = MibScalar
drXpicLocalPolarityDoubleAlm = _DrXpicLocalPolarityDoubleAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 1, 9),
    _DrXpicLocalPolarityDoubleAlm_Type()
)
drXpicLocalPolarityDoubleAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicLocalPolarityDoubleAlm.setStatus("current")
_DrXpicPartnerStatus_ObjectIdentity = ObjectIdentity
drXpicPartnerStatus = _DrXpicPartnerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2)
)
_DrXpicPartneripAddress_Type = IpAddress
_DrXpicPartneripAddress_Object = MibScalar
drXpicPartneripAddress = _DrXpicPartneripAddress_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 1),
    _DrXpicPartneripAddress_Type()
)
drXpicPartneripAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartneripAddress.setStatus("current")
_DrXpicPartnerXpicId_Type = DisplayString
_DrXpicPartnerXpicId_Object = MibScalar
drXpicPartnerXpicId = _DrXpicPartnerXpicId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 2),
    _DrXpicPartnerXpicId_Type()
)
drXpicPartnerXpicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerXpicId.setStatus("current")
_DrXpicPartnerPolarity_Type = DisplayString
_DrXpicPartnerPolarity_Object = MibScalar
drXpicPartnerPolarity = _DrXpicPartnerPolarity_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 3),
    _DrXpicPartnerPolarity_Type()
)
drXpicPartnerPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerPolarity.setStatus("current")
_DrXpicPartnerXcon2Alm_Type = AlarmLevelT
_DrXpicPartnerXcon2Alm_Object = MibScalar
drXpicPartnerXcon2Alm = _DrXpicPartnerXcon2Alm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 4),
    _DrXpicPartnerXcon2Alm_Type()
)
drXpicPartnerXcon2Alm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerXcon2Alm.setStatus("current")
_DrXpicPartnerXcon1Alm_Type = AlarmLevelT
_DrXpicPartnerXcon1Alm_Object = MibScalar
drXpicPartnerXcon1Alm = _DrXpicPartnerXcon1Alm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 5),
    _DrXpicPartnerXcon1Alm_Type()
)
drXpicPartnerXcon1Alm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerXcon1Alm.setStatus("current")
_DrXpicPartnerSynthesizerAlm_Type = AlarmLevelT
_DrXpicPartnerSynthesizerAlm_Object = MibScalar
drXpicPartnerSynthesizerAlm = _DrXpicPartnerSynthesizerAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 6),
    _DrXpicPartnerSynthesizerAlm_Type()
)
drXpicPartnerSynthesizerAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerSynthesizerAlm.setStatus("current")
_DrXpicPartnerTxPwrDiffAlm_Type = AlarmLevelT
_DrXpicPartnerTxPwrDiffAlm_Object = MibScalar
drXpicPartnerTxPwrDiffAlm = _DrXpicPartnerTxPwrDiffAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 7),
    _DrXpicPartnerTxPwrDiffAlm_Type()
)
drXpicPartnerTxPwrDiffAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerTxPwrDiffAlm.setStatus("current")
_DrXpicPartnerRslDiffAlm_Type = AlarmLevelT
_DrXpicPartnerRslDiffAlm_Object = MibScalar
drXpicPartnerRslDiffAlm = _DrXpicPartnerRslDiffAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 8),
    _DrXpicPartnerRslDiffAlm_Type()
)
drXpicPartnerRslDiffAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerRslDiffAlm.setStatus("current")
_DrXpicPartnerPolarityDoubleAlm_Type = AlarmLevelT
_DrXpicPartnerPolarityDoubleAlm_Object = MibScalar
drXpicPartnerPolarityDoubleAlm = _DrXpicPartnerPolarityDoubleAlm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 6, 2, 9),
    _DrXpicPartnerPolarityDoubleAlm_Type()
)
drXpicPartnerPolarityDoubleAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drXpicPartnerPolarityDoubleAlm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DUAL-RADIO-XPIC",
    **{"drXpicEnable": drXpicEnable,
       "drXpicStatus": drXpicStatus,
       "drXpicLocalStatus": drXpicLocalStatus,
       "drXpicLocalipAddress": drXpicLocalipAddress,
       "drXpicLocalXpicId": drXpicLocalXpicId,
       "drXpicLocalPolarity": drXpicLocalPolarity,
       "drXpicLocalXcon2Alm": drXpicLocalXcon2Alm,
       "drXpicLocalXcon1Alm": drXpicLocalXcon1Alm,
       "drXpicLocalSynthesizerAlm": drXpicLocalSynthesizerAlm,
       "drXpicLocalTxPwrDiffAlm": drXpicLocalTxPwrDiffAlm,
       "drXpicLocalRslDiffAlm": drXpicLocalRslDiffAlm,
       "drXpicLocalPolarityDoubleAlm": drXpicLocalPolarityDoubleAlm,
       "drXpicPartnerStatus": drXpicPartnerStatus,
       "drXpicPartneripAddress": drXpicPartneripAddress,
       "drXpicPartnerXpicId": drXpicPartnerXpicId,
       "drXpicPartnerPolarity": drXpicPartnerPolarity,
       "drXpicPartnerXcon2Alm": drXpicPartnerXcon2Alm,
       "drXpicPartnerXcon1Alm": drXpicPartnerXcon1Alm,
       "drXpicPartnerSynthesizerAlm": drXpicPartnerSynthesizerAlm,
       "drXpicPartnerTxPwrDiffAlm": drXpicPartnerTxPwrDiffAlm,
       "drXpicPartnerRslDiffAlm": drXpicPartnerRslDiffAlm,
       "drXpicPartnerPolarityDoubleAlm": drXpicPartnerPolarityDoubleAlm}
)
