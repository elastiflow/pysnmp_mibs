# SNMP MIB module (NEXUM-BDE-EXECUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aton_42755/NEXUM-BDE-EXECUTER-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:38:54 2025
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

atNexumBDEExecuter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1)
)
if mibBuilder.loadTexts:
    atNexumBDEExecuter.setRevisions(
        ("2016-05-17 14:23",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aton_ObjectIdentity = ObjectIdentity
aton = _Aton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755)
)
_ExTrap_ObjectIdentity = ObjectIdentity
exTrap = _ExTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0)
)
_ExStation_ObjectIdentity = ObjectIdentity
exStation = _ExStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1)
)
_StationFID_Type = OctetString
_StationFID_Object = MibScalar
stationFID = _StationFID_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 1),
    _StationFID_Type()
)
stationFID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationFID.setStatus("current")
_StationFKey_Type = OctetString
_StationFKey_Object = MibScalar
stationFKey = _StationFKey_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 2),
    _StationFKey_Type()
)
stationFKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationFKey.setStatus("current")
_StationBezeichnung_Type = OctetString
_StationBezeichnung_Object = MibScalar
stationBezeichnung = _StationBezeichnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 3),
    _StationBezeichnung_Type()
)
stationBezeichnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationBezeichnung.setStatus("current")
_StationIP_Type = OctetString
_StationIP_Object = MibScalar
stationIP = _StationIP_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 4),
    _StationIP_Type()
)
stationIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationIP.setStatus("current")
_StationNexumDB_Type = OctetString
_StationNexumDB_Object = MibScalar
stationNexumDB = _StationNexumDB_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 10),
    _StationNexumDB_Type()
)
stationNexumDB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationNexumDB.setStatus("current")
_StationDataDB_Type = OctetString
_StationDataDB_Object = MibScalar
stationDataDB = _StationDataDB_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 20),
    _StationDataDB_Type()
)
stationDataDB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationDataDB.setStatus("current")
_StationVorlaufDB_Type = OctetString
_StationVorlaufDB_Object = MibScalar
stationVorlaufDB = _StationVorlaufDB_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 30),
    _StationVorlaufDB_Type()
)
stationVorlaufDB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationVorlaufDB.setStatus("current")
_StationSequenzbruch_Type = OctetString
_StationSequenzbruch_Object = MibScalar
stationSequenzbruch = _StationSequenzbruch_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 40),
    _StationSequenzbruch_Type()
)
stationSequenzbruch.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationSequenzbruch.setStatus("current")
_StationVorlaufWarnung_Type = OctetString
_StationVorlaufWarnung_Object = MibScalar
stationVorlaufWarnung = _StationVorlaufWarnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 50),
    _StationVorlaufWarnung_Type()
)
stationVorlaufWarnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationVorlaufWarnung.setStatus("current")
_StationVorlaufAlarm_Type = OctetString
_StationVorlaufAlarm_Object = MibScalar
stationVorlaufAlarm = _StationVorlaufAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 60),
    _StationVorlaufAlarm_Type()
)
stationVorlaufAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationVorlaufAlarm.setStatus("current")
_StationWerkstueckUnbekannt_Type = OctetString
_StationWerkstueckUnbekannt_Object = MibScalar
stationWerkstueckUnbekannt = _StationWerkstueckUnbekannt_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 70),
    _StationWerkstueckUnbekannt_Type()
)
stationWerkstueckUnbekannt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationWerkstueckUnbekannt.setStatus("current")
_StationWerkstueckPruefziffer_Type = OctetString
_StationWerkstueckPruefziffer_Object = MibScalar
stationWerkstueckPruefziffer = _StationWerkstueckPruefziffer_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 1, 80),
    _StationWerkstueckPruefziffer_Type()
)
stationWerkstueckPruefziffer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stationWerkstueckPruefziffer.setStatus("current")
_ExIDSystem_ObjectIdentity = ObjectIdentity
exIDSystem = _ExIDSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 2)
)
_IdFID_Type = OctetString
_IdFID_Object = MibScalar
idFID = _IdFID_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 2, 1),
    _IdFID_Type()
)
idFID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idFID.setStatus("current")
_IdFKey_Type = OctetString
_IdFKey_Object = MibScalar
idFKey = _IdFKey_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 2, 2),
    _IdFKey_Type()
)
idFKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idFKey.setStatus("current")
_IdBezeichnung_Type = OctetString
_IdBezeichnung_Object = MibScalar
idBezeichnung = _IdBezeichnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 2, 3),
    _IdBezeichnung_Type()
)
idBezeichnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idBezeichnung.setStatus("current")
_IdIP_Type = OctetString
_IdIP_Object = MibScalar
idIP = _IdIP_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 2, 4),
    _IdIP_Type()
)
idIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idIP.setStatus("current")
_IdStatusOK_Type = OctetString
_IdStatusOK_Object = MibScalar
idStatusOK = _IdStatusOK_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 2, 10),
    _IdStatusOK_Type()
)
idStatusOK.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idStatusOK.setStatus("current")
_ExIDBTSystem_ObjectIdentity = ObjectIdentity
exIDBTSystem = _ExIDBTSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 3)
)
_IdbtFID_Type = OctetString
_IdbtFID_Object = MibScalar
idbtFID = _IdbtFID_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 3, 1),
    _IdbtFID_Type()
)
idbtFID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idbtFID.setStatus("current")
_IdbtFKEY_Type = OctetString
_IdbtFKEY_Object = MibScalar
idbtFKEY = _IdbtFKEY_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 3, 2),
    _IdbtFKEY_Type()
)
idbtFKEY.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idbtFKEY.setStatus("current")
_IdbtBezeichnung_Type = OctetString
_IdbtBezeichnung_Object = MibScalar
idbtBezeichnung = _IdbtBezeichnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 3, 3),
    _IdbtBezeichnung_Type()
)
idbtBezeichnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idbtBezeichnung.setStatus("current")
_IdbtIP_Type = OctetString
_IdbtIP_Object = MibScalar
idbtIP = _IdbtIP_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 3, 4),
    _IdbtIP_Type()
)
idbtIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idbtIP.setStatus("current")
_IdbtStatusOK_Type = OctetString
_IdbtStatusOK_Object = MibScalar
idbtStatusOK = _IdbtStatusOK_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 3, 10),
    _IdbtStatusOK_Type()
)
idbtStatusOK.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idbtStatusOK.setStatus("current")
_ExIDWKSystem_ObjectIdentity = ObjectIdentity
exIDWKSystem = _ExIDWKSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 4)
)
_IdwkFID_Type = OctetString
_IdwkFID_Object = MibScalar
idwkFID = _IdwkFID_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 4, 1),
    _IdwkFID_Type()
)
idwkFID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idwkFID.setStatus("current")
_IdwkFKEY_Type = OctetString
_IdwkFKEY_Object = MibScalar
idwkFKEY = _IdwkFKEY_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 4, 2),
    _IdwkFKEY_Type()
)
idwkFKEY.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idwkFKEY.setStatus("current")
_IdwkBezeichnung_Type = OctetString
_IdwkBezeichnung_Object = MibScalar
idwkBezeichnung = _IdwkBezeichnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 4, 3),
    _IdwkBezeichnung_Type()
)
idwkBezeichnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idwkBezeichnung.setStatus("current")
_IdwkIP_Type = OctetString
_IdwkIP_Object = MibScalar
idwkIP = _IdwkIP_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 4, 4),
    _IdwkIP_Type()
)
idwkIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idwkIP.setStatus("current")
_IdwkStatusOK_Type = OctetString
_IdwkStatusOK_Object = MibScalar
idwkStatusOK = _IdwkStatusOK_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 4, 10),
    _IdwkStatusOK_Type()
)
idwkStatusOK.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idwkStatusOK.setStatus("current")
_ExIDNKSystem_ObjectIdentity = ObjectIdentity
exIDNKSystem = _ExIDNKSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 5)
)
_IdnkFID_Type = OctetString
_IdnkFID_Object = MibScalar
idnkFID = _IdnkFID_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 5, 1),
    _IdnkFID_Type()
)
idnkFID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idnkFID.setStatus("current")
_IdnkFKEY_Type = OctetString
_IdnkFKEY_Object = MibScalar
idnkFKEY = _IdnkFKEY_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 5, 2),
    _IdnkFKEY_Type()
)
idnkFKEY.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idnkFKEY.setStatus("current")
_IdnkBezeichnung_Type = OctetString
_IdnkBezeichnung_Object = MibScalar
idnkBezeichnung = _IdnkBezeichnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 5, 3),
    _IdnkBezeichnung_Type()
)
idnkBezeichnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idnkBezeichnung.setStatus("current")
_IdnkIP_Type = OctetString
_IdnkIP_Object = MibScalar
idnkIP = _IdnkIP_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 5, 4),
    _IdnkIP_Type()
)
idnkIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idnkIP.setStatus("current")
_IdnkStatusOK_Type = OctetString
_IdnkStatusOK_Object = MibScalar
idnkStatusOK = _IdnkStatusOK_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 5, 10),
    _IdnkStatusOK_Type()
)
idnkStatusOK.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    idnkStatusOK.setStatus("current")
_ExMDSystem_ObjectIdentity = ObjectIdentity
exMDSystem = _ExMDSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10)
)
_MdFID_Type = OctetString
_MdFID_Object = MibScalar
mdFID = _MdFID_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 1),
    _MdFID_Type()
)
mdFID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdFID.setStatus("current")
_MdFKey_Type = OctetString
_MdFKey_Object = MibScalar
mdFKey = _MdFKey_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 2),
    _MdFKey_Type()
)
mdFKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdFKey.setStatus("current")
_MdBezeichnung_Type = OctetString
_MdBezeichnung_Object = MibScalar
mdBezeichnung = _MdBezeichnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 3),
    _MdBezeichnung_Type()
)
mdBezeichnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdBezeichnung.setStatus("current")
_MdIP_Type = OctetString
_MdIP_Object = MibScalar
mdIP = _MdIP_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 4),
    _MdIP_Type()
)
mdIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdIP.setStatus("current")
_MdVendor_Type = OctetString
_MdVendor_Object = MibScalar
mdVendor = _MdVendor_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 5),
    _MdVendor_Type()
)
mdVendor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdVendor.setStatus("current")
_MdStatusOK_Type = OctetString
_MdStatusOK_Object = MibScalar
mdStatusOK = _MdStatusOK_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 10),
    _MdStatusOK_Type()
)
mdStatusOK.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdStatusOK.setStatus("current")
_MdKeineVerbindung_Type = OctetString
_MdKeineVerbindung_Object = MibScalar
mdKeineVerbindung = _MdKeineVerbindung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 20),
    _MdKeineVerbindung_Type()
)
mdKeineVerbindung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdKeineVerbindung.setStatus("current")
_MdSchrauberstoerung_Type = OctetString
_MdSchrauberstoerung_Object = MibScalar
mdSchrauberstoerung = _MdSchrauberstoerung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 21),
    _MdSchrauberstoerung_Type()
)
mdSchrauberstoerung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdSchrauberstoerung.setStatus("current")
_MdXMLErrorCode_Type = OctetString
_MdXMLErrorCode_Object = MibScalar
mdXMLErrorCode = _MdXMLErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 30),
    _MdXMLErrorCode_Type()
)
mdXMLErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdXMLErrorCode.setStatus("current")
_MdErrorCode_Type = OctetString
_MdErrorCode_Object = MibScalar
mdErrorCode = _MdErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 10, 40),
    _MdErrorCode_Type()
)
mdErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mdErrorCode.setStatus("current")
_ExKanal_ObjectIdentity = ObjectIdentity
exKanal = _ExKanal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20)
)
_KanalFID_Type = OctetString
_KanalFID_Object = MibScalar
kanalFID = _KanalFID_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 1),
    _KanalFID_Type()
)
kanalFID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalFID.setStatus("current")
_KanalFKey_Type = OctetString
_KanalFKey_Object = MibScalar
kanalFKey = _KanalFKey_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 2),
    _KanalFKey_Type()
)
kanalFKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalFKey.setStatus("current")
_KanalBezeichnung_Type = OctetString
_KanalBezeichnung_Object = MibScalar
kanalBezeichnung = _KanalBezeichnung_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 3),
    _KanalBezeichnung_Type()
)
kanalBezeichnung.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalBezeichnung.setStatus("current")
_KanalStatusOK_Type = OctetString
_KanalStatusOK_Object = MibScalar
kanalStatusOK = _KanalStatusOK_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 10),
    _KanalStatusOK_Type()
)
kanalStatusOK.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalStatusOK.setStatus("current")
_KanalSteuerungInaktiv_Type = OctetString
_KanalSteuerungInaktiv_Object = MibScalar
kanalSteuerungInaktiv = _KanalSteuerungInaktiv_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 20),
    _KanalSteuerungInaktiv_Type()
)
kanalSteuerungInaktiv.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalSteuerungInaktiv.setStatus("current")
_KanalKanalInaktiv_Type = OctetString
_KanalKanalInaktiv_Object = MibScalar
kanalKanalInaktiv = _KanalKanalInaktiv_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 21),
    _KanalKanalInaktiv_Type()
)
kanalKanalInaktiv.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalKanalInaktiv.setStatus("current")
_KanalArbeitsplanInaktiv_Type = OctetString
_KanalArbeitsplanInaktiv_Object = MibScalar
kanalArbeitsplanInaktiv = _KanalArbeitsplanInaktiv_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 22),
    _KanalArbeitsplanInaktiv_Type()
)
kanalArbeitsplanInaktiv.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalArbeitsplanInaktiv.setStatus("current")
_KanalSchraubstelleAbgewaehlt_Type = OctetString
_KanalSchraubstelleAbgewaehlt_Object = MibScalar
kanalSchraubstelleAbgewaehlt = _KanalSchraubstelleAbgewaehlt_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 23),
    _KanalSchraubstelleAbgewaehlt_Type()
)
kanalSchraubstelleAbgewaehlt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalSchraubstelleAbgewaehlt.setStatus("current")
_KanalErrorCode_Type = OctetString
_KanalErrorCode_Object = MibScalar
kanalErrorCode = _KanalErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 42755, 1, 20, 40),
    _KanalErrorCode_Type()
)
kanalErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    kanalErrorCode.setStatus("current")
_ExCompliances_ObjectIdentity = ObjectIdentity
exCompliances = _ExCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 998)
)
_ExGroups_ObjectIdentity = ObjectIdentity
exGroups = _ExGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999)
)

