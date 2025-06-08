# SNMP MIB module (RA-DMR-SNMP-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/radio_activity_37755/RA-DMR-SNMP-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:42 2025
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
 NotificationType,
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
    "NotificationType",
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

_Radio_activity_ObjectIdentity = ObjectIdentity
radio_activity = _Radio_activity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37755)
)
_Ra_Traps_ObjectIdentity = ObjectIdentity
ra_Traps = _Ra_Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37755, 2)
)
_Ra_Values_ObjectIdentity = ObjectIdentity
ra_Values = _Ra_Values_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37755, 11)
)
_Ra_TestoTensione_Type = OctetString
_Ra_TestoTensione_Object = MibScalar
ra_TestoTensione = _Ra_TestoTensione_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 1),
    _Ra_TestoTensione_Type()
)
ra_TestoTensione.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_TestoTensione.setStatus("mandatory")
_Ra_ValoreTimer_Type = TimeTicks
_Ra_ValoreTimer_Object = MibScalar
ra_ValoreTimer = _Ra_ValoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 2),
    _Ra_ValoreTimer_Type()
)
ra_ValoreTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_ValoreTimer.setStatus("mandatory")
_Ra_TestoTemperatura_Type = OctetString
_Ra_TestoTemperatura_Object = MibScalar
ra_TestoTemperatura = _Ra_TestoTemperatura_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 3),
    _Ra_TestoTemperatura_Type()
)
ra_TestoTemperatura.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_TestoTemperatura.setStatus("mandatory")


class _Ra_ValoreAllarme_Type(Integer32):
    """Custom type ra_ValoreAllarme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ra_ValoreAllarme_Type.__name__ = "Integer32"
_Ra_ValoreAllarme_Object = MibScalar
ra_ValoreAllarme = _Ra_ValoreAllarme_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 4),
    _Ra_ValoreAllarme_Type()
)
ra_ValoreAllarme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_ValoreAllarme.setStatus("mandatory")
_Ra_ValoreNumerico_Type = Integer32
_Ra_ValoreNumerico_Object = MibScalar
ra_ValoreNumerico = _Ra_ValoreNumerico_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 5),
    _Ra_ValoreNumerico_Type()
)
ra_ValoreNumerico.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_ValoreNumerico.setStatus("mandatory")
_Ra_CodiceApparato_Type = Integer32
_Ra_CodiceApparato_Object = MibScalar
ra_CodiceApparato = _Ra_CodiceApparato_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 6),
    _Ra_CodiceApparato_Type()
)
ra_CodiceApparato.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_CodiceApparato.setStatus("mandatory")
_Ra_CodiceImpianto_Type = Integer32
_Ra_CodiceImpianto_Object = MibScalar
ra_CodiceImpianto = _Ra_CodiceImpianto_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 7),
    _Ra_CodiceImpianto_Type()
)
ra_CodiceImpianto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_CodiceImpianto.setStatus("mandatory")
_Ra_BaseStationId_Type = Integer32
_Ra_BaseStationId_Object = MibScalar
ra_BaseStationId = _Ra_BaseStationId_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 8),
    _Ra_BaseStationId_Type()
)
ra_BaseStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_BaseStationId.setStatus("mandatory")


class _Ra_Severity_Type(Integer32):
    """Custom type ra_Severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Ra_Severity_Type.__name__ = "Integer32"