# Managed Objects groups

exStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 2)
)
exStationGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "stationFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationNexumDB"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationDataDB"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationVorlaufDB"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationSequenzbruch"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationVorlaufWarnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationVorlaufAlarm"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationWerkstueckUnbekannt"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationWerkstueckPruefziffer"))
)
if mibBuilder.loadTexts:
    exStationGroup.setStatus("current")

exIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 3)
)
exIDGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "idBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idStatusOK"))
)
if mibBuilder.loadTexts:
    exIDGroup.setStatus("current")

exIDBTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 4)
)
exIDBTGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idbtFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtFKEY"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtStatusOK"))
)
if mibBuilder.loadTexts:
    exIDBTGroup.setStatus("current")

exIDWKGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 5)
)
exIDWKGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idwkFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkFKEY"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkStatusOK"))
)
if mibBuilder.loadTexts:
    exIDWKGroup.setStatus("current")

exIDNKGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 6)
)
exIDNKGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idnkFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkFKEY"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkStatusOK"))
)
if mibBuilder.loadTexts:
    exIDNKGroup.setStatus("current")

exMDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 7)
)
exMDGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "mdFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdVendor"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdStatusOK"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdKeineVerbindung"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdSchrauberstoerung"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdXMLErrorCode"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdErrorCode"))
)
if mibBuilder.loadTexts:
    exMDGroup.setStatus("current")

exKanalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 8)
)
exKanalGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "kanalFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalStatusOK"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalSteuerungInaktiv"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalKanalInaktiv"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalArbeitsplanInaktiv"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalSchraubstelleAbgewaehlt"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalErrorCode"))
)
if mibBuilder.loadTexts:
    exKanalGroup.setStatus("current")


# Notification objects

exGenerischeBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 1)
)
if mibBuilder.loadTexts:
    exGenerischeBenachrichtigung.setStatus(
        "current"
    )

exStationBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 2)
)
exStationBenachrichtigung.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "stationFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationNexumDB"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationDataDB"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationVorlaufDB"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationSequenzbruch"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationVorlaufWarnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationVorlaufAlarm"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationWerkstueckUnbekannt"),
        ("NEXUM-BDE-EXECUTER-MIB", "stationWerkstueckPruefziffer"))
)
if mibBuilder.loadTexts:
    exStationBenachrichtigung.setStatus(
        "current"
    )

exIDBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 3)
)
exIDBenachrichtigung.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "idBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idStatusOK"))
)
if mibBuilder.loadTexts:
    exIDBenachrichtigung.setStatus(
        "current"
    )

exIDBTBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 4)
)
exIDBTBenachrichtigung.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idbtFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idbtStatusOK"))
)
if mibBuilder.loadTexts:
    exIDBTBenachrichtigung.setStatus(
        "current"
    )

exIDWKBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 5)
)
exIDWKBenachrichtigung.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idwkFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idwkStatusOK"))
)
if mibBuilder.loadTexts:
    exIDWKBenachrichtigung.setStatus(
        "current"
    )

exIDNKBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 6)
)
exIDNKBenachrichtigung.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "idnkFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "idnkStatusOK"))
)
if mibBuilder.loadTexts:
    exIDNKBenachrichtigung.setStatus(
        "current"
    )

exMDBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 7)
)
exMDBenachrichtigung.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "mdFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdIP"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdVendor"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdStatusOK"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdKeineVerbindung"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdSchrauberstoerung"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdXMLErrorCode"),
        ("NEXUM-BDE-EXECUTER-MIB", "mdErrorCode"))
)
if mibBuilder.loadTexts:
    exMDBenachrichtigung.setStatus(
        "current"
    )

exKanalBenachrichtigung = NotificationType(
    (1, 3, 6, 1, 4, 1, 42755, 1, 0, 8)
)
exKanalBenachrichtigung.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "kanalFID"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalFKey"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalBezeichnung"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalStatusOK"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalSteuerungInaktiv"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalKanalInaktiv"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalArbeitsplanInaktiv"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalSchraubstelleAbgewaehlt"),
        ("NEXUM-BDE-EXECUTER-MIB", "kanalErrorCode"))
)
if mibBuilder.loadTexts:
    exKanalBenachrichtigung.setStatus(
        "current"
    )