_Ra_Severity_Object = MibScalar
ra_Severity = _Ra_Severity_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 9),
    _Ra_Severity_Type()
)
ra_Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_Severity.setStatus("mandatory")
_Ra_ValoreTensione_Type = Integer32
_Ra_ValoreTensione_Object = MibScalar
ra_ValoreTensione = _Ra_ValoreTensione_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 10),
    _Ra_ValoreTensione_Type()
)
ra_ValoreTensione.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_ValoreTensione.setStatus("mandatory")
_Ra_ValoreTemperatura_Type = Integer32
_Ra_ValoreTemperatura_Object = MibScalar
ra_ValoreTemperatura = _Ra_ValoreTemperatura_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 11),
    _Ra_ValoreTemperatura_Type()
)
ra_ValoreTemperatura.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_ValoreTemperatura.setStatus("mandatory")
_Ra_ValSatelliteId_Type = Integer32
_Ra_ValSatelliteId_Object = MibScalar
ra_ValSatelliteId = _Ra_ValSatelliteId_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 12),
    _Ra_ValSatelliteId_Type()
)
ra_ValSatelliteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_ValSatelliteId.setStatus("mandatory")
_Ra_TxtSatelliteId_Type = OctetString
_Ra_TxtSatelliteId_Object = MibScalar
ra_TxtSatelliteId = _Ra_TxtSatelliteId_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 13),
    _Ra_TxtSatelliteId_Type()
)
ra_TxtSatelliteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_TxtSatelliteId.setStatus("mandatory")
_Ra_GenericText_Type = OctetString
_Ra_GenericText_Object = MibScalar
ra_GenericText = _Ra_GenericText_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 14),
    _Ra_GenericText_Type()
)
ra_GenericText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_GenericText.setStatus("mandatory")


class _Ra_ValDevice_Type(Integer32):
    """Custom type ra_ValDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Ra_ValDevice_Type.__name__ = "Integer32"
_Ra_ValDevice_Object = MibScalar
ra_ValDevice = _Ra_ValDevice_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 15),
    _Ra_ValDevice_Type()
)
ra_ValDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_ValDevice.setStatus("mandatory")
_Ra_AlarmId_Type = Integer32
_Ra_AlarmId_Object = MibScalar
ra_AlarmId = _Ra_AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 16),
    _Ra_AlarmId_Type()
)
ra_AlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_AlarmId.setStatus("mandatory")


class _Ra_CustLev_Type(Integer32):
    """Custom type ra_CustLev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ra_CustLev_Type.__name__ = "Integer32"
_Ra_CustLev_Object = MibScalar
ra_CustLev = _Ra_CustLev_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 17),
    _Ra_CustLev_Type()
)
ra_CustLev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_CustLev.setStatus("mandatory")
_Ra_RelatedText_Type = OctetString
_Ra_RelatedText_Object = MibScalar
ra_RelatedText = _Ra_RelatedText_Object(
    (1, 3, 6, 1, 4, 1, 37755, 11, 18),
    _Ra_RelatedText_Type()
)
ra_RelatedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ra_RelatedText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ra_Allarme1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 1)
)
ra_Allarme1.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme1.setStatus(
        ""
    )

ra_Allarme2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 2)
)
ra_Allarme2.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme2.setStatus(
        ""
    )

ra_Allarme3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 3)
)
ra_Allarme3.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTensione"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TestoTensione"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme3.setStatus(
        ""
    )

ra_Allarme4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 4)
)
ra_Allarme4.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTensione"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TestoTensione"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme4.setStatus(
        ""
    )

ra_Allarme5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 5)
)
ra_Allarme5.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme5.setStatus(
        ""
    )

ra_Allarme6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 6)
)
ra_Allarme6.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme6.setStatus(
        ""
    )

ra_Allarme7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 7)
)
ra_Allarme7.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTemperatura"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TestoTemperatura"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme7.setStatus(
        ""
    )

ra_Allarme8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 8)
)
ra_Allarme8.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTemperatura"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TestoTemperatura"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme8.setStatus(
        ""
    )

ra_Allarme9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 9)
)
ra_Allarme9.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme9.setStatus(
        ""
    )

ra_Allarme10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 10)
)
ra_Allarme10.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme10.setStatus(
        ""
    )

ra_Allarme11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 11)
)
ra_Allarme11.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TxtSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme11.setStatus(
        ""
    )

ra_Allarme12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 12)
)
ra_Allarme12.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TxtSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme12.setStatus(
        ""
    )

ra_Allarme13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 13)
)
ra_Allarme13.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TxtSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme13.setStatus(
        ""
    )

ra_Allarme14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 14)
)
ra_Allarme14.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme14.setStatus(
        ""
    )

ra_Allarme15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 15)
)
ra_Allarme15.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme15.setStatus(
        ""
    )

ra_Allarme16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 16)
)
ra_Allarme16.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TxtSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme16.setStatus(
        ""
    )

ra_Allarme17 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 17)
)
ra_Allarme17.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-TxtSatelliteId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme17.setStatus(
        ""
    )