# Notifications groups

exTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42755, 1, 999, 1)
)
exTrapGroup.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "exGenerischeBenachrichtigung"),
        ("NEXUM-BDE-EXECUTER-MIB", "exStationBenachrichtigung"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDBenachrichtigung"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDBTBenachrichtigung"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDWKBenachrichtigung"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDNKBenachrichtigung"),
        ("NEXUM-BDE-EXECUTER-MIB", "exMDBenachrichtigung"),
        ("NEXUM-BDE-EXECUTER-MIB", "exKanalBenachrichtigung"))
)
if mibBuilder.loadTexts:
    exTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

exFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 42755, 1, 998, 1)
)
exFullCompliance.setObjects(
      *(("NEXUM-BDE-EXECUTER-MIB", "exStationGroup"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDGroup"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDBTGroup"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDWKGroup"),
        ("NEXUM-BDE-EXECUTER-MIB", "exIDNKGroup"),
        ("NEXUM-BDE-EXECUTER-MIB", "exMDGroup"),
        ("NEXUM-BDE-EXECUTER-MIB", "exKanalGroup"),
        ("NEXUM-BDE-EXECUTER-MIB", "exTrapGroup"))
)
if mibBuilder.loadTexts:
    exFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEXUM-BDE-EXECUTER-MIB",
    **{"aton": aton,
       "atNexumBDEExecuter": atNexumBDEExecuter,
       "exTrap": exTrap,
       "exGenerischeBenachrichtigung": exGenerischeBenachrichtigung,
       "exStationBenachrichtigung": exStationBenachrichtigung,
       "exIDBenachrichtigung": exIDBenachrichtigung,
       "exIDBTBenachrichtigung": exIDBTBenachrichtigung,
       "exIDWKBenachrichtigung": exIDWKBenachrichtigung,
       "exIDNKBenachrichtigung": exIDNKBenachrichtigung,
       "exMDBenachrichtigung": exMDBenachrichtigung,
       "exKanalBenachrichtigung": exKanalBenachrichtigung,
       "exStation": exStation,
       "stationFID": stationFID,
       "stationFKey": stationFKey,
       "stationBezeichnung": stationBezeichnung,
       "stationIP": stationIP,
       "stationNexumDB": stationNexumDB,
       "stationDataDB": stationDataDB,
       "stationVorlaufDB": stationVorlaufDB,
       "stationSequenzbruch": stationSequenzbruch,
       "stationVorlaufWarnung": stationVorlaufWarnung,
       "stationVorlaufAlarm": stationVorlaufAlarm,
       "stationWerkstueckUnbekannt": stationWerkstueckUnbekannt,
       "stationWerkstueckPruefziffer": stationWerkstueckPruefziffer,
       "exIDSystem": exIDSystem,
       "idFID": idFID,
       "idFKey": idFKey,
       "idBezeichnung": idBezeichnung,
       "idIP": idIP,
       "idStatusOK": idStatusOK,
       "exIDBTSystem": exIDBTSystem,
       "idbtFID": idbtFID,
       "idbtFKEY": idbtFKEY,
       "idbtBezeichnung": idbtBezeichnung,
       "idbtIP": idbtIP,
       "idbtStatusOK": idbtStatusOK,
       "exIDWKSystem": exIDWKSystem,
       "idwkFID": idwkFID,
       "idwkFKEY": idwkFKEY,
       "idwkBezeichnung": idwkBezeichnung,
       "idwkIP": idwkIP,
       "idwkStatusOK": idwkStatusOK,
       "exIDNKSystem": exIDNKSystem,
       "idnkFID": idnkFID,
       "idnkFKEY": idnkFKEY,
       "idnkBezeichnung": idnkBezeichnung,
       "idnkIP": idnkIP,
       "idnkStatusOK": idnkStatusOK,
       "exMDSystem": exMDSystem,
       "mdFID": mdFID,
       "mdFKey": mdFKey,
       "mdBezeichnung": mdBezeichnung,
       "mdIP": mdIP,
       "mdVendor": mdVendor,
       "mdStatusOK": mdStatusOK,
       "mdKeineVerbindung": mdKeineVerbindung,
       "mdSchrauberstoerung": mdSchrauberstoerung,
       "mdXMLErrorCode": mdXMLErrorCode,
       "mdErrorCode": mdErrorCode,
       "exKanal": exKanal,
       "kanalFID": kanalFID,
       "kanalFKey": kanalFKey,
       "kanalBezeichnung": kanalBezeichnung,
       "kanalStatusOK": kanalStatusOK,
       "kanalSteuerungInaktiv": kanalSteuerungInaktiv,
       "kanalKanalInaktiv": kanalKanalInaktiv,
       "kanalArbeitsplanInaktiv": kanalArbeitsplanInaktiv,
       "kanalSchraubstelleAbgewaehlt": kanalSchraubstelleAbgewaehlt,
       "kanalErrorCode": kanalErrorCode,
       "exCompliances": exCompliances,
       "exFullCompliance": exFullCompliance,
       "exGroups": exGroups,
       "exTrapGroup": exTrapGroup,
       "exStationGroup": exStationGroup,
       "exIDGroup": exIDGroup,
       "exIDBTGroup": exIDBTGroup,
       "exIDWKGroup": exIDWKGroup,
       "exIDNKGroup": exIDNKGroup,
       "exMDGroup": exMDGroup,
       "exKanalGroup": exKanalGroup}
)