ra_Allarme18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 18)
)
ra_Allarme18.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme18.setStatus(
        ""
    )

ra_Allarme19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 19)
)
ra_Allarme19.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme19.setStatus(
        ""
    )

ra_Allarme20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 20)
)
ra_Allarme20.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme20.setStatus(
        ""
    )

ra_Allarme21 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 21)
)
ra_Allarme21.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme21.setStatus(
        ""
    )

ra_Allarme22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 22)
)
ra_Allarme22.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme22.setStatus(
        ""
    )

ra_Allarme23 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 23)
)
ra_Allarme23.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme23.setStatus(
        ""
    )

ra_Allarme24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 24)
)
ra_Allarme24.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme24.setStatus(
        ""
    )

ra_Allarme25 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 25)
)
ra_Allarme25.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme25.setStatus(
        ""
    )

ra_Allarme26 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 26)
)
ra_Allarme26.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme26.setStatus(
        ""
    )

ra_Allarme27 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37755, 2, 0, 27)
)
ra_Allarme27.setObjects(
      *(("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreTimer"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceImpianto"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-BaseStationId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CodiceApparato"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-AlarmId"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValDevice"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-Severity"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-CustLev"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreAllarme"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-ValoreNumerico"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-GenericText"),
        ("RA-DMR-SNMP-TRAPS-MIB", "ra-RelatedText"))
)
if mibBuilder.loadTexts:
    ra_Allarme27.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RA-DMR-SNMP-TRAPS-MIB",
    **{"radio-activity": radio_activity,
       "ra-Traps": ra_Traps,
       "ra-Allarme1": ra_Allarme1,
       "ra-Allarme2": ra_Allarme2,
       "ra-Allarme3": ra_Allarme3,
       "ra-Allarme4": ra_Allarme4,
       "ra-Allarme5": ra_Allarme5,
       "ra-Allarme6": ra_Allarme6,
       "ra-Allarme7": ra_Allarme7,
       "ra-Allarme8": ra_Allarme8,
       "ra-Allarme9": ra_Allarme9,
       "ra-Allarme10": ra_Allarme10,
       "ra-Allarme11": ra_Allarme11,
       "ra-Allarme12": ra_Allarme12,
       "ra-Allarme13": ra_Allarme13,
       "ra-Allarme14": ra_Allarme14,
       "ra-Allarme15": ra_Allarme15,
       "ra-Allarme16": ra_Allarme16,
       "ra-Allarme17": ra_Allarme17,
       "ra-Allarme18": ra_Allarme18,
       "ra-Allarme19": ra_Allarme19,
       "ra-Allarme20": ra_Allarme20,
       "ra-Allarme21": ra_Allarme21,
       "ra-Allarme22": ra_Allarme22,
       "ra-Allarme23": ra_Allarme23,
       "ra-Allarme24": ra_Allarme24,
       "ra-Allarme25": ra_Allarme25,
       "ra-Allarme26": ra_Allarme26,
       "ra-Allarme27": ra_Allarme27,
       "ra-Values": ra_Values,
       "ra-TestoTensione": ra_TestoTensione,
       "ra-ValoreTimer": ra_ValoreTimer,
       "ra-TestoTemperatura": ra_TestoTemperatura,
       "ra-ValoreAllarme": ra_ValoreAllarme,
       "ra-ValoreNumerico": ra_ValoreNumerico,
       "ra-CodiceApparato": ra_CodiceApparato,
       "ra-CodiceImpianto": ra_CodiceImpianto,
       "ra-BaseStationId": ra_BaseStationId,
       "ra-Severity": ra_Severity,
       "ra-ValoreTensione": ra_ValoreTensione,
       "ra-ValoreTemperatura": ra_ValoreTemperatura,
       "ra-ValSatelliteId": ra_ValSatelliteId,
       "ra-TxtSatelliteId": ra_TxtSatelliteId,
       "ra-GenericText": ra_GenericText,
       "ra-ValDevice": ra_ValDevice,
       "ra-AlarmId": ra_AlarmId,
       "ra-CustLev": ra_CustLev,
       "ra-RelatedText": ra_RelatedText}
)
